# 🚀 GLOBAL DELIVERY PLAN — Nexy AI Assistant (macOS)

## 📋 **КОНСТАНТЫ ПРОЕКТА**
- **Azure VM IP:** `20.151.51.172`
- **Основной репозиторий:** `https://github.com/Seregawpn/nexy_new.git`
- **Серверный репозиторий:** `https://github.com/Seregawpn/Nexy_server.git`
- **VM Name:** `nexy-regular`
- **Resource Group:** `Nexy`

## 🎯 Цель
Единый план движения и реализации концепта с тремя режимами (SLEEPING / LISTENING / PROCESSING), упаковкой в подписанный и нотарифицированный PKG, автообновлениями (Sparkle) и переносом серверной части на Azure (без Docker/CI).

- Архитектурные принципы: EventBus, тонкие интеграции (без дублирования логики модулей), координатор лишь координирует.
- Режимы: только 3 (S/L/P). Воспроизведение — подэтап внутри PROCESSING.
- Дистрибуция: финальный артефакт — подписанный/нотарифицированный PKG + `appcast.xml` на Azure.

---

## 🧭 Обзор этапов
1) Этап 1 — Клиент: интеграции и UX (S/L/P) ✅ **ЗАВЕРШЕНО**
2) Этап 2 — **МАСШТАБИРОВАНИЕ + АРХИТЕКТУРНЫЕ УЛУЧШЕНИЯ** ✅ **ЗАВЕРШЕНО**
3) Этап 3 — **ПАРАЛЛЕЛЬНАЯ УПАКОВКА + ДЕПЛОЙ** 🚀 **В ПРОЦЕССЕ**
   - 3.1 Деплой сервера ✅ **ЗАВЕРШЕНО**
   - 3.2 Упаковка PKG/DMG ⏳ **ГОТОВО К ЗАПУСКУ**
4) Этап 4 — Тестирование системы обновлений 🧪 **ГОТОВО К ЗАПУСКУ**

### **✅ ЗАВЕРШЕННЫЕ УЛУЧШЕНИЯ АРХИТЕКТУРЫ:**
- **МАСШТАБИРОВАНИЕ:** gRPC сервер оптимизирован для 100 пользователей
- **МОДУЛЬНАЯ СТРУКТУРА:** gRPC файлы перенесены в правильную структуру модулей
- **МОНИТОРИНГ:** Добавлена система отслеживания производительности
- **ТЕСТИРОВАНИЕ:** Создан скрипт нагрузочного тестирования
- **СОВМЕСТИМОСТЬ:** Обновлены все библиотеки до последних версий
- **AZURE VM:** Сервер развернут и работает на Azure VM
- **АВТОМАТИЧЕСКИЙ ДЕПЛОЙ:** GitHub Actions + скрипт обновления настроены

### **🚀 СЛЕДУЮЩИЙ ПОДХОД: ПАРАЛЛЕЛИЗАЦИЯ С ЦИКЛИЧНЫМ ТЕСТИРОВАНИЕМ**
- **ПОТОК 1:** Упаковка PKG/DMG (2-3 часа) - подпись + нотаризация ⏳ **ГОТОВО К ЗАПУСКУ**
- **ПОТОК 2:** Деплой сервера (1-2 часа) - Azure VM + gRPC + AppCast ✅ **ЗАВЕРШЕНО**
- **ПОТОК 3:** Тестирование обновлений (30 мин) - полный цикл проверки 🧪 **ГОТОВО К ЗАПУСКУ**
- **ЭКОНОМИЯ ВРЕМЕНИ:** 1-2 часа (вместо 4-5 часов последовательно)

### **🧪 СИСТЕМА ЦИКЛИЧНОГО ТЕСТИРОВАНИЯ:**
Каждый этап включает **ТЕСТ → ВАЛИДАЦИЯ → ПЕРЕХОД**:
- **ТЕСТ:** Выполнение проверок и тестов
- **ВАЛИДАЦИЯ:** Проверка критериев успеха
- **ПЕРЕХОД:** Переход к следующему этапу только при успехе
- **ЦИКЛ:** Возврат к исправлению при неудаче

**📋 ПРАВИЛО:** НЕ ПЕРЕХОДИМ к следующему этапу без успешного прохождения всех тестов текущего этапа

Каждый этап разбит на мини‑циклы с целью, действиями и тест‑гейтом (критерием готовности).

---

## ✅ 2) МАСШТАБИРОВАНИЕ + АРХИТЕКТУРНЫЕ УЛУЧШЕНИЯ - ЗАВЕРШЕНО
**Цель**: Подготовка системы к масштабированию до 100 пользователей и исправление архитектурных проблем.

### ✅ **ЭТАП 2 ПОЛНОСТЬЮ ЗАВЕРШЕН (30.09.2025):**

#### **🚀 МАСШТАБИРОВАНИЕ ДО 100 ПОЛЬЗОВАТЕЛЕЙ:**
- ✅ **gRPC сервер:** Увеличены лимиты с 10 до 100 воркеров
- ✅ **Конфигурация:** Обновлены все параметры для высокой нагрузки
- ✅ **Connection pooling:** Оптимизированы настройки для 100 соединений
- ✅ **Память:** Увеличены лимиты памяти в 5-10 раз
- ✅ **API лимиты:** Подготовлены к переходу на платные планы

#### **🏗️ ПРАВИЛЬНАЯ МОДУЛЬНАЯ СТРУКТУРА:**
- ✅ **gRPC файлы:** Перенесены из корня в `modules/grpc_service/`
- ✅ **Protobuf:** Перегенерированы в правильном месте
- ✅ **Импорты:** Обновлены все зависимости
- ✅ **Архитектура:** Соответствует принципам модульности

