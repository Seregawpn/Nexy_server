# Welcome Playback Gate

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-05
- ID (INS-###): <из Docs/CRM_INSTRUCTION_REGISTRY.md>

## Diagnosis
Приветствие запускается до готовности playback, из-за чего аудио теряется.

## Root Cause
Отсутствует gate на событие playback.ready перед отправкой welcome raw audio.

## Optimal Fix
Ввести gate в WelcomeMessageIntegration, запускать приветствие только при готовности playback.

## Verification
- Логи: playback.ready перед welcome запуском.
- Приветствие слышно при старте.

## Запрос/цель
Стабилизировать воспроизведение приветствия.

## Контекст
- Файлы: integration/integrations/welcome_message_integration.py
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без изменения архитектуры

## Решения/выводы
- Добавлен gate на playback.ready и отложенный запуск.

## Открытые вопросы
- Нужны ли дополнительные логи источника shutdown?

## Следующие шаги
- Проверить поведение на чистом старте (fresh install).
