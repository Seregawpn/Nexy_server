# PTT Flow Dedup And Replay Order

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): N/A (не указан в контексте)

## Diagnosis
- В PTT цепочке обнаружены две зоны нестабильности: дублирующий terminal `voice.mic_closed` в рамках одной сессии и гонка порядка между `app.mode_changed(PROCESSING)` и replay `screenshot.captured`.
- Эффект: шум событий, ложные терминальные переходы подписчиков и периодический ложный `скриншот=False` в summary `ProcessingWorkflow`.

## Root Cause
- Причина/арх-нарушение: dedup `voice.mic_closed` был source-scoped, а не session-scoped.
- Механизм: публикация из нескольких terminal веток (`recording_stop`, `v2_completed`, `v2_failed`) с разным `source` проходила dedup.
- Эффект: несколько `voice.mic_closed` на одну и ту же сессию.
- Причина/арх-нарушение: replay `screenshot.captured` выполнялся синхронно в обработчике `app.mode_changed`.
- Механизм: часть подписчиков еще не успевала перейти в ACTIVE и отфильтровывала событие как нерелевантное.
- Эффект: метрика `screenshot_captured` в workflow иногда не выставлялась.

## Optimal Fix
- Goal: стабилизировать terminal path и упорядочить replay без новых сущностей/флагов.
- Architecture Fit: правки в владельцах событий (`VoiceRecognitionIntegration`, `ScreenshotCaptureIntegration`), без обхода coordinator/state manager.
- Where it belongs: integration layer (`integration/integrations/*`) + локальная чистка workflow.
- Source of Truth:
  - `voice.mic_closed` owner: `VoiceRecognitionIntegration`
  - `screenshot.captured` owner/replay: `ScreenshotCaptureIntegration`
  - режимы: `ModeManagementIntegration` + `ApplicationStateManager`
- Breaks architecture: no

- Implementation Plan:
  - Перевести dedup `voice.mic_closed` на session-scoped policy (once-per-session, TTL cleanup).
  - Сдвинуть replay `screenshot.captured` после `app.mode_changed` на следующий event-loop tick.
  - Убрать локальное дублирование `completed_stages.clear()` в `ProcessingWorkflow`.

- Code Touchpoints:
  - `/Users/sergiyzasorin/Fix_new/client/integration/integrations/voice_recognition_integration.py`
  - `/Users/sergiyzasorin/Fix_new/client/integration/integrations/screenshot_capture_integration.py`
  - `/Users/sergiyzasorin/Fix_new/client/integration/workflows/processing_workflow.py`

- Concurrency Guard (if needed):
  - idempotency: once-per-session на `voice.mic_closed`
  - ordering guard: delayed replay (`asyncio.sleep(0)`) для `screenshot.captured`

- What to remove / merge:
  - merged: дубли terminal-публикаций `voice.mic_closed` в единый session-level guard.
  - removed: лишний повтор `completed_stages.clear()` при старте processing chain.

## Verification
- DoD:
  - В рамках одной `session_id` публикуется максимум один `voice.mic_closed`.
  - Replay `screenshot.captured` корректно доходит до `ProcessingWorkflow`.
  - Финальный summary корректно отражает факт скриншота при early-capture + replay.

- Steps:
  - Локальная проверка синтаксиса: `python3 -m py_compile` для 3 измененных файлов.
  - Проверка наличия новых guard/ordering точек через `rg`.

- Expected behavior/logs:
  - `VOICE: mic_closed dedup skipped (session=..., source=...)` при повторной попытке в той же сессии.
  - `ScreenshotCapture: replay screenshot.captured ...` и последующий прием в `ProcessingWorkflow`.

- Regression checks:
  - Семантика mode transitions не меняется.
  - Новых feature flags/state axes не добавлено.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы:
  - `/Users/sergiyzasorin/Fix_new/AGENTS.md`
  - `/Users/sergiyzasorin/Fix_new/client/AGENTS.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/DOCS_INDEX.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/PRE_CHANGE_CHECKLIST.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/PROJECT_REQUIREMENTS.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/ARCHITECTURE_OVERVIEW.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/FEATURE_FLAGS.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/FLOW_INTERACTION_SPEC.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/STATE_CATALOG.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/DOCS_INDEX.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/PRE_CHANGE_CHECKLIST.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/CODEX_PROMPT.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/ANTIGRAVITY_PROMPT.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/assistant_exchange/TEMPLATE.md`

- Source of Truth:
  - События микрофона: `VoiceRecognitionIntegration`
  - События скриншота: `ScreenshotCaptureIntegration`
  - Режимы/сессии: `ModeManagementIntegration` + `ApplicationStateManager`

- Дублирование:
  - `voice.mic_closed` дублировался из разных terminal источников в пределах одной session.
  - `completed_stages.clear()` дублировался при старте processing chain.

- Feature Flags check:
  - Новые flags не добавлялись, пересечений с `/Users/sergiyzasorin/Fix_new/client/Docs/FEATURE_FLAGS.md` нет.

- Race check:
  - scenario: replay `screenshot.captured` публикуется до перехода workflow в ACTIVE.
  - guard: deferred publish после `await asyncio.sleep(0)`.

## Запрос/цель
- Провести общий архитектурный аудит по runtime flow и устранить найденные проблемные места без реархитектуры.

## Контекст
- Файлы:
  - `/Users/sergiyzasorin/Fix_new/client/integration/integrations/voice_recognition_integration.py`
  - `/Users/sergiyzasorin/Fix_new/client/integration/integrations/screenshot_capture_integration.py`
  - `/Users/sergiyzasorin/Fix_new/client/integration/workflows/processing_workflow.py`
- Ограничения:
  - Без новых state axes/feature flags.
  - Без обхода централизованного mode/event ownership.

## Решения/выводы
- Основной путь событий сохранен; исправлены точечные race/duplication дефекты в владельцах событий.
- Риск регрессии низкий, так как изменения локализованы и не меняют контракты payload.

## Открытые вопросы
- Требуется runtime-прогон на реальном сценарии PTT для подтверждения отсутствия дублей в production-логах.

## Следующие шаги
- Прогнать 3-5 ручных PTT сессий и проверить:
  - один `voice.mic_closed` на session,
  - корректный `screenshot=True` в финальном summary processing.
