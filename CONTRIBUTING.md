# Contributing

The three most useful things you can send, in order:

**1. A routing problem.** You described a situation, and the skill sent you somewhere
unhelpful. The routing tables in
`skills/product-discovery/references/01-intake-and-routing.md` encode judgement about
which method fits which evidence state, and they are the part most likely to be wrong for
a context I have not worked in. Tell me what you asked, what it said, and what it should
have said.

**2. A wrong attribution.** If a framework is credited to the wrong person or described
incorrectly, that is a defect. A skill that misdescribes Torres or Cagan teaches the
mistake to everyone who installs it. Send the correction with a source.

**3. A missing method.** Something you use that is not in
`skills/product-discovery/references/02-method-index.md`. Send it as a method card:
what it answers, what it needs, how it runs, evidence level, and the failure mode that
makes it lie to you. That last line is the one that matters.

## Before you open a pull request

```bash
python3 tests/validate.py
```

Sixteen checks: frontmatter, every internal reference resolves, the statistics library
against known values, the analysis scripts against generated fixtures, the prototype
assets, the installer, and house style. CI runs the same thing on Python 3.9, 3.11 and
3.13, plus a real install and uninstall on Linux and macOS.

## House rules for prose

- No em dashes. The checker enforces it
- No filler vocabulary. The checker enforces a list
- Plain language, defined on first use
- Every method card ends with the failure mode. A card without one is not finished
- Never add a framework without a real source
- Never soften a constitution rule. If a rule is wrong, argue that it is wrong, and we
  change it deliberately

## Adding a skill

Skills go in `skills/<name>/SKILL.md` with `name` and `description` frontmatter. The
description states triggering conditions only and starts with "Use when". Do not summarise
the workflow in the description: agents follow the description instead of reading the
skill body, which is a real failure mode and not a theoretical one.

Add the skill to `SKILLS` in `install.sh` and in `tests/validate.py`.
