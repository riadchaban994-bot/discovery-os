# Experiment runbooks

How to actually execute the tests. `../product-discovery/references/02-method-index.md` chooses
the method; this file runs it. Each runbook: setup, what to measure, thresholds, how long,
and the mistake that invalidates it.

---

## Painted door / fake door

**Setup.** Add a real-looking entry point on a surface the target user already visits. On
click: an honest page saying it is being built, plus one intent capture (email, or a "notify
me" that requires a real action).

**Measure.** Impressions, click rate, intent-capture rate among clickers, and the same
figures for a comparable existing entry point as a reference.

**Thresholds.** Set from the business case before launching. Anchor to a comparable
existing feature's click rate, never to an industry benchmark. A rule of thumb: if the
click rate is below half of a comparable existing entry point, demand is weak.

**Duration.** One to two weeks, and at least one full weekly cycle. Never more than three
weeks; a fake door running for a month is a broken promise.

**Invalidating mistakes.**
- Placement in a location nobody visits, so a null result measures placement not demand
- No honest message, which is a trust cost you cannot repay
- No comparison point, so the number is uninterpretable
- Counting clicks as demand. A click is curiosity. The intent capture is the signal
- Leaving it running after the decision is made

**Ethics.** Disclose immediately on click. Never take money. Actually follow up with the
people who signed up, even if the answer is "we decided not to build it".

---

## Demand landing page with paid traffic

**Setup.** A page describing the value proposition in customer language, one call to action,
traffic bought from search or social against a defined audience. Two or three value
propositions running against each other.

**Measure.** Cost per click, click-to-signup, cost per signup, by proposition.

**Thresholds.** Relative, always. Which proposition wins and by how much. An absolute
conversion rate with nothing to compare it to means nothing.

**Duration.** Until 300-500 clicks per variant, typically three to seven days.

**Invalidating mistakes.**
- One proposition only
- Audience too broad, so you measure targeting rather than proposition
- Reading an absolute conversion rate as market demand
- The page promises something the product could not deliver

---

## Concierge

**Setup.** Deliver the outcome manually, for real customers, who know it is manual. Charge
if the real product would charge.

**Measure.** Do they come back? Do they pay? What does the real workflow turn out to be?
What breaks? How long does each delivery take, and does that fall with practice?

**Thresholds.** Repeat usage is the signal. One delighted delivery proves nothing;
three repeat requests from the same customer is real evidence.

**Duration.** Two to six weeks, five to fifteen customers.

**Invalidating mistakes.**
- Doing it for friends
- Not charging when the real product would
- Optimising the manual process instead of learning from it
- Never stopping. Set an end date at the start

---

## Wizard of Oz

**Setup.** A real-looking interface with a human doing the work behind it. Users do not know.

**Measure.** Behaviour as if the product were real: usage, repeat, task completion, what
they ask for that you did not anticipate.

**Duration.** One to three weeks. Constrained by human throughput.

**Invalidating mistakes.**
- Response latency far from what the real system would give, so the behaviour does not
  transfer. Deliberately match the intended timing, including delays
- The human doing a much better job than the system ever could, which produces a positive
  result you cannot reproduce
- Running past the point where the operator is exhausted, which degrades the data

**Ethics.** Acceptable where output quality matches what is promised. The operator must not
see sensitive data without disclosure. If the human is doing something the system will
never do, you are testing a different product.

**Especially useful for AI features:** test the experience before the model exists, and
learn what accuracy threshold the experience actually needs.

**Do not run this at all** where the concealed output is a clinical, diagnostic, financial,
legal or safety judgement, or on a statutory service. A human silently generating a
recommendation that a professional believes came from a checked system is a safety hazard,
is very likely a regulated-device or professional-practice violation, and a debrief
afterwards does not fix it. **Shadow mode** is the substitute: run the logic, log what it
would have done, show nobody, and compare against what actually happened.

---

## Pre-sale, deposit, letter of intent

**Setup.** Offer the thing at the real price with a dated delivery. Take a refundable
deposit, a prepay, or a signature.

**Measure.** Conversion from qualified conversation to commitment. Not interest.

**Thresholds.** In B2B, five signed LOIs from economic buyers out of twenty qualified
conversations is strong. In B2C, compare against your existing pre-order conversion.

**Invalidating mistakes.**
- Testing a price you will not charge
- A champion signing when they have no budget authority
- Discounting to get the signature, which tests the discount
- No delivery date, which makes the commitment meaningless

**Ethics.** Refund policy stated up front and honoured without friction. If you decide not
to build, refund immediately and tell them why.

---

## Comparison prototype test

**Setup.** Two or three prototypes at equal fidelity. Same session. Order counterbalanced
across participants so the first option does not systematically win.

**Measure.** Which they choose, why, what they would use it for, what it would replace,
what is missing. Watch for a specific past situation they can name.

**Thresholds.** Qualitative. The signal is whether they can place it in a real, recent
situation. Enthusiasm without a situation is politeness.

**Sample.** Five to eight per segment. More rounds beats a bigger single round.

**Invalidating mistakes.**
- Showing one option
- Unequal fidelity, so the polished one wins on polish
- Showing before the story has been collected
- Asking "do you like it"

---

## Moderated usability test

**Setup.** Realistic tasks in the participant's own words, not the interface's labels.
Think-aloud. Moderator does not help until the task is genuinely dead.

**Measure.** Task success, time, errors, where they hesitate, what they say at the moment of
confusion, severity of each problem.

**Sample.** Five per round per segment, three rounds, fixing between rounds.

**Thresholds.** Severity-rated problem list. A problem seen in three of five is a design
defect, not a participant quirk.

**Invalidating mistakes.**
- Task phrased in the interface's own words
- Rescuing
- Testing with people who already know the product when the question is about new users
- One round of fifteen instead of three rounds of five

---

## Controlled experiment (A/B)

**Setup.** Pre-registration written and shared. Randomisation checked with an A/A test if
the platform is new. Assignment logged at exposure.

**Measure.** One primary metric, two or three guardrails, secondaries labelled exploratory.

**Before reading anything:** sample ratio mismatch check.

**Duration.** Whole weeks, minimum one full weekly cycle, calculated from
`../discovery-quant/scripts/sample_size.py`. Stop at the planned point, not on a good day.

**Invalidating mistakes.**
- Peeking without a sequential design
- Choosing the primary metric after seeing the results
- Ignoring SRM
- Shipping on a result whose interval includes a business-irrelevant effect
- Reading a novelty spike as a durable effect

---

## Holdout

**Setup.** A persistent randomly-withheld slice, 1-10 percent, excluded from a programme
(CRM, promotions, recommendations) for a defined period.

**Measure.** The difference in the outcome metric between held-out and treated.

**Why it matters more than teams think.** A promotion programme without a holdout cannot
report incrementality. Redemption is not incrementality: many redeemers would have converted
anyway. The same applies to recommendation systems, retention campaigns and lifecycle email.
If a programme has never had a holdout, its reported value is unmeasured.

**Invalidating mistakes.**
- The holdout leaks (users switch devices, or are reached through another channel)
- The holdout is too small to detect the effect
- The holdout is not random

---

## Technical spike

**Setup.** A written brief: the specific unknown, the timebox, what a positive and a
negative result each look like, and where the finding gets written down. Engineer-owned.

**Measure.** Whatever the unknown was, measured at the percentile that matters.

**Invalidating mistakes.**
- The question is "is this hard" rather than a specific unknown
- The timebox is not enforced
- The output is a conversation rather than a written finding
- Success is declared on a happy path that ignores error handling and scale
