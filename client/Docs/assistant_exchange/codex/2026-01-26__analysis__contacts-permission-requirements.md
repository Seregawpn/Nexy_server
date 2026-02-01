# Contacts Permission — Requirements (Ideal)

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-26
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
Contacts‑диалог появляется только если есть рабочий trigger (CNContactStore) и корректная упаковка (pyobjc + Info.plist usage keys). Иначе шаг проходит без prompt.

## Root Cause
Contacts permission зависит от runtime компонентов (pyobjc Contacts framework) и ключа `NSContactsUsageDescription` в Info.plist. При отсутствии хотя бы одного из них диалог не показывается.

## Optimal Fix
Соблюсти цепочку: конфиг → prober → framework → Info.plist → упаковка. Гарантировать, что `ContactsProber.trigger()` выполняется в GUI процессе и не падает.

## Verification
- В логах есть `[CONTACTS_PROBER] Triggered contacts permission request`
- В TCC логах появляется `kTCCServiceContacts`
- В Info.plist присутствует `NSContactsUsageDescription`

## Запрос/цель
Коротко описать, что нужно для корректного отображения Contacts‑разрешения.

## Контекст
- Файлы: config/unified_config.yaml, modules/permissions/v2/probers/contacts.py, packaging/Nexy.spec, requirements.txt, packaging/build_final.sh
- Документы: Docs/PACKAGING_FINAL_GUIDE.md

## Решения/выводы
- Contacts prompt появляется только при наличии: pyobjc‑framework‑Contacts + NSContactsUsageDescription + вызов CNContactStore.

## Открытые вопросы
- Нет.

## Следующие шаги
- Проверить, что все элементы цепочки соблюдены в текущей сборке.

---

# Архитектура и Source of Truth

- Source of Truth (порядок/шаг): `config/unified_config.yaml` → `integrations.permissions_v2.order` и `steps.contacts`.
- Исполнитель запроса: `modules/permissions/v2/probers/contacts.py` (CNContactStore.requestAccess...).
- Принцип: dialog‑based (должен появляться системный prompt).

# Что должно быть указано

1) Конфиг (V2)
- `config/unified_config.yaml`:
  - `integrations.permissions_v2.order` включает `contacts`.
  - `integrations.permissions_v2.steps.contacts.mode = auto_dialog`.
  - `criticality` по необходимости (обычно `hard`).

2) Trigger
- `modules/permissions/v2/probers/contacts.py`:
  - Использовать `CNContactStore.requestAccessForEntityType_`.
  - Логировать успех/ошибку (already present).

3) Info.plist
- Основной `Contents/Info.plist` должен содержать:
  - `NSContactsUsageDescription` (обязательно, иначе prompt не показывается).

4) Зависимости
- `requirements.txt`:
  - `pyobjc-framework-Contacts==<version>` (есть: 12.1).

5) Упаковка (PyInstaller)
- `packaging/Nexy.spec`:
  - Включить `Contacts` в `hiddenimports`.
  - Прописать `NSContactsUsageDescription` в plist (есть).
- `packaging/build_final.sh`:
  - Проверка `import Contacts` (уже есть проверка).

# Идеальное поведение

- При первом запуске:
  - Contacts шаг вызывает `CNContactStore.requestAccess...`.
  - macOS показывает системный prompt Contacts.
  - В логах: `[CONTACTS_PROBER] Triggered contacts permission request`.

# Минимальные проверки

- `requirements.txt` содержит `pyobjc-framework-Contacts`.
- `packaging/Nexy.spec` содержит `Contacts` и `NSContactsUsageDescription`.
- В runtime `import Contacts` проходит без ImportError.

