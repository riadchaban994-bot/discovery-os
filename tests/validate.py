#!/usr/bin/env python3
"""
Discovery OS self-check.

Runs every structural rule the repository claims to hold. Exits non-zero on the
first category that fails, so CI blocks a broken release.

    python3 tests/validate.py            # everything
    python3 tests/validate.py --list     # what it checks
"""

import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SKILLS = ['product-discovery', 'discovery-interviewing', 'discovery-synthesis',
          'discovery-quant', 'discovery-experiments', 'discovery-prototyping',
          'discovery-ops']
COMMANDS = ['discovery', 'discovery-audit', 'discovery-interview',
            'discovery-synthesise', 'discovery-experiment', 'discovery-prototype',
            'discovery-challenge']

failures = []
passes = []


def check(name):
    def deco(fn):
        fn._check_name = name
        return fn
    return deco


def fail(msg):
    failures.append(msg)


def md_files():
    out = []
    for r, d, fs in os.walk('.'):
        d[:] = [x for x in d if x not in ('.git', 'dist', '__pycache__', 'node_modules')]
        out += [os.path.join(r, f) for f in fs if f.endswith('.md')]
    return sorted(out)


def all_text_files():
    out = []
    for r, d, fs in os.walk('.'):
        d[:] = [x for x in d if x not in ('.git', 'dist', '__pycache__', 'node_modules')]
        out += [os.path.join(r, f) for f in fs
                if f.endswith(('.md', '.csv', '.html', '.sh', '.json', '.py'))]
    return sorted(out)


# ---------------------------------------------------------------------------
@check("every declared skill exists and has valid frontmatter")
def t_frontmatter():
    for sk in SKILLS:
        p = f'skills/{sk}/SKILL.md'
        if not os.path.exists(p):
            fail(f'{p} missing'); continue
        src = open(p, encoding='utf-8').read()
        m = re.match(r'^---\n(.*?)\n---\n', src, re.S)
        if not m:
            fail(f'{sk}: no YAML frontmatter'); continue
        fm = m.group(1)
        if len(fm) > 1024:
            fail(f'{sk}: frontmatter is {len(fm)} chars, limit is 1024')
        name = re.search(r'^name:\s*(.+)$', fm, re.M)
        desc = re.search(r'^description:\s*(.+)$', fm, re.M)
        if not name:
            fail(f'{sk}: no name field'); continue
        if not desc:
            fail(f'{sk}: no description field'); continue
        if name.group(1).strip() != sk:
            fail(f'{sk}: name "{name.group(1).strip()}" does not match directory')
        if not re.fullmatch(r'[a-z0-9-]+', name.group(1).strip()):
            fail(f'{sk}: name must be lowercase letters, numbers and hyphens only')
        if not desc.group(1).strip().startswith('Use when'):
            fail(f'{sk}: description must start with "Use when"')


@check("descriptions state triggers, not workflow")
def t_desc_no_workflow():
    # A description that summarises the process gets followed INSTEAD of the skill body.
    tells = [' then ', 'step 1', 'workflow', 'first, ']
    for sk in SKILLS:
        src = open(f'skills/{sk}/SKILL.md', encoding='utf-8').read()
        d = re.search(r'^description:\s*(.+)$', src, re.M).group(1).lower()
        for t in tells:
            if t in d:
                fail(f'{sk}: description may summarise workflow ("{t.strip()}")')


@check("every file path referenced in a skill resolves")
def t_links():
    n = 0
    for p in md_files():
        if not p.startswith('./skills/'):
            continue
        skill_dir = os.sep.join(p.split(os.sep)[:3])   # ./skills/<name>
        for m in re.finditer(r'`((?:\.\./)?[a-z0-9_./-]+\.(?:md|py|csv|html))`',
                             open(p, encoding='utf-8').read()):
            n += 1
            target = os.path.normpath(os.path.join(skill_dir, m.group(1)))
            if not os.path.exists(target):
                fail(f'{p}: broken reference {m.group(1)}')
    if n < 50:
        fail(f'only {n} internal references found, expected 50+; parser may be broken')


