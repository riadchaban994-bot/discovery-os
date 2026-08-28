# Behavioural analysis

## Funnels

**Build it right:**
- Define each step as an event with a definition, not as a page
- Enforce ordering: a user counts at step k only if they passed every prior step.
  `scripts/cohorts_funnels.py` does this
- Choose the window deliberately. A same-session funnel and a 30-day funnel answer
  different questions, and B2B funnels that ignore multi-session behaviour report fiction
- Report both step conversion and conversion from the top
- Always split by segment before concluding anything

**Read it right:**
- The biggest absolute loss is usually the first step, and it is usually the least
  interesting because it includes people who were never going to convert
- The biggest opportunity is the step with the worst conversion **among people who
  demonstrated intent**
- A step that converts at 95 percent is not a success, it is a step that is not doing
  anything. Consider removing it
- Compare against the same funnel for a segment that works, not against an industry
  benchmark

**Do not:** compare a funnel across periods without checking traffic mix.
Run `scripts/cohorts_funnels.py simpson`.

## Cohort retention

The single most informative chart in product analytics.

**Build it right:**
- Cohort by first-value date, not by signup date, where they differ
- The retention event is the **core value action**, never a login. Login retention flatters
  everything and has misled more teams than any other metric choice
- Use the natural period: daily for a daily-use product, weekly for weekly, monthly for
  monthly. A monthly period on a daily product hides everything
- Plot the curve. The table hides the shape

**Read it right:**

| Shape | Meaning |
|---|---|
| Declines to zero | No retained base. Nothing else matters yet |
| Flattens above zero | A segment gets ongoing value. That plateau is your real market |
| Flattens then declines late | Value decays, or a competitor arrived |
| Smiles (rises after a dip) | Resurrection, or a strong network effect |
| Later cohorts above earlier | The product is improving. The most encouraging pattern there is |

The **plateau height** is the number that matters, not the week-one drop. A product with
40 percent week-one retention and a 20 percent plateau is far healthier than one with 70
percent week-one and a 2 percent plateau.

**Segment the curve.** A flat aggregate curve often hides one segment retaining well and
another not at all. That split is usually the most actionable finding available.

## Churn and survival

**Define churn precisely first.** Cancelled and dormant are different events with different
causes and different interventions. Say which one you mean, and say what dormancy window
you chose and why.

**Use survival analysis, not a churn rate**, when users have been around for different
lengths of time. A raw churn rate ignores censoring: users who have not churned *yet* are
not survivors, they are unfinished. `scripts/cohorts_funnels.py survival`.

**Timing tells you the cause:**

| When they churn | Usually |
|---|---|
| Before first value | Onboarding, or a mismatch between the promise and the product |
| Weeks 1-4 | Value not established, habit not formed |
| Months 3-6 | The initial use case ended, or expansion never happened |
| At renewal | Price, procurement, or a champion who left |
| Slow fade | Value decay or gradual displacement |

**Find the leading indicator, then be careful with it.** The behaviour in week one that
predicts month-three retention is a predictor. Making users do it does not make them retain.
Only an experiment can tell you whether the relationship is causal, and usually it is not.

## Segmentation

**Behavioural segments beat demographic ones** for product decisions, almost always. What
someone does with the product predicts what they need; how old they are does not.

**Useful axes:** frequency of the core action, breadth of feature use, entry point, job
being done, team size or account structure, tenure, acquisition channel.

**Method:** start with a hypothesis from qualitative work, then test whether the segments
behave differently on the metrics that matter. Clustering without a hypothesis produces
mathematically valid groups nobody can act on.

**Test a segment is real:** the groups differ on a metric you care about, the difference is
stable across periods, you can identify which group a user is in from data you have, and
you would do something different for each. All four, or it is not a segment.

## Feature adoption

Three dimensions, all needed:

- **Breadth**: what share of eligible users used it at all
- **Depth**: how much the users who adopted it use it
- **Frequency**: how often they come back to it

Low breadth with high depth means a niche feature that matters intensely to a few. That is
a discovery finding, not a failure, and the response is to find out who they are.

Low breadth with low depth means either nobody wants it or nobody found it. You cannot tell
which without an `exposed` event, which is why that event matters.

## Existing-behaviour mining

The cheapest quantitative discovery available on a live product:

- **In-product search with zero results.** What people are looking for and cannot find.
  Usually the highest-yield unused data source in the company
- **Repeated actions in one session.** Signals a missing bulk action or a broken flow
- **Export events.** Every export is a job the product does not do
- **Back-navigation and loops.** Confusion, or a missing overview
- **Rage clicks and dead clicks.** Broken affordances
- **Manual workarounds in the data.** Users putting structured information into free-text
  fields is a feature request written in behaviour
- **Time-of-day and day-of-week patterns.** Tells you the real job context
- **Sessions ending on a specific screen.** Where people give up
