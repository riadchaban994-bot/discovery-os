#!/usr/bin/env python3
"""
Analyse a finished experiment, honestly.

Reports the effect with an interval, checks the things that make experiments lie
(sample ratio mismatch, multiple comparisons, underpowered nulls), and refuses to
print a bare "significant" verdict without the context that makes it meaningful.

Usage
-----
  # Binary metric from counts
  python3 experiment_analysis.py binary --control 1204 24010 --variant 1310 23980

  # Same, with a Bayesian read alongside (needs numpy)
  python3 experiment_analysis.py binary --control 1204 24010 --variant 1310 23980 --bayes

  # Continuous metric from summary statistics
  python3 experiment_analysis.py continuous --control-stats 42.1 30.2 12000 \
                                            --variant-stats 43.8 31.0 11950

  # Continuous metric from a CSV with columns: group,value
  python3 experiment_analysis.py continuous --csv results.csv --group-col group --value-col value

  # Variance reduction with a pre-period covariate (CUPED). CSV: group,value,pre_value
  python3 experiment_analysis.py cuped --csv results.csv

  # Correct a family of metrics you looked at
  python3 experiment_analysis.py multiple --pvalues 0.012 0.031 0.048 0.20 0.44
"""

import argparse
import csv
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from _stats import (norm_ppf, chi2_sf, two_proportion_z, diff_ci, wilson_ci,  # noqa: E402
                    welch_t, benjamini_hochberg, fmt_p)


def srm_check(n1, n2, expected_ratio=0.5):
    total = n1 + n2
    e1, e2 = total * expected_ratio, total * (1 - expected_ratio)
    chi2 = (n1 - e1) ** 2 / e1 + (n2 - e2) ** 2 / e2
    return chi2, chi2_sf(chi2, 1)


def banner(text):
    print()
    print(text)
    print("-" * len(text))


def cmd_binary(a):
    x1, n1 = a.control
    x2, n2 = a.variant
    alpha = a.alpha

    banner("Experiment: binary metric")
    print("  control  %s / %s = %.4f" % (format(x1, ","), format(n1, ","), x1 / n1))
    print("  variant  %s / %s = %.4f" % (format(x2, ","), format(n2, ","), x2 / n2))

    chi2, srm_p = srm_check(n1, n2, a.expected_ratio)
    banner("1. Sample ratio mismatch")
    print("  chi2 = %.3f, p = %s" % (chi2, fmt_p(srm_p)))
    if srm_p < 0.001:
        print("  SRM DETECTED. STOP. Do not read the result below.")
        print("  The assignment or logging pipeline is broken. Everything downstream")
        print("  of a broken randomiser is uninterpretable, including a result that")
        print("  looks good.")
        if not a.force:
            print()
            print("  Re-run with --force only to inspect the numbers for debugging.")
            return
    else:
        print("  OK.")

    p1, p2, diff, z, pval = two_proportion_z(x1, n1, x2, n2)
    lo, hi = diff_ci(x1, n1, x2, n2, alpha)
    rel = diff / p1 if p1 > 0 else float("nan")
    rel_lo, rel_hi = (lo / p1, hi / p1) if p1 > 0 else (float("nan"), float("nan"))

    banner("2. Effect")
    print("  absolute  %+.4f   %d%% CI [%+.4f, %+.4f]"
          % (diff, round((1 - alpha) * 100), lo, hi))
    print("  relative  %+.2f%%   %d%% CI [%+.2f%%, %+.2f%%]"
          % (100 * rel, round((1 - alpha) * 100), 100 * rel_lo, 100 * rel_hi))
    print("  z = %.3f, p = %s" % (z, fmt_p(pval)))
    print("  control CI  [%.4f, %.4f]" % wilson_ci(x1, n1, alpha))
    print("  variant CI  [%.4f, %.4f]" % wilson_ci(x2, n2, alpha))

    banner("3. Reading")
    sig = pval < alpha
    if sig:
        print("  Statistically distinguishable from zero at alpha=%.3f." % alpha)
        print("  The interval is the result, not the point estimate. Plan against")
        print("  the low end: %+.2f%% relative." % (100 * rel_lo))
        if lo * hi < 0:
            print("  NOTE: the interval crosses zero despite p < alpha. Check inputs.")
    else:
        # what could this test have detected?
        from sample_size import mde_proportion
        mde = mde_proportion(p1, min(n1, n2), alpha, 0.8)
        print("  Not distinguishable from zero at alpha=%.3f." % alpha)
        print("  This is NOT evidence of no effect. With n=%s per group this test"
              % format(min(n1, n2), ","))
        print("  could only reliably detect effects above %+.2f%% relative."
              % (100 * mde / p1))
        print("  A real effect smaller than that would look exactly like this.")
    print()
    print("  Still required before shipping:")
    print("   - guardrail metrics unchanged")
    print("   - primary metric declared before launch, not chosen now")
    print("   - full weekly cycles covered")
    print("   - novelty effect checked: is the effect stable across the run?")

    if a.bayes:
        banner("4. Bayesian read")
        try:
            import numpy as np
        except ImportError:
            print("  numpy not installed; skipping.")
            return
        rng = np.random.default_rng(12345)
        draws = 200000
        sa = rng.beta(x1 + 1, n1 - x1 + 1, draws)
        sb = rng.beta(x2 + 1, n2 - x2 + 1, draws)
        p_better = float((sb > sa).mean())
        lift = (sb - sa) / sa
        loss_b = float(np.maximum(sa - sb, 0).mean())
        print("  Uniform Beta(1,1) prior, %s draws." % format(draws, ","))
        print("  P(variant > control) = %.4f" % p_better)
        print("  relative lift, 95%% credible interval [%+.2f%%, %+.2f%%]"
              % (100 * np.percentile(lift, 2.5), 100 * np.percentile(lift, 97.5)))
        print("  expected loss if you ship the variant = %.5f absolute" % loss_b)
        print()
        print("  This is a different question from the p-value, not a friendlier")
        print("  version of it. It answers: given the data and a flat prior, how")
        print("  likely is the variant better. It does not fix peeking either.")


