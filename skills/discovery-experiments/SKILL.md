---
name: discovery-experiments
description: Use when deciding whether to build something, when an idea needs testing before commitment, when mapping assumptions or risks behind a solution, when designing an A/B test or any other experiment, when a test needs a success threshold, when analysing whether a change caused a result, or when a fake door, concierge, Wizard of Oz or pricing test is being planned.
---

# Discovery experiments

## Core principle

An experiment exists to change a belief. Before designing one, write the threshold that
would change yours, and write it before you see any data. A test whose success criterion is
decided afterwards is not a test, it is a search for a number that supports the plan.

Second principle: **test the riskiest assumption with the cheapest method that would
actually move your belief.** Not the easiest assumption. Not the most impressive method.

## The sequence

```
solution  →  assumptions  →  map by importance x evidence  →  pick top-right
          →  choose cheapest sufficient test  →  set threshold BEFORE running
          →  run  →  read honestly  →  record what changed
```

Skipping the mapping step is why teams test the thing that is easy to test.

## Step 1: surface the assumptions

For any solution, list every statement that must be true for it to work. Five categories
(Cagan's four risks plus Torres's ethical):

| Category | The question |
|---|---|
| **Desirability / value** | Do they want it enough to change behaviour? |
| **Usability** | Can they work out how to use it? |
| **Feasibility** | Can we build it, at acceptable cost and performance? |
| **Viability** | Does the business work: cost to serve, price, channel, legal, support? |
| **Ethical** | Could this harm someone, and would we defend it in public? |

**Write each as a falsifiable statement, not a topic.** "Pricing" is a topic. "Merchants
will pay 5 percent of order value for this" is an assumption you can test.

Value risk is the largest in almost every case, and it is the one teams test last because
it is the least comfortable.

## Step 2: map them

Two axes: **importance** (does the solution collapse if this is false?) against **evidence**
(how much do we already have?).

```
  high  |  KNOWN RISK        |  TEST THESE FIRST  |
 impor- |  monitor           |  top-right quadrant|
 tance  |--------------------|--------------------|
        |  ignore            |  interesting, not  |
  low   |                    |  urgent            |
        +--------------------+--------------------+
           high evidence         low evidence
```

Only the top-right quadrant gets tested. Everything else is noted and left alone.
Full protocol in `references/assumption-mapping.md`.

## Step 3: choose the test

Pick the cheapest method that would change your belief, from
`../product-discovery/references/02-method-index.md`. The runbooks for actually executing
each one are in `references/experiment-library.md`.

**Two tests before committing:**
- *Cheapness test:* if a positive result would not raise your confidence and a negative one
  would not lower it, the method is too weak. Move one rung up the evidence ladder.
- *Extravagance test:* if existing data could settle it in two hours, do that first.

## Step 4: set the threshold before running

```
We believe:   Merchants will pay a 5% commission for guaranteed same-day delivery.
We will:      Offer it at 5% to the next 60 merchants who open the delivery screen.
We measure:   Share who accept and complete at least one paid delivery within 14 days.
We are right if:  at least 12 of 60 accept AND at least 8 complete a paid delivery.
We are wrong if:  fewer than 5 accept.
In between:   inconclusive. We will run a second round at 3% before deciding.
Decided on:   2026-04-02, before any data was collected.
```

**The "in between" band is what makes the test honest.** Without it, every result becomes
a success. Derive the threshold from the business case: what acceptance rate would make
this worth building?

## Step 5: read it honestly

- Report the number, the interval, and the threshold you set in advance
- A result inside the inconclusive band is inconclusive. Say so
- A negative result is a finding, and the most valuable kind, because it prevents spend
- Check the sample ratio, the guardrails, and the stability of the effect over time
- Publish the null with the same care as a positive

## Step 6: record what changed

A learning card (`../product-discovery/templates/learning-card.md`): what we believed, what we observed, what we
learned, what we will do. Then update the opportunity solution tree. A failed solution stays
on the tree marked tested-and-failed with the date, which is what stops it being reproposed
in six months.

## Causal designs

| Situation | Design |
|---|---|
| Can randomise, enough traffic | Controlled experiment |
| Users interfere with each other | Switchback, cluster or geo randomisation |
| Cannot randomise, rollout already happened | Difference-in-differences, interrupted time series, or synthetic control. Label quasi-experimental and state the identifying assumption |
| Cannot randomise, no control exists | You cannot answer causally. Give the associational read plus the competing explanations |
| Cumulative effect of a programme | Persistent holdout, 1-10 percent |
| Everyone must eventually receive it (clinical, public service, internal rollout) | Stepped wedge, randomised crossover order |
| Showing the output carries real risk | Shadow mode first, then a controlled rollout |

Design detail and analysis in `references/experiment-design.md`. Calculations in
`../discovery-quant/scripts/`.

## Ethics

Non-negotiable. `references/ethics-and-consent.md`. In short: no test takes real money
without delivering or refunding, no test creates an obligation the user did not choose, no
deceptive test runs without an honest close, and anything that could cause real harm gets
reviewed before it runs.

## Read next

| File | For |
|---|---|
| `references/assumption-mapping.md` | Surfacing and prioritising assumptions |
| `references/experiment-library.md` | Runbooks: how to actually execute each test |
| `references/experiment-design.md` | Randomisation, power, thresholds, quasi-experiments, validity |
| `references/ethics-and-consent.md` | What is and is not acceptable to run on people |

## Red flags

- The success threshold was set after the data arrived
- One solution being "tested" with nothing to compare against
- A fake door with no honest message on the other side
- A test that cannot come back negative
- "Statistically significant" with no effect size or interval
- A test read before the sample ratio check
- An experiment stopped on the day it looked good
- The primary metric was chosen from the results
- A quasi-experiment presented with the confidence of a randomised one
