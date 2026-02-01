# Пошаговый план тестирования аудиосистемы

## Дата: 2025-12-09

## Философия подхода

**Принцип**: Тестируем каждый компонент отдельно, начиная с самых базовых вещей. Если что-то не работает, останавливаемся и исправляем, прежде чем переходить дальше.

**Правило**: Не переходим к следующему шагу, пока текущий не работает на 100%.

---

## ШАГ 1: Проверка базовых компонентов

### Цель
Убедиться, что все зависимости установлены и доступны.

### Что проверяем

#### 1.1. Проверка импортов
```bash
python3 -c "
import sys
print('Python:', sys.version)

# AVFoundation
try:
    from AVFoundation import AVAudioEngine
    print('✅ AVFoundation доступен')
except ImportError as e:
    print('❌ AVFoundation недоступен:', e)
    sys.exit(1)

# Speech framework
try:
    from Speech import SFSpeechRecognizer
    print('✅ Speech framework доступен')
except ImportError as e:
    print('❌ Speech framework недоступен:', e)
    print('💡 Установите: pip3 install pyobjc-framework-Speech --break-system-packages')
    sys.exit(1)

# SpeechRecognition library
try:
    import speech_recognition as sr
    print('✅ SpeechRecognition library доступен')
except ImportError as e:
    print('❌ SpeechRecognition library недоступен:', e)
    print('💡 Установите: pip3 install SpeechRecognition --break-system-packages')
    sys.exit(1)

# numpy и scipy
try:
    import numpy as np
    print('✅ numpy доступен')
except ImportError as e:
    print('❌ numpy недоступен:', e)

try:
    from scipy import signal
    print('✅ scipy доступен')
except ImportError as e:
    print('⚠️ scipy недоступен (не критично, но желательно):', e)

print('\\n✅ Все базовые компоненты доступны!')
"
```

**Ожидаемый результат**: Все импорты успешны.

**Если ошибка**: Установите недостающие зависимости.

---

#### 1.2. Проверка разрешений macOS

```bash
python3 -c "
from Speech import SFSpeechRecognizer, SFSpeechRecognizerAuthorizationStatus

status = SFSpeechRecognizer.authorizationStatus()
print(f'Speech Recognition статус: {status}')

if status == SFSpeechRecognizerAuthorizationStatus.authorized:
    print('✅ Разрешение Speech Recognition предоставлено')
elif status == SFSpeechRecognizerAuthorizationStatus.notDetermined:
    print('⚠️ Разрешение Speech Recognition не запрошено')
    print('💡 Приложение должно запросить разрешение при первом запуске')
elif status == SFSpeechRecognizerAuthorizationStatus.denied:
    print('❌ Разрешение Speech Recognition отклонено')
    print('💡 Включите в System Preferences → Privacy → Speech Recognition')
else:
    print('❌ Разрешение Speech Recognition ограничено')
"
```

**Ожидаемый результат**: `authorized` или `notDetermined`.

**Если `denied`**: Включите разрешение в System Preferences.

---

#### 1.3. Проверка доступности микрофона

```bash
python3 -c "
from AVFoundation import AVAudioEngine, AVAudioSession
from Foundation import NSRunLoop, NSDefaultRunLoopMode
import time

engine = AVAudioEngine.alloc().init()
input_node = engine.inputNode()

if input_node:
    print('✅ Микрофон доступен через AVFoundation')
    print(f'   Sample rate: {input_node.outputFormatForBus_(0).sampleRate()}Hz')
    print(f'   Channels: {input_node.outputFormatForBus_(0).channelCount()}')
else:
    print('❌ Микрофон недоступен')
"
```

**Ожидаемый результат**: Микрофон доступен, выводятся sample_rate и channels.

**Если ошибка**: Проверьте системные настройки → Звук → Вход.

---

## ШАГ 2: Проверка инициализации VoiceRecognitionIntegration

### Цель
Убедиться, что интеграция правильно инициализируется.

### Что проверяем

#### 2.1. Запуск приложения и проверка логов

