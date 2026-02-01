# Client Browser Use Plan

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-18
- ID (INS-###): INS-005

## Diagnosis
Требование: все браузерные действия и установка Chromium должны происходить на клиенте, а не на удаленном сервере.

## Root Cause
`browser_use` реализован как серверный модуль → сервер выполняет Playwright/Chromium → выполнение не локально.

## Optimal Fix
Перенести ownership и исполнение browser automation на клиент, сервер оставить только для LLM и маршрутизации intents.

## Verification
Клиент выполняет установку Chromium и browser tasks; сервер не инициирует установку и не запускает браузер.

## Запрос/цель
Сформировать требования и план реализации с учетом текущей клиентской архитектуры.

## Контекст
- Файлы: server/modules/browser_use/module.py, server/modules/grpc_service/core/grpc_service_manager.py
- Файлы клиента: client/integration/core/simple_module_coordinator.py, client/integration/integrations/, client/modules/
- Документы: Docs/PROJECT_REQUIREMENTS.md, client/Docs/ARCHITECTURE_OVERVIEW.md

## Решения/выводы
- Единый владелец браузерной автоматизации должен быть на клиенте.
- Установка Chromium должна быть частью client module init с single-flight.

## Открытые вопросы
- Сервер должен только выдавать intent или совсем исключить browser_use из gRPC?

## Следующие шаги
- Подтвердить контракт gRPC и перечень событий EventBus.
- Перейти к реализации по плану ниже.
