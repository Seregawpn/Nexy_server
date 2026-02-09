# WhatsApp No-Access Investigation

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-01
- ID (INS-###): N/A (CRM_INSTRUCTION_REGISTRY.md not found)

## Diagnosis
WhatsApp отправка не работает из‑за отсутствия авторизации (QR не просканирован) и несогласованного статуса `whatsapp.status` ("authenticated" не входит в enum), что ломает централизованную логику статуса.

## Root Cause
WhatsApp MCP сервис стартует, но остаётся в состоянии QR/не залогинен → Node возвращает ошибки → клиент сообщает «нет доступа». Дополнительно: `WhatsappIntegration` пишет `authenticated`, а selectors ожидают `connected`, поэтому состояние падает в `DISCONNECTED`.

## Optimal Fix
Привести значение состояния к `connected` и перед отправкой использовать gateway‑guard по `whatsapp.status` (block/notify при qr_required/disconnected).

## Verification
1) `wa-logs.txt`: нет повторяющихся “not logged in/QR Code Received” после скана.
2) Логи клиента: `whatsapp.status=connected`, `actions.send_whatsapp_message.completed`.

## Запрос/цель
Понять источник сообщения «нет доступа» при отправке WhatsApp и предложить архитектурно корректный фикс.

## Контекст
- Файлы: `client/integration/integrations/whatsapp_integration.py`, `client/integration/core/selectors.py`, `client/modules/whatsapp/service_manager.py`, `wa-logs.txt`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`

## Решения/выводы
- В `wa-logs.txt` видны `not logged in` и QR‑циклы → сервис не авторизован.
- Несоответствие статуса `authenticated` ↔ enum `connected` сбрасывает состояние в `DISCONNECTED`.

## Открытые вопросы
- Есть ли `logs/nexy.log` с `actions.send_whatsapp_message` vs `send_message` на момент ошибки?
- Показывался ли QR экран пользователю (или блокирован)?

## Следующие шаги
- Применить фиксы статуса и guard в WhatsAppIntegration.
- Проверить, что QR сканируется и статус переходит в `connected`.
