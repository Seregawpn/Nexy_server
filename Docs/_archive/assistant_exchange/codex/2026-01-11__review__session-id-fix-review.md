# Session ID Fix Review

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-01-11
- ID (INS-###): INS-005

## Diagnosis
Внесены полезные изменения (uuid4, selectors, ErrorHandler), но остались нарушения REQ-003/004 и есть риск регрессий из‑за строгой проверки типов и ослабления first_run guard.

## Root Cause
Неполная миграция на selectors + частичная замена логики first_run → обход централизованных правил и неполное покрытие стейтов.

## Optimal Fix
Довести миграцию до полного запрета прямого `state_manager.get_*`, добавить selectors для ptt/first_run_in_progress, смягчить переход к строковому session_id через безопасную нормализацию.

## Verification
Проверить: no direct state access, session_id всегда строка uuid4, first_run guard не сломан.

## Запрос/цель
Проверить корректность изменений в `voice_recognition_integration.py` и `input_processing_integration.py`.

## Контекст
- Файлы: integration/integrations/voice_recognition_integration.py, integration/integrations/input_processing_integration.py, integration/core/selectors.py
- Документы: Docs/PROJECT_REQUIREMENTS.md
- Ограничения: без реархитектуры

## Решения/выводы
- Итоговый статус: ЧАСТИЧНОЕ
- Требуется доработка для полного соответствия REQ-003/004/009

## Найденные проблемы (если review)
- Критично: остались прямые `state_manager.get_state_data()` в интеграциях (ptt_pressed), что нарушает REQ-004. integration/integrations/voice_recognition_integration.py#L571, integration/integrations/voice_recognition_integration.py#L637, integration/integrations/input_processing_integration.py#L169.
- Высокий риск: `_set_session_id` теперь игнорирует non-str session_id. Если какие-либо источники ещё шлют float, сессии перестанут синхронизироваться. integration/integrations/voice_recognition_integration.py#L206, integration/integrations/input_processing_integration.py#L394.
- Средний риск: заменён check `first_run_in_progress` на `is_first_run(snapshot)`, что может пропустить активный first_run при несинхронизированном `first_run_required`. integration/integrations/voice_recognition_integration.py#L233.

## Открытые вопросы
- Есть ли ещё источники session_id, которые не переведены на uuid4 string?

## Следующие шаги
- Добавить selectors `is_first_run_in_progress()` и `is_ptt_pressed()` и заменить прямые `get_state_data`.
- Ввести мягкую нормализацию session_id (строка) на переходный период.
- Проверить сценарий first_run_started до подписки интеграции.