@check("every slash command names a real skill and resolves its paths")
def t_commands():
    for c in COMMANDS:
        p = f'commands/{c}.md'
        if not os.path.exists(p):
            fail(f'{p} missing'); continue
        src = open(p, encoding='utf-8').read()
        if not src.startswith('---\n'):
            fail(f'{c}: no frontmatter')
        if 'description:' not in src:
            fail(f'{c}: no description')
        m = re.search(r'Invoke the `([a-z-]+)` skill', src)
        if not m:
            fail(f'{c}: does not name a skill to invoke'); continue
        skill = m.group(1)
        if skill not in SKILLS:
            fail(f'{c}: invokes unknown skill "{skill}"'); continue
        for rel in re.findall(r'`((?:references|assets|templates)/[a-z0-9_.-]+)`', src):
            if rel.endswith('/...') or '...' in rel:
                continue          # the "paths are relative to" note, not a real path
            if not os.path.exists(f'skills/{skill}/{rel}'):
                fail(f'{c}: {rel} does not exist in {skill}')


@check("plugin and marketplace manifests are valid and agree")
def t_manifests():
    try:
        plug = json.load(open('.claude-plugin/plugin.json', encoding='utf-8'))
        mkt = json.load(open('.claude-plugin/marketplace.json', encoding='utf-8'))
    except Exception as e:
        fail(f'manifest JSON invalid: {e}'); return
    for k in ('name', 'version', 'description'):
        if k not in plug:
            fail(f'plugin.json missing {k}')
    if not mkt.get('plugins'):
        fail('marketplace.json has no plugins'); return
    entry = mkt['plugins'][0]
    if entry.get('name') != plug.get('name'):
        fail('marketplace plugin name does not match plugin.json name')
    if entry.get('version') != plug.get('version'):
        fail('marketplace plugin version does not match plugin.json version')


@check("the synthetic stamp is byte-identical everywhere it appears")
def t_stamp():
    canonical = 'SYNTHETIC - NOT EVIDENCE'
    seen = 0
    for p in all_text_files():
        s = open(p, encoding='utf-8').read()
        if 'SYNTHETIC' not in s:
            continue
        # dash class written as escapes so this file contains no literal em dash
        for m in re.finditer('SYNTHETIC[ \\t]*[-\\u2013\\u2014:][ \\t]*NOT[ \\t]*EVIDENCE', s):
            seen += 1
            if m.group(0) != canonical:
                fail(f'{p}: stamp variant "{m.group(0)}" is not the canonical form')
    if seen < 5:
        fail(f'stamp appears only {seen} times; it should be in the constitution, the '
             f'AI boundary, the interviewing skill and the template')


@check("no em dashes anywhere (house style)")
def t_no_em_dash():
    for p in all_text_files():
        s = open(p, encoding='utf-8').read()
        dash = '\u2014'           # written as an escape so this file stays clean
        if dash in s:
            line = next(l for l in s.split('\n') if dash in l)
            fail(f'{p}: em dash in "{line.strip()[:60]}"')


@check("no AI filler vocabulary")
def t_no_filler():
    banned = [r'\bdelv(e|ing)\b', r'\bleverag(e|ing)\b(?!-)', r'\bseamless',
              r'\brobust\b', r"worth noting", r"in today'?s", r'\bunlock',
              r'\btapestry\b', r'\brealm\b', r'\bnavigat(e|ing) the\b']
    for p in md_files():
        s = open(p, encoding='utf-8').read()
        for pat in banned:
            for m in re.finditer(pat, s, re.I):
                # "highest-leverage" is a compound noun, allowed
                ctx = s[max(0, m.start() - 10):m.start()]
                if ctx.endswith('highest-') or ctx.endswith('high-'):
                    continue
                fail(f'{p}: filler term "{m.group(0)}"')


