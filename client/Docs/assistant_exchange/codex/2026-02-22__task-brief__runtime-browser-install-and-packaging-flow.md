# Runtime Browser Install + Packaging Flow

## Context
Переведен клиент на модель runtime-установки Chromium (на машине пользователя при первом запуске), без предвложения Chromium в `PKG/DMG`.

## Diagnosis
Сборочный owner-path требовал prebuilt bundled Chromium и блокировал runtime install в модуле браузера. Это создавало конфликт владельцев и ломало ожидаемый UX установки на конечной машине.

## Root Cause
- Runtime owner (`BrowserUseModule`) был принудительно отключен (`raise RuntimeError`).
- Packaging owner (`packaging/build_final.sh`) требовал и вшивал bundled Chromium в `.app`.
- В результате существовали несовместимые правила: runtime install запрещен, но без prebundle запуск не работает.

## Implementation
1. Реактивирован runtime install Chromium в `BrowserUseModule`:
- удалены fail-fast `RuntimeError` в `_ensure_browser_installed` и `_get_or_start_install_task`;
- в `process()` добавлен owner-flow:
  - если браузер отсутствует и runtime install разрешен -> запускается/ожидается single-flight install task;
  - если install disabled -> controlled fail с `browser_runtime_install_disabled`.

2. Обновлен UX статусов установки в `BrowserUseIntegration`:
- обработка `started`, `downloading`, `completed`, `already_installed`, `failed`;
- сообщения идут через startup-очередь (`_queue_or_publish_startup_tts`) и звучат после welcome.

3. Конфиг переключен на runtime install:
- `browser_use.allow_runtime_install: true`.

4. Packaging переведен на no-bundle Chromium:
- убраны strict-gates, завязанные на bundled Chromium;
- удалена обязательная валидация packaged Chromium runtime;
- оставлена проверка Playwright driver в `.app` (`verify_packaged_playwright_driver`).

5. Packaging readiness обновлен:
- убран hard-check `prepare_playwright_browser_bundle.sh --verify-only`.

6. Release manual обновлен:
- удален mandatory pre-step подготовки bundled Chromium;
- зафиксирована политика runtime установки Chromium на конечной машине.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py integration/integrations/browser_use_integration.py scripts/verify_packaging_readiness.py` -> OK.
- `bash -n packaging/build_final.sh` -> OK.
- `python3 scripts/verify_packaging_readiness.py` -> FAIL по внешним зависимостям окружения (`scripts/check_dependencies.py`: версии `pyobjc-framework-*`), не по внесенной логике runtime-install/packaging-flow.

## Информация об изменениях
- Что изменено:
  - Реактивирован runtime owner-path установки Chromium.
  - Переведен packaging на модель без bundled Chromium.
  - Синхронизированы readiness и release-doc flow под новую модель.
  - Добавлен явный UX install lifecycle (уведомления + TTS после welcome).
- Список файлов:
  - `modules/browser_automation/module.py`
  - `integration/integrations/browser_use_integration.py`
  - `config/unified_config.yaml`
  - `packaging/build_final.sh`
  - `scripts/verify_packaging_readiness.py`
  - `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
- Причина/цель изменений:
  - Устранить конфликт owner-path, ускорить/упростить packaging, обеспечить корректную установку Chromium на пользовательской машине.
- Проверка:
  - Выполнены синтаксические проверки Python/Bash;
  - Выполнен readiness run, зафиксирован внешний dependency-blocker окружения.

## Architecture Gates
- Single Owner Gate: owner установки браузера -> `BrowserUseModule` (runtime).
- Zero Duplication Gate: удален дублирующий путь prebundle Chromium как обязательный runtime-owner.
- Anti-Race Gate: сохранен single-flight через `_install_task_guard` + shared install task.
- Flag Lifecycle Gate: `browser_use.allow_runtime_install` теперь runtime-used (активный потребитель в `process()`).
