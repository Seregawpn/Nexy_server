# Quick Build Guide - Nexy AI Assistant

**Единый источник истины:** `Docs/PACKAGING_FINAL_GUIDE.md`

## Быстрый старт

### Полная сборка с нотаризацией (релизный режим)

```bash
cd client
./packaging/build_final.sh
```

**Что происходит:**
- Автоматически выполняется Universal 2 сборка (arm64 + x86_64)
- Подпись всех артефактов (`.app`, `.pkg`, `.dmg`)
- Нотаризация всех артефактов
- Полная финальная проверка (подпись, нотаризация, архитектура, целостность)

### Локальная сборка без нотаризации

```bash
cd client
NEXY_SKIP_NOTARIZATION=1 ./packaging/build_final.sh
```

**Что происходит:**
- Автоматически выполняется Universal 2 сборка (arm64 + x86_64)
- Подпись всех артефактов (`.app`, `.pkg`, `.dmg`)
- Нотаризация пропущена
- Полная финальная проверка (подпись, архитектура, целостность)

### Локальная сборка без timestamp

```bash
cd client
TIMESTAMP_MODE=none NEXY_SKIP_NOTARIZATION=1 ./packaging/build_final.sh
```

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
- Финальная проверка выполняется автоматически в `build_final.sh`
- Лог проверки сохраняется в `dist/packaging_verification.log`