@check("the word 'validated' appears only where it is being banned")
def t_validated():
    for p in md_files():
        s = open(p, encoding='utf-8').read()
        for m in re.finditer(r'\bvalidated\b', s, re.I):
            # "validated learning" is Eric Ries's own term for a concept, not a claim
            if s[m.start():m.start() + 18].lower() == 'validated learning':
                continue
            window = s[max(0, m.start() - 240):m.end() + 240].lower()
            if not any(w in window for w in ('banned', 'nothing is validated',
                                             'the word', 'do not', 'never',
                                             'feeling validated', 'licence', 'accumulates')):
                fail(f'{p}: unqualified use of "validated"')


@check("all Python analysis scripts parse and expose --help")
def t_scripts_parse():
    import ast
    scripts = sorted(f for f in os.listdir('skills/discovery-quant/scripts')
                     if f.endswith('.py'))
    if len(scripts) < 6:
        fail(f'expected 6 script files, found {len(scripts)}')
    for f in scripts:
        p = f'skills/discovery-quant/scripts/{f}'
        try:
            ast.parse(open(p, encoding='utf-8').read())
        except SyntaxError as e:
            fail(f'{p}: syntax error {e}')
        if f.startswith('_'):
            continue
        r = subprocess.run([sys.executable, p, '--help'],
                           capture_output=True, text=True, timeout=60)
        if r.returncode != 0:
            fail(f'{p} --help exited {r.returncode}: {r.stderr[:200]}')


@check("statistics library matches known reference values")
def t_stats_correct():
    sys.path.insert(0, os.path.join(ROOT, 'skills/discovery-quant/scripts'))
    try:
        import _stats as st
    except Exception as e:
        fail(f'cannot import _stats: {e}'); return
    cases = [
        ('norm_ppf(0.975)', st.norm_ppf(0.975), 1.959964, 1e-5),
        ('norm_ppf(0.80)', st.norm_ppf(0.80), 0.841621, 1e-5),
        ('norm_cdf(1.96)', st.norm_cdf(1.96), 0.975002, 1e-5),
        ('t p(2.086, df=20)', st.t_two_sided_p(2.086, 20), 0.05, 1e-3),
        ('chi2_sf(3.841, 1)', st.chi2_sf(3.841, 1), 0.05, 1e-4),
        ('chi2_sf(5.991, 2)', st.chi2_sf(5.991, 2), 0.05, 1e-4),
        ('chi2_sf(11.070, 5)', st.chi2_sf(11.070, 5), 0.05, 1e-4),
    ]
    for label, got, want, tol in cases:
        if abs(got - want) > tol:
            fail(f'{label} = {got:.6f}, expected {want} +/- {tol}')
    lo, hi = st.wilson_ci(5, 20)
    if not (abs(lo - 0.1119) < 1e-3 and abs(hi - 0.4687) < 1e-3):
        fail(f'wilson_ci(5,20) = ({lo:.4f}, {hi:.4f}), expected (0.1119, 0.4687)')
    # Benjamini-Hochberg on the canonical example rejects exactly the first two
    res = st.benjamini_hochberg([0.001, 0.008, 0.039, 0.041, 0.042, 0.06, 0.074, 0.205])
    rejected = [i for i, p, adj, r in res if r]
    if rejected != [0, 1]:
        fail(f'benjamini_hochberg rejected {rejected}, expected [0, 1]')


@check("sample size calculation matches the textbook formula")
def t_sample_size():
    sys.path.insert(0, os.path.join(ROOT, 'skills/discovery-quant/scripts'))
    import sample_size as ss
    n = ss.n_proportion(0.05, 0.055)
    if not 30500 <= n <= 32000:
        fail(f'n_proportion(0.05, 0.055) = {n}, expected ~31,200')
    mde = ss.mde_proportion(0.05, 20000)
    if not 0.0060 <= mde <= 0.0066:
        fail(f'mde_proportion(0.05, 20000) = {mde:.5f}, expected ~0.0063')


