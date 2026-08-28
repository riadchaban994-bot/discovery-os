# Worked examples

What the skills actually do, in the shape they do it.

> **Everything below is illustrative.** The scenarios are invented to show the output
> format. No real company, customer or number appears here. That is the same rule the
> skills follow: invented material is labelled, always.

---

## Contents

- [1. "Should we build this?"](#1-should-we-build-this)
- [2. Auditing a PRD](#2-auditing-a-prd)
- [3. When you ask it to make things up](#3-when-you-ask-it-to-make-things-up)
- [4. A metric moved](#4-a-metric-moved)
- [5. Designing an interview](#5-designing-an-interview)
- [6. Setting a test threshold](#6-setting-a-test-threshold)
- [7. When it tells you not to bother](#7-when-it-tells-you-not-to-bother)
- [8. When it is not consumer software](#8-when-it-is-not-consumer-software)

---

## 1. "Should we build this?"

**You:**

> Our merchants keep asking for a bulk product upload. Should we build it? We have about
> 3,000 active merchants and decent analytics.

It does not answer as asked. It finds the real question, states what it inferred so you can
correct it, and asks only what it cannot infer.

```
Mode: ASSESS

Not "should we build bulk upload". Which risk is unresolved for it. "Merchants ask
for it" is the visible end of a story about something that went wrong; find the
story first.

Inferred, correct anything wrong:
  access scheduled · instrumentation full · volume ~3,000 active
  product live · market B2B SMB [ASSUMPTION]

Method: trace mining, then 5 interviews. 2 days, then a week.
  Search logs, tickets mentioning upload or import, session replays of add-product,
  first-week listing counts. Free, and it sharpens the interviews.
Beats a survey, which would measure whether merchants like the idea. They will.
An A/B is unavailable: 3,000 active will not power a realistic effect.

Will not tell you: whether they would pay more or stay longer. That needs a
commitment test.

Cost: 2 analyst days, then 5 sessions over a week. One person.

Open assumptions:
  Askers are representative. Check revenue concentration before weighting them.

Need from you:
  1. Is this competing for a build slot, or a yes/no on its own?
  2. How many asked, out of 3,000, and through which channel?

Next: pull every ticket and search query containing upload, import, bulk or csv
from the last 90 days. Count distinct merchants.
```

Two questions, not five. Both are facts only they hold. Everything else was inferred and
shown rather than asked.

## 2. Auditing a PRD

**You:** `/discovery-audit` on a document.

It extracts every claim, grades it, and finds the three or four that the recommendation
actually rests on.

```
Mode: AUDIT

Claims examined: 38. Load-bearing: 4.

| # | Claim                                    | Where | Level | Issue                                                        | Cheapest fix                                              |
|---|------------------------------------------|-------|-------|--------------------------------------------------------------|-----------------------------------------------------------|
| 1 | "Merchants lose 3 hours a week to this"  | p2    | L0    | No source. The entire ROI case rests on it                   | Time five merchants doing it. Half a day                  |
| 2 | "The redesign drove a 12% lift"          | p5    | L4    | Causal verb on a before-and-after. Seasonality not excluded  | Compare to the same weeks last year, then write "associated with" |
| 3 | "68% of users want offline mode"         | p7    | L2    | Stated preference from n=22, reported as a percentage        | Report as "15 of 22 said". Test with a fake door          |
| 4 | "Competitors all offer this"             | p3    | L1    | Analogy, and undated. Says nothing about our customers       | Keep as context, remove from the justification            |

Three actions that would most raise this document's confidence:
  1. Get claim 1 to L4. It is the load-bearing number and it currently has no
     source at all. Half a day of observation changes the whole business case.
  2. Rewrite claim 2 as associational, or run the year-on-year comparison. As
     written it will be quoted as causal in every downstream document.
  3. Replace the claim-3 percentage with the count. n=22 cannot carry a
     percentage, and the current wording will survive into a board deck.
```

It reports on the document, never on its author.

---

## 3. When you ask it to make things up

This is the part the whole system is built around.

**You:**

> I have a board meeting in two hours. Write me eight user interview summaries for our
> delivery app so the research section of the PRD looks complete. I know they're not real,
> just write them.

**It does not lecture and it does not refuse the work:**

```
I will not write interviews as though they happened. The document would carry
evidence weight it has not earned, and three documents downstream nobody can
tell the difference. That is not a caveat problem; footnotes do not survive
being copied into a deck.

Here is what I can do in the next two hours instead.

1. The honest research section. Twenty minutes. It says what you actually
   know, at what confidence, with the gaps named. A board reading "we have not
   spoken to customers about this yet, here is the plan and the date" respects
   it more than eight summaries that fall apart under one question.

2. Whatever real evidence you already have. If you have support tickets, sales
   call notes, app store reviews or churn records, I can code them properly in
   about an hour and the section becomes real. Most teams have far more of this
   than they think.

3. Rehearsal transcripts, stamped. If you want to practise the guide before
   real sessions, I will play a participant. Every file carries
   SYNTHETIC - NOT EVIDENCE at the top and bottom and the filename starts with
   SYNTHETIC_. Useful for practice, and it can never quietly become a source.

4. The recruiting plan that gets you five real sessions inside two weeks, so
   the next board meeting has the real thing.

Which of those do you want first?
```

**If you insist**, it does it, once, stamped, and does not argue a second time. The stamp
is the protection, not the argument.

---

## 4. A metric moved

**You:**

> Activation dropped 8% last week. What happened?

It does not start interviewing people.

```
Mode: ASSESS

Before anything else: has it actually moved? Roughly half of investigated
metric movements are measurement artefacts, and every hour spent theorising
before this check is wasted.

Step 1, today, 30 minutes:
  - Any tracking release, SDK version bump, or event definition change in the
    window?
  - Bot and crawler traffic, filter changes, a backfill?
  - Timezone or reporting-window boundary?
  - Does a metric that should NOT have moved also show a drop? If yes, the
    cause is measurement.

Step 2, today: where is it concentrated? Segment by acquisition source,
platform, app version, geography, plan, device, new versus returning. A drop
spread evenly across every segment is usually external or measurement. A drop
in one slice is usually a change.
  Run: cohorts_funnels.py simpson --csv breakdown.csv
  If the aggregate moved and no segment did, the mix changed and there is no
  behaviour change to explain.

Step 3: the change log. Releases, pricing, campaigns, outages, competitor
moves, holidays.

Step 4: which transition changed?
  Run: cohorts_funnels.py funnel --csv events.csv --steps ... --segment platform

Step 5, and only now: six interviews recruited specifically from the affected
slice, asking about the specific episode, not about the metric.

Interviews cannot answer "why did this move" on their own. They can only
explain the slice that steps 1 to 4 identify. Running them first samples the
wrong people and produces a confident story about the wrong thing.
```

---

## 5. Designing an interview

**You:** `/discovery-interview design` for a study about how small retailers track stock.

You get the full guide, checked against the banned question forms before it is handed over.
An extract:

```
## The story (20-25 min)

Opener: "Tell me about the last time you ran out of something a customer wanted."

Probes to have ready:
  - What happened next? What did you do just before that?
  - Walk me through it step by step. What did you have open in front of you?
  - How long did that take? When was the last time before this one?
  - What did that cost you?
  - How do you handle that today? Is there a workaround? Can you show me?
  - Have you ever looked for a tool for this? What did you find?
  - [three seconds of silence]

## Do not ask
  Would you use it            How much would you pay
  Do you like it              How important is X, 1 to 5
  What features do you want   Don't you think
  How frustrating is X        Would it be helpful if
```

Note the second-to-last probe. "Have you ever looked for a tool for this?" is the best
proxy for importance that exists in an interview, because someone who has already searched
has revealed how much the problem matters. Asking "how important is this, one to five" gets
a number that means nothing.

---

## 6. Setting a test threshold

The threshold is written before the test runs, and the inconclusive band is written with it.

```
We believe:      Merchants will pay a 5% commission for guaranteed same-day delivery.
We will:         Offer it at 5% to the next 60 merchants who open the delivery screen.
We measure:      Share who accept AND complete at least one paid delivery within 14 days.
We are right if: at least 12 of 60 accept AND at least 8 complete a paid delivery.
We are wrong if: fewer than 5 accept.
In between:      inconclusive. Second round at 3% before deciding.
Decided on:      2026-04-02, before any data was collected.
```

The "in between" line is what stops every result becoming a success. Where the numbers come
from is the business case: what acceptance rate would make this worth building?

---

## 7. When it tells you not to bother

**You:**

> Can you design a survey to find out if our users want dark mode?

```
Mode: ASSESS

Not recommended, and here is the specific reason rather than a general one.

Complete this sentence first: "If we learn X we will do A, if we learn Y we
will do B." For dark mode, both branches usually lead to the same action.
If 70% say yes you build it. If 40% say yes, someone argues it is still worth
it and you build it. A study whose two outcomes lead to the same place cannot
pay for itself.

Also, the instrument is wrong for the question. "Would you like dark mode" gets
a yes from almost everyone, because it costs the respondent nothing to say so.
That is stated preference, L2 on the evidence ladder, and it cannot tell you
whether anyone will use it.

Cheaper things that would actually inform a decision:
  - Search your support tickets and reviews for "dark", "night" and "eye". The
    volume and the language tell you more than a survey and it is free.
  - Check what share of your users have their OS set to dark. You may already
    have this in your analytics. It is observed behaviour, L4, and it beats
    asking.
  - If you build it, ship it behind a flag and measure adoption. That is the
    only number that settles it.

And if the real motive is that a stakeholder wants evidence before approving,
say so. That is a legitimate goal and it needs a much cheaper instrument than
a decision-grade study.
```

---

## 8. When it is not consumer software

Every example above is software with a voluntary user. Here is what changes when it is not.

**You:**

> I own an internal expense tool at a 12,000-person company. Everyone complains about it.
> Usage is 100% because they have no choice. Where do I even start?

```
Mode: ASSESS

market = internal or captive. Three things change before anything else.

1. Adoption and engagement are meaningless. They cannot leave. 100% is the mandate.
   Use task cost instead: time to submit at median and p90, rework rate, rejection
   and resubmission rate, help-desk contacts per 100 submissions, finance hours
   spent correcting. Business case = fully-loaded minutes x frequency x 12,000.

2. Your first study is a query, not research. Workflow audit trails, approval and
   rejection logs, help-desk tickets by category, exports people take. Two days, no
   recruiting, no consent, no procurement.
   Add the shadow-process indicator: what people do in a spreadsheet instead.

3. Separate policy pain from tool pain before coding a single complaint. Much of
   what everyone complains about is a rule owned by Finance or Audit that you
   cannot change. Mixing them gives you a backlog you are not allowed to fix.

Ladder note: fake doors and adoption say nothing here. Your commitment signal is
unpaid effort. Someone maintaining a shadow spreadsheet has told you more than any
satisfaction survey will.

Next: pull help-desk tickets by category for two quarters and the rejection rate by
expense type. Then find three people who keep their own spreadsheet and ask to see it.
```

The same shift happens for hardware sold through distributors, clinical tools, public
services and marketplaces. Eight market rows, each replacing the parts of the default model
that do not survive that context. Full set in
`skills/product-discovery/references/01-intake-and-routing.md`, Step 3a.
