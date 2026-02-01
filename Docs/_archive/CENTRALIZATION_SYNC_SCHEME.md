# Схема централизации и синхронизации состояния микрофона

## Дата создания
2025-01-XX

## Обзор

Этот документ содержит визуальные схемы, показывающие **как правильно** централизовать и синхронизировать управление состоянием микрофона.

---

## 🎯 Принцип: Единый источник истины

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ПРИНЦИП ЕДИНОГО ИСТОЧНИКА ИСТИНЫ                      │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│         ApplicationStateManager (ЕДИНЫЙ ИСТОЧНИК ИСТИНЫ)               │
│                                                                          │
│  ✅ ЧТЕНИЕ состояния:                                                   │
│     - is_microphone_active()  ← Все компоненты читают отсюда           │
│     - get_microphone_state()  ← Все компоненты читают отсюда           │
│                                                                          │
│  ✅ ЗАПИСЬ состояния:                                                   │
│     - set_microphone_state()  ← Все компоненты пишут сюда               │
│     - force_close_microphone()  ← Принудительное закрытие              │
│                                                                          │
│  ✅ Thread-safe:                                                        │
│     - _microphone_lock (threading.Lock)                                 │
│     - Атомарные операции                                                │
└─────────────────────────────────────────────────────────────────────────┘
           ▲                    ▲                    ▲
           │                    │                    │
           │                    │                    │
           │  ✅ ЧИТАЮТ         │  ✅ ЧИТАЮТ         │  ✅ ЧИТАЮТ
           │                    │                    │
┌──────────┴──────────┐  ┌──────┴──────────┐  ┌──────┴──────────┐
│ InputProcessing      │  │ VoiceRecognition│  │ Другие          │
│ Integration          │  │ Integration    │  │ интеграции      │
│                      │  │                │  │                 │
│ ❌ НЕ используют:   │  │ ❌ НЕ используют:│  │ ❌ НЕ используют:│
│ _recording_started   │  │ _google_recording│  │ локальные флаги │
│ для проверок         │  │ _active для      │  │ для проверок    │
│                      │  │ проверок         │  │                 │
│ ✅ ТОЛЬКО для:       │  │ ✅ ТОЛЬКО для:   │  │ ✅ ТОЛЬКО для:  │
│ внутренней логики    │  │ внутренней логики│  │ внутренней логики│
└──────────────────────┘  └─────────────────┘  └─────────────────┘
```

---

## 🔄 Схема синхронизации: Как это работает

### 1. Активация микрофона (правильная синхронизация)

```
┌─────────────────────────────────────────────────────────────────────────┐
│  СЦЕНАРИЙ: Пользователь нажал Ctrl+N → Активация микрофона              │
└─────────────────────────────────────────────────────────────────────────┘

ШАГ 1: Пользователь нажал Ctrl+N (LONG_PRESS)
│
├─► InputProcessingIntegration._handle_long_press()
│   │
│   ├─► ✅ ПРОВЕРКА: state_manager.is_microphone_active()
│   │   └─► Если True → принудительно закрыть через state_manager
│   │
│   ├─► _recording_started = True  ✅ (только для внутренней логики)
│   │
│   └─► Публикует: voice.recording_start {session_id, source="keyboard"}
│
├─► VoiceRecognitionIntegration._on_recording_start()
│   │
│   ├─► _google_recording_active = True  ✅ (только для внутренней логики)
│   │
│   ├─► ✅ КРИТИЧНО: Синхронизация с state_manager
│   │   └─► state_manager.set_microphone_state("active", session_id)
│   │       └─► _microphone_state = "active"  ✅ (ЕДИНЫЙ ИСТОЧНИК ИСТИНЫ)
│   │
│   └─► Публикует: microphone.opened {session_id}
│
└─► ✅ РЕЗУЛЬТАТ: Все компоненты видят одинаковое состояние
    └─► state_manager.is_microphone_active() = True  ✅
    └─► _recording_started = True  ✅ (локальный флаг, не для проверок)
    └─► _google_recording_active = True  ✅ (локальный флаг, не для проверок)