#### **📊 СИСТЕМА МОНИТОРИНГА:**
- ✅ **Метрики:** Отслеживание активных соединений, RPS, ошибок
- ✅ **Алерты:** Автоматические предупреждения при превышении лимитов
- ✅ **Производительность:** Мониторинг CPU, памяти, времени ответа
- ✅ **Интеграция:** Встроена в gRPC сервер

#### **🧪 НАГРУЗОЧНОЕ ТЕСТИРОВАНИЕ:**
- ✅ **Скрипт:** Автоматическое тестирование до 100 пользователей
- ✅ **Метрики:** Измерение RPS, времени ответа, успешности
- ✅ **Анализ:** Автоматическая оценка готовности к масштабированию
- ✅ **Отчеты:** Детальная статистика производительности

#### **🔧 СОВМЕСТИМОСТЬ БИБЛИОТЕК:**
- ✅ **Protobuf:** Обновлен до версии 6.32.1
- ✅ **gRPC:** Обновлен до версии 1.75.1
- ✅ **Другие библиотеки:** Обновлены до последних версий
- ✅ **Конфликты:** Устранены все проблемы совместимости

---

## ✅ 1) Клиент: интеграции и UX (S/L/P) - ЗАВЕРШЕНО
**Цель**: стабильный UX и полный пользовательский цикл S→L→P→S.

✅ **ЭТАП 1 ПОЛНОСТЬЮ ЗАВЕРШЕН (15.01.2025):**
- ✅ Реализован полный end‑to‑end поток с event-driven переходами
- ✅ Workflows заменили жесткие таймауты на умную координацию
- ✅ Унифицированы прерывания через `playback.cancelled`
- ✅ PyAudio исправлен - реальное распознавание речи работает
- ✅ Все 19 интеграций + workflows реализованы и протестированы
- ✅ VoiceOver интеграция - умное управление для пользователей с нарушениями зрения
- ✅ WelcomeMessage интеграция - приветственное сообщение при запуске
- ✅ Проект оптимизирован - удалено 71 лишний файл
- ✅ Архитектура готова к продакшену

- 1.1 Tray стабилизация
  - Действия: подписка на `app.mode_changed` и `voice.mic_opened/closed`; индикация S/L/P; текст статуса; позже — `network.status_changed`.
  - Тест‑гейт: смена режима мгновенно меняет статус в трее.

- 1.2 Permissions стабилизация
  - Действия: проверка на старте; публикация `permission.*`; инструкции/открытие настроек при отказе.
  - Тест‑гейт: без разрешений — видны инструкции; с разрешениями — событие `permission.all_granted`.

- 1.3 InputProcessing стабилизация
  - Действия: `long_press`→LISTENING; `release`→PROCESSING; `short_press`/ошибка→SLEEPING; дебаунс/анти‑дребезг.
  - Тест‑гейт: надёжные переходы без гонок.

- 1.4 Update Manager (тихий режим)
  - Действия: фоновая проверка; без UI‑диалогов; лог статуса.
  - Тест‑гейт: при запуске фиксируется проверка; без всплывающих окон.

- 1.5 NetworkManagerIntegration
  - Действия: минимальный `NetworkManager` (TCP/53), интеграция, снапшот на `app.startup`; tray tooltip сети.
  - Тест‑гейт: off/on сети → события `network.status_changed`, tray отражает.

- 1.6 AudioDeviceIntegration
  - Действия: выбор/мониторинг устройств (без открытия записи). Физический захват микрофона выполняет VoiceRecognitionIntegration.
  - Тест‑гейт: корректный снапшот/переключения устройств; отсутствие «already running».

- 1.7 InterruptManagementIntegration
  - Действия: `short_press`/ошибка/timeout → безопасный возврат в SLEEPING; останов активных потоков.
  - Тест‑гейт: прерывание из LISTENING/PROCESSING всегда завершает корректно.

- 1.8 VoiceRecognitionIntegration (LISTENING)
  - Действия: LONG_PRESS → `voice.recording_start` → реальное `start_listening()`; RELEASE → `voice.recording_stop` (UI обновляется через `voice.mic_closed`), затем результат (`voice.recognition_completed/failed`). Короткий тап (SHORT_PRESS) возвращает в SLEEPING без открытия микрофона.
  - Тест‑гейт: реальное распознавание работает; события приходят в правильном порядке; нет дублей.

- 1.9 ScreenshotCaptureIntegration (PROCESSING)
  - Действия: захват скриншота по событию `voice.recording_stop` (совпадает с переходом в PROCESSING); оптимизация размера; обработка ошибок разрешений.
  - Тест‑гейт: скрин получен; отказ — событие ошибки.

- 1.10 GrpcClientIntegration (PROCESSING)
  - Действия: отправка (текст+скрин+HWID) на сервер; ретраи/backoff зависят от `network`.
  - Тест‑гейт: успешный ответ; при `DISCONNECTED` — не спамит и восстанавливается.

 - 1.11 SpeechPlaybackIntegration (внутри PROCESSING) — базовая
  - Действия: воспроизведение ответа; по окончании публикует `playback.completed` (использовать для выхода из PROCESSING).
  - Прерывания: НЕ внедряем на этом шаге (минимально жизнеспособная реализация без отмен).
  - Тест‑гейт: аудио доигрывается до конца; корректный переход в SLEEPING по событию.

 - 1.11b SpeechPlaybackInterrupts — расширение
  - Действия: `interrupt.request{scope: playback|all}` и `keyboard.short_press` немедленно останавливают плеер → `playback.cancelled` → (врем.) `processing.complete`.
  - Тест‑гейт: прерывание в любой момент безопасно возвращает в SLEEPING; нет гонок.

