# Nexy Client Documentation Index

**Версия:** 1.0 (обновлено 2026-01-12)  
**Источник истины:** Этот файл является индексом всех канонических документов проекта.

> **ВАЖНО:** Документация разделена на активные файлы в `Docs/` и архивные файлы в `_Docs_ARCHIVED/`. Все ссылки в правилах ассистента (`.cursorrules`, `AGENTS.md`) должны указывать на актуальные пути.

---

## Активные документы (Docs/)

**Эти документы актуальны и используются в текущей работе:**

### Упаковка и сборка
- **`Docs/PACKAGING_FINAL_GUIDE.md`** — **ЕДИНСТВЕННЫЙ источник истины** для канонического процесса упаковки (раздел 0). Все изменения обязаны следовать обязательному процессу из раздела 0.2.
- `Docs/PRE_PACKAGING_VERIFICATION.md` — чек-лист проверки перед упаковкой
- `Docs/PACKAGING_READINESS_CHECKLIST.md` — фиксация результатов проверки упаковки
- `Docs/PREFLIGHT_CHECKS.md` — система предварительных проверок перед сборкой
- `Docs/PREFLIGHT_IMPLEMENTATION_PLAN.md` — план реализации системы preflight проверок

### Feature Flags
- `Docs/FEATURE_FLAGS.md` — единый источник истины для всех feature flags/kill-switches

### Обмен между ассистентами
- `Docs/assistant_exchange/` — директория для документов обмена между ассистентами
  - `codex/` — документы от ассистента Codex
  - `cursor/` — документы от ассистента Cursor
  - `antigravity/` — документы от ассистента Antigravity (если используется)

---

## Архивные документы (_Docs_ARCHIVED/)

**Эти документы находятся в архиве, но все еще используются в правилах:**

### Требования и архитектура
- `_Docs_ARCHIVED/PROJECT_REQUIREMENTS.md` — единый snapshot требований (обязательно при изменении логики)
- `_Docs_ARCHIVED/REQUIREMENTS_SOURCE_MAP.md` — карта всех документов требований с их статусом
- `_Docs_ARCHIVED/ARCHITECTURE_OVERVIEW.md` — связь модулей и интеграций
- `_Docs_ARCHIVED/PRODUCT_CONCEPT.md` — пользовательские сценарии и режимы

### Состояние и отчеты
- `_Docs_ARCHIVED/STATE_CATALOG.md` — единый источник истины для всех осей состояния
- `_Docs_ARCHIVED/CURRENT_STATUS_REPORT.md` — актуальные истории, риски и тесты
- `_Docs_ARCHIVED/first_run_flow_spec.md` — детальная логика запроса разрешений и перезапуска

### Планирование и доставка
- `_Docs_ARCHIVED/GLOBAL_DELIVERY_PLAN.md` — фазы поставки, Azure/AppCast

### Тестирование
- `_Docs_ARCHIVED/TAL_TESTING_CHECKLIST.md` — чек-лист TAL/permission restart с логами и тестами

### Другие документы
- `_Docs_ARCHIVED/README.md` — общий README архива
- `_Docs_ARCHIVED/DOCUMENTATION_MAP.md` — карта документации
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
   - Требования: `_Docs_ARCHIVED/PROJECT_REQUIREMENTS.md`
   - Архитектура: `_Docs_ARCHIVED/ARCHITECTURE_OVERVIEW.md`
   - Состояние: `_Docs_ARCHIVED/STATE_CATALOG.md`
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

**Последнее обновление:** 2026-01-12  
**Ответственный:** Cursor Assistant
