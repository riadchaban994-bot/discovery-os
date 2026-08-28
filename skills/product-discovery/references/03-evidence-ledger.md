# The evidence ledger

Discovery accumulates evidence. It does not "validate". This file defines how evidence is
graded, recorded, and converted into a stated confidence, and how to audit a document
someone else wrote.

---

## The evidence strength ladder

The ladder ranks **how hard the evidence is to fake**, not how useful it is. A high level
is not automatically better; an L7 experiment cannot tell you why, and an L3 interview
cannot tell you how many. Use the lowest level that can carry the decision, and never let
a decision rest above the level of its weakest load-bearing evidence.

| L | Evidence type | What it can support | What it cannot |
|---|---|---|---|
| **L0** | Assertion. Someone's opinion, including a model's. Seniority is irrelevant | Generating a question | Any claim about the world |
| **L1** | Analogy. Competitor behaviour, benchmarks, what worked elsewhere, desk research | Framing a hypothesis, orienting in a category | Any claim about your customers |
| **L2** | Stated preference. Survey answers, feature votes, "would you use", focus groups, intent scales | Choosing what to investigate next | Prevalence, willingness to pay, prioritisation |
| **L3** | Reported behaviour. Interview stories about specific past episodes, support tickets, sales-call records, CRM history | Naming an opportunity, describing a workflow, generating design constraints | Prevalence at population level, causality |
| **L4** | Observed behaviour. Usability sessions, field observation, session replay, existing product analytics | Design decisions, usability judgements, describing what happens now | Why it happens, or what would happen if you changed it |
| **L5** | Simulated commitment. Fake-door click, waitlist signup, landing-page conversion, email intercept, pricing-page interaction | Go or no-go on further investment, relative demand between propositions | Satisfaction after use, retention, absolute market size |
| **L6** | Real commitment. Money paid, contract or LOI signed, tool adopted **by choice** and still used at 30 days, meaningful time invested | The business case, willingness to pay, value delivered | Causality, and generalisation beyond the tested audience |
| **L7** | Controlled experiment. Randomised, powered, pre-registered, on the real product | Causal effect size, scaled rollout decisions | Why the effect exists, and effects outside the tested population and window |

**Lineage.** The graduated-evidence idea comes from Itamar Gilad's Confidence Meter and
from the evidence-strength scale in Bland and Osterwalder's *Testing Business Ideas*.
Savoia's "skin in the game" principle in *The Right It* is the reason L5 and L6 sit where
they do. The levels above are this skill's own calibration; use them consistently rather
than mixing scales.

### When the user cannot choose

L5 and L6 are both **demand signals**, and they assume a person who could have said no.
Strip that and the top of the ladder goes hollow. This is not an edge case: internal tools,
government services, clinical mandates, school systems, compliance software and anything
channel-sold all live here. Reading the ladder literally in those contexts produces the
exact confidence inflation it exists to prevent.

**The mis-grading to watch for.** Mandated usage is not commitment. Twelve thousand
employees using the expense tool is **L4 evidence of behaviour and L0 evidence of value**,
because they had no alternative. Reporting it as L6 and reaching "Established" is the most
available way to break this ledger, and it happens because the L6 row says "tool adopted and
still used at 30 days".

**Substitute commitment signals, by context:**

| Context | What counts as L6 | What does not |
|---|---|---|
| Captive users (internal, mandated, statutory) | Unpaid effort invested: a workaround built, a shadow spreadsheet maintained, time spent beyond the required path, voluntary escalation, refusal to migrate off a bespoke setup. Plus the budget holder funding it | Usage, logins, adoption, satisfaction scores collected at work |
| Channel-sold (distribution, resellers, OEM) | A distributor stocking order at their own risk, a design win at the customer's engineering team, inclusion on an approved-vendor list | End-user enthusiasm the distributor reports back to you |
| Two-sided marketplace | Commitment on **both** sides, measured separately. A supplier turning down other work, a buyer moving spend across | A signal on one side alone, which is usually the easy side |
| Public service | Sustained voluntary use where an offline alternative exists, and complaint volume falling against a stable baseline | Transaction counts, when the service is the only route |
| Clinical or professional | The clinician changing what they do when the tool is not looking, and continued use when an override is one click away | Compliance with a mandated workflow |

**The general test.** Ask what the person gave up. If the answer is nothing, because they had
no alternative, it is not commitment evidence whatever the usage numbers say.

### Published research in regulated and scientific domains

L1 covers "analogy, benchmarks, what worked elsewhere" and that grading is right for a
competitor teardown or a vendor's marketing benchmark. It is **wrong for a peer-reviewed
controlled trial from another institution**, and applying it mechanically pushes people in
clinical, pharmaceutical, education and public-health contexts to spend months generating L3
interview data that is weaker than what a literature search returns for free.

**Rule:** grade published research on the design it actually used, not on the fact that
someone else ran it. A randomised trial published in a peer-reviewed journal is L7 evidence
about its own population, discounted for how far your population and setting differ from it.
State the discount and the reason. In a domain with a real literature, reading it is
frequently the cheapest and strongest study available, and it should be the first step.

### Level modifiers

Apply after assigning a level:

| Modifier | Effect |
|---|---|
| Sample self-selected into the study | Down one level |
| Sample recruited from your happiest users only | Down one level, and flag the sampling frame |
| Data collected more than 12 months ago in a fast-moving category | Down one level, date it visibly |
| Participants knew the answer you wanted | Down one level |
| Two independent sources of different types agree | Up one level, capped at the higher source's level |
| Result contradicts the team's prior and was accepted anyway | Note it. Disconfirming evidence that survived is the most trustworthy kind |
| Single source, however strong | Never above "Supported" as a conclusion |