- 1.12 FSM + Workflows (3 файла) + прерывания
  - Действия: формализовать переходы/таймауты/анти‑гонки; внедрить `sleeping_workflow.py`, `listening_workflow.py`, `processing_workflow.py` (подэтапы: capture→grpc→playback) с единым протоколом прерываний.
  - Прерывания (настройка): определить `interrupt.request{scope: voice|capture|grpc|playback|all, priority, interrupt_id, deadline_ms, reason}` и `interrupt.completed{interrupt_id, result}`; интегрировать точки отмены в каждый подпроцесс; централизованный возврат в SLEEPING через координатор.
  - Тест‑гейт: нет гонок; стабильные сценарии с прерыванием/таймаутами во всех стадиях S/L/P.

**✅ Exit‑критерий Этапа 1 ДОСТИГНУТ**: Полный цикл S→L→P→S проходит стабильно; логика через EventBus; интеграции тонкие; Workflows реализованы; логи без PII.

### Последовательность внедрения (дорожная карта)
1) ScreenshotCaptureIntegration → `screenshot.captured|error`
2) GrpcClientIntegration → `grpc.request_*`
3) SpeechPlaybackIntegration (базовая реализация без прерываний)
4) SpeechPlaybackInterrupts (прерывания для плеера)
5) Формализация `listening_workflow.py` и `processing_workflow.py`
6) Расширение InterruptManagementIntegration (interrupt_id, дедлайны, дедуп)

---

## 🚀 2) ПАРАЛЛЕЛЬНАЯ УПАКОВКА + ДЕПЛОЙ - ТЕКУЩИЙ ЭТАП
**Цель**: параллельная упаковка PKG и деплой сервера для максимального ускорения.
**Статус**: Готово к запуску параллельных потоков.

### **🔥 ПОТОК 1: УПАКОВКА PKG (2-3 часа)**
- 2.1 Сборка .app (см. PACKAGING_PLAN.md)
  - Действия: PyInstaller (.spec) → `.app`; `entitlements.plist` (Mic, Screen Recording, Notifications, Accessibility, VoiceOver).
  - **🧪 ТЕСТ:** Запуск .app локально
  - **✅ КРИТЕРИЙ:** `.app` запускается без ошибок

- 2.2 Подпись .app (см. PACKAGING_PLAN.md)
  - Действия: `codesign` (Developer ID Application, hardened runtime, entitlements).
  - **🧪 ТЕСТ:** Проверка подписи
  - **✅ КРИТЕРИЙ:** `codesign --verify --deep --strict` OK

- 2.3 Сборка и подпись PKG (см. PACKAGING_PLAN.md)
  - Действия: `productbuild` → `.pkg`; `productsign` (Developer ID Installer).
  - **🧪 ТЕСТ:** Локальная установка PKG
  - **✅ КРИТЕРИЙ:** PKG устанавливается без ошибок

- 2.4 Нотарификация и staple (см. PACKAGING_PLAN.md)
  - Действия: `notarytool submit --wait` для `.pkg`; `stapler staple`.
  - **🧪 ТЕСТ:** Установка на чистом пользователе
  - **✅ КРИТЕРИЙ:** PKG устанавливается без Gatekeeper предупреждений

### **🔥 ПОТОК 2: ДЕПЛОЙ СЕРВЕРА - ✅ ПОЛНОСТЬЮ ЗАВЕРШЕНО (2 октября 2025)**

#### **2.5 Azure VM и Инфраструктура ✅ ЗАВЕРШЕНО**
- **VM:** `nexy-regular` (Standard_D2s_v3, 2 vCPUs, 8 GiB RAM)
- **IP:** `20.151.51.172` (публичный, статический)
- **Регион:** Canada Central
- **ОС:** Ubuntu 22.04 LTS
- **Статус:** ✅ Active, стабильная работа

#### **2.6 gRPC Server ✅ ЗАВЕРШЕНО**
  - Действия: ✅ копирование `server/` на Azure VM (20.151.51.172); ✅ установка зависимостей; ✅ настройка systemd сервиса.
  - **🧪 ТЕСТ:** ✅ Проверка gRPC сервера
  - **✅ КРИТЕРИЙ:** ✅ gRPC сервер отвечает на порту 50051

- 2.6 Настройка AppCast сервера ⏳ **ОПЦИОНАЛЬНО**
  - Действия: настройка update-server на порту 8081; генерация appcast.xml; размещение PKG файлов.
  - **🧪 ТЕСТ:** Проверка AppCast доступности
  - **✅ КРИТЕРИЙ:** AppCast доступен по http://20.151.51.172:8081/appcast.xml

- 2.7 Автоматический деплой ✅ **ЗАВЕРШЕНО**
  - Действия: ✅ создан скрипт обновления; ✅ настроен GitHub Actions; ✅ создан Service Principal.
  - **🧪 ТЕСТ:** ✅ Проверка автоматического деплоя
  - **✅ КРИТЕРИЙ:** ✅ Push в main → автоматическое обновление на VM

**Exit‑критерий Этапа 2**: ✅ gRPC сервер работает; ✅ автоматический деплой настроен; ⏳ PKG подписан/нотарифицирован/степлен; ⏳ AppCast доступен; экономия времени 1-2 часа.

