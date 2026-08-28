#!/usr/bin/env python3
"""
Survey instruments used in product discovery, scored correctly and reported with
their limits attached.

Every mode here produces stated-preference evidence (L2 on the discovery evidence
ladder). None of it settles a decision on its own. It tells you what to test.

Usage
-----
  # Kano. CSV: respondent_id, attribute, functional, dysfunctional  (values 1-5)
  #   1 = I like it, 2 = I expect it, 3 = I am neutral,
  #   4 = I can live with it, 5 = I dislike it
  python3 survey_analysis.py kano --csv kano.csv

  # Van Westendorp. CSV: respondent_id, too_cheap, cheap, expensive, too_expensive
  python3 survey_analysis.py vw --csv pricing.csv

  # MaxDiff counting analysis. CSV: respondent_id, task, item, choice (best/worst/shown)
  python3 survey_analysis.py maxdiff --csv maxdiff.csv

  # Sean Ellis product-market fit survey. CSV: respondent_id, answer[, segment]
  #   answer in {very, somewhat, not}
  python3 survey_analysis.py pmf --csv pmf.csv

  # Likert summary done properly (distribution and top-2-box, not a mean)
  python3 survey_analysis.py likert --csv likert.csv --value-col rating
"""

import argparse
import csv
import sys
from collections import defaultdict, Counter

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from _stats import wilson_ci  # noqa: E402


def read_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def bar(frac, width=24):
    return "#" * int(round(frac * width)) + "." * (width - int(round(frac * width)))


# --------------------------------------------------------------------------
# Kano
# --------------------------------------------------------------------------
# Standard Kano evaluation table. Rows = functional answer, cols = dysfunctional.
# A attractive, O one-dimensional, M must-be, I indifferent, R reverse, Q questionable
KANO = [
    ["Q", "A", "A", "A", "O"],
    ["R", "I", "I", "I", "M"],
    ["R", "I", "I", "I", "M"],
    ["R", "I", "I", "I", "M"],
    ["R", "R", "R", "R", "Q"],
]
KANO_NAME = {"A": "Attractive", "O": "One-dimensional", "M": "Must-be",
             "I": "Indifferent", "R": "Reverse", "Q": "Questionable"}


def cmd_kano(a):
    rows = read_csv(a.csv)
    per_attr = defaultdict(Counter)
    sat = defaultdict(lambda: [0, 0, 0])  # A+O, O+M, n
    for r in rows:
        f = int(float(r[a.functional_col]))
        d = int(float(r[a.dysfunctional_col]))
        if not (1 <= f <= 5 and 1 <= d <= 5):
            continue
        cat = KANO[f - 1][d - 1]
        attr = r[a.attribute_col]
        per_attr[attr][cat] += 1

    print()
    print("Kano categorisation")
    print("  n responses = %s, attributes = %d" % (format(len(rows), ","), len(per_attr)))
    print()
    print("  %-28s %5s %5s %5s %5s %5s %5s  %-16s %7s %7s"
          % ("attribute", "A", "O", "M", "I", "R", "Q", "winner", "CS+", "DS-"))
    results = []
    for attr, c in per_attr.items():
        n = sum(c.values())
        # Berger et al. (1993): both Questionable and Reverse are excluded from the
        # denominator. Leaving R in understates both coefficients, and it does so worst
        # on exactly the polarising attributes you would consult them about.
        valid = c["A"] + c["O"] + c["M"] + c["I"]
        if valid <= 0:
            continue
        # Conventional tie-break (Lee and Newcomb): M > O > A > I > R. Resolving ties
        # toward Attractive would flatter the result.
        order = {"M": 0, "O": 1, "A": 2, "I": 3, "R": 4}
        winner = min("AOMIR", key=lambda k: (-c[k], order[k]))
        cs = (c["A"] + c["O"]) / valid
        ds = -(c["O"] + c["M"]) / valid
        q_share = c["Q"] / n if n else 0.0
        results.append((attr, c, n, winner, cs, ds, q_share))
    flagged = []
    for attr, c, n, winner, cs, ds, q_share in sorted(results, key=lambda r: -r[4]):
        mark = "  <-- discard" if q_share > 0.10 else ""
        print("  %-28s %5d %5d %5d %5d %5d %5d  %-16s %+6.2f %+6.2f%s"
              % (attr[:28], c["A"], c["O"], c["M"], c["I"], c["R"], c["Q"],
                 KANO_NAME[winner], cs, ds, mark))
        if q_share > 0.10:
            flagged.append((attr, q_share))
    if flagged:
        print()
        print("  DISCARD, do not interpret: more than 10% Questionable means the question")
        print("  pair was misunderstood, so the category for that attribute is noise.")
        for attr, q in flagged:
            print("    %-30s %.0f%% questionable" % (attr[:30], 100 * q))

    print()
    print("  CS+ = satisfaction if present. DS- = dissatisfaction if absent.")
    print()
    print("  How to act on this:")
    print("   Must-be        build it, get no credit, lose everything if absent")
    print("   One-dimensional  more is better, invest proportionally")
    print("   Attractive     differentiator today, expected in two years")
    print("   Indifferent    do not build. This is where roadmaps go to die")
    print("   Reverse        some users actively do not want it. Segment before building")
    print()
    print("  Limits: stated preference (L2). Categories decay: today's attractive")
    print("  attribute becomes tomorrow's must-be. Rerun annually in a moving category.")
    print("  If any attribute has a high Questionable count, that question was")
    print("  misunderstood and its result should be discarded, not interpreted.")


