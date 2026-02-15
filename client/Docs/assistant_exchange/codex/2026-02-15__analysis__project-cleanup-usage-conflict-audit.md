# Analysis: Project Cleanup Usage/Conflict Audit

Дата: 2026-02-15

## Scope
Аудит клиентского репозитория на предмет:
- неиспользуемых файлов,
- конфликтных/рассинхронизированных артефактов,
- тестовых/временных файлов вне канонического контура,
- приоритета безопасной очистки.

## Key Findings

### P0 (конфликты, которые ломают процесс)
1. CI/правила ссылаются на отсутствующие скрипты:
   - `scripts/generate_requirements_coverage.py` (missing)
   - `scripts/monitor_metrics.py` (missing)
   - `scripts/verify_docs_root_server_links.py` (missing в `client/`, fallback на `../scripts`)
   Источники: `.github/workflows/ci.yml`, `.cursorrules`.

2. Runtime/docs конфликт по TTS compatibility path:
   - `integration/integrations/tts_integration.py` существует, но не регистрируется в `IntegrationFactory`.
   - Доки описывают его как активный compatibility ingress (`speech.playback.request`).

### P1 (кандидаты на удаление/архив без влияния на runtime)
1. Файлы без референсов (не участвуют в runtime/CI):
   - `test_messages_real.py`
   - `verify_first_run_centralization.sh`
   - `check_frozen.py`
   - `main_output.txt`
   - `REFACTORING_STATUS.md`
   - `voiceover.md` (как рабочий артефакт; может быть перенесен в `Docs/_archive/`)

2. `modules/_module_template/`:
   - не используется в импортах/координаторе;
   - безопасный кандидат на архив в `Docs/_archive/` как шаблонный артефакт, либо перенос в отдельный `templates/`.

3. Документы в `Docs/` без внешних ссылок в каноническом контуре:
   - `Docs/HOTKEY_COMBINATION_REQUIREMENTS.md`
   - `Docs/HOTKEY_CONFLICT_GUARD_IMPLEMENTATION_PLAN.md`
   Рекомендуется: либо добавить в `Docs/README.md`/`DOCUMENTATION_MAP.md`, либо архивировать.

### P2 (гигиена репозитория)
1. Трекинг generated-отчётов в корне:
   - `metrics_report.json`
   - `requirements_coverage_report.json`
   - `release_suite_report.json`
   Эти файлы генерируются CI/скриптами и лучше хранить как artifacts, а не как постоянные tracked-файлы.

2. Большой объём локальных артефактов (`__pycache__`, `*.pyc`, `build_logs/`, `dist/`) в рабочем дереве.
   `.gitignore` покрывает их, но нужен регулярный cleanup, чтобы не засорять ревью и preflight.

## Used vs Unused (docs)
- Используемые канонические SoT-документы: `Docs/README.md`, `PROJECT_REQUIREMENTS.md`, `ARCHITECTURE_OVERVIEW.md`, `FLOW_INTERACTION_SPEC.md`, `STATE_CATALOG.md`, `PACKAGING_FINAL_GUIDE.md`, `RELEASE_VERSIONING_AND_PUBLISHING.md`, `FEATURE_FLAGS.md`, `first_run_flow_spec.md`.
- Неопределённый статус/вне карты: `Docs/HOTKEY_COMBINATION_REQUIREMENTS.md`, `Docs/HOTKEY_CONFLICT_GUARD_IMPLEMENTATION_PLAN.md`.

## Cleanup Priority
1. P0: закрыть конфликт CI/скриптов и TTS wiring/docs drift.
2. P1: архивировать/удалить явные orphan/manual файлы.
3. P2: нормализовать generated artifacts policy.

## Safe First Deletions (low risk)
- `test_messages_real.py`
- `verify_first_run_centralization.sh`
- `check_frozen.py`
- `main_output.txt`

## Do Not Remove (active)
- `client/VERSION_INFO.json`
- `client/metrics/registry.md`
- `Docs/PACKAGING_FINAL_GUIDE.md` и канонический SoT набор
- `integration/*`, `modules/*` (кроме `_module_template` после подтверждения)