---

## 📊 **ТЕКУЩИЙ СТАТУС (2 ОКТЯБРЯ 2025): СЕРВЕР ПОЛНОСТЬЮ РАБОТАЕТ**

### ✅ **PRODUCTION СЕРВЕР - ПОЛНОСТЬЮ ГОТОВ:**

#### **Инфраструктура:**
- **Azure VM:** `nexy-regular` (Standard_D2s_v3, 2 vCPUs, 8 GiB RAM)
- **IP адрес:** `20.151.51.172` (публичный, статический)
- **Регион:** Canada Central
- **ОС:** Ubuntu 22.04 LTS
- **Статус:** ✅ Active (running) - стабильная работа с 01:44:16 UTC
- **Uptime:** Стабильно без перезагрузок
- **Ресурсы:** RAM: 96MB/8GB (оптимально), CPU: стабильно

#### **Сервисы:**
- **gRPC Server:** ✅ Порт 50051 - 100 воркеров, готов к 100 пользователям
- **HTTP Server:** ✅ Порт 8080 - health checks & status API
- **Nginx Proxy:** ✅ Порт 80 - reverse proxy → 8080
- **Update Server:** ✅ Порт 8081 - Sparkle обновления
- **Systemd Service:** ✅ `voice-assistant.service` - active (running)

#### **Health Checks:**
- **Health Endpoint:** ✅ `http://20.151.51.172/health` → `200 OK`
- **Status API:** ✅ `http://20.151.51.172/status` → JSON метрики
- **gRPC Port:** ✅ `20.151.51.172:50051` → активен и слушает

#### **Git & CI/CD:**
- **Репозиторий:** ✅ `https://github.com/Seregawpn/Nexy_server.git`
- **Автоматический деплой:** ✅ Скрипт `/home/azureuser/update-server.sh`
- **GitHub Actions:** ⚠️ Workflow настроен, требует исправления Azure auth
- **Service Principal:** ✅ Создан и настроен
- **Protobuf Regeneration:** ✅ Автоматическая при каждом обновлении
- **Rollback Mechanism:** ✅ Автоматический откат при ошибках

#### **Модули и Компоненты:**
- **Text Processing:** ✅ Ready (Gemini API)
- **Audio Generation:** ✅ Ready (Azure Speech)
- **Session Management:** ✅ Active (до 100 сессий)
- **Memory Management:** ✅ Active
- **Interrupt Handling:** ✅ Active
- **Database:** ✅ Connected (PostgreSQL)
- **Monitoring:** ✅ Active (метрики и алерты)
- **GitHub Secrets:** Добавлены и работают
- **Тестирование деплоя:** Выполнено успешно (30 сентября 2025)
- **Синхронизация репозиториев:** Работает корректно
- **Обновление зависимостей:** Автоматическое
- **Проблемы решены:** Конфликты версий grpcio, protobuf, зависимости

### ⏳ **ГОТОВО К ЗАПУСКУ:**
- **Упаковка PKG/DMG:** Подпись + нотаризация
- **AppCast сервер:** Настройка update-server на порту 8081
- **Тестирование обновлений:** Полный цикл проверки

### 🔧 **СЛЕДУЮЩИЕ ШАГИ:**
1. **Добавить GitHub Secrets** (5 мин) - для автоматического деплоя ✅ **ЗАВЕРШЕНО**
2. **Протестировать деплой** - сделать push в main ✅ **ЗАВЕРШЕНО**
3. **Запустить упаковку PKG** - подпись + нотаризация ⏳ **ГОТОВО К ЗАПУСКУ**
4. **Настроить AppCast** - update-server на порту 8081 ⏳ **ГОТОВО К ЗАПУСКУ**

---

## 📁 **ВАЖНО: СТРУКТУРА РЕПОЗИТОРИЕВ**

### **🔗 ДВА РЕПОЗИТОРИЯ:**

**1. Основной проект (локальная разработка):**
- **URL:** `https://github.com/Seregawpn/nexy_new.git`
- **Назначение:** Полный проект (клиент + сервер)
- **Использование:** Локальная разработка, тестирование
- **Структура:** `client/` + `server/` + документация

**2. Серверный репозиторий (Azure деплой):**
- **URL:** `https://github.com/Seregawpn/Nexy_server.git`
- **Назначение:** Только серверная часть для Azure VM
- **Использование:** Автоматический деплой на Azure VM
- **Структура:** Только `server/` файлы + GitHub Actions

### **🔄 ПРОЦЕСС СИНХРОНИЗАЦИИ:**

**При обновлении сервера:**
1. **Разработка** → в основном репозитории (`nexy_new`)
2. **Синхронизация** → копирование `server/` в `Nexy_server`
3. **Деплой** → автоматический через GitHub Actions

**Команды для синхронизации:**
```bash
# Клонировать серверный репозиторий
git clone https://github.com/Seregawpn/Nexy_server.git nexy_server_temp

# Скопировать обновленную версию сервера
cp -r server/* nexy_server_temp/
cp -r server/.* nexy_server_temp/ 2>/dev/null || true

# Обновить репозиторий
cd nexy_server_temp
git add .
git commit -m "🚀 Обновление сервера: [описание изменений]"
git push origin main --force

# Очистить временную директорию
cd .. && rm -rf nexy_server_temp
```

### **⚠️ ВАЖНЫЕ МОМЕНТЫ:**
- **Azure VM** настроена на `Nexy_server` репозиторий
- **GitHub Actions** работает с `Nexy_server`
- **Локальная разработка** ведется в `nexy_new`
- **Синхронизация** нужна при каждом обновлении сервера

