# gRPC send blocked by stale network gate

## Симптом
После `voice.recognition_completed` сразу публиковался `grpc.request_failed(error=offline)`, запрос не уходил.

## Причина
В `GrpcClientIntegration._maybe_send()` при `use_network_gate=true` и `_network_connected=False`
был жесткий ранний выход без попытки реального reconnect.
Если статус сети в state manager устаревал, отправка блокировалась ложно.

## Изменение
- Файл: `integration/integrations/grpc_client_integration.py`
- Ветка `network_gate == offline` изменена:
  - теперь делается `await self._ensure_connected()` (single-flight reconnect probe),
  - только если reconnect не удался — публикуется `grpc.request_failed: offline`,
  - при успехе gate поднимается в `True` и отправка продолжается.

## Эффект
- Убран false-negative `offline` на отправке.
- Сохранена централизация: решение в транспортном слое, а не в input/workflow.

## Проверка
- `python3 -m py_compile integration/integrations/grpc_client_integration.py` ✅
- `pytest -q tests/test_processing_workflow_session_guard.py` ✅