@check("scripts produce correct results on generated fixtures")
def t_end_to_end():
    import csv
    import random
    import tempfile
    random.seed(7)
    d = tempfile.mkdtemp()
    scripts = os.path.join(ROOT, 'skills/discovery-quant/scripts')

    # Simpson's paradox fixture: every segment favours the variant, aggregate does not
    simp = os.path.join(d, 'simp.csv')
    with open(simp, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['segment', 'group', 'converted', 'total'])
        w.writerow(['desktop', 'control', 180, 200])
        w.writerow(['desktop', 'variant', 95, 100])
        w.writerow(['mobile', 'control', 20, 100])
        w.writerow(['mobile', 'variant', 45, 200])
    r = subprocess.run([sys.executable, f'{scripts}/cohorts_funnels.py', 'simpson',
                        '--csv', simp], capture_output=True, text=True)
    if "SIMPSON'S PARADOX" not in r.stdout:
        fail('simpson detector missed a constructed reversal')

    # SRM fixture: a badly skewed split must be flagged
    r = subprocess.run([sys.executable, f'{scripts}/sample_size.py', 'srm',
                        '--counts', '10000', '9000'], capture_output=True, text=True)
    if 'SRM DETECTED' not in r.stdout:
        fail('SRM check missed a 10000/9000 split')

    # An underpowered null must be reported as underpowered, never as "no effect"
    r = subprocess.run([sys.executable, f'{scripts}/experiment_analysis.py', 'binary',
                        '--control', '50', '2000', '--variant', '54', '2000'],
                       capture_output=True, text=True)
    if 'NOT evidence of no effect' not in r.stdout:
        fail('underpowered null was not labelled as underpowered')

    # Saturation: a corpus where late sources add nothing must read as saturated
    codes = os.path.join(d, 'codes.csv')
    with open(codes, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['source_id', 'code'])
        base = ['a', 'b', 'c', 'd']
        for i in range(1, 9):
            for c in (base + (['new%d' % i] if i <= 2 else [])):
                w.writerow(['P%02d' % i, c])
    r = subprocess.run([sys.executable, f'{scripts}/qual_saturation.py', 'saturation',
                        '--csv', codes], capture_output=True, text=True)
    if 'SATURATED' not in r.stdout:
        fail('saturation detector missed a saturated corpus')


@check("prototype assets are self-contained and parse as HTML")
def t_assets():
    import html.parser
    assets = sorted(os.listdir('skills/discovery-prototyping/assets'))
    for a in ['clickable-prototype.html', 'fake-door.html', 'woz-console.html']:
        if a not in assets:
            fail(f'missing asset {a}'); continue
        src = open(f'skills/discovery-prototyping/assets/{a}', encoding='utf-8').read()
        try:
            html.parser.HTMLParser().feed(src)
        except Exception as e:
            fail(f'{a}: HTML parse error {e}')
        if re.search(r'(src|href)\s*=\s*["\']https?://', src):
            fail(f'{a}: loads an external resource, must be self-contained')
    # the fake door must keep its honest close
    fd = open('skills/discovery-prototyping/assets/fake-door.html', encoding='utf-8').read()
    if 'not built yet' not in fd.lower():
        fail('fake-door.html: the honest close has been removed')


@check("installer is valid shell and lists every skill and command")
def t_installer():
    r = subprocess.run(['bash', '-n', 'install.sh'], capture_output=True, text=True)
    if r.returncode != 0:
        fail(f'install.sh syntax error: {r.stderr[:200]}')
    src = open('install.sh', encoding='utf-8').read()
    for sk in SKILLS:
        if sk not in src:
            fail(f'install.sh does not install {sk}')
    for c in COMMANDS:
        if c not in src:
            fail(f'install.sh does not install /{c}')


