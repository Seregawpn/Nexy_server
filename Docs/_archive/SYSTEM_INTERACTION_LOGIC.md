# Логика взаимодействия компонентов системы

## Дата создания
2025-12-02

## Цель
Документировать правильную логику взаимодействия между компонентами системы:
- Input (клавиатура)
- Mode Management (режимы приложения)
- Tray Icon (иконка в меню-баре)
- Signals (аудио сигналы)

---

## 1. Общая архитектура взаимодействия

### 1.1 Цепочка событий

```
Пользователь (Ctrl+N)
    ↓
QuartzKeyboardMonitor → KeyEvent (LONG_PRESS / SHORT_PRESS)
    ↓
InputProcessingIntegration
    ↓
EventBus: mode.request / playback.cancelled / voice.recording_start
    ↓
ModeManagementIntegration → ApplicationStateManager
    ↓
EventBus: app.mode_changed
    ↓
TrayControllerIntegration (иконка) + SignalIntegration (сигналы)
```

---

## 2. Детальная логика компонентов

### 2.1 InputProcessingIntegration

**Ответственность:**
- Обработка клавиатурных событий (LONG_PRESS, SHORT_PRESS, RELEASE)
- Координация перехода в режимы LISTENING/PROCESSING/SLEEPING
- Управление состоянием записи (_input_state, _pending_session_id)

**Ключевые методы:**

#### `_handle_long_press(event: KeyEvent)`
**Логика:**
1. Проверка готовности к записи (`_can_start_recording()`)
2. Если `current_mode == PROCESSING`:
   - **СНАЧАЛА** публикует `mode.request(LISTENING, priority=EventPriority.HIGH)`
   - **ЗАТЕМ** публикует `playback.cancelled` для прерывания воспроизведения
   - Это гарантирует, что режим изменится на LISTENING до обработки прерывания
3. Публикует `voice.recording_start` для начала записи
4. Ожидает `voice.mic_opened` через `_wait_for_mic_opened()`
5. После открытия микрофона переходит в состояние `LISTENING`

**Критично:**
- `mode.request(LISTENING)` должен публиковаться **ПЕРЕД** `playback.cancelled`
- `priority=EventPriority.HIGH` гарантирует приоритетную обработку
- `session_id` должен быть установлен до публикации событий

#### `_handle_short_press(event: KeyEvent)`
**Логика:**
1. Если `current_mode == PROCESSING`:
   - Публикует `playback.cancelled` для прерывания воспроизведения
   - Публикует `interrupt.request` для обработки прерывания
   - Сбрасывает `_input_state = IDLE`, `_pending_session_id = None`
   - Публикует `mode.request(SLEEPING, source='input_processing')`
2. Если `current_mode == SLEEPING` и `_playback_active == True`:
   - Публикует `mode.request(PROCESSING)` для отображения иконки
   - Затем публикует `playback.cancelled` для прерывания

**Критично:**
- При прерывании PROCESSING режим должен перейти в SLEEPING
- Иконка должна обновиться корректно

---

### 2.2 ModeManagementIntegration

**Ответственность:**
- Централизованное управление переходами между режимами
- Валидация переходов через `ModeController`
- Публикация `app.mode_changed` через `ApplicationStateManager`

**Ключевые методы:**

#### `_on_mode_request(event)`
**Логика:**
1. Парсинг `target` (поддержка `AppMode` Enum и строки "AppMode.SLEEPING")
2. Валидация `target in (SLEEPING, LISTENING, PROCESSING)`
3. **КРИТИЧНО:** Обработка `priority`:
   ```python
   priority_raw = data.get("priority", 0)
   if isinstance(priority_raw, EventPriority):
       priority = priority_raw.value  # Enum → int
   else:
       priority = int(priority_raw) if priority_raw is not None else 0
   ```
4. Проверка идемпотентности (игнорирование запросов на тот же режим)
5. **КРИТИЧНО:** Разрешение переходов:
   - `PROCESSING → LISTENING`: разрешено при `source='input_processing'` (новый запрос пользователя)
   - `PROCESSING → SLEEPING`: разрешено при `source in ('interrupt', 'input_processing', 'ProcessingWorkflow.processing_interrupted', 'interrupt_management')`
6. Применение режима через `_apply_mode()`