```

### 2. Деактивация микрофона (правильная синхронизация)

```
┌─────────────────────────────────────────────────────────────────────────┐
│  СЦЕНАРИЙ: Пользователь отпустил Ctrl+N → Деактивация микрофона        │
└─────────────────────────────────────────────────────────────────────────┘

ШАГ 1: Пользователь отпустил Ctrl+N (RELEASE)
│
├─► InputProcessingIntegration._handle_key_release()
│   │
│   ├─► ✅ ПРОВЕРКА: state_manager.is_microphone_active()
│   │   └─► was_recording = state_manager.is_microphone_active()  ✅
│   │
│   └─► Публикует: voice.recording_stop {session_id, source="keyboard"}
│
├─► VoiceRecognitionIntegration._on_recording_stop()
│   │
│   ├─► _google_recording_active = False  ✅ (локальный флаг сброшен)
│   │
│   ├─► ✅ КРИТИЧНО: Синхронизация с state_manager
│   │   └─► state_manager.set_microphone_state("idle", session_id=None)
│   │       └─► _microphone_state = "idle"  ✅ (ЕДИНЫЙ ИСТОЧНИК ИСТИНЫ)
│   │
│   └─► Публикует: microphone.closed {session_id}
│
├─► InputProcessingIntegration._on_playback_finished()
│   │
│   ├─► ✅ ПРОВЕРКА: state_manager.is_microphone_active()
│   │   └─► mic_active = state_manager.is_microphone_active()  ✅
│   │
│   └─► Если mic_active == True → принудительно закрыть через state_manager
│
└─► ✅ РЕЗУЛЬТАТ: Все компоненты видят одинаковое состояние
    └─► state_manager.is_microphone_active() = False  ✅
    └─► _recording_started = False  ✅ (локальный флаг, не для проверок)
    └─► _google_recording_active = False  ✅ (локальный флаг, не для проверок)
```

---

## 📊 Сравнение: Текущая vs Идеальная архитектура

### Текущая архитектура (ПРОБЛЕМА):

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ТЕКУЩАЯ АРХИТЕКТУРА (ПРОБЛЕМА)                        │
└─────────────────────────────────────────────────────────────────────────┘

InputProcessingIntegration
│
├─► _recording_started = True  ❌ (используется для проверок)
│
├─► ❌ ПРОВЕРКА: if mic_active and self._recording_started:
│   └─► Проблема: Два источника истины могут быть рассинхронизированы
│
└─► mic_active = state_manager.is_microphone_active()  ❌ (один из источников)

─────────────────────────────────────────────────────────────────────────

VoiceRecognitionIntegration
│
├─► _google_recording_active = True  ❌ (используется для проверок)
│
├─► ❌ ПРОВЕРКА: if not self._google_recording_active:
│   └─► Проблема: Локальный флаг может быть рассинхронизирован
│
└─► state_manager.set_microphone_state("active")  ❌ (не всегда синхронизировано)

─────────────────────────────────────────────────────────────────────────

ApplicationStateManager
│
└─► _microphone_state = "active"  ❌ (может быть рассинхронизировано)
```

### Идеальная архитектура (РЕШЕНИЕ):

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ИДЕАЛЬНАЯ АРХИТЕКТУРА (РЕШЕНИЕ)                      │
└─────────────────────────────────────────────────────────────────────────┘

InputProcessingIntegration
│
├─► _recording_started = True  ✅ (только для внутренней логики)
│
├─► ✅ ПРОВЕРКА: if state_manager.is_microphone_active():
│   └─► Единый источник истины - нет рассинхронизации
│
└─► ✅ ВСЕ проверки через: state_manager.is_microphone_active()

─────────────────────────────────────────────────────────────────────────

VoiceRecognitionIntegration
│
├─► _google_recording_active = True  ✅ (только для внутренней логики)
│
├─► ✅ ПРОВЕРКА: if state_manager.is_microphone_active():
│   └─► Единый источник истины - нет рассинхронизации
│
└─► ✅ ВСЕ проверки через: state_manager.is_microphone_active()

