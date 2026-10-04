"""Standard-library packaging checks; this is NOT a model behavioral test."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'SKILL.md', 'README.md', 'README.zh-CN.md', 'LICENSE',
    'references/input-schema.md', 'references/calculation-model.md',
    'references/evidence-and-research.md', 'examples/china-household-example.md',
    'tests/scenarios.md', 'tests/behavioral-cases.json', 'tests/validation-report.md',
]
for name in required:
    assert (ROOT / name).is_file(), f'Missing package file: {name}'

skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
frontmatter = skill.split('---', 2)[1]
assert len(frontmatter) < 1024
assert re.search(r'^name: evaluating-job-offers$', frontmatter, re.M)
assert re.search(r'^description: Use when .+', frontmatter, re.M)
for keyword in ('Household mode', 'risk-adjusted', 'after-tax', 'effective hourly', 'Do not fabricate'):
    assert keyword in skill, f'Original discovery/smoke check failed: {keyword}'

for path in ROOT.rglob('*.md'):
    if '.git' in path.parts:
        continue
    text = path.read_text(encoding='utf-8')
    assert '\ufffd' not in text, f'Invalid replacement character: {path}'
    for link in re.findall(r'\]\(([^)]+)\)', text):
        if '://' not in link and not link.startswith('#'):
            target = (path.parent / link.split('#')[0]).resolve()
            assert target.is_relative_to(ROOT), f'Link escapes package: {path}: {link}'
            assert target.exists(), f'Broken local link: {path}: {link}'

cases = json.loads((ROOT / 'tests/behavioral-cases.json').read_text(encoding='utf-8'))
assert len(cases) == 8 and len({c['id'] for c in cases}) == 8
assert all(set(c) == {'id', 'prompt'} and c['prompt'] for c in cases)
assert 'MIT License' in (ROOT / 'LICENSE').read_text(encoding='utf-8')
print('PASS: package, UTF-8, frontmatter, original smoke checks, local links, 8 prompt-only cases.')
print('Structure only. Behavioral acceptance requires separate-context responses and manual scoring.')
