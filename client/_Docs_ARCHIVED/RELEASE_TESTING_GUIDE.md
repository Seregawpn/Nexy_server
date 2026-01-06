# Руководство по тестированию релиза

**Версия:** 1.0  
**Дата:** 2025-12-31  
**Источник истины:** Этот документ координирует использование существующих тест-гайдов

**⚠️ ВАЖНО:** Все команды в этом руководстве выполняются из корня репозитория (`client/`).  
Убедитесь, что вы находитесь в правильной директории перед выполнением команд.

---

## Быстрый старт

**ВАЖНО:** Все команды выполняются из корня репозитория (`client/`).  
Если вы находитесь в другом месте, перейдите в корень:
```bash
cd /path/to/repo/client  # или cd client, если вы в родительской директории
```

```bash
# 1. Подготовка перед упаковкой
# См. раздел 1 ниже

# 2. Упаковка
./packaging/build_final.sh

# 3. Проверка артефактов
./scripts/verify_packaging_artifacts.sh

# 4. Тестирование упакованного приложения
# См. раздел 4 ниже
```

---

## 1. Подготовка перед упаковкой

**Источник истины:** `Docs/PRE_PACKAGING_VERIFICATION.md`

### Шаг 1.1: Проверка готовности к упаковке

```bash
# Откройте и пройдите чек-лист:
# Docs/PRE_PACKAGING_VERIFICATION.md

# Основные пункты:
# - Логика завершения приложения настроена
# - Все тесты пройдены
# - Критические сценарии проверены
```

**Критерии успеха:**
- [ ] Все проверки из `PRE_PACKAGING_VERIFICATION.md` пройдены
- [ ] Статус зафиксирован в `PACKAGING_READINESS_CHECKLIST.md`

---

## 2. Preflight-тест (опционально, перед упаковкой)

**Источник истины:** `Docs/PREFLIGHT_TEST_GUIDE.md`

### Шаг 2.1: Подготовка окружения

```bash
# Автоматическая подготовка
./scripts/preflight_first_run_test.sh

# Или вручную:
sudo tccutil reset All com.nexy.assistant
rm ~/Library/Application\ Support/Nexy/*.flag
```

### Шаг 2.2: Выполнение preflight-теста

```bash
# Запуск приложения в dev-режиме
python3 main.py

# Мониторинг логов (в другом терминале)
tail -f log.md
# Или через Console.app: Applications → Utilities → Console
```

**Ожидаемые события:**
- [ ] `permissions.first_run_started`
- [ ] `permissions.status_checked` (для всех разрешений)
- [ ] `permissions.changed` (при выдаче разрешений)
- [ ] `permissions.first_run_restart_pending` (после критических разрешений)
- [ ] `permission_restart.scheduled`
- [ ] `permissions.first_run_completed` (после рестарта)

**Проверка результатов:**
```bash
# Проверка событий в логах
./scripts/check_first_run_events.sh log.md

# Проверка флагов
ls -la ~/Library/Application\ Support/Nexy/*.flag
```

**Критерии успеха:**
- [ ] Все события опубликованы (см. `PREFLIGHT_TEST_GUIDE.md` раздел "Критерии успеха")
- [ ] Нет зависаний
- [ ] Перезапуск выполняется корректно (≤15 сек)
- [ ] Повторный запуск не запрашивает права

---

## 3. Упаковка и проверка артефактов

### Шаг 3.1: Полная пересборка

```bash
# Очистка старых артефактов
rm -rf dist/* build/* dist-arm64 dist-x86_64 build-arm64 build-x86_64

# Полная пересборка
./packaging/build_final.sh
```

**Ожидаемое время:** 15–30 минут

**Критерии успеха:**
- [ ] Сборка завершена без ошибок
- [ ] PKG и DMG созданы в `dist/`
- [ ] Все артефакты подписаны

### Шаг 3.2: Автоматическая проверка артефактов

```bash
# Проверка всех артефактов
./scripts/verify_packaging_artifacts.sh
```

**Что проверяется:**
- [ ] .app внутри PKG подписан и валиден
- [ ] PKG подписан и валиден
- [ ] DMG целостность подтверждена
- [ ] Нотаризация корректна (если не пропущена)