**Критично:**
- `priority` должен корректно обрабатываться (Enum или int)
- Переходы из PROCESSING должны быть явно разрешены
- `session_id` должен передаваться корректно

---

### 2.3 TrayControllerIntegration

**Ответственность:**
- Обновление иконки в меню-баре при изменении режима
- Визуальная индикация текущего состояния приложения

**Ключевые методы:**

#### `_on_mode_changed(event)`
**Логика:**
1. Получение `new_mode` из `event.data['mode']`
2. **КРИТИЧНО:** Преобразование `new_mode` в `AppMode` Enum:
   ```python
   if isinstance(new_mode, str):
       try:
           new_mode = AppMode(new_mode.lower())
       except (ValueError, AttributeError):
           logger.warning(f"Invalid mode: {new_mode}")
           return
   ```
3. Маппинг `AppMode` → `TrayStatus`:
   ```python
   target_status = self.mode_to_status.get(new_mode)
   ```
4. Установка `_desired_status = target_status`
5. Обновление иконки через `AppHelper.callAfter(_apply_status_ui_sync, target_status)`

**Критично:**
- `new_mode` должен быть корректно преобразован в `AppMode` Enum
- Иконка должна обновляться синхронно в UI-потоке

---

### 2.4 SignalIntegration

**Ответственность:**
- Публикация аудио сигналов при ключевых событиях
- Управление cooldown для предотвращения дублей

**Ключевые методы:**

#### `_on_voice_mic_opened(event)`
**Логика:**
1. Получение `session_id` из `event.data['session_id']`
2. **КРИТИЧНО:** Проверка блокировки повторных сигналов:
   ```python
   sid_str = str(sid) if sid is not None else None
   active_str = str(self._active_listen_session_id) if self._active_listen_session_id is not None else None
   
   if sid_str is not None and sid_str == active_str:
       # Подавляем повторный LISTEN_START для той же сессии
       return
   ```
3. Установка `_active_listen_session_id = sid` и `_listen_start_in_progress = True`
4. Публикация `playback.signal(LISTEN_START)` через `_service.emit()`
5. Сброс `_listen_start_in_progress = False` (но `_active_listen_session_id` остается)

**Критично:**
- `_active_listen_session_id` должен сбрасываться только при `voice.mic_closed` для той же сессии
- Это гарантирует один LISTEN_START на сессию

#### `_on_voice_mic_closed(event)`
**Логика:**
1. Получение `session_id` из `event.data['session_id']`
2. **КРИТИЧНО:** Сброс блокировки только для той же сессии:
   ```python
   if sid_str is not None and sid_str == active_str:
       self._active_listen_session_id = None
       self._listen_start_in_progress = False
   ```

**Критично:**
- Сброс должен происходить только для активной сессии
- Это позволяет новой сессии опубликовать LISTEN_START

---

## 3. Правильная последовательность событий

### 3.1 LONG_PRESS во время PROCESSING

**Правильная последовательность:**
```
1. InputProcessingIntegration._handle_long_press()
   → mode.request(LISTENING, priority=EventPriority.HIGH, source='input_processing')
   
2. ModeManagementIntegration._on_mode_request()
   → Проверка priority (Enum → int)
   → Разрешение PROCESSING → LISTENING (source='input_processing')
   → _apply_mode(LISTENING)
   → ApplicationStateManager.set_mode(LISTENING)
   → app.mode_changed(LISTENING)
   
3. TrayControllerIntegration._on_mode_changed()
   → Преобразование new_mode в AppMode Enum
   → Обновление иконки на LISTENING
   
4. InputProcessingIntegration._handle_long_press() (продолжение)
   → playback.cancelled (прерывание воспроизведения)
   → voice.recording_start
   → Ожидание voice.mic_opened
   
5. VoiceRecognitionIntegration
   → voice.mic_opened (session_id)
   
6. SignalIntegration._on_voice_mic_opened()
   → Проверка _active_listen_session_id
   → playback.signal(LISTEN_START)
```

**Критично:**
- `mode.request(LISTENING)` должен быть **ПЕРЕД** `playback.cancelled`
- `priority` должен быть `EventPriority.HIGH` (обрабатывается как int)
- `voice.mic_opened` должен публиковаться для новой сессии

---

### 3.2 SHORT_PRESS во время PROCESSING

