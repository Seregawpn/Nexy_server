# Direct State Access Scan

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-01-11
- ID (INS-###): INS-005

## Diagnosis
Обнаружены прямые вызовы `state_manager.get_*` в интеграциях, что нарушает REQ-003/004 (решения должны идти через selectors/gateways).

## Root Cause
Часть интеграций не мигрирована на selectors/gateways → обход центра управления → риск дублирования/конфликтов решений.

## Optimal Fix
Мигрировать прямые чтения состояния в selectors/gateways и использовать snapshot/decide_* в интеграциях.

## Verification
Проверить `scripts/verify_no_direct_state_access.py` и убедиться, что direct state access отсутствует.

## Запрос/цель
Проверить, есть ли ещё критические места для централизации.

## Контекст
- Файлы: integration/integrations/mode_management_integration.py, integration/integrations/updater_integration.py, integration/integrations/interrupt_management_integration.py, integration/integrations/tray_controller_integration.py
- Документы: Docs/PROJECT_REQUIREMENTS.md

## Решения/выводы
- Итоговый статус: ЧАСТИЧНОЕ
- Требуется миграция прямых state reads на selectors/gateways.

## Найденные проблемы (если review)
- Высокий риск: прямой доступ к state_manager в mode_management_integration, updater_integration, tray_controller_integration (нарушение REQ-003/004).

## Открытые вопросы
- Какие интеграции уже планируется переводить на selectors/gateways в рамках текущего релиза?

## Следующие шаги
- Согласовать список интеграций для миграции в этом релизе.
- Пройтись по get_current_mode/get_current_session_id и заменить на selectors/gateways.
