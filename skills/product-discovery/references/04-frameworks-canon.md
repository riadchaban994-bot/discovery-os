# Framework canon

Frameworks are argument structures. They organise thinking and make reasoning auditable.
They do not produce evidence, and applying one to weak inputs produces a well-organised
wrong answer.

Where a framework is commonly misapplied, the entry states **what it is not for**. That
line matters more than the description, because most framework misuse is a good tool
pointed at the wrong question. Entries with no such line are ones this skill has no
recorded misuse pattern for, not ones that cannot be misused.

**Rule for using any framework in an output:** apply it with the user's real context and
real evidence, or do not name it. Name-dropping a framework and then writing generic
content underneath it is the most visible form of fluff in product work.

---

## 1. Discovery structure

**Opportunity Solution Tree.** Teresa Torres, *Continuous Discovery Habits* (2021).
One outcome at the root, opportunities (customer needs, pains, desires) beneath it,
solutions beneath those, assumption tests beneath the solutions.
*For:* keeping a team's work visibly connected to one outcome; making trade-offs between
opportunities explicit; showing why a solution exists.
*Not for:* a place to park feature ideas. If the opportunity layer contains product nouns,
the tree is a roadmap wearing a costume.

**Continuous Discovery Habits.** Torres. The practice around the tree: a product trio
(product, design, engineering) interviewing weekly, story-based interviewing, interview
snapshots, experience maps, compare-and-contrast solution testing, assumption mapping
across desirability, viability, feasibility, usability and ethical risk.
*For:* turning discovery from a project into a habit.
*Not for:* teams with no customer access. Fix access first; the habits assume it.

**The four big risks.** Marty Cagan, *Inspired* 2nd edition (2017) and the SVPG writing
around it. Value, usability, feasibility, business viability. Not in the 2008 first
edition. Discovery's job is to address all four before delivery.
*For:* diagnosing which risk is actually open, which determines the method.
*Not for:* a checklist to tick after the decision is made. Torres's addition of ethical
risk is worth carrying.

**Discovery and delivery as parallel tracks.** Desirée Sy (2007) originally, popularised
by Cagan and Jeff Patton as dual-track.
*For:* explaining that discovery is continuous and not a phase.
*Not for:* two separate teams. The point is the same team doing both.

**Product Kata.** Melissa Perri, *Escaping the Build Trap* (2018), adapted from Mike
Rother's *Toyota Kata*. Understand the direction, grasp the current condition, set a
target condition, experiment toward it.
*For:* teams that keep skipping from problem to solution.
*Not for:* situations where the direction itself is the question.

**GIST.** Itamar Gilad. Goals, Ideas, Step-projects, Tasks, with the Confidence Meter
grading evidence behind ideas.
*For:* replacing a feature roadmap with something evidence-weighted.

**Double Diamond.** UK Design Council (2005). Discover, define, develop, deliver, with
divergence and convergence in each half.
*For:* explaining to non-product audiences why you are not narrowing yet.
*Not for:* a project plan. Real discovery loops rather than proceeding.

**Shape Up.** Ryan Singer, Basecamp (2019). Fixed time, variable scope; appetite instead
of estimate; betting table; shaping before committing.
*For:* protecting a team from unbounded work, and forcing a decision about appetite.
*Not for:* a substitute for discovery. Shaping does include problem framing, so this is a
reading rather than a property of the method: in practice teams reach for Shape Up once the
problem is settled, and use it to bound the solution.

**Working Backwards / PR-FAQ.** Amazon; documented in Bryar and Carr, *Working Backwards*
(2021). Write the press release and FAQ before building.
*For:* forcing clarity about the customer benefit and surfacing hard questions early.
*Not for:* evidence. A beautifully written PR-FAQ is still L0 until someone checks it.

**Design Sprint.** Jake Knapp, *Sprint* (2016). Five days from problem to tested prototype.
*For:* breaking a deadlock, or starting fast on a well-bounded question.
*Not for:* the whole of discovery. It is one loop, and the Friday test is five users.

**Discovery Discipline.** Rémi Guyot and Tristan Charvillat (2023). A recent European
method with a strong emphasis on rigour and sequencing. Worth reading in the original; do
not summarise its steps from memory.

---

## 2. Customer and problem understanding

**Jobs to be Done:** two distinct schools. Do not blend them without saying so.