**Правильная последовательность:**
```
1. InputProcessingIntegration._handle_short_press()
   → playback.cancelled
   → interrupt.request
   → mode.request(SLEEPING, source='input_processing')
   
2. ModeManagementIntegration._on_mode_request()
   → Разрешение PROCESSING → SLEEPING (source='input_processing')
   → _apply_mode(SLEEPING)
   → ApplicationStateManager.set_mode(SLEEPING)
   → app.mode_changed(SLEEPING)
   
3. TrayControllerIntegration._on_mode_changed()
   → Обновление иконки на SLEEPING
```

**Критично:**
- Режим должен перейти в SLEEPING при прерывании
- Иконка должна обновиться корректно

---

## 4. Известные проблемы и исправления

### 4.1 Ошибка с priority (ИСПРАВЛЕНО)

**Проблема:**
```python
priority = int(data.get("priority", 0))  # ❌ Ошибка: EventPriority.HIGH не может быть преобразован в int()
```

**Исправление:**
```python
priority_raw = data.get("priority", 0)
if isinstance(priority_raw, EventPriority):
    priority = priority_raw.value  # ✅ Enum → int
else:
    priority = int(priority_raw) if priority_raw is not None else 0
```

**Файл:** `integration/integrations/mode_management_integration.py:190`

---

### 4.2 Проблема с сигналами (АНАЛИЗ)

**Проблема:**
- Сигнал LISTEN_START не публикуется при LONG_PRESS во время PROCESSING

**Причина:**
- `_active_listen_session_id` может быть установлен для предыдущей сессии
- `voice.mic_closed` может не прийти для предыдущей сессии

**Решение:**
- Проверить логику сброса `_active_listen_session_id`
- Убедиться, что `voice.mic_closed` публикуется корректно

---

### 4.3 Проблема с иконкой (АНАЛИЗ)

**Проблема:**
- Иконка не обновляется при переходе PROCESSING → LISTENING

**Причина:**
- Ошибка с `priority` прерывает обработку `mode.request`
- `app.mode_changed` не публикуется

**Решение:**
- Исправление ошибки с `priority` должно решить проблему

---

## 5. Чек-лист проверки логики

### 5.1 InputProcessingIntegration
- [ ] `mode.request(LISTENING)` публикуется **ПЕРЕД** `playback.cancelled` при LONG_PRESS
- [ ] `priority=EventPriority.HIGH` передается корректно
- [ ] `session_id` устанавливается до публикации событий
- [ ] `_input_state` и `_pending_session_id` сбрасываются корректно при SHORT_PRESS

### 5.2 ModeManagementIntegration
- [ ] `priority` корректно обрабатывается (Enum и int)
- [ ] Переходы PROCESSING → LISTENING разрешены при `source='input_processing'`
- [ ] Переходы PROCESSING → SLEEPING разрешены при прерывании
- [ ] `app.mode_changed` публикуется через `ApplicationStateManager`

### 5.3 TrayControllerIntegration
- [ ] `new_mode` корректно преобразуется в `AppMode` Enum
- [ ] Иконка обновляется синхронно в UI-потоке
- [ ] Все режимы (SLEEPING, LISTENING, PROCESSING) отображаются корректно

### 5.4 SignalIntegration
- [ ] `_active_listen_session_id` сбрасывается при `voice.mic_closed`
- [ ] LISTEN_START публикуется для каждой новой сессии
- [ ] Повторные LISTEN_START для той же сессии подавляются

---

## 6. Рекомендации

1. **Всегда проверяйте типы**: `priority` может быть `EventPriority` Enum или `int`
2. **Порядок событий критичен**: `mode.request` должен быть перед `playback.cancelled`
3. **Session ID должен быть уникальным**: Каждая новая сессия должна иметь новый `session_id`
4. **Логирование**: Добавьте логирование для отслеживания последовательности событий
5. **Тестирование**: Протестируйте все сценарии (LONG_PRESS, SHORT_PRESS, RELEASE) в разных режимах

---

## 7. Следующие шаги

1. ✅ Исправить ошибку с `priority` в `ModeManagementIntegration`
2. ⏳ Проверить логику сброса `_active_listen_session_id` в `SignalIntegration`
3. ⏳ Протестировать все сценарии перехода режимов
4. ⏳ Убедиться, что иконка обновляется корректно во всех сценариях
5. ⏳ Убедиться, что сигналы публикуются корректно





