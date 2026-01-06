# Canonical Build Path — Task Brief

**Дата:** 2025-01-04  
**Тип:** task-brief  
**Ассистент:** cursor  
**Статус:** ✅ Завершено

---

## Цель

Установить единственный канонический путь упаковки через `release_build.sh` и обновить документацию.

---

## Выполненные шаги

### 1. Канонический путь установлен

**Единственный entrypoint:**
- `./scripts/release_build.sh release` — релизная сборка с нотаризацией
- `./scripts/release_build.sh local` — локальная сборка без нотаризации

**Цепочка выполнения:**
```
release_build.sh → build_final.sh → verify_packaging_artifacts.sh
```

### 2. Удалены дубликаты

- ✅ `packaging/build_universal_app_only.sh` — удален
- ✅ Все ссылки на удаленные скрипты обновлены

### 3. Документация обновлена

**Основные документы:**
- `Docs/PACKAGING_FINAL_GUIDE.md` — основной гайд (раздел 2.0: Автоматизированная сборка)
- `Docs/QUICK_BUILD_GUIDE.md` — краткая инструкция
- `Docs/RELEASE_BUILD_CHECKLIST.md` — чек-лист (обновлен с правилами защиты подписи)

**Ключевые изменения в RELEASE_BUILD_CHECKLIST.md:**
- Добавлен раздел "КРИТИЧЕСКИ ВАЖНО: Канонический путь сборки"
- Добавлены правила защиты подписи
- Добавлены примечания о timestamp сервисе и логах

### 4. Интеграция с prepare_release.sh

- ✅ `scripts/prepare_release.sh` использует `release_build.sh` (строка 236, 242)
- ✅ Все ссылки согласованы

---

## Итоговый статус

✅ **Все задачи выполнены:**
1. Канонический путь установлен — `release_build.sh` является единственным entrypoint
2. Дубликаты удалены — `build_universal_app_only.sh` удален
3. Документация обновлена — все ссылки указывают на `release_build.sh`
4. Чек-лист обновлен — добавлены правила защиты подписи и канонического пути

---

## Правила использования

### Канонический путь (ОБЯЗАТЕЛЬНО)

```bash
# Релизная сборка
./scripts/release_build.sh release

# Локальная сборка
./scripts/release_build.sh local
```

### Защита подписи (КРИТИЧЕСКИ ВАЖНО)

- ❌ **НЕ открывайте `.app` в Finder** после сборки
- ❌ **НЕ выполняйте `xattr -cr`** на `.app` (удаляет подпись!)
- ❌ **НЕ копируйте `.app`** через Finder или `cp -R`
- ✅ Используйте только `ditto --noextattr --noqtn` для копирования

### Timestamp сервис

- Если timestamp сервис недоступен → используйте `local` режим
- `local` режим не выполняет нотаризацию (требуется timestamp)

### Логи

- Логи автоматически сохраняются в `dist/`:
  - `dist/release_build.log` — полный лог сборки
  - `dist/packaging_verification.log` — лог проверки артефактов

---

## Связанные файлы

- `scripts/release_build.sh` — канонический entrypoint
- `packaging/build_final.sh` — используется release_build.sh
- `scripts/verify_packaging_artifacts.sh` — используется release_build.sh
- `scripts/prepare_release.sh` — использует release_build.sh
- `Docs/PACKAGING_FINAL_GUIDE.md` — основной гайд
- `Docs/QUICK_BUILD_GUIDE.md` — краткая инструкция
- `Docs/RELEASE_BUILD_CHECKLIST.md` — чек-лист (обновлен)

---

## Примечания

- Прямой запуск `build_final.sh` допускается как fallback для отладки, но не рекомендуется
- Все артефакты должны проходить через `release_build.sh` для обеспечения консистентности
- Правила защиты подписи обязательны для всех операций с `.app` после сборки
