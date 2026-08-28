# Artifacts

What discovery produces, and the quality bar for each. Templates are in `templates/` at
the repository root. Every artifact carries provenance, open assumptions, and a date.

**General rules for every artifact:**

- Date it, and name the person who owns it
- Provenance markers inline, never in a footnote
- An Open Assumptions block, even when short
- The answer in the first paragraph, then the support (Minto)
- No section that exists only because the template has it. Delete empty sections rather
  than filling them with filler

---

## 1. Discovery brief `templates/discovery-brief.md`

Written before any study. One page.

**Contains:** the decision, the outcome and its metric, the specific question, what we
already believe and at what confidence, the method and why it beats the alternatives, what
the method cannot tell us, sample and recruiting plan, timeline, cost, and the sentence
"if we learn X we will do Y; if we learn Z we will do W instead".

**Quality bar:** a stranger can tell what decision this feeds and what result would change
it. If the "if we learn" sentence has the same action on both branches, the brief fails.

---

## 2. Interview guide `templates/interview-guide.md`

**Contains:** the learning goals (three at most), consent script, warm-up, the story prompt,
probe ladders, solution exposure if any (always last), close, and a note on what not to ask.

**Quality bar:** no question that can be answered yes or no. No question containing your
solution before the story is collected. No more than one question about the future, and it
is labelled as stated preference.

---

## 3. Interview snapshot `templates/interview-snapshot.md`

One page per interview, produced within a day. Torres's format, adapted.

**Contains:** participant code, date, context, a memorable detail that makes them a person,
the key story with a timeline, verbatim quotes with timestamps, needs and pains surfaced,
opportunities identified, contradictions with prior interviews, and what to ask next time.

**Quality bar:** someone who was not in the session can use it. Every quote is verbatim and
timestamped. The "contradictions" field is filled or explicitly marked none found.

---

## 4. Opportunity solution tree `templates/opportunity-solution-tree.md`

**Quality bar:** the outcome is a customer or business result, not an output. Every
opportunity is phrased in customer language and cites at least one source. No opportunity
contains a product noun. Solutions sit under a single opportunity, and every solution that
is being pursued has at least one assumption test beneath it.

---

## 5. Assumption map `templates/assumption-map.md`

**Contains:** every assumption behind a solution, categorised (desirability, viability,
feasibility, usability, ethical), plotted on importance against current evidence, with the
top-right quadrant listed as the test queue.

**Quality bar:** assumptions are written as falsifiable statements, not as topics.
"Merchants will pay 5% of order value" is an assumption. "Pricing" is not.

---

## 6. Test card and learning card `templates/test-card.md`, `templates/learning-card.md`

Strategyzer format. Test card: we believe X, to verify we will do Y, and measure Z, we are
right if Z exceeds threshold T. Learning card: we believed X, we observed Y, from that we
learned Z, therefore we will W.

**Quality bar:** the threshold T is written **before** the test runs and is not adjusted
afterwards. This is the single most common integrity failure in experimentation.

---

## 7. Experiment plan / pre-registration `templates/experiment-plan.md`

**Contains:** hypothesis, primary metric (one), guardrail metrics, secondary metrics
labelled exploratory, unit of randomisation, sample size and the assumptions behind it,
duration and stopping rule, exclusions defined in advance, analysis method, threats to
validity, and what ship and no-ship each look like.

**Quality bar:** written and shared before launch. Any change after launch is recorded as
an amendment with a reason and a timestamp, not edited silently.

---

## 8. Research readout `templates/research-readout.md`

**Structure, in this order:**

1. The answer, in one paragraph, with its confidence level
2. What we did: method, sample, sampling frame, dates
3. Findings, each with evidence, count out of total sources, and confidence
4. Disconfirming evidence
5. What we still do not know, ranked
6. Recommendation, with the trade-off named
7. Open assumptions
8. Appendix: raw evidence index

**Quality bar:** a reader can find the source of any claim in under a minute. The
disconfirming section is not empty. No claim in section 1 exceeds the confidence of the
evidence in section 3.

---

## 9. Evidence ledger `templates/evidence-ledger.csv`

One row per claim. Schema in `references/03-evidence-ledger.md`.

**Quality bar:** every claim in every readout has an id in the ledger. This is what makes
an AUDIT possible six months later.

---

## 10. Decision record `templates/decision-record.md`

**Contains:** the decision, the date, the decider, the options considered, the evidence
that carried it (by ledger id), the confidence at the time, the assumptions accepted, what
would cause a revisit, and the review date.

**Quality bar:** the decider is a named person. The confidence recorded matches the
evidence, not the mood in the room. This document is what makes a post-mortem honest,
because it captures what was actually known at the time.

---

## 11. Opportunity canvas `templates/opportunity-canvas.md`

Jeff Patton's one-pager, used when a single opportunity is about to get investment.

---

## 12. One-page discovery summary per outcome

The living document `discovery-ops` maintains. What we are trying to change, what we know
and how well, what we are testing now, what we have ruled out and why. Updated weekly,
never rewritten from scratch. This is the artifact that stops the same study being run
twice.

---

## Format guidance

Deliver in the format the reader will actually use. Markdown for a repository, a document
for stakeholders, a spreadsheet for the ledger, slides only when the artifact will be
presented rather than read.

Slides for discovery findings almost always lose the provenance. If findings must be
presented, keep the full readout as the source of truth and treat the deck as a summary
that links back to it.
