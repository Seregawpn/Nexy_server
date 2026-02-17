# Task Brief: BrowserUse macOS runtime preflight and VoiceOver-safe path

## Context
В установленном macOS app browser-use падал в runtime (`uvx` not found), а также была ошибка `chromium_executable is not defined`.
Нужно убрать дубли/конфликты путей запуска и сделать поведение предсказуемым для app-режима без влияния на VoiceOver/focus.

## Diagnosis
Был нецентрализованный fallback-путь внутри browser-use (локальный installer/watchdog), который активировался при некорректной инициализации профиля/браузера.
Это приводило к `uvx`-зависимости и шумным авариям.

## Architecture Fit
- Owner готовности browser runtime: `BrowserUseModule` (preflight + policy gate).
- Owner mode transitions не тронут: `ModeManagementIntegration`.
- Второй путь принятия решений сокращен: fail-fast вместо каскада внутренних fallback.

## Changes
1. `modules/browser_automation/module.py`
- Добавлен единый policy gate runtime-install:
  - `_is_frozen_runtime()`
  - `_allow_runtime_install()` (по умолчанию: `False` для frozen app, `True` для dev)
  - `_is_command_available()`
- Инициализация:
  - eager install запускается только если policy разрешает runtime install.
- `process()`:
  - при отсутствии preinstalled runtime в app-mode — контролируемый `BROWSER_TASK_FAILED` (`browser_runtime_missing_preinstalled_chromium_required`) и `return`.
  - добавлен явный preflight на `chromium_executable`; в app-mode при отсутствии runtime + `uvx` → детерминированная ошибка.
  - `_run_agent(...)` теперь получает `chromium_executable` параметром (fix `name 'chromium_executable' is not defined`).
- `_run_agent()`:
  - fail-fast при ошибке `BrowserProfile` (`browser_profile_init_failed:*`), без провала в внутренний `uvx` fallback.
  - recursive retry path также передает `chromium_executable`.

2. `config/unified_config.yaml`
- Добавлен флаг:
  - `browser_use.allow_runtime_install: false`
  - Это фиксирует app-политику для macOS установленного приложения.

## Concurrency / Race Guard
- Устранен дублирующий fallback path запуска браузера (fail-fast single owner).
- Нет новых shared-state флагов вне owner-модуля.
- Поведение стало идемпотентным: runtime readiness проверяется централизованно до старта Agent.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py integration/integrations/browser_use_integration.py` — OK.
- Проверка наличия новых guards/параметров через `rg` — OK.

## Информация об изменениях
- Что изменено:
  - Централизован preflight browser runtime.
  - Убрана аварийная зависимость от внутреннего `uvx` fallback в app-сценарии.
  - Исправлен bug с `chromium_executable` scope.
- Список файлов:
  - `modules/browser_automation/module.py`
  - `config/unified_config.yaml`
- Причина/цель изменений:
  - Обеспечить корректную работу в установленном macOS app, без dev-runtime зависимостей и без побочных focus-эффектов.
- Проверка:
  - Выполнен `py_compile`; guards и новые коды ошибок подтверждены поиском по коду.