```bash
# Запустите приложение
python client/main.py 2>&1 | tee test_logs_step2.txt

# Проверьте логи на наличие:
grep -E "(AVF|SFSpeech|VoiceRecognition)" test_logs_step2.txt
```

**Ожидаемые логи**:
```
✅ [AVF] AVFoundation аудиосистема включена
✅ [AVF] AVFAudioEngine инициализирован
🎤 [SFSpeech] Пытаемся инициализировать стриминг (context=initialize, language=en-US, on_device=True)
✅ [SFSpeech] Стриминговое распознавание готово (context=initialize, language=en-US)
```

**Если ошибки**:
- `⚠️ [SFSpeech] Недоступен` → Проверьте разрешения (Шаг 1.2)
- `❌ [SFSpeech] Ошибка инициализации` → Проверьте зависимости (Шаг 1.1)
- `ℹ️ [SFSpeech] Стриминг отключен` → Проверьте `unified_config.yaml`

---

#### 2.2. Проверка состояния после инициализации

Добавьте временный код в `voice_recognition_integration.py` после `__init__`:

```python
# В конце __init__, после всех инициализаций
logger.info("🔍 [TEST] Состояние после инициализации:")
logger.info(f"   - _use_avf: {self._use_avf}")
logger.info(f"   - _avf_engine: {self._avf_engine is not None}")
logger.info(f"   - _use_streaming: {self._use_streaming}")
logger.info(f"   - _sf_recognizer: {self._sf_recognizer is not None}")
logger.info(f"   - _streaming_feature_enabled: {self._streaming_feature_enabled}")
logger.info(f"   - _streaming_env_disabled: {self._streaming_env_disabled}")
```

**Ожидаемый результат**: Все флаги установлены правильно.

---

## ШАГ 3: Проверка открытия микрофона

### Цель
Убедиться, что микрофон открывается при `voice.recording_start`.

### Что проверяем

#### 3.1. Запуск записи (без распознавания)

Добавьте временный тест-скрипт:

```python
# test_step3.py
import asyncio
import sys
sys.path.insert(0, 'client')

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
import logging

logging.basicConfig(level=logging.INFO)

async def test_recording_start():
    event_bus = EventBus()
    state_manager = ApplicationStateManager(event_bus)
    error_handler = ErrorHandler(event_bus, state_manager)
    
    integration = VoiceRecognitionIntegration(
        event_bus, state_manager, error_handler, None
    )
    
    await integration.initialize()
    await integration.start()
    
    # Публикуем recording_start
    session_id = "test_step3_123"
    await event_bus.publish("voice.recording_start", {
        "session_id": session_id
    })
    
    # Ждём 2 секунды
    await asyncio.sleep(2)
    
    # Проверяем состояние
    is_active = state_manager.is_microphone_active()
    print(f"\n🔍 [TEST] Микрофон активен: {is_active}")
    
    # Останавливаем
    await event_bus.publish("voice.recording_stop", {
        "session_id": session_id
    })
    
    await asyncio.sleep(1)
    await integration.stop()

if __name__ == "__main__":
    asyncio.run(test_recording_start())
```

**Запуск**:
```bash
python3 test_step3.py
```

**Ожидаемый результат**:
```
✅ [AVF] Микрофон открыт (стриминг/batch) для session test_step3_123
🔍 [TEST] Микрофон активен: True
```

**Если ошибка**: Проверьте логи, найдите где именно падает.

---

#### 3.2. Проверка что audio_callback вызывается

Добавьте счётчик в `audio_callback`:

```python
# В voice_recognition_integration.py, в audio_callback
self._test_chunk_count = getattr(self, '_test_chunk_count', 0) + 1
if self._test_chunk_count <= 5:
    logger.info(f"🔍 [TEST] audio_callback вызван {self._test_chunk_count} раз: {len(data)} bytes")
```

**Ожидаемый результат**: `audio_callback` вызывается несколько раз в секунду.

**Если не вызывается**: Проблема в `AVFAudioEngine.start_input()`.

