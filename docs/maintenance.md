# Maintenance Guide

## Source of truth

- `README.md` is the English structural source.
- `data/ingested_sources.json` is the accepted 155-case source, author, preview, category, and prompt-hash inventory.
- `data/localized-titles/<locale>.tsv` is the reviewed case-title source for each of the ten localized READMEs.
- The ten localized READMEs must keep the same source order, prompt blocks, case anchors, and R2 media order as English.
- Prompt blocks preserve source wording and are never translated or invented.
- Visible case/Menu titles and fixed labels are translated for each locale; a structure/count/media check is not semantic localization evidence.

## Case format

Each public case must include:

- one stable category-local anchor such as `action-fantasy-case-1`
- a linked `### Case N` heading with source and author URLs
- one R2-hosted preview frame linked to the Seedance 2.0 prompt workspace
- one fenced prompt block copied from the accepted source boundary

Duplicate source URLs are not allowed. Numbering is contiguous inside each category.

## Update checklist

1. Confirm the candidate has a public source, author, usable prompt boundary, category, and preview evidence.
2. Add the candidate to English first and update `data/ingested_sources.json`.
3. Update all localized READMEs without translating prompt blocks, URLs, handles, model IDs, or UTM values.
4. Update every reviewed locale title map, then rebuild localized headings, Menu titles, fixed labels, counts, and stable anchors.
5. Upload the complete public media batch to the `github-repo-media` R2 namespace.
6. Run the semantic localization gate, live-star Star History gate, repository verifier, public link audit, and rendered GitHub media audit.
7. Commit and push only when all P0/P1 findings are closed.

## Star History visibility

- Read the live GitHub `stargazers_count` during verification.
- Below 10 stars, all README variants omit Star History.
- At 10 or more stars, all README variants place the chart after Acknowledge as the final public element.
- A failed live count read blocks verification instead of guessing.

## Validation commands

```bash
python3 tools/verify_repo.py
python3 tools/verify_localization.py
python3 tools/verify_star_history.py
git diff --check
find . \( -name .DS_Store -o -name __pycache__ -o -name '*.pyc' \) -print
```

The CI workflow runs the same repository verifier on every pull request and push to `main`.

## Related-repository boundary

This repository owns prompt discovery and reuse. The adjacent Seedance 2.0 API/skill repository owns executable API and installation surfaces; changes to that repository must be audited and released through the Skill + API pipeline rather than from this content repository.
