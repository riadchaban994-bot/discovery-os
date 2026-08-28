# Method index

Every card: what it answers, what it needs, how it runs, and the failure mode that makes
it lie to you. `[L0-L7]` is the evidence level from `references/03-evidence-ledger.md`. Cost is for a
single competent operator, excluding recruitment lead time.

Pick the cheapest card that clears the decision. Read the "Fails when" line before
committing; that line is why most studies produce confident nonsense.

---

## A. Learning what exists (problem and opportunity discovery)

### A1 Story-based customer interview `[L3] [45 min each + 30 min synthesis]`
**Answers:** what people actually do, what it costs them, what they tried instead.
**Needs:** access to people in the situation. Not "users of our product" unless the
question is about using the product.
**How:** open with a specific past episode ("tell me about the last time..."), follow the
timeline, probe for detail, never pitch. Collect one story per session minimum.
**Fails when:** you ask about the future, or about your idea. Both convert it to L2.
**Source:** Torres, *Continuous Discovery Habits*; Fitzpatrick, *The Mom Test*;
Portigal, *Interviewing Users*.

### A2 Jobs-to-be-Done switch interview `[L3] [60-75 min each]`
**Answers:** why someone changed from one solution to another, and what forces moved them.
**Needs:** people who switched recently, ideally within 90 days, memory decays fast.
**How:** reconstruct the timeline backwards from purchase to first thought. Map the four
forces: push of the situation, pull of the new solution, habit of the present, anxiety
about the new.
**Fails when:** run on people who did not actually switch, or too long after the event.
**Source:** the switch interview is Moesta and Spiek's method; Moesta, *Demand-Side Sales
101* (2020, with Greg Engle). Broader theory: Christensen, Hall, Dillon and Duncan,
*Competing Against Luck* (2016).

### A3 Contextual inquiry / field study `[L4] [half day per site]`
**Answers:** what people do rather than what they report doing. Catches workarounds,
environment, interruptions, and the parts of the job nobody thinks to mention.
**Needs:** permission to observe in the real setting.
**How:** watch the work, ask about what you see as it happens, master-apprentice stance.
**Fails when:** you observe a demo instead of the work, or your presence changes it.
**Source:** Beyer and Holtzblatt, *Contextual Design*.

### A4 Diary study `[L3-L4] [2-4 weeks elapsed]`
**Answers:** behaviour over time, infrequent events, emotional arc, context you cannot be
present for.
**Needs:** 8-15 committed participants and a light capture method. Compliance is the
constraint; design for two minutes per entry.
**How:** prompted entries at the moment of the event, plus a closing interview.
**Fails when:** the prompt burden is high, so entries become retrospective summaries.

### A5 Support ticket mining `[L3] [1-2 days] [free]`
**Answers:** what breaks, for whom, how often, in the customer's own words.
**Needs:** a ticket corpus with any tagging at all.
**How:** sample rather than read everything, code inductively, then count by code.
Volume by code is a prevalence signal within the population that contacts support.
**Fails when:** treated as representative of all users. Ticket-raisers are a biased
sample: engaged enough to complain, not so unhappy they left silently.

### A6 Sales call and win-loss mining `[L3] [2-3 days]`
**Answers:** what buyers ask, object to, and compare you against. Why deals died.
**Needs:** recordings or notes. In B2B this is usually the richest untapped corpus.
**How:** code objections, requested capabilities, competitor mentions, loss reasons.
Interview lost buyers where possible; CRM loss codes are usually salesperson-authored
fiction.
**Fails when:** you use the CRM loss reason field as data. It is an internal opinion.

### A7 Review and community mining `[L2-L3] [1 day] [free]`
**Answers:** unprompted language, competitor weaknesses, category expectations.
**Needs:** a public corpus: app stores, G2, Reddit, sector forums, local social groups.
**How:** code for jobs and pains rather than for feature requests. Note the date; reviews
age badly.
**Fails when:** treated as prevalence. Reviewers are extremes.

