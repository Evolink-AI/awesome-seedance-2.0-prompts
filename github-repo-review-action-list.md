# Repository Remediation Action List

## P0

- [x] Restore Seedance 2.0 identity and canonical conversion URLs across all 11 READMEs.
  - Why: the current README sends 2.0 search traffic to Seedance 2.5.
  - Expected result: repository name, About, first screen, CTA, and UTM campaign all describe the same model.
- [x] Restore all localized case media and add a first-screen banner.
  - Why: ten localized files currently render 163 empty output tables each, and the repository has no banner.
  - Expected result: every case has a visible preview in every language and the first screen immediately communicates the repository purpose.
- [x] Reconcile the Apache-2.0 license across badge, file, and README copy.
  - Why: contradictory licensing damages trust and reuse clarity.
  - Expected result: one consistent license statement everywhere.
- [x] Complete the real API smoke gate; task `task-unified-1783761950-eoxo84kb` reached `completed` and returned a valid MP4 result.
  - Why: the full contract does not permit publication on static README claims alone.
  - Expected result: all conversion links are current, attributable, accessible, and runtime-backed or explicitly waived.

## P1

- [x] Deduplicate eight repeated source URLs and rebuild the accepted inventory to 155 unique cases.
  - Why: duplicated sources inflate the badge and corpus size.
  - Expected result: case count, menu count, source count, data count, and unique preview count all equal 155.
- [x] Upload all 155 previews to the locked R2 namespace and rewrite public README references.
  - Why: current contract requires R2-hosted public media plus rendered GitHub verification.
  - Expected result: every public preview resolves from R2 and renders through GitHub/camo.
- [x] Normalize README section order, headings, Menu, Related Repositories, Acknowledge, and Star History.
  - Why: current structure fails template navigation and final-section rules.
  - Expected result: all 11 READMEs share the same contract-compliant section sequence.
- [x] Add tracked source index, maintenance/update docs, security/conduct files, issue/PR templates, verifier, and CI.
  - Why: the repository lacks durable maintenance and review controls.
  - Expected result: future changes can be validated in a fresh clone without ignored local artifacts.
- [x] Complete localized visible prose while preserving prompts and technical literals.
  - Why: localized pages currently retain substantial English framing copy.
  - Expected result: all reader-facing prose is localized and all prompt/source/media invariants stay identical.

## P2

- [ ] Standardize variable guidance with GitHub admonitions where placeholders need explanation.
  - Why: prompt reuse is safer when editable tokens are explicit.
  - Expected result: variable-heavy prompts are easier to adapt without changing prompt meaning.
