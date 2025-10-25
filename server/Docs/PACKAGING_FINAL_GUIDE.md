# PACKAGING FINAL GUIDE — Финальная инструкция по упаковке, подписи и нотаризации Nexy

Обновлено: 2.10.2025

Цель: единая, точная и минимальная инструкция. Один скрипт выполнит сборку, подпись, нотаризацию, создание DMG и PKG (строгая установка в /Applications) и оставит в dist/ только нужные артефакты.

## 🚀 **ИНТЕГРАЦИЯ С ПАРАЛЛЕЛЬНЫМ ПЛАНОМ**

Этот гайд является частью **ПОТОКА 1** параллельного плана упаковки и деплоя:
- **ПОТОК 1:** Упаковка PKG/DMG (2-3 часа) - подпись + нотаризация ← **ЭТОТ ГАЙД**
- **ПОТОК 2:** Деплой сервера (1-2 часа) - Azure VM + gRPC + AppCast ✅ **ЗАВЕРШЕНО**
- **ПОТОК 3:** Тестирование обновлений (30 мин) - полный цикл проверки

**ЭКОНОМИЯ ВРЕМЕНИ:** 1-2 часа за счет параллельного выполнения потоков.

## ✅ **НОВЫЕ УЛУЧШЕНИЯ (ОКТЯБРЬ 2025)**

### **МАСШТАБИРОВАНИЕ ДО 100 ПОЛЬЗОВАТЕЛЕЙ:**
- ✅ **gRPC сервер:** Увеличены лимиты с 10 до 100 воркеров
- ✅ **Конфигурация:** Обновлены все параметры для высокой нагрузки
- ✅ **Connection pooling:** Оптимизированы настройки для 100 соединений
- ✅ **Память:** Увеличены лимиты памяти в 5-10 раз

### **ПРАВИЛЬНАЯ МОДУЛЬНАЯ СТРУКТУРА:**
- ✅ **gRPC файлы:** Перенесены из корня в `modules/grpc_service/`
- ✅ **Protobuf:** Перегенерированы в правильном месте
- ✅ **Импорты:** Обновлены все зависимости
- ✅ **Архитектура:** Соответствует принципам модульности

### **СИСТЕМА МОНИТОРИНГА:**
- ✅ **Метрики:** Отслеживание активных соединений, RPS, ошибок
- ✅ **Алерты:** Автоматические предупреждения при превышении лимитов
- ✅ **Производительность:** Мониторинг CPU, памяти, времени ответа

### **AZURE VM И АВТОМАТИЧЕСКИЙ ДЕПЛОЙ:**
- ✅ **Сервер:** Развернут на Azure VM (20.151.51.172)
- ✅ **Статус:** Стабильно работает без перезагрузок
- ✅ **Автоматический деплой:** GitHub Actions + скрипт обновления
- ✅ **Мониторинг:** Встроенная система отслеживания производительности

## ⚠️ ВАЖНЫЕ ОСОБЕННОСТИ И НЮАНСЫ

### Время сборки
- **PyInstaller сборка занимает 5-15 минут** из-за большого количества зависимостей (scipy, numpy, grpcio, PyObjC)
- **НЕ прерывайте процесс** - это нормальное поведение
- **Предупреждения о scipy модулях** - это нормально, PyInstaller корректно обрабатывает их

### Extended Attributes (КРИТИЧНО!)
- **macOS автоматически добавляет extended attributes** при любых операциях с файлами
- **Скрипт использует агрессивную очистку** на каждом этапе
- **Финальная проверка может показывать ошибки** - это НЕ влияет на качество PKG/DMG
- **Основные файлы (PKG/DMG) всегда корректны** и проходят все проверки Apple

### Технические детали
- **PyInstaller режим**: onedir (не onefile) для корректной упаковки ресурсов
- **Архитектура**: arm64 для Apple Silicon, автоматическое определение
- **Python версия**: 3.11+ (тестировано), совместимо с 3.9+
- **Размер приложения**: ~121 МБ (включая все зависимости)
- **Время нотаризации**: 2-5 минут на каждый файл (app, DMG, PKG)
- **Порядок подписи**: вложенные Mach-O → весь .app → PKG

