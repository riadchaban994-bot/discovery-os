#!/usr/bin/env python3
"""
Behavioural analysis for discovery: funnels, cohort retention, survival, and the
Simpson's paradox check that most funnel analysis skips.

Pure standard library. No pandas required.

Usage
-----
  # Funnel. CSV needs user_id and step columns.
  python3 cohorts_funnels.py funnel --csv events.csv \
      --steps view signup activate purchase

  # Funnel split by a segment column, with a Simpson's paradox check
  python3 cohorts_funnels.py funnel --csv events.csv \
      --steps view signup activate --segment platform

  # Cohort retention. CSV needs user_id, cohort, period.
  python3 cohorts_funnels.py cohort --csv activity.csv --max-periods 12

  # Kaplan-Meier survival. CSV needs duration and event (1 = churned, 0 = still active).
  python3 cohorts_funnels.py survival --csv churn.csv

  # Simpson's paradox check from an aggregate table.
  # CSV needs segment, group, converted, total.
  python3 cohorts_funnels.py simpson --csv breakdown.csv
"""

import argparse
import csv
import math
import sys
from collections import defaultdict, OrderedDict

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from _stats import wilson_ci  # noqa: E402


def read_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def bar(frac, width=28):
    n = int(round(frac * width))
    return "#" * n + "." * (width - n)


# --------------------------------------------------------------------------


def funnel_for(rows, steps, user_col, step_col):
    reached = defaultdict(set)
    for r in rows:
        s = r[step_col]
        if s in steps:
            reached[s].add(r[user_col])
    # enforce ordering: a user counts at step k only if they reached every prior step
    counts, carried = [], None
    for s in steps:
        users = reached.get(s, set())
        carried = users if carried is None else (carried & users)
        counts.append(len(carried))
    return counts


def cmd_funnel(a):
    rows = read_csv(a.csv)
    steps = a.steps

    def report(label, rows_subset):
        counts = funnel_for(rows_subset, steps, a.user_col, a.step_col)
        top = counts[0] if counts and counts[0] else 0
        print()
        print("Funnel: %s" % label)
        print("  %-18s %10s %10s %10s   %s"
              % ("step", "users", "step conv", "from top", ""))
        prev = None
        worst = (None, 1.0)
        for s, c in zip(steps, counts):
            step_conv = (c / prev) if prev else 1.0
            from_top = (c / top) if top else 0.0
            print("  %-18s %10s %9.1f%% %9.1f%%   %s"
                  % (s, format(c, ","), 100 * step_conv, 100 * from_top, bar(from_top)))
            if prev is not None and step_conv < worst[1]:
                worst = (s, step_conv)
            prev = c
        if top:
            lo, hi = wilson_ci(counts[-1], top)
            print("  overall %.2f%%  95%% CI [%.2f%%, %.2f%%]  n=%s"
                  % (100 * counts[-1] / top, 100 * lo, 100 * hi, format(top, ",")))
        if worst[0]:
            print("  biggest single drop: into '%s' (%.1f%% pass)"
                  % (worst[0], 100 * worst[1]))
        return counts

    overall = report("all users", rows)

    if a.segment:
        segments = sorted({r[a.segment] for r in rows if r.get(a.segment)})
        seg_results = {}
        for seg in segments:
            subset = [r for r in rows if r.get(a.segment) == seg]
            seg_results[seg] = report("%s = %s" % (a.segment, seg), subset)

        print()
        print("Segment comparison, end-to-end conversion")
        print("  %-20s %10s %10s" % (a.segment, "n at top", "overall"))
        for seg, counts in sorted(seg_results.items(),
                                  key=lambda kv: -(kv[1][-1] / kv[1][0]) if kv[1][0] else 0):
            top = counts[0]
            if top:
                print("  %-20s %10s %9.2f%%" % (seg, format(top, ","),
                                                100 * counts[-1] / top))
        print()
        print("Read the mix, not just the rates. If the aggregate funnel moved and")
        print("no segment did, the mix changed. Check segment shares over time before")
        print("attributing an aggregate movement to behaviour.")


# --------------------------------------------------------------------------


