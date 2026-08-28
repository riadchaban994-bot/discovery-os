# The analysis scripts

Five command line tools in `skills/discovery-quant/scripts/`. Python 3.8 or newer, standard
library only. numpy is needed for two optional modes and nothing else.

They exist because the statistical parts of discovery are where confident wrong answers come
from, and because a calculation is cheaper than an argument. Every one of them prints its
caveats next to its numbers, on purpose.

Run any with `--help`.

```bash
cd ~/.claude/skills/discovery-quant/scripts     # or wherever you installed
python3 sample_size.py --help
```

---

## Contents

- [sample_size.py](#sample_sizepy)
- [experiment_analysis.py](#experiment_analysispy)
- [cohorts_funnels.py](#cohorts_funnelspy)
- [survey_analysis.py](#survey_analysispy)
- [qual_saturation.py](#qual_saturationpy)
- [Accuracy](#accuracy)

---

## `sample_size.py`

Answer this before running anything: is the test even possible with the traffic you have,
in the time you have?

```bash
# How many per group to detect a 10% relative lift on a 5% baseline, and how long?
python3 sample_size.py proportion --baseline 0.05 --mde-rel 0.10 --daily 4000

# The reverse: what is the smallest effect I could detect with 20,000 per group?
python3 sample_size.py proportion --baseline 0.05 --n 20000

# Continuous metric
python3 sample_size.py mean --mean 42.0 --sd 30.0 --mde-rel 0.05 --daily 4000

# I plan to look at the results five times. Adjust for it.
python3 sample_size.py proportion --baseline 0.05 --mde-rel 0.10 --peeks 5

# Check a running test before trusting anything it says
python3 sample_size.py srm --counts 10432 9987
```

```
Sample size, two proportions
  baseline           0.0500
  target             0.0550  (+10.00% relative, +0.0050 absolute)
  alpha 0.050  power 0.80  looks 1

  n per group        31,234
  n total (2 groups) 62,468

  at 4,000 eligible users/day: 15.6 days (2.2 weeks)

Before trusting any result from this test:
  1. Check sample ratio mismatch (sample_size.py srm --counts a b)
  2. Confirm the primary metric was declared before launch
  3. Confirm the stopping rule was declared before launch
```

It warns when the run exceeds four weeks (drift, cookie churn, concurrent releases) and
when it is under a week (you have not covered the weekly cycle).

---

## `experiment_analysis.py`

Reads a finished experiment honestly. Checks the things that make experiments lie before it
reports anything.

```bash
# Binary metric from counts
python3 experiment_analysis.py binary --control 1204 24010 --variant 1310 23980

# With a Bayesian read alongside (needs numpy)
python3 experiment_analysis.py binary --control 1204 24010 --variant 1310 23980 --bayes

# Continuous, from summary stats or from a CSV of group,value
python3 experiment_analysis.py continuous --control-stats 42.1 30.2 12000 \
                                          --variant-stats 43.8 31.0 11950

# Variance reduction using a pre-period covariate
python3 experiment_analysis.py cuped --csv results.csv

# Correct a family of metrics you looked at
python3 experiment_analysis.py multiple --pvalues 0.012 0.031 0.048 0.20 0.44
```

```
Experiment: binary metric
-------------------------
  control  1,204 / 24,010 = 0.0501
  variant  1,310 / 23,980 = 0.0546

1. Sample ratio mismatch
------------------------
  chi2 = 0.019, p = 0.8911
  OK.

2. Effect
---------
  absolute  +0.0045   95% CI [+0.0005, +0.0085]
  relative  +8.94%   95% CI [+0.99%, +16.89%]
  z = 2.204, p = 0.0275
  control CI  [0.0475, 0.0530]
  variant CI  [0.0518, 0.0576]

3. Reading
----------
  Statistically distinguishable from zero at alpha=0.050.
  The interval is the result, not the point estimate. Plan against
```

**It refuses to read a result through a broken randomiser.** If the sample ratio check
fails at p < 0.001 it stops, explains the usual causes, and requires `--force` to print the
numbers for debugging.

**And it will not let a null be misread.** Feed it an underpowered test:

```
Experiment: binary metric
-------------------------
  control  50 / 2,000 = 0.0250
  variant  54 / 2,000 = 0.0270

1. Sample ratio mismatch
------------------------
  chi2 = 0.000, p = 1.0000
  OK.

2. Effect
---------
```

That last paragraph is the reason this script exists. "Not significant" gets reported as
"no effect" constantly, and on a small sample it means almost nothing.

---

## `cohorts_funnels.py`

Funnels, cohort retention, survival, and the Simpson's paradox check that most funnel
analysis skips. Pure standard library, no pandas.

```bash
# Funnel. CSV needs user_id and step columns.
python3 cohorts_funnels.py funnel --csv events.csv --steps view signup activate purchase

# Split by segment, which you should always do before concluding anything
python3 cohorts_funnels.py funnel --csv events.csv --steps view signup activate \
    --segment platform

# Cohort retention. CSV needs user_id, cohort, period.
python3 cohorts_funnels.py cohort --csv activity.csv --max-periods 12

# Kaplan-Meier survival. CSV needs duration and event (1 = churned, 0 = still active).
python3 cohorts_funnels.py survival --csv churn.csv

# Simpson's paradox check from an aggregate table
python3 cohorts_funnels.py simpson --csv breakdown.csv
```

The funnel enforces ordering: a user counts at step k only if they passed every prior step.
The cohort mode plots the curve and tells you whether it is flattening, which is the primary
product-market-fit signal. The survival mode handles censoring, because users who have not
churned yet are unfinished rather than survivors.

**The Simpson's check on a constructed reversal:**

```
Aggregate
  control             200 / 300      = 0.6667
  variant             140 / 300      = 0.4667
  aggregate difference (variant - control) = -0.2000

By segment
  desktop        control 0.9000 (n=200)   variant 0.9500 (n=100)   diff +0.0500
  mobile         control 0.2000 (n=100)   variant 0.2250 (n=200)   diff +0.0250

  SIMPSON'S PARADOX. Every segment favours variant, the aggregate favours control.

Segment mix
  control        desktop 66.7%   mobile 33.3%
  variant        desktop 33.3%   mobile 66.7%

  If the mix differs between groups, the aggregate comparison is
  comparing populations, not treatments.
```

Every segment favours the variant. The aggregate favours the control. The mix changed. Run
this on any aggregate movement before you attribute it to behaviour.

---

## `survey_analysis.py`

Survey instruments scored correctly, with their limits attached. Everything here produces
stated-preference evidence, L2 on the ladder, and the script says so.

```bash
# Kano. CSV: respondent_id, attribute, functional, dysfunctional (values 1-5)
python3 survey_analysis.py kano --csv kano.csv

# Van Westendorp. CSV: respondent_id, too_cheap, cheap, expensive, too_expensive
python3 survey_analysis.py vw --csv pricing.csv

# MaxDiff counting analysis. CSV: respondent_id, task, item, choice (best/worst/shown)
python3 survey_analysis.py maxdiff --csv maxdiff.csv

# Sean Ellis product-market fit survey. CSV: respondent_id, answer[, segment]
python3 survey_analysis.py pmf --csv pmf.csv

# Likert done properly: distribution and top-2-box, never a mean
python3 survey_analysis.py likert --csv likert.csv --value-col rating
```

```
Product-market fit survey (Sean Ellis)
  'How would you feel if you could no longer use this?'
  n = 220

  Very disappointed            89   40.5%  ##########..............
  Somewhat disappointed        76   34.5%  ########................
  Not disappointed             55   25.0%  ######..................

  Very disappointed: 40.5%  95% CI [34.2%, 47.1%]

  By segment
  segment                         n       very 
  solo                           67      70.1%  #################.......
  team                           74      33.8%  ########................
  enterprise                     79      21.5%  #####...................

  Reading this honestly:
   - Valid only among users who have experienced the core value at least
     twice. Surveying everyone dilutes it into meaninglessness.
   - The 40% threshold is a widely used heuristic from Sean Ellis's work,
```

Note what it does with the segment breakdown. The headline says 40.5 percent, which reads
as a pass against the usual heuristic. The segments say one group is at 70 percent and
another at 21 percent. The segment split is the finding; the headline is an average of two
different products.

Van Westendorp flags internally inconsistent responses rather than silently including them,
and tells you the output is a range to test with commitment, not a price to set. The Likert
mode refuses to print a mean and explains why, and detects bimodal distributions.

---

## `qual_saturation.py`

How many interviews is enough? Measured, not felt.

```bash
# Saturation curve. CSV: source_id, code[, segment]  (one row per code applied)
python3 qual_saturation.py saturation --csv codes.csv

# Per segment, which is the only valid way to claim saturation
python3 qual_saturation.py saturation --csv codes.csv --segment-col segment

# Code frequency by source count, the only count you may report
python3 qual_saturation.py frequency --csv codes.csv

# Inter-coder agreement
python3 qual_saturation.py kappa --csv doublecoded.csv
```

```
Saturation: all sources
  #    source                codes      new cumulative   new codes
  1    P01                       7        7          7   #######
  2    P02                       7        2          9   ##
  3    P03                       7        0          9   
  4    P04                       4        0          9   
  5    P05                       4        0          9   
  6    P06                       3        0          9   
  7    P07                       4        0          9   
  8    P08                       4        0          9   
  9    P09                       5        0          9   
  10   P10                       3        0          9   
  11   P11                       3        0          9   
  total unique codes: 9 across 11 sources

  SATURATED for this segment: the last 2 sources added no new codes.
  Additional interviews in this segment will mostly confirm. Move to a
  different segment, or to a different question.
```

If the second half of the corpus produces more new codes than the first, it tells you so:
that is the signature of a heterogeneous sample, and you are looking at two segments rather
than one.

The `frequency` mode counts **sources, not mentions**. One person saying something six
times is one source, and that single rule prevents more overclaiming than any other.

The `kappa` mode computes Cohen's kappa, which corrects for chance agreement, and lists the
most frequent disagreements so you can fix the codebook rather than average the difference.

---

## Accuracy

`_stats.py` implements the distributions from standard numerical recipes so the tools run on
a plain Python install:

| Function | Method | Verified against |
|---|---|---|
| `norm_cdf` | `math.erf` | machine precision |
| `norm_ppf` | Acklam's rational approximation plus one Halley step | 1.959964 at p=0.975, 0.841621 at p=0.80 |
| `t_sf` | regularised incomplete beta, continued fraction | p=0.05 at t=2.086, df=20 |
| `chi2_sf` | exact for 1 df, series and continued fraction otherwise | p=0.05 at 3.841/1df, 5.991/2df, 11.070/5df |
| `wilson_ci` | Wilson score interval | (0.1119, 0.4687) for 5/20 |
| `benjamini_hochberg` | Benjamini-Hochberg step-up | rejects exactly the first two of the canonical eight-p-value example |

`tests/validate.py` asserts all of these on every CI run, across Python 3.9, 3.11 and 3.13.
The end-to-end checks feed each script a fixture with a known answer: a constructed
Simpson's reversal, a skewed split, an underpowered null, and a saturated corpus.
