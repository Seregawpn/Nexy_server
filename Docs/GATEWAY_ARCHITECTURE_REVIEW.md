# Review: DecisionEngine-based Gateway Architecture

**Дата**: 2025-01-30  
**Предложенная архитектура**: Rule-based DecisionEngine с hard_stop/graceful/preference

---

## ✅ Что хорошо в предложенной архитектуре

### 1. Rule-based подход
- **Плюс**: Правила изолированы, легко тестируются
- **Плюс**: Соответствует структуре `interaction_matrix.yaml` (hard_stop/graceful/preference)
- **Плюс**: Легко добавлять новые правила без изменения существующих

### 2. Приоритеты правил
- **Плюс**: Четкий порядок: `hard_stop > graceful > preference`
- **Плюс**: Соответствует документации в `.cursorrules` раздел 18.2

### 3. Структура файлов
- **Плюс**: Разделение на `decision_types.py`, `selectors.py`, `gateways.py`, `decision_logging.py`
- **Плюс**: Чистые интерфейсы, легко поддерживать

---

## ❌ Проблемы и несоответствия

### 1. Несовместимость с текущей реализацией

**Текущая реализация**:
```python
def decide_start_listening(s: Snapshot) -> Decision:
    # Возвращает только Decision
    return Decision.START
```

**Предложенная**:
```python
def decide_start_listening(s: Snapshot) -> Tuple[Decision, str]:
    # Возвращает (Decision, log_string)
    return Decision.START, log_string
```

**Проблема**: Все существующие вызовы gateways ожидают только `Decision`, не `Tuple[Decision, str]`.

**Решение**: Либо мигрировать все вызовы, либо сделать log опциональным.

---

### 2. DecisionEngine создается каждый раз

**Предложенный код**:
```python
def decide_start_listening(s: Snapshot) -> Tuple[Decision, str]:
    return build_default_engine().decide(s, source="audio.start_listening")
```

**Проблема**: `build_default_engine()` создается при каждом вызове — неэффективно.

**Решение**: Создавать engine один раз и кэшировать.

---

### 3. decision_logging.py не интегрирован

**Текущая реализация**:
```python
def _log_decision(*, level: str, decision: Decision, s: Snapshot, source: str, reason: str | None = None, duration_ms: int | None = None) -> None:
    # Логирует через logger
    log_fn = getattr(logger, level, logger.info)
    log_fn(msg)
```

**Предложенная**:
```python
def decision_log(decision: Decision, *, ctx: Mapping[str, object], source: str, started_ts: float) -> str:
    # Возвращает строку, не логирует
    return f"decision={decision.name.lower()} ..."
```

**Проблема**: 
- Предложенная версия возвращает строку, не логирует
- Текущая версия логирует напрямую через logger
- Нет интеграции между ними

**Решение**: Объединить подходы — логировать через logger И возвращать строку для тестов.

---

### 4. Отсутствует update_in_progress в Snapshot

**Текущая реализация**:
```python
@dataclass(frozen=True)
class Snapshot:
    # ...
    restart_pending: bool = False
    update_in_progress: bool = False  # ✅ Есть
```

**Предложенная**:
```python
@dataclass(frozen=True)
class Snapshot:
    # ...
    update_in_progress: bool = False  # ✅ Есть в предложенном коде
```

**Статус**: ✅ ОК, есть в обоих.

---

### 5. Правила хардкодятся, а не загружаются из YAML

**Текущая реализация**: Правила закодированы в функциях `decide_*()`.

**Предложенная**: Правила хардкодятся в `build_default_engine()`.

**Проблема**: Согласно `.cursorrules` раздел 18.2, правила должны быть в `interaction_matrix.yaml`.

**Решение**: Загружать правила из YAML и регистрировать их в engine.

---

### 6. Нет интеграции с существующими selectors

**Текущая реализация**:
```python
from integration.core.selectors import (
    mic_ready, screen_ready, can_start_listening,
    is_first_run_restart_pending, ...
)
```

**Предложенная**: Создает свои версии selectors в `selectors.py`.

**Проблема**: Дублирование кода, рассинхронизация.

**Решение**: Использовать существующие selectors из `integration/core/selectors.py`.

---

### 7. decision_logging.py не учитывает duration_ms правильно

**Предложенный код**:
```python
def decision_log(decision: Decision, *, ctx: Mapping[str, object], source: str, started_ts: float) -> str:
    duration_ms = int((time.time() - started_ts) * 1000)
    # ...
```

**Проблема**: Если `started_ts` передан извне, может быть неточным. Лучше передавать `duration_ms` напрямую.

**Решение**: Принимать `duration_ms` как параметр, не вычислять внутри.

---

## 🔧 Рекомендации по улучшению

### 1. Интеграция с текущей архитектурой

