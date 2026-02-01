# Визуальное руководство: Централизация и синхронизация состояния микрофона

## Дата создания
2025-01-XX

## Обзор

Этот документ показывает **как правильно** централизовать и синхронизировать управление состоянием микрофона, с визуальными схемами и конкретными примерами кода.

---

## 🎯 Принцип: Единый источник истины

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ПРИНЦИП ЕДИНОГО ИСТОЧНИКА ИСТИНЫ                     │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│  ❌ ПЛОХО: Множественные источники истины (текущая проблема)           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  InputProcessingIntegration                                            │
│    └─ _recording_started = True  ✅                                     │
│                                                                          │
│  VoiceRecognitionIntegration                                            │
│    └─ _google_recording_active = False  ❌                              │
│                                                                          │
│  ApplicationStateManager                                                │
│    └─ is_microphone_active() = True  ✅                                 │
│                                                                          │
│  ❌ РАССИНХРОНИЗАЦИЯ: Разные компоненты видят разное состояние!        │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│  ✅ ХОРОШО: Единый источник истины (решение)                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ApplicationStateManager                                                │
│    └─ is_microphone_active() = True  ✅ ЕДИНЫЙ ИСТОЧНИК                │
│                                                                          │
│  InputProcessingIntegration                                            │
│    └─ Читает: state_manager.is_microphone_active()  ✅                 │
│                                                                          │
│  VoiceRecognitionIntegration                                            │
│    └─ Читает: state_manager.is_microphone_active()  ✅                 │
│                                                                          │
│  ✅ СИНХРОНИЗАЦИЯ: Все компоненты видят одно и то же состояние!        │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Схема 1: Текущая архитектура (проблема)

```
┌─────────────────────────────────────────────────────────────────────────┐
│              ТЕКУЩАЯ АРХИТЕКТУРА (МНОЖЕСТВЕННЫЕ ИСТОЧНИКИ)             │
└─────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────┐
│  InputProcessingIntegration          │
│                                      │
│  Локальные флаги:                    │
│  ├─ _recording_started = True       │  ← Источник истины #1
│  ├─ _playback_active = False        │  ← Источник истины #2
│  └─ _pending_session_id = "abc"    │
│                                      │
│  Проверки состояния:                │
│  ├─ if self._recording_started:     │  ❌ Использует локальный флаг
│  ├─ if state_manager.is_microphone_active():│  ✅ Использует state_manager
│  └─ if mic_active and self._recording_started:│  ❌ Смешанная проверка
│                                      │
│  Проблема:                           │
│  ❌ Два источника истины могут быть рассинхронизированы                │
└──────────────┬───────────────────────┘
               │
               │ События: voice.recording_start/stop
               │
               ▼
┌──────────────────────────────────────┐
│  VoiceRecognitionIntegration         │
│                                      │
│  Локальные флаги:                    │
│  ├─ _google_recording_active = True │  ← Источник истины #3
│  ├─ _user_initiated_recording = True│  ← Источник истины #4
│  └─ _playback_active = False        │  ← Источник истины #5
│                                      │
│  Проверки состояния:                │
│  ├─ if self._google_recording_active:│  ❌ Использует локальный флаг
│  └─ if state_manager.is_microphone_active():│  ✅ Использует state_manager
│                                      │
│  Проблема:                           │
│  ❌ Три источника истины могут быть рассинхронизированы                │
└──────────────┬───────────────────────┘
               │
               │ События: microphone.opened/closed
               │
               ▼
┌──────────────────────────────────────┐
│  ApplicationStateManager             │
│                                      │
│  Централизованное состояние:          │
│  ├─ _microphone_state = "active"    │  ← Источник истины #6
│  └─ _microphone_session_id = "abc"  │
│                                      │
│  Методы:                             │
│  ├─ is_microphone_active()          │  ✅ Единый источник истины
│  ├─ set_microphone_state()          │  ✅ Единый источник истины
│  └─ force_close_microphone()        │  ✅ Единый источник истины
│                                      │
│  Проблема:                           │
│  ❌ Не синхронизирован с локальными флагами!                           │
└──────────────────────────────────────┘

❌ РЕЗУЛЬТАТ: 6 источников истины, которые могут быть рассинхронизированы!
```

