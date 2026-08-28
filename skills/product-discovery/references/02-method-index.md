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
**Source:** Moesta and Spiek, *Demand-Side Sales*; Christensen, *Competing Against Luck*.

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
**Source:** Ulwick, *Outcome-Driven Innovation*.

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
**How:** automated scan catches roughly a third of issues. Manual keyboard and screen
reader testing catches the rest. At least two sessions with actual assistive-technology
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

### E3 Conjoint / MaxDiff `[L2-L3] [n>=200]`
**Answers:** relative value of attributes including price, via forced trade-offs. Much
better than direct rating because respondents must give something up.
**Fails when:** attribute list is written from internal language, or has more than about
six attributes for MaxDiff comfort.

### E4 Price A/B test `[L7] [needs volume + willingness]`
**Answers:** actual demand curve behaviour.
**Fails when:** existing customers see different prices, which is a fairness and legal
problem in several jurisdictions. Test on new customers only, and check local law.

### E5 Unit economics model `[L1-L6, inherits from inputs]`
**Answers:** whether the business case can hold at all.
**How:** acquisition cost, conversion, price, cost to serve, retention, payback. Tag each
input with its evidence level; the model's confidence equals its weakest load-bearing input.
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
**How:** a persistent randomly-withheld slice, typically 1-10%.
**Note:** promotion and CRM programmes without a holdout cannot report incrementality.
Redemption is not incrementality; many redeemers would have converted anyway.

### G7 Interleaving `[L7] [ranking systems]`
**Answers:** which ranking is better, with far higher sensitivity than an A/B test.

### G8 Staged rollout with guardrails `[L6]`
**Answers:** whether anything breaks, with limited blast radius. Not a substitute for an
experiment; it has no control group unless you build one.

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
`product_state = concept`. Every one of these is L1-L2. Say so.

1. Desk research with sources and dates, gaps named explicitly
2. Expert interviews, labelled as orientation
3. Public review and forum mining
4. Search volume and query analysis
5. Competitor teardown against jobs, not features
6. A demand landing page with paid traffic, which is the fastest route from L1 to L5
7. A recruiting plan, because access is the actual blocker and everything else is a
   workaround for not having fixed it

Present these as a bridge to real evidence, with a date by which access must exist. A
project that stays in this set for a quarter is not doing discovery.
