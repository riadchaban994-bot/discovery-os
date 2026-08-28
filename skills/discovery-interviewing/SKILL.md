---
name: discovery-interviewing
description: Use when planning, writing, or running customer interviews, when recruiting or screening participants, when a user interview produced nothing useful, when moderating a research session, when practising interview technique before a real session, or when writing up an interview.
---

# Discovery interviewing

## Core principle

An interview collects **stories about specific past episodes**. It does not collect
opinions, predictions, feature requests, or approval. Everything valuable comes from
"tell me about the last time", and everything worthless comes from "would you".

The interviewer's job is to stay quiet, follow a real episode in detail, and resist the
urge to explain. Most bad interviews are bad because the interviewer talked.

## Three modes, kept strictly separate

| Mode | Participant | Output usable as evidence |
|---|---|---|
| **Design** | none | The guide itself |
| **Moderate** | a real person | Yes |
| **Rehearse** | model-simulated | **Never.** Stamped `SYNTHETIC - NOT EVIDENCE` |

Never blend them. A rehearsal transcript that loses its stamp becomes indistinguishable
from a real one within a week, and there is no way to recover the distinction downstream.

## The interview types

| Type | Use for | Length | Read |
|---|---|---|---|
| Story-based / continuous | Ongoing opportunity discovery | 30-45 min | `references/interview-types.md` |
| JTBD switch | Why someone changed solution | 60-75 min | same |
| Contextual inquiry | What actually happens at the work | 2-4 hrs | same |
| Churn / exit | Why someone left | 30 min | same |
| Usability session | Where the interface fails | 45-60 min | `discovery-prototyping` |
| Solution feedback | Reaction to two or more options | 45 min | same |
| Expert / domain | Orientation in an unfamiliar domain | 45 min | `references/interview-types.md` |

## Guide structure

Learning goals first, at most three. A guide with six goals produces six shallow answers.

1. **Consent and framing** (2 min). Who you are, what this is for, recording permission,
   no right answers, they can stop or skip anything.
2. **Warm-up** (3 min). Their role and context. Real questions, not small talk.
3. **The story** (20-25 min). One specific recent episode, walked through in order. This
   is the interview. Everything else is scaffolding.
4. **Probing** (inside the story). Depth over breadth.
5. **Solution exposure** (10 min, optional, always last). Two or more options,
   counterbalanced. Never before the story.
6. **Close** (3 min). Anything I should have asked. Who else should I talk to.

`references/question-bank.md` has the openers, probes and closers, plus the banned forms.

## Probing: the only technique that matters

When you get a general statement, get the specific episode underneath it.

> "Reconciliation is a nightmare."
> → "When did you last do it?"
> → "Walk me through that evening, from when you started."
> → "What did you have open in front of you?"
> → "What happened when the numbers did not match?"
> → "What did you do then?"
> → "How long did that take?"
> → "Who else was involved?"
> → "What would you have done if you had not caught it?"

Five levels down is where the finding is. Most interviewers stop at one.

**The four probes that do most of the work:** "Tell me about the last time." "What did you
do next?" "What did you do before this?" And silence, held for three full seconds.

## Sample size

| Purpose | Sample | Stop when |
|---|---|---|
| Problem discovery in one segment | 5-8, then continue weekly | New codes per interview approaches zero |
| Multiple segments | 5-8 per segment | Saturation within each segment separately |
| Usability | 5 per round, 3 rounds | Round 3 finds nothing new |
| Enterprise | 5-8 total is a strong sample | Coverage of the buying roles matters more than count |
| Prevalence | Interviews cannot answer this | Route to `discovery-quant` |

Saturation is measured, not felt. `discovery-synthesis` has the saturation curve method.

## Recruiting

Recruiting is the constraint, not the interview. Teams that interview weekly have solved
recruiting once; teams that interview rarely re-solve it every time.

Full guidance in `references/recruiting-and-sampling.md`, including screener design,
the automated in-product recruiting pattern, incentives, and the sampling-frame statement
that must appear in every readout.

## AI-moderated interviews with real participants

Permitted under the protocol in `references/live-interview-copilot.md`. Disclosure and
consent up front, fixed protocol, full transcript reviewed by a human before synthesis,
and the method's limits stated in the readout. Good for structured collection at volume
and for languages the team does not speak. Poor for exploratory or sensitive work.

## Rehearsal mode

The model plays a participant so the interviewer can practise. Useful, and safe only under
the stamp.

**Protocol:** the model takes a described persona, answers in character, includes realistic
vagueness and reluctance, and does not volunteer perfectly structured insight. After the
session, it switches out of character and critiques the interviewer: leading questions,
missed probes, pitching, rescuing, questions about the future, talk-time ratio.

Every rehearsal output carries the stamp at top and bottom, and the filename starts with
`SYNTHETIC_`.

## After the interview

Within 24 hours, while it is still in your head:

1. Interview snapshot (`../product-discovery/templates/interview-snapshot.md`)
2. Verbatim quotes with timestamps, marked `[inaudible]` where unclear, never filled in
3. Update the experience map and the opportunity solution tree
4. Note contradictions with previous interviews explicitly
5. Note what to ask next time

Then `discovery-synthesis` for coding across the corpus.

## Read next

| File | For |
|---|---|
| `references/interview-types.md` | Choosing and structuring a type |
| `references/question-bank.md` | Openers, probes, closers, banned forms |
| `references/recruiting-and-sampling.md` | Getting the right people, repeatedly |
| `references/live-interview-copilot.md` | Moderating live, and the AI-moderation protocol |
| `references/moderator-errors.md` | The twelve ways interviews go wrong, and the recovery for each |

## Red flags

- The guide contains your solution before the story section
- More than three learning goals
- Any question starting "would you", "do you think", or "how important is"
- The interviewer spoke more than a quarter of the time
- The participant agreed with everything
- No specific date, number, or name in the whole transcript
- You finished feeling validated
