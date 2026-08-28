# Intake and routing

The job of this file is to turn a vague request into one named method, chosen for the
evidence the team actually has rather than the evidence they wish they had.

---

## Step 1: find the real question

Users describe discovery work in solution language. Translate before routing. Say the
translation out loud once, then route on the translation.

| What they say | What they are usually asking | Route |
|---|---|---|
| "Should we build X?" | Which of the four risks is unresolved for X? | Assumption map first, then risk-specific method |
| "Can you validate this idea?" | What evidence would make us confident enough to commit? | Assumption map, then Q3 below |
| "We need user research" | What decision is stuck? | Fill the Decision slot before anything else |
| "Make me a persona" | Who are we building for and what do we know about them? | Segmentation from real traces, or interviews |
| "Users are complaining about X" | How widespread is X, and what is underneath it? | Trace mining for prevalence, interviews for cause |
| "Our competitor launched Y" | Does Y address a need our customers have? | Opportunity check, not a feature-match exercise |
| "The CEO wants Z" | What would change the CEO's mind, and is that reachable? | Assumption map on Z, evidence-based challenge |
| "Retention is bad" | Bad relative to what, for whom, from when? | Diagnostic sequence in `discovery-quant` |
| "We need to prioritise the roadmap" | Do we have real opportunities to prioritise, or a wish list? | Check the source of the list first |
| "Run an A/B test on this" | Is randomisation possible and is the effect detectable? | Power check before design |
| "What's the market size?" | What decision needs the number, and to what precision? | Sizing, with inputs exposed |
| "Write the PRD" | Has discovery happened? | AUDIT the evidence behind it before writing |

**The most valuable single move in intake** is asking what happens if the answer comes
back negative. If nobody can say, the request is not a decision, and the right response
is to say so kindly and reframe.

---

## Step 2: the fifteen questions

Every discovery request reduces to one of these. Pick one. If two apply, sequence them.

### Q1. Is this problem real, and for whom?

| `customer_access` | `product_state` | Primary method | Sample | Fallback if blocked |
|---|---|---|---|---|
| on demand / scheduled | any | Story-based interviews, continuous | 5-8 per segment, then to saturation | n/a |
| slow | live | Trace mining first (tickets, sales calls, reviews, search logs, session replay), then interviews | full corpus, then 5 interviews | n/a |
| none | live | Trace mining only, conclusion marked provisional | full corpus | Open a parallel workstream to fix access. Access is the real blocker |
| none | concept | Secondary research plus expert interviews plus proxy communities | 5-10 experts or forum threads | Say plainly: no primary evidence is available, so everything is a hypothesis |

**Enterprise and government variant.** Access exists but is politically gated. Route
through the account manager or the sponsoring department, offer to run the session with
them present, and accept n=5 as a real sample. Do not substitute a survey.

**Never route this question to:** a survey asking whether people have the problem. People
under-report problems they have normalised and over-report problems they have just been
reminded of.

### Q2. Which opportunity do we take first?

**Precondition, non-negotiable.** The opportunity set must be derived from customer
evidence. Prioritising a brainstormed list produces a confident ranking of guesses.

| Situation | Method |
|---|---|
| Opportunities sit under one outcome and are comparable | Opportunity solution tree, then Torres's four sizing criteria: opportunity size, market factors, company factors, customer factors |
| Opportunities compete across outcomes | Force a single outcome first. Cross-outcome prioritisation is a strategy decision, not a discovery one |
| Need a defensible score for stakeholders | RICE or WSJF, with every input's source shown. Publish the inputs, not just the score |
| Need to know which unmet needs matter most, at scale | Outcome-Driven Innovation opportunity scoring: importance and satisfaction on desired-outcome statements, n>=180 for segment-level reads |
| Need to know which attributes delight versus which are expected | Kano questionnaire, functional and dysfunctional pairs, n>=100 |
| Small team, no scoring appetite | Assumption-map the top three and let the evidence sort them |

**Scoring frameworks are argument structuring devices, not measurements.** A RICE score
is exactly as good as its reach and impact inputs. Show the inputs or do not show the
score.

### Q3. Will this solution deliver the outcome?

Split by which of the four risks is actually open. (Cagan: value, usability, feasibility,
business viability. Torres adds ethical, which is worth keeping.)

| Risk open | `volume` | Method | Evidence level |
|---|---|---|---|
| Value | over 1k/wk on the surface | Painted door or fake door with intent capture, honest close | L5 |
| Value | under 1k/wk, B2C | Concierge or Wizard of Oz with 5-15 real users | L4-L6 |
| Value | B2B enterprise | Letter of intent, paid pilot, or reference-customer commitment | L6 |
| Value | concept only | Comparison prototype test in interviews, plus demand landing page | L2-L5 |
| Usability | prototype exists | Moderated usability test, 5 per round, 2-3 rounds | L4 |
| Feasibility | any | Technical spike, timeboxed, engineer-owned, written finding | L4 |
| Viability | any | Unit economics model with real cost inputs, plus channel and CAC test | L3-L6 |
| Ethical | any | Structured harms assessment plus premortem before build | n/a |