def cmd_cohort(a):
    rows = read_csv(a.csv)
    cohorts = defaultdict(lambda: defaultdict(set))
    sizes = defaultdict(set)
    for r in rows:
        c = r[a.cohort_col]
        p = int(float(r[a.period_col]))
        u = r[a.user_col]
        cohorts[c][p].add(u)
        if p == 0:
            sizes[c].add(u)
    for c in cohorts:
        if not sizes[c]:
            sizes[c] = cohorts[c][min(cohorts[c])]

    names = sorted(cohorts)
    maxp = min(a.max_periods, max(max(v) for v in cohorts.values()) + 1)

    print()
    print("Cohort retention")
    header = "  %-14s %8s" % ("cohort", "size")
    header += "".join("%8s" % ("P%d" % p) for p in range(maxp))
    print(header)
    matrix = OrderedDict()
    for c in names:
        base = len(sizes[c])
        if not base:
            continue
        line = "  %-14s %8s" % (c, format(base, ","))
        vals = []
        for p in range(maxp):
            n = len(cohorts[c].get(p, set()))
            v = n / base
            vals.append(v if n or p == 0 else None)
            line += "%7.1f%%" % (100 * v) if n or p == 0 else "%8s" % "-"
        matrix[c] = vals
        print(line)

    # average curve, only over cohorts that have data at that period
    print()
    print("Average curve (cohorts with data at each period)")
    avg = []
    for p in range(maxp):
        vals = [m[p] for m in matrix.values() if len(m) > p and m[p] is not None]
        if vals:
            mean = sum(vals) / len(vals)
            avg.append(mean)
            print("  P%-3d %6.1f%%  %s  (n=%d cohorts)" % (p, 100 * mean, bar(mean), len(vals)))

    print()
    print("Flattening check")
    if len(avg) >= 4:
        tail = avg[-3:]
        drops = [tail[i] - tail[i + 1] for i in range(len(tail) - 1)]
        avg_drop = sum(drops) / len(drops)
        print("  last three periods: %s" % "  ".join("%.1f%%" % (100 * v) for v in tail))
        print("  average period-over-period drop in the tail: %.2f pp" % (100 * avg_drop))
        if avg_drop < 0.01 and tail[-1] > 0.05:
            print("  The curve is flattening above zero. That is the shape you want:")
            print("  a stable base of users who keep coming back.")
        elif tail[-1] <= 0.02:
            print("  The curve is approaching zero. No retained base yet. Nothing about")
            print("  acquisition or pricing matters until this changes.")
        else:
            print("  Still declining. Extend the window before concluding. A curve that")
            print("  has not flattened is not evidence of fit.")
    else:
        print("  Not enough periods to judge. Need at least 4.")
    print()
    print("Define the retention event as the core value action, not as a login.")
    print("Login-based retention curves flatter every product ever measured.")


# --------------------------------------------------------------------------


