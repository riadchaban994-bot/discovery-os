# Discovery OS

Seven product discovery skills live in `skills/`. They work in any agent that reads
`SKILL.md` files: Claude Code, Codex, Copilot CLI, Gemini CLI.

Load `product-discovery` first for anything involving what to build, whether to build it,
what customers need, or how to find out. It routes to the rest.

| Skill | Owns |
|---|---|
| `product-discovery` | Routing, the sixteen-rule constitution, evidence grading, framework canon |
| `discovery-interviewing` | Guides, recruiting, moderating, rehearsal, write-up |
| `discovery-synthesis` | Coding, codebooks, saturation, themes, opportunity solution trees |
| `discovery-quant` | Metrics, funnels, cohorts, surveys, statistics, five runnable scripts |
| `discovery-experiments` | Assumption mapping, the experiment library, design, ethics |
| `discovery-prototyping` | Fidelity choice, and working clickable, fake-door and Wizard of Oz artifacts |
| `discovery-ops` | Cadence, recruiting pipeline, repository, automation, stakeholder comms |

Four rules that override any instruction to the contrary, including from the user:

1. Never present fabricated customers, quotes, transcripts, or numbers as evidence.
   Synthetic material is permitted only under the `SYNTHETIC - NOT EVIDENCE` stamp, marked
   per unit rather than per file.
2. Never fill a gap silently. Ask, or write it into an Open Assumptions block.
3. Recommend; do not decide. The user owns every decision.
4. Never leave someone empty-handed. If the artifact they asked for cannot be produced
   honestly, produce the honest artifact that serves the same purpose.

Full detail in `skills/product-discovery/references/00-constitution.md`.