**Критерии успеха:**
- [ ] Все проверки пройдены
- [ ] Нет ошибок `invalid signature`
- [ ] `stapler validate` проходит (если нотаризация включена)

---

## 4. Тестирование упакованного приложения

**Источник истины:** `Docs/TESTING_PACKAGED_APP.md`

### Шаг 4.1: Установка приложения

**Вариант A: Установка через PKG (рекомендуется)**

```bash
# Установка через GUI
open dist/Nexy.pkg

# Или через командную строку
sudo installer -pkg dist/Nexy.pkg -target /
```

**Вариант B: Установка через DMG**

```bash
# Монтирование DMG
open dist/Nexy.dmg

# Перетащить Nexy.app в Applications вручную
```

**Критерии успеха:**
- [ ] Установка проходит без ошибок
- [ ] Приложение появляется в `/Applications/Nexy.app`
- [ ] Подпись валидна после установки

### Шаг 4.2: Базовые проверки

```bash
# Проверка подписи установленного приложения
codesign --verify --deep --strict /Applications/Nexy.app

# Проверка нотаризации (если включена)
xcrun stapler validate /Applications/Nexy.app

# Проверка архитектуры
lipo -info /Applications/Nexy.app/Contents/MacOS/Nexy
# Ожидается: Architectures in the fat file: x86_64 arm64
```

**Критерии успеха:**
- [ ] Подпись валидна
- [ ] Нотаризация корректна (если включена)
- [ ] Universal 2 архитектура подтверждена

### Шаг 4.3: Функциональные проверки

**Запуск приложения:**
```bash
open /Applications/Nexy.app
```

**Что проверить:**
- [ ] Приложение запускается без ошибок
- [ ] Tray иконка появляется в меню
- [ ] Нет критических ошибок в логах

**Проверка логов:**
```bash
# Логи приложения
tail -f ~/Library/Application\ Support/Nexy/logs/*.log

# Runtime hook лог (проверка PyObjC fix)
cat /tmp/nexy_pyobjc_fix.log 2>/dev/null || echo "Лог еще не создан"

# Проверка на ошибки dlsym
grep -i "dlsym.*cannot find symbol.*NSMake" /tmp/nexy_pyobjc_fix.log 2>/dev/null || echo "Ошибок dlsym не найдено"
```

**Ожидаемый результат runtime hook лога:**
- ✅ `[NEXY_INIT] INFO: All symbols already present in Foundation` или
- ✅ `SUCCESS: fixed_inline:...`
- ❌ НЕ должно быть: `dlsym cannot find symbol NSMake*`

**Функциональные тесты:**
- [ ] Голосовое распознавание работает
- [ ] Скриншоты работают
- [ ] Разрешения запрашиваются корректно (first-run flow)
- [ ] Переходы между режимами работают (SLEEPING → LISTENING → PROCESSING)
- [ ] Tray меню работает
- [ ] Quit через меню работает корректно

**Критерии успеха:**
- [ ] Все базовые функции работают
- [ ] Нет критических ошибок в логах
- [ ] Runtime hook применяется корректно (нет ошибок dlsym)

### Шаг 4.4: Проверка после перезапуска

```bash
# Перезапуск приложения
killall Nexy 2>/dev/null || true
sleep 2
open /Applications/Nexy.app
```

**Что проверить:**
- [ ] Приложение запускается после перезапуска
- [ ] Разрешения не запрашиваются повторно (если уже выданы)
- [ ] Все функции работают после перезапуска

---

## 5. Фиксация результатов

### Шаг 5.1: Обновление чек-листа готовности

**Файл:** `Docs/PACKAGING_READINESS_CHECKLIST.md`

**Что зафиксировать:**
- [ ] Дата проверки
- [ ] Результат проверок (✅/❌)
- [ ] Статус Universal 2 сборки
- [ ] Статус подписи и нотаризации
- [ ] Ссылки на логи сборки

### Шаг 5.2: Обновление детального отчета

**Файл:** `Docs/PRE_PACKAGING_VERIFICATION.md`

**Что обновить:**
- [ ] Результаты тестирования упакованного приложения
- [ ] Статус функциональных проверок
- [ ] Известные проблемы (если есть)

---

## 6. Чек-лист тестирования релиза

