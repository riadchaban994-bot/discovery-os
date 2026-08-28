# Installation guide

Discovery OS is a set of seven Agent Skills. Any agent that reads `SKILL.md` files can use
it: Claude Code, Codex, GitHub Copilot CLI, Gemini CLI, and Claude Desktop or claude.ai
where custom skills are available on your plan.

Nothing is installed outside your home directory. Nothing is sent anywhere. There is no
telemetry.

---

## Contents

- [Option 1: Claude Code plugin (two commands)](#option-1-claude-code-plugin)
- [Option 2: the installer script (everything else)](#option-2-the-installer-script)
- [Option 3: manual copy](#option-3-manual-copy)
- [Option 4: one skill at a time](#option-4-one-skill-at-a-time)
- [Verifying the install](#verifying-the-install)
- [Upgrading](#upgrading)
- [Uninstalling](#uninstalling)
- [Requirements](#requirements)
- [Troubleshooting](#troubleshooting)

---

## Option 1: Claude Code plugin

The shortest path, and the one that keeps itself updated.

```bash
/plugin marketplace add riadchaban994-bot/discovery-os
```

```bash
/plugin install discovery-os@riadchaban
```

Restart Claude Code. You now have seven skills and seven slash commands.

`riadchaban994-bot/discovery-os` is the repository. `riadchaban` is the marketplace name
declared inside it. They differ on purpose, so the install command reads as a name rather
than a path.

**Project-scoped instead of personal?** Add it to the repository's `.claude/settings.json`
so everyone on the team gets it on checkout:

```json
{
  "extraKnownMarketplaces": {
    "riadchaban": {
      "source": { "source": "github", "repo": "riadchaban994-bot/discovery-os" }
    }
  },
  "enabledPlugins": { "discovery-os@riadchaban": true }
}
```

---

## Option 2: the installer script

Works for every agent, including Claude Code. Use this if you are on Codex, Copilot CLI or
Gemini CLI, or if you would rather not use the plugin system.

```bash
curl -fsSL https://raw.githubusercontent.com/riadchaban994-bot/discovery-os/main/install.sh | bash
```

Or from a clone, which is better if you want to read the script first:

```bash
git clone https://github.com/riadchaban994-bot/discovery-os.git
cd discovery-os
./install.sh
```

**What it does.** Detects every agent in your home directory, installs the seven skills
into each one's skills directory, installs the slash commands where the runtime supports
them, checks for Python and numpy, and prints what it did.

| Flag | Effect |
|---|---|
| `--dry-run` | Print every action, change nothing |
| `--uninstall` | Remove everything it installed |
| `--dir PATH` | Install from a specific local checkout |
| `--help` | Usage |

It is idempotent. Run it again to upgrade.

---

## Option 3: manual copy

Copy the seven directories inside `skills/` into your agent's skills directory.

| Agent | Personal skills directory |
|---|---|
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` (or `$CODEX_HOME/skills/`) |
| GitHub Copilot CLI | `~/.copilot/skills/` |
| Gemini CLI | `~/.gemini/skills/` |
| Codex, Copilot and Gemini together | `~/.agents/skills/` |

```bash
git clone https://github.com/riadchaban994-bot/discovery-os.git
cp -R discovery-os/skills/* ~/.claude/skills/
```

Claude Code does not read `~/.agents/skills/`. The other three do.

**Slash commands** are optional. For Claude Code, copy `commands/*.md` into
`~/.claude/commands/`. Without them the skills still trigger from plain description of the
situation.

---

## Option 4: one skill at a time

Some platforms take a single skill as a zip. Every
[release](https://github.com/riadchaban994-bot/discovery-os/releases) ships one zip per
skill for exactly this.

Start with `product-discovery.zip`. It is the router and it carries the constitution, so it
is the one that works alone. The other six are specialists it hands off to, and it will
tell you when one of them would help.

Build them yourself from a clone with `./package.sh`.

---

## Verifying the install

**In your agent**, ask something a skill should catch:

> We are thinking about adding a bulk upload feature. Should we build it?

You should get a diagnosis before any answer: what decision is at stake, what evidence
exists, and the cheapest method that would settle it. If you get a feature spec instead,
the skill did not load.

**On disk:**

```bash
ls ~/.claude/skills/ | grep discovery
```

**The analysis scripts:**

```bash
python3 ~/.claude/skills/discovery-quant/scripts/sample_size.py \
  proportion --baseline 0.05 --mde-rel 0.10 --daily 4000
```

**The whole repository**, from a clone:

```bash
python3 tests/validate.py
```

Sixteen checks covering structure, every internal reference, the statistics against known
values, the scripts against generated fixtures, the assets, the installer and house style.

---

## Upgrading

| Installed via | Upgrade |
|---|---|
| Claude Code plugin | `/plugin marketplace update riadchaban` then `/plugin update discovery-os` |
| Installer script | Run the same one-liner again |
| Manual copy | `git pull` then copy again |

The installer replaces each skill directory rather than merging, so a removed file does not
linger.

---

## Uninstalling

```bash
./install.sh --uninstall
```

Or, for the plugin:

```bash
/plugin uninstall discovery-os
```

Or by hand: delete the seven `discovery-*` and `product-discovery` directories from your
agent's skills directory, and the seven `discovery*.md` files from its commands directory.

---

## Requirements

| For | You need |
|---|---|
| The skills themselves | Nothing. They are Markdown |
| The five analysis scripts | Python 3.8 or newer, standard library only |
| Bayesian experiment reads and CUPED | numpy (`pip install numpy`) |
| The three prototype artifacts | A browser |
| The installer | bash, and git only if you pipe it from curl |

No API keys. No accounts. No network calls at runtime.

---

## Troubleshooting

**The skill does not trigger.**
Restart the agent; skills are read at startup. Check the directory is named exactly
`product-discovery` and contains `SKILL.md` with frontmatter. Then be explicit: "use the
product-discovery skill".

**`/plugin marketplace add` fails.**
The repository must be reachable and public. Check `git ls-remote
https://github.com/riadchaban994-bot/discovery-os.git`. If you are behind a proxy, use
Option 2 or 3.

**Slash commands do not appear.**
Only Claude Code installs them by default. On other runtimes, invoke the skill by name.
The commands are thin wrappers over the skills; nothing is lost.

**`python3: command not found`.**
Everything except the five analysis scripts still works. Install Python 3.8+ when you need
the quantitative side.

**"numpy not installed".**
Optional. Only the Bayesian read in `experiment_analysis.py` and the CUPED mode need it.
Every other calculation is pure standard library.

**A script cannot find `_stats`.**
Run it by path rather than copying a single file out of `scripts/`. The five scripts share
`_stats.py` and expect to sit next to it.

**The agent invents customers or numbers anyway.**
That is a bug, and the one worth reporting most. Open an issue with the prompt you used.
The constitution is in `skills/product-discovery/references/00-constitution.md` and it
should be holding.
