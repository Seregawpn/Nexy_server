# Quit Owner + Fallback Timeout Parity

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
- В quit path был дублирующий writer `USER_QUIT_INTENT` (tray integration + coordinator).
- Anti-stale timeout policy была только в Quartz path; fallback `KeyboardMonitor` отставал и мог расходиться по поведению.

## Root Cause
- Дубли ownership повышал риск конфликтов порядка событий.
- Расходящиеся guard-политики между backend увеличивали вероятность непредсказуемых input-симптомов.

## Optimal Fix
- Централизация quit-intent owner:
  - `TrayControllerIntegration` теперь только публикует `tray.quit_clicked`;
  - `USER_QUIT_INTENT` остается owner-логикой coordinator.
- Добавлен runtime stale-timeout reconcile в fallback `KeyboardMonitor`:
  - combo timeout reset;
  - single-key timeout release;
  - partial combo stale-state cleanup.
- Приведена parity с Quartz timeout healing.

## Verification
- `pytest -q tests/test_quartz_stale_state_timeout.py tests/test_keyboard_monitor_stale_timeout.py tests/test_quartz_voiceover_passthrough.py tests/test_tray_quit_dispatch.py tests/test_user_quit_ack.py`
- Результат: `13 passed`.

## Запрос/цель
- Убрать дубли/конфликты/гонки и централизовать ownership в quit/input path.

## Контекст
- Файлы:
  - `integration/integrations/tray_controller_integration.py`
  - `modules/input_processing/keyboard/keyboard_monitor.py`
  - `tests/test_keyboard_monitor_stale_timeout.py`

## Решения/выводы
- Quit owner теперь единый (coordinator).
- Input stale-timeout поведение выровнено между Quartz и fallback backend.

## Открытые вопросы
- Нужен ручной прогон в среде пользователя (VoiceOver + Safari/YouTube + Spotlight) для финального подтверждения UX.

## Следующие шаги
- Выполнить ручной сценарий и проверить отсутствие “оживления через Cmd+Tab”.
