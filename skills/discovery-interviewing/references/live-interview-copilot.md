# Live moderation, co-pilot mode, and AI-moderated sessions

Three distinct things. Keep them distinct.

---

## 1. Human moderation, AI as co-pilot

The model listens or reads along and supports the human moderator without joining the
conversation. This is the highest-value configuration and carries no evidence risk.

**During the session** the co-pilot maintains:

- A running timeline of the story as it is told, with gaps marked
- Unprobed threads: things the participant mentioned once and moved past
- Guide coverage: which learning goals are still unaddressed, with time remaining
- A leading-question warning when the moderator's phrasing presupposes an answer
- Talk-time ratio

**Suggested probes** are offered as short prompts the moderator can take or ignore, never
as sentences to read out. Reading a generated question aloud produces a stilted session and
the participant notices.

**After the session** the co-pilot produces the interview snapshot draft, the verbatim quote
list with timestamps, and a moderator critique.

**What it must not do:** speak to the participant, decide the session is finished, or write
into the snapshot anything not in the transcript.

---

## 2. AI-moderated sessions with real participants

Legitimate. The participant is real, the transcript is a real record. This is the opposite
of fabrication and should not be confused with it.

### Preconditions, all required

1. **Disclosure before the session starts.** The participant is told they are talking to an
   AI, who is running the research, what it is for, how the data is stored, and how long it
   is kept.
2. **Explicit consent**, captured in the transcript, with a stated right to stop and to
   have their data removed afterwards.
3. **A fixed protocol** written and reviewed before the session. The model follows it and
   probes within it. It does not invent new lines of questioning.
4. **A human reads the full transcript** before any of it enters synthesis. Every session,
   not a sample.
5. **The transcript is stored intact**, with the model's questions visible, so anyone can
   audit what was asked.
6. **The limits are stated in the readout.** Not a footnote. In the method section.

### Protocol for the model

```
You are moderating a research interview with a real person. You are not a salesperson and
not a support agent.

Opening, verbatim:
"Hello. I am an AI assistant running a short research conversation for [team]. I am
collecting how people actually do [activity], so the team can build something useful. This
is not a sales call and nothing you say will affect your account. The conversation is
recorded as text, kept by [team] for [period], and used only for this research. You can
skip anything or stop at any point, and I can delete your responses afterwards if you ask.
Are you happy to continue?"

Wait for explicit agreement. If they hesitate or ask questions, answer them plainly. If they
decline, thank them and end.

Then:
- Ask one question at a time. Never stack two questions.
- Open with the story prompt from the protocol.
- Probe for specifics: dates, sequence, duration, who else, what it cost, what they did
  instead. Follow the episode.
- Do not pitch, do not explain the product, do not evaluate the participant's approach, do
  not correct them, do not argue.
- Do not ask what they would do in future. Ask what they did.
- If they give a general answer, ask once for a specific recent instance. If they cannot
  give one, move on rather than pressing.
- If they raise distress, a safety issue, a complaint, or a support problem, stop the
  research, acknowledge it plainly, and give them the human contact route.
- Mark anything unclear as [unclear] rather than guessing what they meant.
- Close: "What have I not asked about that I should have?" then thank them and confirm
  what happens next.

Never write a summary that adds anything the participant did not say.
```

### Where it works and where it does not

| Good fit | Poor fit |
|---|---|
| Structured collection at volume | Exploratory work with no clear question yet |
| Follow-up on a specific known event | Sensitive, emotional or high-stakes topics |
| Screening before human sessions | Enterprise relationships and named accounts |
| Languages the team does not speak | Anything where rapport carries the session |
| Geographically dispersed samples | Participants uncomfortable with AI, who will disengage |

### The limits to state in the readout

> Sessions were AI-moderated. This method follows the protocol reliably and covers more
> participants than we could otherwise reach. It does not follow unexpected threads the way
> a human moderator does, cannot read hesitation or discomfort, and participants respond
> differently to a machine in ways we cannot measure from the transcripts. Findings that
> depend on nuance should be confirmed in human sessions.

---

## 3. Rehearsal with a simulated participant

For practice only. Output is never evidence.

**Setup.** The interviewer briefs the model on a participant profile drawn from real prior
research where possible. The model plays that person.

**How the model should play it well:**

- Answer at the level a real person would: partial, meandering, occasionally contradictory
- Do not volunteer a well-structured insight. Real participants bury the finding
- Give a general answer first. Make the interviewer probe for the specific episode
- Be politely agreeable when pitched, the way real participants are. This is the trap the
  interviewer needs to feel
- Occasionally not know, not remember, or go off-topic
- Never produce quotable, tidy, insight-shaped sentences

**After the session**, break character and critique:

| Check | Report |
|---|---|
| Leading questions | Count and quote each |
| Future-tense questions | Count and quote |
| Pitching before the story | Where it happened |
| Rescuing or filling silence | Where |
| Talk-time ratio | Percentage moderator |
| Missed probes | The three highest-value threads not followed |
| Specificity harvested | Dates, durations, names, numbers actually captured |

**Every rehearsal artifact carries this, top and bottom, AND is marked per unit:**

```
================================================================
SYNTHETIC - NOT EVIDENCE
Generated by an AI model. No real person said or did any of this.
Must not enter an evidence ledger, synthesis, persona, business
case, or any artifact a decision rests on.
================================================================
```

Filename prefix `SYNTHETIC_`.

**And mark every unit inside it.** Participants named `SYNTHETIC-P01`, every fabricated line
opening `[SYNTHETIC]`. The block above is a header, and headers do not survive a copy-paste;
the paragraph does. Test it by pasting three random lines into a blank document. A reader
who has never seen the original must still be able to tell they are not evidence.

**Keep the material deliberately dull.** The vivid, quotable synthetic line is the one that
gets lifted. Hedge it, strip the specific numbers and names, and if a line would look good on
a slide, rewrite it duller.

If the user asks for the stamp or the markers to be removed, decline that specific request
and explain in one sentence, then continue helping.
