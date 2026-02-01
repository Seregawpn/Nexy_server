# Проверка использования библиотеки SpeechRecognition

## Текущее использование

### 1. Создание AudioData ✅
```python
audio_data_obj = sr.AudioData(audio_bytes_int16, sample_rate, 2)
```
- `frame_data`: `audio_bytes_int16` (bytes) ✅
- `sample_rate`: `sample_rate` (16000Hz после ресемплинга) ✅
- `sample_width`: `2` (int16 = 2 bytes) ✅

**Соответствует документации**: `AudioData(frame_data, sample_rate, sample_width)`

### 2. Вызов recognize_google ✅
```python
text = recognizer.recognize_google(audio_data_obj, language=language, show_all=False)
```
- `audio_data`: `audio_data_obj` (AudioData) ✅
- `language`: `language` (en-US) ✅
- `show_all`: `False` ✅

**Соответствует документации**: `recognize_google(audio_data, language=None, key=None, pfilter=1, show_all=False, with_confidence=False)`

### 3. Создание Recognizer ✅
```python
recognizer = sr.Recognizer()
```
или
```python
recognizer = self._recognizer.recognizer
```

**Соответствует документации**: Стандартное использование

## Потенциальные проблемы

### 1. Формат аудио перед созданием AudioData
**Текущий код**:
```python
# Конвертируем int16 → float32 и нормализуем
audio_array_float32 = audio_array_int16.astype(np.float32) / 32767.0

# Если многоканальное - усредняем до моно
if channels > 1:
    frame_count = len(audio_array_float32) // channels
    audio_array_float32 = audio_array_float32[:frame_count * channels].reshape(frame_count, channels).mean(axis=1)
else:
    frame_count = len(audio_array_float32)

# Ресемплинг до 16kHz
audio_array_float32 = signal.resample(audio_array_float32, num_samples)

# Конвертируем обратно в int16
audio_array_int16_resampled = (np.clip(audio_array_float32, -1.0, 1.0) * 32768.0).astype(np.int16)
audio_bytes_int16 = audio_array_int16_resampled.tobytes()
```

**Проблема**: При нормализации используется `/ 32767.0`, но при обратной конвертации используется `* 32768.0`. Это может привести к небольшому искажению.

**Рекомендация**: Использовать одинаковый множитель:
```python
# Нормализация: [-32768, 32767] → [-1.0, 1.0]
audio_array_float32 = audio_array_int16.astype(np.float32) / 32768.0

# Обратная конвертация: [-1.0, 1.0] → [-32768, 32767]
audio_array_int16_resampled = (np.clip(audio_array_float32, -1.0, 1.0) * 32768.0).astype(np.int16)
```

### 2. Тишина в начале/конце аудио
**Проблема**: Google Speech API может возвращать `UnknownValueError` если в начале/конце много тишины.

**Текущее состояние**: Первые 10 samples = `[0, 0, 0, ...]` - это тишина!

**Рекомендация**: Добавить обрезку тишины (VAD - Voice Activity Detection) перед отправкой в Google.

### 3. Длительность аудио
**Текущее состояние**: Duration = 21.16s (слишком длинное)

**Проблема**: Google Speech API может иметь проблемы с очень длинным аудио, особенно если большая часть - тишина.

**Рекомендация**: 
- Обрезать тишину в начале/конце
- Разбивать длинное аудио на сегменты (если > 10s)

### 4. Проверка формата перед созданием AudioData
**Текущий код**:
```python
# ✅ ПРОВЕРКА: Валидация формата перед созданием AudioData
if len(audio_bytes_int16) == 0:
    logger.error(f"❌ [AVF] Пустой аудио буфер после обработки!")
    return
```

**Рекомендация**: Добавить дополнительные проверки:
```python
# Проверка что аудио не пустое
if len(audio_bytes_int16) == 0:
    logger.error(f"❌ [AVF] Пустой аудио буфер после обработки!")
    return

# Проверка что sample_rate правильный
if sample_rate != 16000:
    logger.warning(f"⚠️ [AVF] Sample rate не 16kHz: {sample_rate}Hz")

# Проверка что аудио не только тишина
if audio_rms_resampled < 50:
    logger.warning(f"⚠️ [AVF] RMS очень низкий ({audio_rms_resampled:.2f} < 50), возможно тишина")
```

## Вывод

✅ **Использование библиотеки SpeechRecognition правильное** - мы правильно создаём `AudioData` и вызываем `recognize_google()`.

⚠️ **Проблема не в подключении библиотеки**, а в:
1. **Качестве аудио** - много тишины в начале/конце
2. **Длительности аудио** - 21.16s (слишком длинное)
3. **Формате данных** - небольшая асимметрия в нормализации (32767 vs 32768)

## Рекомендации

1. ✅ Исправить нормализацию (использовать 32768 везде)
2. ⏳ Добавить обрезку тишины (VAD) перед отправкой в Google
3. ⏳ Ограничить длительность аудио (максимум 10-15 секунд)
4. ⏳ Прослушать WAV файл для проверки качества аудио