def cmd_survival(a):
    rows = read_csv(a.csv)
    data = []
    for r in rows:
        data.append((float(r[a.duration_col]), int(float(r[a.event_col]))))
    data.sort()
    n = len(data)
    at_risk = n
    s = 1.0
    print()
    print("Kaplan-Meier survival")
    print("  n = %s, events (churned) = %d, censored (still active) = %d"
          % (format(n, ","), sum(e for _, e in data), sum(1 - e for _, e in data)))
    print()
    print("  %-10s %10s %8s %10s   %s" % ("t", "at risk", "events", "S(t)", ""))
    i = 0
    median = None
    rows_out = []
    while i < n:
        t = data[i][0]
        j = i
        d = 0
        while j < n and data[j][0] == t:
            d += data[j][1]
            j += 1
        censored = (j - i) - d
        if d > 0 and at_risk > 0:
            s *= (1.0 - d / at_risk)
        rows_out.append((t, at_risk, d, s))
        if median is None and s <= 0.5:
            median = t
        at_risk -= (j - i)
        i = j
    step = max(1, len(rows_out) // 25)
    for k, (t, ar, d, sv) in enumerate(rows_out):
        if k % step == 0 or d > 0:
            print("  %-10.4g %10s %8d %9.3f   %s" % (t, format(ar, ","), d, sv, bar(sv)))
    print()
    if median is not None:
        print("  median survival time = %.4g" % median)
    else:
        print("  median survival not reached within the observation window")
    print()
    print("  Censoring matters. Users who have not churned yet are not survivors,")
    print("  they are unfinished. A raw churn rate that ignores them overstates")
    print("  retention for recent cohorts and understates it for old ones.")


# --------------------------------------------------------------------------


def cmd_simpson(a):
    rows = read_csv(a.csv)
    agg = defaultdict(lambda: [0, 0])
    seg = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    for r in rows:
        g = r[a.group_col]
        s = r[a.segment_col]
        c, t = int(float(r[a.converted_col])), int(float(r[a.total_col]))
        agg[g][0] += c
        agg[g][1] += t
        seg[s][g][0] += c
        seg[s][g][1] += t

    groups = sorted(agg)
    if len(groups) != 2:
        sys.exit("simpson check expects exactly 2 groups, found: %s" % ", ".join(groups))
    g1, g2 = groups

    print()
    print("Aggregate")
    for g in groups:
        c, t = agg[g]
        print("  %-14s %8s / %-8s = %.4f" % (g, format(c, ","), format(t, ","), c / t))
    agg_diff = agg[g2][0] / agg[g2][1] - agg[g1][0] / agg[g1][1]
    print("  aggregate difference (%s - %s) = %+.4f" % (g2, g1, agg_diff))

    print()
    print("By segment")
    signs = []
    for s in sorted(seg):
        if g1 not in seg[s] or g2 not in seg[s]:
            print("  %-14s incomplete, skipped" % s)
            continue
        c1, t1 = seg[s][g1]
        c2, t2 = seg[s][g2]
        if not t1 or not t2:
            continue
        d = c2 / t2 - c1 / t1
        signs.append(d)
        print("  %-14s %s %.4f (n=%s)   %s %.4f (n=%s)   diff %+.4f"
              % (s, g1, c1 / t1, format(t1, ","), g2, c2 / t2, format(t2, ","), d))

    print()
    if signs and all(d > 0 for d in signs) and agg_diff < 0:
        print("  SIMPSON'S PARADOX. Every segment favours %s, the aggregate favours %s."
              % (g2, g1))
    elif signs and all(d < 0 for d in signs) and agg_diff > 0:
        print("  SIMPSON'S PARADOX. Every segment favours %s, the aggregate favours %s."
              % (g1, g2))
    elif signs and len({d > 0 for d in signs}) > 1:
        print("  Segments disagree in direction. The aggregate hides opposite effects.")
        print("  Report by segment. The average is not a description of anyone.")
    else:
        print("  No reversal detected. Aggregate and segments point the same way.")

    print()
    print("Segment mix")
    for g in groups:
        tot = agg[g][1]
        parts = []
        for s in sorted(seg):
            if g in seg[s]:
                parts.append("%s %.1f%%" % (s, 100 * seg[s][g][1] / tot))
        print("  %-14s %s" % (g, "   ".join(parts)))
    print()
    print("  If the mix differs between groups, the aggregate comparison is")
    print("  comparing populations, not treatments.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("funnel")
    f.add_argument("--csv", required=True)
    f.add_argument("--steps", nargs="+", required=True)
    f.add_argument("--user-col", default="user_id")
    f.add_argument("--step-col", default="step")
    f.add_argument("--segment")
    f.set_defaults(func=cmd_funnel)

    c = sub.add_parser("cohort")
    c.add_argument("--csv", required=True)
    c.add_argument("--user-col", default="user_id")
    c.add_argument("--cohort-col", default="cohort")
    c.add_argument("--period-col", default="period")
    c.add_argument("--max-periods", type=int, default=12)
    c.set_defaults(func=cmd_cohort)

    s = sub.add_parser("survival")
    s.add_argument("--csv", required=True)
    s.add_argument("--duration-col", default="duration")
    s.add_argument("--event-col", default="event")
    s.set_defaults(func=cmd_survival)

    p = sub.add_parser("simpson")
    p.add_argument("--csv", required=True)
    p.add_argument("--segment-col", default="segment")
    p.add_argument("--group-col", default="group")
    p.add_argument("--converted-col", default="converted")
    p.add_argument("--total-col", default="total")
    p.set_defaults(func=cmd_simpson)

    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
