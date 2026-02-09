# WhatsApp QR Guard & Status Alignment

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-01
- ID (INS-###): N/A (CRM_INSTRUCTION_REGISTRY.md not found)

## Diagnosis
WhatsApp отправка запускалась без валидной сессии, а статус `authenticated` не совпадал с enum → система видела `DISCONNECTED` и не могла корректно маршрутизировать действия.

## Root Cause
Несогласованные значения `whatsapp.status` + отсутствие guard перед отправкой при `qr_required/disconnected`.

## Optimal Fix
- Привести статус к `connected`.
- Добавить guard в `whatsapp.request` через gateway.
- Расширить правила interaction_matrix для `disconnected/connecting`.

## Verification
- Логи: `whatsapp.status=connected` после авторизации.
- `actions.send_whatsapp_message.completed` при connected.
- При `qr_required` запросы блокируются с TTS-инструкцией.

## Запрос/цель
Сделать поведение WhatsApp предсказуемым: отправка только при доступе, иначе QR-инструкция.

## Контекст
- Файлы: `client/integration/integrations/whatsapp_integration.py`, `client/config/interaction_matrix.yaml`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`

## Решения/выводы
- Статус выровнен на `connected`.
- Guard реализован через gateway с `Decision.NOTIFY_USER`.

## Открытые вопросы
- Нужна ли явная метрика для частоты QR‑блокировок?

## Следующие шаги
- Запустить ручной QR‑логин и проверить отправку.
