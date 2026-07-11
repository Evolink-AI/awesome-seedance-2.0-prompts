# Repository Audit Report

## Audit identity

- Repository: `Evolink-AI/awesome-seedance-2.0-prompts`
- Baseline commit: `7c0eb05`
- Audit date: 2026-07-11
- Pipeline: `guide-prompt`
- Shape: `prompt`
- Run mode: `recurring-update`
- Contract: `model-repo-pipeline/contracts/standard-guide-repo-contract.md`
- Child reviews: `github-template`, `prompt-repo-update`, and `github-repo-review`
- Baseline verdict: **FAIL — do not push**

## Executive verdict

The repository has a valuable 163-entry source-attributed prompt corpus, but its public front door and multilingual media surface are not release-safe. The repository identity is Seedance 2.0, while the current first screen, CTA destinations, and UTM campaign advertise Seedance 2.5. Ten localized READMEs contain 163 empty media tables each. Eight source URLs are duplicated, which explains the difference between 163 displayed cases and 155 unique preview assets.

The narrow prompt update verifier returned PASS because it checked counts and missing local paths but did not detect empty localized media tables, incorrect model routing, license contradictions, R2 policy, or community-standard gaps. Under the full contract, the repository remains blocked until every P0/P1 below is closed or explicitly waived.

## Baseline evidence

| Check | Result |
|---|---|
| Remote identity | `origin` resolves to `Evolink-AI/awesome-seedance-2.0-prompts` |
| Public metadata | Public, default branch `main`, homepage `https://evolink.ai/seedance-2-0-prompts` |
| README policy | Exactly 11 required README files; no `README_en.md` |
| Case inventory | 163 displayed cases and prompt blocks in every README |
| Unique source inventory | 155 unique source URLs; 8 duplicate source URLs |
| Preview inventory | 155 local JPG files |
| English media | 163 preview references, all local |
| Localized media | 0 preview references in each of 10 localized READMEs; empty output tables remain |
| Existing CI | No GitHub Actions workflows |
| Community files | `CONTRIBUTING.md` and `LICENSE` only |
| Narrow child verifier | PASS, but insufficient for contract acceptance |

## P0 blockers

| ID | Finding | Evidence | Required fix |
|---|---|---|---|
| P0-1 | Repository/model identity mismatch | Repository name, About, topics, and homepage say Seedance 2.0; README first screen repeatedly says Seedance 2.5 and links to `/launch/seedance-2-5`. | Restore Seedance 2.0 positioning and canonical URL across all 11 READMEs. |
| P0-2 | Wrong UTM campaign and incomplete slot attribution | README uses `awesome-seedance-2.5-prompts` and omits required `utm_content` on multiple slots. | Use `awesome-seedance-2.0-prompts` and placement-specific medium/content values. |
| P0-3 | Localized media is absent | Each localized README has 163 output tables but zero image references. | Synchronize the exact source/media mapping from English into all localized case blocks. |
| P0-4 | No first-screen banner | The centered top block starts with badges; no banner image appears in the first 120 lines. | Add a linked, owner-controlled Seedance 2.0 preview banner with accurate alt text. |
| P0-5 | License is contradictory | Badge says CC BY 4.0; `LICENSE` is Apache-2.0; README says no license exists. | Make badge and README copy match Apache-2.0, or replace the license only with explicit owner direction. |
| P0-6 | Conversion path is not trustworthy | The 2.0 prompt repo labels a 2.5 launch page as its model route and labels adjacent links ambiguously. | Provide action-labeled 2.0 model, API key, docs/API, and skill routes; never substitute 2.5. |
| P0-7 | Full public-surface acceptance evidence is missing | No complete Markdown/HTML/raw/relative/anchor/UTM audit exists. | Run a deduplicated public-surface link audit with P0/P1 severity and zero unresolved blockers. |
| P0-8 | Real API smoke evidence is missing | README documents a real model ID and endpoint, but no credit-consuming request/task evidence is recorded. | Run the contract smoke with an approved credit budget, or obtain an explicit run-scoped waiver. |

## P1 blockers

| ID | Finding | Evidence | Required fix |
|---|---|---|---|
| P1-1 | Media violates current R2 policy | All 155 previews are served from local repository paths. | Upload the complete media directory to the locked `github-repo-media` R2 namespace and rewrite all public README references. |
| P1-2 | Duplicate public cases | Eight source URLs appear twice across categories. | Keep the first justified occurrence, remove later duplicates across all languages, renumber affected category-local sequences, and update counts/menu/data. |
| P1-3 | Menu and heading contract drift | `EvoLink Quick Start`, `Statistics`, `How to Use`, `Contributing`, `License`, and `Copyright Notice` lack required emoji; Quick Start is absent from Menu; Acknowledge is not the last main content section. | Normalize heading hierarchy, required section order, Menu coverage, Related Repositories, and Star History placement. |
| P1-4 | Required maintenance/community surfaces are missing | No `docs/maintenance.md`, update log, PR template, issue templates, `SECURITY.md`, or `CODE_OF_CONDUCT.md`. | Add real contribution, security, conduct, issue, PR, maintenance, and update workflows. |
| P1-5 | No durable source/data equality surface | The source dataset referenced by contributing guidance is absent from the tracked repository. | Create a tracked source index derived from the accepted public inventory and verify README/data equality. |
| P1-6 | Localization is incomplete | 114 of 163 case titles remain byte-identical to English in every locale; Acknowledge, Contributing, License, and Copyright prose remain English. | Localize visible prose while preserving prompt blocks, source URLs, handles, model IDs, commands, and UTM values. |
| P1-7 | No repository-level verifier or CI | The narrow external verifier misses empty media tables and model/UTM/license drift. | Add a repo-owned verifier and GitHub Actions workflow covering identity, language set, sources, cases, media, links, headings, and data equality. |
| P1-8 | Rendered GitHub media evidence is missing | Origin/local file presence does not prove GitHub rendering or camo delivery. | After push, audit rendered README HTML, canonical sources, actual image URLs, status, and content type. |

