# WhatsApp Activation On Demand

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-05
- ID (INS-###): N/A

## Diagnosis
WhatsApp автозапускается при старте, а требование — активация только при запросе пользователя или упоминании WhatsApp в ответе ассистента.

## Root Cause
`whatsapp.auto_start=true` + логика `_do_start` инициирует сервис без запроса.

## Optimal Fix
Отключить автозапуск, добавить триггер на `grpc.response.text` с ключевыми словами и запускать сервис только при `whatsapp.status=disconnected`.

## Verification
Без запросов/ответов про WhatsApp сервис не стартует. При `read/send` или ответе с “WhatsApp” — запускается и показывает QR.

## Запрос/цель
Активировать WhatsApp только по запросу пользователя или ответу ассистента про WhatsApp.

## Контекст
- Файлы: `client/integration/integrations/whatsapp_integration.py`, `client/config/unified_config.yaml`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`
- Ограничения: без новых источников истины

## Решения/выводы
- Добавлен триггер на `grpc.response.text` с ключевыми словами.
- Автозапуск отключён.

## Открытые вопросы
- Нужен ли более строгий детектор (intent/command payload) вместо ключевых слов?

## Следующие шаги
- Прогнать ручную проверку через реальный запрос/ответ.
