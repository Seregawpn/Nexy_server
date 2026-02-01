# Offline Notary Guard

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-30
- ID (INS-###): INS-005

## Diagnosis
Нотаризация падает при офлайне (CloudKit), хотя локальная подпись валидна.

## Root Cause
Скрипт всегда запускает notarization submit/staple без проверки доступности CloudKit.

## Optimal Fix
Добавить опциональную проверку доступности CloudKit и авто-пропуск нотаризации при офлайне.

## Verification
Сборка не падает при отсутствии сети; при наличии сети — нотарификация выполняется.

## Запрос/цель
Добавить guard в packaging script, чтобы не падать на validate при офлайне.

## Контекст
- Файлы: client/packaging/build_final.sh
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без изменения pipeline шагов при наличии сети

## Решения/выводы
- Добавлен флаг NEXY_SKIP_NOTARIZATION_IF_OFFLINE (default=1) с проверкой CloudKit через curl.

## Открытые вопросы
- Нужно ли выключать auto-skip в CI (если есть)?

## Следующие шаги
- Пересобрать и проверить поведение офлайн/онлайн.