## Template audit: baseline

| # | Rule | Status | Priority | Note |
|---:|---|---|---|---|
| 1 | Centered cover block | PASS | — | `<div align="center">` exists. |
| 2 | License -> usage -> language badge order | FAIL | P0 | Prompt count badge precedes usage; license label is wrong. |
| 3 | English source is `README.md` | PASS | — | No English duplicate file. |
| 4 | Fixed 11-language order | PASS | — | Required order and filenames exist. |
| 5 | `## <emoji> <Title>` headings | FAIL | P1 | Multiple functional headings have no emoji. |
| 6 | Linked `### Case X` source/author headings | PASS | — | All 163 headings are source-attributed. |
| 7 | Optional type labels | PASS | — | Omission is acceptable. |
| 8 | Media layout | FAIL | P0 | Ten locales render empty output tables. |
| 9 | Source attribution | PASS | — | Source and author are in headings. |
| 10 | English bold labels | PASS | — | Prompt labels are present. |
| 11 | Public prompt fenced blocks | PASS | — | 163 fenced prompt blocks per README. |
| 12 | Variable notes | PARTIAL | P2 | Variable guidance is inconsistent. |
| 13 | Menu covers all sections/cases | FAIL | P0 | Quick Start missing; section order drifts. |
| 14 | Acknowledge at end | FAIL | P1 | Three content sections follow it; no Star History chart. |
| 15 | Clear Evolink use entry | FAIL | P0 | Entry exists but targets the wrong model/campaign. |

- Baseline template score: 8 PASS / 6 FAIL / 1 PARTIAL.
- Baseline template verdict: **FAIL**.

## General GitHub review: baseline

- Positioning: FAIL because the README contradicts the repository's canonical 2.0 identity.
- About: PASS for current description, homepage, topics, visibility, and default branch.
- README front door: FAIL because the next action routes to the wrong model and lacks a banner.
- GitHub SEO: FAIL because first-screen 2.5 keywords conflict with the 2.0 repository name and topics.
- Structure and maintainability: FAIL because the source index, maintenance docs, full verifier, and CI are absent.
- Community standards: FAIL because security, conduct, issue templates, and PR template are absent.
- Prompt asset quality: PARTIAL because prompts are source-attributed, but duplicate cases and localized empty media damage trust and browsing.
- Adoption value: high after remediation; not recommendable in the baseline state.

## Remediation order

1. Lock the 2.0 identity, canonical URLs, UTM matrix, license, and first-screen conversion path.
2. Deduplicate to the 155 unique-source inventory and rebuild category numbering/menu/counts.
3. Upload all 155 preview assets to the locked R2 namespace and synchronize media blocks across 11 READMEs.
4. Normalize required README sections and fully localize visible framing copy.
5. Add source index, maintenance/community files, repo verifier, and CI.
6. Run template, prompt-update, localization, data-equality, media, link, and git hygiene checks until P0/P1 are zero.
7. Run the approved real API smoke or record an explicit waiver.
8. Commit and push only after completion-gate permits publication; then verify raw/rendered README, media/camo, metadata, commit, and remote branch.

## Completion rule

This report remains `FAIL` until its final re-audit section is updated with P0=0, P1=0, required evidence paths, commit hash, push result, remote readback, and the final `published` state.

## Remediation progress

- Closed locally: P0-1 through P0-7 and P1-1 through P1-8.
- Closed: P0-8 real API smoke — task `task-unified-1783761950-eoxo84kb` completed and returned a valid H.264 MP4 result.
- Non-generating credential gate: PASS — `GET /v1/credits` returned HTTP 200; no key, balance, or account data was recorded.
- API smoke media evidence: PASS — 864×496, 24 fps, 4.041667 seconds, `video/mp4`.
- API smoke cost evidence: actual usage was 20.46 credits, 1.94 above the 18.52 estimate derived from a stale related Gateway README. No retry was submitted; the target repository contains no pricing claim.
- Current local verifier: PASS — 11 READMEs, 155 unique sources/cases/prompts/media, Seedance 2.0 identity, R2 hosting, and README/data equality.
- Current public link audit: PASS — P0=0, P1=0, P2=1 transient Star History HTTP 500.
- Current pre-push GitHub render audit: PASS — 156/156 R2 canonical images and 156/156 GitHub camo images.
- Publication state: not pushed, as required by the audit-first contract.

## Final local re-audit

- Verdict: **LOCAL PASS — eligible for commit and push**.
- P0 findings remaining: `0`.
- P1 findings remaining: `0`.
- P2 advisories remaining: `1` transient Star History API HTTP 503 after HEAD, Range GET, and curl fallback; non-blocking under the contract because P0/P1 are zero and the source is third-party visualization only.
- Repository verifier: PASS — 11 READMEs and 155 unique cases/sources/prompts/media per README.
- Rendered media: PASS — 156/156 GitHub-rendered images, 156/156 R2 canonical sources, 156/156 camo sources.
- Real API smoke: PASS — one approved request, one recovered task ID, terminal `completed`, one valid MP4 URL.
- Publication hygiene: PASS — internal `.codex/` evidence is ignored and will not be staged.
- Remaining steps are publication evidence only: precise staging, commit, push, remote commit/readback, live README/media/metadata verification, and CI readback.
