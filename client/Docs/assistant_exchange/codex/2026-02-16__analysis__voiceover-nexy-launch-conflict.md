# Analysis: VoiceOver + Nexy launch conflict

## Context
Проверка конфликтов между запуском `VoiceOver` и `Nexy` по логам `log.md` и `voiceover.md`.

## Findings
- Конфликт подтвержден на уровне аудио-арбитража:
  - `audiomxd` фиксирует одновременно две `Primary` сессии (`Nexy` и `VoiceOver`) и не выбирает владельца: `will use session={clientName:'(null)', displayID:'(null)'}`.
  - Это повторяется минимум в двух окнах: `17:07:07` и `17:07:22`.
- В те же окна у `Nexy` наблюдается флаппинг аудио-состояния:
  - переходы `input_running: true -> false`, `starting recording -> stopping recording`, `beginInterruption/endInterruption`.
- На стороне `VoiceOver` в те же периоды повторяются ошибки буфера:
  - `AVAudioBuffer.mm:281 mBuffers[0].mDataByteSize (0) should be non-zero`.
- Косвенный системный признак конкуренции за audio route:
  - `coreaudiod` IO error report с `other_active_clients`, где одновременно присутствуют `com.apple.VoiceOver` и `com.nexy.assistant`.

## Verification
- Проверенные источники:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/log.md`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/voiceover.md`
- Ключевые маркеры:
  - `log.md`: `shouldRequestForForceHijack ... Found 2 different sessions ... will use session=(null)`.
  - `voiceover.md`: тот же `audiomxd` маркер + синхронные ошибки `AVAudioBuffer.mm:281`.

## Информация об изменениях
- Что изменено:
  - Добавлен отчёт анализа конфликта VoiceOver/Nexy.
- Список файлов:
  - `Docs/assistant_exchange/codex/2026-02-16__analysis__voiceover-nexy-launch-conflict.md`
- Причина/цель изменений:
  - Зафиксировать подтверждение конфликта и воспроизводимые сигналы для последующего фикса.
- Проверка (что выполнено для валидации):
  - Сопоставление временных окон и событий аудио-арбитража в двух логах.
