# Analysis: VoiceOver Log Conflict Check (Latest) (2026-02-17)

## Goal
Проверить актуальный `voiceover.md` на наличие конфликтов аудиосессий и определить, есть ли regression.

## Source
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/voiceover.md` (4900 lines)

## Metrics
- `Found 2 different sessions`: `18`
- `_StartIO error 35`: `11`
- `AudioDeviceDuck(...)`: `36`
- `mDataByteSize(0)`: `0`
- `org.python.python` references: `17`

## Key evidence
- Python vs VoiceOver conflict examples:
  - line `982`
  - line `1118`
  - line `2298`
  - line `2574` .. `2603`
  - line `2791`, `2853`, `2874`, `3017`, `3096`, `4356`
- `_StartIO error 35` burst examples:
  - line `2543`, `2558`, `2565`, `2570`
  - line `2658`
  - line `2816`, `2834`, `2847`
  - line `2916`, `2952`, `2964`

## Conclusion
- Конфликт присутствует и значимый: активные force-hijack события между `org.python.python` и `VoiceOver`.
- Ducking работает, но coexistence в этой сессии нестабильный.

## Verification
- `rg -c "Found 2 different sessions" voiceover.md` -> 18
- `rg -c "_StartIO\(\): Start failed - StartAndWaitForState returned error 35" voiceover.md` -> 11
- `rg -c "AudioDeviceDuck\(" voiceover.md` -> 36
- `rg -c "mDataByteSize\(0\)" voiceover.md` -> 0

## Информация об изменениях
- Что изменено:
  - Изменения в код не вносились.
  - Выполнен анализ актуального лога и зафиксированы метрики.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__analysis__voiceover-log-conflict-check-latest.md`
- Причина/цель изменений:
  - Подтвердить факт наличия/отсутствия конфликта в текущем runtime.
- Проверка (что выполнено для валидации):
  - Подсчет сигнатур и сверка с конкретными строками лога.

Изменения не вносились.
