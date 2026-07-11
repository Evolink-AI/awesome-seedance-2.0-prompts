# Contributing

## Scope

This repository is a curated Seedance 2.0 prompt library. Contributions should improve prompt quality, source attribution, media evidence, localization, or repository consistency.

## What qualifies

Valid entries include direct video-generation prompts, reusable prompt templates, structured prompt formats, and reference-driven prompts whose media tokens are part of the public prompt.

Do not submit commentary, repost captions, marketing copy, unsupported fragments, duplicate source URLs, private material, or generated prompts presented as creator originals.

## Required evidence

Every proposed case needs:

- a public source URL
- an author profile URL
- the exact reusable prompt boundary
- one existing category
- public preview evidence

Keep prompt-internal media references such as `@image1` when they are required. Remove social mentions only when they are surrounding noise rather than prompt logic.

## Repository synchronization

Update English first, then all localized READMEs. Preserve prompt blocks, source/author URLs, handles, model IDs, commands, media URLs, and UTM parameters across languages. Update `data/ingested_sources.json`, Menu links, category counts, and the 155-case badge in the same change.

## Pull request gate

Before opening a pull request, run:

```bash
python3 tools/verify_repo.py
git diff --check
```

Use the pull request checklist to record source metadata, localization, R2 media, validation, and the boundary between this prompt repository and the adjacent API/skill repository.
