# Tray Icon Acceptance Checklist

Быстрый чек-лист для приёмки tray icon с метриками и диагностикой.

## Быстрый прогон (≈15 минут)

### 1. Тёплый старт ×3

**Действие:**
- Полный выход из Nexy → запуск вручную

**Ожидаемое в логах:**
- ✅ `TRAY_SERIES_ID=<uuid>` при старте
- ✅ `TRAY_ATTEMPT1 result=ok` ≤ 5 с
- ✅ `TAL=hold` → `TAL=released` до `tray.ready`
- ✅ Нет каскада `…-Aux[n]-NSStatusItemView`

**Проверка:**
```bash
log show --last 5m --style compact \
  --predicate 'process == "Nexy" && (eventMessage CONTAINS[c] "TRAY_" OR eventMessage CONTAINS[c] "TAL=")'
```

---

### 2. Холодный старт ×3

**Действие:**
- Перезагрузка macOS → автозапуск/запуск Nexy

**Ожидаемое в логах:**
- ✅ `CC_READY ts=...` (момент готовности Control Center)
- ✅ `TRAY_ATTEMPT{n} result=ok` у 95% ≤ 30 с, у 99% ≤ 60 с
- ✅ `TRAY_BACKOFF_NEXT=<ms>ms` с jitter ±15% при ошибках
- ✅ Нет «лесенки» `Aux[n]`

**Проверка:**
```bash
log show --last 10m --style compact \
  --predicate 'process == "Nexy" && (eventMessage CONTAINS[c] "TRAY_" OR eventMessage CONTAINS[c] "CC_READY")'
```

**Анализ SLO:**
```bash
python scripts/parse_tray_metrics.py log.md --cold-start
```

---

### 3. Перезапуск после TCC

**Действие:**
- Спровоцировать запросы разрешений → авто-релонч

**Ожидаемое в логах:**
- ✅ `RESTART_FLAG seen_ts=..., age_ms=..., pid=...` **ровно один раз** после перезапуска
- ✅ `TRAY_ATTEMPT{n} result=ok` в тех же SLO, что в холодном старте
- ✅ Атомарная запись: `atomic write -> rename`
- ✅ Атомарное чтение-и-удаление: `atomic read-and-remove`

**Проверка:**
```bash
log show --last 10m --style compact \
  --predicate 'process == "Nexy" && (eventMessage CONTAINS[c] "RESTART_FLAG" OR eventMessage CONTAINS[c] "ATOMIC_FLAG")'
```

---

### 4. Перезапуск Control Center

**Действие:**
- `killall ControlCenter` во время работы Nexy

**Ожидаемое в логах:**
- ✅ Аккуратное восстановление одной серией попыток
- ✅ При 3 подряд ошибках: `CIRCUIT_OPEN reason=..., series_errors=3, after=8000ms`
- ✅ После паузы: `CIRCUIT_CLOSE after=8000ms`
- ✅ Нет шквала попыток без пауз

**Проверка:**
```bash
log show --last 5m --style compact \
  --predicate 'process == "Nexy" && (eventMessage CONTAINS[c] "CIRCUIT_" OR eventMessage CONTAINS[c] "TRAY_ATTEMPT")'
```

---

### 5. «Без трея» fallback

**Действие:**
- Эмулировать тяжёлые условия (нагрузка/задержка CC)

**Ожидаемое в логах:**
- ✅ После 60 s: переход в режим без tray (если реализовано)
- ✅ Фоновый редкий retry каждые 30–60 s (single-flight)
- ✅ Нет шквала попыток

**Проверка:**
```bash
log show --last 10m --style compact \
  --predicate 'process == "Nexy" && eventMessage CONTAINS[c] "TRAY_"'
```

---

## Что должно быть в логах

### Обязательные метрики

- ✅ `TRAY_SERIES_ID=<uuid>` — при каждом старте
- ✅ `TRAY_ATTEMPT{n} start` — начало попытки
- ✅ `TRAY_ATTEMPT{n} result=ok|error (code=..., duration=...ms)` — результат
- ✅ `TRAY_BACKOFF_NEXT=<ms>ms (jitter=±15%)` — следующий backoff
- ✅ `CC_READY ts=...` — момент готовности Control Center
- ✅ `CIRCUIT_OPEN reason=..., series_errors=3, after=8000ms` — открытие circuit
- ✅ `CIRCUIT_CLOSE after=8000ms` — закрытие circuit
- ✅ `TAL=hold (ts=...)` — начало TAL удержания
- ✅ `TAL=released (ts=..., duration=...s)` — снятие TAL удержания
- ✅ `RESTART_FLAG seen_ts=..., age_ms=..., pid=..., reason=...` — обнаружение флага перезапуска

---

## Что НЕ должно быть в логах

### Критические проблемы

- ❌ Повторяющиеся `com.apple.controlcenter:…-Aux[n]-NSStatusItemView` (каскад сцен)
- ❌ Каскад `BSServiceConnectionErrorDomain` без пауз (не сработал circuit-breaker)
- ❌ `_kLSApplicationWouldBeTerminatedByTALKey=1` до `tray.ready` (TAL снят раньше времени)
- ❌ `RESTART_FLAG` появляется несколько раз (не атомарное read-and-remove)

---

## Удобные команды наблюдения

### Только нужные процессы

```bash
log stream --style compact \
  --predicate 'process == "Nexy" || process == "ControlCenter" || process == "tccd" || process == "audiomxd"'
```

### Быстрый срез по ошибкам сцены

```bash
log show --last 10m --style compact \
  --predicate '(eventMessage CONTAINS[c] "FBSScene" OR eventMessage CONTAINS[c] "BSServiceConnectionErrorDomain") && process == "Nexy"'
```

