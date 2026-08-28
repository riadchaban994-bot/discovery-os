# Discovery OS

**Product discovery for AI agents, done properly.**

A master skill system that turns Claude Code, Codex, Copilot CLI or Gemini CLI into a
disciplined discovery partner: one that picks the method your evidence can actually
support, and refuses to invent a customer, a number, or a confidence level to fill a gap.

Free. MIT licensed. Built for [ProductTank Syria](https://www.meetup.com/pro/producttank),
Damascus, August 2026.

---

## The problem it solves

AI has made every part of product discovery faster, including the parts whose value came
from being slow. Ask a model for user research and you get research-shaped text: fluent
personas nobody met, quotes nobody said, market sizes nobody measured, and a confident
recommendation resting on none of it. It reads exactly like the real thing, and three
documents downstream nobody can tell the difference.

Discovery OS makes that failure structurally hard. Every claim carries its source. Every
gap is declared rather than filled. Every conclusion carries a confidence level it can
defend. And on any question of what customers want, the system will not let a model stand
in for a person.

It also does the opposite job, which matters just as much: it stops teams running elegant
research that changes no decision.

---

## Install

### Claude Code, one command

```bash
/plugin marketplace add riadchaban/discovery-os
```

then

```bash
/plugin install discovery-os@riadchaban
```

Restart, and `/discovery` is live.

### Everything else, one command

```bash
curl -fsSL https://raw.githubusercontent.com/riadchaban/discovery-os/main/install.sh | bash
```

Detects every agent on your machine, installs into each, and tells you what it did.
Works with Claude Code, Codex, Copilot CLI and Gemini CLI. Idempotent, so run it again to
upgrade. `--uninstall` removes everything. `--dry-run` shows you first.

### Or by hand

Copy `skills/*` into your agent's skills directory:

| Agent | Path |
|---|---|
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |
| Copilot CLI | `~/.copilot/skills/` |
| Gemini CLI | `~/.gemini/skills/` |
| Codex, Copilot and Gemini together | `~/.agents/skills/` |

No dependencies. Python 3.8+ is needed only for the five analysis scripts, and numpy only
for the Bayesian and CUPED modes.

---

## Use it

Describe the situation and the skills trigger on their own. Or be explicit:

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
situation.

---

## What is inside

**Seven skills.**

| Skill | Owns |
|---|---|
| `product-discovery` | The commander. Routes any question to the right method for your evidence. Carries the constitution, the evidence ladder, 60+ method cards, the framework canon, and the AI boundary |
| `discovery-interviewing` | Guide design, recruiting and screening, moderating, AI-moderated sessions with real participants, rehearsal, write-up |
| `discovery-synthesis` | Coding and codebooks, saturation measured rather than felt, thematic analysis, opportunity solution trees, JTBD forces, experience maps |
| `discovery-quant` | Metric design, funnels, cohorts, retention, survival, surveys, statistical guardrails, and five tested scripts |
| `discovery-experiments` | Assumption mapping, experiment runbooks, causal and quasi-causal design, ethics of testing |
| `discovery-prototyping` | Fidelity choice by question, and three working artifacts you can run today |
| `discovery-ops` | Weekly cadence, recruiting pipeline, research repository, automation, stakeholder communication |

**Five analysis scripts that actually run.** Standard library, no install.

```bash
# Can we even detect the effect we care about, with the traffic we have?
python3 sample_size.py proportion --baseline 0.05 --mde-rel 0.10 --daily 4000

# Read a finished experiment, including what a null result does and does not mean
python3 experiment_analysis.py binary --control 1204 24010 --variant 1310 23980 --bayes

# Funnels, cohort retention, Kaplan-Meier survival, Simpson's paradox detection
python3 cohorts_funnels.py cohort --csv activity.csv

# Kano, Van Westendorp, MaxDiff, PMF survey, Likert done properly
python3 survey_analysis.py kano --csv kano.csv

# Have we done enough interviews? Measured, not felt
python3 qual_saturation.py saturation --csv codes.csv --segment-col segment
```

Each one prints its own caveats next to its numbers, on purpose.

**Three working prototypes.** Open them in a browser, no build step.

- `clickable-prototype.html` logs every hotspot click, every **dead click**, task time and
  outcome, and exports a CSV you can compare across a round of sessions
- `fake-door.html` with the honest close and the threshold built in
- `woz-console.html` for Wizard of Oz, with enforced latency so the result transfers

**Thirteen templates.** Discovery brief, interview guide and snapshot, opportunity solution
tree, assumption map, test and learning cards, experiment pre-registration, research
readout, evidence ledger, decision record, opportunity canvas, and the synthetic stamp.

---

## The constitution

Sixteen rules bind every output. The five that matter most:

1. **Evidence has a source or it does not exist.** No tag means it is written as
   `[ASSUMPTION]`, not asserted.
2. **Never invent a customer.** No fabricated quotes, transcripts, or personas-as-evidence.
   Synthetic material exists only under a stamp that survives downstream.
3. **The user decides.** The system recommends with reasoning and names the trade-off. It
   never records a decision you did not make.
4. **Assumptions are declared, never absorbed.** Silently filling a gap with a plausible
   value is treated as a bug, because that is what it is.
5. **AI does not replace customer contact.** Asked to substitute model knowledge for a real
   person on a question of value, it produces the smallest real-contact path instead.

When you push against a rule, it does not argue twice and it does not refuse the work. It
does the work with the guardrail made structural: stamped, bracketed, or labelled at the
confidence the evidence supports.

**Never refuse to help. Never agree to mislabel.**

---

## The evidence ladder

Every claim is graded on how hard it would be to fake. A decision may not claim more
confidence than its weakest load-bearing evidence.

| | Evidence | Supports |
|---|---|---|
| **L0** | Assertion, including a model's | A question |
| **L1** | Analogy, benchmarks, desk research | A hypothesis |
| **L2** | Stated preference, surveys, "would you use" | What to investigate next |
| **L3** | Reported behaviour, interview stories, tickets | Naming an opportunity |
| **L4** | Observed behaviour, usability, analytics | Design decisions |
| **L5** | Simulated commitment, fake door, waitlist | Go or no-go |
| **L6** | Real commitment, money, contracts, adoption | The business case |
| **L7** | Controlled experiment | Causal claims |

Conclusions carry one of four words: **Speculative, Indicated, Supported, Established** 
plus the single piece of evidence that would most change them.

"Validated" is banned. It has no threshold and it ends thinking.

---

## Grounded in

Teresa Torres, *Continuous Discovery Habits* · Marty Cagan, *Inspired* and *Empowered* ·
Tony Ulwick, *Outcome-Driven Innovation* · Bob Moesta and Clayton Christensen on
Jobs to be Done · Rob Fitzpatrick, *The Mom Test* · Erika Hall, *Just Enough Research* ·
Steve Portigal, *Interviewing Users* · Indi Young, *Mental Models* · David Bland and Alex
Osterwalder, *Testing Business Ideas* · Alberto Savoia, *The Right It* · Ron Kohavi, Diane
Tang and Ya Xu, *Trustworthy Online Controlled Experiments* · Braun and Clarke on thematic
analysis · Melissa Perri, *Escaping the Build Trap* · Itamar Gilad's Confidence Meter ·
Jeff Patton · Gojko Adzic · Simon Wardley · Noriaki Kano · Jakob Nielsen · Dan Olsen ·
Jeff Gothelf and Josh Seiden.

The skills apply these with your real context and your real evidence, or they do not name
them. Name-dropping a framework and writing generic content underneath it is the most
visible form of fluff in product work, and the system treats it as a defect.

---

## What it will not do

- Write a quote nobody said
- Produce a market size with no source
- Call a before-and-after result an effect
- Turn "four of seven participants" into "57% of users"
- Choose your opportunity, set your priority, or declare product-market fit for you
- Design a study whose two possible outcomes lead to the same action
- Let a positive prototype test be reported as demand
- Use the word "validated"

---

## Contributing

Issues and pull requests welcome, particularly: methods that are missing, framework
attributions that are wrong, and cases where the routing sends you somewhere unhelpful.
The last of those is the most useful thing you can report.

## Licence

MIT. Use it commercially, fork it, teach from it. Attribution appreciated, not required.

Built by [Riad Chaban](https://www.linkedin.com/in/riadchaban).
