# Task Brief: Root architecture governance gates

- Author: codex
- Date: 2026-02-15
- Scope: only root-level files (no edits in `client/` or `server/`).

## Goal
Внедрить единые архитектурные гейты против дублей/конфликтов/гонок/децентрализации на уровне root правил.

## Changes
1. Updated `AGENTS.md`
- Added section `## 9) Архитектурные гейты (обязательно)`.
- Added 4 mandatory gates:
  - Single Owner Gate
  - Zero Duplication Gate
  - Anti-Race Gate
  - Flag Lifecycle Gate
- Added canonical reference to `Docs/ARCHITECTURE_GOVERNANCE.md`.

2. Added new canonical root document
- `Docs/ARCHITECTURE_GOVERNANCE.md`
- Contains formal policy for:
  - single owner
  - duplication control
  - race guards
  - flag lifecycle
  - legacy path removal policy
  - architecture DoD

3. Updated prompt rules
- `Docs/CODEX_PROMPT.md`: added section `## 10) Architecture Governance (обязательно)`.
- `Docs/ANTIGRAVITY_PROMPT.md`: added section `## 10) Architecture Governance (обязательно)`.

4. Updated root architecture index
- `Docs/ARCHITECTURE_OVERVIEW.md`: linked governance canon in root-level rules.

## Validation
- All updated files exist and include `ARCHITECTURE_GOVERNANCE` references.
- Scope respected: no edits inside `client/` or `server/`.
