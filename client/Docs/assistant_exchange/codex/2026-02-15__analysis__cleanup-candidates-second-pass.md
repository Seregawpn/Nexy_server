# Analysis: Cleanup Candidates (Second Pass)

Дата: 2026-02-15

## Контекст
Проведён второй проход поиска файлов/документов с низким/нулевым usage в активном контуре (без `Docs/assistant_exchange`, `Docs/_archive`, `_Docs_ARCHIVED`, `build_logs`).

## Findings

### A) Документы в `Docs/` с нулевыми активными ссылками
- `Docs/HOTKEY_COMBINATION_REQUIREMENTS.md`
- `Docs/HOTKEY_CONFLICT_GUARD_IMPLEMENTATION_PLAN.md`

Рекомендация: перенести в `Docs/_archive/` или явно добавить в `Docs/README.md` + `Docs/DOCUMENTATION_MAP.md` как active.

### B) Root-файлы с нулевыми ссылками (кандидаты на архив)
- `REFACTORING_STATUS.md`
- `voiceover.md`
- `run_diagnostics.py`
- `check_version.py`
- `test_first_run_centralization.py`
- `verify_path_resolution.py`

Рекомендация: перенос в `Docs/_archive/`/`scripts/_legacy/` с пометкой legacy, затем удаление после 1 релизного цикла.

### C) Скрипты в `scripts/` с 0 ссылок (НЕ удалять автоматически)
Есть несколько `scripts/*` с 0 ссылками в docs/ci, но они могут использоваться вручную (ops/dev). Среди них: `release_build.sh`, `reset_permissions.sh`, `set_version.py`, часть debug/manual whatsapp и audio-скриптов.

Рекомендация: не удалять по метрике ссылок; сначала owner-review + telemetry фактического использования.

### D) Тесты с 0 ссылок (НЕ считать orphan)
Многие `tests/test_*.py` имеют 0 прямых ссылок, но используются через pytest discovery.

Рекомендация: не удалять по критерию ссылок; удаление только при подтверждённом dead-scope.

### E) Process conflicts
- CI/.cursorrules ранее ссылались на missing scripts; в первом cleanup-pass добавлены:
  - `scripts/generate_requirements_coverage.py`
  - `scripts/monitor_metrics.py`
  - `scripts/verify_docs_root_server_links.py`
- Gate проверен: blocking=0.

## Suggested Next Cleanup Batch (low-risk)
1. Архивировать:
   - `Docs/HOTKEY_COMBINATION_REQUIREMENTS.md`
   - `Docs/HOTKEY_CONFLICT_GUARD_IMPLEMENTATION_PLAN.md`
2. Переместить в legacy-папку:
   - `run_diagnostics.py`
   - `check_version.py`
   - `verify_path_resolution.py`
3. Переместить в doc-archive:
   - `REFACTORING_STATUS.md`
   - `voiceover.md`

## Verification for next batch
- `./.venv/bin/python scripts/verify_doc_links.py`
- `REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh`
- grep-check отсутствия ссылок на перемещённые файлы в `Docs/README.md`, `Docs/DOCUMENTATION_MAP.md`, `.cursorrules`, `.github/workflows/ci.yml`.

