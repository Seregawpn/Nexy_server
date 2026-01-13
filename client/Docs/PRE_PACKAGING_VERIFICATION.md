# Проверка перед упаковкой (Pre-Packaging Verification)

**Версия:** 2.0 (обновлено 2026-01-11)  
**Источник истины:** `Docs/PACKAGING_FINAL_GUIDE.md` (раздел 0)

> **ОБЯЗАТЕЛЬНО:** Этот чек-лист должен быть пройден перед каждым запуском `build_final.sh`. Результаты фиксируются в `Docs/PACKAGING_READINESS_CHECKLIST.md`.

---

## 1. Проверка триггеров изменений

**Проверить, какие файлы изменены:**

```bash
# Проверить измененные файлы
git status --short | grep -E "(main\.py|integration/|modules/|resources/|assets/|vendor_binaries/|config/|packaging/|scripts/|requirements\.txt|pyproject\.toml)"
```

**Если найдены изменения:**
- [ ] Определить тип изменения (код, ресурсы, бинарники, конфигурация)
- [ ] Следовать обязательному процессу из `PACKAGING_FINAL_GUIDE.md` (раздел 0.2)

---

## 2. Проверка окружения

### 2.1. Python (Universal 2)

```bash
# Проверка архитектуры Python
python3 -c "import platform; print(platform.machine())"
# Ожидается: arm64

# Проверка x86_64 через Rosetta
arch -x86_64 python3 -c "import platform; print(platform.machine())"
# Ожидается: x86_64
```

- [ ] Python Universal 2 установлен (arm64 + x86_64)
- [ ] Путь: `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`

### 2.2. Сертификаты

```bash
# Проверка Developer ID Application
security find-identity -v -p codesigning | grep "Developer ID Application"

# Проверка Developer ID Installer (опционально, для PKG)
security find-identity -v -p basic | grep "Developer ID Installer"
```

- [ ] Developer ID Application сертификат найден
- [ ] Developer ID Installer сертификат найден (для PKG, опционально)

### 2.3. Инструменты

```bash
# Проверка необходимых инструментов
command -v pyinstaller && echo "✓ PyInstaller"
command -v codesign && echo "✓ codesign"
command -v pkgbuild && echo "✓ pkgbuild"
command -v productbuild && echo "✓ productbuild"
command -v notarytool && echo "✓ notarytool"
command -v stapler && echo "✓ stapler"
command -v lipo && echo "✓ lipo"
```

- [ ] Все инструменты установлены и доступны

---

## 3. Проверка артефактов упаковки

### 3.1. Nexy.spec

**Если добавлены новые ресурсы/бинарники:**

- [ ] Новые ресурсы добавлены в секцию `datas` в `packaging/Nexy.spec`
- [ ] Новые бинарники добавлены в секцию `binaries` (если нужно)
- [ ] Пути корректны (абсолютные пути через `client_dir`)
- [ ] Структура директорий соответствует структуре в `.app/Contents/Resources/`

**Проверка:**
```bash
# Проверить, что новые ресурсы упомянуты в Nexy.spec
grep -E "(new_resource|new_binary)" packaging/Nexy.spec
```

### 3.2. stage_universal_binaries.py

**Если добавлен новый бинарник в `vendor_binaries/`:**

- [ ] Определение бинарника добавлено в `BINARY_DEFS` в `scripts/stage_universal_binaries.py`
- [ ] Пути к arm64 и x86_64 версиям корректны
- [ ] Выходной путь соответствует структуре в `resources/`

**Проверка:**
```bash
# Проверить, что новый бинарник упомянут в stage_universal_binaries.py
grep -E "new_binary" scripts/stage_universal_binaries.py
```

### 3.3. Universal 2 бинарники

**Если добавлены новые бинарники:**

```bash
# Проверить наличие arm64 и x86_64 версий
ls -la vendor_binaries/new_binary/arm64/
ls -la vendor_binaries/new_binary/x86_64/
```

- [ ] arm64 версия бинарника присутствует
- [ ] x86_64 версия бинарника присутствует
- [ ] Обе версии исполняемые (`chmod +x`)

---

## 4. Проверка зависимостей

### 4.1. requirements.txt

