"""Validate default template metadata and local policy references."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
for template in (root / '.github/ISSUE_TEMPLATE').glob('*.md'):
    start, meta, body = template.read_text().split('---', 2)
    assert not start and body.strip(), template
    for field in ('name', 'about'):
        assert re.search(rf'^{field}: .+', meta, re.M), (template, field)
for doc in root.rglob('*.md'):
    for link in re.findall(r'\]\(([^)]+)\)', doc.read_text()):
        if '://' not in link and not link.startswith('#'):
            assert (doc.parent / link.split('#')[0]).exists(), (doc, link)
print('Checked issue templates and local policy links')