- *Outcome-Driven Innovation*: Tony Ulwick, *What Customers Want* (2005), *Jobs to be
  Done: Theory to Practice* (2016). Jobs decompose into desired outcome statements
  (direction + metric + object + context), rated on importance and satisfaction.
  Opportunity score = importance + max(importance - satisfaction, 0).
  **The inputs are top-two-box percentages** of respondents rating the outcome important
  and rating themselves satisfied, not raw means. Applied to mean scores the formula
  produces nonsense.
  *For:* quantifying unmet need at scale. Strategyn's own practice suggests roughly 180
  responses per segment for a stable read `[practitioner guidance, not a statistical rule]`.
  *Not for:* small qualitative samples. The algorithm needs survey data.
- *Switch / Forces*: the switch interview was developed by Bob Moesta and Chris Spiek at
  Re-Wired. Moesta sets it out in *Demand-Side Sales 101* (2020, with Greg Engle); the
  broader theory is in Christensen, Hall, Dillon and Duncan, *Competing Against Luck*
  (2016). Reconstruct the timeline of a real switch and map the four forces: push of the
  situation, pull of the new, habit of the present, anxiety about the new.
  *For:* understanding why change happened, and what blocks it.
  *Not for:* prevalence or sizing.

**The Mom Test.** Rob Fitzpatrick (2013). Talk about their life, not your idea. Ask about
specifics in the past. Listen more than you talk. Compliments, generic claims and future
promises are bad data.
*For:* the single most useful thing to hand someone before their first interview.

**Just Enough Research.** Erika Hall (2013, 2nd ed. 2019). Research as a decision-support
activity with a defined question and a defined stopping point.
*For:* the discipline of naming the decision before designing the study.

**Interviewing Users.** Steve Portigal (2013, 2nd ed. 2023). Interviewing craft: rapport,
silence, the follow-up question, managing your own assumptions.

**Mental Models.** Indi Young (2008). Diagram the customer's reasoning and task structure
independent of any product, then align capabilities to it.
*For:* problem-space work in complex domains.
*Not for:* fast projects. It is heavy and it earns its cost only at real complexity.

**Empathy map.** Dave Gray, XPLANE. Says, thinks, does, feels.
*For:* organising observations for a team.
*Not for:* evidence, when filled from imagination. Every quadrant needs a source.

**Service blueprint.** G. Lynn Shostack (HBR, 1984) introduced the blueprint, the line of
visibility and fail points. The five-lane, three-line version in common use today, adding
physical evidence and the line of internal interaction, is Bitner, Ostrom and Morgan
(2008), developed from Shostack. Cite whichever you are actually using.
*For:* service and operational products where the failure is behind the counter. Full
anatomy in `../discovery-synthesis/references/experience-mapping.md`; use one version
consistently rather than mixing the 1984 and 2008 layouts.

**Personas:** only legitimate when built from real research and carrying their evidence.
A persona with a stock photo, a name, and invented hobbies is a liability. Prefer
behavioural segments: what they do, in what situation, with what constraint. If demographic
attributes do not change the design, leave them out.

---

## 3. Opportunity and prioritisation

**Kano model.** Noriaki Kano et al. (1984). Must-be, one-dimensional, attractive,
indifferent, reverse. Functional and dysfunctional question pairs.
*For:* understanding that satisfaction is not linear, and that expected attributes buy
nothing when present and cost everything when absent.
*Not for:* small samples, and not a permanent classification. Attractive attributes decay
into must-be over time.

**RICE.** Intercom. Reach, Impact, Confidence, Effort.
*For:* structuring an argument between comparable items and exposing where people disagree.
*Not for:* a measurement. The score inherits every input's weakness. Publish the inputs.

**ICE.** Sean Ellis. Impact, Confidence, Ease. Faster and cruder than RICE.

**WSJF / Cost of Delay.** Don Reinertsen, *The Principles of Product Development Flow*
(2009), operationalised in SAFe. Cost of delay divided by duration. Delay has a cost, not
a value, and the wording matters because it is what makes the number computable.
*For:* sequencing when delay genuinely costs money, which is more often than teams think.

**Now / Next / Later.** Janna Bastow, ProdPad.
*For:* a roadmap that communicates intent without promising dates it cannot keep.

**Impact Mapping.** Gojko Adzic (2012). Goal, actors, impacts, deliverables.
*For:* connecting a deliverable to a behaviour change in a named actor.