---

## ✅ Схема 2: Идеальная архитектура (решение)

```
┌─────────────────────────────────────────────────────────────────────────┐
│              ИДЕАЛЬНАЯ АРХИТЕКТУРА (ЕДИНЫЙ ИСТОЧНИК ИСТИНЫ)            │
└─────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────┐
│  InputProcessingIntegration          │
│                                      │
│  Локальные флаги (только для         │
│  внутренней логики, НЕ для проверок):│
│  ├─ _recording_started = True       │  ← Только для отслеживания
│  ├─ _playback_active = False        │  ← Только для отслеживания
│  └─ _pending_session_id = "abc"     │  ← Только для отслеживания
│                                      │
│  ✅ ВСЕ проверки состояния:          │
│  ├─ state_manager.is_microphone_active()│  ✅ Единый источник
│  ├─ state_manager.get_microphone_state()│  ✅ Единый источник
│  └─ НЕ используем локальные флаги для проверок!                        │
│                                      │
│  ✅ Публикация событий:              │
│  ├─ voice.recording_start → VoiceRecognitionIntegration
│  └─ voice.recording_stop → VoiceRecognitionIntegration
└──────────────┬───────────────────────┘
               │
               │ События: voice.recording_start/stop
               │
               ▼
┌──────────────────────────────────────┐
│  VoiceRecognitionIntegration         │
│                                      │
│  Локальные флаги (только для         │
│  внутренней логики, НЕ для проверок):│
│  ├─ _google_recording_active = True │  ← Только для callback защиты
│  ├─ _user_initiated_recording = True│  ← Только для callback защиты
│  └─ _playback_active = False        │  ← Только для callback защиты
│                                      │
│  ✅ ВСЕ проверки состояния:          │
│  ├─ state_manager.is_microphone_active()│  ✅ Единый источник
│  └─ state_manager.get_microphone_state()│  ✅ Единый источник
│                                      │
│  ✅ Обновление состояния:            │
│  ├─ state_manager.set_microphone_state("active", session_id)│  ✅
│  └─ state_manager.set_microphone_state("idle", None)│  ✅
│                                      │
│  ✅ Публикация событий:              │
│  ├─ microphone.opened → ApplicationStateManager
│  └─ microphone.closed → ApplicationStateManager
└──────────────┬───────────────────────┘
               │
               │ События: microphone.opened/closed
               │
               ▼
┌──────────────────────────────────────┐
│  ApplicationStateManager             │
│  (ЕДИНЫЙ ИСТОЧНИК ИСТИНЫ)            │
│                                      │
│  Централизованное состояние:          │
│  ├─ _microphone_state = "active"    │  ✅ ЕДИНЫЙ ИСТОЧНИК
│  └─ _microphone_session_id = "abc"  │  ✅ ЕДИНЫЙ ИСТОЧНИК
│                                      │
│  Методы (thread-safe):               │
│  ├─ is_microphone_active()          │  ✅ Все читают отсюда
│  ├─ get_microphone_state()          │  ✅ Все читают отсюда
│  ├─ set_microphone_state()          │  ✅ Все пишут сюда
│  └─ force_close_microphone()        │  ✅ Все пишут сюда
│                                      │
│  ✅ СИНХРОНИЗАЦИЯ:                   │
│  - Все компоненты читают отсюда      │
│  - Все компоненты пишут сюда          │
│  - Thread-safe (блокировки)          │
└──────────────────────────────────────┘

✅ РЕЗУЛЬТАТ: 1 источник истины, все компоненты синхронизированы!
```

---

## 🔄 Схема 3: Поток синхронизации при активации микрофона