---

## 🧪 3) ТЕСТИРОВАНИЕ СИСТЕМЫ ОБНОВЛЕНИЙ - ГОТОВО К ЗАПУСКУ
**Цель**: проверка полного цикла обновлений и интеграции клиент-сервер.
**Статус**: Готово к тестированию после завершения упаковки PKG.

- 3.1 Проверка AppCast доступности
  - Действия: проверка http://20.151.51.172:8081/appcast.xml; валидация XML; проверка ссылок на PKG.
  - **🧪 ТЕСТ:** Валидация AppCast XML
  - **✅ КРИТЕРИЙ:** AppCast возвращает валидный XML с актуальной версией

- 3.2 Тестирование клиента обновлений
  - Действия: запуск клиента; ручная проверка обновлений; анализ логов в ~/Library/Logs/Nexy/updater.log.
  - **🧪 ТЕСТ:** Проверка клиента обновлений
  - **✅ КРИТЕРИЙ:** Клиент успешно проверяет обновления без ошибок

- 3.3 Полный цикл обновления
  - Действия: создание тестовой версии; загрузка PKG на сервер; тестирование скачивания и установки; проверка перезапуска.
  - **🧪 ТЕСТ:** Полный цикл обновления
  - **✅ КРИТЕРИЙ:** Полный цикл обновления работает без ошибок

**Exit‑критерий Этапа 3**: Система обновлений полностью функциональна; клиент успешно обновляется с сервера.

---

## 🧪 **ДЕТАЛЬНАЯ СИСТЕМА ЦИКЛИЧНОГО ТЕСТИРОВАНИЯ**

### **🔄 ПРИНЦИП: ТЕСТ → ВАЛИДАЦИЯ → ПЕРЕХОД**
```
┌─────────┐    ┌─────────────┐    ┌──────────┐
│  ТЕСТ   │───▶│ ВАЛИДАЦИЯ   │───▶│ ПЕРЕХОД  │
│         │    │             │    │          │
│ Выполня-│    │ Проверка    │    │ К следу- │
│ ем      │    │ критериев   │    │ ющему    │
│ проверки│    │ успеха      │    │ этапу    │
└─────────┘    └─────────────┘    └──────────┘
     ▲                                    │
     │                                    │
     └─────────── НЕУДАЧА ────────────────┘
     │
     ▼
┌─────────────┐
│ ИСПРАВЛЕНИЕ │
│             │
│ Анализ      │
│ ошибок      │
│ и исправ-   │
│ ление       │
└─────────────┘
```

### **📋 ПРАВИЛА ЦИКЛИЧНОГО ТЕСТИРОВАНИЯ:**
1. **НЕ ПЕРЕХОДИМ** к следующему этапу без успешного прохождения тестов
2. **ДОКУМЕНТИРУЕМ** все результаты тестирования
3. **АНАЛИЗИРУЕМ** неудачи и исправляем проблемы
4. **ПОВТОРЯЕМ** тесты после исправлений
5. **ВЕДЕМ** журнал всех тестовых циклов

---

### **🚀 ЭТАП 1: ПОДГОТОВКА (3 теста)**

#### **🧪 ТЕСТ 1.1: Проверка готовности упаковки**
**Действия:**
```bash
ls -la client/packaging/
ls -la client/packaging/build_final.sh
ls -la client/packaging/Nexy.spec
ls -la client/packaging/entitlements.plist
ls -la client/packaging/distribution.xml
```
**✅ КРИТЕРИЙ:** Все файлы упаковки присутствуют, build_final.sh исполняемый

#### **🧪 ТЕСТ 1.2: Проверка готовности сервера**
**Действия:**
```bash
ls -la server/
ls -la server/main.py
ls -la server/grpc_server.py
ls -la server/requirements.txt
ls -la server/config.env
```
**✅ КРИТЕРИЙ:** Все серверные файлы присутствуют, requirements.txt актуален

#### **🧪 ТЕСТ 1.3: Проверка конфигурации обновлений**
**Действия:**
```bash
grep -A 10 "updater:" client/config/unified_config.yaml
grep -A 5 "appcast:" client/config/network_config.yaml
```
**✅ КРИТЕРИЙ:** appcast_url настроен на IP (20.151.51.172), параметры корректны

---

### **🚀 ЭТАП 2: ПАРАЛЛЕЛЬНАЯ УПАКОВКА + ДЕПЛОЙ (7 тестов)**

#### **🔥 ПОТОК 1: УПАКОВКА (4 теста)**

**🧪 ТЕСТ 2.1.1: Сборка .app**
**Действия:** `cd client/packaging && ./build_final.sh`
**✅ КРИТЕРИЙ:** .app файл создан в dist/, приложение запускается локально

**🧪 ТЕСТ 2.1.2: Подпись .app**
**Действия:** `codesign --verify --deep --strict dist/Nexy.app`
**✅ КРИТЕРИЙ:** Подпись валидна, нет ошибок верификации

**🧪 ТЕСТ 2.1.3: Сборка и подпись PKG**
**Действия:** `pkgutil --check-signature dist/Nexy.pkg && sudo installer -pkg dist/Nexy.pkg -target /`
**✅ КРИТЕРИЙ:** PKG создан успешно, подпись валидна, установка проходит

**🧪 ТЕСТ 2.1.4: Нотаризация**
**Действия:** `xcrun stapler validate dist/Nexy.pkg && spctl --assess --type install dist/Nexy.pkg`
**✅ КРИТЕРИЙ:** Нотаризация успешна, PKG проходит Gatekeeper

