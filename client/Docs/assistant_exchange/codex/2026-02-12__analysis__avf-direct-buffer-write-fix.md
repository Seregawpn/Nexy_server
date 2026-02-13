# AVF direct buffer write fix

## Context
Пользователь сообщает, что аудио "по логам идет", но фактически не слышно.

## Diagnosis
В playback loop использовался хрупкий путь записи в `AVAudioPCMBuffer` через `objc.varlist` indexed assignment + test write.
Это могло давать ложноположительную диагностику при нестабильной записи в фактическую память буфера.

## Fix
- В `modules/speech_playback/core/avf_player.py` запись в буфер переведена на стабильный путь:
  - `ptr.as_buffer(frame_count)` -> `memoryview`
  - `np.frombuffer(..., dtype=np.float32, count=frame_count)`
  - прямое присваивание `dst[:] = audio_contiguous`
- Убран неиспользуемый `ctypes` import.

## Why architecture-safe
- Логика не вынесена наружу; owner остаётся `AVFoundationPlayer`.
- Source of truth не менялся: playback runtime внутри AVF player.
- Новых состояний не добавлено.

## Verification
- `python3 -m py_compile modules/speech_playback/core/avf_player.py` — OK.