```
┌─────────────────────────────────────────────────────────────────────────┐
│         ПОТОК СИНХРОНИЗАЦИИ: Активация микрофона (ИДЕАЛЬНО)             │
└─────────────────────────────────────────────────────────────────────────┘

ШАГ 1: Пользователь нажал Ctrl+N (LONG_PRESS)
│
├─► InputProcessingIntegration._handle_long_press()
│   │
│   ├─► ✅ ПРОВЕРКА: state_manager.is_microphone_active()  ← Единый источник
│   │   └─ Результат: False (микрофон не активен)
│   │
│   ├─► Локальный флаг (только для отслеживания):
│   │   └─ _recording_started = True  ← НЕ используется для проверок!
│   │
│   └─► Публикация: voice.recording_start {session_id, source="keyboard"}
│
└─────────────────────────────────────────────────────────────────────────

ШАГ 2: VoiceRecognitionIntegration получает событие
│
├─► VoiceRecognitionIntegration._on_recording_start()
│   │
│   ├─► ✅ ПРОВЕРКА: state_manager.is_microphone_active()  ← Единый источник
│   │   └─ Результат: False (микрофон не активен, можно активировать)
│   │
│   ├─► Локальный флаг (только для callback защиты):
│   │   └─ _google_recording_active = True  ← НЕ используется для проверок!
│   │
│   ├─► AVF диагностика (если нужно)
│   │   └─ AVF активируется и деактивируется
│   │
│   ├─► Google Speech Recognition активация
│   │   └─ listen_in_background(microphone, callback)
│   │
│   └─► ✅ ОБНОВЛЕНИЕ: state_manager.set_microphone_state("active", session_id)
│       └─ Это ЕДИНСТВЕННОЕ место, где обновляется состояние!
│
└─────────────────────────────────────────────────────────────────────────

ШАГ 3: ApplicationStateManager обновляет состояние
│
├─► ApplicationStateManager.set_microphone_state("active", session_id)
│   │
│   ├─► Thread-safe обновление (блокировка):
│   │   ├─ _microphone_state = "active"  ✅
│   │   └─ _microphone_session_id = session_id  ✅
│   │
│   └─► Логирование: "🔄 [MIC_STATE] idle → active"
│
└─────────────────────────────────────────────────────────────────────────

ШАГ 4: Все компоненты видят обновленное состояние
│
├─► InputProcessingIntegration
│   └─✅ state_manager.is_microphone_active() = True  ← Синхронизировано!
│
├─► VoiceRecognitionIntegration
│   └─✅ state_manager.is_microphone_active() = True  ← Синхронизировано!
│
└─► Другие компоненты
    └─✅ state_manager.is_microphone_active() = True  ← Синхронизировано!

✅ РЕЗУЛЬТАТ: Все компоненты видят одно и то же состояние!
```

---

## 🔄 Схема 4: Поток синхронизации при деактивации микрофона

```
┌─────────────────────────────────────────────────────────────────────────┐
│        ПОТОК СИНХРОНИЗАЦИИ: Деактивация микрофона (ИДЕАЛЬНО)            │
└─────────────────────────────────────────────────────────────────────────┘

ШАГ 1: Пользователь отпустил Ctrl+N (RELEASE)
│
├─► InputProcessingIntegration._handle_key_release()
│   │
│   ├─► ✅ ПРОВЕРКА: state_manager.is_microphone_active()  ← Единый источник
│   │   └─ Результат: True (микрофон активен, нужно остановить)
│   │
│   └─► Публикация: voice.recording_stop {session_id, source="keyboard"}
│
└─────────────────────────────────────────────────────────────────────────

ШАГ 2: VoiceRecognitionIntegration получает событие
│
├─► VoiceRecognitionIntegration._on_recording_stop()
│   │
│   ├─► ✅ ПРОВЕРКА: state_manager.is_microphone_active()  ← Единый источник
│   │   └─ Результат: True (микрофон активен, нужно остановить)
│   │
│   ├─► Локальный флаг (только для callback защиты):
│   │   └─ _google_recording_active = False  ← НЕ используется для проверок!
│   │
│   ├─► Остановка Google Speech Recognition
│   │   └─ _google_stop_listening()
│   │
│   └─► ✅ ОБНОВЛЕНИЕ: state_manager.set_microphone_state("idle", None)
│       └─ Это ЕДИНСТВЕННОЕ место, где обновляется состояние!
│
└─────────────────────────────────────────────────────────────────────────

ШАГ 3: ApplicationStateManager обновляет состояние
│
├─► ApplicationStateManager.set_microphone_state("idle", None)
│   │
│   ├─► Thread-safe обновление (блокировка):
│   │   ├─ _microphone_state = "idle"  ✅
│   │   └─ _microphone_session_id = None  ✅
│   │
│   └─► Логирование: "🔄 [MIC_STATE] active → idle"
│
└─────────────────────────────────────────────────────────────────────────

ШАГ 4: Все компоненты видят обновленное состояние
│
├─► InputProcessingIntegration
│   └─✅ state_manager.is_microphone_active() = False  ← Синхронизировано!
│
├─► VoiceRecognitionIntegration
│   └─✅ state_manager.is_microphone_active() = False  ← Синхронизировано!
│
└─► Другие компоненты
    └─✅ state_manager.is_microphone_active() = False  ← Синхронизировано!

✅ РЕЗУЛЬТАТ: Все компоненты видят одно и то же состояние!
```