# --------------------------------------------------------------------------
# Van Westendorp
# --------------------------------------------------------------------------


def _cross(prices, f1, f2):
    """First price where curve f1 crosses f2."""
    prev = None
    for p in prices:
        d = f1[p] - f2[p]
        if prev is not None and prev[1] * d <= 0 and prev[1] != d:
            # linear interpolation between prev price and p
            p0, d0 = prev
            if d - d0 == 0:
                return p
            return p0 + (p - p0) * (0 - d0) / (d - d0)
        prev = (p, d)
    return None


def cmd_vw(a):
    rows = read_csv(a.csv)
    tc, ch, ex, te = [], [], [], []
    for r in rows:
        try:
            tc.append(float(r["too_cheap"]))
            ch.append(float(r["cheap"]))
            ex.append(float(r["expensive"]))
            te.append(float(r["too_expensive"]))
        except (KeyError, ValueError):
            continue
    n = len(tc)
    if n == 0:
        sys.exit("no usable rows. Need columns: too_cheap, cheap, expensive, too_expensive")

    # basic consistency check: too_cheap <= cheap <= expensive <= too_expensive
    bad = sum(1 for i in range(n) if not (tc[i] <= ch[i] <= ex[i] <= te[i]))

    allp = sorted(set(tc + ch + ex + te))
    f_tc = {p: sum(1 for v in tc if v >= p) / n for p in allp}   # descending
    f_ch = {p: sum(1 for v in ch if v >= p) / n for p in allp}   # descending
    f_ex = {p: sum(1 for v in ex if v <= p) / n for p in allp}   # ascending
    f_te = {p: sum(1 for v in te if v <= p) / n for p in allp}   # ascending

    ipp = _cross(allp, f_ch, f_ex)
    opp = _cross(allp, f_tc, f_te)
    pmc = _cross(allp, f_tc, f_ex)
    pme = _cross(allp, f_ch, f_te)

    print()
    print("Van Westendorp price sensitivity meter")
    print("  n = %s" % format(n, ","))
    if bad:
        print("  WARNING: %d responses (%.1f%%) are internally inconsistent"
              % (bad, 100 * bad / n))
        print("  (prices not in ascending order). Standard practice is to exclude them.")
        print("  Rerun on cleaned data before using these numbers.")
    print()
    print("  Point of marginal cheapness (PMC)   %s" % _fmt(pmc))
    print("  Optimal price point (OPP)           %s" % _fmt(opp))
    print("  Indifference price point (IPP)      %s" % _fmt(ipp))
    print("  Point of marginal expensiveness     %s" % _fmt(pme))
    if pmc and pme:
        print()
        print("  Range of acceptable prices: %s to %s" % (_fmt(pmc), _fmt(pme)))
    print()
    print("  What this is: a map of price PERCEPTION from people who have not paid.")
    print("  What this is not: a price. Willingness to pay stated in a survey runs")
    print("  well above willingness to pay at a checkout, and the gap is not a")
    print("  constant you can subtract.")
    print()
    print("  Correct use: take two or three prices from this range and test them")
    print("  with commitment. A pricing page A/B, a pre-sale, or a paid pilot.")
    print("  Set the price from that, not from this.")