**Opportunity Canvas.** Jeff Patton. One page: problem, users, solutions, adoption
strategy, measures.
*For:* a lightweight structure before committing to a solution.

**Story Mapping.** Jeff Patton, *User Story Mapping* (2014). The narrative backbone of a
journey, with slices for releases.
*For:* scoping a release around a complete journey rather than a list of features.

**Wardley Mapping.** Simon Wardley. Value chain against evolution (genesis, custom,
product, commodity), anchored on user need.
*For:* strategic positioning and build-versus-buy. Answers "where should we play", not
"what should we build next sprint".

**Diffusion of Innovations / Crossing the Chasm.** Everett Rogers (1962); Geoffrey Moore
(1991).
*For:* remembering that early adopters and the mainstream want different things, and that
evidence from one does not transfer to the other.

---

## 4. Experimentation and testing

**Testing Business Ideas.** David Bland and Alex Osterwalder (2019). A library of
experiments organised by desirability, feasibility and viability, with an explicit
evidence-strength scale, plus test cards and learning cards. (Adaptability appears in later
Strategyzer work, *The Invincible Company*, 2020, not as a fourth axis here.)
*For:* the single best reference for choosing an experiment.

**Assumption mapping.** Bland. Importance against evidence, 2x2. Top-right (important,
unevidenced) is what you test first.
*For:* deciding what to test. Do this before designing any test.

**Pretotyping.** Alberto Savoia, *The Right It* (2019). Test "the right it" before
building "it right". XYZ hypothesis ("at least X% of Y will do Z"). Named patterns
including fake door, mechanical turk, pinocchio, provincial and one-night stand. His
central principle is skin in the game: measure what people give up, not what they say.
*For:* the fastest, cheapest demand evidence available.

**Riskiest Assumption Test:** popularised by Rik Higham as a corrective to MVP misuse.
Build the smallest thing that tests the riskiest assumption, which is usually not a
product at all.
*For:* stopping "MVP" being used to mean "version one, but rushed".

**Lean Startup.** Eric Ries (2011). Build-measure-learn, minimum viable product,
validated learning, innovation accounting, pivot or persevere.
*For:* the loop, and for innovation accounting in genuinely new ventures.
*Not for:* an excuse to ship an incomplete product. Ries's MVP is an experiment, not a
release.
*A note on his vocabulary:* "validated learning" is Ries's term and it is used here to name
his concept. It is not a licence to write "validated" in your own outputs. Evidence
accumulates or fails to; use the four confidence levels instead.

**Lean UX.** Jeff Gothelf and Josh Seiden (2013). Hypothesis format: We believe [outcome]
will be achieved if [user] attains [benefit] with [feature]. We will know we are right when
we see [signal].
*For:* forcing a testable statement out of a feature request.

**Trustworthy Online Controlled Experiments.** Ron Kohavi, Diane Tang, Ya Xu (2020). The
reference for online experimentation: the overall evaluation criterion, guardrail metrics,
sample ratio mismatch, A/A tests, Twyman's law (any figure that looks interesting is
usually wrong), interference, and the many ways experiments lie.
*For:* everything about running experiments properly.

**Value Proposition Canvas / Business Model Canvas.** Alex Osterwalder et al.
*For:* structuring the fit between customer jobs, pains and gains and what you offer, and
for exposing which parts of a business model are assumptions.

**Lean Canvas.** Ash Maurya, *Running Lean*. The Business Model Canvas adapted for
startups, with problem, solution and unfair advantage.

---

## 5. Metrics and measurement

**North Star Framework.** Amplitude, largely authored by John Cutler. One leading metric
that represents delivered customer value, decomposed into three to five inputs a team can
move.
*For:* aligning a team on an outcome rather than a feature list.
*Not for:* a metric that is really a revenue proxy in disguise. If the north star can be
moved without a customer being better off, it is the wrong metric.

**HEART + Goals-Signals-Metrics.** Kerry Rodden, Hilary Hutchinson, Xin Fu (Google, CHI
2010). Happiness, Engagement, Adoption, Retention, Task success; and the discipline of
going goal, then signal, then metric.
*For:* designing a measurement set for a feature without defaulting to page views.

**AARRR.** Dave McClure. Acquisition, Activation, Retention, Revenue, Referral.
*For:* a shared vocabulary for a funnel.
*Not for:* a strategy. It is a checklist, and it says nothing about loops.

