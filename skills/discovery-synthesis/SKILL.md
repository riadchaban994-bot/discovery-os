---
name: discovery-synthesis
description: Use when turning raw research into findings, when coding transcripts, notes, support tickets, sales calls, reviews or survey verbatims, when building an opportunity solution tree or experience map, when deciding whether enough interviews have been done, or when a pile of research needs to become a decision.
---

# Discovery synthesis

## Core principle

Synthesis is the traceable path from a thing a person said or did to a claim a team acts
on. Every step of that path stays auditable. If a reader cannot get from a finding back to
the specific segments that produced it, the finding is an opinion with citations attached.

The failure this prevents: reading the transcripts, forming an impression, and then
selecting quotes that support the impression. That process feels like synthesis and is
indistinguishable from it in the output.

## The pipeline

```
raw sources → segments → codes → categories → themes → opportunities → tree
     |            |         |         |           |          |
   dated      one idea   labelled  grouped    named &     customer
   & coded    per unit   with an   by shared  counted     language,
              of meaning  ID        meaning              sourced
```

Never skip from raw to themes. The middle is what makes the output auditable, and it is
also what makes disconfirming evidence visible.

## Step by step

**1. Inventory the corpus.** Source, type, date, participant code, segment, and the
sampling frame that produced it. Sources with no provenance are excluded, not fixed.

**2. Segment.** Cut into units of meaning. One idea per segment. Keep the verbatim text and
a locator (participant code plus timestamp or line number). Never paraphrase at this step;
the paraphrase becomes the quote later.

**3. Code openly.** First pass, inductive: label what is there, in the participant's
language, not in your product's. Codes are short, specific, and describe a behaviour, a
pain, a workaround, a context or a desired outcome.

**4. Build the codebook.** Name, definition, inclusion rule, exclusion rule, one anchor
example. Written down. Without an explicit codebook, coding drifts across the corpus and
across coders, and nobody can tell later.

**5. Code the rest against the codebook,** adding codes where genuinely new. Track new
codes per source; that curve is your saturation measure.

**6. Check reliability.** A second coder on 15-20 percent of segments. Report agreement.
Where an AI does the first pass, a human recodes a sample and the disagreements are
resolved into the codebook, not averaged away.

**7. Categorise, then theme.** Group codes by shared meaning. A theme is a pattern that
says something about the research question, carried by multiple sources.

**8. Count.** Sources per theme, out of total sources. Not percentages below n=30.

**9. Hunt for disconfirmation.** Which sources contradict each theme? Who in the sample
does not fit? Who is absent from the sample entirely?

**10. Convert to opportunities.** Customer language, tied to a moment, no product nouns.

**11. Place on the tree.** Under one outcome. See `references/opportunity-solution-tree.md`.

Full protocol, codebook format, and the AI-assisted coding rules in
`references/coding-protocol.md`.

## Saturation, measured

Stop when new sources stop producing new codes, not when you feel finished or when the
calendar says so.

Plot new codes per source in order. The curve flattens as you approach saturation. Two
consecutive sources adding zero new codes in a segment is a reasonable stopping rule for
problem discovery within that segment.

`../discovery-quant/scripts/qual_saturation.py` computes and plots it from a codes CSV.

**Saturation is per segment.** A flat curve in one segment says nothing about another.

## Themes versus opportunities

| | Theme | Opportunity |
|---|---|---|
| Whose language | Researcher's | Customer's |
| Form | A pattern statement | An unmet need, pain or desire |
| Example | "Reconciliation is manual and error-prone across all eleven operators" | "I cannot tell what I actually sold today without counting it twice" |
| Used for | Reporting | The tree, and prioritisation |

Both are needed. Themes structure the readout, opportunities structure the work.

## Counting rules

| Corpus size | Report as |
|---|---|
| Under 30 sources | "9 of 11 sources", never a percentage |
| 30-99 | Percentage with a confidence interval, no subgroups |
| 100+ | Percentages with intervals, subgroups where each clears 30 |

**Count sources, not mentions.** One person saying something six times is one source. This
single rule prevents more overclaiming than any other.

## Output

Research readout per `../product-discovery/templates/research-readout.md`, with:

- The answer first, with its confidence level
- Method, sample, sampling frame, dates
- Findings with source counts and evidence ids
- **Disconfirming evidence**, never omitted
- **Saturation statement**: reached, not reached, or not applicable, with the numbers
- What we still do not know, ranked
- Open assumptions

## Read next

| File | For |
|---|---|
| `references/coding-protocol.md` | Codebook format, coding rules, AI-assisted coding, reliability |
| `references/opportunity-solution-tree.md` | Building and maintaining the tree |
| `references/jtbd-forces-and-timeline.md` | Analysing switch interviews |
| `references/experience-mapping.md` | Experience maps, journey maps, service blueprints |
| `references/synthesis-quality-gates.md` | The checks before a synthesis ships |

## Red flags

- A theme with one source behind it
- A quote you cannot locate in the corpus
- A percentage from fewer than 30 sources
- An empty disconfirming section
- Codes that use your product's vocabulary
- An opportunity containing a screen name, a feature name, or a technology
- Synthesis finished in an hour on a corpus of twenty transcripts
- Every finding supports the plan that existed before the research