### Только метрики tray

```bash
log show --last 10m --style compact \
  --predicate 'process == "Nexy" && (eventMessage CONTAINS[c] "TRAY_" OR eventMessage CONTAINS[c] "CC_READY" OR eventMessage CONTAINS[c] "CIRCUIT_" OR eventMessage CONTAINS[c] "TAL=" OR eventMessage CONTAINS[c] "RESTART_FLAG")'
```

### Анализ SLO

```bash
# Тёплый старт
python scripts/parse_tray_metrics.py log.md --warm-start

# Холодный старт
python scripts/parse_tray_metrics.py log.md --cold-start
```

---

## Если что-то пошло не так — короткая развилка

### Видишь `…-Aux[n]` сериями

**Проблема:** Сломан single-flight

**Проверка:**
- Убедись, что `StatusItemManager.start_creation()` использует `threading.Lock()`
- Проверь, что `_is_creating` блокирует параллельные попытки

**Исправление:**
```python
# В status_item_manager.py
def start_creation(self) -> bool:
    with self._lock:
        if self._is_creating:
            return False  # Single-flight блокировка
        self._is_creating = True
        return True
```

---

### Много `OperationFailed/InvalidScene` подряд без `CIRCUIT_OPEN`

**Проблема:** Счётчик ошибок серии не инкрементится или не сбрасывается при успехе

**Проверка:**
- Убедись, что `_consecutive_failures` инкрементируется в `finish_creation(success=False)`
- Проверь, что `_consecutive_failures` сбрасывается в `finish_creation(success=True)`
- Проверь, что `CIRCUIT_OPEN_THRESHOLD = 3` достижим

**Исправление:**
```python
# В status_item_manager.py
def finish_creation(self, success: bool, ...):
    if success:
        self._consecutive_failures = 0  # Сброс при успехе
    else:
        self._consecutive_failures += 1  # Инкремент при ошибке
        if self._consecutive_failures >= self.CIRCUIT_OPEN_THRESHOLD:
            self._open_circuit(...)
```

---

### `TAL=released` до `tray.ready`

**Проблема:** TAL удержание снято раньше времени

**Проверка:**
- Убедись, что `_release_tal_hold()` вызывается **только** в `_on_tray_ready()` или по таймауту 60s
- Проверь, что нет других мест, где вызывается `enableAutomaticTermination_()`

**Исправление:**
```python
# В simple_module_coordinator.py
async def _on_tray_ready(self, event):
    self._tray_ready = True
    self._release_tal_hold()  # ТОЛЬКО здесь или по таймауту
```

---

### `RESTART_FLAG` появляется несколько раз

**Проблема:** Не атомарное read-and-remove или TTL не работает

**Проверка:**
- Убедись, что `read_and_remove()` использует `fcntl.flock()` для блокировки
- Проверь, что флаг удаляется после чтения
- Проверь, что `MAX_FLAG_AGE_SEC = 60.0` (10 минут) работает

**Исправление:**
```python
# В atomic_flag.py
def read_and_remove(self) -> Optional[RestartFlagData]:
    with open(self.flag_path, 'r+') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)  # Блокировка
        # ... чтение ...
        f.seek(0)
        f.truncate()  # Удаление содержимого
        fcntl.flock(f.fileno(), fcntl.LOCK_UN)
    self.flag_path.unlink()  # Удаление файла
```

---

## Конфигурация (для подкрутки без перекомпиляции)

Все параметры в `config/unified_config.yaml`:

```yaml
tray:
  status_item:
    circuit_open_threshold: 3
    circuit_open_duration_ms: 8000
    max_attempts_per_series: 10
    initial_backoff_ms: 800
    max_backoff_ms: 10000
    backoff_multiplier: 1.5
    jitter_percent: 0.15
    control_center_ready_timeout_sec: 10.0
    first_attempt_delay_ms: 1000
    final_timeout_ms: 60000
    background_retry_interval_sec: 45
```

---

## Критерии «Принято»

- ✅ **Тёплый старт:** tray ≤ 5 с, 0 ретраев, без Aux-лесенки
- ✅ **Холодный старт (3–5 циклов):** у 95% запусков ≤ 30 с, у 99% ≤ 60 с, без каскадного Aux
- ✅ **После выдачи разрешений и авто-перезапуска:** флаг отработал 1 раз, tray в SLO
- ✅ **При рестарте Control Center:** восстановление иконки без шквала попыток
- ✅ **Нет `_kLSApplicationWouldBeTerminatedByTALKey=1` до `tray.ready`**

---

## Быстрая диагностика

### Парсинг логов

```bash
# Все метрики
python scripts/parse_tray_metrics.py log.md

# Только тёплый старт
python scripts/parse_tray_metrics.py log.md --warm-start

# Только холодный старт
python scripts/parse_tray_metrics.py log.md --cold-start
```

### Поиск проблем

```bash
# Каскад Aux
grep -i "Aux\[" log.md | wc -l  # Должно быть 0 или минимально

# Circuit не сработал
grep -i "CIRCUIT_OPEN" log.md | wc -l  # Должно быть > 0 при ошибках

# TAL снят раньше времени
grep -i "TAL=released" log.md | head -1  # Проверить timestamp относительно tray.ready
```

---

## Следующие шаги

1. Прогнать все 5 тестов (≈15 минут)
2. Проверить логи на наличие всех метрик
3. Запустить `parse_tray_metrics.py` для анализа SLO
4. Если что-то не так — использовать развилку выше
5. При необходимости подкрутить конфиг в `unified_config.yaml`