@check("templates referenced by the skills all exist")
def t_templates():
    expected = ['discovery-brief', 'interview-guide', 'interview-snapshot',
                'assumption-map', 'test-card', 'learning-card', 'experiment-plan',
                'research-readout', 'decision-record', 'opportunity-canvas',
                'opportunity-solution-tree', 'synthetic-stamp']
    for t in expected:
        p = f'skills/product-discovery/templates/{t}.md'
        if not os.path.exists(p):
            fail(f'missing template {p}')
    if not os.path.exists('skills/product-discovery/templates/evidence-ledger.csv'):
        fail('missing evidence-ledger.csv template')


@check("markdown links in README, docs and CONTRIBUTING resolve")
def t_doc_links():
    import urllib.parse
    targets = ['README.md', 'CONTRIBUTING.md', 'AGENTS.md'] + \
              [f'docs/{f}' for f in sorted(os.listdir('docs'))]
    for t in targets:
        if not os.path.exists(t):
            fail(f'{t} missing'); continue
        src = open(t, encoding='utf-8').read()
        base = os.path.dirname(t)
        for m in re.finditer(r'\]\((?!https?:|mailto:)([^)#\s]+)(#[^)\s]*)?\)', src):
            rel = urllib.parse.unquote(m.group(1))
            target = os.path.normpath(os.path.join(base, rel))
            if not os.path.exists(target):
                fail(f'{t}: link to {rel} does not resolve')
            anchor = m.group(2)
            if anchor and target.endswith('.md'):
                heads = re.findall(r'^#{1,6}\s+(.+)$', open(target, encoding='utf-8').read(), re.M)
                slugs = set()
                for h in heads:
                    slug = re.sub(r'[^\w\s-]', '', h.lower()).strip().replace(' ', '-')
                    slugs.add('#' + slug)
                if anchor not in slugs:
                    fail(f'{t}: anchor {anchor} not found in {rel}')


@check("installer resolve_source writes only the path to stdout")
def t_installer_stdout_clean():
    # Regression: when piped from curl the script clones itself, and any progress
    # message written to stdout is captured as part of the source path, which
    # silently breaks every install that is not run from a clone.
    src = open('install.sh', encoding='utf-8').read()
    m = re.search(r'resolve_source\(\)\s*\{(.*?)\n\}', src, re.S)
    if not m:
        fail('cannot find resolve_source in install.sh'); return
    body = m.group(1)
    for line in body.split('\n'):
        st = line.strip()
        if not st or st.startswith('#'):
            continue
        # every emitting call inside this function must be redirected to stderr
        if re.match(r'(dim|bold|ok|skip|warn|echo)\b', st) and '>&2' not in st:
            fail(f'install.sh resolve_source writes to stdout: "{st[:60]}"')
        if st.startswith('git clone') and '>&2' not in st:
            fail('install.sh: git clone in resolve_source must redirect to stderr')


# ---------------------------------------------------------------------------
def main():
    checks = [v for k, v in sorted(globals().items())
              if k.startswith('t_') and callable(v)]
    if '--list' in sys.argv:
        for c in checks:
            print(' -', c._check_name)
        return 0

    print('Discovery OS self-check')
    print('=' * 66)
    for c in checks:
        before = len(failures)
        try:
            c()
        except Exception as e:
            fail(f'{c._check_name}: check itself raised {type(e).__name__}: {e}')
        added = len(failures) - before
        mark = 'ok  ' if added == 0 else 'FAIL'
        print(f'  [{mark}] {c._check_name}' + (f'  ({added})' if added else ''))
        if added == 0:
            passes.append(c._check_name)

    print('=' * 66)
    if failures:
        print(f'{len(failures)} problem(s):\n')
        for f in failures:
            print('  x', f)
        return 1
    print(f'{len(passes)}/{len(checks)} checks passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
