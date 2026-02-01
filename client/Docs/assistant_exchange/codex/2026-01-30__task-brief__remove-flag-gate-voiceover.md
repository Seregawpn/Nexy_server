# Remove Flag Gate From VoiceOver Ducking

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-30
- ID (INS-###): N/A

## Diagnosis
VoiceOverDuckingIntegration читала `permissions_first_run_completed.flag`, создавая второй SoT и риск рассинхрона с ledger/state_manager.

## Root Cause
Локальный флаг‑гейт вместо централизованных selectors/state_manager.

## Optimal Fix
Заменить проверку флага на snapshot из selectors (first_run) и ждать `permissions.first_run_completed`.

## Verification
- При fresh ledger (first_run=true) интеграция отложена до `permissions.first_run_completed`.
- При completed ledger — инициализация без ожидания.

## Запрос/цель
Убрать флаг‑гейт, чтобы first-run логика была централизована.

## Контекст
- Файлы: `integration/integrations/voiceover_ducking_integration.py`
- Документы: `Docs/PROJECT_REQUIREMENTS.md` (REQ-010)
- Ограничения: без новых флагов

## Решения/выводы
- Удалено чтение файлового флага, использован selectors snapshot.

## Открытые вопросы
- Нужны ли ещё интеграции с флаг‑гейтами для зачистки?

## Следующие шаги
- При необходимости заменить остальные флаг‑чтения на selectors.