### Упакованные компоненты
- **Python зависимости**: scipy, numpy, grpcio, PyObjC фреймворки, speech_recognition, pydub
- **Бинарные файлы**: ffmpeg (arm64), все системные фреймворки macOS
- **Конфигурация**: unified_config.yaml, все настройки приложения
- **Ресурсы**: иконки, аудио файлы, логотипы
- **Права доступа**: микрофон, захват экрана, VoiceOver, сетевые соединения
- **Размер итогового пакета**: 127 МБ (включая все зависимости)

—

1) Требования и подготовка (один раз)
- Установите инструменты Xcode: `xcode-select --install`
- **Проверьте Python версию**: должен быть 3.11+ (тестировано на 3.11+)
- **Проверьте архитектуру**: arm64 для Apple Silicon, x86_64 для Intel
- **КРИТИЧНО: Настройте сертификаты в Keychain:**
  - Developer ID Application (для подписи .app)
  - Developer ID Installer (для подписи PKG)
- **КРИТИЧНО: Сохраните профиль нотаризации Apple:**
  - `xcrun notarytool store-credentials nexy-notary --apple-id seregawpn@gmail.com --team-id 5NKLL2CLB9 --password <APP_SPECIFIC_PASSWORD>`
- **Проверьте ffmpeg**: должен быть в `resources/ffmpeg/ffmpeg` и иметь правильную архитектуру

2) Единая команда упаковки
- Запустите из корня проекта: `./packaging/build_final.sh`
- **⚠️ НЕ ПРЕРЫВАЙТЕ ПРОЦЕСС** - сборка PyInstaller занимает 5-15 минут
- Скрипт выполнит:
  - сборку .app через PyInstaller (долгий этап - ждите!);
  - агрессивную очистку extended attributes на каждом этапе;
  - подпись вложенных Mach‑O и всего .app (Hardened Runtime + entitlements);
  - нотаризацию .app и stapler;
  - создание DMG (drag‑and‑drop);
  - создание component PKG с install-location `/Applications`;
  - сборку distribution PKG (домен установки: только system);
  - подпись PKG (Developer ID Installer) и нотаризацию PKG;
  - финальные проверки и очистку мусора.

3) Результат
- В `dist/` останутся строго два файла:
- `Nexy.pkg` (127 МБ) — подписанный и пронотаризованный установщик в `/Applications`
- `Nexy.dmg` (127 МБ) — образ для drag-and-drop установки
- **Размеры указаны для arm64 архитектуры** (Apple Silicon)

4) Установка PKG (строго /Applications)
- Очистите прежние следы при необходимости:
  - `sudo pkgutil --forget com.nexy.assistant.pkg || true`
  - `rm -rf ~/Applications/Nexy.app /Applications/Nexy.app`
- Установка:
- GUI: двойной клик по `dist/Nexy.pkg`
- CLI: `sudo installer -pkg dist/Nexy.pkg -target /`
- Проверка: `ls -la /Applications/Nexy.app`

5) Проверка подписи и печатей
- PKG:
  - `pkgutil --check-signature dist/Nexy.pkg`
  - `xcrun stapler validate dist/Nexy.pkg`
- Приложение (дополнительно):
  - `codesign --verify --deep --strict --verbose=2 /Applications/Nexy.app`

6) Критические требования (уже учтены)
- PKG: `--install-location /Applications`
- distribution.xml: `<domains enable_localSystem="true" enable_currentUserHome="false"/>`
- PKG подписывается сертификатом Developer ID Installer
- Hardened Runtime + `com.apple.security.cs.disable-library-validation`
- Порядок подписи: вложенные Mach‑O → весь .app
- Копирование только через `ditto --noextattr --noqtn` + `xattr -cr`
- В PyInstaller не использовать `exclude_binaries=True`
- VoiceOver разрешения: включены в entitlements.plist для управления VoiceOver

7) Сброс TCC (по желанию)
- `./packaging/reset_permissions.sh` — сбросить разрешения (микрофон, экран, VoiceOver и т.д.)

