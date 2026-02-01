# First-Run Duplication Risks

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-30
- ID (INS-###): N/A

## Diagnosis
Есть остаточные дубликаты источника истины first-run (ledger vs flag) и локальные проверки флага в интеграциях, что может создавать рассинхрон.

## Root Cause
Флаг `permissions_first_run_completed.flag` используется как локальный gate в отдельных интеграциях → второй SoT → риск расхождений с ledger/state_manager.

## Optimal Fix
Убрать чтение флага из интеграций и использовать централизованные selectors/state_manager (или ledger-статус), флаг оставить только как кэш.

## Verification
- Первичный запуск с пустым ledger вызывает wizard.
- Повторный запуск при completed ledger не вызывает wizard, и все интеграции стартуют без ожидания флага.

## Запрос/цель
Оценить дубли/конфликты/гонки в логике first-run.

## Контекст
- Файлы: `integration/integrations/voiceover_ducking_integration.py`, `integration/core/simple_module_coordinator.py`, `integration/integrations/first_run_permissions_integration.py`
- Документы: `Docs/PROJECT_REQUIREMENTS.md` (REQ-010)

## Решения/выводы
- Основной риск — локальные проверки флага в отдельных интеграциях (например VoiceOver) → второй SoT.
- Событийная синхронизация first_run через event bus уже есть; её нужно использовать везде.

## Открытые вопросы
- Можно ли заменить flag‑gate в VoiceOverDucking на selector/state_manager без изменения поведения?

## Следующие шаги
- Согласовать замену flag‑gate на selector в интеграциях.
