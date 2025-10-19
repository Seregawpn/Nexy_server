# Очистка диагностических изменений

## ⚠️ ВАЖНО: Удалите диагностические изменения после сбора данных

После завершения диагностики **обязательно удалите** все временные изменения из кода:

### 1. config/unified_config.yaml
```yaml
# Строка 57: верните обратно
enable_debug_logging: false  # было: true
```

### 2. modules/voice_recognition/core/speech_recognizer.py

#### Удалите диагностические логи (строки ~308-315):
```python
# УДАЛИТЬ эти строки:
# ДИАГНОСТИКА: Логируем параметры ПЕРЕД открытием потока
logger.info("🔧 Открываем InputStream:")
logger.info("   device_id=%s", device_id)
logger.info("   samplerate=%s", self.actual_input_rate)
logger.info("   channels=%s", self.actual_input_channels)
logger.info("   dtype=float32")
logger.info("   blocksize=%s", self.config.chunk_size)
```

#### Удалите диагностику потока (строки ~320-327):
```python
# УДАЛИТЬ эти строки:
# ДИАГНОСТИКА: Проверяем состояние потока
logger.info("✅ InputStream открыт:")
logger.info("   active=%s", stream.active)
logger.info("   device=%s", stream.device)
logger.info("   samplerate=%s", stream.samplerate)
logger.info("   channels=%s", stream.channels)
```

#### Удалите детальный анализ чанков (строки ~345-370):
```python
# УДАЛИТЬ эти строки:
# ДИАГНОСТИКА: Анализируем КАЖДЫЙ чанк
chunk_peak = float(np.max(np.abs(indata)))
chunk_rms = float(np.sqrt(np.mean(indata.astype(np.float64) ** 2)))
chunk_num = len(self.audio_data)

if chunk_num == 1:
    logger.info(
        "🔊 Первый чанк: frames=%s, dtype=%s, shape=%s",
        frames,
        indata.dtype,
        indata.shape,
    )
    logger.info("   📊 Первые 10 значений: %s", indata[:10].flatten().tolist())
    logger.info("   📊 Peak=%.6f, RMS=%.6f", chunk_peak, chunk_rms)
elif chunk_num <= 5:
    # Первые 5 чанков
    logger.info("   Chunk %d: Peak=%.6f, RMS=%.6f", chunk_num, chunk_peak, chunk_rms)
elif chunk_num % 20 == 0:
    # Каждый 20-й чанк
    logger.debug("   Chunk %d: Peak=%.6f, RMS=%.6f", chunk_num, chunk_peak, chunk_rms)

# Предупреждение если сигнал нулевой
if chunk_num <= 20 and chunk_peak == 0.0:
    logger.warning("   ⚠️ Chunk %d: НУЛЕВОЙ СИГНАЛ! (peak=0, rms=%.6f)", chunk_num, chunk_rms)
```

#### Удалите сохранение WAV файла (строки ~374-383):
```python
# УДАЛИТЬ эти строки:
# Временная диагностика - сохранение сырого WAV файла
import wave
import pathlib
capture_path = pathlib.Path("~/Desktop/nexy_capture.wav").expanduser()
with wave.open(str(capture_path), "wb") as wf:
    wf.setnchannels(self.actual_input_channels)
    wf.setsampwidth(2)
    wf.setframerate(int(self.actual_input_rate))
    wf.writeframes((audio_data * 32767).astype("int16").tobytes())
logger.info(f"🔍 Диагностический WAV сохранен: {capture_path}")
```

### 3. Восстановите оригинальный код

После удаления диагностики код должен вернуться к оригинальному виду:

```python
# В _run_listening():
with sd.InputStream(
    device=device_id,
    samplerate=self.actual_input_rate,
    channels=self.actual_input_channels,
    dtype='float32',
    blocksize=self.config.chunk_size,
    callback=self._audio_callback,
):
    while self.is_listening and not self.stop_event.is_set():
        time.sleep(0.1)

# В _audio_callback():
if self.is_listening:
    with self.audio_lock:
        self.audio_data.append(indata.copy())
        if len(self.audio_data) == 1:
            logger.debug(
                "🔊 Первый чанк получен: frames=%s, dtype=%s",
                frames,
                indata.dtype,
            )
```

### 4. Удалите временные файлы

```bash
# Удалите диагностические файлы
rm -rf ~/Desktop/nexy_diagnostics/
rm -f ~/Desktop/nexy_capture.wav

# Удалите диагностические скрипты
rm -f collect_audio_diagnostics.sh
rm -f AUDIO_DIAGNOSTICS_INSTRUCTIONS.md
rm -f CLEANUP_DIAGNOSTICS.md
```

### 5. Проверьте git статус

```bash
git status
git diff
```

Убедитесь, что все диагностические изменения удалены и не попадут в коммит.

## 🎯 Итог

После очистки:
- ✅ Код вернулся к оригинальному состоянию
- ✅ Временные файлы удалены
- ✅ Логирование вернулось к нормальному уровню
- ✅ WAV файлы с личными данными удалены
- ✅ Готово к коммиту без диагностического кода
