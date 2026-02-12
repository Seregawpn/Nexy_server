# Remove AppMode Fallbacks And State Access Centralization

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
В runtime-контуре оставались fallback `AppMode` и точечные прямые `state_manager.get_state_data(...)`, что создавало дубли decision-path.

## Root Cause
Локальные fallback-и и прямой доступ к state в интеграциях обходили централизованный selector-layer.

## Optimal Fix
1. Удалены fallback `AppMode` в:
   - `integration/workflows/base_workflow.py`
   - `integration/core/gateways/permission_gateways.py`
2. Прямой state-read заменён на selector accessors:
   - `integration/integrations/autostart_manager_integration.py`
   - `integration/integrations/updater_integration.py`
   - `integration/integrations/speech_playback_integration.py`

## Verification
- `PYTHONPATH=. pytest -q tests/test_event_ownership_contract.py tests/test_mode_management_mode_request_dedup.py tests/test_gateways.py tests/test_welcome_startup_sequence.py`
- Результат: `23 passed`.

## Запрос/цель
Убрать остаточные дубли/конфликты в управлении режимами и state access, повысить централизацию.

## Контекст
- Файлы:
  - `integration/workflows/base_workflow.py`
  - `integration/core/gateways/permission_gateways.py`
  - `integration/integrations/autostart_manager_integration.py`
  - `integration/integrations/updater_integration.py`
  - `integration/integrations/speech_playback_integration.py`

## Решения/выводы
- Удалён второй источник типа режимов (`AppMode` fallback enum).
- Снижено число прямых state-read в интеграциях в пользу selectors.

## Открытые вопросы
- Нужен отдельный статический тест/линт-правило, запрещающее fallback `AppMode` и прямой `get_state_data` в runtime-интеграциях.

## Следующие шаги
- Добавить contract-тест на «no local AppMode enum fallback» и «no direct state_manager.get_state_data in integrations/*».
