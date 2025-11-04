# DecisionEngine "Скелет" — финальная структура

**Статус**: ✅ Этап 2 завершен — DecisionEngine интегрирован

---

## 📐 Скелет (3 слоя)

### 1. STATE_CATALOG.md — "кости"
- Перечень осей состояния
- Владелец каждой оси
- Обязанность синхронизировать правила и код

### 2. interaction_matrix.yaml — "суставы"
- Формализованные правила `when → decision` с приоритетом
- Привязка к gateway через поле `gateway`
- Схема: `interaction_matrix.schema.json`

### 3. Gateways layer — "мышцы"
- `integration/core/gateways/decision_engine.py` — движок правил
- `integration/core/gateways/rule_loader.py` — загрузка из YAML
- `integration/core/gateways/predicates.py` — регистр предикатов
- `integration/core/gateways/base.py` — DecisionCtx и логирование
- `integration/core/gateways/engine_loader.py` — кэширование engines
- `integration/core/gateways/common.py` — публичные gateways
- `integration/core/gateways/permission_gateways.py` — permission gateways

---

## ✅ Что сделано (Этап 2)

### 1. Интегрирован DecisionEngine в публичные gateways

**`decide_start_listening()`**:
```python
def decide_start_listening(s: Snapshot) -> Decision:
    try:
        engine = get_engine("decide_start_listening")
        ctx = create_ctx_from_snapshot(s)
        return engine.decide(s, source="listening_gateway", ctx=ctx, extra=None)
    except Exception as exc:
        # Fallback to legacy logic
        ...
```

**`decide_process_audio()`**, **`decide_continue_integration_startup()`**, **`decide_permission_restart_safety()`** — аналогично.

### 2. Синхронизированы правила в YAML

**Адаптированы ключи**:
- `Permission.mic: denied` → `perm.mic: denied`
- `FirstRun: true` → `app.first_run: true`
- `Device.input: busy` → `device.busy: true`
- `Network: offline` → `network.offline: true`
- `appMode: LISTENING` → `app.mode: listening`
- `update_in_progress: true` → `update.in_progress: true`

**Адаптированы решения**:
- `abort_listen` → `abort`
- `retry_backoff` → `retry`
- `degrade_offline` → `degrade`
- `abort_permission_restart` → `abort`

### 3. Добавлены предикаты

- `app.restart_pending` — проверка restart_pending
- `app.first_run_restart_pending` — проверка first_run + restart_pending
- `update.in_progress` — проверка update_in_progress (из extra)

---

## 🔄 Обратная совместимость

✅ **Сохраняется**:
- Все функции возвращают только `Decision`
- Fallback на legacy логику при ошибках engine
- Логирование через `log_decision()` в каноническом формате

---

## 📋 Правила в YAML (адаптированные)

### decide_start_listening
```yaml
- gateway: decide_start_listening
  priority: hard_stop
  when: {perm.mic: denied}
  decision: abort

- gateway: decide_start_listening
  priority: hard_stop
  when: {app.first_run: true}
  decision: abort

- gateway: decide_start_listening
  priority: graceful
  when: {device.busy: true}
  decision: retry

- gateway: decide_start_listening
  priority: graceful
  when: {network.offline: true}
  decision: degrade
```

### decide_permission_restart_safety
```yaml
- gateway: decide_permission_restart_safety
  priority: hard_stop
  when: {app.first_run_restart_pending: true}
  decision: abort

- gateway: decide_permission_restart_safety
  priority: graceful
  when: {update.in_progress: true}
  decision: abort
```

### decide_continue_integration_startup
```yaml
- gateway: decide_continue_integration_startup
  priority: hard_stop
  when: {app.first_run_restart_pending: true}
  decision: abort
```

---

## ⚠️ Важные моменты

1. **Fallback логика**: Если DecisionEngine не работает, используется legacy логика (для безопасности)

2. **Кэширование**: Engine создается один раз и кэшируется (singleton pattern через `engine_loader.py`)

3. **Правила из YAML**: Правила должны быть синхронизированы с предикатами

4. **Extra контекст**: `update_in_progress` передается через `extra` dict для `decide_permission_restart_safety`

5. **Логирование**: DecisionEngine использует `log_decision()` из `base.py`, который логирует в каноническом формате

---

## 📝 Следующие шаги (Этап 3)

1. **Валидация YAML**: Добавить проверку схемы в CI
2. **Golden-тест**: Реализовать валидацию реального лог-файла
3. **Тесты**: Добавить тесты для загрузки правил из YAML

---

**Владелец**: Tech Lead клиента  
**Последнее обновление**: 2025-01-30