**Вариант A (минимальные изменения)**: Оставить текущую архитектуру, добавить DecisionEngine как опциональный слой.

```python
# В common.py
class DecisionEngine:
    # ... как в предложенном коде

# В decide_start_listening() - использовать engine, но возвращать только Decision
def decide_start_listening(s: Snapshot) -> Decision:
    engine = _get_default_engine()  # Кэшированный engine
    decision, log = engine.decide(s, source="listening_gateway")
    _log_decision(decision=decision, s=s, source="listening_gateway")
    return decision
```

**Вариант B (полная миграция)**: Мигрировать все gateways на DecisionEngine.

- Требует изменения всех вызовов
- Более гибко, но больше работы

---

### 2. Загрузка правил из interaction_matrix.yaml

```python
def load_rules_from_matrix(matrix_path: Path) -> DecisionEngine:
    """Load rules from interaction_matrix.yaml."""
    with open(matrix_path, "r") as f:
        matrix = yaml.safe_load(f)
    
    engine = DecisionEngine()
    
    for rule in matrix.get("rules", []):
        priority = rule.get("priority", "preference")
        when = rule.get("when", {})
        
        # Создать правило из YAML
        rule_func = create_rule_from_yaml(when)
        
        if priority == "hard_stop":
            engine.add_hard_stop(rule_func)
        elif priority == "graceful":
            engine.add_graceful(rule_func)
        else:
            engine.add_preference(rule_func)
    
    return engine
```

---

### 3. Интеграция decision_logging с текущим _log_decision

```python
def decision_log(
    decision: Decision,
    *,
    ctx: Mapping[str, object],
    source: str,
    duration_ms: int | None = None,
) -> str:
    """Generate canonical decision log string.
    
    Also logs via logger for backward compatibility.
    """
    # Генерировать строку
    log_str = f"decision={decision.value} ctx={...} source={source}"
    if duration_ms is not None:
        log_str += f" duration_ms={duration_ms}"
    
    # Логировать через logger (как в текущей реализации)
    logger.info(log_str)
    
    return log_str
```

---

### 4. Кэширование DecisionEngine

```python
# В common.py
_default_engine: DecisionEngine | None = None

def _get_default_engine() -> DecisionEngine:
    """Get or create default DecisionEngine (cached)."""
    global _default_engine
    if _default_engine is None:
        _default_engine = build_default_engine()
    return _default_engine
```

---

## 📊 Сравнение подходов

| Аспект | Текущая реализация | Предложенная архитектура |
|--------|-------------------|--------------------------|
| **Структура** | Функции `decide_*()` | DecisionEngine с правилами |
| **Правила** | Хардкод в функциях | Правила в engine (можно загружать из YAML) |
| **Логирование** | `_log_decision()` | `decision_log()` возвращает строку |
| **Возврат** | `Decision` | `Tuple[Decision, str]` |
| **Тестируемость** | Средняя | Высокая (правила изолированы) |
| **Расширяемость** | Средняя | Высокая (легко добавлять правила) |
| **Соответствие YAML** | Частичное | Полное (можно загружать) |

---

## ✅ Итоговая оценка

### Что нужно исправить:

1. **Интеграция с текущим кодом**:
   - Использовать существующие selectors
   - Интегрировать с `_log_decision()` (логировать через logger)
   - Сохранить возврат только `Decision` (или мигрировать все вызовы)

2. **Загрузка правил из YAML**:
   - Загружать правила из `interaction_matrix.yaml`
   - Не хардкодить в `build_default_engine()`

3. **Кэширование engine**:
   - Создавать engine один раз, не при каждом вызове

4. **Decision logging**:
   - Логировать через logger (как сейчас)
   - Возвращать строку для тестов (опционально)

---

## 🎯 Рекомендация

**Гибридный подход**: Использовать DecisionEngine внутри текущих функций `decide_*()`, но сохранить текущий интерфейс.

```python
# В common.py
_default_engine = None

def _get_default_engine() -> DecisionEngine:
    global _default_engine
    if _default_engine is None:
        _default_engine = load_engine_from_matrix()  # Загрузить из YAML
    return _default_engine

def decide_start_listening(s: Snapshot) -> Decision:
    """Decide whether to start listening (backward compatible)."""
    engine = _get_default_engine()
    decision, log_str = engine.decide(s, source="listening_gateway")
    
    # Логировать через текущий механизм
    _log_decision(decision=decision, s=s, source="listening_gateway")
    
    return decision  # Возвращаем только Decision для совместимости
```

**Преимущества**:
- ✅ Сохраняет обратную совместимость
- ✅ Использует rule-based подход
- ✅ Правила загружаются из YAML
- ✅ Легко тестировать и расширять

---

**Владелец**: Tech Lead клиента  
**Последнее обновление**: 2025-01-30