def cmd_continuous(a):
    if a.csv:
        rows = list(csv.DictReader(open(a.csv)))
        groups = {}
        for r in rows:
            g = r[a.group_col]
            groups.setdefault(g, []).append(float(r[a.value_col]))
        if len(groups) != 2:
            sys.exit("expected exactly 2 groups, found %d: %s"
                     % (len(groups), ", ".join(sorted(groups))))
        keys = sorted(groups)
        c, v = groups[keys[0]], groups[keys[1]]
        m1, m2 = sum(c) / len(c), sum(v) / len(v)
        s1 = math.sqrt(sum((x - m1) ** 2 for x in c) / (len(c) - 1))
        s2 = math.sqrt(sum((x - m2) ** 2 for x in v) / (len(v) - 1))
        n1, n2 = len(c), len(v)
        label1, label2 = keys[0], keys[1]
    else:
        m1, s1, n1 = a.control_stats[0], a.control_stats[1], int(a.control_stats[2])
        m2, s2, n2 = a.variant_stats[0], a.variant_stats[1], int(a.variant_stats[2])
        label1, label2 = "control", "variant"

    banner("Experiment: continuous metric")
    print("  %-8s mean %.4f  sd %.4f  n %s" % (label1, m1, s1, format(n1, ",")))
    print("  %-8s mean %.4f  sd %.4f  n %s" % (label2, m2, s2, format(n2, ",")))

    chi2, srm_p = srm_check(n1, n2, a.expected_ratio)
    banner("1. Sample ratio mismatch")
    print("  chi2 = %.3f, p = %s%s" % (chi2, fmt_p(srm_p),
                                       "   SRM DETECTED" if srm_p < 0.001 else "   OK"))

    t, df, pval = welch_t(m1, s1, n1, m2, s2, n2)
    se = math.sqrt(s1 * s1 / n1 + s2 * s2 / n2)
    z = norm_ppf(1 - a.alpha / 2)
    diff = m2 - m1
    banner("2. Effect (Welch, unequal variance)")
    print("  absolute  %+.4f   %d%% CI [%+.4f, %+.4f]"
          % (diff, round((1 - a.alpha) * 100), diff - z * se, diff + z * se))
    if m1 != 0:
        print("  relative  %+.2f%%   %d%% CI [%+.2f%%, %+.2f%%]"
              % (100 * diff / m1, round((1 - a.alpha) * 100),
                 100 * (diff - z * se) / m1, 100 * (diff + z * se) / m1))
    print("  t = %.3f, df = %.1f, p = %s" % (t, df, fmt_p(pval)))

    banner("3. Distribution warning")
    print("  Revenue, session length and count metrics are heavy-tailed. A mean")
    print("  comparison on a heavy tail is driven by a handful of users and moves")
    print("  between runs. Before shipping on this result:")
    print("   - winsorise at the 99th percentile and re-run. If the sign flips, the")
    print("     effect is a few outliers, not the treatment")
    print("   - report the median and a quantile comparison alongside the mean")
    print("   - check whether the effect is a shift in the whole distribution or a")
    print("     change in the proportion of users who did anything at all")


