# Prototype build guide

Working starting points in `assets/`. All three are single files with no dependencies: open
them in a browser and they run.

| File | What it is |
|---|---|
| `assets/clickable-prototype.html` | Clickable prototype with a built-in usability observation log and CSV export |
| `assets/fake-door.html` | Fake-door page with the honest close and intent capture built in |
| `assets/woz-console.html` | Wizard of Oz harness: participant pane plus operator console |

---

## 1. Clickable prototype

**Authoring.** Two objects at the top of the file: `TASKS` and `SCREENS`. Each screen is a
title plus HTML. Any element with `data-go="screen_id"` becomes a hotspot;
`data-label="..."` names it in the log.

**Why this one instead of a design tool.** It records the session automatically:

| Logged | Why it matters |
|---|---|
| Every hotspot click, with a label and a timestamp | The path they actually took, not the one you remember |
| Every **dead click** on a non-interactive element | The strongest usability signal there is. A dead click is a participant telling you where they expected something to be |
| Time per task from start | Comparable across participants |
| Task outcome: completed or gave up | The success rate, computed rather than recalled |

Export the CSV, and one line per session gives you a comparable dataset across the round.

**Moderator keys, hidden from the participant:** `h` toggles hotspot highlighting, `n`
marks the current task complete, `x` marks it failed.

**Rules when authoring.**
- Real copy and real numbers, always. Placeholder text makes the prototype untestable for
  comprehension, which is usually half of what you are testing
- Build only the screens the tasks need. Every extra screen is time spent on something
  nobody will look at
- When comparing two approaches, build both in the same file at the same fidelity and
  counterbalance which one the participant sees first
- Do not build error states unless an error state is the question

---

## 2. Fake door

**What is built in and must stay:** the honest close fires immediately on click, no money is
taken, no obligation is created, and the sign-up promises a real follow-up including when
the decision is not to build.

**Set before running:** the threshold, in the `THRESHOLD` object, with a note on where it
came from; the comparison point, which is the click rate of a comparable existing entry
point on the same surface; and the end date.

**Replace the local logging** with your real analytics events. The template stores to
`localStorage` only so the mechanics are visible without a backend.

**Report three numbers, never one:** click rate against the comparison point, intent-capture
rate among clickers, and total absolute volume. The middle number is the signal. Clicks are
curiosity.

**Then actually write back to the people who signed up.** This is not optional and it is the
part teams skip. It costs an hour and it is the difference between research and a trick.

---

## 3. Wizard of Oz

**How it runs.** Two browser panes talking over a `BroadcastChannel`. `?role=user` and
`?role=operator`. For a real remote session, replace the channel with a websocket, a shared
document, or a chat tool. The interaction design is the part worth keeping, not the
transport.

**The rule that makes the data valid:** match the latency the real system would have. The
template enforces `DELAY_MS`. An operator who answers instantly, or far better than the
system ever could, produces a result you cannot reproduce with software.

**Do not run this at all** where the concealed output is a clinical, diagnostic, financial,
legal or safety judgement, or on a statutory service. A human silently generating
recommendations a professional believes came from a checked system is a safety hazard, not a
research method. Use shadow mode instead: run the logic, log what it would have done, show
nobody, compare against what actually happened.

**The operator's real job:** answer as the system would, not as a helpful human would. Keep
the wording consistent. When you cannot answer, say what the system would say. **Log every
question you could not answer.** That log is the requirements document, and it is the single
most valuable output of a Wizard of Oz test.

**Especially valuable for AI features.** It tells you what accuracy the experience actually
requires, which is nearly always different from what the team assumed, and it tells you what
the failure mode needs to look like before you have a model to fail.

---

## 4. Other patterns worth building

**Data mock layer.** Before building a prototype against real data, extract 50 to 100 real
records into a JSON file, including the messy ones: long names, missing fields, unusual
characters, zero and negative values, and the outliers. Most concepts that look good on
designed data fall apart here, and it costs a morning to find out.

**Paper prototype sheets.** Printed screen frames with the interactive elements cut out
separately so the moderator can swap them. Still the fastest way to test a flow that does
not exist, and the honesty of the feedback is noticeably higher than for anything that looks
built.

**Concierge tracker.** A spreadsheet, not software: one row per delivery, with what was
asked, what was done, how long it took, what broke, and whether they came back. That
spreadsheet becomes the specification.

**Video prototype.** Screen recording plus voiceover, telling the story of the product in
under 90 seconds. Cheap, scales to hundreds of viewers, and can be paired with an intent
capture to move from L2 to L5.

---

## Publishing a prototype

- Local file for moderated sessions, which is the default and needs nothing
- A static host for unmoderated remote tests
- Password or an obscure URL if it must not be found, and a "this is a prototype" banner if
  it might be
- Take it down when the round ends. A prototype left up is a promise you did not make
