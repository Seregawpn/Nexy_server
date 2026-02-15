# Nexy Client Documentation Index

**Версия:** 2.0 (обновлено 2026-01-13)  
**Источник истины:** Этот файл является индексом всех канонических документов проекта.

> **ВАЖНО:** Актуальные документы находятся в `Docs/`. Архивные документы в `_Docs_ARCHIVED/` используются только для исторической справки.

---

## Активные документы (Docs/)

**Эти документы актуальны и используются в текущей работе:**

### Архитектура и требования
- **`Docs/ARCHITECTURE_OVERVIEW.md`** — связь модулей и интеграций, обзор архитектуры
- **`Docs/FLOW_INTERACTION_SPEC.md`** — канон взаимодействий и контракты событий (включая активные compatibility-пути, раздел 5.1)
- **`Docs/PROJECT_REQUIREMENTS.md`** — единый snapshot требований (обязательно при изменении логики)
- **`Docs/REQUIREMENTS_SOURCE_MAP.md`** — карта всех документов требований с их статусом
- **`Docs/PRODUCT_CONCEPT.md`** — пользовательские сценарии и режимы
- **`Docs/STATE_CATALOG.md`** — единый источник истины для всех осей состояния
- **`Docs/DOCUMENTATION_MAP.md`** — карта документации и навигатор

### Первый запуск и разрешения
- **`Docs/first_run_flow_spec.md`** — детальная логика запроса разрешений и перезапуска

### Упаковка и сборка
- **`Docs/PACKAGING_FINAL_GUIDE.md`** — **ЕДИНСТВЕННЫЙ источник истины** для канонического процесса упаковки (раздел 0). Все изменения обязаны следовать обязательному процессу из раздела 0.2.
- **`Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`** — канонический регламент обновления версии клиента и правильной заливки в GitHub (`Nexy_client_test` only).
- `Docs/PRE_PACKAGING_VERIFICATION.md` — чек-лист проверки перед упаковкой
- `Docs/PACKAGING_READINESS_CHECKLIST.md` — фиксация результатов проверки упаковки

### Quality Gates (скрипты)
- `scripts/pre_build_gate.sh` — базовый pre-build gate
- `scripts/quality_strict.sh` — строгий алиас pre-build gate (`--require-basedpyright`)
- `scripts/problem_scan.sh` — consolidated scan + priority report
- `scripts/problem_scan_gate.sh` — release/CI gate (blocking issues only)
- `scripts/problem_scan_prioritize.py` — генерация приоритетного отчёта
- `scripts/setup_dev_env.sh` — bootstrap dev-окружения для quality checks

### Feature Flags
- `Docs/FEATURE_FLAGS.md` — единый источник истины для всех feature flags/kill-switches

### Обмен между ассистентами
- `Docs/assistant_exchange/` — директория для документов обмена между ассистентами
  - `codex/` — документы от ассистента Codex
  - `cursor/` — документы от ассистента Cursor
  - `antigravity/` — документы от ассистента Antigravity (если используется)

---

## Архивные документы (_Docs_ARCHIVED/)

**Эти документы находятся в архиве и используются только для исторической справки (`Docs/_archive/` и `_Docs_ARCHIVED/`):**

### Отчёты и планы (исторические)
- `_Docs_ARCHIVED/CURRENT_STATUS_REPORT.md` — исторические отчёты о статусе
- `_Docs_ARCHIVED/GLOBAL_DELIVERY_PLAN.md` — исторические планы доставки
- `_Docs_ARCHIVED/TAL_TESTING_CHECKLIST.md` — исторические чек-листы тестирования

### Другие документы
- `_Docs_ARCHIVED/README.md` — общий README архива
- `_Docs_ARCHIVED/assistant_exchange/` — архивные документы обмена между ассистентами

---

## Отсутствующие документы

**Эти документы упоминаются в правилах, но не найдены в репозитории:**

### Протоколы координации ассистентов
- `ASSISTANT_COORDINATION_PROTOCOL.md` — протокол координации между ассистентами
- `ANTIGRAVITY_PROMPT.md` — prompt-файл для ассистента Antigravity
- `CODEX_PROMPT.md` — prompt-файл для ассистента Codex
- `TEMPLATE.md` — шаблон для документов обмена между ассистентами

### CRM Task Management
- `Docs/CRM_CONSOLIDATED_RULES.md` — полные правила CRM Task Management (упоминается в `.cursorrules` раздел 22.7)
- `Docs/CRM_ASSISTANT_INSTRUCTIONS.md` — инструкция для ассистентов по CRM (упоминается в `.cursorrules` раздел 22.7)

**Рекомендация:** Если эти документы необходимы, их следует создать или восстановить из архива. До восстановления используйте существующие примеры в `Docs/assistant_exchange/` для формата документов обмена.

---

## Требования окружения

**Актуальные требования (синхронизированы с `Docs/PACKAGING_FINAL_GUIDE.md`):**

- **macOS:** 13+ (для Rosetta 2 на Apple Silicon, сборка Universal 2)
- **Python:** 3.13.7 Universal 2 (установлен через официальный `python-3.13.7-macos11.pkg`)
  - Путь: `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`
  - **ВАЖНО:** Не использовать arm64-only Python из pyenv
- **Минимальная версия для приложения:** 12.0 (Monterey) - указано в Info.plist

---

## Правила использования документации

1. **Активные документы** (`Docs/`) — используются в текущей работе, регулярно обновляются
2. **Архивные документы** (`_Docs_ARCHIVED/`) — исторические документы, но все еще используются в правилах
3. **Единый источник истины:**
   - Упаковка: `Docs/PACKAGING_FINAL_GUIDE.md` (раздел 0)
   - Требования: `Docs/PROJECT_REQUIREMENTS.md`
   - Архитектура: `Docs/ARCHITECTURE_OVERVIEW.md`
   - Состояние: `Docs/STATE_CATALOG.md`
   - Feature Flags: `Docs/FEATURE_FLAGS.md`

4. **Обновление ссылок:** При изменении местоположения документов обновлять:
   - `.cursorrules` — все ссылки на документы
   - `AGENTS.md` — ссылки в разделе "Контекст клиента"
   - Этот файл (`Docs/README.md`) — индекс документов

---

## Связанные документы

- `.cursorrules` — правила разработки клиента
- `AGENTS.md` — базовые правила проекта
- `Docs/PACKAGING_FINAL_GUIDE.md` — канонический процесс упаковки
- `_Docs_ARCHIVED/README.md` — общий README архива

---

**Последнее обновление:** 2026-02-15  
**Ответственный:** Cursor Assistant  
**Изменения:** Перемещены актуальные документы из `_Docs_ARCHIVED/` в `Docs/`