### A8 Search and query-log mining `[L4] [1 day]`
**Answers:** what people are trying to find, in their words, at scale. In-product search
queries with zero results are the single highest-yield free discovery source most teams
never look at.
**Needs:** search logs, internal or external keyword tools.
**How:** cluster queries by intent, weight by volume, isolate zero-result and refined
queries.
**Fails when:** you read demand into queries that are navigational.

### A9 Session replay review `[L4] [half day]`
**Answers:** where people hesitate, loop, rage-click, or abandon.
**Needs:** replay tooling and consent-compliant capture.
**How:** sample from a specific failure event rather than browsing randomly. Watch 15-20
sessions of the same failed transition.
**Fails when:** used as a browsing activity. Always start from a defined event.

### A10 Expert interview `[L1-L2] [45 min]`
**Answers:** domain shape, regulation, vocabulary, who the real actors are.
**Needs:** access to practitioners, not consultants selling into the space.
**How:** treat as orientation. Experts describe the category, not your customers.
**Fails when:** substituted for customer contact. An expert's model of the customer is
still a model.

### A11 Service safari / mystery shopping `[L4] [half day]`
**Answers:** what the end-to-end experience is actually like, including yours.
**How:** go through the real journey as a customer, unassisted, and record every friction
with a timestamp.
**Fails when:** done by someone who knows the shortcuts.

### A12 Competitor teardown `[L1] [1 day]`
**Answers:** what the category has trained customers to expect, and where the gaps are.
**How:** map their flows against the jobs your evidence has surfaced, not against a
feature checklist.
**Fails when:** it becomes a feature-parity list. Copying a competitor's feature copies
their unvalidated bet.
### A13 Operational and regulatory records you already hold `[L4] [1-3 days] [free]`
**Answers:** what is actually happening, at full population, from data the organisation
already has under existing operational authority. No recruiting, no consent process, no
procurement, usually no permission beyond a query.

**This is the first corpus in every non-consumer market, and it is the one teams miss**,
because the standard discovery reading list is written for consumer software and lists
support tickets, app reviews and session replay. Those may not exist for you. These will.

| Context | The dataset sitting there already |
|---|---|
| Clinical and healthcare | The EHR audit log. Alert firing counts, override rates, timestamps, clinician ids, order sets. Answers "how bad is this and for whom" this afternoon |
| Channel-sold and hardware | Distributor sell-through against sell-in, stocking depth, RMA and warranty claims, field service reports, returns reason codes |
| Government and public service | Case management records, inspection and works-order data, contact-centre logs, statutory reporting returns, complaints registers |
| Internal and captive | Workflow audit trails, approval and rejection logs, help-desk tickets by category, the exports people take, the spreadsheets on the shared drive |
| Financial services | Transaction and exception logs, dispute and chargeback records, manual-review queues, regulatory reporting |
| Marketplace | Match and fill logs, cancellation reasons, dispute records, supplier earnings distribution |

**How:** name the dataset, name who owns it, confirm the existing authority to query it, then
sample rather than reading everything. Code inductively. Volume by code is a prevalence
signal within the population the system observes.

**Fails when:** treated as complete. It records what the system saw, not what happened. An
alert nobody logged, a fault nobody reported and a workaround done on paper are all invisible
here, and the gap between the record and reality is itself a finding worth chasing.

**Run this before designing any new collection.** Planning fresh data gathering while the
answer sits in a table you can already query is the most expensive avoidable mistake in
non-consumer discovery.

### A14 Structured literature review `[L1 to L7, graded on the source's own design] [1-3 days]`
**Answers:** what has already been established, by someone with a bigger sample and a better
design than you can afford.
**Needs:** a domain with a real published literature: clinical, pharmaceutical, education,
public health, safety, human factors, economics.
**How:** search the actual databases rather than the open web. Grade each paper on **its own
design**, not on the fact that someone else ran it, then discount for how far its population
and setting sit from yours. State the discount and the reason.
**Fails when:** graded L1 as generic desk research, which is the default error and which
pushes people to spend months generating weaker primary evidence than a morning of reading
would have returned. See `references/03-evidence-ledger.md`.
**In a domain with a literature, this is frequently the cheapest and strongest study
available.**