#### **🔥 ПОТОК 2: ДЕПЛОЙ СЕРВЕРА (3 теста)**

**🧪 ТЕСТ 2.2.1: Деплой gRPC сервера**
**Действия:** 
```bash
scp -r server/ nexy@20.151.51.172:/home/nexy/app/
ssh nexy@20.151.51.172 "cd /home/nexy/app/server && python3.11 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt"
ssh nexy@20.151.51.172 "sudo systemctl start nexy-grpc"
```
**✅ КРИТЕРИЙ:** Файлы скопированы, зависимости установлены, сервис запущен

**🧪 ТЕСТ 2.2.2: Проверка gRPC сервера**
**Действия:**
```bash
ssh nexy@20.151.51.172 "systemctl status nexy-grpc"
ssh nexy@20.151.51.172 "netstat -tlnp | grep 50051"
telnet 20.151.51.172 50051
```
**✅ КРИТЕРИЙ:** Сервис активен, порт 50051 открыт, подключение успешно

**🧪 ТЕСТ 2.2.3: Настройка AppCast сервера**
**Действия:**
```bash
ssh nexy@20.151.51.172 "sudo systemctl start nexy-update"
curl -v http://20.151.51.172:8081/appcast.xml
```
**✅ КРИТЕРИЙ:** update-server запущен, AppCast доступен, XML валиден

---

### **🧪 ЭТАП 3: ТЕСТИРОВАНИЕ ОБНОВЛЕНИЙ (3 теста)**

**🧪 ТЕСТ 3.1: Проверка AppCast доступности**
**Действия:**
```bash
curl -f -s http://20.151.51.172:8081/appcast.xml
xmllint --noout http://20.151.51.172:8081/appcast.xml
curl -I http://20.151.51.172:8081/Nexy.pkg
```
**✅ КРИТЕРИЙ:** AppCast возвращает HTTP 200, XML валиден, PKG файл доступен

**🧪 ТЕСТ 3.2: Тестирование клиента обновлений**
**Действия:**
```bash
cd client && python main.py &
CLIENT_PID=$!
sleep 5
tail -f ~/Library/Logs/Nexy/updater.log
kill $CLIENT_PID
```
**✅ КРИТЕРИЙ:** Клиент запускается без ошибок, логи создаются, нет критических ошибок

**🧪 ТЕСТ 3.3: Полный цикл обновления**
**Действия:**
```bash
./scripts/create_version_release.sh v1.0.1 "Test update"
scp client/dist/Nexy.pkg nexy@20.151.51.172:/var/www/nexy/appcast/
# Ручная проверка через клиент
```
**✅ КРИТЕРИЙ:** Тестовая версия создана, PKG загружен, клиент видит обновление, установка успешна

---

### **📊 ЖУРНАЛ ТЕСТИРОВАНИЯ**

**📋 ШАБЛОН ЗАПИСИ ТЕСТА:**
```
Дата: YYYY-MM-DD HH:MM:SS
Тест: [Название теста]
Этап: [Номер этапа]
Результат: ✅ УСПЕХ / ❌ НЕУДАЧА
Детали: [Описание результата]
Исправления: [Если неудача - что исправлено]
Следующий тест: [Название следующего теста]
```

**📈 МЕТРИКИ КАЧЕСТВА:**
- **Процент успешных тестов:** ≥95%
- **Время на исправление:** ≤30 минут на тест
- **Количество итераций:** ≤3 на этап
- **Критические ошибки:** 0

---

### **🎯 КРИТЕРИИ ГОТОВНОСТИ К ПРОДАКШЕНУ**

**✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ:**
1. **Упаковка:** PKG подписан, нотарифицирован, устанавливается
2. **Сервер:** gRPC работает, AppCast доступен
3. **Обновления:** Полный цикл обновления функционирует
4. **Интеграция:** Клиент-сервер взаимодействие работает

**🚀 ГОТОВНОСТЬ К ЗАПУСКУ:**
- Все критические тесты пройдены
- Нет блокирующих ошибок
- Документация обновлена
- Команда готова к продакшену

**Exit‑критерий Этапа 3**: Продовый сервер доступен; клиент работает end‑to‑end; обновления распределяются с Azure.

---

## 🔁 Зависимости и порядок
- Этап 1 → Этап 2 → Этап 3. Этап 2 можно готовить к концу Этапа 1 (скрипты подписи/нотаризации). Этап 3 можно поднимать параллельно 1.9–1.11.

## ⚙️ Конфиг, логи, безопасность
- Конфиги клиента: `client/config/*.yaml` — `grpc_host`, `grpc_port`, `appcast_url`, таймауты, ретраи, backoff.
- Логи: единый формат, уровни по компонентам; без PII; ключевые события (режимы/сеть/обновления).
- Разрешения/Entitlements: Mic, Screen Recording, Notifications, Accessibility, VoiceOver, Network — согласованы с `permissions`.
- Секреты: Apple (подпись/нотаризация) — локально/в защищенном хранилище; Azure — App Settings/Key Vault.

---

## ✅ Текущий статус (сводно)
- ✅ **ЭТАП 1 ЗАВЕРШЕН:** Все 19 интеграций + workflows реализованы
- ✅ **Архитектура:** Event-driven FSM, унифицированные прерывания
- ✅ **Полный цикл:** S→L→P→S работает стабильно
- ✅ **VoiceOver интеграция:** Умное управление для пользователей с нарушениями зрения
- ✅ **WelcomeMessage интеграция:** Приветственное сообщение при запуске
- ✅ **Оптимизация:** Проект очищен, готов к продакшену
- 🔥 **ТЕКУЩИЙ ФОКУС:** Настройка сертификатов → PKG упаковка → Azure развертывание → E2E тестирование

