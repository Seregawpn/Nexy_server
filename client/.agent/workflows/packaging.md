---
description: Единый workflow упаковки macOS приложения (Universal 2 .app + .pkg + .dmg)
---

# 📦 macOS Packaging Workflow

> [!CAUTION]
> **Это ЕДИНСТВЕННЫЙ способ упаковки.** Любые ручные шаги вне этого workflow ЗАПРЕЩЕНЫ.
> Проблемы упаковки в прошлом возникали именно из-за отклонений от этого процесса.

---

## Правила (ОБЯЗАТЕЛЬНЫ)

1. **Никаких ручных шагов** — только автоматизированные скрипты
2. **Одна команда** — `./packaging/build_final.sh` делает ВСЁ
3. **Всегда проверяй** — `./scripts/verify_packaging_artifacts.sh` после сборки
4. **Документация** — единственный источник: `Docs/PACKAGING_FINAL_GUIDE.md`

---

## Стандартная сборка (с нотаризацией)

// turbo-all

### Шаг 1: Предварительная проверка окружения

```bash
cd /Users/sergiyzasorin/Fix_new/client

# Проверка Python Universal 2
python3 -c "import platform; print(platform.machine())"
arch -x86_64 python3 -c "import platform; print(platform.machine())"

# Проверка сертификатов
security find-identity -v -p codesigning | grep "Developer ID Application"
security find-identity -v -p basic | grep "Developer ID Installer"
```

**Ожидается:**
- Python: `arm64` (нативно) и `x86_64` (через Rosetta)
- Оба сертификата найдены

---

### Шаг 2: Полная сборка (ОДНА КОМАНДА)

```bash
./packaging/build_final.sh
```

**Что делает `build_final.sh` автоматически:**
1. ✅ Проверка актуальности protobuf (`scripts/regenerate_proto.sh --check`)
2. ✅ Стейджинг Universal 2 бинарников (`scripts/stage_universal_binaries.py`)
3. ✅ Проверка зависимостей (`scripts/check_dependencies.py`)
4. ✅ Обновление версий модулей (`scripts/update_module_versions.py`)
5. ✅ Универсализация .so файлов (если нужно)
6. ✅ Двойная сборка PyInstaller (arm64 + x86_64)
7. ✅ Объединение в Universal 2 через `create_universal_app.py`
8. ✅ Подготовка Python.framework к подписи
9. ✅ Подпись через `sign_all_binaries.sh`
10. ✅ Нотаризация .app
11. ✅ Создание и нотаризация DMG
12. ✅ Создание, подпись и нотаризация PKG

**Артефакты:**
- `dist/Nexy.app`
- `dist/Nexy.pkg`
- `dist/Nexy.dmg`

---

### Шаг 3: Проверка артефактов

```bash
./scripts/verify_packaging_artifacts.sh
```

**Проверяет:**
- Подпись .app (`codesign --verify --deep --strict`)
- Нотаризацию (`xcrun stapler validate`)
- Архитектуру (Universal 2: arm64 + x86_64)
- Содержимое PKG и DMG
- Runtime hook лог

---

## Dev-сборка (БЕЗ нотаризации)

Для локальной разработки, когда нотаризация не нужна:

```bash
cd /Users/sergiyzasorin/Fix_new/client
NEXY_SKIP_NOTARIZATION=1 ./packaging/build_final.sh
./scripts/verify_packaging_artifacts.sh --app-only
```

> [!NOTE]
> Для установки без нотаризации см. `Docs/INSTALLATION_WITHOUT_NOTARIZATION.md`

---

## Диагностика проблем

### IncompatibleBinaryArchError при x86_64 сборке

```bash
# Установить пакеты для x86_64
arch -x86_64 python3 -m pip install --target /tmp/x86_64_site_packages -r requirements.txt

# Объединить .so файлы  
python3 scripts/merge_so_from_x86_64.py

# Повторить сборку
./packaging/build_final.sh
```

### Проверка архитектуры бинарников

```bash
lipo -info dist/Nexy.app/Contents/MacOS/Nexy
lipo -info dist/Nexy.app/Contents/Resources/resources/ffmpeg/ffmpeg
```

---

## Исключённые модули

> [!NOTE]
> Следующие модули **НЕ упакованы** и отключены по умолчанию:
> - ❌ **WhatsApp** (whatsapp_integration)
> - ❌ **Payment** (payment_integration)
>
> Для включения см. [PACKAGING_FINAL_GUIDE.md](file:///Users/sergiyzasorin/Fix_new/client/Docs/PACKAGING_FINAL_GUIDE.md)

---

## Связанная документация

| Документ | Назначение |
|----------|------------|
| [PACKAGING_FINAL_GUIDE.md](file:///Users/sergiyzasorin/Fix_new/client/Docs/PACKAGING_FINAL_GUIDE.md) | Полное руководство |
| [PRE_PACKAGING_VERIFICATION.md](file:///Users/sergiyzasorin/Fix_new/client/Docs/PRE_PACKAGING_VERIFICATION.md) | Чек-лист перед упаковкой |
| [PACKAGING_VERIFICATION_CHECKLIST.md](file:///Users/sergiyzasorin/Fix_new/client/Docs/PACKAGING_VERIFICATION_CHECKLIST.md) | Чек-лист проверки |
| [PACKAGING_READINESS_CHECKLIST.md](file:///Users/sergiyzasorin/Fix_new/client/Docs/PACKAGING_READINESS_CHECKLIST.md) | Резюме готовности |

---

## ⛔ Запрещённые действия

| Действие | Почему запрещено |
|----------|------------------|
| Ручной запуск PyInstaller | Пропускает стейджинг бинарников |
| Ручной codesign | Неправильный порядок подписи |
| Копирование .app после подписи | Ломает печать нотаризации |
| Модификация PKG после productsign | Ломает подпись .app внутри |
| Использование `ditto --noextattr` для PKG | Теряет печать нотаризации |