**A13 or A14 first?** Run them in parallel; they answer different questions and neither
blocks the other. A13 tells you what is happening *here*, at your population, right now.
A14 tells you what is already established *anywhere*, usually at a better sample and design
than you can afford. Clinical, public-health and education work typically has both a rich
operational record and a real literature, and a week spent on one while ignoring the other
is a week wasted either way.

### A15 Field trial / alpha programme `[L4-L6] [4-12 weeks]`
**Answers:** how the thing behaves in the real environment, on real sites, over enough time
for the failure modes to appear. For a physical product this is the closest you get to a
controlled experiment, because randomisation across 200 factories is not available.
**Needs:** three to ten named sites that agree to run it and report back, a contact at each,
and a defined reporting cadence. In a channel-sold product the distributor usually has to be
brought in as a partner rather than routed around.
**How:** instrument the units if you can. Fixed check-in schedule. Log every failure,
workaround and support call with its site and date. Ask what they stopped doing, and what
they went back to.
**Proves:** durability, environment tolerance, installation reality, the support burden per
unit, and whether anyone uses the feature you built it for.
**Cannot prove:** demand at scale, or anything about sites unlike the ones who volunteered,
and volunteers are systematically your most engaged customers.
**Fails when:** run for less time than the failure mode takes to appear, or when the sites
are chosen for being easy. Include one hostile environment on purpose.


---

## B. Structuring what you learned

### B1 Opportunity solution tree `[structuring device]`
**Answers:** how a set of opportunities and solutions ladder up to one outcome.
**How:** outcome at the root, opportunities (needs, pains, desires from customers)
beneath, solutions beneath those, assumption tests beneath the solutions.
**Fails when:** opportunities are solutions in disguise, or when it is built once and
never updated. It is a living map, not a deliverable.
**Source:** Torres, *Continuous Discovery Habits*.

### B2 Experience map `[structuring device]`
**Answers:** the current end-to-end experience from the customer's point of view, before
you narrow to opportunities.
**How:** build from interview stories, not from your funnel. Draw it before the first
interview from assumptions, then correct it with each session.
**Fails when:** it maps your process rather than their experience.

### B3 Thematic analysis / coding `[method]`
**Answers:** what patterns exist across a qualitative corpus, defensibly.
**How:** familiarise, generate initial codes, search for themes, review, define, report.
Track new codes per interview to detect saturation.
**Source:** Braun and Clarke (2006). Full protocol in `discovery-synthesis`.

### B4 Affinity mapping `[method] [2-4 hours, whole team]`
**Answers:** shared understanding, fast, and a first cut at themes.
**How:** one observation per note with its source code attached, cluster silently first,
name clusters last.
**Fails when:** notes lose their provenance, which makes every later claim unauditable.

### B5 Mental model diagram `[structuring device]`
**Answers:** the customer's own reasoning and task structure, independent of your product.
**Source:** Indi Young, *Mental Models*.

### B6 Opportunity sizing `[method]`
**Answers:** which opportunity is worth more.
**How:** Torres's four criteria (opportunity size, market factors, company factors,
customer factors) for a comparative judgement, or ODI opportunity scoring
(`importance + max(importance - satisfaction, 0)`) where a survey of n>=180 exists.
**Fails when:** applied to opportunities that came from a brainstorm.

### B7 Jobs-to-be-Done outcome statements `[method]`
**Answers:** the measurable outcomes customers are trying to achieve, framed so they can
be rated.
**How:** direction + metric + object + context. "Minimise the time it takes to reconcile
cash against orders at end of day."
**Source:** Ulwick's Outcome-Driven Innovation. Books: *What Customers Want* (2005),
*Jobs to be Done: Theory to Practice* (2016).

---

## C. Testing value and desirability