def _fmt(v):
    return "%.2f" % v if v is not None else "not reached in this data"


# --------------------------------------------------------------------------
# MaxDiff
# --------------------------------------------------------------------------


def cmd_maxdiff(a):
    rows = read_csv(a.csv)
    shown = Counter()
    best = Counter()
    worst = Counter()
    for r in rows:
        item = r[a.item_col]
        ch = (r[a.choice_col] or "").strip().lower()
        shown[item] += 1
        if ch == "best":
            best[item] += 1
        elif ch == "worst":
            worst[item] += 1
    if not shown:
        sys.exit("no rows read")

    print()
    print("MaxDiff, counting analysis")
    print("  respondents = %d, observations = %s"
          % (len({r[a.respondent_col] for r in rows}), format(len(rows), ",")))
    print()
    print("  %-34s %7s %7s %7s %9s" % ("item", "shown", "best", "worst", "score"))
    res = []
    for item in shown:
        s = (best[item] - worst[item]) / shown[item]
        res.append((item, shown[item], best[item], worst[item], s))
    for item, sh, b, w, s in sorted(res, key=lambda r: -r[4]):
        print("  %-34s %7d %7d %7d %+8.3f  %s"
              % (item[:34], sh, b, w, s, bar((s + 1) / 2, 20)))
    print()
    print("  Score = (best - worst) / times shown, range -1 to +1.")
    print("  Counting analysis is robust and enough for ranking. Hierarchical Bayes")
    print("  gives individual-level utilities and is worth it only when you need")
    print("  segment-level preference structure.")
    print()
    print("  MaxDiff beats rating scales because respondents must give something up.")
    print("  It still measures stated preference. It ranks; it does not size demand.")


# --------------------------------------------------------------------------
# PMF survey
# --------------------------------------------------------------------------


def cmd_pmf(a):
    rows = read_csv(a.csv)
    overall = Counter()
    by_seg = defaultdict(Counter)
    for r in rows:
        ans = (r[a.answer_col] or "").strip().lower()
        key = "very" if ans.startswith("very") else \
              "somewhat" if ans.startswith("somewhat") else \
              "not" if ans.startswith("not") else None
        if not key:
            continue
        overall[key] += 1
        if a.segment_col and r.get(a.segment_col):
            by_seg[r[a.segment_col]][key] += 1

    n = sum(overall.values())
    if not n:
        sys.exit("no usable answers. Expected values starting with very/somewhat/not")
    very = overall["very"] / n
    lo, hi = wilson_ci(overall["very"], n)

    print()
    print("Product-market fit survey (Sean Ellis)")
    print("  'How would you feel if you could no longer use this?'")
    print("  n = %s" % format(n, ","))
    print()
    for k, label in (("very", "Very disappointed"), ("somewhat", "Somewhat disappointed"),
                     ("not", "Not disappointed")):
        c = overall[k]
        print("  %-24s %6s  %5.1f%%  %s" % (label, format(c, ","), 100 * c / n,
                                            bar(c / n)))
    print()
    print("  Very disappointed: %.1f%%  95%% CI [%.1f%%, %.1f%%]"
          % (100 * very, 100 * lo, 100 * hi))
    if n < 40:
        print("  n is small. The interval above is wide for a reason; do not report")
        print("  the point estimate on its own.")

    if by_seg:
        print()
        print("  By segment")
        print("  %-24s %8s %10s %s" % ("segment", "n", "very", ""))
        for seg, c in sorted(by_seg.items(),
                             key=lambda kv: -(kv[1]["very"] / max(1, sum(kv[1].values())))):
            sn = sum(c.values())
            print("  %-24s %8s %9.1f%%  %s" % (seg, format(sn, ","),
                                               100 * c["very"] / sn, bar(c["very"] / sn)))

    print()
    print("  Reading this honestly:")
    print("   - Valid only among users who have experienced the core value at least")
    print("     twice. Surveying everyone dilutes it into meaninglessness.")
    print("   - The 40% threshold is a widely used heuristic from Sean Ellis's work,")
    print("     not a law and not a statistical result.")
    print("   - The signal is the 'very disappointed' SEGMENT, not the percentage.")
    print("     Find out who they are and what they have in common. That is your")
    print("     market. Build for them.")
    print("   - Retention curve first. If the curve does not flatten, this survey")
    print("     cannot rescue the conclusion.")


