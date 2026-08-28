# Prototype testing protocol

## Before the session

- Write the one question this test answers, and what result would change the design
- Write the tasks in the **participant's words**, not the interface's. "Find out how much
  you sold today", never "open the sales report"
- Decide the rescue rule and hold to it: no help until the task is genuinely dead
- Pilot with a colleague to catch broken links and confusing task wording. Never spend a
  real participant on a broken prototype
- Prepare the observation sheet, or use the built-in log in
  `assets/clickable-prototype.html`

## Session structure, 45 minutes

| Time | What |
|---|---|
| 0-3 | Consent, framing, no right answers, think aloud, we are testing the design not you |
| 3-10 | Context and the story. Their situation, and the last time they did this activity |
| 10-35 | Tasks, think-aloud, minimal intervention |
| 35-42 | Reactions, comparison across options, what it would replace |
| 42-45 | Anything I should have asked, who else should I talk to |

**The story comes before the prototype, always.** Once they have seen your solution,
everything they say about their needs is contaminated by it.

## During

**Say once, at the start:** "Please think out loud. Tell me what you are looking at, what
you expect to happen, and what you are trying to do. If you get stuck, that is useful, so
keep going as long as you can."

**When they go quiet:** "What are you thinking?" Never "what would you click?"

**When they get stuck:** wait. Count to ten. Then "what are you looking for?" Then wait
again. Rescue only when the task is dead, and record that you rescued.

**When they ask "is this right?":** "There is no right answer. What would you do if I were
not here?"

**When they say they like it:** "What would you use it for?" Then, "Tell me about the last
time you needed that." Enthusiasm without a specific recent situation is politeness.

**Never:** explain how it works, defend a decision, say "you would normally...", or point.

## What to record

| Signal | Meaning |
|---|---|
| **Dead clicks** | They expected something there. The strongest single signal |
| Hesitation over 3 seconds | Unclear affordance or unclear label |
| Wrong path taken confidently | The information scent points the wrong way |
| Back-navigation | The previous screen did not deliver |
| Reading aloud slowly | Comprehension load |
| Asking what a word means | Your jargon |
| Wrong mental model expressed | The most valuable finding, and the hardest to fix |
| Task time | Comparable across participants |
| Success, partial, failed, rescued | The success rate |

## Severity rating

| Level | Definition | Action |
|---|---|---|
| **Critical** | Blocks the task. Cannot proceed | Fix before the next round |
| **Serious** | Task completed with difficulty, or wrong result reached | Fix before release |
| **Minor** | Slowed down or briefly confused | Fix when convenient |
| **Cosmetic** | Noticed, no impact | Backlog |

Rate by **impact and frequency together**. A critical problem seen in one of five is more
urgent than a minor one seen in five of five.

## Rounds

Three rounds of five beats one round of fifteen, because you fix between rounds and learn
whether the fix worked. Five per segment, not five in total, when segments differ
meaningfully.

Stop when a round produces no new critical or serious findings.

## Comparison testing

- Equal fidelity across options, or the polished one wins on polish
- Counterbalance the order across participants
- Ask which and why, then probe the why until it reaches a need
- Never ask them to rank features
- Record which they chose and, separately, which they used more fluently. These often differ,
  and the difference is worth understanding

## After

Within 24 hours: findings list with severity, the evidence for each (participant code plus
timestamp), the design change proposed, and what is still unknown.

**The claim you may make:** "Four of five participants could not find X, and three expected
it to be in Y." That is a usability finding, L4.

**The claim you may not make:** "Users want this." A prototype test measures comprehension
and task success. It does not measure demand. Demand needs a commitment step, and a positive
prototype test is the most over-interpreted result in product discovery.
