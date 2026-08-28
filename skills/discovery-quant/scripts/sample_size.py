#!/usr/bin/env python3
"""
Sample size, power, and minimum detectable effect for discovery experiments.

Answers the question you must answer before running anything: is this test even
possible with the traffic we have, in the time we have?

Usage
-----
  # How many users per group to detect a 10% relative lift on a 5% baseline?
  python3 sample_size.py proportion --baseline 0.05 --mde-rel 0.10

  # Same, but tell me the duration given 4000 eligible users per day
  python3 sample_size.py proportion --baseline 0.05 --mde-rel 0.10 --daily 4000

  # What is the smallest effect I could detect with 20000 per group?
  python3 sample_size.py proportion --baseline 0.05 --n 20000

  # Continuous metric (revenue per user, time on task)
  python3 sample_size.py mean --mean 42.0 --sd 30.0 --mde-rel 0.05 --daily 4000

  # I plan to look at the results 5 times. Adjust for it.
  python3 sample_size.py proportion --baseline 0.05 --mde-rel 0.10 --peeks 5

  # Check a running test for sample ratio mismatch before trusting anything
  python3 sample_size.py srm --counts 10432 9987
"""

import argparse
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from _stats import norm_ppf, chi2_sf, fmt_p  # noqa: E402


def z_for(alpha, power, peeks=1):
    """Two-sided alpha, one-sided power. Bonferroni across looks if peeks > 1."""
    a = alpha / peeks if peeks > 1 else alpha
    return norm_ppf(1.0 - a / 2.0), norm_ppf(power), a


def n_proportion(p1, p2, alpha=0.05, power=0.8, peeks=1):
    """Per-group sample size for two independent proportions, equal allocation."""
    za, zb, _ = z_for(alpha, power, peeks)
    pbar = (p1 + p2) / 2.0
    num = (za * math.sqrt(2.0 * pbar * (1.0 - pbar))
           + zb * math.sqrt(p1 * (1.0 - p1) + p2 * (1.0 - p2))) ** 2
    return int(math.ceil(num / (p2 - p1) ** 2))


def n_mean(sd, delta, alpha=0.05, power=0.8, peeks=1):
    """Per-group sample size for a difference in means."""
    za, zb, _ = z_for(alpha, power, peeks)
    return int(math.ceil(2.0 * ((za + zb) * sd / delta) ** 2))


def mde_proportion(p1, n, alpha=0.05, power=0.8, peeks=1):
    """Smallest absolute lift detectable at given n per group. Solved numerically."""
    lo, hi = 1e-9, min(1.0 - p1 - 1e-9, 1.0)
    for _ in range(200):
        mid = (lo + hi) / 2.0
        try:
            need = n_proportion(p1, p1 + mid, alpha, power, peeks)
        except (ValueError, ZeroDivisionError):
            lo = mid
            continue
        if need > n:
            lo = mid
        else:
            hi = mid
    return hi


def mde_mean(sd, n, alpha=0.05, power=0.8, peeks=1):
    za, zb, _ = z_for(alpha, power, peeks)
    return (za + zb) * sd * math.sqrt(2.0 / n)


def duration_note(per_group, daily_eligible, groups=2):
    if not daily_eligible:
        return None
    total = per_group * groups
    days = total / float(daily_eligible)
    return total, days


def cmd_proportion(a):
    p1 = a.baseline
    if not 0 < p1 < 1:
        sys.exit("--baseline must be strictly between 0 and 1")

    if a.n:
        abs_mde = mde_proportion(p1, a.n, a.alpha, a.power, a.peeks)
        print("Minimum detectable effect at n=%d per group" % a.n)
        print("  baseline           %.4f" % p1)
        print("  absolute MDE       %+.4f  (to %.4f)" % (abs_mde, p1 + abs_mde))
        print("  relative MDE       %+.2f%%" % (100.0 * abs_mde / p1))
        print("  alpha %.3f  power %.2f  looks %d" % (a.alpha, a.power, a.peeks))
        print()
        print("Read this as: effects smaller than the MDE will usually be missed.")
        print("A non-significant result at this n does not mean no effect.")
        return

    if a.mde_rel:
        p2 = p1 * (1.0 + a.mde_rel)
    elif a.mde_abs:
        p2 = p1 + a.mde_abs
    else:
        sys.exit("give one of --mde-rel, --mde-abs, or --n")
    if not 0 < p2 < 1:
        sys.exit("target rate %.4f is out of range" % p2)

    n = n_proportion(p1, p2, a.alpha, a.power, a.peeks)
    print("Sample size, two proportions")
    print("  baseline           %.4f" % p1)
    print("  target             %.4f  (%+.2f%% relative, %+.4f absolute)"
          % (p2, 100.0 * (p2 - p1) / p1, p2 - p1))
    print("  alpha %.3f  power %.2f  looks %d" % (a.alpha, a.power, a.peeks))
    print()
    print("  n per group        %s" % format(n, ","))
    print("  n total (2 groups) %s" % format(2 * n, ","))
    if a.peeks > 1:
        print("  (alpha split across %d looks by Bonferroni: %.4f per look."
              % (a.peeks, a.alpha / a.peeks))
        print("   Conservative. A sequential method costs less sample for the same")
        print("   protection, but this is the version you can defend without one.)")

    d = duration_note(n, a.daily)
    if d:
        total, days = d
        print()
        print("  at %s eligible users/day: %.1f days (%.1f weeks)"
              % (format(a.daily, ","), days, days / 7.0))
        if days > 28:
            print("  WARNING: over 4 weeks. Long tests drift: seasonality, cookie churn,")
            print("  and concurrent releases all contaminate the comparison.")
        if days < 7:
            print("  NOTE: run at least 7 full days regardless, to cover the weekly cycle.")
    print()
    print("Before trusting any result from this test:")
    print("  1. Check sample ratio mismatch (sample_size.py srm --counts a b)")
    print("  2. Confirm the primary metric was declared before launch")
    print("  3. Confirm the stopping rule was declared before launch")