---

## Confidence levels for conclusions

Use exactly these four words. Every conclusion gets one, plus a falsifier.

| Level | Requires | Wording |
|---|---|---|
| **Speculative** | L0-L1 only | "Speculative. No evidence about our customers yet." |
| **Indicated** | L2-L3, thin, single-source, or no saturation | "Indicated. Three of six mentioned it, one segment only." |
| **Supported** | L3-L4, multiple independent sources, saturation reached, no unexplained contradiction | "Supported. Nine of eleven, plus matching ticket volume." |
| **Established** | L5+ with a second independent source, or L7, and disconfirming evidence actively sought and addressed | "Established. Experiment n=18k, plus a matching commitment test." |

**The falsifier is mandatory.** Every conclusion states the single piece of evidence that
would most reduce confidence in it, and the cheapest way to get that evidence. A
conclusion with no falsifier is not a conclusion, it is a belief.

**"Validated" is banned.** It has no defined evidence threshold, it ends inquiry, and it
travels into decks where nobody can audit it. Use the four levels.

---

## The ledger itself

One row per claim. Kept as a spreadsheet or a table in the repository. The point is that
any claim in any document can be traced back to a row.

| Field | Content |
|---|---|
| `id` | Stable, e.g. `EV-041` |
| `claim` | One sentence, falsifiable, no hedging |
| `level` | L0-L7 |
| `confidence` | Speculative / Indicated / Supported / Established |
| `sources` | Participant codes, dataset with date range and n, ticket query, experiment id |
| `date` | When collected, not when written |
| `n` | Sample, with the population it was drawn from |
| `contradicts` | Ids of claims this conflicts with |
| `supports` | Which opportunity or decision it feeds |
| `decays` | When this should be rechecked. Everything decays |
| `owner` | Who can answer questions about it |

`templates/evidence-ledger.csv` has the header row ready to use.

**Decay is not optional.** In a fast-moving category, qualitative claims about behaviour
should be rechecked within 6-12 months, pricing claims within 6, competitive claims within
3. An undated claim in a strategy document is a liability.

---

## Provenance tags in prose

Inline, in every document, on every factual sentence.

```
Operators reconcile stock manually at the end of each day [src: interviews P01-P11,
Feb-Mar 2026, n=11 of 11 who run physical stock] and the step takes 20-40 minutes
[src: observed in 4 field visits, timed].

[ASSUMPTION] This cost is high enough for them to pay to remove it. Unsupported.
Cheapest check: offer a paid pilot to three operators.

[UNVERIFIED: ~60% of small retailers in the region use a smartphone POS? source needed]
```

Three markers, used consistently, do almost all the work:

- `[src: ...]`: has provenance
- `[ASSUMPTION]`: a belief the document depends on, stated as such
- `[UNVERIFIED: ...]`: a number or fact that needs a source, with a pointer to where

---

## AUDIT mode protocol

When handed a PRD, roadmap, business case, strategy doc, or research readout:

1. **Extract every claim.** A claim is any sentence that asserts something about the world:
   customers, market, competitors, costs, behaviour, causes. Ignore intentions and plans.
2. **Grade each one.** Level, confidence, source. Most claims in most documents grade L0.
3. **Find the load-bearing ones.** Which claims, if false, break the document's
   recommendation? Usually three to five out of forty.
4. **Check the load-bearing ones hardest.** Everything else can stay ungraded if time is
   short. Effort belongs where the risk is.
5. **Flag the causal language.** Every "drove", "caused", "led to", "resulted in",
   "because of" attached to a non-experimental result.
6. **Flag the sample crimes.** Percentages from small n, subgroup claims, "users" from
   fewer than five sources, missing denominators.
7. **Flag the survivors.** Numbers with no source. Quotes with no participant code.
   Benchmarks with no citation.
8. **Report as a table**, then the three cheapest actions that would most raise the
   document's overall confidence.

**Audit output shape:**

```
## Audit: [document], [date]

Claims examined: 38. Load-bearing: 4.

| # | Claim | Where | Level | Issue | Cheapest fix |
|---|-------|-------|-------|-------|--------------|
| 1 | "Merchants lose 3 hours a week to reconciliation" | p2 | L0 | No source. Load-bearing: the whole ROI case rests on it | Time 5 merchants doing it. Half a day |
| 2 | "The redesign drove a 12% lift" | p5 | L4 | Causal verb on a before-and-after. Seasonality not excluded | Compare to same weeks last year, then say "associated with" |
| 3 | "68% of users want offline mode" | p7 | L2 | Stated preference from n=22, reported as a percentage | Report as "15 of 22 said". Test with a fake door |

## Three actions that would most raise confidence
1. ...
```

Be neutral and specific. The audit is about the document, never about the author. Name the
issue and the fix, not the failing.

---

## Triangulation

A claim supported by two sources of **different types** is much stronger than one
supported by two sources of the same type. Twenty interviews are still one method.

| Claim type | Strong triangulation |
|---|---|
| A problem exists | Interview stories + support ticket volume + observed workaround in the field |
| A problem is widespread | Interviews + prevalence survey with a defined frame + behavioural analytics |
| A solution is wanted | Comparison prototype + fake-door conversion + pre-sale |
| A change worked | Experiment + qualitative follow-up + a guardrail metric that did not degrade |
| Willingness to pay | Pricing test + actual purchases + retention after purchase |

Where two source types disagree, that disagreement is the most valuable finding in the
corpus. Do not average them. Explain them.
