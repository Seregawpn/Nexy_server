# Реорганизация документации: перемещение актуальных документов

**Дата:** 2026-01-13  
**Тип:** task-brief  
**Автор:** Cursor Assistant  
**Статус:** ✅ Завершено

---

## Задача

Переместить актуальные документы из `_Docs_ARCHIVED/` в `Docs/`, исключив:
- `CURRENT_STATUS_REPORT.md`
- `GLOBAL_DELIVERY_PLAN.md`
- `TAL_TESTING_CHECKLIST.md`

## Выполненные действия

### 1. Перемещены документы из `_Docs_ARCHIVED/` в `Docs/`

✅ **Перемещено 6 документов:**
1. `STATE_CATALOG.md` — единый источник истины для осей состояния
2. `ARCHITECTURE_OVERVIEW.md` — обзор архитектуры
3. `PROJECT_REQUIREMENTS.md` — единый snapshot требований
4. `REQUIREMENTS_SOURCE_MAP.md` — карта источников требований
5. `PRODUCT_CONCEPT.md` — концепция продукта
6. `DOCUMENTATION_MAP.md` — карта документации

### 2. Удалены дубликаты из `_Docs_ARCHIVED/`

✅ **Удалено 3 дубликата:**
- `first_run_flow_spec.md` (оставлен в `Docs/`)
- `PACKAGING_FINAL_GUIDE.md` (оставлен в `Docs/`)
- `FEATURE_FLAGS.md` (оставлен в `Docs/`)

### 3. Обновлены ссылки в правилах

✅ **Обновлены ссылки в:**
- `.cursorrules` — все ссылки на `_Docs_ARCHIVED/` → `Docs/` для перемещённых документов
- `AGENTS.md` — обновлены ссылки на архитектуру и требования
- `Docs/README.md` — обновлён индекс документов с новой структурой

### 4. Проверка целостности

✅ **Проверено:**
- Все 6 документов присутствуют в `Docs/`
- Дубликаты удалены из `_Docs_ARCHIVED/`
- В перемещённых документах нет ссылок на `_Docs_ARCHIVED/`
- Все ссылки в правилах обновлены

---

## Итоговая структура

### Активные документы в `Docs/`

**Архитектура и требования:**
- `Docs/ARCHITECTURE_OVERVIEW.md`
- `Docs/PROJECT_REQUIREMENTS.md`
- `Docs/REQUIREMENTS_SOURCE_MAP.md`
- `Docs/PRODUCT_CONCEPT.md`
- `Docs/STATE_CATALOG.md`
- `Docs/DOCUMENTATION_MAP.md`

**Первый запуск:**
- `Docs/first_run_flow_spec.md`

**Упаковка:**
- `Docs/PACKAGING_FINAL_GUIDE.md`
- `Docs/PRE_PACKAGING_VERIFICATION.md`
- `Docs/PACKAGING_READINESS_CHECKLIST.md`
- `Docs/PREFLIGHT_CHECKS.md`
- `Docs/PREFLIGHT_IMPLEMENTATION_PLAN.md`

**Feature Flags:**
- `Docs/FEATURE_FLAGS.md`

### Оставлены в архиве `_Docs_ARCHIVED/`

- `CURRENT_STATUS_REPORT.md` (по запросу)
- `GLOBAL_DELIVERY_PLAN.md` (по запросу)
- `TAL_TESTING_CHECKLIST.md` (по запросу)
- `README.md` (общий README архива)
- `assistant_exchange/` (архивные документы обмена)

---

## Обновлённые ссылки

### В `.cursorrules`:
- `_Docs_ARCHIVED/PROJECT_REQUIREMENTS.md` → `Docs/PROJECT_REQUIREMENTS.md`
- `_Docs_ARCHIVED/REQUIREMENTS_SOURCE_MAP.md` → `Docs/REQUIREMENTS_SOURCE_MAP.md`
- `_Docs_ARCHIVED/PRODUCT_CONCEPT.md` → `Docs/PRODUCT_CONCEPT.md`
- `_Docs_ARCHIVED/ARCHITECTURE_OVERVIEW.md` → `Docs/ARCHITECTURE_OVERVIEW.md`
- `_Docs_ARCHIVED/STATE_CATALOG.md` → `Docs/STATE_CATALOG.md`
- `_Docs_ARCHIVED/first_run_flow_spec.md` → `Docs/first_run_flow_spec.md`

### В `AGENTS.md`:
- `_Docs_ARCHIVED/ARCHITECTURE_OVERVIEW.md` → `Docs/ARCHITECTURE_OVERVIEW.md`
- `_Docs_ARCHIVED/PROJECT_REQUIREMENTS.md` → `Docs/PROJECT_REQUIREMENTS.md`

### В `Docs/README.md`:
- Полностью обновлён раздел "Активные документы"
- Обновлён раздел "Единый источник истины"
- Обновлена версия документа (2.0)

---

## Результат

✅ **Все актуальные документы теперь находятся в `Docs/`**  
✅ **Дубликаты удалены**  
✅ **Все ссылки в правилах обновлены**  
✅ **Структура документации соответствует фактическому использованию**

---

## Следующие шаги

1. ✅ Проверить работу ссылок в правилах
2. ⏳ Обновить ссылки в других документах (если есть)
3. ⏳ Обновить ссылки в скриптах (если есть)

---

**Время выполнения:** ~30 минут  
**Файлов перемещено:** 6  
**Файлов удалено:** 3  
**Ссылок обновлено:** ~20