### C1 Comparison prototype test `[L2-L4] [1 week]`
**Answers:** which of several approaches speaks to a real need, and why.
**Needs:** two or three prototypes at equal fidelity, and participants who have the need.
**How:** same session, counterbalanced order, ask which and why, probe to the need.
**Fails when:** fidelity differs between options, or only one option is shown.

### C2 Painted door / fake door `[L5] [2-4 days build]`
**Answers:** whether people will take a real step toward a thing that does not exist yet.
**Needs:** live traffic on a relevant surface, roughly 1k+ weekly visits to get a usable
read in a week.
**How:** real-looking entry point, click captured, honest message on the other side
("we are building this, want to be first?"), email capture as the intent signal.
**Fails when:** the entry point is placed where nobody looks, so a null result measures
placement rather than demand; or when the honest message is missing, which is a trust
cost you cannot repay.
**Ethics:** never take money. Always disclose immediately after the click.
**Do not run** in clinical, financial-advice, legal, safety-critical or statutory-service
contexts, or on vulnerable populations, without a named approval from whoever owns that
risk. A fake door implies a capability, and in those settings implying a capability you do
not have is a regulatory matter, not a research one.

### C3 Demand landing page + paid traffic `[L5] [3-5 days]`
**Answers:** whether a proposition attracts a defined audience, and at what cost.
**Needs:** a budget (small: enough for ~300-500 clicks), and a clear audience definition.
**How:** page describing the value proposition, single call to action, traffic from paid
search or social, measure click-to-signup. Run at least two value propositions against
each other; an absolute conversion rate with nothing to compare it to is uninterpretable.
**Fails when:** read as an absolute. A 4% signup rate means nothing alone.
**Source:** Savoia, *The Right It*.

### C4 Concierge test `[L6] [1-3 weeks]`
**Answers:** whether the outcome is valuable when delivered manually, and what the real
workflow is.
**Needs:** a handful of real customers who know it is manual.
**How:** deliver the outcome by hand, repeatedly, for real customers. Learn the process
before automating it.
**Fails when:** it becomes a service business nobody is willing to stop.
**Source:** Cagan, *Inspired*; Ries, *The Lean Startup*.

### C5 Wizard of Oz `[L5-L6] [1-2 weeks]`
**Answers:** how people behave with a working product, before the product works.
**Needs:** a front end that looks real and a human behind it. Users do not know.
**How:** real interface, manual fulfilment. Especially strong for AI features: test the
experience before the model exists.
**Fails when:** manual latency differs so much from the real system that behaviour is not
transferable. Match the timing.
**Ethics:** acceptable where output quality matches what is promised and no sensitive data
is exposed to the operator without disclosure.
**Do not run** where the concealed output is a clinical, diagnostic, financial, legal or
safety judgement. A human silently generating recommendations that a professional believes
came from a checked system is a safety hazard, is very likely a regulated-device or
professional-practice violation, and is not fixed by a debrief afterwards. In those
settings use shadow mode instead: the new logic runs and is logged but is never shown, and
you compare what it would have done against what happened.

### C6 Single-feature MVP `[L6] [2-6 weeks]`
**Answers:** whether the core value holds when everything else is stripped away.
**Fails when:** "minimum" is used to justify shipping something that cannot deliver the
value at all, so the negative result is uninformative.

### C7 Pre-sale or deposit `[L6] [days to weeks]`
**Answers:** willingness to pay, with money.
**How:** take a refundable deposit or a discounted prepay for a dated delivery.
**Fails when:** the price tested is not the price you will charge.
**Ethics:** refund policy stated up front and honoured.

### C8 Letter of intent `[L6] [B2B, 1-3 weeks]`
**Answers:** whether an enterprise buyer will commit their name to wanting this.
**How:** non-binding but signed, naming the problem, the intended scope, and an indicative
budget band.
**Fails when:** signed by a champion with no budget authority. Get the economic buyer.

### C9 Crowdfunding or waiting list `[L5]`
**Answers:** demand at scale from a self-selected audience.
**Fails when:** read as market demand. The audience is people who found your campaign.

