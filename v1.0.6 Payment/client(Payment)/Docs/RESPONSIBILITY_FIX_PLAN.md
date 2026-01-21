# 📋 План исправления распределения ответственности

## 🎯 Цель

Установить `MicrophoneStateManager` как **единственный источник истины** для событий `voice.mic_opened` и `voice.mic_closed`, устранив дублирование и нарушение принципа единой ответственности.

---

## 📊 Текущее состояние

### ❌ Проблемы:
1. `VoiceRecognitionIntegration` публикует `voice.mic_opened` напрямую (строка 351)
2. `VoiceRecognitionIntegration` публикует `voice.mic_closed` напрямую (строки 465, 497)
3. `InputProcessingIntegration` публикует `voice.mic_closed` напрямую (строки 912, 1402, 739)
4. `MicrophoneStateManager` НЕ публикует `voice.mic_opened/closed` (должен быть единственным источником)

---

## ✅ Целевое состояние

### Правильный поток событий:
```
[Клавиатура] → InputProcessingIntegration
    ↓
voice.recording_start
    ↓
VoiceRecognitionIntegration._on_recording_start
    ↓
MicrophoneStateManager.request_open()
    ↓
microphone.open_requested
    ↓
VoiceRecognitionIntegration._on_microphone_open_requested
    ↓
SpeechRecognizer.start_listening()
    ↓
microphone.opened
    ↓
MicrophoneStateManager._on_microphone_opened
    ↓
voice.mic_opened ✅ (ЕДИНСТВЕННЫЙ ИСТОЧНИК)
    ↓
[SignalIntegration, TrayControllerIntegration, InputProcessingIntegration]
```

---

## 🔧 План исправлений (пошагово)

### **ЭТАП 1: Добавить публикацию `voice.mic_opened/closed` в `MicrophoneStateManager`**

**Файл:** `client(prod)/modules/microphone_state/core/microphone_state_manager.py`

**Изменения:**

1. **В методе `_on_microphone_opened` (после строки 324):**
   ```python
   async def _on_microphone_opened(self, event: Dict[str, Any]):
       """Обработчик события открытия микрофона"""
       try:
           data = event.get("data", {}) or event
           session_id = data.get("session_id")
           
           async with self._state_lock:
               if self._state == MicrophoneState.OPENING:
                   await self._set_state(MicrophoneState.ACTIVE, session_id)
                   
                   # Уведомляем ожидающие задачи
                   if self._opened_event:
                       self._opened_event.set()
                   
                   # ✅ ИСПРАВЛЕНИЕ: Публикуем voice.mic_opened (ЕДИНСТВЕННЫЙ ИСТОЧНИК)
                   await self._event_bus.publish("voice.mic_opened", {
                       "session_id": session_id,
                       "timestamp": time.time(),
                       "source": "microphone_state_manager"
                   })
                   logger.info(f"✅ [MIC_STATE] voice.mic_opened опубликовано для session {session_id}")
               else:
                   logger.warning(
                       f"⚠️ [MIC_STATE] Неожиданное состояние при opened: {self._state.value}"
                   )
       except Exception as e:
           logger.error(f"❌ [MIC_STATE] Ошибка обработки microphone.opened: {e}")
   ```

2. **В методе `_on_microphone_closed` (после строки 344):**
   ```python
   async def _on_microphone_closed(self, event: Dict[str, Any]):
       """Обработчик события закрытия микрофона"""
       try:
           data = event.get("data", {}) or event
           session_id = data.get("session_id")
           
           async with self._state_lock:
               if self._state in [MicrophoneState.ACTIVE, MicrophoneState.CLOSING]:
                   await self._set_state(MicrophoneState.IDLE, None)
                   
                   # Уведомляем ожидающие задачи
                   if self._closed_event:
                       self._closed_event.set()
                   
                   # ✅ ИСПРАВЛЕНИЕ: Публикуем voice.mic_closed (ЕДИНСТВЕННЫЙ ИСТОЧНИК)
                   await self._event_bus.publish("voice.mic_closed", {
                       "session_id": session_id,
                       "timestamp": time.time(),
                       "source": "microphone_state_manager"
                   })
                   logger.info(f"✅ [MIC_STATE] voice.mic_closed опубликовано для session {session_id}")
               else:
                   logger.warning(
                       f"⚠️ [MIC_STATE] Неожиданное состояние при closed: {self._state.value}"
                   )
       except Exception as e:
           logger.error(f"❌ [MIC_STATE] Ошибка обработки microphone.closed: {e}")
   ```