---

## 📌 Мини‑контрольные списки (пример)
- Клиент/Сеть: off/on → `network.status_changed`, tray отражает.
- Голосовой цикл: S→L→P→S — без гонок; ресурсы освобождены.
- PKG: `codesign`/`productbuild`/`productsign`/`notarytool`/`stapler` — все OK.
- Azure: health “Serving”; TLS/HTTP2 включены; `appcast.xml`/PKG по HTTPS.

---

## 🗂 Связанные документы
- `client/Docs/INTEGRATION_MASTER_PLAN.md` — подробный план интеграции.
- `client/Docs/PRODUCT_CONCEPT.md` — UX и сценарии.
- (Auth/Chat — отложено; план удалён из репозитория)
- `client/PACKAGING_README.md`, `PACKAGING_README.md`, `PRODUCTION_BUILD_GUIDE.md` — упаковка.
- `AZURE_SETUP.md` — заметки по Azure (при необходимости дополнить).

---

## ☁️ Azure VM — параметры и чек‑лист переноса ✅ **ЗАВЕРШЕНО**

### ✅ **ТЕКУЩИЕ ПАРАМЕТРЫ (НАСТРОЕНЫ И РАБОТАЮТ):**
- **Resource group**: Nexy
- **Region**: Canada Central
- **VM OS**: Linux (Ubuntu 22.04)
- **VM Name**: nexy-regular
- **IP Address**: 20.151.51.172
- **Size**: Standard_D2s_v3 (2 vCPUs, 8 GiB RAM)
- **Status**: ✅ Active (running)

### ✅ **НАСТРОЕННЫЕ СЕРВИСЫ:**
- **HTTP Server**: ✅ Работает на порту 8080 (проксируется через nginx на порт 80)
- **gRPC Server**: ✅ Работает на порту 50051
- **Health Endpoints**: ✅ `/health` и `/status` доступны
- **Systemd Service**: ✅ `voice-assistant.service` настроен и работает
- **Nginx**: ✅ Работает как reverse proxy
- **Git Repository**: ✅ `https://github.com/Seregawpn/Nexy_server.git` клонирован

### ✅ **АВТОМАТИЧЕСКИЙ ДЕПЛОЙ НАСТРОЕН:**
- **Update Script**: ✅ `/home/azureuser/update-server.sh` создан и протестирован
- **Error Handling**: ✅ Автоматический откат при проблемах
- **Health Checks**: ✅ Проверка работоспособности после обновления
- **Logging**: ✅ Все операции записываются в лог
- **Service Principal**: ✅ Создан для GitHub Actions
- **GitHub Actions**: ✅ Workflow `.github/workflows/deploy-to-azure.yml` готов

### ✅ **ИСПРАВЛЕННЫЕ ПРОБЛЕМЫ:**
- **Port Conflict**: ✅ Исправлен конфликт порта 80 (изменен на 8080)
- **Git Permissions**: ✅ Настроены безопасные права доступа к репозиторию
- **Systemd Service**: ✅ Настроен автозапуск и перезапуск при ошибках
- **Dependencies**: ✅ Обновлены все Python зависимости

### 🔧 **СЛЕДУЮЩИЕ ШАГИ:**
1. **GitHub Secrets**: Добавить `AZURE_CREDENTIALS` в GitHub Repository Settings
2. **Test Deploy**: Протестировать первый автоматический деплой
3. **SSH Access**: Настроить SSH доступ для удобного управления (опционально)
4. **Update Server**: Настроить update сервер на порту 8081 (опционально)
- **Size**: Standard D2s v3 (2 vCPUs, 8 GiB)
- **Public IP (primary NIC)**: 20.151.51.172
- **VNet/Subnet**: nexy-vnet/default
- **DNS name**: Not configured (настроить ниже)
- **Subscription**: Azure subscription 1
- **Subscription ID**: 6d225f4c-756c-41ff-b361-62f248a60a2d
- **Status**: Stopped (deallocated) — перед переносом запустить

### План действий для переноса без Docker/CI
1) Сетевые настройки и безопасность
   - Закрепить Public IP как Static.
   - Настроить DNS‑имя для IP (например, `api.yourdomain.com`).
   - Открыть порты: 22 (временно под ваш IP), 80 (HTTP, для certbot), 443 (HTTPS, HTTP/2).
   - Включить UFW/NSG правила, после деплоя ограничить/закрыть 22.
2) Подготовка системы
   - Создать пользователя `nexy`; обновить систему пакетов.
   - Установить: `python3.11`, `python3.11-venv`, `nginx`, `certbot`, `python3-certbot-nginx`.
3) Доставка кода сервера (`server/`)
   - Вариант A: `scp` архива с локальной машины → `~nexy/app/server/`.
   - Вариант B: `curl -L -o release.zip` из GitHub Releases → распаковать.
   - Заполнить `config.env` по `server/config.env.example`.
   - Создать venv и установить зависимости: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`.
4) Сервис gRPC
   - systemd unit `nexy-grpc.service` (слушает `127.0.0.1:50051`, HTTP/2):
     - ExecStart: `/home/nexy/app/server/.venv/bin/python grpc_server.py --host 127.0.0.1 --port 50051`
     - Restart=always, WantedBy=multi-user.target
5) Nginx + TLS + статические файлы обновлений
   - Выдать сертификат: `sudo certbot --nginx -d api.yourdomain.com`.
   - Nginx 443: `listen 443 ssl http2;` и прокси `grpc_pass grpc://127.0.0.1:50051;`.
   - Папка для AppCast/PKG: `/var/www/nexy/appcast/`.
   - Раздача обновлений по `https://api.yourdomain.com/updates/` (alias на папку выше).
