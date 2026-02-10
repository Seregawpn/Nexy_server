# Messages Fallback Routing And Open App Check

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-10
- ID (INS-###): N/A

## Diagnosis
При `send_message` recoverable-ошибки контакта маршрутизировались через общий `actions.open_app.failed` путь, что вызывало лишний `interrupt.request` и срыв fallback-подсказки.

## Root Cause
Неверный owner маршрутизации failure-события (`feature_id`-based для app действий) применялся и к messages-командам → неверный event-domain + преждевременная отмена playback.

## Optimal Fix
Цель: сохранить единый owner (`ActionExecutionIntegration`), но разделить terminal/recoverable ошибки в рамках command-domain.

- Добавлен command-aware mapping для failure-событий (`actions.<command>.failed`).
- Для recoverable контактов (`similar_contacts_found`, `ambiguous_contact`) отключен auto-cancel playback.
- Источник cancel/speech теперь привязывается к команде (`actions.send_message`, `actions.open_app`, и т.д.).
- Добавлена классификация ошибок отправки сообщения по номеру/получателю:
  - `invalid_recipient`
  - `send_failed`
  - `timeout`

## Verification
- Тесты: `PYTHONPATH=. pytest -q ../tests/test_action_execution_failure_routing.py` из директории `/Users/sergiyzasorin/Fix_new/client`.
- Результат: `2 passed`.
- Проверено:
  - `send_message` failure публикуется как `actions.send_message.failed` и не шлёт `interrupt.request` при suppress.
  - `open_app` failure сохраняет cancel-path (`interrupt.request`).

## Запрос/цель
Проверить и корректно починить fallback для:
- `open_app` при отсутствии приложения
- `send_message` при несуществующем контакте/некорректном номере

## Контекст
- Файлы:
  - `client/integration/integrations/action_execution_integration.py`
  - `client/modules/messages/send_message.py`
  - `client/modules/action_errors/messages.py`
  - `tests/test_action_execution_failure_routing.py`
- Документы:
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `Docs/_archive/CODEX_PROMPT.md`

## Решения/выводы
- `open_app` fallback уже присутствует (MCP missing → system `open`), исправления были не в fallback-наличии, а в failure-routing.
- Ключевой баг — клиентский orchestration path в `ActionExecutionIntegration`.

## Открытые вопросы
- Нужен ли отдельный UX-текст для `timeout` отправки сообщений (сейчас есть общий template).

## Следующие шаги
- Прогнать ручной сценарий с реальными командами:
  - `send_message` с несуществующим контактом
  - `send_message` с контактом без валидного iMessage recipient
  - `open_app` с заведомо отсутствующим приложением
