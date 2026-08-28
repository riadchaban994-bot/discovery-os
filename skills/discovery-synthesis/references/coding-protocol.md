# Coding protocol

Qualitative coding done so a stranger can audit it. Based on Braun and Clarke's thematic
analysis (2006), with the adaptations that AI-assisted coding requires.

---

## Segmentation

A segment is one unit of meaning: usually one to five sentences carrying a single idea.

**Rules:**
- Keep verbatim text. Never store a paraphrase, because the paraphrase becomes the quote
- Every segment carries: `source_id`, `locator` (timestamp or line), `segment_id`,
  `speaker`, `verbatim`
- Split when the speaker changes idea, not when they change sentence
- Mark unclear audio as `[inaudible]`. Never infer the missing words
- Keep the interviewer's question attached to the answer. A leading question changes how
  the answer must be read

---

## Codebook format

Written before mass coding, revised as it develops, versioned.

```
CODE: workaround-spreadsheet
DEFINITION: Participant maintains a spreadsheet outside the system to hold information
            the system does not hold or does not show usefully.
INCLUDE: Any manual file, sheet, or notebook used alongside the tool for the same job.
EXCLUDE: Spreadsheets used for a genuinely separate task (payroll, tax) with no overlap.
         Exports used once and discarded.
ANCHOR: "I keep my own sheet because the report only shows me last month" [P04, 14:22]
CREATED: 2026-03-04, v1.2
```

**Every code needs an exclusion rule.** Codes without one expand until they mean nothing,
which is how a corpus ends up with one code applied to 60 percent of segments.

**Code types worth separating:**

| Type | Captures |
|---|---|
| `behaviour-*` | What they do |
| `pain-*` | What costs them |
| `workaround-*` | What they built to cope. Highest-value code family |
| `context-*` | Conditions that change the behaviour |
| `outcome-*` | What they are trying to achieve |
| `trigger-*` | What starts the episode |
| `constraint-*` | What blocks a change |
| `quote-*` | Especially clear articulations, for the readout |

---

## AI-assisted coding

Where the real gain is: coding 400 tickets or 60 sales calls that nobody was ever going to
code by hand.

**The rules, all of them required:**

1. **A human writes or approves the codebook before mass coding.** The codebook is the
   judgement; the application is the labour.
2. **The model codes only what is present.** Every applied code cites the exact verbatim
   span that justifies it. A code with no span is a defect, not a finding.
3. **Confidence per application.** Anything below the threshold goes to a human queue
   rather than into the counts.
4. **New codes are proposed, never adopted silently.** The model returns proposals with
   the segments that motivated them; a human accepts or rejects.
5. **A human recodes a 15-20 percent sample blind.** Compare, compute agreement, resolve
   disagreements by revising the codebook rather than by splitting the difference.
6. **Never let the model summarise before coding.** Summarising first loses the detail and
   introduces the model's framing, which then contaminates the codes.
7. **Never let the model write a quote.** Quotes are extracted spans with locators, always.

**Agreement.** Percentage agreement for a quick read; Cohen's kappa where you need a
defensible number, since kappa corrects for chance agreement. Above 0.8 is strong, 0.6-0.8
is workable with documented disagreements, below 0.6 means the codebook is ambiguous and
needs rewriting before the corpus is coded.
`../discovery-quant/scripts/qual_saturation.py --kappa` computes it.

**The failure mode to watch for.** A model asked to "find the themes" will produce
plausible, well-written themes whether or not they are in the data. Always code first, then
theme from the codes. Never theme directly from raw text.

---

## Coding across languages

- Code in the language of the source, then translate the codebook, not the segments
- Keep the original verbatim alongside any translation, always
- Note where a concept does not translate. Those gaps are findings about the market
- Where translation is machine-assisted, a human speaker checks every quote that reaches
  the readout

---

## From codes to themes

1. Sort codes by source count, descending
2. Group by shared meaning, not by shared word
3. A candidate theme needs at least three independent sources, or it is a signal to
   investigate rather than a finding. Three is the floor for a theme; a claim about what
   "users" in general do needs five or more, and a single-source theme is a red flag, not a
   small theme. The three numbers describe three different claims, not three opinions about
   the same one
4. Write the theme as a full sentence that makes a claim, not as a topic label.
   "Reconciliation happens twice because the two systems disagree" is a theme.
   "Reconciliation" is a folder
5. For each theme, list: supporting segments, source count out of total, contradicting
   segments, and the segments that nearly fit but do not
6. Check the theme against a source that was not used to build it

**Negative case analysis.** Take the strongest theme and find every source that does not
fit. Either the theme narrows to a segment, or it needs a condition, or it is weaker than
it looked. This step is what separates synthesis from storytelling, and it is the step
that is always skipped.

---

## Traceability record

Every finding in the readout carries:

```
Finding: Operators reconcile twice because the POS and the delivery app disagree.
Sources: 7 of 11 (P01, P03, P04, P06, P08, P09, P11)
Codes: workaround-spreadsheet, pain-double-entry, trigger-mismatch
Contradicting: P05 (single channel, no mismatch), P10 (uses one integrated system)
Confidence: Supported
Would drop if: a representative sample showed most operators already use an integrated
system. Cheapest check: 200-response screener on POS and delivery stack.
```
