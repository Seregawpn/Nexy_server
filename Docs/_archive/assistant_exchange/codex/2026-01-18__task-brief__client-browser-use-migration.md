# Client Browser Use Migration

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-18
- ID (INS-###): INS-005

## Diagnosis
Browser automation и установка Chromium сейчас выполняются на сервере, что противоречит требованию выполнять все действия на клиенте.

## Root Cause
`browser_use` является серверным модулем → сервер запускает Playwright и Chromium → клиент не является владельцем выполнения.

## Optimal Fix
Перенести выполнение `browser_use` и установку Chromium на клиентскую часть, сервер оставить только для LLM/обработки запросов.

## Verification
Клиент локально устанавливает Chromium и выполняет браузерные задачи, сервер не инициирует установку браузера.

## Запрос/цель
Перепланировать архитектуру так, чтобы все браузерные действия и установка происходили на клиенте.

## Контекст
- Файлы: server/modules/browser_use/module.py, server/modules/grpc_service/core/grpc_service_manager.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md, client/Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без новой архитектуры, сохранить EventBus и централизацию

## Решения/выводы
- Единый владелец browser automation должен быть на клиенте.
- Сервер не должен запускать `playwright install chromium`.

## Открытые вопросы
- Нужно ли, чтобы сервер вообще принимал `browser_use` команды, или клиент будет решать локально?
- Нужны ли прогресс‑события `browser.progress` как сейчас?

## Следующие шаги
- Утвердить перенос ownership на клиент.
- Подготовить детальный план изменений client/server.