**Growth loops.** Brian Balfour, Casey Winters (Reforge). Output of one cycle becomes
input to the next.
*For:* seeing why funnel thinking undercounts compounding channels.

**Product-market fit signals:** retention curve flattening is the primary signal. Sean
Ellis's 40% "very disappointed" survey is a secondary heuristic, valid only among users who
have experienced core value. Rahul Vohra's Superhuman method (First Round Review, 2018)
segments the "very disappointed" group and builds for them specifically.
*For:* an honest read on fit.
*Not for:* a single number to report upward. Fit is per segment.

**PMF Pyramid.** Dan Olsen, *The Lean Product Playbook* (2015). Target customer,
underserved needs, value proposition, feature set, UX, layered.
*For:* diagnosing which layer is broken when a product is not landing.

**OKRs.** Andy Grove at Intel, popularised by John Doerr, *Measure What Matters* (2018);
practical guidance in Christina Wodtke's *Radical Focus* (2016).
*For:* committing to outcomes.
*Not for:* discovery planning. Key results are targets, not hypotheses.

---

## 6. Behaviour and psychology

**Fogg Behaviour Model.** B.J. Fogg. Behaviour = Motivation × Ability × Prompt, all three
required at the same moment.
*For:* diagnosing why an intended behaviour is not happening. Usually the answer is ability
or prompt, and teams reach for motivation.

**COM-B.** Michie, van Stralen and West (2011). Capability, Opportunity, Motivation
produce Behaviour.
*For:* behaviour-change products, health, public sector, compliance.

**Hooked.** Nir Eyal (2014). Trigger, action, variable reward, investment.
*For:* understanding habit formation.
*Ethics:* the same model describes compulsion. Run a harms assessment before applying it
to anything with a vulnerable audience.

**Loss aversion, status quo bias, present bias.** Switching costs are usually
psychological before they are technical. A new product must be substantially better than
the incumbent to overcome the pull of the present, and "substantially" is larger than
teams assume.

---

## 7. Analysis and reasoning

**Thematic analysis.** Virginia Braun and Victoria Clarke (2006). Six phases:
familiarisation, initial codes, searching for themes, reviewing themes, defining and
naming, reporting.
*For:* the defensible way to get from transcripts to themes.

**Five Whys.** Originated by Sakichi Toyoda; embedded in the Toyota Production System by
Taiichi Ohno. Iteratively ask why to reach a cause.
*For:* a fast root-cause probe.
*Not for:* a single causal chain in a complex system. Real causes branch. Use a fishbone
diagram or a fault tree when the system is not linear.

**Premortem.** Gary Klein (HBR, 2007). Imagine the failure has happened, then write down
why, individually and silently before sharing.
*For:* surfacing risks that hierarchy suppresses.

**Cynefin.** Dave Snowden. Clear, complicated, complex, chaotic, confused.
*For:* choosing an approach. In complex contexts, probe first: experiments beat analysis.
In complicated ones, analysis and expertise work.

**Pyramid Principle.** Barbara Minto. Answer first, then grouped supporting arguments,
MECE.
*For:* structuring the readout so a busy reader gets the answer in the first line.

---

## 8. Choosing between frameworks

| Situation | Reach for |
|---|---|
| Team busy, unclear why | Opportunity solution tree, plus one outcome |
| Cannot decide what to test | Assumption mapping |
| Idea keeps mutating | Lean UX hypothesis format, written down |
| Everyone has an opinion, no evidence | Evidence ledger and the confidence meter |
| Feature list masquerading as strategy | Impact mapping or Wardley mapping |
| Need to understand why people switched | JTBD switch interview and forces |
| Need to size unmet need | ODI outcome statements and opportunity scoring |
| Metric chosen badly | HEART with goals-signals-metrics |
| Growth flat, funnel already optimised | Growth loops |
| Feature shipped, nobody uses it | Fogg model diagnosis, then usability, then value |
| Stakeholder certainty versus evidence | AUDIT mode, claim by claim |
| New market, unfamiliar dynamics | Wardley map, expert interviews, then primary research |
| Complex regulated domain | Mental models, service blueprint, ethical assessment |

**Cap: two frameworks per output.** More than two and the reader is reading structure
instead of findings. A framework earns its place by changing the recommendation; if the
recommendation would be identical without it, drop it.
