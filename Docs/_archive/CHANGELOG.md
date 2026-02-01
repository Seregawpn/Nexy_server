# Changelog


## [Breaking Change] 2026-01-12 - Строгий контракт идентификаторов

### Изменения
- **`session_id` теперь обязателен в `StreamAudio`** (ранее был `optional` в proto)
  - Сервер возвращает `INVALID_ARGUMENT` с `error_message` при отсутствии `session_id`
  - Единственный источник истины: `InputProcessingIntegration` на клиенте
- **`hardware_id` не может быть пустым или "unknown"**
  - Сервер возвращает `INVALID_ARGUMENT` при пустом или "unknown" значении
- **`InterruptSession` использует поле `message` вместо `error_message`** (исправление контракта)

### Миграция
- **Обновить клиент** до версии, которая передаёт `session_id` от `InputProcessingIntegration`
- Убедиться, что `hardware_id` валиден (не пустой и не "unknown")
- Проверить обработку ошибок `INVALID_ARGUMENT` на клиенте
- **Обновить proto-файлы:** В `streaming.proto` поле `session_id` больше не имеет `optional` и помечено комментарием `REQUIRED`. Регенерировать protobuf файлы: `python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. modules/grpc_service/streaming.proto`

### Обратная совместимость
- ❌ **Breaking change:** старые клиенты без `session_id` перестанут работать
- ✅ **Рекомендуется:** обновление всех клиентов до версии с поддержкой обязательного `session_id`

### Документация
- См. `Docs/assistant_exchange/cursor/2026-01-12__review__server-identifier-contract.md` для детального анализа
- См. `server/server/Docs/GRPC_PROTOCOL_AUDIT.md` для обновлённых правил совместимости

---

## [v1.0.0] - 2026-01-05
- **NEXY-003**: Release Packaging (Auto-Sync) (@DevOps)

All notable changes to this project will be documented in this file.