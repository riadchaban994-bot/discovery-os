# The AI boundary

Per activity: what the model may do, what it must never do, and what a human must own.
This exists because AI makes every discovery activity faster, including the ones whose
whole value came from being slow.

**The general rule.** A model may operate on evidence. It may not be the source of
evidence. Anything a model generates about what customers think, want, or do is a
hypothesis until a real person confirms it.

---

## Activity boundaries

| Activity | AI may | AI must never | Human owns |
|---|---|---|---|
| Framing the question | Translate a vague request into a decision, propose the outcome metric, surface the assumptions | Decide which question matters | Choosing the question |
| Recruiting | Draft screeners, write outreach, spot screener loopholes, manage the pipeline | Fabricate a participant, or screen for people who agree | Approving the sample and its frame |
| Guide design | Draft the guide, flag leading questions, build probe ladders, sequence for contamination | Add questions that pitch the solution | Final guide, and what to cut |
| Moderating | Moderate a real session with a real participant under a fixed protocol; act as live co-pilot suggesting probes | Play the participant in anything that will be treated as data | Consent, judgement calls, and following the interesting thread |
| Rehearsal | Play a synthetic participant so the interviewer can practise, under the synthetic stamp | Let the rehearsal output leave the rehearsal | Deciding it was practice |
| Transcription | Transcribe, clean, speaker-label, timestamp | Fill an inaudible gap with plausible text. Mark it `[inaudible]` | Verifying key quotes against audio |
| Coding | Apply a documented codebook, propose new codes with evidence, compute code frequency and saturation, flag contradictions | Invent a quote, merge codes to make a cleaner story, or code the researcher's paraphrase as the participant's words | Approving the codebook and resolving disagreements |
| Synthesis | Draft themes with citations to specific segments, write the disconfirming section, propose opportunities in customer language | Assert a theme that no coded segment supports | Signing off that the synthesis is faithful |
| Opportunity framing | Rewrite solutions as needs, spot duplicates, structure the tree | Add opportunities nobody voiced | Which opportunities are real |
| Prioritisation | Compute scores from stated inputs, expose sensitivity, argue both sides | Choose the priority | The priority |
| Experiment design | Compute sample size and duration, draft the pre-registration, name the guardrails, list the threats to validity | Change the metric or the stopping rule after seeing data | Deciding to run it, and shipping on the result |
| Analysis | Run the calculation, check assumptions, check SRM, present the interval, present competing explanations | Report a point estimate without uncertainty, or a causal claim from a non-causal design | Interpreting in context |
| Prototyping | Build the artifact: clickable flows, fake doors, operator consoles, data mocks | Present a prototype's warm reception as demand evidence | What to build and what to show |
| Writing up | Draft the readout, keep provenance intact, hold the structure | Strengthen a conclusion beyond its evidence, or drop the caveat to make it read better | The claim being made |
| Deciding | Recommend, with reasoning and the trade-off named | Record a decision the user did not make | The decision |

---

## AI-moderated interviews with real participants

Legitimate, and increasingly useful for reach. Distinct from fabrication in one way that
matters: the participant is a real person and the transcript is a real record.

**Permitted when all of these hold:**

- The participant is told, before starting, that they are talking to an AI, who is
  collecting the data, what it is for, and how it will be stored
- Consent is captured and recorded, and withdrawal is possible afterwards
- The protocol is fixed in advance and the model follows it
- The model does not pitch, does not evaluate the participant, and does not argue
- A human reads the full transcript before anything enters synthesis
- The transcript is stored intact, with the model's questions visible

**Its real limits, which must be stated in the readout:**

- It cannot follow a surprising thread the way a skilled human can, and the surprising
  thread is often the finding
- It cannot read hesitation, discomfort, or the pause before a careful answer
- It will miss the thing the participant almost said
- Participants perform differently for a machine: some are franker, some are shallower,
  and you cannot tell which you got

**Best fit:** structured, high-volume, low-ambiguity collection. Screening. Follow-up on a
specific known event. Multi-language reach where you have no moderator.

**Poor fit:** exploratory work where you do not yet know what you are looking for.
Sensitive topics. Enterprise relationships. Anything where rapport carries the session.

---

## The synthetic data question, settled

**Never permitted:** synthetic transcripts, quotes, or personas entering a synthesis, an
opportunity tree, a persona document, a business case, a deck, or any artifact that
informs a decision. Not with a footnote. Not as "placeholder for illustration". Documents
outlive their footnotes.

**Permitted, stamped:** rehearsal, teaching examples, and testing an analysis pipeline
before real data arrives.

**Why the line is absolute rather than a matter of degree.** Synthetic customer data is
indistinguishable from real customer data three documents downstream. There is no reliable
mechanism to strip it once it is in circulation. The only enforceable control is at the
point of creation, which is why the stamp is on the artifact and not in a process
document.

**The stamp, used verbatim:**

```
================================================================
SYNTHETIC - NOT EVIDENCE
Generated by an AI model. No real person said or did any of this.
Must not enter an evidence ledger, synthesis, persona, business
case, or any artifact a decision rests on.
================================================================
```

Top and bottom of the file. In the filename: `SYNTHETIC_`. If the format supports it, in
a header comment too.

---

## Where AI genuinely helps discovery

Say yes loudly to these. Refusing them is as unhelpful as fabricating.

- **Corpus scale.** Coding 400 support tickets or 60 sales calls, which nobody was ever
  going to do by hand. This is the single largest real win.
- **Speed to first draft.** Guides, screeners, protocols, readouts, pre-registrations.
- **Consistency.** Applying one codebook identically across a corpus, which humans do not.
- **Devil's advocate.** Generating the strongest case against a conclusion on demand.
- **Statistical hygiene.** Power, intervals, SRM, multiple comparisons, correct tests.
- **Language reach.** Interviewing and coding in a language the team does not read.
- **Recall.** Surfacing the study from 18 months ago that already answered the question.
- **Prototype speed.** A working clickable prototype in an hour instead of a day.
- **Never losing provenance.** Machines are better than people at keeping the citation
  attached to the claim.

The pattern: AI is excellent at operating on evidence and at removing the cost of rigour.
It is not a source of evidence. Every good use above keeps that line intact.
