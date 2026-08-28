# Metric design

## Goals, signals, metrics

The order is the method (Rodden, Hutchinson and Fu, Google, CHI 2010). Reversing it is how
teams end up optimising page views.

1. **Goal.** What should be true for the user, in a sentence. Not what you will ship.
2. **Signal.** What observable behaviour would change if the goal were achieved. What would
   change if it failed.
3. **Metric.** How that signal becomes a number: definition, unit, window, population.

Write all three down. Most measurement failures are visible at the signal step, where the
team cannot name a behaviour that would change.

## HEART

For a feature or an experience, pick the two or three categories that matter and skip the
rest. Filling in all five is a sign you have not chosen.

| Category | Measures | Typical metric |
|---|---|---|
| Happiness | Attitude | Satisfaction after a task, top-2-box, not a mean |
| Engagement | Depth of use | Actions per active user per week |
| Adoption | New users of the feature | Share of eligible users who used it in 30 days |
| Retention | Users who come back | Share of last period's users active this period |
| Task success | Efficiency and completion | Completion rate, time on task, error rate |

Adoption and retention need a defined eligible population, or they measure the mix.

## North Star

One metric representing the value customers get, decomposed into three to five inputs a
team can actually move.

**Tests for a real north star:**
- Can it go down if you do a bad job?
- Would a customer recognise it as something good happening to them?
- Can a team move it within a quarter?
- Does it lead revenue rather than restate it?

Revenue fails the second and fourth. Logins fail the second. Page views fail all four.

**Example structure:** north star "weekly orders fulfilled on time", inputs: merchants
active this week, orders per active merchant, on-time rate, repeat rate.

## Guardrails

Every primary metric needs two or three guardrails: things that must not get worse while
you optimise the primary. Without them, optimisation finds the shortcut.

| Optimising | Guardrail |
|---|---|
| Signup conversion | 30-day retention of new signups, support tickets per signup |
| Engagement | Uninstall rate, opt-out rate, complaints |
| Revenue per user | Churn, refund rate, satisfaction |
| Speed of a flow | Error rate, task success, rework |
| Notification volume | Opt-out rate, next-week retention |

## Counter-metrics and the mix problem

Any rate can be improved by changing the denominator. Conversion rate rises if you turn off
your cheapest traffic. Always report the rate **and** the volume, and check the mix before
crediting a rate change to a product change.

## Leading and lagging

Lagging metrics (revenue, churn, LTV) confirm; they cannot steer inside a quarter. Find the
leading indicator: the early behaviour that predicts the lagging outcome.

**How to find one properly:** take a cohort with known outcomes, test candidate early
behaviours for their correlation with the outcome, then check the relationship holds in a
later cohort. The result is a predictor, not a lever. Pushing users into the behaviour does
not automatically produce the outcome, because the behaviour was a symptom of the users who
were going to succeed anyway. Only an experiment tells you whether it is causal, and this is
the single most common analytics error in product teams.

## Definitions

Every metric needs a written definition, and this is what stops two teams reporting
different numbers for the same thing.

```
METRIC: weekly active merchant
DEFINITION: A merchant account that recorded at least one completed order in a rolling
            7-day window ending Sunday 23:59 in the merchant's local timezone.
POPULATION: Accounts with status = active. Excludes internal test accounts (flag
            is_internal), accounts created in the last 24 hours, and accounts in trial.
WINDOW: Rolling 7 days, computed daily.
SOURCE: orders table, event order_completed.
KNOWN ISSUES: Multi-branch merchants have one account per branch, so a chain of five
            counts as five. Changed 2026-02: cancelled orders no longer count.
OWNER: [name]
```

The "known issues" and "changed" lines are what make a year-old chart readable.

## Instrumentation

A discovery question you cannot answer because the event does not exist is not a research
problem, it is a backlog item. Name it as such.

**Minimum event set for a new feature:** exposed (saw it), engaged (interacted), completed
(reached the intended outcome), failed (with a reason), abandoned (left mid-flow). With
properties for segment, entry point, and variant.

`exposed` is the one teams skip, and without it adoption is unmeasurable because you cannot
tell the difference between "nobody wanted it" and "nobody saw it".
