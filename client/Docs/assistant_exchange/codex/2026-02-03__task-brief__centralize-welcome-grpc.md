# Task Brief: Centralize Welcome gRPC Access

## Scope
Централизация доступа WelcomeMessage к gRPC через GrpcClientIntegration.

## Changes
- `integration/integrations/grpc_client_integration.py`: добавлены `get_client()`, `get_server_name()`, `get_request_timeout_sec()`.
- `modules/welcome_message/core/audio_generator.py`: поддержка инъекции gRPC клиента/параметров; fallback на локальный конфиг только если клиент не передан.
- `modules/welcome_message/core/welcome_player.py`: прокидывание gRPC клиента/параметров в генератор.
- `integration/integrations/welcome_message_integration.py`: получение gRPC клиента из интеграции и передача в WelcomePlayer.
- `integration/core/integration_factory.py`: передача grpc интеграции в welcome интеграцию.

## Verification
- `scripts/verify_feature_flags.py` отсутствует (скрипт не найден).
- Тесты не запускались.