**The single-solution trap.** Never test one solution alone. A solution tested alone gets
a warm reception because participants are polite and have nothing to reject it against.
Test two or three, ask which and why, and the differences do the work. (Torres calls this
compare and contrast.)

### Q4. Can people use it?

Moderated usability testing, five participants per round, three rounds beats fifteen
participants in one round because you fix between rounds. (Nielsen and Landauer's five-user
finding is about *interface problem discovery* on a homogeneous user group. It is not a
sample-size rule for anything else, and it does not hold across distinct segments; five
per segment.)

| Need | Method |
|---|---|
| Find interface problems | Moderated usability test, think-aloud, task-based |
| Test at scale or without a moderator | Unmoderated remote test, 15-30, expect noisier data |
| Test navigation and labels before design | Tree test and first-click test |
| Test information structure | Card sort, open then closed |
| Test comprehension of a page in isolation | 5-second test |
| Cheap pre-check before spending on participants | Heuristic evaluation, 3 evaluators, plus cognitive walkthrough |
| Statutory or contractual accessibility need | Accessibility audit against WCAG, plus at least two sessions with users of assistive technology |

### Q5. Can we build it?

Only an engineer can answer this. The skill's job is to shape the question, not to answer
it. Produce a spike brief: the specific technical unknown, the timebox, what a positive
and negative result each look like, and what gets written down. Feasibility is answered by
building the risky part, never by discussion.

Common feasibility unknowns that need a spike rather than an opinion: third-party API
behaviour under real load, data availability and quality for a model, latency at the
required percentile, migration path for existing records, offline behaviour, cost per
transaction at scale.

### Q6. Does the business case hold?

Build the model before the research, so the research knows what precision it needs.

Minimum viable model: acquisition volume, conversion, price, cost to serve, retention
curve, payback period. Mark each input with its evidence level. The output range is
determined by the weakest input, and the weakest input tells you what to research.

Route to `discovery-quant` for the model, `discovery-experiments` for the pricing and
channel tests that feed it.

### Q7. Could this harm someone?

Run before build. Structured harms assessment with these prompts, answered in writing:

- Who could be harmed by this working exactly as intended?
- Who could be harmed by it failing, and how would they know?
- What does the worst-behaved 1% of users do with this?
- What happens to someone excluded by the model, the rule, or the design?
- What data does this create, who can see it, and what happens if it leaks?
- Would we be comfortable if this were reported accurately in public?
- In regulated or government contexts: which obligation applies, and who signs it off?

Output is a written risk list with owners, not a discussion.

### Q8. Which of these options is best?

Compare and contrast, always. Two to three options, same participants, order
counterbalanced across the sample so the first option does not systematically win. Ask
which and why. Probe the why until it reaches a need, not a preference.

Never ask participants to rank features. Feature ranking measures the vividness of the
description, not the value of the feature.

### Q9. Why did this metric move?

**Sequence matters. Do not start with interviews.**

1. Verify the metric moved. Tracking change, instrumentation break, bot traffic, timezone
   or reporting-window artefact, definition change. Roughly half of investigated metric
   movements are measurement artefacts. Check this first, every time.
2. Decompose. Segment by acquisition source, platform, geography, cohort, plan, device,
   app version. Find where the movement concentrates. A movement everywhere is usually
   external or measurement; a movement in one slice is usually a change.
3. Correlate with the change log. Releases, pricing changes, campaigns, outages,
   competitor moves, seasonality, calendar events.
4. Isolate the step. Funnel decomposition to find which transition changed.
5. Only now, interviews. Recruit specifically from the affected slice, and ask about the
   specific episode, not about the metric.

Steps 1 to 4 live in `discovery-quant`. Step 5 in `discovery-interviewing`.

**Simpson's paradox check is mandatory at step 2.** An aggregate that moves while every
segment holds steady means the mix changed, not the behaviour.

### Q10. Did our change cause this?

| Can you randomise? | Volume sufficient for power? | Design |
|---|---|---|
| Yes | Yes | Controlled experiment, pre-registered OEC and guardrails |
| Yes | No | Do not run an underpowered test. Use a qualitative plus commitment route, or accumulate over a longer window with a pre-committed stop rule |
| No (interference between users) | Yes | Switchback, cluster or geo randomisation |
| No (rollout already happened) | Yes | Difference-in-differences with a control group and a parallel-trends check, or interrupted time series, or synthetic control. Label as quasi-experimental and state the identifying assumption |
| No, and no control exists | Either | You cannot answer this causally. Say so. Offer the best associational read plus the competing explanations |

Full design and analysis guidance in `discovery-experiments`.

### Q11. What will people pay?

Ordered by evidence strength, weakest first. Use the strongest one your situation allows.

1. Direct question ("how much would you pay"): L2, near worthless alone, useful only as
   conversation opener
