# MEMORY REQUIREMENTS (Pre-Implementation Contract)

## 1. Цель

Зафиксировать единый runtime-контракт памяти до реализации:
- что и в каком формате извлекается;
- что и как сохраняется;
- как кэшируется;
- как memory context передается основному ассистенту.

Документ обязателен для всех изменений memory-path.

## 2. Scope и границы

Включено:
- short-term, medium-term, long-term память;
- async extraction после ответа пользователю;
- owner-path валидации/сохранения;
- DB + cache политика;
- anti-race / idempotency требования.

Не включено:
- изменение формата пользовательского ответа;
- реархитектура gRPC/runtime flow.

## 3. Single Owner

- Owner решения `save/drop/merge`: `MemoryManager`.
- `MemoryWorkflowIntegration`: только orchestration и cache lifecycle.
- `MemoryAnalyzer` (LLM): только extraction/canonicalization, без права записи напрямую.
- Прямая запись в БД вне `MemoryManager` запрещена.

## 4. Runtime flow (обязательно)

1. Запрос пользователя приходит в основной workflow.
2. Основной ассистент формирует и отправляет ответ пользователю (sync-path).
3. После `response.sent` публикуется async memory extraction request.
4. Memory extractor формирует `memory_candidates` по строгой схеме.
5. `MemoryManager` валидирует, фильтрует, дедуплицирует, применяет TTL/merge.
6. Валидные данные сохраняются в БД (write-through cache).
7. На следующий запрос основной ассистент получает обновленный `runtime_memory_context`.

## 5. Формат входа в memory extraction

```json
{
  "session_id": "uuid",
  "hardware_id": "string",
  "turn_index": 12,
  "current_request": {
    "user": "Найди скидки на наушники",
    "assistant_response": "Ищу лучшие варианты со скидкой.",
    "action_outcome": "user requested browser search 'скидки на наушники' -> success"
  },
  "previous_requests": [
    {"turn": 11, "user": "...", "assistant_result": "..."},
    {"turn": 10, "user": "...", "assistant_result": "..."},
    {"turn": 9, "user": "...", "assistant_result": "..."},
    {"turn": 8, "user": "...", "assistant_result": "..."}
  ],
  "current_memory_snapshot": {
    "medium_term": ["..."],
    "long_term": {
      "profile": {"name": "Сергей", "language": "ru"},
      "contacts": []
    }
  }
}
```

## 6. Формат выхода memory extraction

```json
{
  "memory_candidates": {
    "short_term_snapshot": {
      "turn_index": 12,
      "current_request": {
        "turn": 12,
        "user": "Найди скидки на наушники",
        "assistant_result": "Поиск скидок выполнен",
        "action_outcome": "browser.search success"
      },
      "previous_requests": [
        {"turn": 11, "position": "prev_1", "user": "...", "assistant_result": "..."},
        {"turn": 10, "position": "prev_2", "user": "...", "assistant_result": "..."},
        {"turn": 9, "position": "prev_3", "user": "...", "assistant_result": "..."},
        {"turn": 8, "position": "prev_4", "user": "...", "assistant_result": "..."}
      ]
    },
    "medium_term": [
      "Пользователь регулярно просит искать скидки на электронику"
    ],
    "long_term_facts": [
      {"key": "name", "value": "Сергей", "confidence": 0.99},
      {"key": "language", "value": "ru", "confidence": 0.95}
    ]
  }
}
```

## 7. Требования по tier-логике

### 7.1 Short-term (оперативная память)
- Формат обязателен: `current_request + previous_requests (prev_1..prev_4)`.
- Хранить максимум 4 предыдущих запроса.
- Хранить только человекочитаемые итоги и контекст; raw JSON запрещен.
- `turn_index` обязателен и монотонно растет.
- TTL: 1 час (настраиваемо через config, но дефолт 1h).

### 7.2 Medium-term (рабочая история)
- Хранить только сжатые смысловые пункты (topics/outcomes), не raw диалог.
- За один extraction cycle: максимум 3 записи.
- Ретеншн: 30 дней.
- Дубликаты по смыслу не допускаются.

### 7.3 Long-term (факты профиля)
- Хранить только факты (slot-based), без inference.
- Разрешенные ключи:
  - `name`, `surname`, `email`, `language`, `preference`, `contact`.
- Обновление через upsert по ключу слота.
- Одноразовые задачи/временные состояния/технические детали сохранять запрещено.

## 8. Валидация и фильтрация (обязательно)

Перед сохранением каждый candidate проходит проверки в `MemoryManager`:
- schema validation;
- raw JSON / tool payload / logs reject;
- allowlist для `long_term_facts.key`;
- confidence threshold (для long-term);
- dedup (idempotency key + semantic dedup);
- stale-update reject (старый turn не может перезаписать новый).

Если проверка не пройдена: запись не сохраняется и логируется `drop_reason`.

## 9. Сохранение в БД

Требование owner-path:
- только `MemoryManager` вызывает DB update API.

Базовая схема хранения (без реархитектуры):
- `users.short_term_memory`: medium-term JSON digest (исторический слой);
- `users.long_term_memory`: long-term slot JSON;
- `short_term_snapshot`: L1 in-memory snapshot (опционально mirror в persisted JSON при расширении схемы).

## 10. Кэширование

### 10.1 L1 (ephemeral)
- Short-term snapshot per `hardware_id`.
- TTL: 1h.
- Bounded max entries (обязательно).

### 10.2 L2 (persistent cache)
- Medium/Long per `hardware_id`.
- TTL: 5m.
- Bounded max entries.

### 10.3 Политика
- Read path: cache-first.
- Cache miss: fetch from DB + populate cache.
- Stale read разрешен только с async refresh.
- Write-through: successful DB write -> cache update в том же owner-path.

## 11. Concurrency / Anti-Race

Обязательные guard-механизмы:
- per-user lock для update path;
- idempotency key: `hardware_id:turn_index`;
- stale-write reject (turn/order guard);
- single-flight fetch для одного `hardware_id`.

Out-of-order и retry не должны создавать дубли и не должны откатывать память назад.

## 12. Runtime формат для основного ассистента

```json
{
  "runtime_memory_context": {
    "short": {
      "current": "...",
      "prev_1": "...",
      "prev_2": "...",
      "prev_3": "...",
      "prev_4": "..."
    },
    "medium": ["...", "..."],
    "long": {
      "name": "...",
      "language": "...",
      "preferences": ["..."]
    }
  }
}
```

Требования:
- формат стабилен между запросами;
- нет сырого payload/JSON;
- short всегда содержит актуальный `current`.

## 13. Observability

Обязательные логи:
- `memory.extract.request`
- `memory.validate.accept`
- `memory.validate.drop` (`reason=...`)
- `memory.persist.ok`
- `memory.cache.hit|miss|stale_refresh`

Минимальные метрики:
- extraction latency;
- validation drop rate;
- dedup hit rate;
- cache hit ratio;
- size per tier.

## 14. Запреты

Запрещено:
- хранить raw JSON/tool args/log chunks в любом tier;
- писать в БД памяти в обход `MemoryManager`;
- создавать второй owner-path в workflow/integrations;
- продвигать transient task details в long-term.

## 15. DoD (Definition of Done)

Изменение считается готовым только если:
1. Short-term строго в формате `current + prev_1..prev_4`.
2. Medium-term хранит только сжатые outcomes/topics и соблюдает TTL 30d.
3. Long-term хранит только factual slots (allowlist).
4. Нет raw JSON в сохраненной памяти.
5. Async extraction не влияет на latency пользовательского ответа.
6. Retry/out-of-order не создают дублей и не ломают порядок turn.

