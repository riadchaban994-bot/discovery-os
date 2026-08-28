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

---

## 1. "Should we build this?"

**You:**

> Our merchants keep asking for a bulk product upload. Should we build it? We have about
> 3,000 active merchants and decent analytics.

**It does not answer the question as asked.** It finds the real one first, states what it
inferred so you can correct it, and asks only what it cannot infer.

```
Mode: ASSESS

The real question is not whether to build bulk upload. It is which risk is
unresolved for it. "Merchants ask for it" is a feature request, which is the
visible end of a story about something that went wrong. The job is to find
that story and then decide what actually addresses it.

Inferred from what you wrote, correct anything wrong:
  customer_access    scheduled (you have 3,000 merchants you can reach)
  instrumentation    full analytics
  volume             ~3,000 active, so a surface-level A/B is marginal
  product_state      live
  market             B2B SMB  [ASSUMPTION, confirm]

Three questions:
  1. What decision does this change? Is bulk upload competing with something
     else for the same build slot, or is this a yes/no on its own?
  2. Roughly how many merchants have asked, out of 3,000, and where did the
     asks come from? Support, sales, or one large account?
  3. Do you know how many products a typical merchant lists in their first
     week, and how that compares to merchants who stay?
```

Once you answer, it routes:

```
Method: trace mining first, then five interviews. Two days, then one week.

Why this beats the alternatives here:
  - You have a live product, so the cheapest evidence already exists and is
    free. Search logs, support tickets mentioning upload or import, session
    replays of the add-product flow, and the drop-off in first-week listing
    counts. That is two days and it sharpens everything after it.
  - A survey is wrong for this. It would tell you how many merchants like the
    idea of bulk upload, which they will, and nothing about what they were
    trying to do.
  - An A/B test is not available yet. At 3,000 active merchants the surface
    does not have the volume to detect a realistic effect in a sensible
    window. Run sample_size.py against your real numbers to confirm.

What this will not tell you:
  Whether merchants would pay more, or stay longer, if it existed. Trace
  mining and interviews establish the problem and its shape. Willingness to
  pay needs a commitment test, and retention impact needs an experiment you
  cannot currently run.

Cost: 2 analyst days, then 5 sessions over one week. One person.

Open assumptions:
  1. Merchants asking are representative of merchants who matter. Unverified.
     Check the revenue concentration of the askers before weighting them.
  2. Market is B2B SMB. If any of these are enterprise accounts, the sample
     logic changes.

Next action: pull every support ticket and search query containing upload,
import, bulk or csv from the last 90 days, and count distinct merchants.
```

---

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
