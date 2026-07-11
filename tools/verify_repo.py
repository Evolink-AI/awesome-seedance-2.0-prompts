#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from urllib.parse import parse_qs, urlparse
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
READMES = [
    'README.md', 'README_es.md', 'README_pt.md', 'README_ja.md', 'README_ko.md',
    'README_de.md', 'README_fr.md', 'README_tr.md', 'README_zh-TW.md',
    'README_zh-CN.md', 'README_ru.md',
]
R2_PREFIX = 'https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/'
CAMPAIGN = 'awesome-seedance-2.0-prompts'
CASE_RE = re.compile(r'^### Case (\d+): \[([^]]+)\]\(([^)]+)\) \(by \[@([^]]+)\]\(([^)]+)\)\)', re.M)
PROMPT_RE = re.compile(r'(?ms)\*\*Prompt:\*\*\n\n```\n(.*?)\n```')
IMAGE_RE = re.compile(r'<img src="([^"]+)"')
HTTP_RE = re.compile(r'https?://[^\s)>"]+')

errors: list[str] = []

def check(ok: bool, message: str) -> None:
    if not ok:
        errors.append(message)

def main() -> int:
    actual = sorted(p.name for p in ROOT.glob('README*.md'))
    check(actual == sorted(READMES), f'language file set mismatch: {actual}')
    texts = {name: (ROOT / name).read_text() for name in READMES if (ROOT / name).exists()}
    check(len(texts) == 11, 'all 11 README files must exist')
    if len(texts) != 11:
        return finish()

    expected_sources = None
    expected_prompts = None
    expected_images = None
    english_cases = None
    for name, text in texts.items():
        cases = CASE_RE.findall(text)
        sources = [case[2] for case in cases]
        prompts = PROMPT_RE.findall(text)
        all_images = [url for url in IMAGE_RE.findall(text) if '/seedance_2_prompt_images/' in url]
        images = all_images[1:]  # the first matching image is the first-screen banner
        anchors = re.findall(r'<a id="([a-z0-9-]+-case-\d+)"></a>', text)
        menu_links = re.findall(r'^  - \[Case \d+: .*?\]\(#([a-z0-9-]+-case-\d+)\)$', text, re.M)

        check(len(cases) == 155, f'{name}: expected 155 cases, got {len(cases)}')
        check(len(set(sources)) == 155, f'{name}: sources are not unique')
        check(len(prompts) == 155, f'{name}: expected 155 prompt blocks, got {len(prompts)}')
        check(len(images) == 155, f'{name}: expected 155 case images, got {len(images)}')
        check(all(url.startswith(R2_PREFIX) for url in images), f'{name}: non-R2 case media found')
        check(len(anchors) == 155 and anchors == menu_links, f'{name}: Menu/case anchor mismatch')
        check('| Output |\n| :----: |\n\n**Prompt:**' not in text, f'{name}: empty output table found')
        check('Seedance 2.5' not in text and 'awesome-seedance-2.5-prompts' not in text, f'{name}: Seedance 2.5 drift found')
        check('CC BY 4.0' not in text and 'final open-source license file has not been added' not in text, f'{name}: license drift found')
        check('./public/seedance_2_prompt_images/' not in text, f'{name}: local public media reference found')
        check(not re.search(r'\b(?:TODO|TBD)\b|translation pending|translate to|\{\{[^}]+\}\}', text, re.I), f'{name}: unresolved placeholder found')
        if name != 'README.md':
            check(') or [' not in text, f'{name}: English Quick Start connector leaked into localized copy')
        check(text.find('<img src=') < text.find('## 🍌'), f'{name}: banner must be before Introduction')
        check(text.rstrip().endswith('&Date)'), f'{name}: Star History must be the final element')
        check(text.rfind('## 🙏') > text.rfind('### Case '), f'{name}: Acknowledge must follow all cases')
        for anchor in ['introduction','quick-start','statistics','how-to-use','menu','related-repositories','contributing','license','copyright-notice','acknowledge']:
            check(f'<a id="{anchor}"></a>' in text, f'{name}: missing section anchor {anchor}')

        if expected_sources is None:
            expected_sources, expected_prompts, expected_images = sources, prompts, images
            english_cases = cases
        else:
            check(sources == expected_sources, f'{name}: source order differs from English')
            check(prompts == expected_prompts, f'{name}: prompt blocks differ from English')
            check(images == expected_images, f'{name}: media order differs from English')

        for url in HTTP_RE.findall(text):
            parsed = urlparse(url.rstrip('.,;'))
            if parsed.netloc not in {'evolink.ai', 'docs.evolink.ai'}:
                continue
            query = parse_qs(parsed.query)
            check(query.get('utm_source') == ['github'], f'{name}: missing utm_source on {url}')
            check(query.get('utm_campaign') == [CAMPAIGN], f'{name}: wrong utm_campaign on {url}')
            check(bool(query.get('utm_medium')) and bool(query.get('utm_content')), f'{name}: incomplete slot UTM on {url}')

    data = json.loads((ROOT / 'data/ingested_sources.json').read_text())
    rows = data.get('cases', [])
    check(data.get('case_count') == 155 and len(rows) == 155, 'source index case count must be 155')
    check([row['source_url'] for row in rows] == expected_sources, 'source index order differs from README.md')
    check([row['preview_url'] for row in rows] == expected_images, 'source index media differs from README.md')
    check([row['title'] for row in rows] == [case[1] for case in english_cases], 'source index titles differ from README.md')
    check([row['author_handle'] for row in rows] == [case[3] for case in english_cases], 'source index author handles differ from README.md')
    check([row['author_url'] for row in rows] == [case[4] for case in english_cases], 'source index author URLs differ from README.md')
    check([row['prompt_sha256'] for row in rows] == [hashlib.sha256(prompt.encode()).hexdigest() for prompt in expected_prompts], 'source index prompt hashes differ from README.md')
    check(sum(item['count'] for item in data.get('categories', [])) == 155, 'category counts do not sum to 155')

    required = [
        'LICENSE', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md', 'SECURITY.md',
        'docs/maintenance.md', 'docs/update-log.md', '.github/PULL_REQUEST_TEMPLATE.md',
        '.github/ISSUE_TEMPLATE/prompt-proposal.yml', '.github/ISSUE_TEMPLATE/problem-report.yml',
    ]
    for rel in required:
        check((ROOT / rel).is_file(), f'missing required file: {rel}')
    return finish()

def finish() -> int:
    if errors:
        print('Repository verification: FAIL')
        for error in errors:
            print(f'- {error}')
        return 1
    print('Repository verification: PASS')
    print('- README files: 11')
    print('- Unique cases/sources/prompts/media per README: 155')
    print('- Model identity: Seedance 2.0')
    print('- Media policy: R2-hosted')
    print('- Source/data equality: PASS')
    return 0

if __name__ == '__main__':
    sys.exit(main())