### C10 Email or in-product campaign test `[L5] [days]`
**Answers:** interest among existing users, cheaply.
**How:** describe the capability to a random subset, measure click-through to a signup or
waitlist, hold out a control.
**Fails when:** sent to your most engaged segment only.

### C11 404 / button-to-nowhere test `[L5] [hours]`
**Answers:** whether an entry point gets used at all.
**How:** ship the control, log the click, show an honest "coming soon".
**Fails when:** left running for weeks. It is a two-week instrument at most.
**Do not run** on a statutory service, a safety path, or anywhere a user could reasonably
believe the control performs a duty someone owes them.

### C12 High-fidelity value test in interview `[L2-L4] [per session]`
**Answers:** whether people understand the value, and whether it connects to a need they
already described.
**How:** show after they have told their story, never before. Ask them to react, not to
approve. Watch for the difference between "that's nice" and "when can I have it".
**Fails when:** run before the story, which contaminates everything they say afterwards.

---

## D. Testing usability

### D1 Moderated usability test `[L4] [5 per round]`
**Answers:** where the interface defeats people.
**How:** realistic tasks, think-aloud, no leading, no rescuing until the task is
genuinely dead. Severity-rate findings. Three rounds of five, fixing between rounds.
**Fails when:** tasks are phrased using the interface's own labels, which gives the answer
away.
**Source:** Nielsen; Krug, *Rocket Surgery Made Easy*.

### D2 Unmoderated remote test `[L4] [15-30 participants] [days]`
**Answers:** task success rates and where people fail, at higher n and lower depth.
**Fails when:** you need to ask why. You cannot probe.

### D3 First-click test `[L4] [n>=30]`
**Answers:** whether the first move toward a task is obvious. First-click success
correlates strongly with overall task success.

### D4 Tree test `[L4] [n>=30]`
**Answers:** whether the information structure works, independent of visual design.

### D5 Card sort `[L3] [n=15-30]`
**Answers:** how users group and name concepts. Open for generating structure, closed for
validating one.

### D6 5-second test `[L3] [n>=25]`
**Answers:** what a page communicates at a glance.

### D7 Heuristic evaluation `[L1] [3 evaluators, half day]`
**Answers:** likely usability problems, cheaply, before spending participant time.
**Fails when:** substituted for user testing. It finds expert-visible problems only.

### D8 Cognitive walkthrough `[L1] [2 hours]`
**Answers:** whether a first-time user could reason their way through each step.

### D9 Accessibility audit `[L4] [1-3 days]`
**Answers:** conformance against WCAG, plus real barriers.
**How:** `[HEURISTIC]` an automated scan catches a minority of real accessibility issues,
commonly cited as around a third; treat it as a first pass, not coverage. Manual keyboard
and screen reader testing is where the rest are found. At least two sessions with actual assistive-technology
users.

---

## E. Testing viability and pricing

### E1 Van Westendorp price sensitivity meter `[L2] [n>=100]`
**Answers:** an acceptable price range and the point of marginal cheapness and expensiveness.
**How:** four questions (too cheap, cheap/bargain, expensive, too expensive), plot
cumulative curves, read the intersections.
**Fails when:** used to set a price. It maps perception, not behaviour, and it works only
for products respondents genuinely understand.

### E2 Gabor-Granger `[L2] [n>=100]`
**Answers:** purchase-intent decay across price points, and a revenue-maximising point
under stated intent.
**Fails when:** stated intent is treated as demand. Deflate heavily.

### E3 MaxDiff (best-worst scaling) `[L2-L3] [n>=200]`
**Answers:** the relative importance of a list of items, by forcing a best and a worst
choice from each subset. Much better than rating scales because respondents must give
something up.
**Scales to long lists**, typically 10 to 40 items, showing each respondent subsets of four
or five. With six or fewer items, run a full ranking instead; MaxDiff earns its complexity
on lists too long to rank.
**Cannot price.** It ranks items against each other and produces no willingness-to-pay.
**Fails when:** the item list is written in internal language rather than the customer's.

