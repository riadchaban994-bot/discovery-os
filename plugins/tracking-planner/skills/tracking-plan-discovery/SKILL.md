---
name: tracking-plan-discovery
description: Walk any app hands-on and build or update a real product-analytics tracking plan from what you actually see. Use this whenever someone needs an event taxonomy, a tracking plan, a measurement plan, an analytics spec, an event dictionary, instrumentation for GA4 / Firebase / Amplitude / Mixpanel / Segment / PostHog, or wants to audit or extend tracking that already exists. Use it when the ask is "what should we track", "our analytics are broken", "we have no funnel data", "design the events for this feature", "map the user journeys", or "the dev team needs a spec". It drives an Android emulator, an iOS simulator, a browser or a Figma file, screenshots every surface, groups parameters into reusable attribute packs, grades every event by how strong the evidence for it actually is, and ships a phased, buildable Excel workbook with embedded screenshots. Works for any app in any industry. Reach for it even when the person only says "events" or "instrumentation" and has not used the words tracking plan.
---

# Tracking plan discovery

Most tracking plans are written from memory in a document, and they are wrong in ways nobody notices until the data
arrives months later. This skill exists to produce one from evidence instead: open the app, walk every journey, screenshot
every surface, and write the plan from what is actually there.

The single idea that makes this work: **be honest about what you have seen.** A plan that says "I watched this fire" for
some events and "I designed this, confirm it" for others is far more useful than one that speaks with uniform confidence
and is quietly fictional in half its rows.

## What you produce

A multi-tab Excel workbook, built by `scripts/build_workbook.py` from a single JSON file. Sections you
do not supply are simply skipped, so the same script serves a six-event first pass and a mature plan:

| Tab | What it is |
|---|---|
| Read me | Architecture, conventions, identity, privacy, platform limits, rollout |
| **Phase 1 build ask** | **The deliverable.** Only the events to build now, with source, evidence, screens, work estimate, parameters |
| Roadmap | Phase 2 and 3, what earns each, and what was cut with the reason |
| Attribute packs | Every parameter: required/conditional/optional, type, values, notes |
| All events | The full target state, phased and evidence-graded |
| User properties | Persistent attributes and their update rules |
| Custom definitions | What to register in the analytics tool before shipping |
| Key events & audiences | Conversions and standing segments |
| Journey funnels | Ordered event sequences per KPI, with measured baselines |
| Gaps closed | Each known problem mapped to the event that fixes it |
| Journey map | Screen-by-screen record of the walkthrough |
| Confirm before build | What is designed rather than observed, and what to ask engineering |
| Screen gallery | Every screenshot, embedded, with reverse lookup (omitted when there are no screenshots) |

## The workflow

### 1. Establish what matters before you look at anything

Ask, or find in the codebase or documents: what does the business get paid on, what is already broken, and what leaks are
already known. Without this you will produce a taxonomy instead of a plan, and a taxonomy is a document nobody builds.

If the user has an existing tracking plan, read it first. Your job then is a delta, not a rewrite.

**Ask which analytics tool they use before you design anything.** Read `references/platforms.md`.
The destination changes real decisions: on GA4 a hard 25-parameter cap and a 50-dimension quota make
consolidation essential and force activation into its own event, while on Amplitude or Mixpanel
billing is by volume so the pressure is on event count instead, and group analytics become available.
Designing GA4 discipline into an Amplitude plan is not a small error. Put the destination in the plan
as `meta.destination` so the validator checks against the right limits rather than defaulting to GA4.

### 2. Walk the app

Read `references/app-walkthrough.md`. It has the universal journey checklist that applies to any product, the platform
mechanics for driving an Android emulator, iOS simulator, browser or Figma file, and the specific traps that produced
wrong plans before.

Screenshot every distinct surface into `tracking_plan_screens/` as `SCR-nn_what-it-shows.png`, numbered in journey order.
These are the evidence, and later the workbook embeds them.

Three rules while walking:

- **Never transact.** No real orders, no completed payments, no credentials entered on someone's behalf. Walk to the
  commit button and stop. Anything past it gets graded UNVERIFIABLE and declared, not guessed.
- **Exercise the branches, not just the happy path.** A picker you opened but never used tells you nothing about what it
  emits. Empty states, error states, blocked states and signed-out states are where the interesting events live.
