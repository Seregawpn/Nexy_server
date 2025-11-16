## План вывода Nexy в тестовую бету (macOS)

**Обновлено:** 15 января 2025  
**Назначение:** единый источник истины о готовности продукта к закрытой бете. Документ фиксирует архитектуру клиента и сервера, проверенные механики обновлений, обязательные проверки и ожидаемый опыт тестеров.

---

## 1. Картина на сегодня

| Канал | Статус | Комментарии / ссылки |
|-------|--------|----------------------|
| Dev (CLI) | ✅ активен | Все интеграции поднимаются через `client/main.py`, см. `scripts/run_release_suite.py`. |
| Beta (.app) | ✅ сборка протестирована | Подписанный `.app` + PKG/DMG проверены по `Docs/PRE_PACKAGING_VERIFICATION.md` и `Docs/PACKAGING_READINESS_CHECKLIST.md`. |
| Production rollout | ⏳ чек-лист в работе | Инфраструктура готова, финализируем `Docs/GLOBAL_DELIVERY_PLAN.md` (DELIVERY-002). |

**Основные утверждения:**
- ✅ В кодовой базе включены **22 интеграции** (каталог `client/integration/integrations/`) и **19 модулей** (каталог `client/modules/`); все работают в составе EventBus-архитектуры.
- ✅ **Workflows** (`integration/workflows/`) управляют жизненным циклом LISTENING → PROCESSING → SLEEPING.
- ✅ **Обновления**: реализован HTTP AppCast + DMG/PKG пайплайн (`client/modules/updater/*`, конфиг `client/config/unified_config.yaml` секция `updater`).
- ✅ **Сервер** развёрнут на Azure VM (20.151.51.172): gRPC (50051), TLS-прокси (443), HTTP health (8080), Update service (8081). Точки входа — `server/server/main.py` и `server/server/modules/grpc_service/core/grpc_server.py`.
- ✅ **Мониторинг и тесты**: `scripts/run_release_suite.py`, `scripts/pre_build_gate.sh`, `scripts/prepare_release.sh` — зелёные.

**Активные риски:**  
`TCC-AX-001` — миграция с приватного `TCCAccessRequest` на публичный API.  
`AUDIO-035` — уточнить retry для CoreAudio HAL Error 35.  
`DELIVERY-002` — зафиксировать все шаги Azure/AppCast в `GLOBAL_DELIVERY_PLAN.md`.

---

## 2. Архитектура платформы

### 2.1 Клиентское приложение
- **Точка входа:** `client/main.py` — настраивает AppKit, румпс и EventBus, запускает `SimpleModuleCoordinator`.
- **Централизация конфигурации:** `client/config/unified_config.yaml` (единственный источник версий, серверов, приоритетов интеграций).
- **Координатор:** `integration/core/simple_module_coordinator.py` и `integration/core/state_manager.py` управляют EventBus и режимами.
- **Workflows:** `integration/workflows/` (BaseWorkflow, ListeningWorkflow, ProcessingWorkflow) выстраивают последовательность операций без прямых связей между интеграциями.
- **Модули (19 шт.)** находятся в `client/modules/` (grpc_client, updater, voice_recognition, permissions и т.д.). Модули не знают о режимах/состоянии.
- **Интеграции (22 шт.)** в `client/integration/integrations/` используют EventBus, чтобы связать бизнес-логику:
  - Жизненный цикл / UX: `mode_management`, `tray_controller`, `input_processing`, `voiceover_ducking`.
  - Доступность: `permissions`, `first_run_permissions`, `permission_restart`, `voiceover_ducking`, `update_notification`.
  - Обновления и стабильность: `updater_integration`, `update_notification_integration`, `instance_manager`, `autostart_manager`.
  - Графический/аудио пайплайн: `screenshot_capture`, `speech_playback`, `signal`, `voice_recognition`.
  - Сеть и внешние сервисы: `grpc_client`, `network_manager`, `hardware_id`.

