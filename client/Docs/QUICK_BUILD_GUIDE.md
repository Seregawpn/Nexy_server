# Quick Build Guide - Nexy AI Assistant

**Единый источник истины:** `Docs/PACKAGING_FINAL_GUIDE.md`

## Быстрый старт

### Режим RELEASE (полная сборка с timestamp и нотаризацией)

```bash
cd client
./scripts/release_build.sh release
```

**Что происходит:**
- Автоматически настраивается `TIMESTAMP_MODE=auto`
- Запускается `build_final.sh` с нотаризацией
- Автоматически запускается `verify_packaging_artifacts.sh`
- Жесткая проверка подписи и нотаризации

### Режим LOCAL (локальная сборка без нотаризации)

```bash
cd client
./scripts/release_build.sh local
```

**Что происходит:**
- Автоматически настраивается `TIMESTAMP_MODE=none`
- Автоматически устанавливается `NEXY_SKIP_NOTARIZATION=1`
- Запускается `build_final.sh` без нотаризации
- Автоматически запускается `verify_packaging_artifacts.sh`
- Проверка подписи (нотаризация пропущена)

## КРИТИЧНО: Защита подписи после сборки

**После завершения сборки НЕ выполняйте:**

- ❌ Открытие `.app` в Finder (может изменить extended attributes)
- ❌ Выполнение `xattr -cr` на `.app` (удаляет подпись кода!)
- ❌ Копирование через `cp -R` или Finder (не сохраняет подпись)
- ❌ Архивирование через `zip` без специальных флагов

**Разрешенные операции:**

- ✅ Использование `ditto --noextattr --noqtn` для копирования
- ✅ Использование `safe_copy_preserve_signature` из `build_final.sh`
- ✅ Проверка через `codesign --verify --deep --strict`

## Диагностика

Если подпись ломается, система checkpoint-ов в `build_final.sh` покажет точный этап:

- Все checkpoint-ы логируют детальную информацию
- Первый FAIL укажет на точку повреждения
- Детали ошибки в `/tmp/checkpoint_<name>_codesign.log`

## Дополнительная информация

- Полная документация: `Docs/PACKAGING_FINAL_GUIDE.md`
- Проверка артефактов: `./scripts/verify_packaging_artifacts.sh`
- Ручная сборка (для отладки): см. раздел 2.1 в `PACKAGING_FINAL_GUIDE.md`