def cmd_mean(a):
    if a.n:
        d = mde_mean(a.sd, a.n, a.alpha, a.power, a.peeks)
        print("Minimum detectable effect at n=%d per group" % a.n)
        print("  sd                 %.4f" % a.sd)
        print("  absolute MDE       %+.4f" % d)
        if a.mean:
            print("  relative MDE       %+.2f%%" % (100.0 * d / a.mean))
        return
    if a.mde_rel:
        if not a.mean:
            sys.exit("--mde-rel needs --mean")
        delta = a.mean * a.mde_rel
    elif a.mde_abs:
        delta = a.mde_abs
    else:
        sys.exit("give one of --mde-rel, --mde-abs, or --n")

    n = n_mean(a.sd, delta, a.alpha, a.power, a.peeks)
    print("Sample size, difference in means")
    if a.mean:
        print("  mean               %.4f" % a.mean)
    print("  sd                 %.4f" % a.sd)
    print("  delta              %+.4f" % delta)
    print("  alpha %.3f  power %.2f  looks %d" % (a.alpha, a.power, a.peeks))
    print()
    print("  n per group        %s" % format(n, ","))
    print("  n total (2 groups) %s" % format(2 * n, ","))
    d = duration_note(n, a.daily)
    if d:
        total, days = d
        print()
        print("  at %s eligible/day: %.1f days (%.1f weeks)"
              % (format(a.daily, ","), days, days / 7.0))
    print()
    print("Revenue-style metrics are heavy-tailed. The sd from a short window")
    print("underestimates the real one, so this n is optimistic. Consider winsorising")
    print("at the 99th percentile and recomputing, and report both.")


def cmd_srm(a):
    counts = a.counts
    expected = a.expected
    total = sum(counts)
    if expected:
        if abs(sum(expected) - 1.0) > 1e-6:
            s = sum(expected)
            expected = [e / s for e in expected]
    else:
        expected = [1.0 / len(counts)] * len(counts)
    exp_counts = [e * total for e in expected]
    chi2 = sum((o - e) ** 2 / e for o, e in zip(counts, exp_counts))
    df = len(counts) - 1
    p = chi2_sf(chi2, df)
    print("Sample ratio mismatch check")
    print("  observed   %s" % "  ".join(format(c, ",") for c in counts))
    print("  expected   %s" % "  ".join(format(int(round(e)), ",") for e in exp_counts))
    print("  chi2 = %.4f, df = %d, p = %s" % (chi2, df, fmt_p(p)))
    print()
    if p < 0.001:
        print("  SRM DETECTED. Do not interpret this experiment.")
        print("  The randomiser, the logging, or the filtering is broken. Common causes:")
        print("    - redirect or latency differences between variants")
        print("    - bot filtering applied after assignment")
        print("    - assignment logged before an eligibility check that differs by arm")
        print("    - one variant crashing and dropping its own telemetry")
        print("  Fix the pipeline and rerun. A result from an SRM test is not a result.")
    elif p < 0.01:
        print("  Borderline. Investigate before reading the result.")
    else:
        print("  No mismatch detected. This is a necessary check, not a sufficient one.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    common = dict(alpha=("--alpha", 0.05), power=("--power", 0.8))

    p = sub.add_parser("proportion", help="binary metric: conversion, click, signup")
    p.add_argument("--baseline", type=float, required=True)
    p.add_argument("--mde-rel", type=float, help="relative lift, e.g. 0.10 for +10%%")
    p.add_argument("--mde-abs", type=float, help="absolute lift, e.g. 0.005")
    p.add_argument("--n", type=int, help="known n per group; returns the MDE instead")
    p.add_argument("--daily", type=int, help="eligible users per day, for a duration estimate")
    p.add_argument("--alpha", type=float, default=0.05)
    p.add_argument("--power", type=float, default=0.8)
    p.add_argument("--peeks", type=int, default=1, help="planned number of looks at the data")
    p.set_defaults(func=cmd_proportion)

    m = sub.add_parser("mean", help="continuous metric: revenue, duration, count")
    m.add_argument("--mean", type=float)
    m.add_argument("--sd", type=float, required=True)
    m.add_argument("--mde-rel", type=float)
    m.add_argument("--mde-abs", type=float)
    m.add_argument("--n", type=int)
    m.add_argument("--daily", type=int)
    m.add_argument("--alpha", type=float, default=0.05)
    m.add_argument("--power", type=float, default=0.8)
    m.add_argument("--peeks", type=int, default=1)
    m.set_defaults(func=cmd_mean)

    s = sub.add_parser("srm", help="sample ratio mismatch check")
    s.add_argument("--counts", type=int, nargs="+", required=True)
    s.add_argument("--expected", type=float, nargs="+",
                   help="expected proportions, default equal split")
    s.set_defaults(func=cmd_srm)

    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