### E3b Choice-based conjoint `[L2-L3] [n>=250]`
**Answers:** trade-offs across attribute *bundles* including price, and from that a demand
curve and attribute-level utilities.
**Needs:** realistic, mutually exclusive attribute levels. A badly specified attribute list
invalidates the whole study, and this is the usual failure.
**Fails when:** used where MaxDiff would do. Conjoint is the heavier instrument and it is
worth it only when you need the price interaction.

### E4 Price A/B test `[L7] [needs volume + willingness]`
**Answers:** actual demand curve behaviour.
**Fails when:** existing customers see different prices, which is a fairness and legal
problem in several jurisdictions. Test on new customers only, and check local law.

### E4b Market sizing by Fermi decomposition `[L1-L3, inherits from inputs] [hours]`
**Answers:** roughly how many, to an order of magnitude, when no published figure exists or
the published ones are vendor marketing.
**Needs:** one real anchor with a source and a date. A government register, a census, a
regulator's published count, a platform's disclosed totals. Without an anchor this is not an
estimate, it is a sequence of guesses.
**How:** anchor, then multiply down by filters. Each multiplier carries its own tag:
`[src]`, or `[ASSUMPTION]` with a deliberately wide band. Report a range, never a point.
Name the single input that would most narrow it, and what it would cost to get.
**Fails when:** the multipliers are model-generated and the brackets get stripped three
documents later. See the Fermi constraints under rule 3 in `references/00-constitution.md`.
**Use it as the honest substitute** when someone needs a market number today and no
defensible published figure exists. That is rule 17 in practice.

### E5 Unit economics model `[L1-L6, inherits from inputs]`
**Answers:** whether the business case can hold at all.
**How:** acquisition cost, conversion, price, cost to serve, retention, payback. Tag each
input with its evidence level; the model's confidence equals its weakest load-bearing input.
**The default stack above is consumer-shaped.** Channel-sold products need the channel margin
stack or the model shows a viable product that is not. Captive and internal products have no
price and no acquisition cost, and the case is fully-loaded minutes times frequency times
headcount. Marketplaces need both sides. See `references/01-intake-and-routing.md` Step 3a.
**Fails when:** built with placeholder numbers that lose their brackets.

### E6 Channel and CAC test `[L6] [2-4 weeks]`
**Answers:** whether you can reach the segment at a viable cost.
**How:** small budget across two or three channels, measure cost per qualified signup.
**Fails when:** run for less than a full purchase cycle.

### E7 Sales pitch test `[L3-L6] [B2B]`
**Answers:** whether the proposition survives contact with a buyer.
**How:** real pitch to real prospects, track objections and the point where interest
dies. Ends in an ask, so it can produce L6 evidence.

---

## F. Testing feasibility

### F0 Regulatory and approval feasibility `[L4] [days to weeks] [run first]`
**Answers:** what permission, licence, certification or approval this needs in order to
exist at all, who grants it, how long it takes, what it costs, and what a refusal looks
like.
**Needs:** someone who has been through it, or the regulator's own published process. Not a
summary from a model, and not a competitor's marketing.
**How:** name every gate, its lead time and its owner. Then work backwards from the launch
date. If the licence takes twelve months and the plan is nine, that is the finding and
everything else is secondary.
**Fails when:** skipped, or left until after the product works. Licensing, medical-device
classification, financial services authorisation, CE, FCC, ATEX and IP ratings, data
residency and accessibility law all determine whether a product can ship, and all of them
have lead times measured in months.
**Run this before F1 to F5**, on the same logic F3 uses for data availability: there is no
point proving you can build a thing you are not permitted to sell.

### F1 Technical spike `[L4] [timeboxed 1-5 days]`
**Answers:** one named technical unknown.
**How:** written brief with the unknown, the timebox, and what a yes and a no each look
like. Engineer-owned. Output is a written finding, not a conversation.
**Fails when:** the timebox is not enforced, or the question is "is this hard" rather than
a specific unknown.

### F2 Feasibility prototype `[L4] [days]`
**Answers:** can the risky part be built at all, at acceptable performance.
**How:** throwaway code, engineer-written, tests one thing.
**Source:** Cagan, *Inspired*.

