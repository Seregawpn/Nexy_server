# План реализации: AVF диагностика → Google запись

## 🎯 Цель

Реализовать логику, где:
1. **AVF активирует микрофон на ~1 секунду** → получает информацию об устройстве (формат, имя, диагностика)
2. **AVF дезактивирует микрофон** ✅
3. **Google активирует микрофон** через `sr.Microphone()` → записывает речь
4. **Google распознаёт** через `recognize_google()`

---

## 📋 Детальный план изменений

### Этап 1: Изменения в `initialize()`

**Текущий код:**
```python
if self._use_avf:
    self._recognizer = None  # Не создаём SpeechRecognizer
```

**Новый код:**
```python
if self._use_avf:
    # ✅ Создаём SpeechRecognizer для Google записи
    if not self.config.simulate and _REAL_VOICE_AVAILABLE:
        try:
            self._recognizer = SpeechRecognizer(DEFAULT_RECOGNITION_CONFIG)
            logger.info("✅ [AVF] SpeechRecognizer создан для Google записи")
        except Exception as e:
            logger.warning(f"⚠️ [AVF] Не удалось создать SpeechRecognizer: {e}")
            self._recognizer = None
    else:
        self._recognizer = None
```

**Что меняется:**
- ✅ Создаём `SpeechRecognizer` даже при `_use_avf = True`
- ✅ AVF будет использоваться только для диагностики
- ✅ Google будет использоваться для записи

---

### Этап 2: Новый метод `_get_device_info_via_avf()`

**Новый метод:**
```python
async def _get_device_info_via_avf(self) -> Optional[Dict[str, Any]]:
    """
    Получает информацию об устройстве через AVF (активация на ~1 секунду).
    
    Returns:
        Dict с информацией: device_info, input_format, diagnostics
        None если не удалось получить
    """
    if not self._use_avf or not self._avf_engine:
        return None
    
    try:
        logger.info("🔍 [AVF] Получение информации об устройстве (активация на ~1 секунду)...")
        
        # ✅ ШАГ 1: Активируем AVF на ~1 секунду
        success = await self._avf_engine.start_input()
        if not success:
            logger.warning("⚠️ [AVF] Не удалось активировать для диагностики")
            return None
        
        # Ждём ~1 секунду для получения данных
        await asyncio.sleep(1.0)
        
        # ✅ ШАГ 2: Останавливаем и получаем результат
        result = await self._avf_engine.stop_input()
        if not result:
            logger.warning("⚠️ [AVF] Не удалось получить диагностику")
            return None
        
        # Формируем информацию об устройстве
        device_info = {
            "device_info": {
                "name": result.device_info.name if result.device_info else None,
                "uid": result.device_info.uid if result.device_info else None,
                "is_input": result.device_info.is_input if result.device_info else True
            } if result.device_info else None,
            "input_format": {
                "sample_rate": result.input_format.sample_rate if result.input_format else None,
                "channels": result.input_format.channels if result.input_format else None,
                "bit_depth": result.input_format.bit_depth if result.input_format else 16
            } if result.input_format else None,
            "diagnostics": result.diagnostics
        }
        
        logger.info(f"✅ [AVF] Диагностика получена: device={device_info['device_info']['name'] if device_info['device_info'] else 'unknown'}, format={device_info['input_format']}")
        
        return device_info
        
    except Exception as e:
        logger.error(f"❌ [AVF] Ошибка получения диагностики: {e}", exc_info=True)
        return None
```

**Что делает:**
- ✅ Активирует AVF на ~1 секунду
- ✅ Получает информацию об устройстве
- ✅ Дезактивирует AVF
- ✅ Возвращает информацию для использования

---

### Этап 3: Изменения в `_on_recording_start()`

**Текущий код:**
```python
if self._use_avf and self._avf_engine:
    # AVF записывает всё время
    await self._avf_engine.start_input(callback=audio_callback)
```

