# Statistical guardrails

The failures that make product analysis wrong, and the check for each. Ordered by how often
they cause real damage.

---

## 1. Measurement before world

Before believing any movement: tracking release, SDK version, event definition change, bot
and crawler traffic, timezone, reporting window, backfill, pipeline failure, filter change.

**Check:** does a metric that should not have moved also move? If yes, the cause is
measurement. Twyman's law: any figure that looks interesting is usually wrong.

## 2. No denominator

Every rate carries its denominator, every count carries its population, every comparison
carries its base. "Conversion improved 30 percent" with no base is not a finding.

## 3. Small n percentages

Below n=30, counts only. Below n=100, no subgroups. A subgroup of 12 out of a sample of 400
is a sample of 12.

**Check:** every percentage in the document has n next to it, and n is at least 30.

## 4. No interval

Every estimate gets an interval. The interval is the result; the point estimate is the
midpoint of a range you should be planning against. Plan against the pessimistic end of
the interval for any decision that costs money.

## 5. Non-significant read as no effect

A non-significant result means the test could not distinguish the effect from zero. With a
small sample, that is almost guaranteed regardless of the truth.

**Check:** report the minimum detectable effect alongside every null.
`scripts/sample_size.py proportion --baseline B --n N`.

## 6. Sample ratio mismatch

If the split is not what you designed, the randomiser or the logging is broken and nothing
downstream is interpretable, including a result that looks good.

**Check:** `scripts/sample_size.py srm --counts a b`, before reading anything. p < 0.001 means stop.

Common causes: redirect latency differing by arm, bot filtering applied after assignment,
assignment logged before an eligibility check that differs by arm, one variant crashing and
losing its own telemetry.

## 7. Peeking

Watching a running test and stopping when it looks good inflates the false-positive rate
severely. At a nominal alpha of 0.05, repeated significance testing on a true null gives
roughly 8% after 2 looks, 14% after 5, 19% after 10 and 25% after 20
`[src: Armitage, McPherson and Rowe (1969); reproduced by simulation in this
repository's test suite]`. A one-in-three false-positive rate needs about fifty looks.

**Fix:** fixed horizon declared in advance, or a sequential method built for continuous
monitoring, or Bonferroni across a small declared number of looks
(`scripts/sample_size.py --peeks K`, conservative but defensible).

## 8. Multiple comparisons

Twenty metrics at alpha=0.05 gives a 64 percent chance of at least one false positive.

**Fix:** one declared primary metric. Everything else labelled exploratory, or corrected
(`scripts/experiment_analysis.py multiple`).

## 9. Simpson's paradox

The aggregate moves while every segment holds steady, because the mix changed.

**Check:** `scripts/cohorts_funnels.py simpson` on every aggregate movement, and check segment
shares over time before attributing a change to behaviour.

## 10. Heavy tails

Revenue, session length and counts are heavy-tailed. A mean comparison is driven by a
handful of users and is unstable between runs.

**Fix:** winsorise at the 99th percentile and re-run. If the sign flips, the effect was a
few outliers. Report the median and a quantile comparison alongside the mean. Check whether
the effect is a distributional shift or a change in the share of users who did anything.

## 11. Survivorship

Analysing only users who are still here, only completed sessions, only successful accounts.
The ones who left are the sample you need.

**Check:** who is missing from this dataset because of what happened to them?

## 12. Regression to the mean

Select the worst-performing segment, intervene, observe improvement. Some of that
improvement would have happened anyway, because you selected on an extreme.

**Fix:** a control group drawn by the same selection rule.

## 13. Novelty and primacy

Early experiment results move because the change is new (novelty) or because existing users
are disrupted (primacy). Both fade.

**Check:** plot the effect over time within the experiment. If it is trending toward zero,
the result is novelty. Run long enough to see it settle, and check new users separately
from existing ones.

## 14. Interference

When one user's treatment affects another's outcome, user-level randomisation is invalid.
Marketplaces, social features, shared inventory, dispatch, pricing.

**Fix:** switchback, cluster randomisation, or geo experiments.

## 15. Correlation as cause

Users of feature X retain better, therefore push X. Users who chose X differ from users who
did not, in ways that also cause retention.

**Fix:** experiment. Failing that, write "associated with" and list the competing
explanations.

## 16. Before and after

The most common invalid causal design in product work. Confounded by seasonality, concurrent
releases, campaigns, and external events.

**Fix:** a control group, a comparison to the same window in a prior year, a
difference-in-differences with a parallel-trends check, or an explicit label as
non-causal.

## 17. Metric definition drift

The number changed because the definition changed. Usually discovered a quarter later.

**Fix:** versioned metric definitions with a changed-on line, and a note on every chart
that spans a definition change.

---

## Pre-registration template

Written and shared before launch. Any change afterwards is an amendment with a reason and a
timestamp, not a silent edit.

```
HYPOTHESIS: [specific, directional, falsifiable]
PRIMARY METRIC: [one, with its definition]
MDE: [the smallest effect worth acting on, decided from the business case, not from
      what the sample can detect]
GUARDRAILS: [2-3, with the thresholds that would stop the rollout]
SECONDARY: [labelled exploratory]
UNIT OF RANDOMISATION: [user / session / account / geo / time block]
SAMPLE SIZE: [n per group, and the calculation]
DURATION: [dates, whole weeks]
STOPPING RULE: [fixed horizon, or the sequential method]
EXCLUSIONS: [defined now, not after seeing the data]
ANALYSIS: [test, alpha, correction]
SHIP IF: [condition]
DO NOT SHIP IF: [condition]
THREATS TO VALIDITY: [interference, novelty, seasonality, concurrent changes]
```

The MDE line is the one teams skip. Deciding the smallest effect worth acting on **before**
seeing the data is what stops a statistically significant 0.2 percent lift from being
shipped as a win.