### F3 Data availability audit `[L4] [1-3 days]`
**Answers:** does the data this feature needs exist, at the quality and freshness required.
**How:** trace each required field to a real source, check coverage, nulls, latency, and
who owns it. Run this before any AI or analytics feature is scoped, always.
**Fails when:** skipped, which is the most common cause of dead AI features.

### F4 Model feasibility test `[L4] [1-2 weeks]`
**Answers:** can a model hit the accuracy the experience needs.
**How:** label a representative sample by hand, establish the human baseline, build the
simplest possible model, compare. Define the accuracy threshold from the user experience
before you measure, not after.
**Fails when:** the threshold is set after seeing the result.

### F5 Load and latency test `[L4]`
**Answers:** behaviour at the required percentile, not the mean. Design to p95 or p99.

---

## G. Testing at scale (live product)

### G1 Controlled experiment (A/B) `[L7]`
**Answers:** the causal effect of a change on a pre-declared metric.
**Needs:** randomisation, sufficient traffic for power, a working assignment and logging
pipeline.
**How:** pre-register the overall evaluation criterion, guardrail metrics, sample size and
duration. Run an A/A test first if the platform is new. Check sample-ratio mismatch before
reading any result.
**Fails when:** peeking without sequential correction, stopping on a good day, testing
many metrics without correction, or shipping on a result from a broken randomiser.
**Source:** Kohavi, Tang and Xu, *Trustworthy Online Controlled Experiments*.

### G2 Multivariate test `[L7] [high volume only]`
**Answers:** interaction effects between elements. Needs far more traffic than an A/B.

### G3 Multi-armed bandit `[L6]`
**Answers:** which variant to serve while minimising regret. Optimises rather than
measures. Use for short campaigns; use A/B when you need a clean effect size.

### G4 Switchback test `[L7]`
**Answers:** effects where users interfere with each other (marketplaces, dispatch,
pricing). Randomise time blocks in a region rather than users.

### G5 Geo experiment `[L6-L7]`
**Answers:** effects of things you cannot randomise per user, like marketing spend.
**Fails when:** too few geo units. You need enough regions for the variance to behave.

### G6 Holdout group `[L7]`
**Answers:** the cumulative effect of everything a team shipped over a quarter, and the
true incremental value of a programme (CRM, recommendations, promotions).
**How:** a persistent randomly-withheld slice. Size it from the power calculation for the
effect you need to detect, not from a convention. Small enough not to cost real revenue,
large enough to detect the effect: those two constraints usually decide it.
**Note:** promotion and CRM programmes without a holdout cannot report incrementality.
Redemption is not incrementality; many redeemers would have converted anyway.

### G7 Interleaving `[L7] [ranking systems]`
**Answers:** which ranking is better, with far higher sensitivity than an A/B test.

### G8 Staged rollout with guardrails `[L6]`
**Answers:** whether anything breaks, with limited blast radius. Not a substitute for an
experiment; it has no control group unless you build one.

### G8b Stepped-wedge rollout `[L6-L7]`
**Answers:** the causal effect where everyone must eventually receive the intervention.
**How:** units (wards, branches, regions, schools, teams) cross over from control to
treatment in a randomised order, at staggered times. Every unit ends up treated, which is
exactly why ethics committees and unions accept it where a withheld-control design would be
refused.
**Best for:** healthcare, education, public services, and internal rollouts across sites.
The standard design in health services research and almost unknown in product teams.
**Fails when:** there are too few units, or a secular trend is confounded with the rollout
order. Model time explicitly.

### G8c Shadow mode / silent launch `[L4-L6]`
**Answers:** what the new logic would have done, without anyone acting on it.
**How:** run the new model, rule or ranking in production, log its output, show nobody.
Compare against what actually happened and against the incumbent.
**Best for:** any setting where showing an unproven output carries real risk: clinical
decision support, credit decisions, fraud, safety alerting, moderation.
**Fails when:** treated as sufficient on its own. It tells you what the system would output,
not how a human would respond to seeing it. Pair it with a controlled rollout afterwards.

