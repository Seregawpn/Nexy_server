# Remote config sync: primary/fallback/model

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-22
- ID (INS-###): N/A

## Diagnosis
Удалённый сервер использовал конфигурацию, расходящуюся с локальной, что вызывало нестабильный bootstrap text_processing и циклы restart.

## Root Cause
Отсутствовала гарантированная синхронизация runtime-полей `GEMINI_API_KEY` / `GEMINI_FALLBACK_API_KEY` / `GEMINI_PRIMARY_MODEL` на VM.

## Optimal Fix
Выполнена прямая синхронизация удалённого `/home/azureuser/voice-assistant/config.env` из локального `config.env` по ключам Gemini + модель.

## Verification
- unit: `voice-assistant.service` использует `/home/azureuser/voice-assistant` как `WorkingDirectory`.
- post-check:
  - `SERVICE_STATUS=active`
  - `health`: `{"status":"OK","latest_version":"1.6.1.43","latest_build":"1.6.1.43"}`
  - за последнюю минуту нет новых ошибок инициализации.

## Информация об изменениях
- Что изменено:
  - На VM обновлены `GEMINI_API_KEY`, `GEMINI_FALLBACK_API_KEY`, `GEMINI_PRIMARY_MODEL`.
  - Перезапущен сервис `voice-assistant`.
- Файлы:
  - remote `/home/azureuser/voice-assistant/config.env`
- Причина/цель:
  - Привести удалённый runtime к локальному канону конфигурации.
- Проверка:
  - `systemctl is-active`, `/health`, свежий `journalctl`.

## Запрос/цель
Сделать на удалённом сервере такую же конфигурацию LLM, как локально.

## Контекст
- VM: `NexyNew` / RG: `NexyNewRG`
- Service: `voice-assistant`
- Repo path: `/home/azureuser/voice-assistant`

## Решения/выводы
- Конфигурация синхронизирована и сервис стабилизирован в `active`.
- В удалённом репозитории ветка остаётся `release/v2.0.0.4`; кодовый деплой не выполнялся в этой задаче.

## Открытые вопросы
- Нужна ли отдельная задача на доставку последних локальных кодовых фиксов в удалённую ветку/деплой.

## Следующие шаги
- При необходимости: выполнить отдельный кодовый deploy в `Nexy` и перепроверить production runtime.