---

## 🔧 Схема 5: Конкретные изменения в коде

### Изменение 1: InputProcessingIntegration._on_playback_finished()

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ❌ ТЕКУЩИЙ КОД (проблема):                                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  async def _on_playback_finished(self, event):                          │
│      mic_active = self.state_manager.is_microphone_active()  ✅         │
│      if mic_active and self._recording_started:  ❌ Смешанная проверка  │
│          # _recording_started = False (локальный флаг)                  │
│          # НО mic_active = True (state_manager)                        │
│          return  # ❌ ВЫХОДИМ, НЕ ЗАКРЫВАЯ МИКРОФОН!                    │
│                                                                          │
│  ❌ ПРОБЛЕМА: Использует два источника истины                           │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│  ✅ ИСПРАВЛЕННЫЙ КОД (решение):                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  async def _on_playback_finished(self, event):                          │
│      # ✅ ТОЛЬКО единый источник истины                                  │
│      mic_active = self.state_manager.is_microphone_active()            │
│                                                                          │
│      if mic_active:  # ✅ Только state_manager                           │
│          logger.warning("⚠️ PLAYBACK: микрофон активен - принудительно закрываем")
│          # ✅ Используем существующий метод (единый источник истины)    │
│          self.state_manager.force_close_microphone(reason="playback_completed")
│          # ✅ Публикуем событие для синхронизации                       │
│          await self._publish_recording_stop_with_debounce({...})
│          # ✅ Ждём закрытия микрофона                                  │
│          await self._wait_for_mic_closed_with_timeout(...)              │
│                                                                          │
│      # ✅ Локальный флаг _recording_started используется только для     │
│      #    отслеживания публикации voice.recording_start, НЕ для проверок│
│      if mic_active and self._recording_started:                         │
│          # НЕ сбрасываем сессию - это правильно                         │
│          return                                                          │
│                                                                          │
│  ✅ РЕШЕНИЕ: Использует только единый источник истины                   │
└─────────────────────────────────────────────────────────────────────────┘
```

### Изменение 2: VoiceRecognitionIntegration._on_recording_start()

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ❌ ТЕКУЩИЙ КОД (проблема):                                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  async def _on_recording_start(self, event):                            │
│      # ❌ ПРОБЛЕМА: Проверка AVF выполняется только один раз            │
│      if avf_engine.is_input_active:                                     │
│          logger.warning("⚠️ AVF все еще активен...")                    │
│          await asyncio.sleep(0.5)  # Одна попытка                       │
│          if avf_engine.is_input_active:                                 │
│              logger.error("❌ AVF все еще активен...")                   │
│              # ❌ ПРОБЛЕМА: Продолжаем работу!                          │
│                                                                          │
│      # ❌ ПРОБЛЕМА: Разрешения могут быть пропущены                     │
│      try:                                                               │
│          mic_permission = permission_checker.check_microphone_permission()
│          if mic_permission != "granted":                                │
│              raise RuntimeError("...")                                  │
│      except Exception as perm_error:                                     │
│          logger.warning("⚠️ Не удалось проверить разрешения...")        │
│          # ❌ ПРОБЛЕМА: Продолжаем работу!                             │
│                                                                          │
│  ❌ ПРОБЛЕМА: Нет гарантии деактивации AVF и проверки разрешений        │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│  ✅ ИСПРАВЛЕННЫЙ КОД (решение):                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  async def _on_recording_start(self, event):                            │
│      # ✅ ГАРАНТИРОВАННАЯ деактивация AVF (5 попыток)                 │
│      if self._use_avf and self._avf_engine is not None:                │
│          # ... AVF диагностика ...                                      │
│          max_avf_check_attempts = 5                                     │
│          for attempt in range(max_avf_check_attempts):                   │
│              if avf_engine.is_input_active:                             │
│                  logger.warning(f"⚠️ AVF все еще активен (попытка {attempt+1})")
│                  await asyncio.sleep(0.2)                               │
│              else:                                                       │
│                  logger.info(f"✅ AVF полностью деактивирован")        │
│                  break                                                  │
│          else:                                                           │
│              # ✅ ПРОБЛЕМА: Выбрасываем исключение, не продолжаем!      │
│              raise RuntimeError("AVF not deactivated after all attempts")
│                                                                          │
│      # ✅ ОБЯЗАТЕЛЬНАЯ проверка разрешений (ошибка → исключение)       │
│      try:                                                               │
│          mic_permission = permission_checker.check_microphone_permission()
│          if mic_permission != "granted":                                │
│              raise RuntimeError(f"Microphone permission not granted: {mic_permission}")
│      except RuntimeError:                                                │
│          raise  # ✅ Пробрасываем RuntimeError                          │
│      except Exception as perm_error:                                     │
│          # ✅ ПРОБЛЕМА: Выбрасываем исключение, не продолжаем!         │
│          raise RuntimeError(f"Permission check failed: {perm_error}") from perm_error
│                                                                          │
│      # ✅ ОБНОВЛЕНИЕ: state_manager.set_microphone_state("active", session_id)
│      #    Это ЕДИНСТВЕННОЕ место, где обновляется состояние!           │
│      self.state_manager.set_microphone_state("active", session_id=str(session_id))
│                                                                          │
│  ✅ РЕШЕНИЕ: Гарантированная деактивация AVF и обязательная проверка     │
└─────────────────────────────────────────────────────────────────────────┘
```