# --------------------------------------------------------------------------
# Likert
# --------------------------------------------------------------------------


def cmd_likert(a):
    rows = read_csv(a.csv)
    vals = []
    for r in rows:
        try:
            vals.append(int(float(r[a.value_col])))
        except (KeyError, ValueError):
            continue
    n = len(vals)
    if not n:
        sys.exit("no usable values")
    c = Counter(vals)
    lo_v, hi_v = min(c), max(c)
    top2 = sum(c[v] for v in (hi_v, hi_v - 1))
    bot2 = sum(c[v] for v in (lo_v, lo_v + 1))
    tl, th = wilson_ci(top2, n)

    print()
    print("Likert distribution  (n = %s)" % format(n, ","))
    for v in range(lo_v, hi_v + 1):
        print("  %2d  %6s  %5.1f%%  %s" % (v, format(c[v], ","), 100 * c[v] / n,
                                           bar(c[v] / n)))
    print()
    print("  top-2-box   %5.1f%%  95%% CI [%.1f%%, %.1f%%]"
          % (100 * top2 / n, 100 * tl, 100 * th))
    print("  bottom-2-box %4.1f%%" % (100 * bot2 / n))
    print("  median      %d" % sorted(vals)[n // 2])
    print()
    print("  The mean of a Likert scale is not reported here on purpose. The")
    print("  distance between 'agree' and 'strongly agree' is not the same as")
    print("  between 'neutral' and 'agree', so the arithmetic mean has no defined")
    print("  meaning. Report the distribution, the median, and top-2-box.")
    if c[hi_v] + c[lo_v] > 0.6 * n:
        print()
        print("  This distribution is bimodal. Two groups feel opposite ways. Any")
        print("  single summary statistic describes neither of them. Segment.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    k = sub.add_parser("kano")
    k.add_argument("--csv", required=True)
    k.add_argument("--attribute-col", default="attribute")
    k.add_argument("--functional-col", default="functional")
    k.add_argument("--dysfunctional-col", default="dysfunctional")
    k.set_defaults(func=cmd_kano)

    v = sub.add_parser("vw")
    v.add_argument("--csv", required=True)
    v.set_defaults(func=cmd_vw)

    m = sub.add_parser("maxdiff")
    m.add_argument("--csv", required=True)
    m.add_argument("--respondent-col", default="respondent_id")
    m.add_argument("--item-col", default="item")
    m.add_argument("--choice-col", default="choice")
    m.set_defaults(func=cmd_maxdiff)

    p = sub.add_parser("pmf")
    p.add_argument("--csv", required=True)
    p.add_argument("--answer-col", default="answer")
    p.add_argument("--segment-col", default="segment")
    p.set_defaults(func=cmd_pmf)

    l = sub.add_parser("likert")
    l.add_argument("--csv", required=True)
    l.add_argument("--value-col", default="value")
    l.set_defaults(func=cmd_likert)

    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
