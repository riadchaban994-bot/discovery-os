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

## Metric models outside consumer software

The HEART and North Star guidance above assumes a voluntary user inside a live digital
product that emits a demand signal. Strip that assumption and the defaults mislead. Pick the
model for your context before designing anything, and cross-check the market row in
`../product-discovery/references/01-intake-and-routing.md` Step 3a.

### Captive users (internal tools, mandated systems, statutory services)

**Adoption is meaningless.** They cannot leave, so usage measures the mandate, not the
value. Reporting mandated usage as engagement is the most common measurement error in
internal product work.

Measure **task cost** instead:

| Metric | Why |
|---|---|
| Time to complete the task, median and p90 | The p90 is where the pain lives |
| Error and rework rate | Errors are paid for twice, once by the user and once downstream |
| Rejection and resubmission rate | Measures whether the rules are legible |
| Help-desk contacts per hundred transactions | The clearest proxy for confusion, and already instrumented |
| Hours the receiving team spends correcting | Usually the largest hidden cost, and the one finance cares about |
| **Shadow-process indicator** | What people do in a spreadsheet or a chat group instead. The most honest signal a captive tool emits |

**The business case** is fully-loaded minutes times frequency times headcount. That is a hard
number finance accepts, and it does not require a price or an acquisition cost, neither of
which exists here.

**Before coding any complaint corpus, separate policy pain from tool pain.** In expense,
procurement, HR and compliance systems a large share of complaints are about a rule owned by
Finance, Audit or Legal that the product team cannot change. Mixing them produces a backlog
of things you are not allowed to fix, and it discredits the research.

### Marketplaces and two-sided products

Single-sided retention analysis is actively misleading here. A retention curve for a supplier
who never received a match is not a retention finding.

| Metric | Why |
|---|---|
| Supply-to-demand ratio, and jobs per supplier | Check before any product hypothesis. Saturation is a demand problem no retention work fixes |
| Distribution of matches across suppliers | If the top decile takes most of the work, the rest churn structurally |
| Time to first match, and share with at least one match per period | The single best predictor of supply-side retention |
| Retention **conditioned on having received a match** | The only retention number that means anything |
| Match rate, fill rate, take rate | The system's health |

**Segment by the unit of liquidity**, never by platform or device. Language pair, city,
category, vehicle class, skill. Two liquidity pools are two marketplaces, and aggregating
them produces a Simpson's paradox by construction.

**Every experiment needs a metric on each side and a joint overall evaluation criterion.** A
change that spreads work more evenly to help supply retention usually costs the demand side
speed or quality, and a one-sided read will call it a win.

### Clinical and safety-critical

Clinical mandates are captive, so the task-cost model above applies. Add the measures the
field already uses, because inventing your own here is both slower and less credible with
the clinicians whose behaviour you are trying to change.

| Metric | Why |
|---|---|
| Alert or interruption burden per clinician per shift | The exposure. The denominator matters more than the rate |
| Override or dismissal rate, by alert type | The blunt signal that an alert is not earning its interruption |
| Appropriateness-adjusted override | Overriding a bad alert is correct behaviour. Splitting appropriate from inappropriate overrides is the whole analysis |
| Time to dismiss | Sub-second dismissal means it was never read |
| Effect on the downstream clinical action | The only outcome that matters, and the one that needs a design, not a dashboard |

**The trap:** optimising the override rate by suppressing alerts. That improves the metric
and can harm patients. Any alert-burden work needs a safety guardrail on missed events, and a
design that can detect one.

### Public services

**The outcome is a duty against a published standard**, not growth. Time to resolve, repeat
contact rate, first-contact resolution, and **equity of service across districts or
demographics**, which is a metric a commercial product never has and a public one is
accountable for.

**Ground truth does not come from users.** Reports received measures reporting propensity.
Incidence comes from the operational source: inspection crews, contractors, sensors, case
records. Optimising on reports alone systematically serves the districts that already
complain and under-serves the ones that do not.

### Channel-sold and hardware

Sell-in (units shipped to the channel) is not sell-through (units bought by end customers),
and the gap is inventory that will come back. Track both, plus channel margin, stocking
depth, return and RMA rate, attach rate for consumables, and time from design win to first
production order.

**The discovery corpus for a physical product** is not tickets and reviews. It is warranty
and RMA claims with their reason codes, field service reports, installed-base telemetry where
the device reports home, distributor sell-through, and the alpha or field-trial programme
with named sites. RMA reason codes in particular are a free, structured, honest record of
what fails in the real world, and almost nobody in product reads them.

---

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