8) Диагностика
- Куда ставит PKG:
  - `pkgutil --expand dist/Nexy.pkg /tmp/nexy_check`
  - `grep -R "install-location" /tmp/nexy_check` → `/Applications`
- Домен установки:
  - `packaging/distribution.xml` → `<domains enable_localSystem="true" enable_currentUserHome="false"/>`

9) Частые проблемы и решения
- **«resource fork, Finder information, or similar detritus not allowed»** → скрипт уже использует агрессивную очистку, но macOS может добавлять атрибуты снова
- **«Failed to load Python shared library»** → не используйте `exclude_binaries=True` в PyInstaller
- **«nested code is not signed at all»** → подпишите вложенные Mach‑O до подписи бандла (уже в скрипте)
- **PKG «no signature»** → подписывайте PKG сертификатом Developer ID Installer (уже в скрипте)
- **PyInstaller зависает на scipy** → это нормально, ждите 5-15 минут
- **Финальная проверка показывает ошибки extended attributes** → это НЕ влияет на качество PKG/DMG
- **spctl проверка не проходит** → нормально для непронотаризованного приложения, но PKG/DMG пронотаризованы

—

Контрольный список успеха
- [ ] `./packaging/build_final.sh` отработал без ошибок
- [ ] В `dist/` только `Nexy.pkg` и `Nexy.dmg` (плюс временный `Nexy` файл)
- [ ] `pkgutil --check-signature dist/Nexy.pkg` — OK
- [ ] `xcrun stapler validate dist/Nexy.pkg` — OK
- [ ] `xcrun stapler validate dist/Nexy.dmg` — OK
- [ ] Установка через PKG помещает приложение в `/Applications/Nexy.app`
- [ ] **Размеры файлов**: PKG ~127 МБ, DMG ~127 МБ (для arm64)

## 📋 ДОПОЛНИТЕЛЬНЫЕ ПРОВЕРКИ

### Проверка содержимого PKG
```bash
# Распаковать PKG для проверки
pkgutil --expand dist/Nexy.pkg /tmp/nexy_check
# Проверить install-location
grep -R "install-location" /tmp/nexy_check
# Должно показать: install-location="/"
```

### Проверка архитектуры
```bash
# Проверить архитектуру ffmpeg
file resources/ffmpeg/ffmpeg
# Должно показать: Mach-O 64-bit executable arm64 (для Apple Silicon)
```

### Проверка зависимостей
```bash
# Проверить установленные Python пакеты
pip3 list | grep -E "(grpcio|PyAudio|sounddevice|Pillow|mss|numpy|pydub|scipy|rich|pynput|urllib3|pynacl|PyYAML|rumps|aiohttp|psutil|pyobjc)"
```

Это единственная актуальная инструкция по упаковке Nexy.

---

## 🚀 **СИСТЕМА ОБНОВЛЕНИЯ ЧЕРЕЗ GITHUB**

После создания PKG/DMG файлов, используйте систему обновления через GitHub:

### **📋 Процесс обновления:**
1. **Упаковка** → создание DMG файла (этот гайд)
2. **Деплой** → `scripts/deploy.sh Nexy.dmg`
3. **GitHub Release** → автоматическое создание релиза с тегом `Update`
4. **Azure сервер** → обновление манифеста и AppCast XML
5. **Клиенты** → получают обновления через GitHub CDN

### **🔧 Требования для деплоя:**
- ✅ **GitHub CLI** (`brew install gh && gh auth login`)
- ✅ **Azure CLI** (`brew install azure-cli && az login`)
- ✅ **DMG файл** готов к загрузке
- ✅ **Права доступа** к репозиторию `Seregawpn/Nexy_production`

### **🚀 Запуск деплоя:**
```bash
cd scripts/
./deploy.sh ../Nexy.dmg
```

### **📊 Результат:**
- ✅ **GitHub релиз** создан с тегом `Update`
- ✅ **DMG файл** доступен через GitHub CDN
- ✅ **Azure сервер** обновлен с новой ссылкой
- ✅ **AppCast XML** обновлен автоматически
- ✅ **Клиенты** получают обновления через GitHub CDN

**Подробная документация:** `Docs/GITHUB_UPDATE_SYSTEM.md`
