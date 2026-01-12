# Verification: Session ID Contract Readiness

**Дата:** 2026-01-12  
**Тип:** verification  
**Ассистент:** cursor  
**Статус:** ✅ Готово к тестированию

---

## Executive Summary

Все компоненты готовы к строгому контракту `session_id`. Код обновлен, документация синхронизирована, fail-fast проверки на месте. Система готова к smoke-тестированию.

---

## Проверка компонентов

### ✅ 1. Proto-файлы синхронизированы

**Server:**
- `server/server/modules/grpc_service/streaming.proto`
  - `session_id` помечен как `REQUIRED` (строка 24)
  - Комментарий: `// REQUIRED: ID сессии для отслеживания (обязателен с 2026-01-12, см. CHANGELOG.md)`

**Client:**
- `client/modules/grpc_client/proto/streaming.proto`
  - Синхронизирован с серверной версией
  - `session_id` помечен как `REQUIRED` (строка 24)

### ✅ 2. Клиентский код обновлен

**`client/modules/grpc_client/core/grpc_client.py`:**
- ✅ Обязательный параметр `session_id: str` (строка 261)
- ✅ Fail-fast проверка (строки 272-275):
  ```python
  if not session_id or not session_id.strip():
      error_msg = "session_id is required and must be provided (Source of Truth: ApplicationStateManager)"
      logger.error(f"❌ [gRPC] {error_msg}")
      raise ValueError(error_msg)
  ```
- ✅ `session_id` передается в `StreamRequest` (строка 308)

**`modules/grpc_client/core/grpc_client.py` (production):**
- ✅ Обновлен аналогично

**`integration/integrations/grpc_client_integration.py`:**
- ✅ Получает `session_id` из `ApplicationStateManager` через `get_current_session_id` (строка 363)
- ✅ Использует `final_session_id` во всех местах
- ✅ Передает `session_id` в `stream_audio` (строка 440)
- ✅ TRACE логи используют `final_session_id` (строки 413, 447)

### ✅ 3. Серверный валидатор

**`server/server/modules/grpc_service/core/grpc_server.py`:**
- ✅ Строгая валидация `session_id` (строки 125-137)
- ✅ Возвращает `INVALID_ARGUMENT` при отсутствии `session_id`
- ✅ Логирует `decision=abort` с `reason=missing_session_id`

### ✅ 4. Документация

**`Docs/CHANGELOG.md`:**
- ✅ Breaking change зафиксирован (2026-01-12)
- ✅ Описаны изменения, миграция и обратная совместимость

**`server/server/Docs/GRPC_PROTOCOL_AUDIT.md`:**
- ✅ Обновлен раздел "Breaking Changes (2026-01-12)"
- ✅ `session_id` помечен как `required*` с пояснением

---

## План smoke-тестирования

### Тест 1: Валидный запрос с session_id

**Цель:** Убедиться, что запросы с валидными идентификаторами проходят успешно.

**Шаги:**
1. Запустить клиент с валидным `session_id` из `ApplicationStateManager`
2. Отправить `StreamAudio` запрос
3. Проверить успешность запроса

**Ожидаемое поведение:**
- ✅ Клиент: `TRACE phase=grpc.start ... session=<uuid>`
- ✅ Клиент: `TRACE phase=grpc.response ... session=<uuid>`
- ✅ Сервер: нет `decision=abort` с `reason=missing_session_id`
- ✅ Сервер: успешная обработка запроса

**Команда для тестирования:**
```bash
# Запустить сервер
cd server/server
python main.py

# В другом терминале: запустить клиент и выполнить PTT → STT → gRPC
cd /Users/sergiyzasorin/Fix_new
python main.py
# Выполнить PTT (push-to-talk) и проверить логи
```

### Тест 2: Fail-fast на клиенте (без session_id)

**Цель:** Убедиться, что клиент не отправляет запросы без `session_id`.

**Шаги:**
1. Симулировать ситуацию, когда `session_id` отсутствует в `ApplicationStateManager`
2. Попытаться отправить запрос
3. Проверить, что запрос не отправляется

**Ожидаемое поведение:**
- ✅ Клиент: `❌ [gRPC] session_id is required and must be provided`
- ✅ Клиент: `grpc.request_failed` с `error="missing_session_id"`
- ✅ Сервер: запрос не доходит до сервера