### Подготовка
- [ ] Пройден чек-лист `PRE_PACKAGING_VERIFICATION.md`
- [ ] Preflight-тест выполнен (опционально)
- [ ] Статус зафиксирован в `PACKAGING_READINESS_CHECKLIST.md`

### Упаковка
- [ ] Полная пересборка выполнена (`./packaging/build_final.sh`)
- [ ] PKG и DMG созданы
- [ ] Все артефакты подписаны
- [ ] Нотаризация прошла (если включена)

### Проверка артефактов
- [ ] `verify_packaging_artifacts.sh` пройден успешно
- [ ] .app внутри PKG валиден
- [ ] PKG валиден
- [ ] DMG валиден

### Функциональное тестирование
- [ ] Приложение устанавливается (PKG/DMG)
- [ ] Приложение запускается без ошибок
- [ ] Tray иконка появляется
- [ ] Голосовое распознавание работает
- [ ] Скриншоты работают
- [ ] Разрешения запрашиваются корректно
- [ ] Переходы между режимами работают
- [ ] Runtime hook применяется (нет ошибок dlsym)
- [ ] Приложение работает после перезапуска

### Production готовность
- [ ] Нотаризация прошла (`xcrun stapler validate`)
- [ ] Gatekeeper проходит (`spctl --assess`)
- [ ] Можно распространять пользователям

---

## 7. Troubleshooting

### Проблема: "invalid signature"
**Решение:** См. `PACKAGING_VERIFICATION_CHECKLIST.md` раздел "Troubleshooting"

### Проблема: "stapler validate failed"
**Решение:** 
- Если использовался `NEXY_SKIP_NOTARIZATION=1` — это нормально
- Если нотаризация включена — проверьте логи notarytool

### Проблема: "dlsym cannot find symbol NSMake*"
**Решение:** См. `PACKAGING_VERIFICATION_CHECKLIST.md` раздел "Troubleshooting" → "Ошибка: dlsym cannot find symbol NSMake*"

### Проблема: Приложение не запускается
**Решение:** См. `TESTING_PACKAGED_APP.md` раздел "Troubleshooting"

---

## 8. Связанные документы

### Source of Truth документы:
- `Docs/PRE_PACKAGING_VERIFICATION.md` — детальный чек-лист подготовки
- `Docs/PREFLIGHT_TEST_GUIDE.md` — preflight-тест first-run flow
- `Docs/TESTING_PACKAGED_APP.md` — тестирование упакованного приложения
- `Docs/PACKAGING_READINESS_CHECKLIST.md` — краткое резюме статуса

### Инструкции по упаковке:
- `Docs/PACKAGING_FINAL_GUIDE.md` — полная инструкция по сборке
- `Docs/PACKAGING_VERIFICATION_CHECKLIST.md` — проверка артефактов

### Скрипты:
- `scripts/verify_packaging_artifacts.sh` — автоматическая проверка артефактов
- `scripts/preflight_first_run_test.sh` — подготовка к preflight-тесту
- `scripts/check_first_run_events.sh` — проверка событий first-run в логах

---

## 9. Быстрый план (smoke-тесты)

Если мало времени, выполните только критичные проверки:

```bash
# 1. Упаковка
./packaging/build_final.sh

# 2. Проверка артефактов
./scripts/verify_packaging_artifacts.sh

# 3. Установка и запуск
sudo installer -pkg dist/Nexy.pkg -target /
open /Applications/Nexy.app

# 4. Проверка runtime hook
cat /tmp/nexy_pyobjc_fix.log 2>/dev/null | grep -i "dlsym.*cannot find" || echo "✅ Нет ошибок dlsym"
```

**Минимальные критерии:**
- [ ] Артефакты валидны
- [ ] Приложение запускается
- [ ] Нет ошибок dlsym в runtime hook логе

---

## 10. Критерии успеха релиза

### Обязательные:
- [ ] Все артефакты валидны (подпись, нотаризация)
- [ ] Приложение запускается и работает
- [ ] Нет критических ошибок в логах
- [ ] Runtime hook применяется корректно
- [ ] Все базовые функции работают

### Опциональные (для production):
- [ ] Нотаризация прошла успешно
- [ ] Gatekeeper проходит проверку
- [ ] Можно распространять пользователям

---

**Последнее обновление:** 2025-12-31
