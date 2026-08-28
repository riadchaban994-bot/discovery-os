# Synthesis quality gates

Run before a synthesis ships. Any failed gate blocks the readout until it is fixed or the
limitation is stated explicitly in the method section.

---

## Gate 1: traceability

- [ ] Every finding lists the segment ids that support it
- [ ] Every quote has a participant code and a locator
- [ ] Every quote is verbatim. No cleaned-up, composite, or representative quotes
- [ ] No claim in the summary exceeds the evidence in the body

**Composite quotes are prohibited.** A quote assembled from several participants to
"capture the sentiment" is a fabrication with a research-shaped wrapper. If you need to
express a pattern, write a theme sentence and cite the sources.

## Gate 2: counting

- [ ] Source counts, not mention counts
- [ ] No percentages below n=30
- [ ] No subgroup claims where the subgroup is under 30
- [ ] Every count carries its denominator
- [ ] "Most", "many", "several" replaced with numbers

## Gate 3: sampling

- [ ] The sampling frame is stated in one sentence
- [ ] Exclusions are named
- [ ] Who is missing is named
- [ ] Segments analysed separately, not averaged
- [ ] The frame's bias is stated in the same paragraph as the headline finding, not in an
      appendix

## Gate 4: disconfirmation

- [ ] Disconfirming evidence section is present and non-empty, or its emptiness is
      explained and flagged as a warning
- [ ] Negative case analysis run on the strongest theme
- [ ] At least one finding that was not expected before the study. If everything confirms
      the prior, the study probably measured the prior

## Gate 5: saturation

- [ ] New-codes-per-source curve computed and reported
- [ ] Saturation claimed only where the curve supports it
- [ ] Claimed per segment, not across the whole sample
- [ ] Where saturation was not reached, the readout says so and says what is still open

## Gate 6: language

- [ ] Opportunities in customer language
- [ ] No product nouns in opportunities
- [ ] Codes not named after your features
- [ ] Jargon defined on first use

## Gate 7: causality

- [ ] No causal verbs on qualitative or observational findings
- [ ] Participant self-attribution labelled as self-attribution, not as cause
- [ ] Where a cause is proposed, competing explanations are listed

## Gate 8: decision

- [ ] The decision this feeds is named
- [ ] The recommendation states its trade-off
- [ ] The next action has a shape and an owner slot
- [ ] What we still do not know is ranked, and the top item has a cheapest-next-step

## Gate 9: the honesty pass

Read the synthesis as the strongest opponent of its conclusion.

- What would they attack first?
- Which finding is doing the most work with the least evidence?
- Which quote is being asked to carry a claim it cannot?
- If the opposite conclusion were true, what in this corpus would look different, and did
  anyone check?

Write down the answer to the last question. If nobody checked, that is a limitation and it
belongs in the readout.

---

## The one-page confidence summary

Ends every synthesis. Nothing else in the document may exceed these levels.

```
| Claim | Sources | Level | Confidence | Would change if |
|-------|---------|-------|------------|-----------------|
| Operators reconcile twice | 7/11 | L3 | Supported | Representative sample showed integrated stacks are the norm |
| The cost is 20-40 min/day | 4 timed observations | L4 | Indicated | Wider timing sample, or self-reported logs across 20 operators |
| They would pay to remove it | 0 | L0 | Speculative | Any commitment test. This is the load-bearing gap |
```

The third row is the point of the table. It makes the gap between what is known and what
the plan assumes visible on one line, which no amount of prose does as well.
