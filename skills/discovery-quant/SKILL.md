---
name: discovery-quant
description: Use when a product metric moved and the cause is unknown, when designing what to measure for a feature or outcome, when analysing funnels, cohorts, retention or churn, when working out how many users a test needs, when analysing a survey, or when a number in a document needs checking before anyone acts on it.
---

# Discovery quant

## Core principle

Quantitative analysis tells you **how much, how often, and for whom**. It cannot tell you
why. Every "why" question routed here must end with a qualitative step, and every
qualitative claim about prevalence must end here.

Second principle, equally load-bearing: **before believing a movement, check that it
happened.** A large share of investigated metric movements are tracking changes, bot
traffic, definition changes, timezone artefacts, or reporting-window effects. Check
measurement before you check the world.

## Runnable scripts

All in `scripts/`, standard library only unless noted, tested and working.

| Script | Does |
|---|---|
| `scripts/sample_size.py` | Sample size, power, minimum detectable effect, duration, SRM check |
| `scripts/experiment_analysis.py` | Binary and continuous results with intervals, Bayesian read, CUPED, multiple-comparison correction |
| `scripts/cohorts_funnels.py` | Funnels with segment split, cohort retention with flattening check, Kaplan-Meier survival, Simpson's paradox detector |
| `scripts/survey_analysis.py` | Kano, Van Westendorp, MaxDiff, PMF survey, Likert done properly |
| `scripts/qual_saturation.py` | Saturation curve, code frequency by source, Cohen's kappa |

Run any with `--help`. They print their own caveats alongside the numbers, by design.

## The diagnostic sequence

When a metric moves, run these in order. Do not skip to step 5.

**1. Did it actually move?**
Tracking release, SDK version, definition change, bot or crawler traffic, timezone or
reporting window, a backfill, a data pipeline failure, a filter change. Compare against a
metric that should not have moved. If that one moved too, the cause is measurement.

**2. Where is it concentrated?**
Decompose by acquisition source, platform, app version, geography, plan, device, cohort,
new versus returning. A movement spread evenly across every segment is usually external or
measurement. A movement concentrated in one slice is usually a change.
Run the Simpson's check: `scripts/cohorts_funnels.py simpson`.

**3. What changed at the same time?**
Releases, pricing, campaigns, outages, competitor moves, seasonality, holidays, a
partner's change. Build the timeline before forming a theory.

**4. Which transition changed?**
Funnel decomposition on the affected slice: `scripts/cohorts_funnels.py funnel --segment`.

**5. Now ask people.**
Recruit specifically from the affected slice and ask about the specific episode, not about
the metric. Route to `discovery-interviewing`.

## Metric design

Goals, then signals, then metrics, in that order (Rodden, Hutchinson and Fu, Google).
Choosing a metric before naming the goal produces whatever is easiest to log.

Every metric set needs: one primary, two or three guardrails, and a stated direction.
A metric that cannot go down when you do a bad job is not a metric.

Full guidance, including HEART, North Star, counter-metrics and the common traps, in
`references/metric-design.md`.

## Behavioural analysis

Funnels, cohorts, retention curves, survival, segmentation, feature adoption breadth and
depth. `references/behavioural-analysis.md`.

**Retention first, always.** A flattening retention curve on the core value action is the
primary signal of product-market fit. Acquisition and pricing work is wasted while the
curve goes to zero.

## Surveys

Only after qualitative grounding. A survey written before the interviews measures the
author's assumptions. `references/survey-methods.md` covers instrument choice, question
design, sampling frames, non-response bias, and the scoring for each instrument.

## Statistical guardrails

`references/statistical-guardrails.md`. The short version:

- No percentages below n=30. No subgroups below n=30
- Every estimate gets an interval. The interval is the result
- Non-significant is not the same as no effect. Report the minimum detectable effect
- Check sample ratio mismatch before reading any experiment
- Correct for multiple comparisons, or declare metrics exploratory
- Never peek without a design that allows it
- Heavy-tailed metrics: winsorise and re-check before shipping on a mean
- Simpson's paradox on every aggregate movement
- Correlation is not cause, and neither is before-and-after

## Output rules

- Every number carries n and the date range
- Every rate carries its denominator
- Every comparison carries an interval
- Every causal claim carries its design, or the label "associational"
- Every chart is described in words, because the words are what get quoted

## Read next

| File | For |
|---|---|
| `references/metric-design.md` | Choosing what to measure |
| `references/behavioural-analysis.md` | Funnels, cohorts, retention, churn, segmentation |
| `references/survey-methods.md` | Designing and scoring surveys |
| `references/statistical-guardrails.md` | Not being wrong |

## Red flags

- A metric that only goes up
- A percentage with no denominator
- A comparison with no interval
- A causal verb on a before-and-after
- An aggregate that moved with no segment check
- A survey designed before any interviews
- A dashboard nobody has questioned in six months
- An experiment result read before the SRM check
- "Statistically significant" with no effect size
