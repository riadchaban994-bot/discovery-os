---
description: Build a clickable prototype, fake door page, or Wizard of Oz console for a specific discovery question.
argument-hint: [what needs testing, and the question it answers]
---

Invoke the `discovery-prototyping` skill for: $ARGUMENTS

Paths written as `references/...`, `assets/...` and `templates/...` below are relative to the `discovery-prototyping` skill's own directory.

1. Establish the one question this prototype answers, and what result would change the
   design. Do not build until it is written down.
2. Choose the type and the fidelity per dimension using `references/fidelity-ladder.md`.
   Content fidelity is high in almost every case: real copy and real numbers, never
   placeholder text.
3. Build it from the patterns in `references/prototype-build-guide.md`, starting from the
   working files in `assets/`:
   - `clickable-prototype.html` for task and usability questions. Author the `TASKS` and
     `SCREENS` objects. It logs hotspot clicks, dead clicks, task time and outcomes, and
     exports CSV.
   - `fake-door.html` for demand questions. Set the threshold and the comparison point
     before running. Keep the honest close.
   - `woz-console.html` for value questions where the automation does not exist yet. Set
     `DELAY_MS` to the latency the real system would have. **Do not use it where the
     concealed output is a clinical, diagnostic, financial, legal or safety judgement, or on
     a statutory service. Shadow mode instead.**
4. Produce the test protocol from `references/prototype-testing.md`: tasks in the
   participant's words, the rescue rule, and the observation sheet.

When the prototype tests well, say plainly what that does and does not prove. A positive
prototype test measures comprehension and task success. It does not measure demand.