2. Van Westendorp price sensitivity meter: L2, gives an acceptable range, not a price
3. Gabor-Granger: L2, purchase-intent curve at price points
4. Conjoint or MaxDiff: L2-L3, good for relative feature and price trade-offs at n>=200
5. Pricing page A/B with real checkout: L7 where volume allows
6. Pre-sale, deposit, or annual prepay at the tested price: L6
7. Signed letter of intent or paid pilot in enterprise: L6

**Rule.** Never set a price from stated-preference research alone. Use it to pick which
prices to test with commitment.

### Q12. Do we have product-market fit?

Retention curve first. If the curve does not flatten, there is no fit and no survey will
change that. Cohort retention by weekly or monthly cohort, plotted, looking for a plateau
above zero in the core-action metric, not in logins.

Then, and only then, the Sean Ellis survey: "How would you feel if you could no longer use
[product]?" with very disappointed / somewhat disappointed / not disappointed. The 40%
threshold is a widely used heuristic, not a law, and it is only meaningful among users who
have actually experienced the core value at least twice. Segment the "very disappointed"
group and study them; that segment is the signal, not the headline percentage.

Supporting reads: cohort revenue retention for B2B, organic and referral share of
acquisition, and whether growth continues when paid spend pauses.

### Q13. Why are people leaving?

Quantitative first, qualitative second, and recruit from the right population.

1. Define churn precisely: cancelled, or dormant for N days? They have different causes.
2. Find when: survival curve, time-to-churn distribution. Early churn is onboarding and
   expectation-setting; late churn is value decay or competitive displacement.
3. Find who: churn rate by segment, plan, acquisition source, first-week behaviour.
4. Find the leading indicator: which behaviour in week one predicts month-three retention.
5. Interview churned users, not current ones. This is the step teams skip because churned
   users are hard to reach. It is the only step that explains anything.
6. Cancellation-flow surveys are the weakest instrument here. They capture the last straw
   and the socially acceptable reason, not the cause.

### Q14. What do we already know?

Almost always the first study to run, and almost always skipped. Corpus: past research,
support tickets, sales call recordings and CRM loss reasons, app store and G2 reviews,
NPS verbatims, session replays, search-inside-product queries, community and social
mentions, churn exit notes, onboarding drop-off points.

Route to `discovery-synthesis`. Output is a coded corpus with an explicit map of what is
known, what is contested, and what is absent. The absences are the research plan.

### Q15. How do we run discovery continuously?

Route to `discovery-ops`. The core move is a standing weekly customer touchpoint owned by
the trio, with recruiting automated so next week is always booked, and an opportunity
solution tree that is updated rather than rebuilt.

---

## Step 3: apply the evidence overrides

Run these checks after selecting a method. Any one of them can veto the choice.

| Check | If it fails |
|---|---|
| Does the method's precondition hold given the evidence inventory? | Switch to the fallback in the method card |
| Can the sample actually be recruited in the time box? | Reduce scope or extend. Do not silently plan an unrecruitable study |
| Is the surface high enough traffic for the design? | Run the power calculation before committing. `../discovery-quant/scripts/sample_size.py` |
| Does the result arrive before the decision must be made? | A study that lands after the decision is theatre. Redesign for the deadline |
| Does anyone own acting on the result? | Name them now |
| Is there a cheaper method one rung down that would settle it? | Take it |
| Would a negative result actually be accepted? | If not, this is advocacy. Say so and reframe |

---

## Step 4: sequencing

Most real questions need two methods, in order. The pairs that matter:

| Pair | Order | Why |
|---|---|---|
| Quant then qual | Always, for "why did X happen" | Quant finds where and who; qual explains why. Reversed, you interview the wrong people |
| Qual then quant | Always, for "how common is this" | Qual finds the phenomenon and the language; quant sizes it. Reversed, you measure the wrong thing |
| Trace mining then interviews | Always, when a live product exists | Free, fast, and it sharpens the interview guide |
| Prototype then experiment | For value risk | Cheaper to fail in a prototype |
| Interviews then survey | Never survey first | A survey written without qualitative grounding measures the author's assumptions |

**The one-line rule.** Qualitative tells you what exists and why. Quantitative tells you
how much and how often. Neither substitutes for the other, and a request that needs both
gets both or gets an honest caveat.

---

## Step 5: write the routing decision down

```
## Routing decision
Real question: Q9, why did activation drop
Evidence state: instrumentation=full, volume=12k/wk, access=scheduled, market=B2C
Method: diagnostic sequence (steps 1-4), then 6 interviews recruited from the affected
        Android cohort
Rejected: immediate interviews (would sample the wrong users), survey (cannot answer why
          at the level of a specific episode)
This will not tell us: whether the drop is caused by the release or by the campaign mix
        change, unless step 3 separates them cleanly
Decision it feeds: whether to roll back release 4.2 by Friday
Cost: 2 analyst days, 6 sessions over 5 working days
```
