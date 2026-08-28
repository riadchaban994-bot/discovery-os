#!/usr/bin/env python3
"""
Measure qualitative saturation and inter-coder agreement.

Saturation is the only defensible answer to "how many interviews is enough".
It is measured from the data, not felt. This computes new codes per source and
draws the curve, per segment.

Usage
-----
  # Saturation curve. CSV: source_id, code[, segment]   (one row per code applied)
  python3 qual_saturation.py saturation --csv codes.csv

  # Per segment
  python3 qual_saturation.py saturation --csv codes.csv --segment-col segment

  # Inter-coder agreement. CSV: segment_id, coder_a, coder_b
  python3 qual_saturation.py kappa --csv doublecoded.csv

  # Code frequency by source count (the only count that may be reported)
  python3 qual_saturation.py frequency --csv codes.csv
"""

import argparse
import csv
import sys
from collections import defaultdict, Counter, OrderedDict


def read_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def bar(n, scale=1, ch="#"):
    return ch * int(round(n * scale))


def saturation_for(pairs):
    """pairs: ordered list of (source_id, set_of_codes). Returns per-source rows."""
    seen = set()
    out = []
    for i, (src, codes) in enumerate(pairs, 1):
        new = codes - seen
        seen |= codes
        out.append((i, src, len(codes), len(new), len(seen)))
    return out


