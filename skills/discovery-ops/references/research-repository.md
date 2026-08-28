# Research repository

The purpose is not storage. It is two things: stopping the same study being run twice, and
letting someone six months from now trace a claim back to its source.

---

## Structure

Organise by **outcome**, not by study. Studies are events; outcomes persist, and the
question people ask is "what do we know about X", never "what did study 14 find".

```
discovery/
  outcomes/
    merchants-reach-first-order-in-48h/
      SUMMARY.md              living one-pager. The document people read
      evidence-ledger.csv     every claim, graded and sourced
      opportunity-tree.md
      snapshots/              one per interview, by participant code
        P01-2026-03-04.md
      studies/
        2026-03-12_interviews_onboarding_new-merchants/
          brief.md            written before the study
          guide.md
          codes.csv
          readout.md
        2026-04-02_faketest_bulk-upload/
          plan.md             pre-registration, with the threshold
          results.md
      decisions/
        2026-04-10_build-bulk-upload.md
  raw/                        recordings and transcripts, access controlled, dated deletion
  codebook.md                 versioned, shared across studies
```

**Naming:** `YYYY-MM-DD_type_topic_segment`. Sorts chronologically and searches on any part.
Types: `interviews`, `usability`, `survey`, `experiment`, `faketest`, `analysis`, `desk`.

---

## The living summary

The only document most people will ever read. One page. Rewritten, not appended.

```markdown
# Merchants reach their first order within 48 hours
Updated 2026-04-18 by [name]. Next review 2026-05-16.

## Where we are
Median time to first order is 6 days [src: cohort analysis, Jan-Mar 2026, n=1,840].
Target is 48 hours. 38% never reach a first order at all.

## What we know
| Claim | Confidence | Sources |
|---|---|---|
| Merchants stall at adding the first product, not at signup | Supported | EV-012, EV-019, EV-031 |
| Photos are the specific blocker, not the form | Supported | EV-022, EV-024 |
| Merchants who add 5+ products in week 1 retain 3x better | Indicated (correlational, not causal) | EV-028 |

## What we are testing now
Bulk upload from a phone gallery. Fake door running since 2026-04-02, reads 2026-04-16.
Threshold set in advance: 12% of eligible merchants click, 25% of clickers sign up.

## Ruled out
- Simplifying the signup form. Tested Feb 2026, no effect on time to first order [EV-015].
  Do not repropose without new evidence.
- Onboarding video. Watched by 4% of new merchants [EV-018].

## Biggest open question
Whether merchants who never add a product were ever going to sell, or were blocked.
Cheapest next step: 5 interviews with merchants who signed up and never listed anything.
Recruiting is the constraint; they do not answer email.
```

**The "Ruled out" section is the most valuable part** and the one nobody writes. It is what
stops the same idea being proposed every six months by someone new.

---

## Evidence ledger

Schema in `../product-discovery/references/03-evidence-ledger.md`. One row per claim, stable
ids, referenced from every readout and every decision record. Kept as a CSV or a
spreadsheet, so it can be sorted and filtered.

This is the file that makes an audit possible. Without it, a claim in a strategy document is
unverifiable in practice, whatever the footnotes say.

---

## Decay

| Claim type | Recheck |
|---|---|
| Behavioural, stable domain | 12 months |
| Behavioural, fast-moving domain | 6 months |
| Pricing and willingness to pay | 6 months |
| Competitive | 3 months |
| Market size and structure | 12 months |
| Technical feasibility | On any material stack change |
| Regulatory | On any change, and annually |

Set the recheck date when the claim is created, not later. An automation can list what is
overdue; a human decides whether it matters.

---

## Access and retention

- Raw recordings: controlled access, dated deletion, separate from the write-ups
- Identity mapping separate from research content, with the narrowest access
- Participant codes in every artifact, names in none
- Withdrawal must be executable: a participant code that can be found and removed everywhere

---

## Making it findable

- One index page per outcome, linked from wherever the team actually works
- Tag by segment, method, and outcome. Three tag dimensions is enough; more and nobody tags
- Every readout starts with its answer in one paragraph, so search results are useful
- Consistent titles: `[Method] on [topic] with [segment], [date]`

**The test of a repository:** a new team member, given a question, can find whether it has
already been answered in under five minutes. If they cannot, the structure has failed
regardless of how much is in it.