### Изменение 3: InputProcessingIntegration._handle_long_press()

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ❌ ТЕКУЩИЙ КОД (проблема):                                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  async def _handle_long_press(self, event):                             │
│      if current_mode == AppMode.PROCESSING:                             │
│          if self._playback_active:  ❌ Локальный флаг                   │
│              logger.warning("🔒 LONG_PRESS blocked...")                 │
│              return  # ❌ БЛОКИРУЕМ ВСЕ активации!                     │
│                                                                          │
│  ❌ ПРОБЛЕМА: Блокирует все активации, включая пользовательские         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│  ✅ ИСПРАВЛЕННЫЙ КОД (решение):                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  async def _handle_long_press(self, event):                             │
│      # ✅ Используем gateway для принятия решения                       │
│      from integration.core.gateways.audio_gateways import decide_allow_shortcut_during_processing
│      from integration.core.selectors import create_snapshot_from_state_manager
│                                                                          │
│      snapshot = create_snapshot_from_state_manager(self.state_manager)  │
│      decision = decide_allow_shortcut_during_processing(snapshot, source="keyboard")
│                                                                          │
│      if decision == Decision.ABORT:                                     │
│          logger.warning("🔒 LONG_PRESS blocked by gateway")             │
│          return                                                          │
│                                                                          │
│      # ✅ Разрешаем активацию через Shortcut для прерывания             │
│      logger.info("✅ LONG_PRESS: разрешена активация микрофона")         │
│                                                                          │
│      # ✅ Принудительное закрытие микрофона перед новой записью         │
│      mic_active = self.state_manager.is_microphone_active()  ✅ Единый источник
│      if mic_active:                                                      │
│          logger.warning("⚠️ LONG_PRESS: микрофон активен - принудительно закрываем")
│          await self._publish_recording_stop_with_debounce({...})         │
│          await self._wait_for_mic_closed_with_timeout(...)              │
│                                                                          │
│  ✅ РЕШЕНИЕ: Использует gateway для принятия решения, единый источник   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 Правила централизации и синхронизации

