# Welcome Greeting Missing + Auto Quit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-05
- ID (INS-###): <из Docs/CRM_INSTRUCTION_REGISTRY.md>

## Diagnosis
Приветствие запускается до готовности воспроизведения и теряет аудио; авто-выключение выглядит как пользовательский quit или рестарт после разрешений.

## Root Cause
Отсутствие gate на playback.ready и start() -> playback.raw_audio уходит, когда AVFoundationPlayer еще не инициализирован -> приветствие не воспроизводится.

## Optimal Fix
Добавить gate в WelcomeMessageIntegration (ожидание playback.ready и _running) и диагностически различить auto-quit (user quit vs permission restart).

## Verification
- Логи: playback.ready до welcome_message и playback.raw_audio.
- Приветствие слышно на первом запуске.
- В логах auto-quit есть явный источник (user.quit или permission_restart).

## Запрос/цель
Разобрать: приветствие не играет и приложение само выключается.

## Контекст
- Файлы: integration/integrations/welcome_message_integration.py, integration/integrations/speech_playback_integration.py, modules/permissions/v2/integration.py, modules/tray_controller/core/tray_controller.py
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без изменения архитектуры и источников истины

## Решения/выводы
- Приветствие теряется из-за раннего вызова до готовности playback.
- Авто-выключение требует точной валидации источника (user quit vs permission restart).

## Открытые вопросы
- Есть ли в логах permission_restart.executing или Quit requested via tray menu в момент авто-выключения?

## Следующие шаги
- Добавить gate на playback.ready в welcome интеграции.
- Добавить явный лог-маркер источника shutdown.
