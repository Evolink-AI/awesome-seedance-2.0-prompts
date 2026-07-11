#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = {
    "README_es.md": ("es", "Caso", "por", "Resultado", "Prompt"),
    "README_pt.md": ("pt", "Caso", "por", "Resultado", "Prompt"),
    "README_ja.md": ("ja", "ケース", "投稿者", "出力", "プロンプト"),
    "README_ko.md": ("ko", "사례", "작성자", "결과", "프롬프트"),
    "README_de.md": ("de", "Fall", "von", "Ausgabe", "Prompt"),
    "README_fr.md": ("fr", "Cas", "par", "Résultat", "Prompt"),
    "README_tr.md": ("tr", "Örnek", "yazan", "Çıktı", "İstem"),
    "README_zh-TW.md": ("zh-TW", "案例", "作者", "輸出", "提示詞"),
    "README_zh-CN.md": ("zh-CN", "案例", "作者", "输出", "提示词"),
    "README_ru.md": ("ru", "Пример", "автор", "Результат", "Промпт"),
}
CASE_RE = re.compile(
    r'<a id="(?P<id>[a-z0-9-]+-case-\d+)"></a>\n(?:<!--[^\n]*-->\n)?'
    r'### (?P<case_label>[^:\n]*?)\s+(?P<number>\d+): \[(?P<title>.*?)\]\((?P<source>https?://[^)]+)\) '
    r'\((?P<by_label>[^()\n]*?) \[@(?P<handle>[^]]+)\]\((?P<author>https?://[^)]+)\)\)', re.M,
)
MENU_RE = re.compile(r'^  - \[(?P<label>.*?)\]\(#(?P<id>[a-z0-9-]+-case-\d+)\)$', re.M)
CODE_RE = re.compile(r'^```[^\n]*\n(.*?)\n```$', re.M | re.S)


def cases(path: Path) -> list[dict[str, str]]:
    return [match.groupdict() for match in CASE_RE.finditer(path.read_text(encoding="utf-8"))]


def load_titles(locale: str) -> list[tuple[str, str]]:
    rows = []
    for line in (ROOT / f"data/localized-titles/{locale}.tsv").read_text(encoding="utf-8").splitlines():
        parts = line.split("\t", 1)
        if len(parts) != 2 or not all(parts):
            raise ValueError(f"{locale}: malformed localized title row")
        rows.append((parts[0], parts[1]))
    return rows


def main() -> int:
    errors: list[str] = []
    english_text = (ROOT / "README.md").read_text(encoding="utf-8")
    english = cases(ROOT / "README.md")
    english_by_id = {case["id"]: case for case in english}
    english_codes = CODE_RE.findall(english_text)
    sequences: list[tuple[str, ...]] = []

    if len(english) != 155 or len(english_codes) != 155:
        errors.append("README.md must contain 155 parseable cases and prompt blocks")

    for filename, (locale, case_label, by_label, output_label, prompt_label) in CONFIG.items():
        path = ROOT / filename
        text = path.read_text(encoding="utf-8")
        localized = cases(path)
        localized_by_id = {case["id"]: case for case in localized}
        menu = {match.group("id"): match.group("label") for match in MENU_RE.finditer(text)}
        title_rows = load_titles(locale)
        expected_titles = dict(title_rows)
        expected_ids = list(english_by_id)
        if [row[0] for row in title_rows] != expected_ids:
            errors.append(f"{locale}: title map ids/order differ from English")
        if list(localized_by_id) != expected_ids:
            errors.append(f"{filename}: case ids/order differ from English")
        if CODE_RE.findall(text) != english_codes:
            errors.append(f"{filename}: prompt blocks differ from English")
        if text.count(f"| {output_label} |") != 155 or text.count(f"**{prompt_label}:**") != 155:
            errors.append(f"{filename}: localized Output/Prompt labels are incomplete")
        for case_id, source in english_by_id.items():
            item = localized_by_id.get(case_id)
            if not item:
                continue
            expected_title = expected_titles[case_id]
            if item["title"] != expected_title:
                errors.append(f"{filename}: {case_id} title differs from reviewed mapping")
            if item["title"] == source["title"]:
                errors.append(f"{filename}: {case_id} remains unchanged English")
            if item["case_label"] != case_label or item["by_label"] != by_label:
                errors.append(f"{filename}: {case_id} fixed labels are not localized")
            for key in ("number", "source", "handle", "author"):
                if item[key] != source[key]:
                    errors.append(f"{filename}: {case_id} immutable {key} differs from English")
            menu_label = menu.get(case_id, "")
            if not menu_label.startswith(f"{case_label} {item['number']}:") or expected_title not in menu_label:
                errors.append(f"{filename}: {case_id} Menu title differs from heading")
        sequences.append(tuple(item["title"] for item in localized))

    if len(set(sequences)) != len(CONFIG):
        errors.append("localized title sequences must be locale-specific")

    if errors:
        print("Localization verification: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Localization verification: PASS")
    print("- Locales: 10")
    print("- Reviewed titles: 155 per locale")
    print("- Unchanged English titles: 0")
    print("- Prompt blocks and immutable metadata: byte-identical")
    return 0


if __name__ == "__main__":
    sys.exit(main())