### G9 Quasi-experiments `[L5-L6]`
Difference-in-differences, interrupted time series, regression discontinuity, synthetic
control. For when randomisation was impossible. Each rests on an identifying assumption
that must be stated and checked. Never present the output with the same confidence as G1.

---

## H. Survey instruments

### H1 Prevalence survey `[L2-L3] [n>=200 for a population read]`
**Answers:** how common a behaviour or problem is, among a defined and reachable
population.
**Needs:** qualitative grounding first, a defined sampling frame, and an honest account of
who is missing.
**Fails when:** written before the interviews. The questions then measure the author's
assumptions. Also fails on non-response bias, which is usually larger than the effect
being measured.

### H2 Kano questionnaire `[L2] [n>=100]`
**Answers:** which attributes are expected, which are linear, which delight.
**How:** functional and dysfunctional question pairs per attribute, mapped to the Kano
categories. Cap at about ten attributes; the instrument is tiring.
**Source:** Kano et al. (1984).

### H3 Sean Ellis product-market fit survey `[L2]`
**Answers:** whether a segment would miss the product.
**How:** ask only users who have experienced the core value at least twice. Study the
"very disappointed" segment, not the headline number. The 40% figure is a heuristic.

### H4 In-product intercept `[L2-L3]`
**Answers:** context-specific reactions at the moment of use.
**Fails when:** it interrupts the task being studied.

### H5 NPS verbatim mining `[L2-L3]`
**Answers:** language and themes. The verbatims are useful; the score is a management
metric, not a discovery instrument, and it cannot tell you what to build.

---

## I. Ethical and risk methods

### I1 Structured harms assessment `[required before build for anything consequential]`
Prompts in `references/01-intake-and-routing.md` Q7. Output is a written risk list with owners.

### I2 Premortem `[1 hour, whole team]`
**Answers:** what will have gone wrong, surfaced before commitment.
**How:** "It is a year from now and this failed badly. Write down why." Silent individual
writing first, then share. Silence-first is what makes it work.
**Source:** Klein (2007).

### I3 Privacy and data protection review `[required where personal data is involved]`
What data, what basis, who can access, how long retained, what happens on breach.

### I4 Bias and exclusion audit `[required for any model or automated decision]`
Who is misclassified, who is excluded, what the error costs them, and what recourse
exists.

---

## J. When you have nothing

The honest set for `customer_access = none`, `instrumentation = none`,
`product_state = concept`. Most of these are L1-L2 and you should say so. The exception is
item 1: in a domain with a published literature, a controlled trial is graded on its own
design and can be far stronger than anything else on this list.

1. Desk research with sources and dates, gaps named explicitly. In a domain with a real
   published literature, this is A14 and it is graded on each source's own design, not as
   generic desk research. Do that before anything else on this list
2. Expert interviews, labelled as orientation
3. Public review and forum mining
4. Search volume and query analysis
5. Competitor teardown against jobs, not features
6. A demand landing page with paid traffic, which is the fastest route from L1 to L5
7. **Commission local capacity.** A paid local research partner, an enumerator, a
   university student, a merchant association, an NGO already working with the segment.
   This is the standard move in markets you cannot easily travel to, it converts
   `customer_access = none` into `scheduled` in about three weeks, and it is missing from
   most plans because teams think of research as something they must do personally
8. A recruiting plan, because access is the actual blocker and everything else is a
   workaround for not having fixed it

**Where the audience is not on the open web**, and in most emerging markets they are not,
the instruments above need substituting. Search-volume tools have thin coverage, and a paid
landing page assumes people are reachable on search or social and will convert on a web
form. The real channels are messaging apps, community groups, trade associations and the
physical marketplace. The L5 instrument becomes a messaging-app waitlist, a deposit
collected by an agent, or a pre-order taken in person. Same evidence level, different
plumbing.

Present these as a bridge to real evidence, with a date by which access must exist. A
project that stays in this set for a quarter is not doing discovery.