3. **В методе `_force_close_internal` (после строки 234):**
   ```python
   async def _force_close_internal(self, reason: str):
       """Внутренний метод для принудительного закрытия"""
       old_state = self._state
       if old_state != MicrophoneState.IDLE:
           await self._set_state(MicrophoneState.IDLE, None)
           self._error_count += 1
           logger.warning(
               f"⚠️ [MIC_STATE] Принудительное закрытие: {old_state.value} → IDLE "
               f"(reason={reason}, error_count={self._error_count})"
           )
           
           # ✅ ИСПРАВЛЕНИЕ: Публикуем voice.mic_closed при принудительном закрытии
           await self._event_bus.publish("voice.mic_closed", {
               "session_id": None,
               "timestamp": time.time(),
               "source": "microphone_state_manager",
               "reason": reason
           })
           logger.info(f"✅ [MIC_STATE] voice.mic_closed опубликовано (принудительное закрытие: {reason})")
   ```

**Проверка:**
- ✅ `MicrophoneStateManager` теперь публикует `voice.mic_opened` и `voice.mic_closed`
- ✅ Импорт `time` добавлен в начало файла (если отсутствует)

---

### **ЭТАП 2: Убрать публикацию `voice.mic_opened` из `VoiceRecognitionIntegration`**

**Файл:** `client(prod)/integration/integrations/voice_recognition_integration.py`

**Изменения:**

1. **Удалить строки 348-352 (публикация `voice.mic_opened`):**
   ```python
   # ❌ УДАЛИТЬ:
   # КРИТИЧНО: Публикуем voice.mic_opened СРАЗУ при recording_start,
   # чтобы сигнал воспроизводился сразу при переходе в LISTENING режим,
   # а не после открытия микрофона (которое может занимать время для Bluetooth)
   await self.event_bus.publish("voice.mic_opened", {"session_id": session_id})
   logger.info(f"🎤 VOICE: microphone opened (pending) для session {session_id}")
   ```

   **Заменить на:**
   ```python
   # ✅ ИСПРАВЛЕНИЕ: voice.mic_opened будет опубликовано MicrophoneStateManager
   # после получения microphone.opened от SpeechRecognizer
   logger.debug(f"🎤 VOICE: ожидание открытия микрофона для session {session_id}")
   ```

2. **Удалить комментарий на строке 378 (если есть):**
   ```python
   # ❌ УДАЛИТЬ:
   # КРИТИЧНО: voice.mic_opened уже опубликован выше при recording_start
   # для немедленного воспроизведения сигнала
   ```

**Проверка:**
- ✅ `VoiceRecognitionIntegration` больше НЕ публикует `voice.mic_opened`
- ✅ Событие будет публиковаться только через `MicrophoneStateManager`

---

### **ЭТАП 3: Убрать публикацию `voice.mic_closed` из `VoiceRecognitionIntegration`**

**Файл:** `client(prod)/integration/integrations/voice_recognition_integration.py`

**Изменения:**

1. **Удалить строку 465 (публикация `voice.mic_closed` при принудительной остановке):**
   ```python
   # ❌ УДАЛИТЬ:
   await self.event_bus.publish("voice.mic_closed", {"session_id": None, "reason": "force_stop_no_session"})
   ```

   **Заменить на:**
   ```python
   # ✅ ИСПРАВЛЕНИЕ: voice.mic_closed будет опубликовано MicrophoneStateManager
   # после получения microphone.closed или при принудительном закрытии
   logger.debug("🎤 VOICE: ожидание закрытия микрофона (принудительная остановка)")
   ```

2. **Удалить строку 497 (публикация `voice.mic_closed` при нормальной остановке):**
   ```python
   # ❌ УДАЛИТЬ:
   await self.event_bus.publish("voice.mic_closed", {"session_id": session_id})
   ```

   **Заменить на:**
   ```python
   # ✅ ИСПРАВЛЕНИЕ: voice.mic_closed будет опубликовано MicrophoneStateManager
   # после получения microphone.closed от SpeechRecognizer
   logger.debug(f"🎤 VOICE: ожидание закрытия микрофона для session {session_id}")
   ```

**Проверка:**
- ✅ `VoiceRecognitionIntegration` больше НЕ публикует `voice.mic_closed`
- ✅ Событие будет публиковаться только через `MicrophoneStateManager`

---

### **ЭТАП 4: Убрать публикацию `voice.mic_closed` из `InputProcessingIntegration`**

**Файл:** `client(prod)/integration/integrations/input_processing_integration.py`

**Изменения:**

