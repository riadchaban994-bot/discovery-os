#!/usr/bin/env python3
"""Check a tracking plan before it is built or handed over.

    python3 validate_plan.py plan.json [--platform ga4]

Every check here exists because the corresponding mistake shipped at least once. The
checks are grouped by how they fail: BLOCKER means the plan will produce wrong data or
cannot be built, WARN means a reader will be misled or an engineer will have to guess.
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

LIMITS = {
    "amplitude": {"event_name_len": 1024, "params_per_event": 1000, "event_dimensions": 2000,
                  "user_dimensions": 1000, "metrics": 2000, "user_prop_name": 1024,
                  "user_prop_value": 1024, "reserved": {"revenue", "$identify"}, "prefixes": ("[Amplitude]",)},
    "mixpanel": {"event_name_len": 255, "params_per_event": 255, "event_dimensions": 2000,
                 "user_dimensions": 1000, "metrics": 2000, "user_prop_name": 255,
                 "user_prop_value": 255, "reserved": set(), "prefixes": ("mp_", "$")},
    "posthog": {"event_name_len": 200, "params_per_event": 500, "event_dimensions": 2000,
                "user_dimensions": 1000, "metrics": 2000, "user_prop_name": 200,
                "user_prop_value": 1000, "reserved": set(), "prefixes": ("$",)},
    "segment": {"event_name_len": 255, "params_per_event": 500, "event_dimensions": 2000,
                "user_dimensions": 1000, "metrics": 2000, "user_prop_name": 255,
                "user_prop_value": 1000, "reserved": set(), "prefixes": ()},
    "ga4": {"event_name_len": 40, "params_per_event": 25, "event_dimensions": 50,
            "user_dimensions": 25, "metrics": 50, "user_prop_name": 24, "user_prop_value": 36,
            "reserved": {"first_open", "first_visit", "session_start", "screen_view", "page_view",
                         "user_engagement", "app_update", "app_remove", "os_update", "app_install",
                         "in_app_purchase", "ad_click", "ad_impression", "notification_receive",
                         "notification_open"},
            "prefixes": ("firebase_", "google_", "ga_")},
    "generic": {"event_name_len": 64, "params_per_event": 100, "event_dimensions": 500,
                "user_dimensions": 100, "metrics": 500, "user_prop_name": 64, "user_prop_value": 255,
                "reserved": set(), "prefixes": ()},
}
GRADES = {"OBSERVED", "PARTIAL", "INFERRED", "UNVERIFIABLE", "SDK"}
# words that look like event names but are not, so the dangling-reference check stays quiet
KNOWN_NON_EVENTS = {"not_referenced", "no_screen", "to_confirm", "user_id", "session_id",
                    "first_open", "session_start", "screen_view", "page_view", "user_engagement"}
REQ = {"required", "conditional", "optional", "see owner", "n/a - SDK"}


def check(plan_path, platform="ga4"):
    base = Path(plan_path).resolve().parent
    d = json.loads(Path(plan_path).read_text())
    meta = d.get("meta", {})
    if platform is None:
        platform = str(meta.get("destination", "ga4")).lower().strip()
        if platform not in LIMITS:
            platform = "generic"
    L = dict(LIMITS.get(platform, LIMITS["generic"]))
    # The plan may state its own account-level quotas. The builder already honours these,
    # so the validator must too, or the two disagree about the same file.
    for k, v in (meta.get("limits") or {}).items():
        if k in L and isinstance(v, int):
            L[k] = v
    ev = d.get("events", [])
    packs = d.get("packs", [])
    blockers, warns = [], []

    if not ev:
        return ["plan has no events"], []

    # --- names and duplicates
    seen = set()
    for e in ev:
        n = e.get("name", "")
        if n in seen:
            blockers.append(f"duplicate event name: {n}")
        seen.add(n)
        if e.get("type") == "auto":
            continue
        if len(n) > L["event_name_len"]:
            blockers.append(f"event name over {L['event_name_len']} chars: {n}")
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", n):
            blockers.append(f"event name has illegal characters: {n}")
        if n.startswith(L["prefixes"]):
            blockers.append(f"event name uses a reserved prefix: {n}")
        if n in L["reserved"]:
            blockers.append(f"event name collides with a reserved/auto event: {n}")

    # --- evidence and required grading, the honesty checks
    for e in ev:
        g = e.get("evidence")
        if not g:
            warns.append(f"no evidence grade: {e['name']} (a reader cannot tell fact from proposal)")
        elif g not in GRADES:
            warns.append(f"unknown evidence grade '{g}': {e['name']}")
        if not e.get("source"):
            warns.append(f"no source (FE/BE/FE + BE/SDK): {e['name']}")
        if e.get("phase") == "P1" and not e.get("why_p1"):
            warns.append(f"Phase 1 event with no stated reason for being in Phase 1: {e['name']}")

    pack_params = {p["id"]: {q["name"] for q in p.get("params", [])} for p in packs}
    for p in packs:
        for q in p.get("params", []):
            if q.get("req") and q["req"] not in REQ:
                warns.append(f"unknown req value '{q['req']}': {p['id']}.{q['name']}")
            elif not q.get("req"):
                warns.append(f"no required/conditional/optional marker: {p['id']}.{q['name']}")

    # --- attachment integrity: named params must exist, extras must not repeat packs
    for e in ev:
        attached = set()
        for spec in e.get("packs", []):
            pid = str(spec).split(" ")[0].split("(")[0].strip()
            if pid and pid not in pack_params:
                blockers.append(f"{e['name']}: attaches pack '{pid}', which is not defined. "
                                f"The event would carry none of its parameters and nothing else would warn you.")
                continue
            attached |= pack_params.get(pid, set())
            m = re.search(r"\(([^)]*)\)", str(spec))
            if m and pid in pack_params:
                for tok in m.group(1).split(","):
                    nm = tok.strip().split("=")[0].split(" ")[0].strip()
                    if re.match(r"^[a-z][a-z0-9_]+$", nm) and nm not in pack_params[pid]:
                        blockers.append(f"{e['name']}: '{nm}' is not a parameter of pack {pid}")
        for x in e.get("extra_params", []):
            nm = str(x).split(":")[0].split("/")[0].strip()
            if nm in attached:
                warns.append(f"{e['name']}: extra param '{nm}' repeats an attached pack parameter")

    # --- parameter budget on the heaviest events
    for e in ev:
        total = 0
        for spec in e.get("packs", []):
            pid = str(spec).split(" ")[0].split("(")[0].strip()
            m = re.search(r"\(([^)]*)\)", str(spec))
            if pid.upper() in ("ITM", "ITEMS"):
                total += 1
                continue
            if m and pid in pack_params:
                total += sum(1 for t in m.group(1).split(",")
                             if t.strip().split("=")[0].split(" ")[0].strip() in pack_params[pid])
            else:
                total += len(pack_params.get(pid, ()))
        total += len(e.get("extra_params", []))
        if total > L["params_per_event"]:
            blockers.append(f"{e['name']}: {total} parameters, over the {L['params_per_event']} cap "
                            f"(the platform will silently drop the excess)")
        elif total == L["params_per_event"]:
            warns.append(f"{e['name']}: exactly at the {L['params_per_event']} parameter cap, no headroom")

    # --- quotas
    dims = sum(1 for p in packs for q in p.get("params", []) if q.get("register"))
    mets = sum(1 for p in packs for q in p.get("params", []) if q.get("register_metric"))
    ups = d.get("user_properties", [])
    if dims > L["event_dimensions"]:
        blockers.append(f"{dims} registered dimensions, over the {L['event_dimensions']} quota")
    if len(ups) > L["user_dimensions"]:
        blockers.append(f"{len(ups)} user properties, over the {L['user_dimensions']} quota")
    if mets > L["metrics"]:
        blockers.append(f"{mets} custom metrics, over the {L['metrics']} quota")
    for u in ups:
        if len(u.get("name", "")) > L["user_prop_name"]:
            blockers.append(f"user property name over {L['user_prop_name']} chars: {u['name']}")
        for v in str(u.get("values", "")).split("|"):
            if len(v.strip()) > L["user_prop_value"]:
                warns.append(f"user property value may truncate: {u['name']} -> {v.strip()[:40]}")

    # --- the spreadsheet formula trap: invisible in source, renders as an error
    def walk(o, path=""):
        if isinstance(o, dict):
            for k, v in o.items():
                walk(v, f"{path}.{k}")
        elif isinstance(o, list):
            for i, v in enumerate(o):
                walk(v, f"{path}[{i}]")
        elif isinstance(o, str) and o.lstrip()[:1] in ("=", "+", "-", "@") and len(o.strip()) > 1:
            blockers.append(f"value starts with '{o.lstrip()[0]}' so a spreadsheet parses it as a "
                            f"formula and shows an error: {path} = {o[:40]!r}")
    walk(d)

    # --- cross-tab references that break after merges
    names = {e["name"] for e in ev}
    for j in d.get("journeys", []):
        for step in j.get("events", []):
            b = re.split(r"[ (|]", str(step).strip())[0]
            if b and b not in names:
                blockers.append(f"journey '{j['name']}' references an event that does not exist: {b}")
    ke = {k["name"] for k in d.get("key_events", [])}
    flagged = {e["name"] for e in ev if e.get("key_event")}
    if ke and ke != flagged:
        warns.append(f"key event list and key_event flags disagree: only in list {sorted(ke - flagged)}, "
                     f"only flagged {sorted(flagged - ke)}")

    # --- Gate 1.1: an event name mentioned anywhere must still exist.
    # Merges are what break this: a tab keeps pointing at a name that was consolidated away.
    for section, field in (("gaps_closed", "fix"), ("open_questions", None),
                           ("roadmap", None), ("cuts", None), ("journey_map", None),
                           ("audiences", None), ("key_events", "name")):
        for item in d.get(section, []) or []:
            if isinstance(item, dict):
                text = " ".join(str(v) for v in item.values())
            else:
                text = " ".join(str(v) for v in item)
            for cand in re.findall(r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+){1,4}\b", text):
                if cand in names or cand in KNOWN_NON_EVENTS:
                    continue
                # only flag things that look like event names: verb-ish endings
                if re.search(r"_(viewed|selected|started|completed|failed|submitted|"
                             r"changed|applied|added|removed|opened|closed|shown|"
                             r"delivered|cancelled|refused|granted|renewed|expired|"
                             r"purchased|blocked|abandoned|resumed|set|sent|tapped)$", cand):
                    warns.append(f"{section} mentions '{cand}', which is not an event in this plan. "
                                 f"If it was merged away, update the wording.")

    # --- Gate 1.3: numbers stated in prose must match the data.
    # A summary that says 52 while the tab holds 50 destroys trust in every other number.
    counts = {
        "events": len(ev),
        "P1": sum(1 for e in ev if e.get("phase") == "P1"),
        "packs": len(packs),
        "user_properties": len(ups),
    }
    for e_grade in ("OBSERVED", "PARTIAL", "INFERRED", "UNVERIFIABLE"):
        counts[e_grade] = sum(1 for e in ev if e.get("evidence") == e_grade)
    prose = " ".join(str(v) for k, v in (d.get("meta") or {}).items() if isinstance(v, str))
    for row in (d.get("roadmap") or []):
        prose += " " + " ".join(str(x) for x in row)
    for label, pat in (("events to build in Phase 1", r"(\d+)\s+events?\s+to\s+build"),
                       ("Phase 1 count", r"[Bb]uild\s+(\d+)\s+events?")):
        for m in re.finditer(pat, prose):
            if int(m.group(1)) != counts["P1"]:
                blockers.append(f"prose says {m.group(1)} {label} but {counts['P1']} events are "
                                f"marked P1. A count that disagrees with the data poisons every "
                                f"other number in the document.")
    for grade in ("OBSERVED", "PARTIAL", "INFERRED", "UNVERIFIABLE"):
        for m in re.finditer(rf"(\d+)\s+{grade}", prose):
            if int(m.group(1)) != counts[grade]:
                blockers.append(f"prose says {m.group(1)} {grade} but the data has {counts[grade]}.")

    # --- the honesty check. This skill's whole premise is evidence, so a plan with no
    # observed events must not be able to present itself as though it had any.
    observed = counts["OBSERVED"]
    if observed == 0 and any(e.get("type") != "auto" for e in ev):
        warns.append("no event is graded OBSERVED, so nothing in this plan was seen in a running "
                     "app. That is legitimate when there is no build to walk, but the plan must "
                     "say so plainly on tab 1 and in the first open question, or it presents "
                     "itself as evidence-based when it is not.")

    # --- screenshots
    folder = base / "tracking_plan_screens"
    cites = {m.upper() for e in ev for m in re.findall(r"SCR-\d+", str(e.get("screens", "") or ""), re.I)}
    if cites and not folder.is_dir():
        blockers.append(f"{len(cites)} events cite screenshots but there is no tracking_plan_screens/ "
                        f"folder beside the plan. The workbook would build with dead evidence links "
                        f"and no warning. An OBSERVED row with no evidence attached is an INFERRED "
                        f"row wearing a better label.")
    if folder.is_dir():
        files = {f.name.split("_")[0].upper() for f in folder.iterdir() if f.suffix.lower() == ".png"}
        refs = {m.upper() for e in ev for m in re.findall(r"SCR-\d+", str(e.get("screens", "") or ""), re.I)}
        for r in sorted(refs - files):
            blockers.append(f"screen referenced but no file exists: {r}")
        for u in sorted(files - refs):
            warns.append(f"screenshot never referenced by any event: {u}")
    for e in ev:
        if not e.get("screens"):
            warns.append(f"no screen reference and no stated reason: {e['name']}")

    # --- style
    for m in re.finditer("[\u2014\u2013]", json.dumps(d, ensure_ascii=False)):
        warns.append("plan contains an em or en dash; house style is to use commas or full stops")
        break
    return blockers, warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--platform", default=None, choices=sorted(LIMITS),
                    help="destination. Defaults to meta.destination in the plan, then ga4.")
    a = ap.parse_args()
    b, w = check(a.plan, a.platform)
    dest = a.platform or str(json.loads(Path(a.plan).read_text()).get("meta", {}).get("destination", "ga4"))
    d = json.loads(Path(a.plan).read_text())
    ev = d.get("events", [])
    print(f"destination: {dest}")
    print(f"{len(ev)} events | phases {dict(Counter(e.get('phase', '-') for e in ev))} "
          f"| evidence {dict(Counter(e.get('evidence', '-') for e in ev))}")
    print()
    if b:
        print(f"BLOCKERS ({len(b)}) - fix before building:")
        for x in b:
            print("  x", x)
        print()
    if w:
        print(f"WARNINGS ({len(w)}) - a reader will be misled or an engineer will guess:")
        for x in w[:40]:
            print("  !", x)
        if len(w) > 40:
            print(f"  ... and {len(w) - 40} more")
        print()
    if not b and not w:
        print("Clean. Now render the workbook and LOOK at it: source checks cannot see a")
        print("clipped column, a mis-stamped header, or a cell rendering as a formula error.")
    sys.exit(1 if b else 0)


if __name__ == "__main__":
    main()
