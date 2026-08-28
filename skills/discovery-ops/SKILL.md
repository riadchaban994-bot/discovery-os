---
name: discovery-ops
description: Use when setting up a discovery practice, when research keeps being a one-off project instead of a habit, when recruiting participants is the bottleneck, when past research cannot be found or gets redone, when discovery findings are not reaching stakeholders, or when scheduling and automating the recurring parts of research.
---

# Discovery ops

## Core principle

Discovery fails operationally far more often than it fails intellectually. Teams know what
to do. They cannot hold a cadence, cannot recruit reliably, cannot find last quarter's
study, and cannot get a finding in front of the person who needs it.

The fix is boring infrastructure: a standing slot, an automated recruiting pipeline, a
repository with a naming convention, and a weekly one-page summary. Boring infrastructure
is what turns discovery from a project into a habit.

## The weekly cadence

The minimum viable practice, and the thing to build first.

| When | What | Who | Time |
|---|---|---|---|
| Weekly, fixed slot | One or two customer conversations | Product trio, all present | 60-90 min |
| Immediately after | Interview snapshots | Whoever was in the room | 30 min |
| Weekly | Update the opportunity solution tree | Trio | 30 min |
| Weekly | One assumption test running, always | Trio | varies |
| Fortnightly | Review the test queue and the evidence ledger | Trio | 30 min |
| Monthly | One-page summary per outcome, published | Product | 60 min |
| Quarterly | What have we ruled out, and what has decayed | Trio | 90 min |

**The trio attends together** (Torres). Discovery that one person does and reports back does
not transfer; the engineer who heard the customer say it builds a different thing from the
engineer who read it in a document.

**Protect the slot.** If nobody is booked, use it for synthesis. Never give it back, because
a slot given back once is gone.

## Recruiting as a pipeline

Recruiting is the constraint. Treat it as a pipeline with a target, not as a scramble
before each study.

```
in-product prompt  ─┐
email segment      ─┼─► booking link ─► confirmed ─► completed ─► follow-up pool
support follow-up  ─┤        (over-recruit 30%)                    (re-contactable)
referrals from     ─┘
sessions
```

**Target: next week always booked.** The pipeline is healthy when you never have to think
about it.

**The single highest-leverage build:** an in-product prompt on the screen where the relevant
behaviour happens, linked to a booking page. Build it once and recruiting stops being work.
It biases toward active users, so keep one other channel for everyone else.

**Ask every participant** who else you should talk to. That referral question is a recruiting
engine that costs nothing.

Detail in `references/cadence-and-automation.md`.

## Research repository

The purpose is not storage. It is stopping the same study being run twice and letting
someone six months from now audit a claim.

**Structure:** one folder per outcome, not per study. Inside: the living one-page summary,
the evidence ledger, snapshots by participant code, raw data with retention dates, decision
records.

**Naming:** `YYYY-MM-DD_type_topic_segment`. Sorts chronologically, searches by any part.

**The living summary is the artifact people actually read.** Everything else is the audit
trail behind it. Detail in `references/research-repository.md`.

**Decay.** Every claim has a recheck date. Behavioural claims 6-12 months, pricing 6,
competitive 3. An undated claim in a strategy document is a liability.

## What to automate

Automate the parts that are mechanical and skipped when busy. Do not automate judgement.

| Safe to automate | Never automate |
|---|---|
| Recruiting outreach and scheduling | Deciding who to talk to |
| Transcription and speaker labelling | Deciding what a quote means |
| Applying an approved codebook at scale | Writing the codebook |
| Computing saturation, frequency, agreement | Deciding when to stop |
| Monitoring metric movements and alerting | Diagnosing why |
| Reminders: snapshot due, claim decayed, test running with no threshold | The threshold |
| Assembling the weekly digest from existing artifacts | Its conclusions |
| Flagging unsourced claims in a document | Whether the claim is true |

Concrete recipes, including scheduled agent jobs and folder-watch intake, in
`references/cadence-and-automation.md`.

## Stakeholder communication

Findings that do not reach a decision-maker have not been produced. `references/stakeholder-comms.md`
covers the weekly digest, the readout, handling a stakeholder who disagrees with the
evidence, and the two-sentence format that gets a finding into a decision.

## Output

Terse by default. One line per point, not a paragraph per point. Prose only where a number
would be misread without a sentence of context.

No preamble, no restating the request, no closing summary of what you just said. Drop any
section that would be empty rather than filling it.

Ask when a missing answer changes the recommendation, not otherwise. Use the
`AskUserQuestion` tool where the runtime has it and the choice is a real fork between two to
four known options, recommendation first. Ask in plain numbered text for open-ended facts
only the user holds. Ask nothing where a sensible default exists: state the assumption
inline and move on.

Full contract and word ceilings: `../product-discovery/SKILL.md`, Output contract.

## Read next

| File | For |
|---|---|
| `references/cadence-and-automation.md` | Building the habit, the pipeline, and the automation |
| `references/research-repository.md` | Structure, naming, decay, and the living summary |
| `references/stakeholder-comms.md` | Getting findings into decisions |

## Red flags

- Discovery happens when there is time
- Recruiting starts when a study is planned
- Only one person attends the sessions
- The same question was researched last year and nobody knew
- Findings live in a slide deck nobody can search
- No claim in the strategy document has a date
- The test queue is empty and nobody noticed
- A research repository with more than fifty documents and no summary
