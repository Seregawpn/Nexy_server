# Welcome gRPC Refresh (Deferred Injection)

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-05
- ID (INS-###): INS-005

## Diagnosis
Welcome использует локальный fallback, потому что gRPC клиент не инжектится в момент воспроизведения.

## Root Cause
gRPC клиент появляется после инициализации welcome, но не обновляется → `GrpcClient not injected` → fallback.

## Optimal Fix
Отложенная инъекция gRPC клиента: обновлять `WelcomePlayer` перед воспроизведением и при старте интеграции.

## Verification
- Логи без `GrpcClient not injected`
- Приветствие использует server audio при доступном gRPC

## Запрос/цель
Гарантировать основной TTS через gRPC для welcome.

## Контекст
- Файлы: `client/integration/integrations/welcome_message_integration.py`, `client/modules/welcome_message/core/welcome_player.py`, `client/modules/welcome_message/core/audio_generator.py`

## Решения/выводы
- Добавлен `set_grpc_client` и refresh перед воспроизведением.

## Открытые вопросы
- Нужна ли строгая задержка welcome до `grpc.connected`?

## Следующие шаги
- Перезапуск клиента и проверка логов.
