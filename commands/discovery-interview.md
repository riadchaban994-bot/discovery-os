---
description: Design an interview guide, rehearse the session, or write up and code what you learned.
argument-hint: [design | rehearse | debrief] [topic or transcript path]
---

Invoke the `discovery-interviewing` skill for: $ARGUMENTS

Paths written as `references/...`, `assets/...` and `templates/...` below are relative to the `discovery-interviewing` skill's own directory.

Pick the mode from what was asked, and say which mode you are in:

**Design.** Establish the learning goals, at most three, and the segment. Then produce the
full guide using `skills/product-discovery/templates/interview-guide.md`: consent script verbatim, warm-up, the story
opener naming a specific activity, probe ladders, solution exposure last if any, close.
Check it against the banned question forms in `references/question-bank.md` before
delivering.

**Rehearse.** Play a participant so the user can practise. Answer the way a real person
does: partial, meandering, occasionally contradictory, politely agreeable when pitched.
Never produce tidy insight-shaped sentences. Afterwards, break character and critique the
interviewer against the checks in `references/live-interview-copilot.md`.
Stamp every rehearsal artifact `SYNTHETIC - NOT EVIDENCE` at the top and bottom, and prefix
the filename with `SYNTHETIC_`.

**Debrief.** Produce the interview snapshot from `skills/product-discovery/templates/interview-snapshot.md`. Verbatim
quotes with timestamps only, `[inaudible]` where unclear and never filled in. Fill the
contradictions field. Then hand off to `discovery-synthesis` for coding.

Never write a quote that was not said. Never add a participant.
