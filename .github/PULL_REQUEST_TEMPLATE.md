## Summary

Describe the user-facing change and why it belongs in this Seedance 2.0 prompt library.

## Case metadata

- [ ] Public source URL and author URL are present.
- [ ] Prompt boundary is copied from the source and contains no invented text.
- [ ] Category and category-local case number are correct.
- [ ] `data/ingested_sources.json` matches README order and metadata.

## Localization

- [ ] All 11 README files have the same case/source order.
- [ ] Prompt blocks, source URLs, handles, model IDs, commands, and UTM values are unchanged.
- [ ] Every case/Menu title matches its reviewed `data/localized-titles/<locale>.tsv` mapping.
- [ ] Case/author/output/prompt labels and visible framing copy are localized without TODO placeholders.
- [ ] The semantic localization gate reports zero unexplained unchanged English titles.

## Media and R2

- [ ] Preview media is in the locked `github-repo-media` R2 namespace.
- [ ] Every README uses the same R2 media URL for the case.
- [ ] GitHub rendered/camo media was checked when the change is published.

## Validation

- [ ] `python3 tools/verify_repo.py`
- [ ] `python3 tools/verify_localization.py`
- [ ] `python3 tools/verify_star_history.py` records the live star count and enforces the 10-star threshold.
- [ ] `git diff --check`
- [ ] Public links, relative links, and anchors were audited.

## Related-repository boundary

- [ ] This PR changes prompt/discovery content only; API/skill release changes are routed to the separate Skill + API pipeline.