---

## ШАГ 4: Проверка стриминга (если включен)

### Цель
Убедиться, что стриминговая сессия запускается и чанки отправляются.

### Что проверяем

#### 4.1. Проверка запуска стриминговой сессии

Добавьте логи в `_start_streaming_session`:

```python
# В voice_recognition_integration.py, в _start_streaming_session
logger.info("🔍 [TEST] _start_streaming_session вызван")
logger.info(f"   - _is_streaming_active(): {self._is_streaming_active()}")
logger.info(f"   - _sf_recognizer: {self._sf_recognizer is not None}")
logger.info(f"   - recognizer state: {getattr(self._sf_recognizer, '_state', None) if self._sf_recognizer else None}")
```

**Ожидаемый результат**:
```
🎤 [SFSpeech] Стриминговая сессия запущена (session=...)
🔍 [TEST] _start_streaming_session вызван
   - _is_streaming_active(): True
   - _sf_recognizer: True
   - recognizer state: RecognitionState.RECOGNIZING
```

**Если ошибка**: Проверьте почему `start_recognition()` возвращает False.

---

#### 4.2. Проверка отправки чанков в стриминг

Добавьте логи в `audio_callback`:

```python
# В audio_callback, перед append_audio
should_stream = self._is_streaming_session_live(session_id)
logger.debug(f"🔍 [TEST] audio_callback: should_stream={should_stream}, sf_recognizer={self._sf_recognizer is not None}")

if should_stream and self._sf_recognizer is not None:
    logger.debug(f"🔍 [TEST] Вызываем append_audio: {len(data)} bytes")
    success = self._sf_recognizer.append_audio(data, sample_rate, channels)
    logger.debug(f"🔍 [TEST] append_audio вернул: {success}")
```

**Ожидаемый результат**: `append_audio` возвращает `True` для каждого чанка.

**Если `False`**: Проверьте состояние recognizer (должно быть `RECOGNIZING`).

---

#### 4.3. Проверка промежуточных результатов

Добавьте логи в `on_streaming_result`:

```python
# В _start_streaming_session, в on_streaming_result
def on_streaming_result(text: str, is_final: bool) -> None:
    logger.info(f"🔍 [TEST] on_streaming_result вызван: text='{text[:50]}...', is_final={is_final}")
    self._streaming_partial_result = text
    # ... остальной код
```

**Ожидаемый результат**: `on_streaming_result` вызывается с промежуточными результатами.

**Если не вызывается**: Проблема в SFSpeechRecognizer или коллбек не установлен.

---

## ШАГ 5: Проверка завершения стриминга

### Цель
Убедиться, что стриминг правильно завершается и возвращает результат.

### Что проверяем

#### 5.1. Проверка finish_recognition

Добавьте логи в `_on_recording_stop`:

```python
# В _on_recording_stop, перед finish_recognition
if self._is_streaming_session_live(session_id):
    logger.info("🔍 [TEST] Завершение стриминга...")
    logger.info(f"   - _streaming_partial_result: {self._streaming_partial_result}")
    logger.info(f"   - recognizer state: {getattr(self._sf_recognizer, '_state', None)}")
    
    timeout = getattr(self, '_streaming_timeout', 5.0)
    logger.info(f"   - timeout: {timeout}s")
    
    final_text = await self._sf_recognizer.finish_recognition(timeout=timeout)
    logger.info(f"🔍 [TEST] finish_recognition вернул: '{final_text[:100] if final_text else None}...'")
```

**Ожидаемый результат**: `finish_recognition` возвращает текст (или использует `_streaming_partial_result`).

**Если пустой**: Проверьте `_streaming_partial_result` (используется как fallback).

---

## ШАГ 6: Проверка batch fallback

### Цель
Убедиться, что batch распознавание работает, если стриминг недоступен.

### Что проверяем

#### 6.1. Отключение стриминга и проверка batch

```bash
# Отключите стриминг временно
export NEXY_DISABLE_STREAMING_RECOGNITION=true

# Запустите приложение и попробуйте распознавание
python client/main.py
```