1. **Удалить строки 912-916 (публикация `voice.mic_closed` при SHORT_PRESS):**
   ```python
   # ❌ УДАЛИТЬ:
   # Также публикуем событие закрытия микрофона напрямую
   await self.event_bus.publish("voice.mic_closed", {
       "source": "keyboard",
       "timestamp": event.timestamp,
       "reason": "force_close_on_short_press"
   })
   ```

   **Заменить на:**
   ```python
   # ✅ ИСПРАВЛЕНИЕ: voice.mic_closed будет опубликовано MicrophoneStateManager
   # после получения microphone.closed или при принудительном закрытии
   logger.debug("🎤 [INPUT_PROCESSING] ожидание закрытия микрофона (SHORT_PRESS)")
   ```

2. **Удалить строки 1402-1406 (публикация `voice.mic_closed` при RELEASE):**
   ```python
   # ❌ УДАЛИТЬ:
   # Также публикуем событие закрытия микрофона напрямую
   await self.event_bus.publish("voice.mic_closed", {
       "source": "keyboard",
       "timestamp": event.timestamp,
       "reason": "force_close_on_release"
   })
   ```

   **Заменить на:**
   ```python
   # ✅ ИСПРАВЛЕНИЕ: voice.mic_closed будет опубликовано MicrophoneStateManager
   # после получения microphone.closed или при принудительном закрытии
   logger.debug("🎤 [INPUT_PROCESSING] ожидание закрытия микрофона (RELEASE)")
   ```

3. **Удалить строки 739-743 (публикация `voice.mic_closed` при таймауте мониторинга):**
   ```python
   # ❌ УДАЛИТЬ:
   # Публикуем событие закрытия микрофона для синхронизации с другими модулями
   try:
       asyncio.create_task(self.event_bus.publish("voice.mic_closed", {
           "source": "mic_reset_timeout",
           "timestamp": time.time(),
           "reason": "mic_reset_timeout"
       }))
   except Exception as e:
       logger.error(f"❌ [INPUT_PROCESSING] Ошибка публикации voice.mic_closed при сбросе: {e}")
   ```

   **Заменить на:**
   ```python
   # ✅ ИСПРАВЛЕНИЕ: voice.mic_closed будет опубликовано MicrophoneStateManager
   # при принудительном закрытии через force_close_microphone()
   logger.debug("🎤 [INPUT_PROCESSING] ожидание закрытия микрофона (таймаут мониторинга)")
   ```

**Проверка:**
- ✅ `InputProcessingIntegration` больше НЕ публикует `voice.mic_closed`
- ✅ Событие будет публиковаться только через `MicrophoneStateManager`

---

### **ЭТАП 5: Проверка импортов и зависимостей**

**Файл:** `client(prod)/modules/microphone_state/core/microphone_state_manager.py`

**Проверка:**
- ✅ Импорт `time` присутствует в начале файла
- ✅ Если отсутствует, добавить: `import time`

---

## 🧪 План тестирования

### Тест 1: Нормальное открытие микрофона
**Сценарий:**
1. Нажать и удерживать Control+N (LONG_PRESS)
2. Проверить логи:
   - ✅ `voice.recording_start` опубликовано `InputProcessingIntegration`
   - ✅ `microphone.open_requested` опубликовано `MicrophoneStateManager`
   - ✅ `microphone.opened` опубликовано `VoiceRecognitionIntegration`
   - ✅ `voice.mic_opened` опубликовано **ТОЛЬКО** `MicrophoneStateManager` (ЕДИНСТВЕННЫЙ ИСТОЧНИК)

**Ожидаемый результат:**
- Сигнал воспроизводится один раз
- Нет дублирования событий

---

### Тест 2: Нормальное закрытие микрофона
**Сценарий:**
1. Отпустить Control+N (RELEASE)
2. Проверить логи:
   - ✅ `voice.recording_stop` опубликовано `InputProcessingIntegration`
   - ✅ `microphone.close_requested` опубликовано `MicrophoneStateManager`
   - ✅ `microphone.closed` опубликовано `VoiceRecognitionIntegration`
   - ✅ `voice.mic_closed` опубликовано **ТОЛЬКО** `MicrophoneStateManager` (ЕДИНСТВЕННЫЙ ИСТОЧНИК)

**Ожидаемый результат:**
- Событие закрытия публикуется один раз
- Нет дублирования событий

---

### Тест 3: Принудительное закрытие микрофона (SHORT_PRESS)
**Сценарий:**
1. Нажать и удерживать Control+N (LONG_PRESS)
2. Нажать Control+N еще раз (SHORT_PRESS) до отпускания
3. Проверить логи:
   - ✅ `voice.recording_stop` опубликовано `InputProcessingIntegration`
   - ✅ `microphone.close_requested` опубликовано `MicrophoneStateManager` (с `force=True`)
   - ✅ `voice.mic_closed` опубликовано **ТОЛЬКО** `MicrophoneStateManager` (ЕДИНСТВЕННЫЙ ИСТОЧНИК)