─────────────────────────────────────────────────────────────────────────

ApplicationStateManager (ЕДИНЫЙ ИСТОЧНИК ИСТИНЫ)
│
├─► ✅ set_microphone_state("active", session_id)  ← Все пишут сюда
│
├─► ✅ is_microphone_active()  ← Все читают отсюда
│
└─► ✅ Thread-safe: _microphone_lock гарантирует синхронизацию
```

---

## 🔧 Конкретные изменения в коде

### Изменение 1: InputProcessingIntegration._on_playback_finished()

**Текущий код (ПРОБЛЕМА):**
```python
# ❌ ПРОБЛЕМА: Использует два источника истины
mic_active = self.state_manager.is_microphone_active()  # Источник 1
if mic_active and self._recording_started:  # Источник 2 (локальный флаг)
    return  # НЕ закрывает микрофон, если _recording_started = False
```

**Исправленный код (РЕШЕНИЕ):**
```python
# ✅ РЕШЕНИЕ: Использует только единый источник истины
mic_active = self.state_manager.is_microphone_active()  # Единый источник
if mic_active:
    # ✅ КРИТИЧНО: Принудительно закрываем микрофон через state_manager
    logger.warning(f"⚠️ PLAYBACK: микрофон активен после playback.completed - принудительно закрываем")
    self.state_manager.force_close_microphone(reason="playback_completed")
    await self._publish_recording_stop_with_debounce({
        "source": "playback_finished",
        "timestamp": time.time(),
        "session_id": None,
    })
    await self._wait_for_mic_closed_with_timeout(timeout=1.0, source="playback_finished")

# ✅ _recording_started используется только для внутренней логики, не для проверок
if mic_active and self._recording_started:
    # Это новая запись, начатая во время playback - НЕ сбрасываем сессию
    return
```

### Изменение 2: InputProcessingIntegration._handle_long_press()

**Текущий код (ПРОБЛЕМА):**
```python
# ❌ ПРОБЛЕМА: Блокирует все активации на основе локального флага
if self._playback_active:  # Локальный флаг
    return  # Блокирует активацию
```

**Исправленный код (РЕШЕНИЕ):**
```python
# ✅ РЕШЕНИЕ: Использует gateway для принятия решения
from integration.core.gateways.audio_gateways import decide_allow_shortcut_during_processing
from integration.core.selectors import create_snapshot_from_state_manager

snapshot = create_snapshot_from_state_manager(self.state_manager)
decision = decide_allow_shortcut_during_processing(snapshot, source="keyboard")

if decision == Decision.ABORT:
    logger.warning("🔒 LONG_PRESS blocked by gateway decision")
    return

# ✅ Проверка состояния через единый источник истины
mic_active = self.state_manager.is_microphone_active()
if mic_active:
    # Принудительно закрываем через state_manager
    self.state_manager.force_close_microphone(reason="long_press_cleanup")
    await self._publish_recording_stop_with_debounce({...})
```

### Изменение 3: VoiceRecognitionIntegration._on_recording_start()

**Текущий код (ПРОБЛЕМА):**
```python
# ❌ ПРОБЛЕМА: AVF деактивация проверяется только один раз
if avf_engine.is_input_active:
    await asyncio.sleep(0.5)
    if avf_engine.is_input_active:
        logger.error("❌ AVF все еще активен...")
        # ❌ ПРОБЛЕМА: Продолжаем работу!
```

**Исправленный код (РЕШЕНИЕ):**
```python
# ✅ РЕШЕНИЕ: Гарантированная деактивация AVF (5 попыток)
max_avf_check_attempts = 5
for attempt in range(max_avf_check_attempts):
    if hasattr(self._avf_engine, 'is_input_active') and self._avf_engine.is_input_active:
        logger.warning(f"⚠️ [AVF] AVF все еще активен (попытка {attempt+1}/{max_avf_check_attempts})")
        await asyncio.sleep(0.2)
    else:
        logger.info(f"✅ [AVF] AVF полностью деактивирован (попытка {attempt+1})")
        break
