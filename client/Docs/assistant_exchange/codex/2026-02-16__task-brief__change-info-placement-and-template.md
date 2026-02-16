# Task Brief: clarify where to place change-information block

## Request
Clarify exact file/section where assistants must add change information; remove ambiguity.

## Implemented

1. Explicit placement in client assistant rules
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/AGENTS.md`.
- Added rule: block `Информация об изменениях` must be placed immediately after `## Verification`.

2. Explicit placement in Codex/Antigravity prompts
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/Docs/CODEX_PROMPT.md`.
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/Docs/ANTIGRAVITY_PROMPT.md`.
- Added same placement rule for both assistants.

3. Shared report template updated
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/Docs/assistant_exchange/TEMPLATE.md`.
- Added dedicated section `## Информация об изменениях` after `## Verification`.

4. Governance journal updated
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/LATEST_CHANGES.md`.

## Validation
- Verified all updated files now explicitly define both required content and exact section placement.

## Outcome
Rule is now unambiguous: assistants must write change information in a dedicated section immediately after `## Verification` in every report.
