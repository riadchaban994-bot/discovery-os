# Tracking Planner

**Tracking plans written from evidence, not from memory.**

A skill for Claude Code, Codex, Copilot CLI, Gemini CLI or any agent that reads
skills. Point it at your app and it walks every journey hands-on, an Android
emulator, an iOS simulator, a browser or a Figma file, screenshots every surface,
and writes the tracking plan from what is actually there. The output is a phased,
buildable Excel workbook your developers can pick up, with the evidence embedded.

Free, MIT, no accounts, no telemetry. Built as a giveaway for ProductTank Syria,
Damascus, August 2026. Companion to
[Discovery OS](https://github.com/riadchaban994-bot/discovery-os).

## The problem it solves

Most tracking plans are written from memory in a document, and they are wrong in
ways nobody notices until the data arrives months later. Events that fire at the
wrong moment. Enum values nobody has ever seen in the app. A design that reads as
a specification, so engineers build the parts that were made up along with the
parts that were real.

The fix is one idea applied without mercy: be honest about what you have seen.
Every event, and every value inside every parameter, carries an evidence grade.

| Grade | Meaning |
|---|---|
| OBSERVED | Seen firing in the running app, screenshot attached |
| PARTIAL | The surface was seen, at least one branch was not exercised |
| INFERRED | Never seen. Designed from convention or documents |
| UNVERIFIABLE | Needs a real transaction or an unlaunched feature to check |

A plan that says "I watched this fire" for some rows and "I designed this,
confirm it" for others is buildable. One that speaks with uniform confidence is
quietly fictional in half its rows.

## Quick start

### Claude Code

```
/plugin marketplace add riadchaban994-bot/discovery-os
/plugin install tracking-planner@riadchaban
```

Restart. The marketplace is shared with Discovery OS, so if you already added it,
only the second line is needed.

### Any other agent

```
git clone https://github.com/riadchaban994-bot/tracking-planner.git
cp -R tracking-planner/skills/* ~/.claude/skills/   # or ~/.codex/skills/, ~/.agents/skills/
```

### Then try it

> Build a tracking plan for our app. We are on GA4.

You should be asked what the business gets paid on, what is already broken, and
which analytics tool the events land in, before a single event is designed. If
you get a hundred-event taxonomy instead, the skill did not load.

## What it does

1. **Establishes what matters first.** KPIs, known leaks, the destination tool.
   Without that you get a taxonomy, and a taxonomy is a document nobody builds.
2. **Walks the app.** A twelve-journey checklist that applies to any product,
   platform mechanics for adb, the iOS simulator, browsers and Figma, and hard
   safety rules: never transact, never enter credentials, stop at the commit
   button.
3. **Designs the taxonomy.** Parameters grouped into reusable attribute packs,
   sibling events consolidated where the merge is safe (six order-status events
   become one event with a status parameter), every row graded by evidence.
4. **Phases it.** Phase 1 admits an event only if it fixes something already
   broken, computes a contracted KPI, or measures a leak already costing money.
5. **Builds the workbook.** `scripts/build_workbook.py` turns one JSON file into
   a styled multi-tab Excel file, screenshots embedded and internally linked.
6. **Validates before handover.** `scripts/validate_plan.py` checks naming rules,
   parameter budgets and quotas against the real platform limits, catches values
   a spreadsheet would parse as formulas, and separates blockers from warnings.
   It exits non-zero on blockers, so it drops straight into CI.

## What is in the repo

```
skills/tracking-plan-discovery/
  SKILL.md                the workflow
  references/
    methodology.md        the evidence ladder, packs, consolidation, phasing, naming
    app-walkthrough.md    the field playbook for walking any app
    pack-library.md       a starter pack library with per-industry variants
    platforms.md          destination rules: GA4 and Firebase, Amplitude, Mixpanel, PostHog, Segment
    qa-gates.md           eight QA gates and the pre-handover checklist
  scripts/
    build_workbook.py     plan JSON in, Excel workbook out
    validate_plan.py      blockers and warnings before anything ships
  assets/
    plan_schema.json      the plan structure
    example_plan.json     a synthetic worked example
```

## Requirements

Python 3.8+ for the scripts. The validator is standard library only. The workbook
builder needs `openpyxl`, plus `Pillow` if you want screenshots embedded:

```
pip install openpyxl Pillow
```

## What it will not do

It never places a real order, never completes a payment, never enters
credentials, and never submits anything that reaches another human. Everything
past the commit button is graded UNVERIFIABLE and declared, not guessed. A plan
that admits its ceiling is worth building. One that pretends it saw the checkout
is not.

## Uninstall

```
/plugin uninstall tracking-planner@riadchaban
```

Or delete `skills/tracking-plan-discovery/` from wherever you copied it.

## Licence

MIT. Do what you like, keep the notice.