else:
    logger.error("❌ [AVF] AVF не деактивирован после всех попыток")
    raise RuntimeError("AVF not deactivated after all attempts")

# ✅ КРИТИЧНО: Синхронизация с state_manager ПЕРЕД активацией Google
self.state_manager.set_microphone_state("active", session_id=str(session_id), reason="google_recording_started")
await self.event_bus.publish("microphone.opened", {"session_id": session_id})
```

---

## 🔄 Схема потока синхронизации

```
┌─────────────────────────────────────────────────────────────────────────┐
│              ПОТОК СИНХРОНИЗАЦИИ СОСТОЯНИЯ МИКРОФОНА                     │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│  ЭТАП 1: Активация микрофона                                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  InputProcessingIntegration                                             │
│    └─► Публикует: voice.recording_start                                │
│                                                                          │
│  VoiceRecognitionIntegration                                            │
│    ├─► _google_recording_active = True  ✅ (локальный флаг)            │
│    │                                                                     │
│    └─► ✅ СИНХРОНИЗАЦИЯ:                                                │
│        state_manager.set_microphone_state("active", session_id)        │
│        └─► _microphone_state = "active"  ✅ (ЕДИНЫЙ ИСТОЧНИК ИСТИНЫ)   │
│                                                                          │
│  ApplicationStateManager                                                │
│    └─► _microphone_state = "active"  ✅ (синхронизировано)             │
│                                                                          │
│  ✅ РЕЗУЛЬТАТ: Все компоненты видят одинаковое состояние                │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│  ЭТАП 2: Проверка состояния (все компоненты)                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  InputProcessingIntegration                                             │
│    └─► ✅ ПРОВЕРКА: state_manager.is_microphone_active()  ✅ True       │
│                                                                          │
│  VoiceRecognitionIntegration                                            │
│    └─► ✅ ПРОВЕРКА: state_manager.is_microphone_active()  ✅ True       │
│                                                                          │
│  Другие интеграции                                                      │
│    └─► ✅ ПРОВЕРКА: state_manager.is_microphone_active()  ✅ True       │
│                                                                          │
│  ✅ РЕЗУЛЬТАТ: Все компоненты получают одинаковый результат             │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│  ЭТАП 3: Деактивация микрофона                                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  InputProcessingIntegration                                             │
│    └─► Публикует: voice.recording_stop                                 │
│                                                                          │
│  VoiceRecognitionIntegration                                            │
│    ├─► _google_recording_active = False  ✅ (локальный флаг)            │
│    │                                                                     │
│    └─► ✅ СИНХРОНИЗАЦИЯ:                                                │
│        state_manager.set_microphone_state("idle", session_id=None)      │
│        └─► _microphone_state = "idle"  ✅ (ЕДИНЫЙ ИСТОЧНИК ИСТИНЫ)     │
│                                                                          │
│  ApplicationStateManager                                                │
│    └─► _microphone_state = "idle"  ✅ (синхронизировано)               │
│                                                                          │
│  ✅ РЕЗУЛЬТАТ: Все компоненты видят одинаковое состояние                │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 Правила синхронизации

### Правило 1: Единый источник истины

```
✅ ПРАВИЛО: ApplicationStateManager - единственный источник истины для состояния микрофона

✅ ЧТЕНИЕ состояния:
   - Все компоненты читают через: state_manager.is_microphone_active()
   - Все компоненты читают через: state_manager.get_microphone_state()

✅ ЗАПИСЬ состояния:
   - Все компоненты пишут через: state_manager.set_microphone_state()
   - Принудительное закрытие: state_manager.force_close_microphone()

❌ ЗАПРЕЩЕНО:
   - Использовать локальные флаги для проверок состояния
   - Прямой доступ к _microphone_state (только через методы)
```

### Правило 2: Локальные флаги только для внутренней логики