6) AppCast/PKG
   - Разместить `appcast.xml` и `Nexy-x.y.z.pkg` в `/var/www/nexy/appcast/`.
   - Проверить доступность: `https://api.yourdomain.com/updates/appcast.xml`.
7) Клиентские конфиги
   - `client/config/app_config.yaml` / `network_config.yaml`:
     - `grpc_host: api.yourdomain.com`, `grpc_port: 443`, `use_tls: true`.
     - `appcast_url: https://api.yourdomain.com/updates/appcast.xml`.
     - (План) `auth.enabled: true` — клиент добавляет `authorization: Bearer <token>` в metadata всех RPC.
8) Проверки
   - `systemctl status nexy-grpc` — активен; `nginx -t` — OK; certbot — валидный cert.
   - Клиентский сценарий S→L→P→S работает; Sparkle тянет апдейт с `appcast.xml`.

### Плейсхолдеры для заполнения
- Домен (A/AAAA к 20.151.51.172): `api.yourdomain.com`
- Email для Certbot: `admin@yourdomain.com`
- Пути публикации AppCast/PKG: `/var/www/nexy/appcast/`
- Версии релизов и ссылки внутри `appcast.xml`

---

## 🔐 Подпись и нотарификация — параметры и безопасное хранение

### Данные (несекретные — фиксируем в плане)
- Apple ID (email): seregawpn@gmail.com
- Team ID (App ID Prefix): 5NKLL2CLB9
- Bundle ID (explicit): com.nexy.assistant
- Платформы: iOS, iPadOS, macOS, tvOS, watchOS, visionOS
- Название проекта: Nexy

> Примечание: App‑Specific Password передается и хранится ТОЛЬКО локально в Keychain, не коммитится в репозиторий.

### Сертификаты (плейсхолдеры — подставить точные имена из Keychain)
- Developer ID Application: "Developer ID Application: <Your Name> (5NKLL2CLB9)"
- Developer ID Installer:  "Developer ID Installer: <Your Name> (5NKLL2CLB9)"

Проверка наличия сертификатов:
```bash
security find-identity -p codesigning -v | cat
```

### Настройка notarytool (безопасное хранение App‑Specific Password)
Сохранить учетные данные в Keychain под профилем `nexy-notary` (пароль вводится локально и не попадает в git):
```bash
xcrun notarytool store-credentials nexy-notary \
  --apple-id seregawpn@gmail.com \
  --team-id 5NKLL2CLB9 \
  --keychain-profile nexy-notary
```

Нотарификация с использованием профиля:
```bash
xcrun notarytool submit Nexy.pkg --keychain-profile nexy-notary --wait
xcrun stapler staple Nexy.pkg
```

### Подпись .app и .pkg (шаблон команд)
```bash
# Подпись приложения (.app)
codesign --deep --force --options runtime \
  --entitlements client/entitlements.plist \
  --sign "Developer ID Application: <Your Name> (5NKLL2CLB9)" Nexy.app

# Сборка и подпись инсталлятора (.pkg)
productbuild --component Nexy.app /Applications Nexy.pkg
productsign --sign "Developer ID Installer: <Your Name> (5NKLL2CLB9)" Nexy.pkg Nexy.pkg

# Нотарификация и степлинг
xcrun notarytool submit Nexy.pkg --keychain-profile nexy-notary --wait
xcrun stapler staple Nexy.pkg
```

### Sparkle (обновления)
- Ключи Sparkle (EdDSA): хранить приватный ключ локально/в secret‑хранилище; публичный ключ можно хранить в репозитории.
- `appcast.xml`: размещаем на Azure (см. раздел Azure VM). Ссылки на `.pkg` по HTTPS.

### Конфиги клиента (привязка к подписанному релизу)
- `client/config/app_config.yaml`:
  - `appcast_url: https://api.<domain>.com/updates/appcast.xml`
- `client/config/network_config.yaml`:
  - `grpc_host: api.<domain>.com`, `grpc_port: 443`, `use_tls: true`

### Политика безопасности
- Не коммитить App‑Specific Password, .p12 и приватные ключи Sparkle в git.
- Использовать macOS Keychain и ограниченный доступ к секретам.
- При необходимости — отдельный пользователь macOS для сборки и подписи.

---

## ⚠️ Конфиденциальные данные (временно сохранены по запросу)

> ВНИМАНИЕ: хранение секретов в репозитории небезопасно. Рекомендуется перенести в macOS Keychain/секрет‑хранилище и сменить пароль после переноса.

- Apple ID (email): seregawpn@gmail.com
- Team ID: 5NKLL2CLB9
- Bundle ID: com.nexy.assistant
- App‑Specific Password: qtiv-kabm-idno-qmbl

> После завершения настройки notarytool/CI рекомендуется: 
> 1) РОТИРОВАТЬ App‑Specific Password в Apple ID.
> 2) Удалить этот раздел из репозитория.
### Аутентификация клиента (план)
- Токен аутентификации хранится в macOS Keychain
- gRPC вызовы сопровождаются `metadata.authorization: Bearer <token>`
- Минимальный CLI‑чат для валидации потока (отложено)
