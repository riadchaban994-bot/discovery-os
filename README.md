# Discovery OS

**Product discovery for AI agents, done properly.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/riadchaban994-bot/discovery-os?color=blue)](https://github.com/riadchaban994-bot/discovery-os/releases/latest)
[![validate](https://github.com/riadchaban994-bot/discovery-os/actions/workflows/validate.yml/badge.svg)](https://github.com/riadchaban994-bot/discovery-os/actions/workflows/validate.yml)
[![Claude Code](https://img.shields.io/badge/Claude_Code-plugin-8B5CF6)](https://code.claude.com/docs/en/discover-plugins)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-blue)](https://agentskills.io)
[![Python](https://img.shields.io/badge/python-3.8%2B-3776AB)](#requirements)

Seven skills that turn Claude Code, Codex, Copilot CLI or Gemini CLI into a disciplined
discovery partner. It picks the research method your evidence can actually support, and it
will not invent a customer, a number, or a confidence level to fill a gap.

Free, MIT, no accounts, no telemetry. Built as a giveaway for
[ProductTank Syria](https://www.meetup.com/pro/producttank), Damascus, August 2026.

```bash
/plugin marketplace add riadchaban994-bot/discovery-os
/plugin install discovery-os@riadchaban
```

<sub>Not on Claude Code? One line: [`curl -fsSL .../install.sh | bash`](#quick-start)</sub>

---

## Contents

- [The problem it solves](#the-problem-it-solves)
- [Quick start](#quick-start)
- [The seven skills](#the-seven-skills)
- [Commands](#commands)
- [The constitution](#the-constitution)
- [The evidence ladder](#the-evidence-ladder)
- [How the routing works](#how-the-routing-works)
- [The analysis scripts](#the-analysis-scripts)
- [The prototype artifacts](#the-prototype-artifacts)
- [Templates](#templates)
- [What it will not do](#what-it-will-not-do)
- [Grounded in](#grounded-in)
- [File structure](#file-structure)
- [FAQ](#faq)
- [Requirements](#requirements)
- [Uninstall](#uninstall)
- [Contributing](#contributing)
- [Licence](#licence)

---

## The problem it solves

AI has made every part of product discovery faster, including the parts whose value came
from being slow.

Ask a model for user research and you get research-shaped text: fluent personas nobody met,
quotes nobody said, market sizes nobody measured, and a confident recommendation resting on
none of it. It reads exactly like the real thing. Three documents downstream, nobody can
tell the difference, and a quarter gets spent on it.

Discovery OS makes that failure structurally hard. Every claim carries its source. Every gap
is declared rather than filled. Every conclusion carries a confidence level it can defend.
On any question about what customers want, it will not let a model stand in for a person.

It also does the opposite job, which matters just as much. It stops teams running elegant
research that changes no decision. Before any study is designed it makes you finish this
sentence: *if we learn X we will do A, if we learn Y we will do B instead.* If both branches
lead to the same action, it cancels the study and tells you why.

**Two failure modes, one system.** Under-rigour builds the wrong thing. Discovery theatre
builds nothing at all. Both waste the same quarter.

---

## Quick start

### Claude Code

```bash
/plugin marketplace add riadchaban994-bot/discovery-os
```

```bash
/plugin install discovery-os@riadchaban
```

Restart. You have seven skills and seven slash commands.

### Codex, Copilot CLI, Gemini CLI, or anything else

```bash
curl -fsSL https://raw.githubusercontent.com/riadchaban994-bot/discovery-os/main/install.sh | bash
```

Detects every agent on your machine, installs into each, checks your Python, and prints what
it did. Idempotent, so the same line upgrades. `--dry-run` to preview, `--uninstall` to
remove.

### By hand

```bash
git clone https://github.com/riadchaban994-bot/discovery-os.git
cp -R discovery-os/skills/* ~/.claude/skills/     # or ~/.codex/skills/, ~/.agents/skills/
```

Full guide including per-platform paths, project-scoped installs, single-skill zips and
troubleshooting: **[docs/INSTALL.md](docs/INSTALL.md)**.

### Then try it

> We are thinking about adding a bulk upload feature. Should we build it?

You should get a diagnosis before an answer: what decision is at stake, what evidence
exists, and the cheapest method that would settle it. If you get a feature spec instead, the
skill did not load.

---

## The seven skills

| Skill | Owns | Read |
|---|---|---|
| **`product-discovery`** | The commander. Routes any question to the right method for your evidence. Carries the constitution, the evidence ladder, 60+ method cards, the framework canon, the AI boundary, and thirteen templates | [details](docs/SKILLS.md#product-discovery--the-commander) |
| **`discovery-interviewing`** | Guide design, recruiting as a pipeline, moderating, AI-moderated sessions with real participants, rehearsal under a stamp, write-up | [details](docs/SKILLS.md#discovery-interviewing) |
| **`discovery-synthesis`** | Coding and codebooks, saturation measured rather than felt, thematic analysis, opportunity solution trees, JTBD forces, experience maps | [details](docs/SKILLS.md#discovery-synthesis) |
| **`discovery-quant`** | Metric design, funnels, cohorts, retention, survival, segmentation, surveys, statistical guardrails, five runnable scripts | [details](docs/SKILLS.md#discovery-quant) |
| **`discovery-experiments`** | Assumption mapping, experiment runbooks, causal and quasi-causal design, thresholds set before the test, ethics | [details](docs/SKILLS.md#discovery-experiments) |
| **`discovery-prototyping`** | Fidelity chosen by question, and three working artifacts you can run today | [details](docs/SKILLS.md#discovery-prototyping) |
| **`discovery-ops`** | Weekly cadence, recruiting pipeline, research repository, automation, stakeholder communication | [details](docs/SKILLS.md#discovery-ops) |

The commander is the one that works alone. The other six are specialists it hands off to,
and it tells you when one of them would help.

---

## Commands

| Command | For |
|---|---|
| `/discovery` | "We want to build X." Diagnoses the real question and routes it |
| `/discovery-audit` | Paste a PRD or business case. Grades every claim against its evidence |
| `/discovery-interview` | Design a guide, rehearse the session, or write it up |
| `/discovery-synthesise` | Transcripts, tickets or survey exports become traceable findings |
| `/discovery-experiment` | Maps the assumptions, designs the cheapest test that settles one |
| `/discovery-prototype` | Builds a clickable prototype, a fake door, or a Wizard of Oz console |
| `/discovery-challenge` | Red-teams a plan or a conclusion |

On agents without slash commands, say "use the product-discovery skill" and describe the
situation. Or just describe the situation; the skills trigger on their own.

See **[docs/EXAMPLES.md](docs/EXAMPLES.md)** for what each one actually produces.

---

## The constitution

Seventeen rules bind every output. They are inline in the commander skill so they always load.

1. **Evidence has a source or it does not exist.** No tag means it is written as
   `[ASSUMPTION]`, not asserted
2. **Never invent a customer.** No fabricated quotes, transcripts, or personas-as-evidence
3. **Never invent a number.** Market sizes and benchmarks need a source and a date, or they
   are written as `[UNVERIFIED: how to get this]`
4. **The user decides.** It recommends with reasoning and names the trade-off. It never
   records a decision you did not make
5. **Assumptions are declared, never absorbed.** Silently filling a gap with a plausible
   value is treated as a bug, because that is what it is
6. **Opinion is not a finding**, whoever holds it
7. **Opportunities come from customers, solutions come from teams.** An opportunity phrased
   as a solution gets rewritten
8. **No causal claim without a causal design.** Including when the result is convenient
9. **Small n stays small n.** Below 30, counts not percentages. "Four of seven" never
   becomes "57% of users"
10. **Research must be able to change a decision**, or it is cancelled and the reason
    recorded
11. **Ask about the past, not the future**
12. **Test the riskiest assumption first, with the cheapest method that settles it**
13. **Contradicting evidence is surfaced, never smoothed**
14. **Consent and dignity are preconditions**
15. **Confidence is stated, not implied**, with the evidence that would most change it
16. **AI does not replace customer contact.** Asked to substitute, it produces the smallest
    real-contact path instead
17. **The user still needs something they can use.** Rigour that leaves someone with an
    empty table four hours before a meeting has failed them. When the artifact as asked for
    cannot be produced honestly, it produces the honest artifact that serves the same
    purpose

### When you push back

It does not argue twice and it does not refuse the work. It does the work with the guardrail
made structural:

- Fabricated material only under a `SYNTHETIC - NOT EVIDENCE` stamp, marked **per unit**:
  every participant `SYNTHETIC-P01`, every line opening `[SYNTHETIC]`, because a header does
  not survive a copy-paste
- Unsourced figures stay in `[UNVERIFIED]` brackets rather than being quietly promoted
- A decision recorded on thin evidence gets a confidence label matching the evidence, not
  matching the confidence in the room

> **Never refuse to help. Never agree to mislabel.**

A flat "no" gets worked around in one prompt. A stamp that travels three documents
downstream does not.

Full enforcement behaviour, the rationalisation table, and the exact wording for each rule:
[`skills/product-discovery/references/00-constitution.md`](skills/product-discovery/references/00-constitution.md).

---

## The evidence ladder

Every claim is graded on **how hard it would be to fake**. A decision may not claim more
confidence than its weakest load-bearing evidence.

| | Evidence | Supports | Cannot support |
|---|---|---|---|
| **L0** | Assertion, including a model's | A question | Anything about the world |
| **L1** | Analogy, benchmarks, desk research | A hypothesis | Anything about your customers |
| **L2** | Stated preference, surveys, "would you use" | What to investigate next | Prevalence, willingness to pay |
| **L3** | Reported behaviour, interview stories, tickets | Naming an opportunity | Prevalence, causality |
| **L4** | Observed behaviour, usability, analytics | Design decisions | Why, or what would happen if you changed it |
| **L5** | Simulated commitment, fake door, waitlist | Go or no-go | Satisfaction after use, retention |
| **L6** | Real commitment, money, contracts, adoption | The business case | Causality |
| **L7** | Controlled experiment | Causal effect size | Why the effect exists |

Conclusions carry one of four words: **Speculative, Indicated, Supported, Established**, plus
the single piece of evidence that would most change them.

**"Validated" is banned.** It has no defined threshold, it ends inquiry, and it travels into
decks where nobody can audit it.

---

## How the routing works

The intelligence is in refusing to recommend a method your situation cannot support.

Six values, guessed from context and corrected by you:

```
customer_access    none / slow / scheduled / on demand
qual_data          none / raw / coded
instrumentation    none / partial events / full analytics / experimentation platform
volume             under 100 per week / 100 to 1k / 1k to 10k / over 10k
product_state      concept / prototype / live and small / live at scale
market             B2C mass / B2B SMB / B2B enterprise / internal or government / marketplace
```

Then the overrides fire, and any one of them can veto the method you wanted:

- `customer_access = none` means no primary qualitative method is available this week. It
  routes to trace mining and opens fixing access as its own workstream, because that is the
  real blocker
- `instrumentation = none` means no diagnostic or causal quantitative method exists. It will
  not model around the gap
- `volume < 1k/week` means an A/B test will not reach power in a sensible window. It routes
  to commitment tests rather than running an underpowered test whose null gets misread as
  "no effect"
- `product_state = concept` means every behavioural method is off the table
- `market = enterprise or government` means small samples by nature, so it weights depth,
  triangulation and commitment evidence instead of pretending significance is available

`market` does more than adjust sample size. It changes what counts as evidence of value and
what a good metric looks like, so there is a full override per value: B2C, B2B SMB, B2B
enterprise, channel-sold, marketplace, internal or captive, government, clinical or
regulated.

Captive users cannot express demand, so the top of the evidence ladder does not apply to
them and mandated usage is graded L4 behaviour, never L6 commitment. A distributor's
interests oppose your research and they are a customer in their own right. A marketplace has
a liquidity problem before it has a product problem. A public service is judged against a
duty, not a growth target. In a clinical setting fake doors and Wizard of Oz are prohibited,
and stepped-wedge and shadow-mode designs take their place.

**Gates come before methods.** Procurement, ethics or IRB approval, certification, licensing
and design freezes are not deadlines. A deadline shortens the plan; a gate reorders it and
removes methods from the menu. And where a decision becomes irreversible at a freeze,
discovery is front-loaded onto it even when a cheaper method exists elsewhere.

Fifteen canonical questions, each with its own decision table, live in
[`01-intake-and-routing.md`](skills/product-discovery/references/01-intake-and-routing.md).

---

## The analysis scripts

Five command line tools. Standard library, no install. numpy only for two optional modes.

```bash
# Is this test even possible with the traffic we have?
python3 sample_size.py proportion --baseline 0.05 --mde-rel 0.10 --daily 4000

# Read a finished experiment, honestly
python3 experiment_analysis.py binary --control 1204 24010 --variant 1310 23980 --bayes

# Funnels, cohorts, Kaplan-Meier survival, Simpson's paradox detection
python3 cohorts_funnels.py cohort --csv activity.csv

# Kano, Van Westendorp, MaxDiff, PMF survey, Likert done properly
python3 survey_analysis.py kano --csv kano.csv

# Have we done enough interviews? Measured, not felt
python3 qual_saturation.py saturation --csv codes.csv --segment-col segment
```

Each prints its caveats next to its numbers, on purpose. Feed `experiment_analysis.py` an
underpowered null and it says so:

```
  Not distinguishable from zero at alpha=0.050.
  This is NOT evidence of no effect. With n=2,000 per group this test
  could only reliably detect effects above +63.19% relative.
  A real effect smaller than that would look exactly like this.
```

It also refuses to read a result through a broken randomiser: if the sample ratio check
fails, it stops and explains the usual causes rather than printing a number.

Every command, and the reference values the statistics are verified against:
**[docs/SCRIPTS.md](docs/SCRIPTS.md)**.

---

## The prototype artifacts

Three self-contained HTML files. Open in a browser, no build step, no dependencies.

**`clickable-prototype.html`** logs every hotspot click and every **dead click**, task time
and outcome, then exports a CSV comparable across a round of sessions. Dead clicks are the
strongest usability signal there is: a participant telling you where they expected something
to be. Author it by editing two objects at the top of the file.

**`fake-door.html`** with the honest close firing immediately on click, an intent capture,
and the threshold set in the file before you run. The ethics are built in and the validator
checks they are still there.

**`woz-console.html`** for Wizard of Oz: a participant pane and an operator pane, with
enforced latency so the operator cannot answer faster than the real system would. The log of
questions the operator could not answer is the requirements document.

---

## Templates

Thirteen, in `skills/product-discovery/templates/`:

discovery brief · interview guide · interview snapshot · opportunity solution tree ·
assumption map · test card · learning card · experiment pre-registration · research readout ·
evidence ledger (CSV) · decision record · opportunity canvas · the synthetic stamp

Each has a quality bar attached in
[`06-artifacts.md`](skills/product-discovery/references/06-artifacts.md). The bar is the
useful part. A test card whose threshold was written after the data arrived is not a test
card.

---

## What it will not do

- Write a quote nobody said
- Produce a market size with no source
- Call a before-and-after result an effect
- Turn "four of seven participants" into "57% of users"
- Choose your opportunity, set your priority, or declare product-market fit for you
- Design a study whose two possible outcomes lead to the same action
- Let a positive prototype test be reported as demand
- Grade mandated usage as evidence that anyone wanted the thing
- Recommend a fake door or a Wizard of Oz in a clinical or safety-critical setting
- Use the word "validated"

---

## Grounded in

Teresa Torres, *Continuous Discovery Habits* · Marty Cagan, *Inspired*, *Empowered* ·
Tony Ulwick, *Outcome-Driven Innovation* · Bob Moesta and Clayton Christensen on Jobs to be
Done · Rob Fitzpatrick, *The Mom Test* · Erika Hall, *Just Enough Research* · Steve Portigal,
*Interviewing Users* · Indi Young, *Mental Models* · David Bland and Alex Osterwalder,
*Testing Business Ideas* · Alberto Savoia, *The Right It* · Ron Kohavi, Diane Tang and Ya Xu,
*Trustworthy Online Controlled Experiments* · Virginia Braun and Victoria Clarke on thematic
analysis · Melissa Perri, *Escaping the Build Trap* · Itamar Gilad's Confidence Meter ·
Jeff Patton · Gojko Adzic · Simon Wardley · Noriaki Kano · Jakob Nielsen · Dan Olsen ·
Jeff Gothelf and Josh Seiden · Gary Klein · Eric Ries · Ash Maurya.

Forty-five frameworks, each with what it is for and, more usefully, **what it is not for**:
[`04-frameworks-canon.md`](skills/product-discovery/references/04-frameworks-canon.md).

The skills apply these with your real context and your real evidence, or they do not name
them. Name-dropping a framework and writing generic content underneath it is the most visible
form of fluff in product work, and it is treated here as a defect.

---

## File structure

```
discovery-os/
├── skills/
│   ├── product-discovery/          the commander
│   │   ├── SKILL.md                constitution, modes, intake, router
│   │   ├── references/             8 files: constitution, routing, methods,
│   │   │                           evidence, frameworks, anti-patterns,
│   │   │                           artifacts, AI boundary
│   │   └── templates/              13 fill-in artifacts
│   ├── discovery-interviewing/     5 references
│   ├── discovery-synthesis/        5 references
│   ├── discovery-quant/            4 references + 6 scripts
│   ├── discovery-experiments/      4 references
│   ├── discovery-prototyping/      4 references + 3 working HTML artifacts
│   └── discovery-ops/              3 references
├── commands/                       7 slash commands
├── docs/                           INSTALL, SKILLS, SCRIPTS, EXAMPLES
├── tests/validate.py               16 self-checks, run in CI
├── install.sh                      multi-runtime installer
├── package.sh                      builds release zips
└── .claude-plugin/                 plugin and marketplace manifests
```

**Verified on every push**, across Python 3.9, 3.11 and 3.13, on Linux and macOS:

```bash
python3 tests/validate.py
```

Sixteen checks: frontmatter, every internal reference resolves, the statistics library
against published values, the scripts against generated fixtures with known answers, the
prototype assets, the installer, and house style. Plus a real install and uninstall into a
sandbox home.

---

## FAQ

**Do I need Claude Code?**
No. It is Agent Skills, so it works in Codex, Copilot CLI and Gemini CLI too. The skills are
Markdown; the slash commands are a Claude Code convenience.

**Is this going to slow me down?**
For a two-line question, no; it answers in two lines. The discipline scales with the stakes.
Where it does add a step is before a study or a build decision, and that step is naming the
decision the work serves. That step saves quarters.

**What if I actually do want synthetic data?**
You can have it, stamped. Rehearsal transcripts for practising an interview are a legitimate
and useful thing. The stamp means it cannot quietly become a source six weeks later.

**Can it run interviews for me?**
It can moderate a session with a real participant under a strict protocol: disclosure,
recorded consent, a fixed guide, and a human reading the full transcript before synthesis.
It will not play the participant in anything that becomes data. The limits of AI moderation
are stated in the readout it writes, not hidden.

**Does it work for non-software products?**
The interviewing, synthesis, experiments and ops skills are product-agnostic. The
quantitative skill assumes you have digital behavioural data. Service, retail and
operational products are covered explicitly, including service blueprints.

**Does it work in Arabic, or other languages?**
The skills are in English. They contain explicit guidance on interviewing and coding in the
participant's strongest language, back-translating guides, and the concepts that travel
badly. Coding a corpus in a language your team does not read is one of the genuinely large
wins available here.

**I disagree with one of the seventeen rules.**
Open an issue and argue it. They are deliberate, not sacred. What they are not is
adjustable per prompt, because a guardrail you can talk your way past is decoration.

**Why is there no telemetry?**
Because a discovery tool that collects your product data without asking would be a bad joke.

---

## Requirements

**Context cost.** Installed, the seven skills and seven commands add about **880 tokens to
every session** as always-on descriptions, which is what lets them trigger on their own. The
commander costs roughly 5k more only when it actually fires; each specialist 1.1k to 1.6k.
Figures from `claude plugin details discovery-os`, so you can check them yourself.

| For | You need |
|---|---|
| The skills | Nothing. They are Markdown |
| The five analysis scripts | Python 3.8+, standard library only |
| Bayesian reads and CUPED | numpy |
| The three prototype artifacts | A browser |
| The installer | bash, plus git if you pipe it from curl |

No API keys. No accounts. No network calls at runtime.

---

## Uninstall

```bash
./install.sh --uninstall
```

or `/plugin uninstall discovery-os`. Either way it leaves nothing behind.

---

## Contributing

The three most useful things you can send, in order: a **routing problem** (you described a
situation and it sent you somewhere unhelpful), a **wrong attribution**, and a **missing
method**. See [CONTRIBUTING.md](CONTRIBUTING.md).

Run `python3 tests/validate.py` before opening a pull request.

---

## Companion

[**Tracking OS**](https://github.com/riadchaban994-bot/tracking-os) does the other half. Discovery OS
decides what to build; Tracking OS decides what to measure once you have built it. It walks the app,
screenshots every surface, and writes the tracking plan from what it saw, grading every event by how
strong the evidence actually is.

```bash
/plugin marketplace add riadchaban994-bot/tracking-os
/plugin install tracking-os@riadchaban
```

## Licence

MIT. Use it commercially, fork it, teach from it. Attribution appreciated, not required.

Built by [Riad Chaban](https://www.linkedin.com/in/riadchaban), Senior Product Manager,
Sharjah Digital Department.
