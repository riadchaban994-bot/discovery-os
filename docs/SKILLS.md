# The seven skills

One commander and six specialists. The commander routes; the specialists execute. You can
invoke any of them directly, but describing your situation to the commander is usually
faster because the routing is the hard part.

---

## `product-discovery`  (the commander)

**Triggers on:** deciding what to build or whether to build it, an idea that needs
evidence, a metric that moved, research that needs planning or synthesising, sizing or
prioritising, auditing a document, setting up a discovery practice.

**What it does.** Finds the real question behind the request, inventories what evidence you
actually have, and routes to the cheapest method that can answer it. It carries the seventeen
rules that bind every other skill, and it calibrates the size of the answer to the size of
the decision: a two-line question gets two lines.

**Six modes.** State the mode, get the matching output.

| Mode | Use for | You get |
|---|---|---|
| `ASSESS` | default. "What should I do about X" | Diagnosis, chosen method, what it will not tell you, cost, next action |
| `RUN` | "Write the guide", "design the test" | The artifact, no preamble |
| `SYNTHESISE` | raw data handed over | Coded evidence, themes, confidence per claim |
| `CHALLENGE` | "Poke holes in this" | Red team ranked by how much each finding changes the answer |
| `AUDIT` | a PRD or business case | Claim-by-claim evidence grading and the cheapest gap-closers |
| `TEACH` | "Explain X" | The framework with its real source, what it is for, what it is not for |

**The intake.** Five slots: the decision, the outcome, the customer, the evidence on hand,
the constraint. It infers what it can, shows you the inference, and asks at most three
questions. If the decision slot cannot be filled it stops and fills that first, because
everything routes off it.

**The evidence inventory** drives the routing. Six values, guessed from context and
corrected by you:

| Field | Values |
|---|---|
| `customer_access` | none / slow / scheduled / on demand |
| `qual_data` | none / raw / coded |
| `instrumentation` | none / partial events / full analytics / experimentation platform |
| `volume` | under 100 per week / 100 to 1k / 1k to 10k / over 10k |
| `product_state` | concept / prototype / live and small / live at scale |
| `market` | B2C mass / B2B SMB / B2B enterprise / channel-sold / marketplace / internal or captive / government / clinical or regulated |

`market` carries a full override per value, because it changes what counts as evidence and
what a good metric looks like, not just the sample size. Nine rows: B2C mass, B2B SMB, B2B
enterprise, channel-sold, marketplace, internal or captive, government, clinical or
regulated. Read the row for yours before reading any method card.

**Inside it:**

| File | What |
|---|---|
| `references/00-constitution.md` | The seventeen rules, with the enforcement behaviour and exact wording for each |
| `references/01-intake-and-routing.md` | Fifteen canonical questions, each with a decision table, plus the overrides that veto a method |
| `references/02-method-index.md` | 77 method cards: what it answers, what it needs, how it runs, the failure mode that makes it lie to you, and where it applies, the contexts in which it must not be run at all |
| `references/03-evidence-ledger.md` | The L0 to L7 ladder, the four confidence levels, provenance tags, the AUDIT protocol |
| `references/04-frameworks-canon.md` | 45+ frameworks with real sources, and what each is **not** for |
| `references/05-anti-patterns.md` | 35 ways discovery produces confident nonsense, and the CHALLENGE protocol |
| `references/06-artifacts.md` | Every deliverable and its quality bar |
| `references/07-ai-boundary.md` | Per activity: what AI may do, must never do, and what a human owns |
| `templates/` | Thirteen fill-in artifacts |

---

## `discovery-interviewing`

**Triggers on:** planning or running customer interviews, recruiting, moderating, an
interview that produced nothing useful, practising before a real session, writing one up.

**Three modes, kept strictly separate.**

| Mode | Participant | Usable as evidence |
|---|---|---|
| Design | none | The guide itself |
| Moderate | a real person | Yes |
| Rehearse | model-simulated | **Never.** Stamped `SYNTHETIC - NOT EVIDENCE` |

**AI-moderated interviews with real participants** are supported under a strict protocol:
disclosure before the session, recorded consent, a fixed protocol, a human reading the full
transcript before synthesis, and the method's limits stated in the readout. Good for
structured collection at volume and for languages your team does not speak. Poor for
exploratory or sensitive work, and it says so.

**Covers:** seven interview types (story-based, JTBD switch, contextual inquiry, churn,
solution feedback, expert, stakeholder), the question bank with banned forms and their
replacements, recruiting as a pipeline rather than a scramble, screener design, incentives,
cross-language and cross-cultural adaptation, and twelve moderator errors with the recovery
for each.

**The single most useful line in it:** ask about the past, not the future. "Tell me about
the last time you needed a number you did not have" beats "would you use a dashboard" at
every sample size.

---

## `discovery-synthesis`

**Triggers on:** turning raw research into findings, coding transcripts or tickets or sales
calls or reviews, building an opportunity solution tree, deciding whether enough interviews
have been done.

**The pipeline, and you may not skip the middle:**

```
raw sources -> segments -> codes -> categories -> themes -> opportunities -> tree
```

Jumping from raw text to themes is how synthesis becomes storytelling. The middle is what
makes a finding auditable and what makes disconfirming evidence visible.

**Saturation is measured, not felt.** New codes per source, plotted, per segment.
`qual_saturation.py` computes it and applies a stopping rule. If the second half of your
corpus produces more new codes than the first, it tells you that you are looking at two
segments, not one.