```
✅ ПРАВИЛО: Локальные флаги (_recording_started, _google_recording_active) 
            используются ТОЛЬКО для внутренней логики, НЕ для проверок состояния

✅ ИСПОЛЬЗОВАНИЕ:
   - _recording_started: отслеживание публикации voice.recording_start
   - _google_recording_active: защита callback от обработки после остановки
   - _playback_active: отслеживание воспроизведения

❌ ЗАПРЕЩЕНО:
   - Использовать локальные флаги для проверок состояния микрофона
   - if mic_active and self._recording_started:  ❌ (неправильно)
   - if state_manager.is_microphone_active():  ✅ (правильно)
```

### Правило 3: Синхронизация при каждом изменении

```
✅ ПРАВИЛО: При каждом изменении состояния микрофона ОБЯЗАТЕЛЬНО 
            синхронизировать с ApplicationStateManager

✅ ПОСЛЕДОВАТЕЛЬНОСТЬ:
   1. Изменить локальный флаг (если нужен для внутренней логики)
   2. Синхронизировать с state_manager: set_microphone_state()
   3. Публиковать событие: microphone.opened/closed

❌ ЗАПРЕЩЕНО:
   - Изменять локальный флаг без синхронизации с state_manager
   - Пропускать синхронизацию при ошибках
```

### Правило 4: Thread-safe операции

```
✅ ПРАВИЛО: Все операции с состоянием микрофона должны быть thread-safe

✅ ApplicationStateManager:
   - Использует _microphone_lock (threading.Lock)
   - Все методы thread-safe

✅ ИНТЕГРАЦИИ:
   - Используют методы state_manager (уже thread-safe)
   - Не требуют дополнительных блокировок
```

---

## 🎯 Чек-лист централизации

### Перед изменением кода:

- [ ] Определить, какие локальные флаги используются для проверок состояния
- [ ] Заменить все проверки на `state_manager.is_microphone_active()`
- [ ] Оставить локальные флаги только для внутренней логики

### При изменении состояния:

- [ ] Изменить локальный флаг (если нужен для внутренней логики)
- [ ] Синхронизировать с `state_manager.set_microphone_state()`
- [ ] Публиковать событие `microphone.opened/closed`

### При проверке состояния:

- [ ] Использовать только `state_manager.is_microphone_active()`
- [ ] НЕ использовать локальные флаги для проверок
- [ ] НЕ использовать прямые проверки `_microphone_state`

---

## 📊 Сравнительная таблица: До и После

| Аспект | До (проблема) | После (решение) |
|--------|---------------|-----------------|
| **Источник истины** | Множественные (локальные флаги + state_manager) | Единый (ApplicationStateManager) |
| **Проверки состояния** | `if mic_active and self._recording_started:` | `if state_manager.is_microphone_active():` |
| **Синхронизация** | Отсутствует (может быть рассинхронизация) | Гарантирована (при каждом изменении) |
| **Локальные флаги** | Используются для проверок состояния | Только для внутренней логики |
| **Thread-safety** | Не гарантирована | Гарантирована (через _microphone_lock) |

---

## 🎯 Выводы

### Как правильно централизовать:

1. **ApplicationStateManager как единый источник истины:**
   - Все компоненты читают состояние через `state_manager.is_microphone_active()`
   - Все компоненты пишут состояние через `state_manager.set_microphone_state()`

2. **Локальные флаги только для внутренней логики:**
   - `_recording_started`, `_google_recording_active` - только для внутренней логики
   - НЕ используются для проверок состояния

3. **Синхронизация при каждом изменении:**
   - При изменении состояния ОБЯЗАТЕЛЬНО синхронизировать с state_manager
   - Публиковать события `microphone.opened/closed` после синхронизации

4. **Thread-safe операции:**
   - Все операции через методы state_manager (уже thread-safe)
   - Не требуются дополнительные блокировки

---

## Связанные документы

- `Docs/SYNC_PROBLEM_VISUAL_DIAGRAM.md` — визуальная схема проблемы рассинхронизации
- `Docs/SOLUTIONS_IMPLEMENTATION_PLAN.md` — план реализации решений
- `Docs/ROOT_CAUSE_ANALYSIS.md` — анализ корневой причины

