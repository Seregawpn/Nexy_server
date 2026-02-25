# Remote welcome audio ffmpeg path fix

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-22
- ID (INS-###): N/A

## Diagnosis
На удалённой VM `GenerateWelcomeAudio` падал с `ffmpeg not available for MP3 to PCM conversion`, несмотря на рабочий gRPC коннект.

## Root Cause
`ffmpeg` отсутствовал, затем после установки был недоступен процессу сервиса из-за урезанного systemd `PATH` (`/home/azureuser/voice-assistant/venv/bin` только).

## Optimal Fix
- Установлен `ffmpeg` на VM.
- Добавлен systemd override для `voice-assistant` с полным PATH, включающим `/usr/bin`.
- Перезапущен сервис.
- Прогнан серверный тест `server/scripts/test_welcome_audio.py --host localhost --port 50051`.

## Verification
- До фикса: тест welcome падал с `ffmpeg not available for MP3 to PCM conversion`.
- После фикса: тест прошёл успешно (`152` аудио чанка, `617472` байт).
- Сервис после фикса: `systemctl is-active voice-assistant` -> `active`.

## Информация об изменениях
- Что изменено:
  - runtime fix на VM: установка ffmpeg + systemd PATH override.
  - добавлен preflight guard на ffmpeg.
  - в `/health` добавлен флаг `ffmpeg_available`.
- Файлы:
  - remote `/etc/systemd/system/voice-assistant.service.d/override.conf`
  - `server/scripts/preflight_check.sh`
  - `server/main.py`
- Причина/цель:
  - восстановить основной серверный путь welcome TTS без клиентского fallback.
- Проверка:
  - remote welcome test + service status + локальная py/shell syntax validation.

## Запрос/цель
Убрать серверный сбой welcome-аудио на удалённом хосте.

## Контекст
- VM: `NexyNew` (RG: `NexyNewRG`)
- Service: `voice-assistant`
- Симптом: `ffmpeg not available for MP3 to PCM conversion`

## Решения/выводы
- Проблема была в runtime dependency + service PATH, не в клиенте.
- После фикса welcome-аудио снова идёт по server path.

## Открытые вопросы
- Нужен ли отдельный автоматический post-deploy smoke, который всегда вызывает `GenerateWelcomeAudio`.

## Следующие шаги
- Закрепить деплой-процесс: запуск preflight с ffmpeg check до restart/publish.