def cmd_cuped(a):
    try:
        import numpy as np
    except ImportError:
        sys.exit("cuped needs numpy")
    rows = list(csv.DictReader(open(a.csv)))
    groups = {}
    for r in rows:
        g = r[a.group_col]
        groups.setdefault(g, []).append((float(r[a.value_col]), float(r[a.pre_col])))
    keys = sorted(groups)
    if len(keys) != 2:
        sys.exit("expected exactly 2 groups")

    allv = np.array([v for k in keys for v, _ in groups[k]])
    allx = np.array([x for k in keys for _, x in groups[k]])
    varx = allx.var(ddof=1)
    if varx == 0:
        sys.exit("covariate has zero variance")
    theta = np.cov(allv, allx, ddof=1)[0, 1] / varx
    xbar = allx.mean()
    corr = float(np.corrcoef(allv, allx)[0, 1])

    banner("CUPED variance reduction")
    print("  theta = %.4f" % theta)
    print("  corr(metric, pre-period covariate) = %.4f" % corr)
    print("  expected variance reduction = %.1f%%" % (100 * corr ** 2))
    if abs(corr) < 0.2:
        print("  Covariate is weak. CUPED will not help much here. A stronger")
        print("  covariate is usually the same metric measured in the pre-period.")

    out = []
    for k in keys:
        arr = np.array(groups[k])
        adj = arr[:, 0] - theta * (arr[:, 1] - xbar)
        out.append((k, arr[:, 0], adj))

    for label, raw, adj in out:
        print("  %-10s raw mean %.4f (sd %.4f) -> adjusted mean %.4f (sd %.4f)"
              % (label, raw.mean(), raw.std(ddof=1), adj.mean(), adj.std(ddof=1)))

    (k1, r1, a1), (k2, r2, a2) = out
    t_raw, df_raw, p_raw = welch_t(r1.mean(), r1.std(ddof=1), len(r1),
                                   r2.mean(), r2.std(ddof=1), len(r2))
    t_adj, df_adj, p_adj = welch_t(a1.mean(), a1.std(ddof=1), len(a1),
                                   a2.mean(), a2.std(ddof=1), len(a2))
    print()
    print("  raw:      diff %+.4f, p = %s" % (r2.mean() - r1.mean(), fmt_p(p_raw)))
    print("  adjusted: diff %+.4f, p = %s" % (a2.mean() - a1.mean(), fmt_p(p_adj)))
    print()
    print("  CUPED reduces variance using pre-experiment data. It does not change")
    print("  the expected effect and it is not a way to rescue a null result. If")
    print("  the adjusted effect differs a lot from the raw one, check that the")
    print("  covariate is genuinely pre-treatment.")


def cmd_multiple(a):
    res = benjamini_hochberg(a.pvalues, a.alpha)
    banner("Multiple comparison correction")
    print("  %d metrics tested, alpha = %.3f" % (len(a.pvalues), a.alpha))
    print()
    print("  %-6s %-10s %-12s %-10s %s" % ("#", "raw p", "BH adj p", "bonf p", "survives BH"))
    m = len(a.pvalues)
    for i, p, adj, rej in sorted(res, key=lambda r: r[1]):
        print("  %-6d %-10s %-12s %-10s %s"
              % (i + 1, fmt_p(p), fmt_p(adj), fmt_p(min(1.0, p * m)),
                 "yes" if rej else "no"))
    print()
    print("  Testing %d metrics at alpha=%.3f gives roughly a %.0f%% chance of at"
          % (m, a.alpha, 100 * (1 - (1 - a.alpha) ** m)))
    print("  least one false positive with no correction at all.")
    print()
    print("  The real fix is upstream: declare ONE primary metric before launch.")
    print("  Everything else is exploratory and is reported as exploratory.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("binary")
    b.add_argument("--control", type=int, nargs=2, required=True, metavar=("CONV", "N"))
    b.add_argument("--variant", type=int, nargs=2, required=True, metavar=("CONV", "N"))
    b.add_argument("--alpha", type=float, default=0.05)
    b.add_argument("--expected-ratio", type=float, default=0.5)
    b.add_argument("--bayes", action="store_true")
    b.add_argument("--force", action="store_true", help="print results despite SRM")
    b.set_defaults(func=cmd_binary)

    c = sub.add_parser("continuous")
    c.add_argument("--control-stats", type=float, nargs=3, metavar=("MEAN", "SD", "N"))
    c.add_argument("--variant-stats", type=float, nargs=3, metavar=("MEAN", "SD", "N"))
    c.add_argument("--csv")
    c.add_argument("--group-col", default="group")
    c.add_argument("--value-col", default="value")
    c.add_argument("--alpha", type=float, default=0.05)
    c.add_argument("--expected-ratio", type=float, default=0.5)
    c.set_defaults(func=cmd_continuous)

    u = sub.add_parser("cuped")
    u.add_argument("--csv", required=True)
    u.add_argument("--group-col", default="group")
    u.add_argument("--value-col", default="value")
    u.add_argument("--pre-col", default="pre_value")
    u.set_defaults(func=cmd_cuped)

    mm = sub.add_parser("multiple")
    mm.add_argument("--pvalues", type=float, nargs="+", required=True)
    mm.add_argument("--alpha", type=float, default=0.05)
    mm.set_defaults(func=cmd_multiple)

    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