**Ожидаемый результат**: Используется batch режим, аудио накапливается в буфере.

---

#### 6.2. Проверка сохранения WAV файла

```bash
# Включите сохранение аудио
export NEXY_DEBUG_SAVE_AUDIO=true

# Запустите приложение, зажмите Ctrl+N, скажите что-то, отпустите
python client/main.py

# Проверьте что файл создан
ls -lh /tmp/nexy_debug_session_*.wav

# Прослушайте файл
afplay /tmp/nexy_debug_session_*.wav
```

**Ожидаемый результат**: WAV файл создан, в нём слышен голос.

**Если только тишина**: Проблема с микрофоном или записью.

---

#### 6.3. Проверка ресемплинга

Добавьте логи в `_recognize_avf_audio`:

```python
# В _recognize_avf_audio, после ресемплинга
logger.info("🔍 [TEST] Ресемплинг выполнен:")
logger.info(f"   - original: {original_sample_rate}Hz, {original_duration_sec:.2f}s")
logger.info(f"   - resampled: {sample_rate}Hz, {resampled_duration_sec:.2f}s")
logger.info(f"   - audio_rms: {audio_rms_original:.2f} (original), {audio_rms_resampled:.2f} (resampled)")
```

**Ожидаемый результат**: Ресемплинг выполнен, RMS разумный (> 100 для голоса).

---

#### 6.4. Проверка вызова Google Speech API

Добавьте логи перед `recognize_google`:

```python
# В _recognize_avf_audio, перед recognize_google
logger.info("🔍 [TEST] Вызываем recognize_google:")
logger.info(f"   - audio_bytes: {len(audio_bytes_int16)} bytes")
logger.info(f"   - sample_rate: {sample_rate}Hz")
logger.info(f"   - language: {language}")
```

**Ожидаемый результат**: `recognize_google` вызывается и возвращает текст.

**Если `UnknownValueError`**: Проверьте WAV файл и RMS.

---

## ШАГ 7: Полный end-to-end тест

### Цель
Проверить весь поток от начала до конца.

### Сценарий

1. Запустите приложение
2. Зажмите Ctrl+N
3. Произнесите короткую фразу на английском (например, "Hello")
4. Отпустите Ctrl+N
5. Проверьте результат

**Ожидаемый результат**: 
- Микрофон открывается
- Аудио записывается
- Распознавание выполняется (стриминг или batch)
- Результат публикуется в `voice.recognition_completed`
- Текст отправляется на сервер

---

## Чек-лист для каждого шага

Для каждого шага проверьте:

- [ ] Логи не содержат ошибок (ERROR)
- [ ] Ожидаемые сообщения присутствуют в логах
- [ ] Состояние компонентов правильное
- [ ] Нет исключений (Exception)
- [ ] Время выполнения разумное (нет зависаний)

---

## Что делать если шаг не проходит

1. **Остановитесь** - не переходите к следующему шагу
2. **Проанализируйте логи** - найдите первую ошибку
3. **Проверьте схему** - посмотрите в `AUDIO_SYSTEM_FLOW_SCHEMA.md` раздел "ТОЧКИ ОТКАЗА"
4. **Исправьте проблему** - следуйте рекомендациям из схемы
5. **Повторите шаг** - убедитесь что он проходит на 100%
6. **Только потом** переходите к следующему шагу

---

## Быстрая диагностика

Если нужно быстро понять где проблема:

```bash
# Запустите с максимальным логированием
python client/main.py 2>&1 | tee full_log.txt

# Найдите все ошибки
grep -E "(ERROR|❌|⚠️)" full_log.txt

# Найдите все тестовые логи
grep "🔍 \[TEST\]" full_log.txt

# Найдите все SFSpeech логи
grep "\[SFSpeech\]" full_log.txt

# Найдите все AVF логи
grep "\[AVF\]" full_log.txt
```

---

## Готово к тестированию! 🚀

Начните с Шага 1 и двигайтесь последовательно. Не пропускайте шаги!