**Новый код:**
```python
if self._use_avf and self._avf_engine:
    # ✅ ШАГ 1: Получаем диагностику через AVF (активация на ~1 секунду)
    device_info = await self._get_device_info_via_avf()
    if device_info:
        # Сохраняем информацию об устройстве для использования
        self._avf_device_info = device_info
        logger.info(f"✅ [AVF] Информация об устройстве сохранена")
    
    # ✅ ШАГ 2: Небольшая пауза для гарантии деактивации AVF
    await asyncio.sleep(0.2)
    
    # ✅ ШАГ 3: Активируем Google через speech_recognition
    if self._recognizer:
        try:
            logger.info("🎤 [Google] Активация микрофона через speech_recognition...")
            await self._recognizer.start_listening()
            logger.info("✅ [Google] Микрофон активирован через speech_recognition")
            
            # Публикуем событие
            self.state_manager.set_microphone_state("active", session_id=str(session_id), reason="google_recording_started")
            await self.event_bus.publish("microphone.opened", {"session_id": session_id})
        except Exception as e:
            logger.error(f"❌ [Google] Ошибка активации микрофона: {e}", exc_info=True)
            self.state_manager.set_microphone_state("idle", session_id=None, reason="google_mic_open_failed")
            return
    else:
        logger.error("❌ [Google] SpeechRecognizer не создан")
        return
```

**Что меняется:**
- ✅ Сначала получаем диагностику через AVF (на ~1 секунду)
- ✅ Дезактивируем AVF
- ✅ Пауза 0.2 секунды для гарантии деактивации
- ✅ Активируем Google через `SpeechRecognizer.start_listening()`

---

### Этап 4: Изменения в `_on_recording_stop()`

**Текущий код:**
```python
if self._use_avf and self._avf_engine:
    result = await self._avf_engine.stop_input()
    await self._publish_mic_data_ready(result, session_id)
```

**Новый код:**
```python
if self._recognizer:
    # ✅ Останавливаем Google запись
    try:
        logger.info("🎤 [Google] Остановка записи через speech_recognition...")
        audio_data = await self._recognizer.stop_listening()
        
        if audio_data:
            # ✅ Распознаём через Google
            await self._recognize_google_audio(audio_data, session_id)
        else:
            logger.warning("⚠️ [Google] Пустые данные от speech_recognition")
            await self.event_bus.publish("voice.recognition_failed", {
                "session_id": session_id,
                "error": "Empty audio data from Google",
                "source": "google_recognition"
            })
    except Exception as e:
        logger.error(f"❌ [Google] Ошибка остановки записи: {e}", exc_info=True)
        await self.event_bus.publish("voice.recognition_failed", {
            "session_id": session_id,
            "error": str(e),
            "source": "google_recognition"
        })
    finally:
        # Обновляем состояние микрофона
        self.state_manager.set_microphone_state("idle", session_id=None, reason="google_recording_stopped")
        await self.event_bus.publish("microphone.closed", {"session_id": session_id})
```

**Что меняется:**
- ✅ Останавливаем Google запись через `SpeechRecognizer.stop_listening()`
- ✅ Получаем данные от Google
- ✅ Распознаём через `recognize_google()`

---

### Этап 5: Новый метод `_recognize_google_audio()`

**Новый метод:**
```python
async def _recognize_google_audio(self, audio_data: Any, session_id: str) -> None:
    """
    Распознавание аудио через Google Speech API.
    
    Args:
        audio_data: AudioData объект от speech_recognition
        session_id: ID сессии
    """
    try:
        import speech_recognition as sr
        
        # Проверяем тип данных
        if not isinstance(audio_data, sr.AudioData):
            logger.error(f"❌ [Google] Неверный тип данных: {type(audio_data)}")
            await self.event_bus.publish("voice.recognition_failed", {
                "session_id": session_id,
                "error": "Invalid audio data type",
                "source": "google_recognition"
            })
            return
        
        # Получаем язык из конфигурации
        language = self.config.language
        
        # Создаём recognizer
        recognizer = sr.Recognizer()
        
        logger.info(f"🎤 [Google] Начинаем распознавание: language={language}")
        
        # Распознаём через Google
        try:
            text = recognizer.recognize_google(audio_data, language=language)
            
            logger.info(f"✅ [Google] Распознавание успешно: '{text[:100]}...'")
            
            # Публикуем результат
            await self.event_bus.publish("voice.recognition_completed", {
                "session_id": session_id,
                "text": text,
                "confidence": None,
                "language": language,
                "source": "google_recognition",
                "device_info": getattr(self, '_avf_device_info', None)  # Добавляем диагностику от AVF
            })
            
        except sr.UnknownValueError:
            logger.warning("⚠️ [Google] Речь не распознана")
            await self.event_bus.publish("voice.recognition_failed", {
                "session_id": session_id,
                "error": "Speech not recognized",
                "source": "google_recognition"
            })
        except sr.RequestError as e:
            logger.error(f"❌ [Google] Ошибка сервиса: {e}")
            await self.event_bus.publish("voice.recognition_failed", {
                "session_id": session_id,
                "error": str(e),
                "source": "google_recognition"
            })
            
    except Exception as e:
        logger.error(f"❌ [Google] Ошибка распознавания: {e}", exc_info=True)
        await self.event_bus.publish("voice.recognition_failed", {
            "session_id": session_id,
            "error": str(e),
            "source": "google_recognition"
        })
```

