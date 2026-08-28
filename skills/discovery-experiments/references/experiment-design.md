# Experiment design

## Randomisation

**Unit of randomisation** must match the unit of interference.

| Unit | Use when | Watch for |
|---|---|---|
| User | Independent users, most product changes | Cross-device: one person becomes two units |
| Session | Effect is within-session only | Same user in both arms, which biases toward null |
| Account or team | B2B, shared workspaces | Small number of units, so power is low |
| Geo | Marketing, pricing, supply-side changes | Few units, high variance, needs long windows |
| Time block (switchback) | Marketplaces, dispatch, shared inventory | Carryover between blocks |
| Cluster | Social graphs, network effects | Cluster definition determines validity |

**The interference test:** can one user's assignment affect another user's outcome? If yes,
user-level randomisation is invalid and the result will be biased, usually toward zero.

**Assignment must be:** deterministic from a stable id, independent of any user attribute,
logged at the moment of exposure, and identical across platforms. Randomising at page load
but logging at page render loses users differentially by speed, which manufactures SRM.

## Power and duration

`../discovery-quant/scripts/sample_size.py`. Decide these before launching:

- **Alpha.** 0.05 conventionally. Lower it if the cost of a false positive is high.
- **Power.** 0.8 conventionally. Raise it to 0.9 if a missed effect is expensive.
- **MDE.** The smallest effect worth acting on, from the business case, never from what the
  sample happens to be able to detect. This is the number teams skip.
- **Duration.** Whole weeks. At least one full weekly cycle. Longer than four weeks invites
  drift, cookie churn and concurrent releases.

If the required sample is unreachable, the experiment is not available. Say so and route to
a qualitative or commitment-based method rather than running an underpowered test whose null
will be misread as no effect.

## Thresholds and decision rules

Written before launch:

```
SHIP IF:        primary metric lift > MDE, lower bound of the 95% interval above zero,
                no guardrail degraded beyond its threshold
DO NOT SHIP IF: lower bound below zero, or any guardrail breached
INCONCLUSIVE:   anything else. Named in advance so it cannot be reinterpreted later
```

The inconclusive band is what keeps the test honest.

## Quasi-experimental designs

When randomisation is impossible. Each rests on an identifying assumption that must be
stated in the readout and checked.

**Difference-in-differences.** Compare the change in a treated group to the change in an
untreated one.
*Assumption:* parallel trends. The two groups would have moved together absent treatment.
*Check:* plot both series for several periods before treatment. If they were not parallel
before, the design is invalid.

**Interrupted time series.** Model the pre-period trend, project it, compare to actual.
*Assumption:* nothing else changed at the same time, and the pre-trend is stable.
*Check:* the change log, and a control series that should not have been affected.

**Regression discontinuity.** Exploit a threshold rule (a score cutoff, a date, a price
band) where units just either side are comparable.
*Assumption:* units cannot precisely manipulate their position around the cutoff.
*Check:* the density of units around the threshold for bunching.

**Synthetic control.** Build a weighted combination of untreated units that reproduces the
treated unit's pre-period, then compare after.
*Assumption:* the synthetic control would have continued to track.
*Check:* pre-period fit quality, and placebo tests on untreated units.

**Propensity matching.** Match treated and untreated units on observed characteristics.
*Assumption:* no unobserved confounders. This assumption is almost always false in product
data, because the decision to adopt a feature is driven by exactly the unobserved motivation
that also drives the outcome.
*Use with heavy caveats, or not at all.*

**Reporting rule.** A quasi-experimental result is never presented with the confidence of a
randomised one. State the design, the assumption, the check you ran, and the competing
explanation you could not rule out.

## Threats to validity, checked every time

| Threat | Check |
|---|---|
| Sample ratio mismatch | Chi-square before anything else |
| Novelty effect | Effect over time within the experiment; new versus existing users |
| Primacy effect | Existing users separately; effect in later weeks |
| Interference | Is the unit of randomisation right for the mechanism |
| Seasonality | Whole weeks; compare to the same window last year |
| Concurrent changes | The release and campaign log for the window |
| Selection into exposure | Was assignment logged at exposure or earlier |
| Instrumentation differences | Does one arm log differently, or crash more |
| Multiple comparisons | One primary, everything else exploratory or corrected |
| Peeking | Fixed horizon or a sequential design |
| Winner's curse | The measured effect of a barely-significant winner is biased upward. Expect the real effect to be smaller than the estimate |

## Reading a result

1. SRM check. If it fails, stop
2. Guardrails. If breached, stop
3. Primary metric: effect, interval, against the pre-declared threshold
4. Effect stability over the run
5. Segment reads, labelled exploratory unless pre-declared
6. Decision against the pre-declared rule

**Report the interval, not the point.** Plan against the pessimistic end. A "+8 percent"
result with an interval from +1 to +15 is a decision about whether +1 is worth shipping.

## When you cannot experiment

Small traffic, no platform, a one-way change, an enterprise product with forty customers.
This is normal and it is not a reason to guess.

- Commitment evidence (L6) substitutes well for causal evidence on value questions
- Qualitative depth substitutes well on "why" questions
- A holdout on a programme is often possible even where a feature test is not
- Staged rollout with a carefully watched control cohort gives a weak but honest read
- Say "we cannot establish causality here" and give the associational read with the
  competing explanations listed. That is a better answer than a confident wrong one
