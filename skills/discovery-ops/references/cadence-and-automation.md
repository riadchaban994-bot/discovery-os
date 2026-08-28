# Cadence and automation

## Building the habit, in order

Do these one at a time. Teams that try to build the whole practice at once build none of it.

**Week 1. Book the slot.** A recurring 90 minutes in the trio's calendar. Even with nobody
to talk to yet. The slot creates the pressure that solves the rest.

**Week 2. Get one conversation.** Any channel: a customer success introduction, an email to
five users, a support follow-up. One is enough to start.

**Week 3. Write the first snapshot.** Within a day. Badly is fine.

**Week 4. Build the recruiting pipeline.** Now that you know it is needed, and now the
in-product prompt has an obvious justification.

**Week 6. Start the opportunity solution tree.** From the first five snapshots, not from a
workshop.

**Week 8. Run the first assumption test.** Small, cheap, with a threshold set in advance.

**Month 3. Publish the first one-page summary.** This is when stakeholders start pulling
rather than you pushing.

**What breaks it:** starting with the tooling, starting with a framework workshop, or
starting with a big study. Start with the slot.

---

## Recruiting pipeline

**Target:** next week is always booked, without anyone having to think about it.

**Health metrics, checked monthly:** sessions completed per month, days from request to
session, no-show rate, share of sessions from each channel, size of the re-contactable pool.

**The in-product prompt.** A small dismissible prompt on the screen where the behaviour
happens, offering a short conversation with an incentive, linked to a booking page. Rules:
never show it twice to the same person inside 90 days, never during a task, never to someone
in an active support ticket, and always make the incentive clear before they click.

**Over-recruit by 30 percent.** `[HEURISTIC]` no-show rates in the twenties are common for consumer
research, higher when unpaid and lower in B2B where a colleague made the introduction.
Track your own; it varies more by recruiting channel than by anything else.

**Confirm 24 hours before**, with a short message from a person.

**Keep a re-contactable pool** of participants who agreed to be approached again, with the
date they were last contacted and what they were asked about. This becomes the fastest
channel you have.

---

## Automation recipes

These assume an AI coding agent with file access and a scheduler. Adapt the mechanism to
whatever you run. The logic is the part that matters.

**1. Transcript intake.** A watched folder. New recording or transcript appears, and the
agent transcribes if needed, speaker-labels, applies the approved codebook, produces a
snapshot draft, and flags every low-confidence code for human review. The human reviews;
the machine never files a code it was not confident about.

**2. Weekly discovery digest.** Scheduled Monday morning. Assembles from artifacts that
already exist: sessions run last week, new codes added, opportunities added or changed,
tests running and their status, claims that decayed, the test queue. Publishes to the team
channel. Reports only what the artifacts say, and never draws conclusions.

**3. Decayed-claim alert.** Scheduled monthly. Reads the evidence ledger, lists claims past
their recheck date, sorted by how many decisions depend on each. Sends a list, not a
narrative.

**4. Unsourced-claim linter.** Runs on any document in the repository. Flags sentences that
make factual claims with no provenance marker, causal verbs on non-experimental results,
percentages with n under 30, and the word "validated". Reports; never edits.

**5. Metric watch.** Scheduled daily. Compares the key metrics against a baseline, alerts on
movement beyond a threshold, and includes the segment breakdown so the first diagnostic step
is already done. Alerts with the measurement checks listed, so nobody starts theorising
before checking whether the movement is real.

**6. Recruiting top-up.** Scheduled weekly. Checks the number of confirmed sessions for the
coming week against the target, and if short, drafts outreach to the next batch from the
re-contactable pool. A human sends it.

**7. Saturation check.** After each coding pass, recompute the saturation curve per segment
and report whether the stopping rule is met.
`../discovery-quant/scripts/qual_saturation.py saturation --csv codes.csv --segment-col segment`

**8. Pre-launch experiment check.** Before any experiment goes live, verify the
pre-registration exists, the primary metric is declared, the threshold is set, the sample
size calculation is attached, and the guardrails are named. Block the launch if any are
missing.

---

## The automation boundary

Every recipe above operates on artifacts a human created or approved. None of them creates
evidence, decides what something means, or closes a question.

**The test before automating anything:** if this ran wrong for a month and nobody noticed,
what would the damage be? Mechanical work, low damage: automate it. Judgement work, high
damage: do not.

**Alert fatigue is a real failure mode.** An automation that fires weekly and is ignored is
worse than none, because it creates the appearance of monitoring. Any alert that has been
ignored three times in a row is either wrong or unnecessary. Fix it or turn it off.
