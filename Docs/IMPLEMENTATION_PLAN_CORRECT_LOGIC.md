# План реализации правильной логики

## 🎯 Правильная логика (как должно работать)

### Последовательность:

1. **Активация AVF (на секунду для диагностики)**
   ```
   voice.recording_start
       ↓
   AVFAudioEngine.start_input()
       ↓
   Записывает ~1 секунду
       ↓
   Получает: формат, устройство, диагностику
       ↓
   AVFAudioEngine.stop_input() ✅ (дезактивирует)
   ```

2. **Активация Google (через speech_recognition)**
   ```
   Создаём sr.Microphone()
       ↓
   recognizer.adjust_for_ambient_noise() (опционально)
       ↓
   recognizer.listen() → запись речи
       ↓
   Пользователь говорит
   ```

3. **Остановка и распознавание**
   ```
   voice.recording_stop
       ↓
   recognizer.stop() → получаем аудио данные
       ↓
   Создаём sr.AudioData
       ↓
   recognizer.recognize_google(audio_data, language)
       ↓
   Публикуем результат
   ```

---

## 🔧 Что нужно изменить

### 1. В `initialize()`:

**Было:**
```python
if self._use_avf:
    self._recognizer = None  # Не создаём SpeechRecognizer
```

**Должно быть:**
```python
if self._use_avf:
    # Создаём SpeechRecognizer для Google записи
    self._recognizer = SpeechRecognizer(DEFAULT_RECOGNITION_CONFIG)
    # AVF будет использоваться только для диагностики
```

---

### 2. В `_on_recording_start()`:

**Было:**
```python
if self._use_avf and self._avf_engine:
    # AVF записывает всё время
    await self._avf_engine.start_input(callback=audio_callback)
```

**Должно быть:**
```python
if self._use_avf and self._avf_engine:
    # ✅ ШАГ 1: AVF активирует на секунду для диагностики
    await self._avf_engine.start_input()
    await asyncio.sleep(1.0)  # Записываем ~1 секунду
    result = await self._avf_engine.stop_input()
    
    # Получаем диагностику: формат, устройство, etc.
    if result:
        logger.info(f"✅ [AVF] Диагностика получена: {result.device_info}, {result.input_format}")
    
    # ✅ ШАГ 2: Активируем Google через speech_recognition
    if self._recognizer:
        await self._recognizer.start_listening()
```

---

### 3. В `_on_recording_stop()`:

**Было:**
```python
if self._use_avf and self._avf_engine:
    result = await self._avf_engine.stop_input()
    await self._publish_mic_data_ready(result, session_id)
```

**Должно быть:**
```python
if self._recognizer:
    # ✅ Останавливаем Google запись
    audio_data = await self._recognizer.stop_listening()
    
    # ✅ Распознаём через Google
    if audio_data:
        await self._recognize_google_audio(audio_data, session_id)
```

---

### 4. Новый метод `_recognize_google_audio()`:

```python
async def _recognize_google_audio(self, audio_data: sr.AudioData, session_id: str):
    """Распознавание через Google Speech API"""
    try:
        import speech_recognition as sr
        
        recognizer = sr.Recognizer()
        language = self.config.language
        
        text = recognizer.recognize_google(audio_data, language=language)
        
        await self.event_bus.publish("voice.recognition_completed", {
            "session_id": session_id,
            "text": text,
            "source": "google_recognition"
        })
    except sr.UnknownValueError:
        await self.event_bus.publish("voice.recognition_failed", {
            "session_id": session_id,
            "error": "Speech not recognized",
            "source": "google_recognition"
        })
    except sr.RequestError as e:
        await self.event_bus.publish("voice.recognition_failed", {
            "session_id": session_id,
            "error": str(e),
            "source": "google_recognition"
        })
```

---

## 📋 Чек-лист изменений

- [ ] Изменить `initialize()`: создавать `SpeechRecognizer` при `_use_avf`
- [ ] Изменить `_on_recording_start()`: AVF на секунду → дезактивировать → активировать Google
- [ ] Изменить `_on_recording_stop()`: останавливать Google → распознавать
- [ ] Создать `_recognize_google_audio()`: метод для распознавания через Google
- [ ] Убрать эстафету `voice.mic_data_ready` (не нужна)
- [ ] Убрать `_publish_mic_data_ready()` (не нужна)
- [ ] Убрать `_on_mic_data_ready()` (не нужна)
- [ ] Убрать защиту от двойной активации (теперь это нормально)

---

## 🎯 Итоговая схема

```
1. voice.recording_start
   ├─ AVF активирует (~1 сек) → получает диагностику → дезактивирует ✅
   └─ Google активирует → записывает речь

2. Пользователь говорит
   └─ Google записывает через sr.Microphone()

3. voice.recording_stop
   ├─ Google останавливает → получает данные
   └─ Распознаёт через recognize_google() → результат
```