### Правило 1: Единый источник истины

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ✅ ПРАВИЛО: ApplicationStateManager - единственный источник истины    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ЧТЕНИЕ состояния:                                                      │
│  ✅ state_manager.is_microphone_active()                                │
│  ✅ state_manager.get_microphone_state()                                │
│                                                                          │
│  ЗАПИСЬ состояния:                                                      │
│  ✅ state_manager.set_microphone_state("active", session_id)            │
│  ✅ state_manager.set_microphone_state("idle", None)                   │
│  ✅ state_manager.force_close_microphone(reason)                       │
│                                                                          │
│  ❌ НЕ используем локальные флаги для проверок состояния!              │
└─────────────────────────────────────────────────────────────────────────┘
```

### Правило 2: Локальные флаги только для внутренней логики

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ✅ ПРАВИЛО: Локальные флаги НЕ используются для проверок состояния    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  InputProcessingIntegration:                                            │
│  ├─ _recording_started  ← Только для отслеживания публикации           │
│  ├─ _playback_active    ← Только для отслеживания воспроизведения      │
│  └─ НЕ используется для проверок состояния микрофона!                  │
│                                                                          │
│  VoiceRecognitionIntegration:                                            │
│  ├─ _google_recording_active  ← Только для защиты callback             │
│  ├─ _user_initiated_recording  ← Только для защиты callback           │
│  └─ НЕ используется для проверок состояния микрофона!                  │
│                                                                          │
│  ✅ ВСЕ проверки состояния через state_manager!                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Правило 3: Синхронизация при каждом изменении

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ✅ ПРАВИЛО: Обновляем state_manager при каждом изменении состояния    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  При активации микрофона:                                               │
│  ├─ VoiceRecognitionIntegration._on_recording_start()                   │
│  └─✅ state_manager.set_microphone_state("active", session_id)          │
│                                                                          │
│  При деактивации микрофона:                                             │
│  ├─ VoiceRecognitionIntegration._on_recording_stop()                    │
│  └─✅ state_manager.set_microphone_state("idle", None)                 │
│                                                                          │
│  При принудительном закрытии:                                           │
│  ├─ InputProcessingIntegration._on_playback_finished()                  │
│  └─✅ state_manager.force_close_microphone(reason)                     │
│                                                                          │
│  ✅ ВСЕ изменения состояния через state_manager!                        │
└─────────────────────────────────────────────────────────────────────────┘
```

### Правило 4: Thread-safe операции

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ✅ ПРАВИЛО: ApplicationStateManager использует блокировки              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ApplicationStateManager:                                               │
│  ├─ _microphone_lock = threading.Lock()  ✅ Thread-safe                │
│  ├─ set_microphone_state()  ✅ Использует блокировку                    │
│  ├─ is_microphone_active()  ✅ Использует блокировку                   │
│  └─ force_close_microphone()  ✅ Использует блокировку                │
│                                                                          │
│  ✅ ВСЕ операции thread-safe!                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Чек-лист централизации и синхронизации

### Перед изменением кода:

- [ ] Определить, где используется состояние микрофона
- [ ] Заменить все проверки локальных флагов на `state_manager.is_microphone_active()`
- [ ] Убедиться, что все изменения состояния идут через `state_manager.set_microphone_state()`
- [ ] Проверить, что локальные флаги используются только для внутренней логики

### После изменения кода:

- [ ] Все проверки состояния через `state_manager.is_microphone_active()`
- [ ] Все изменения состояния через `state_manager.set_microphone_state()`
- [ ] Локальные флаги не используются для проверок состояния
- [ ] Thread-safe операции (блокировки в state_manager)

---

## 📊 Сравнительная таблица: До и После

| Аспект | До (проблема) | После (решение) |
|--------|---------------|-----------------|
| **Источник истины** | 6 источников (локальные флаги + state_manager) | 1 источник (state_manager) |
| **Проверки состояния** | Смешанные (локальные флаги + state_manager) | Только state_manager |
| **Изменения состояния** | Разбросаны по коду | Только через state_manager |
| **Синхронизация** | Отсутствует (может быть рассинхронизация) | Гарантирована (thread-safe) |
| **Локальные флаги** | Используются для проверок | Только для внутренней логики |

---

## Связанные документы

- `Docs/SYNC_PROBLEM_VISUAL_DIAGRAM.md` — визуальная схема проблемы рассинхронизации
- `Docs/SOLUTIONS_IMPLEMENTATION_PLAN.md` — план реализации решений
- `Docs/ROOT_CAUSE_ANALYSIS.md` — анализ корневой причины