def report_curve(label, pairs, threshold):
    rows = saturation_for(pairs)
    total = rows[-1][4] if rows else 0
    print()
    print("Saturation: %s" % label)
    print("  %-4s %-18s %8s %8s %10s   %s"
          % ("#", "source", "codes", "new", "cumulative", "new codes"))
    for i, src, ncodes, new, cum in rows:
        print("  %-4d %-18s %8d %8d %10d   %s"
              % (i, str(src)[:18], ncodes, new, cum, bar(new)))
    print("  total unique codes: %d across %d sources" % (total, len(rows)))

    tail = [r[3] for r in rows[-threshold:]] if len(rows) >= threshold else None
    print()
    if tail is None:
        print("  Not enough sources to judge saturation. Need at least %d." % threshold)
    elif all(t == 0 for t in tail):
        print("  SATURATED for this segment: the last %d sources added no new codes."
              % threshold)
        print("  Additional interviews in this segment will mostly confirm. Move to a")
        print("  different segment, or to a different question.")
    else:
        recent = sum(r[3] for r in rows[-threshold:])
        print("  NOT SATURATED: the last %d sources added %d new codes."
              % (threshold, recent))
        remaining = "a few more" if recent <= 2 else "several more"
        print("  Keep going. Estimate: %s sources in this segment." % remaining)
        print("  Reporting prevalence or completeness from this corpus would overstate")
        print("  what you know.")

    if len(rows) >= 4:
        first_half = sum(r[3] for r in rows[:len(rows) // 2])
        second_half = sum(r[3] for r in rows[len(rows) // 2:])
        if second_half > first_half:
            print()
            print("  WARNING: the second half of the corpus produced MORE new codes than")
            print("  the first. That is the signature of a heterogeneous sample. You are")
            print("  probably looking at two or more segments. Split them and rerun.")


def cmd_saturation(a):
    rows = read_csv(a.csv)
    order = OrderedDict()
    seg_of = {}
    for r in rows:
        src = r[a.source_col]
        order.setdefault(src, set()).add(r[a.code_col])
        if a.segment_col and r.get(a.segment_col):
            seg_of[src] = r[a.segment_col]

    if a.segment_col and seg_of:
        groups = defaultdict(list)
        for src, codes in order.items():
            groups[seg_of.get(src, "(unassigned)")].append((src, codes))
        for seg in sorted(groups):
            report_curve("%s = %s" % (a.segment_col, seg), groups[seg], a.threshold)
        print()
        print("Saturation is per segment. A flat curve in one segment says nothing")
        print("about another. Never claim saturation across a pooled sample.")
    else:
        report_curve("all sources", list(order.items()), a.threshold)


def cmd_frequency(a):
    rows = read_csv(a.csv)
    sources = set()
    by_code = defaultdict(set)
    for r in rows:
        sources.add(r[a.source_col])
        by_code[r[a.code_col]].add(r[a.source_col])
    n = len(sources)
    print()
    print("Code frequency by SOURCE count (n = %d sources)" % n)
    print("  One source mentioning something six times is one source.")
    print()
    print("  %-38s %10s   %s" % ("code", "sources", ""))
    for code, srcs in sorted(by_code.items(), key=lambda kv: -len(kv[1])):
        c = len(srcs)
        print("  %-38s %6d/%-4d %s" % (code[:38], c, n, bar(c / n, 24)))
    print()
    if n < 30:
        print("  n < 30: report these as counts out of %d. Do not convert to" % n)
        print("  percentages. 'Seven of eleven' is a finding. '64%' is an overclaim.")
    weak = [c for c, s in by_code.items() if len(s) < 3]
    if weak:
        print()
        print("  %d codes appear in fewer than 3 sources. These are signals to look"
              % len(weak))
        print("  into, not themes. A theme needs at least three independent sources.")


def cmd_kappa(a):
    rows = read_csv(a.csv)
    pairs = [(r[a.coder_a_col], r[a.coder_b_col]) for r in rows
             if r.get(a.coder_a_col) and r.get(a.coder_b_col)]
    n = len(pairs)
    if not n:
        sys.exit("no usable double-coded rows")
    agree = sum(1 for x, y in pairs if x == y)
    po = agree / n
    ca = Counter(x for x, _ in pairs)
    cb = Counter(y for _, y in pairs)
    labels = set(ca) | set(cb)
    pe = sum((ca[k] / n) * (cb[k] / n) for k in labels)
    kappa = (po - pe) / (1 - pe) if pe < 1 else 1.0

    print()
    print("Inter-coder agreement (Cohen's kappa)")
    print("  double-coded segments  %d" % n)
    print("  distinct labels        %d" % len(labels))
    print("  observed agreement     %.4f" % po)
    print("  chance agreement       %.4f" % pe)
    print("  kappa                  %.4f" % kappa)
    print()
    if kappa >= 0.8:
        print("  Strong. The codebook is unambiguous enough to apply at scale.")
    elif kappa >= 0.6:
        print("  Workable. Resolve the disagreements by tightening code definitions,")
        print("  then recode the affected segments. Do not average the two codings.")
    else:
        print("  TOO LOW. The codebook is ambiguous. Do not code the rest of the corpus")
        print("  yet. Sit with the disagreements, rewrite the inclusion and exclusion")
        print("  rules, and re-test on a fresh sample.")

    print()
    print("  Most frequent disagreements:")
    dis = Counter((x, y) for x, y in pairs if x != y)
    for (x, y), c in dis.most_common(8):
        print("    %-24s vs %-24s  %d" % (x[:24], y[:24], c))
    if not dis:
        print("    none")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("saturation")
    s.add_argument("--csv", required=True)
    s.add_argument("--source-col", default="source_id")
    s.add_argument("--code-col", default="code")
    s.add_argument("--segment-col")
    s.add_argument("--threshold", type=int, default=2,
                   help="consecutive sources with zero new codes to call saturation")
    s.set_defaults(func=cmd_saturation)

    f = sub.add_parser("frequency")
    f.add_argument("--csv", required=True)
    f.add_argument("--source-col", default="source_id")
    f.add_argument("--code-col", default="code")
    f.set_defaults(func=cmd_frequency)

    k = sub.add_parser("kappa")
    k.add_argument("--csv", required=True)
    k.add_argument("--coder-a-col", default="coder_a")
    k.add_argument("--coder-b-col", default="coder_b")
    k.set_defaults(func=cmd_kappa)

    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