**AI-assisted coding is allowed and is the biggest real win in the whole system**, because
it makes coding 400 support tickets possible. Under rules: a human approves the codebook
first, every applied code cites the exact span justifying it, new codes are proposed and
never adopted silently, and a human recodes a 15 to 20 percent sample blind with agreement
computed.

**Covers:** codebook format with inclusion **and** exclusion rules, thematic analysis after
Braun and Clarke, inter-coder agreement, opportunity solution trees, JTBD forces and
timeline analysis, experience maps versus journey maps versus service blueprints, and nine
quality gates that block a readout.

---

## `discovery-quant`

**Triggers on:** a metric moved and nobody knows why, designing what to measure, funnels,
cohorts, retention, churn, how many users a test needs, analysing a survey, checking a
number before anyone acts on it.

**The diagnostic sequence, in order, and step 5 is not step 1:**

1. Did it actually move? Tracking release, bot traffic, definition change, timezone,
   backfill. A large share of investigated movements are measurement artefacts
2. Where is it concentrated? Segment decomposition, plus a Simpson's paradox check
3. What changed at the same time? The release and campaign log
4. Which transition changed? Funnel decomposition on the affected slice
5. **Now** ask people, recruited from the affected slice

**Five runnable scripts.** See [SCRIPTS.md](SCRIPTS.md).

**Covers:** goals-signals-metrics and HEART, North Star design and its four tests, guardrail
metrics, the leading-indicator trap (a predictor is not a lever), metric definitions that
survive a year, funnels, cohort retention and what each curve shape means, survival
analysis and what churn timing tells you, behavioural segmentation, feature adoption in
three dimensions, existing-behaviour mining, survey instrument choice and scoring, and
seventeen statistical guardrails.

**The one it will not let you skip:** retention curve before any product-market-fit claim.
If the curve does not flatten, no survey rescues the conclusion.

---

## `discovery-experiments`

**Triggers on:** deciding whether to build, testing an idea before commitment, mapping
assumptions, designing an A/B test or any other test, setting a success threshold,
analysing whether a change caused a result, planning a fake door or concierge or pricing
test.

**The sequence:**

```
solution -> assumptions -> map by importance x evidence -> take the top-right quadrant
         -> cheapest sufficient method -> threshold set BEFORE running -> run -> read honestly
```

**Five risk categories** (Cagan's four plus Torres's ethical): desirability, usability,
feasibility, viability, ethical. Each assumption written as a falsifiable statement.
"Pricing" is a topic; "merchants will pay 5 percent of order value" is an assumption.

**The threshold rule.** Success, failure, **and the inconclusive band between them**, all
written before any data exists. The inconclusive band is what stops every result becoming a
success.

**Covers:** assumption surfacing prompts per category, the importance-against-evidence map,
runbooks for the tests that matter (painted door, demand landing page, concierge, Wizard of
Oz, pre-sale and letter of intent, comparison prototype, moderated usability, controlled
experiment, holdout, technical spike) each with setup, thresholds, duration and the mistake
that invalidates it, randomisation units and the interference test, quasi-experimental
designs with their identifying assumptions, eleven threats to validity, and the ethics of
testing on people.

**On holdouts:** a promotion or CRM programme without one cannot report incrementality.
Redemption is not incrementality. Many redeemers would have converted anyway.

---

## `discovery-prototyping`

**Triggers on:** turning an idea into something people can react to, choosing fidelity,
building a clickable prototype or fake door or Wizard of Oz console, preparing to test a
design.

**Fidelity is four independent dials**, not one: visual, content, interaction, data. Choose
each from the question. Content fidelity is high in almost every row of that table; visual
fidelity rarely is. Real words and real numbers matter more than polish, and polish buys
you politeness rather than information.

**Three working artifacts** in `skills/discovery-prototyping/assets/`, self-contained, no
build step:

- **`clickable-prototype.html`** logs every hotspot click and every **dead click**, task
  time, and outcome, then exports a CSV. Dead clicks are the strongest usability signal
  there is: a participant telling you where they expected something to be. Edit two objects
  at the top of the file to author it
- **`fake-door.html`** with the honest close firing on click, an intent capture, and the
  threshold set in the file before you run
- **`woz-console.html`**, a participant pane and an operator pane, with enforced latency so
  the operator cannot answer faster than the real system would

**Covers:** twelve prototype types with what each proves and cannot prove, the fidelity
ladder and the cost of getting it wrong in each direction, throwaway versus foundation
decided before you build, the testing protocol, severity rating, and comparison testing.

**The line it holds:** a well-received prototype demonstrates comprehension and politeness.
It is not demand evidence. Demand needs a commitment step, and this is the single most
over-interpreted result in product discovery.

---

## `discovery-ops`

**Triggers on:** setting up a discovery practice, research that keeps being a project
instead of a habit, recruiting as the bottleneck, past research nobody can find, findings
not reaching stakeholders, automating the recurring parts.

**Discovery fails operationally far more often than intellectually.** Teams know what to do.
They cannot hold a cadence, recruit reliably, find last quarter's study, or get a finding to
the person who needs it.

**Covers:** the weekly cadence and an eight-week plan for building the habit one step at a
time (start with the calendar slot, not the tooling), recruiting as a pipeline with health
metrics, research repository structure organised by outcome rather than by study, the living
one-page summary that people actually read, decay dates per claim type, eight automation
recipes and the boundary that governs them, the weekly digest format, the readout, and what
to do when a stakeholder disagrees with the evidence.

**The section nobody writes and everybody needs:** "Ruled out". What you tested, what came
back negative, and the date. It is what stops the same idea being reproposed every six
months by someone new, and it is the clearest evidence that discovery saves money.
