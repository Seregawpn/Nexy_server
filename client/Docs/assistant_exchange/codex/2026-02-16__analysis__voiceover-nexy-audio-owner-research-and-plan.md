# Analysis: VoiceOver + Nexy audio owner research and implementation plan

## Context
Проведен аудит архитектуры, runtime-кода и флагов для конфликта VoiceOver/Nexy при запуске и записи.

## Verification
- Изучены архитектурные документы:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/ARCHITECTURE_OVERVIEW.md`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/PROJECT_REQUIREMENTS.md`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/STATE_CATALOG.md`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/FLOW_INTERACTION_SPEC.md`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/FEATURE_FLAGS.md`
- Проверены owner-гейты и interaction matrix:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/scripts/verify_architecture_guards.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/config/interaction_matrix.yaml`
- Исследованы ключевые runtime-модули:
  - `integration/integrations/voice_recognition_integration.py`
  - `modules/voice_recognition/core/google_sr_controller.py`
  - `integration/integrations/speech_playback_integration.py`
  - `integration/integrations/mode_management_integration.py`
  - `integration/integrations/input_processing_integration.py`
  - `integration/integrations/interrupt_management_integration.py`
  - `integration/integrations/voiceover_ducking_integration.py`
  - `modules/voiceover_control/core/controller.py`
- Подтверждены конфликтные маркеры в логах:
  - `log.md`, `voiceover.md` (конкурирующие primary sessions в `audiomxd`).

## Findings
- Конфликт проявляется в системном audio arbitration (`audiomxd`): одновременно `Nexy` и `VoiceOver` как `Primary` с `will use session=(null)`.
- На стороне Nexy в те же окна фиксируется флаппинг input/start-stop, что усиливает гонку route/session.
- VoiceOver ducking сейчас не root-cause: в конфиге `accessibility.voiceover_control.enabled=false`.
- В STT path найден дублирующий callback completion:
  - `modules/voice_recognition/core/google_sr_controller.py:299-301` (двойной `_on_completed(result)` в текущей ветке).
- Ввод/распознавание/воспроизведение уже имеют локальные guard-ы, но owner-правило аудио-арбитража между STT и playback не оформлено как единая policy-ось.

## Risks
- Вторичный owner-path в формате локальных workaround (в отдельных интеграциях) нарушит One Event One Owner.
- Попытка быстро «приглушить» VoiceOver через ducking не решит корневой конфликт аудио-сессий.

## Информация об изменениях
- Что изменено:
  - Добавлен аналитический отчет и план внедрения.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-16__analysis__voiceover-nexy-audio-owner-research-and-plan.md`
- Причина/цель изменений:
  - Зафиксировать результат полного исследования архитектуры/кода/флагов и подготовить архитектурно-валидный план фикса.
- Проверка (что выполнено для валидации):
  - Сверка логов конфликтов + audit owner-цепочек и runtime guards в коде.