**Ключевые инварианты:**
1. **Только EventBus** — между интеграциями нет прямых вызовов (см. `integration/core/event_bus.py`).
2. **Режимы жёстко централизованы** — любые изменения состояния проходят через `ModeManagementIntegration`.
3. **PTT по Left Shift** — задаётся в `unified_config.yaml` (`integrations.keyboard.key_to_monitor`).
4. **Доступность — по умолчанию**: FirstRunPermissions + PermissionRestart, VoiceOver ducking, голосовые уведомления обновлений.
5. **Верификация обновлений** — `client/modules/updater/verify.py` + `replace.py` гарантируют целостность DMG/PKG.

### 2.2 Сервер
- **Точка входа:** `server/server/main.py` — запускает aiohttp endpoints (`/health`, `/status`) и асинхронный gRPC сервер.
- **gRPC стек:** `server/server/modules/grpc_service/core/grpc_server.py` + `grpc_service_manager`. Контроль нагрузки (`backpressure.py`), перехватчики (`grpc_interceptor.py`).
- **Доменные модули:** `server/server/modules/audio_generation`, `text_processing`, `session_management`, `interrupt_handling`, `update`.
- **Конфигурация:** `server/server/config/unified_config.py` — один YAML/ENV источник (метаданные версии, порты, ключи Azure TTS, Gemini Live).
- **Обновления:** `server/server/modules/update` выдаёт AppCast/DMG, синхронизирован с клиентским конфигом (порты и URL).
- **Мониторинг и логирование:** `server/server/utils/logging_formatter.py`, `metrics_collector.py`; логика используется main.py и gRPC сервером.

---

## 3. Принципы разработки и эксплуатации

1. **Single Source of Truth:** версия приложения задаётся в `client/config/unified_config.yaml`, сервер читает метаданные из `server/server/config/unified_config.py`.
2. **Никаких «скрытых» параметров** — все фичефлаги и приоритеты описаны в YAML (см. секции `integrations`, `features`, `updater`).
3. **Accessibility-first:** горячие клавиши, VoiceOver, автоматические подсказки и голосовые уведомления обновлений активны всегда, отключение только через конфиг.
4. **Fail Fast + Restart:** `PermissionRestartIntegration` и `InstanceManagerIntegration` следят за консистентностью процессов.
5. **Безопасные обновления:** только HTTPS (допускается self-signed на бете), проверка контрольных сумм, голосовые подтверждения этапов обновления.
6. **Scriptable Releases:** каждый шаг релиза автоматизирован — см. раздел 5.

---

## 4. Обновления, упаковка и распространение

- **Упаковка:** PyInstaller → pkgbuild/productbuild → notarization. Скрипт: `scripts/prepare_release.sh` (включает pre-build gate, release suite, сборку PKG/DMG, валидацию).
- **Артефакты:** подписанный `.app`, `pkg`, `dmg`. Хранятся в `dist/` и загружаются на Azure VM в каталог `/var/www/updates`.
- **AppCast:** `https://20.151.51.172/updates/appcast.xml` (stable), а также beta/alpha каналы — задаются в `updater.default.channels`.
- **Клиентский апдейтер:** `client/modules/updater/net.py` (HTTP), `verify.py` (hash/подпись), `replace.py` (atomarная подмена `.app`), `dmg.py`/`pkg.py` (распаковка). Конфигурация — `unified_config.yaml` → `integrations.updater` и `updater.default`.
- **UX обновлений:** `UpdateNotificationIntegration` + `SignalIntegration` дают голосовую и звуковую обратную связь (progress, success, failure). Работает поверх SpeechPlayback.
- **Сервер обновлений:** часть `server/server/modules/update`, подключена в `server/server/main.py`. Следит за версией (`SERVER_VERSION`, `SERVER_BUILD`) и выдаёт JSON для health/status.

---

## 5. Проверки и автоматизация

| Скрипт / документ | Назначение |
|------------------|-----------|
| `scripts/pre_build_gate.sh` | Обязательные проверки перед сборкой (линтеры, статические анализаторы, специфические проверки TAL/permissions/updater). |
| `scripts/run_release_suite.py` | Интеграционные проверки: инициализация всех интеграций, EventBus, режимы, Bluetooth/audio, updater dry-run. |
| `scripts/prepare_release.sh` | Конвейер сборки PKG/DMG + notarization + выкладка AppCast. |
| `client/Docs/PRE_PACKAGING_VERIFICATION.md` | Журнал контрольных прогонов packaging/notarization. |
| `FINAL_UPDATE_FLOW_TEST_REPORT.md` | Подтверждённый отчёт по автообновлению. |
| `scripts/test_*` (tray, tal, critical_paths) | Дополнительные smoke-проверки. |