```bash
# Проверить, что все зависимости установлены и совместимы
python3 -m pip check

# Установить недостающие зависимости (если нужно)
python3 -m pip install -r requirements.txt
```

- [ ] Все зависимости из `requirements.txt` установлены
- [ ] Версии зависимостей соответствуют требованиям
- [ ] Нет конфликтов зависимостей (`pip check` не выдает ошибок)

### 4.2. pyproject.toml

- [ ] Конфигурация `pyproject.toml` актуальна
- [ ] Нет конфликтов с `requirements.txt`

---

## 5. Проверка конфигурации

### 5.1. unified_config.yaml

```bash
# Проверить валидность конфигурации
python3 -c "import yaml; yaml.safe_load(open('config/unified_config.yaml'))"
```

- [ ] `unified_config.yaml` валиден (нет синтаксических ошибок)
- [ ] Версия приложения обновлена (если нужно)

### 5.2. Info.plist

- [ ] Минимальная версия macOS = 12.0
- [ ] Bundle identifier = `com.nexy.assistant`
- [ ] Версия приложения соответствует `unified_config.yaml`

---

## 6. Проверка ресурсов

### 6.1. Иконки

```bash
# Проверить наличие иконки
ls -la assets/icons/app_icon.icns
```

- [ ] Иконка приложения присутствует: `assets/icons/app_icon.icns`

### 6.2. Аудио ресурсы

```bash
# Проверить наличие аудио ресурсов
ls -la resources/audio/
```

- [ ] Аудио ресурсы присутствуют (если используются)

### 6.3. Бинарники

```bash
# Проверить Universal 2 бинарники (после stage_universal_binaries.py)
lipo -info resources/ffmpeg/ffmpeg
lipo -info resources/audio/SwitchAudioSource
lipo -info resources/audio/flac
```

- [ ] FFmpeg: Universal 2 (arm64 + x86_64)
- [ ] SwitchAudioSource: Universal 2 (arm64 + x86_64)
- [ ] FLAC: Universal 2 (arm64 + x86_64)

---

## 7. Проверка кода

### 7.1. Импорты

```bash
# Проверить импорты (если скрипт доступен)
python3 scripts/verify_imports.py
```

- [ ] Все импорты корректны
- [ ] Нет отсутствующих модулей

### 7.2. PyInstaller совместимость

```bash
# Проверить совместимость с PyInstaller (если скрипт доступен)
python3 scripts/verify_pyinstaller.py
```

- [ ] Код совместим с PyInstaller
- [ ] Нет проблем с hidden imports

### 7.3. ctypes/нативный код

```bash
# Проверить ctypes/нативный код (если скрипт доступен)
python3 scripts/verify_ctypes.py
```

- [ ] ctypes/нативный код корректно настроен
- [ ] Нет проблем с библиотеками

---

## 8. Проверка тестов

**Если есть тесты:**

```bash
# Запустить тесты (если доступны)
python3 -m pytest tests/ -v
```

- [ ] Все тесты пройдены
- [ ] Нет критических ошибок

---

## 9. Фиксация результатов

**ОБЯЗАТЕЛЬНО:** После прохождения чек-листа зафиксировать результаты:

1. **Обновить `Docs/PACKAGING_READINESS_CHECKLIST.md`:**
   - Указать дату проверки
   - Отметить пройденные пункты
   - Указать найденные проблемы (если есть)
   - Приложить логи проверок

2. **Приложить к PR/таске:**
   - Скриншоты/логи проверок
   - Ссылку на обновленный `PACKAGING_READINESS_CHECKLIST.md`

---

## 10. Готовность к упаковке

**После прохождения всех проверок:**

- [ ] Все пункты чек-листа пройдены
- [ ] Результаты зафиксированы в `PACKAGING_READINESS_CHECKLIST.md`
- [ ] Готовность к запуску `build_final.sh`

**Следующий шаг:**
```bash
# Запустить канонический процесс упаковки
./packaging/build_final.sh
```

---

## Связанные документы

- `Docs/PACKAGING_FINAL_GUIDE.md` — основной гайд по упаковке (раздел 0)
- `Docs/PACKAGING_READINESS_CHECKLIST.md` — фиксация результатов проверки
- `packaging/build_final.sh` — канонический скрипт упаковки
- `.cursorrules` — правила разработки (раздел 11.2)