**Ожидаемый результат:**
- Микрофон закрывается корректно
- Нет дублирования событий

---

### Тест 4: Принудительное закрытие при таймауте
**Сценарий:**
1. Нажать и удерживать Control+N (LONG_PRESS)
2. Дождаться таймаута мониторинга (если настроен)
3. Проверить логи:
   - ✅ `voice.mic_closed` опубликовано **ТОЛЬКО** `MicrophoneStateManager` (через `_force_close_internal`)

**Ожидаемый результат:**
- Микрофон закрывается корректно
- Нет дублирования событий

---

## ✅ Критерии успеха

1. ✅ `voice.mic_opened` публикуется **ТОЛЬКО** из `MicrophoneStateManager`
2. ✅ `voice.mic_closed` публикуется **ТОЛЬКО** из `MicrophoneStateManager`
3. ✅ `InputProcessingIntegration` **НЕ** публикует события микрофона
4. ✅ `VoiceRecognitionIntegration` **НЕ** публикует `voice.mic_opened/closed` напрямую
5. ✅ Все компоненты подписываются на события микрофона, но не публикуют их
6. ✅ Нет дублирования событий в логах
7. ✅ Сигналы воспроизводятся корректно (один раз)

---

## 📝 Порядок выполнения

1. **ЭТАП 1** → Тестирование → ✅
2. **ЭТАП 2** → Тестирование → ✅
3. **ЭТАП 3** → Тестирование → ✅
4. **ЭТАП 4** → Тестирование → ✅
5. **ЭТАП 5** → Финальное тестирование всех сценариев → ✅

---

## 🔍 Проверка после исправлений

### Команда для проверки публикации событий:
```bash
# Проверить, что voice.mic_opened публикуется только из MicrophoneStateManager
grep -r "voice.mic_opened" client\(prod\)/integration/integrations/ | grep -v "subscribe"

# Проверить, что voice.mic_closed публикуется только из MicrophoneStateManager
grep -r "voice.mic_closed" client\(prod\)/integration/integrations/ | grep -v "subscribe"
```

**Ожидаемый результат:**
- Только подписки (`subscribe`), без публикаций (`publish`) в интеграциях
- Публикации только в `MicrophoneStateManager`

---

## 🎯 Итоговая архитектура

```
┌─────────────────────────┐
│ InputProcessingIntegration│
│ ✅ voice.recording_start │
│ ✅ voice.recording_stop   │
│ ❌ НЕ публикует mic_*    │
└───────────┬─────────────┘
            │
            ↓
┌─────────────────────────┐
│ VoiceRecognitionIntegration│
│ ✅ microphone.opened     │
│ ✅ microphone.closed     │
│ ✅ microphone.error      │
│ ❌ НЕ публикует voice.mic_*│
└───────────┬─────────────┘
            │
            ↓
┌─────────────────────────┐
│ MicrophoneStateManager   │
│ ✅ voice.mic_opened      │ ← ЕДИНСТВЕННЫЙ ИСТОЧНИК
│ ✅ voice.mic_closed      │ ← ЕДИНСТВЕННЫЙ ИСТОЧНИК
└───────────┬─────────────┘
            │
            ↓
┌─────────────────────────┐
│ SignalIntegration        │
│ TrayControllerIntegration│
│ InputProcessingIntegration│
│ (подписчики)            │
└─────────────────────────┘
```

---

## 📌 Важные замечания

1. **Задержка воспроизведения сигнала:**
   - Раньше `voice.mic_opened` публиковалось сразу при `recording_start`
   - Теперь оно публикуется после фактического открытия микрофона
   - Это может создать небольшую задержку для Bluetooth устройств
   - **Решение:** Если задержка критична, можно добавить `voice.mic_opening` событие для немедленного воспроизведения сигнала (но это требует дополнительного анализа)

2. **Обратная совместимость:**
   - Все подписчики (`SignalIntegration`, `TrayControllerIntegration`, `InputProcessingIntegration`) продолжают работать
   - Изменяется только источник событий, формат событий остается прежним

3. **Логирование:**
   - Добавлено подробное логирование в `MicrophoneStateManager` для отслеживания публикации событий
   - Все изменения логируются с префиксом `[MIC_STATE]`

---

## ✅ Готовность к выполнению

Все этапы детализированы, изменения минимальны и изолированы. Можно приступать к исправлениям.