В CI (`.github/workflows/ci.yml`) запускаются pre-build gate и сокращённый release suite.

---

## 6. Опыт тестера

1. **Горячая клавиша:** Left Shift (удержание) → LISTENING, отпускание → PROCESSING. Альтернативы не предусмотрены; конфликтов с VoiceOver нет благодаря `VoiceOverDuckingIntegration`.
2. **Разрешения:** при первом запуске `FirstRunPermissionsIntegration` проводит пользователя через Microphone, Screen Recording, Input Monitoring, Accessibility, Notifications. `PermissionRestartIntegration` автоматически перезапускает приложение при выдаче критичных прав.
3. **Режимы:** три статуса в меню-баре (`assets/icons/*`): SLEEPING (серый), LISTENING (синий), PROCESSING (жёлтый). Все переходы управляются событиями `mode.*`.
4. **Поток запроса:** Left Shift удержан → сигнал `listen_start` → запись → скриншот (WebP base64) → gRPC → ответ (аудио + текст) → `playback.completed` + возврат в SLEEPING.
5. **Приватность:** скриншоты не сохраняются на диск; аудио хранится только в памяти. Логи (`logs/nexy.log`) содержат идентификаторы сессий без контента.
6. **Обновления:** при выходе новой версии клиент озвучивает старт/прогресс/результат, загружает DMG/PKG, проводит проверку, показывает уведомление об автоматическом перезапуске.

Сценарии «из коробки» (рекомендации тестерам): описать экран, описать картинку, описать график/таблицу. Производительность: TTV ≤ 5 с, полный ответ ≤ 30 с.

---

## 7. План движения и критерии готовности

### 7.1 Состояние циклов
- ✅ **Цикл 1 — Локальный клиент:** EventBus, режимы, 22 интеграции, оффлайн поведение.
- ✅ **Цикл 2 — Подписанный PKG + обновления:** упаковка, подпись, AppCast, TCC-потоки.
- ✅ **Цикл 3 — Удалённый сервер:** Azure VM, TLS, gRPC, производительность, восстановление сети.
- ⏳ **Цикл 4 — Закрытая бета:** подбор когорты, инструкции, сбор фидбека и телеметрии.

### 7.2 Требования ко входу в Цикл 4
1. Подписанный PKG/DMG загружены на AppCast, проверены вручную на 2–3 машинах.
2. Подготовлены инструкция для тестеров (permissions, hotkey, примеры сценариев) и канал обратной связи (Discord/email).
3. Минимальная телеметрия (`install`, `first_run`, `ptt`, `recognition_completed`, `grpc.request_*`, `playback.*`) включена.
4. Скрипты `run_release_suite.py` и `prepare_release.sh` прошли на последнем билде.

### 7.3 Действия на время беты
1. Сформировать волну 20–50 пользователей (US/CA accessibility community).
2. Выпустить билд N на AppCast, подтвердить автообновление на контрольной группе.
3. Провести «консьерж»-сессию с 3 пилотами и зафиксировать проблемы (логирование + обратная связь).
4. Запланировать мини-спринт на критические фидбеки, подготовить билд N+1.
5. Сформировать отчёт: TTV, успешность сценариев, топ-проблемы, предложения по улучшению UX.

---

## 8. Риски и next steps

| ID | Описание | Что делаем |
|----|----------|------------|
| TCC-AX-001 | Перевести проверку Accessibility на публичный API | Исследование API Accessibility Inspector + обновление `permissions`/`permission_restart`. |
| AUDIO-035 | Дебаунс/ретраи для HAL Error 35 | Анализ логов `default_audio` и `voice_recognition`, настройка `silent_window_seconds`, `retry_delay`. |
| DELIVERY-002 | Закрепить Azure/AppCast план | Обновить `Docs/GLOBAL_DELIVERY_PLAN.md`, описать выкладку AppCast и сервера обновлений. |

**Проект готов к закрытому бета-тестированию.** Следующий рубеж — успешное завершение Цикла 4 и блокировка Production rollout чек-листа.
