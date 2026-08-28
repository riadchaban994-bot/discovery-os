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
| any | non-consumer market | **A13 first**: the operational or regulatory records you already hold. Then interviews | full corpus | This is free, needs no recruiting, and is the step most often skipped |
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
| Value | B2B enterprise | Letter of intent, paid pilot, or reference-customer commitment from the economic buyer | L6 |
| Value | channel-sold | A distributor stocking order at their own risk, or a design win at the customer engineering team. **Not** an LOI from an end user who does not buy | L6 |
| Value | clinical or regulated | Shadow mode, then a stepped-wedge rollout. Deceptive tests are prohibited here | L6-L7 |
| Value | concept only | Comparison prototype test in interviews, plus demand landing page | L2-L5 |
| Usability | prototype exists | Moderated usability test, 5 per round, 3 rounds | L4 |
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
**Substitute the stack for your market first** (Step 3a): channel margin for channel-sold,
fully-loaded time saved for captive and internal, both sides for a marketplace. The default
above is consumer-shaped and will show a viable product that is not.

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
   or reporting-window artefact, definition change. `[HEURISTIC]` a large share of
   investigated metric movements turn out to be measurement artefacts rather than behaviour.
   Check this first, every time. The cost of checking is an hour; the cost of skipping it is
   a week of theorising about a tracking bug.
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
| Withholding it permanently is not acceptable (clinical, public service, internal rollout) | Enough units | Stepped wedge, randomised crossover order |
| Showing the output carries real risk | Any | Shadow mode first, then a controlled rollout |

Full design and analysis guidance in `discovery-experiments`.

### Q11. What will people pay?

Ordered by evidence strength, weakest first. Use the strongest one your situation allows.

1. Direct question ("how much would you pay"): L2, near worthless alone, useful only as
   conversation opener
2. Van Westendorp price sensitivity meter: L2, gives an acceptable range, not a price
3. Gabor-Granger: L2, purchase-intent curve at price points
4. MaxDiff for relative importance across a long item list, n>=200. Choice-based conjoint
   for price and bundle trade-offs, n>=250. Both L2-L3
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

Almost always the first study to run, and almost always skipped. Consumer-software corpus:
past research, support tickets, sales call recordings and CRM loss reasons, app store and G2
reviews, NPS verbatims, session replays, search-inside-product queries, community and social
mentions, churn exit notes, onboarding drop-off points.

**Outside consumer software that list is the wrong one.** Start with A13, the operational and
regulatory records the organisation already holds: the EHR audit log, distributor sell-through
and RMA records, case management and inspection data, workflow audit trails, transaction and
exception logs. No recruiting, no consent process, no procurement. And in any domain with a
published literature, A14, a structured literature review, graded on each source's own design
rather than as desk research.

Route to `discovery-synthesis`. Output is a coded corpus with an explicit map of what is
known, what is contested, and what is absent. The absences are the research plan.

### Q15. How do we run discovery continuously?

Route to `discovery-ops`. The core move is a standing weekly customer touchpoint owned by
the trio, with recruiting automated so next week is always booked, and an opportunity
solution tree that is updated rather than rebuilt.

---

## Step 3a: apply the market override

`market` is collected at intake and it is the field teams get wrong most often. Every value
below replaces part of the default model. Read the row for your market before reading any
method card, because these change what "good" even looks like.

### B2C mass
The default the rest of this skill is written against. Voluntary users, demand signals
available, volume usually sufficient for experiments.

### B2B SMB
Smaller n, buyer and user often the same person, churn visible monthly. Interviews reach
saturation faster because the segment is narrower. Commitment evidence via pre-sale or
annual prepay is usually available.

### B2B enterprise
Sample sizes are small by nature. Weight depth, triangulation and commitment evidence.
Statistical significance is usually unavailable and pretending otherwise is worse than
admitting it.
**Metric model:** account-level, not user-level. Seat usage against contracted seats, ticket
severity, sponsor turnover, whether the original business case was ever measured. Survival
curves and week-one leading indicators are user-churn tools and become noise below about 100
accounts. Do not plot Kaplan-Meier on thirty-four accounts.
**Roles:** buyer, user, approver and blocker are four different interviews. The person who
signs the renewal may never open the product.
**Politics:** researching an account inside an active renewal cycle reads to the customer as
a save motion, and the account executive's commission is exposed. Agree the approach with
them first, and say what the research is for.

### Channel-sold (distributors, resellers, OEM, retail)
**The gatekeeper's interests oppose the research.** A distributor has an active margin
incentive to prevent you talking to end users, because disintermediation is the threat.
Treat the distributor as a customer in their own right with their own buying criteria:
stocking cost, channel margin, support burden, shelf or catalogue space. Those have nothing
to do with end-user value and they decide whether you sell anything.
**Commitment signal:** a stocking order placed at the distributor's own risk, or a design
win at the customer's engineering team. Not end-user enthusiasm relayed to you.
**Unit economics** must carry the channel margin stack. `[HEURISTIC]` in industrial
distribution it is commonly a substantial share of list price, often a quarter to
two-fifths, but it varies enough by sector that you must get your own numbers from the
actual contracts rather than planning against a range from a document. A model without it can show a viable product that is not.

