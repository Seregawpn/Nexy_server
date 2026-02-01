# Packaged App Debug Plan (Browser/Close/Payment)

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-30
- ID (INS-###): INS-005

## Diagnosis
Проблемы в packaged app связаны с зависимостью от Python/MCP и отсутствием драйверов Playwright внутри bundle, из-за чего browser-use и close_app ломаются в frozen окружении.

## Root Cause
PyInstaller bundle не содержит драйвер Playwright, а MCP запускается через sys.executable (в bundled app это сама .app) → MCP скрипты не исполняются, инициализация browser/close_app падает.

## Optimal Fix
Цель: восстановить работоспособность browser-use и close_app в packaged app через штатные точки интеграции, без дублирования логики.

## Verification
Проверка работоспособности через manual тесты packaged app (browser-use, close_app, self-close), без регрессии в non-packaged.

## Запрос/цель
Сформировать план внедрения fixes для browser-use, close_app и проверки PaymentIntegration в packaged macOS app.

## Контекст
- Файлы: client/packaging/Nexy.spec, client/integration/integrations/action_execution_integration.py, client/integration/integrations/browser_use_integration.py, client/modules/browser_automation/module.py, client/integration/integrations/payment_integration.py
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без реархитектуры, без новых источников истины

## Решения/выводы
- Центральная точка исполнения действий — ActionExecutionIntegration; fallback для close_app должен жить там.
- Для browser-use ключевой блокер — отсутствие Playwright driver в bundle.

## Открытые вопросы
- Нужно ли добавлять уникальный путь/переменную окружения для playwright driver в frozen env?
- Есть ли отдельные ошибки PaymentIntegration в packaged логах (aiohttp import/host)?

## Следующие шаги
- Добавить сбор Playwright driver в Nexy.spec.
- Добавить osascript fallback в close_app.
- Усилить логирование browser_use initialize.