**Проверка в коде:**
```python
# В grpc_client_integration.py (строки 366-369)
if not session_id or not session_id.strip():
    logger.error(f"❌ [gRPC] session_id отсутствует в state_manager и не передан - fail-fast")
    await self.event_bus.publish("grpc.request_failed", {"session_id": session_id, "error": "missing_session_id"})
    return
```

### Тест 3: Валидация на сервере (защита от старых клиентов)

**Цель:** Убедиться, что сервер отклоняет запросы без `session_id` от старых клиентов.

**Шаги:**
1. Использовать `grpc_smoke.py` для отправки запроса без `session_id`
2. Проверить ответ сервера

**Ожидаемое поведение:**
- ✅ Сервер: `decision=abort` с `reason=missing_session_id`
- ✅ Сервер: `error_message: "session_id is required and must be provided by client"`

**Команда для тестирования:**
```bash
cd server/server
python scripts/grpc_smoke.py localhost 50051
# Тест test_stream_audio_missing_session_id должен пройти
```

### Тест 4: Регрессионная проверка (PTT → STT → gRPC → playback)

**Цель:** Убедиться, что полный цикл работает без ошибок.

**Шаги:**
1. Выполнить полный цикл: PTT → STT → gRPC → playback
2. Проверить отсутствие `grpc.request_failed`

**Ожидаемое поведение:**
- ✅ Нет `grpc.request_failed` в логах
- ✅ Успешное воспроизведение аудио
- ✅ Корректная обработка `session_id` на всех этапах

---

## Чек-лист готовности

### Код
- [x] Proto-файлы синхронизированы (server и client)
- [x] Все вызовы `stream_audio` обновлены с передачей `session_id`
- [x] Fail-fast проверка добавлена в `grpc_client.py`
- [x] `grpc_client_integration` получает `session_id` из `ApplicationStateManager`
- [x] `final_session_id` используется во всех событиях/логах
- [x] Серверный валидатор проверяет `session_id`

### Документация
- [x] Breaking change зафиксирован в `CHANGELOG.md`
- [x] `GRPC_PROTOCOL_AUDIT.md` обновлен
- [x] Миграционные инструкции добавлены

### Тестирование
- [ ] Smoke-тест с валидными `session_id`/`hardware_id` (требует запуска)
- [ ] Fail-fast тест без `session_id` (требует запуска)
- [ ] Проверка логов на отсутствие `missing_session_id` (требует запуска)
- [ ] Регрессионная проверка PTT → STT → gRPC → playback (требует запуска)

---

## Критерии успеха

### Код готов ✅
- Все компоненты обновлены
- Fail-fast проверки на месте
- Единый источник истины соблюден

### Документация готова ✅
- Breaking change зафиксирован
- Миграционные инструкции добавлены
- Proto-контракт синхронизирован

### Готово к тестированию ✅
- Smoke-тесты доступны (`grpc_smoke.py`)
- План тестирования определен
- Критерии успеха ясны

---

## Следующие шаги

1. **Запустить smoke-тесты:**
   ```bash
   cd server/server
   python scripts/grpc_smoke.py localhost 50051
   ```

2. **Провести ручное тестирование:**
   - Запустить клиент и выполнить PTT → STT → gRPC
   - Проверить логи на наличие `TRACE phase=grpc.start ... session=<uuid>`
   - Убедиться, что нет `grpc.request_failed`

3. **Проверить серверные логи:**
   - Убедиться, что нет `decision=abort` с `reason=missing_session_id` при валидных запросах
   - Проверить, что валидация работает для запросов без `session_id`

---

## Заключение

**Статус:** ✅ **Готово к релизу при условии прохождения smoke-тестов**

Все компоненты обновлены и готовы. Код соответствует строгому контракту `session_id`, документация синхронизирована, fail-fast проверки на месте. Система готова к тестированию и последующему релизу.

**Критерий "стало проще/стабильнее":** ✅ Выполнен
- Контракт соблюден во всех компонентах
- Поведение предсказуемо (fail-fast на клиенте, валидация на сервере)
- Единый источник истины (`ApplicationStateManager`)
- Нет "тихих" fallback'ов