### Marketplace or two-sided
**Diagnose liquidity before you diagnose product.** Supply-side retention is usually a
distribution problem: if the top decile of suppliers takes most of the work, everyone else
churns because they never got a second job. A retention curve for a supplier who received
zero matches is a meaningless number.
**Check the ratio first.** Suppliers to buyers, and jobs to suppliers. A heavily
supply-saturated marketplace has a demand problem that no supply-side retention work will
fix.
**Metric model:** match rate, fill rate, time to first match, share of suppliers with at
least one match per period, retention **conditioned on having received a match**, take rate.
**Segment by the unit of liquidity**, not by platform or device. Language pair, city,
category, vehicle class. Two language pairs are two marketplaces and aggregating them is a
Simpson's paradox waiting to happen.
**Every experiment needs a metric on both sides and a joint overall evaluation criterion.**
A change that spreads work more evenly to help supply retention usually costs the demand
side speed or quality. Randomise by time block, cluster or geo, never by user.

### Internal tools and captive users
**Adoption is meaningless.** They cannot leave. See the captive-user block in
`references/03-evidence-ledger.md` before grading anything.
**Metric model is task cost, not usage:** time to complete, error and rework rate, rejection
and resubmission rate, help-desk contacts per hundred transactions, and hours the receiving
team spends correcting. The business case is fully-loaded minutes times frequency times
headcount, which finance accepts as a hard number.
**The shadow-process indicator is the most honest signal a captive tool emits.** What are
people doing in a spreadsheet instead, and why.
**Separate policy pain from tool pain before coding a single complaint.** In expense,
procurement, HR and compliance tools, a large share of what "everyone complains about" is a
rule owned by Finance, Audit or Legal that the product team cannot change. Mixing the two
produces a backlog of things you are not allowed to fix.

### Government and public service
**The outcome is a duty, not a growth target.** Judged against a statutory or published
service standard: time to resolve, repeat contact rate, and equity of service across
districts or demographics. Not volume.
**Ground truth does not come from users.** Reports received measures reporting propensity,
not incidence. Get incidence from the operational source: inspection crews, contractors,
sensors, case records. Otherwise you optimise for the districts that already complain.
**The excluded population is the research question**, more often than the served one.
**Incentives** for participants are restricted or prohibited in many public contexts. Check
before designing recruitment around them.
**A commitment made upward is usually not reversible.** When a director has promised a
minister or a mayor, "change their mind with evidence" is startup advice that ends careers
in a hierarchy. The move is to keep the commitment and use discovery to decide what it
resolves to in practice, so the promised thing lands on a real operational problem.

### Clinical, regulated and safety-critical
**Find out what the constraint actually forbids before accepting it.** Research on
professionals using a tool is often quality improvement or non-human-subjects work and
frequently exempt; it becomes regulated research when it touches patient outcomes or seeks
generalisable knowledge. Getting that determination is usually a short conversation and it
opens most of the study.
**Two designs exist that ethics committees routinely accept**, and both are missing from
most product teams' vocabulary: **shadow or silent mode**, where new logic runs without
being displayed and you compare what it would have done against what happened, carrying
essentially no risk; and the **stepped-wedge rollout**, where every unit receives the
intervention eventually and the order is randomised, which is why it gets approved.
**Published literature is not L1 here.** See `references/03-evidence-ledger.md`.
**Deceptive tests are prohibited.** No fake doors, no Wizard of Oz, no concealment of who or
what is generating a clinical, financial or legal output.

---

## Step 3b: name the external gates

Four things determine when discovery must happen and which methods are purchasable at all.
They are not deadlines. A deadline shortens the plan; a gate reorders it and removes options.

| Gate | Typical lead time | What it removes |
|---|---|---|
| Procurement | 1 to 6 months | Paid tools, panels, incentives, media spend, agencies |
| Ethics, IRB or clinical governance | 2 weeks to 3 months | Anything touching patients or generalisable knowledge |
| Legal, privacy and data protection | 2 to 8 weeks | Recording, PII handling, cross-border transfer, deceptive tests |
| Certification and licensing | 3 to 18 months | Shipping at all. Often the dominant risk, and usually discovered late |
| Tooling, BOM or design freeze | fixed date | Every change to the frozen part, permanently |
| Component lead time and sourcing | weeks to a year | Any design depending on a long-lead or sole-source part. On a long cycle this is routinely the schedule-dominant risk and it is the one teams discover last |

**Write the gates down before selecting methods.** For each: lead time, who grants it, and
which methods it makes unavailable inside your window. In S-tier failure cases, a team plans
a study that requires a tool they cannot buy for four months.

### Sort assumptions by when the decision freezes, not only by cost

The default rule is "cheapest method that settles it". That is right when decisions stay
reversible. Where they do not, reversibility outranks cost.

| Decision type | Discovery timing |
|---|---|
| Irreversible after a freeze (tooling, moulds, BOM, chip selection, licence scope, public commitment, data model at scale) | Front-load. Spend disproportionately here, before the freeze, even on expensive methods |
| Expensive to reverse (pricing tiers, brand, API contracts, integrations shipped to customers) | Test before commitment, accept a slower method |
| Cheap to reverse (copy, layout, flows, most software features) | Ship and learn. A test here often costs more than the mistake |

**In long-cycle products the manufacturing loop is not the learning loop.** An 18-month
hardware cycle does not mean 18-month feedback. Decouple them: keep the irreversible physical
decisions on the slow loop with heavy up-front discovery, and run continuous discovery on the
firmware, calibration, software and service layers that stay changeable for years.

---

## Step 3c: apply the evidence overrides

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