- **Record what the app actually says.** Its vocabulary, not yours. If the app says "Online" do not write "open".

**If there is no app to walk** (no build yet, no environment, a design still in Figma, or a client who
cannot give you access), say so plainly and carry on. A plan written from a description is worth
having; a plan that pretends it was written from an app is not. In that case:

- Grade every event INFERRED, or UNVERIFIABLE where it needs a transaction or an unlaunched feature.
  Nothing is OBSERVED, because nothing was observed.
- Say it on tab 1 and make it the first entry in "Confirm before build": the first ask is a build or
  a staging environment to walk.
- Leave the journey map stating that no walkthrough happened rather than inventing screens for it.

The validator warns when no event is graded OBSERVED, which is the correct behaviour rather than
something to suppress.

### 3. Design the taxonomy

Read `references/methodology.md` for the full method, and `references/pack-library.md` for a starter pack library with
realistic sample values by industry, so you are adapting a taxonomy rather than inventing one.

The moves that matter most:

**Group parameters into attribute packs.** Define reusable bundles once and have events attach them. One definition,
attached everywhere, changed in one place.

**Consolidate sibling events.** Six order-status events become one event with a status parameter, which turns six backend
integration points into one. This is where a 120-event plan becomes a 79-event plan without losing a single answer. Some
merges are forbidden, and the methodology file says which.

**Grade every event by evidence.** OBSERVED, PARTIAL, INFERRED or UNVERIFIABLE. This is not decoration. It is what stops
a design being built as a specification.

**Mark every parameter** required, conditional or optional, and every event FE, BE, FE + BE or SDK, so the mobile ticket
and the backend ticket separate cleanly.

### 4. Phase it

Nobody ships 120 events. Phase 1 admits an event only if it fixes something already broken, or is required for a
contracted KPI, or is the only measurement point of a leak already costing money.

Do not cut to the theoretical minimum. A Phase 1 so small the team must immediately reopen it is a worse outcome than one
slightly larger that stands on its own. On the engagement this method came from, a 21-event Phase 1 was rejected as too
thin and rebalanced to 50.

### 5. Build the workbook

Write the plan as JSON matching `assets/plan_schema.json`, then:

```bash
python3 scripts/build_workbook.py plan.json
```

It handles the tabs, the styling, the evidence colour-coding, the embedded screenshots with internal links, the row
heights and the print setup. Derived tables (registered dimensions, user-property lists) are generated from the source
data rather than hand-maintained, because a hand-kept copy drifts and the drift is invisible.

### 6. Verify before you hand it over

Read `references/qa-gates.md` and run:

```bash
python3 scripts/validate_plan.py plan.json --platform ga4
```

It reads `meta.destination` from the plan when you do not pass `--platform`, and honours any
account-level quotas you state in `meta.limits`. It separates blockers from warnings and exits
non-zero on blockers, so it drops straight into CI.

Then **render the workbook and look at it**:

```bash
soffice --headless --convert-to pdf --outdir _qa workbook.xlsx
pdftoppm -jpeg -r 100 _qa/workbook.pdf _qa/p
```

Reading the rendered pages catches a whole class of defect that source inspection cannot: a value beginning with `=`
silently becomes a formula error, columns wrap mid-word, a repeated header stamps the wrong labels on a second table.
This is not optional polish. It is the step that finds the errors.

## Updating an existing plan

The same pipeline, with two differences. Load the existing plan as the base and produce an explicit delta: what to add,
what to merge, what to retire, what to reword. And re-walk the app rather than trusting the document, because the app has
moved since it was written. Every row you leave untouched still needs an evidence grade, and "it was in the old plan" is
not evidence.

## Working with an adversary

Before handover, have an independent reviewer try to **refute** the plan rather than confirm it. Ask them to prove that a
named KPI cannot be computed, to find parameters whose values were invented, and to find events that reference names that
no longer exist after merges. On the engagement this method came from, that pass found roughly 40 invented enum values and
two entire tabs still pointing at deleted events. Confirmation bias is the default failure mode of anyone who just spent a
day building something.

## What good looks like

The plan is finished when an engineer can build from it without asking you a question, an analyst can compute every named
KPI from it, and a sceptic reading it can tell instantly which parts are fact and which are proposal. If any of those
three fails, it is not finished, however polished it looks.
