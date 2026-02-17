# Analysis

## Context
Проверен сценарий Dev-запуска, где при BrowserUse шагах не слышна озвучка прогресса.

## Findings
- В Dev включены `actions` и `browser` (`config/unified_config.yaml`), а `ActionExecutionIntegration` в `development` включается по умолчанию.
- Browser runtime TTS централизованно подавляется при активном playback:
  - `BROWSER_TTS suppressed ... reason=playback_active_same_session`
  - `BROWSER_TTS suppressed ... reason=playback_active_other_session`
- Подтверждено в логе:
  - `/Users/sergiyzasorin/Library/Logs/Nexy/nexy-dev.log` строки ~12700, ~13095, ~15646.
- Это не отдельный Dev-баг маршрутизации аудио: это owner-guard в `BrowserUseIntegration._should_suppress_browser_runtime_tts`.

## Verification
- Проверены источники:
  - `integration/integrations/browser_use_integration.py`
  - `integration/core/integration_factory.py`
  - `config/unified_config.yaml`
  - `/Users/sergiyzasorin/Library/Logs/Nexy/nexy-dev.log`
- Команды:
  - `rg` по suppress/tts/playback/browser
  - просмотр секций конфигурации и runtime-логов

## Информация об изменениях
- Изменения не вносились.
- Список файлов (только анализ):
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__analysis__dev-browser-step-audio-suppression.md`
- Причина/цель изменений:
  - Зафиксировать root-cause Dev-сценария “browser steps without speech”.
- Проверка (что выполнено для валидации):
  - Сопоставление логов suppress с кодовым guard-путем.