**Что делает:**
- ✅ Принимает `AudioData` от `speech_recognition`
- ✅ Распознаёт через `recognize_google()`
- ✅ Публикует результат или ошибку
- ✅ Добавляет диагностику от AVF в результат

---

### Этап 6: Удаление ненужного кода

**Что нужно удалить/изменить:**

1. **Убрать эстафету `voice.mic_data_ready`:**
   - Удалить `_publish_mic_data_ready()`
   - Удалить `_on_mic_data_ready()`
   - Удалить подписку на `voice.mic_data_ready`

2. **Убрать обработку данных от AVF:**
   - Удалить `_recognize_avf_audio()` (или оставить для legacy fallback)
   - Удалить обработку `result.data` в `_on_recording_stop()`

3. **Убрать защиту от двойной активации:**
   - Удалить `_processed_mic_data_sessions` (теперь это нормально)
   - Удалить проверки в `_on_mic_data_ready()`

---

## 📊 Итоговая схема

```
1. voice.recording_start
   │
   ├─► _get_device_info_via_avf()
   │   ├─ AVF активирует (~1 сек)
   │   ├─ Получает: device_info, format, diagnostics
   │   └─ AVF дезактивирует ✅
   │
   ├─► Пауза 0.2 сек (гарантия деактивации)
   │
   └─► SpeechRecognizer.start_listening()
       └─ Google активирует микрофон ✅

2. Пользователь говорит
   │
   └─► Google записывает через sr.Microphone()

3. voice.recording_stop
   │
   └─► SpeechRecognizer.stop_listening()
       ├─ Получаем AudioData
       └─ _recognize_google_audio()
           ├─ recognizer.recognize_google()
           └─ Публикуем результат
```

---

## ⚠️ Потенциальные проблемы и решения

### Проблема 1: Конфликт между AVF и Google

**Решение:**
- ✅ Пауза 0.2 секунды между деактивацией AVF и активацией Google
- ✅ Проверка, что AVF полностью деактивирован перед активацией Google

### Проблема 2: macOS может показать два диалога разрешений

**Решение:**
- ✅ AVF активирует только на ~1 секунду (минимальное время)
- ✅ Google активирует сразу после (разрешение уже запрошено)

### Проблема 3: Задержка перед записью

**Решение:**
- ✅ Минимальная задержка (~1.2 секунды: 1 сек AVF + 0.2 сек пауза)
- ✅ Логирование для пользователя: "Получение информации об устройстве..."

---

## ✅ Чек-лист реализации

- [ ] Изменить `initialize()`: создавать `SpeechRecognizer` при `_use_avf`
- [ ] Создать `_get_device_info_via_avf()`: получение диагностики через AVF
- [ ] Изменить `_on_recording_start()`: AVF диагностика → пауза → Google активация
- [ ] Изменить `_on_recording_stop()`: остановка Google → распознавание
- [ ] Создать `_recognize_google_audio()`: распознавание через Google
- [ ] Удалить эстафету `voice.mic_data_ready`
- [ ] Удалить `_publish_mic_data_ready()` и `_on_mic_data_ready()`
- [ ] Удалить защиту от двойной активации
- [ ] Добавить логирование для отладки
- [ ] Протестировать с реальным микрофоном

---

## 🎯 Ожидаемый результат

1. ✅ AVF получает информацию об устройстве (формат, имя, диагностика)
2. ✅ Google записывает речь напрямую (корректное распознавание)
3. ✅ Информация об устройстве доступна для использования
4. ✅ Нет проблем с некорректным распознаванием данных от AVF

