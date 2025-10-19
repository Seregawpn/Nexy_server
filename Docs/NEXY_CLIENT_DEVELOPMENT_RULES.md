# Nexy Client Development Rules

> Обновлено: 2025-10-20  
> Эти правила синхронизированы с текущим состоянием репозитория `client/`.

## 1. Контекст перед началом работы
Перед изменениями освежи знание ключевых документов:
- `Docs/PRODUCT_CONCEPT.md` — пользовательские сценарии и режимы.
- `Docs/ARCHITECTURE_OVERVIEW.md` — описание потоков событий и взаимодействия компонентов.
- `Docs/CURRENT_STATUS_REPORT.md` — актуальные истории, фичи и TODO.
- `Docs/GLOBAL_DELIVERY_PLAN.md` и `Docs/GO_TO_MARKET_BETA_PLAN_RU.md` — требования к релизам.
- `Docs/packaging/*` — вспомогательные материалы по поставке.
- `../Docs/PACKAGING_FINAL_GUIDE.md` — финальный пайплайн сборки .app/PKG (расположен на уровень выше каталога `client/`).

⚠️ Файл `PERMISSIONS_REPORT.md` в репозитории отсутствует. Если требуется вести учёт разрешений, создай его в `Docs/` и поддерживай вручную.

## 2. Среда выполнения и запуск
- Основная директория разработки: `client/`.
- macOS 13+, Python 3.11, зависимые инструменты указаны в `requirements.txt`.
- Точка входа: `python main.py` (в корне `client/`). Скрипт сам настраивает `sys.path` для `modules/` и `integration/`.
- Для `pydub` используется локальный `ffmpeg` по пути `resources/ffmpeg/ffmpeg`. Убедись, что бинарь присутствует или упакован внутрь `.app`.
- Сборка `.app` и PKG описана в `../Docs/PACKAGING_FINAL_GUIDE.md` (PyInstaller + pkgbuild/productbuild).

## 3. Архитектурные компоненты
- **Core (`integration/core/`)** — `EventBus`, `SimpleModuleCoordinator`, `ApplicationStateManager`, `ErrorHandler`.
- **Modules (`modules/*/`)** — низкоуровневая логика и платформенные детали.
- **Integrations (`integration/integrations/`)** — адаптеры между EventBus и модулями. Большинство интеграций — тонкие классы, некоторые (например, `VoiceOverDuckingIntegration`) наследуют `BaseIntegration`, остальные используют собственный жизненный цикл.
- **Workflows (`integration/workflows/`)** — координаторы режимов (Listening/Processing).
- **Core adapters (`integration/adapters/`)** — вспомогательные переходники (например, `EventBusAudioSink`).

Модуль `permissions` существует (`modules/permissions/`), но отдельная интеграция не реализована. Проверки разрешений распределены по интеграциям микрофона, скриншотов и VoiceOver.

## 4. Порядок инициализации и запуска
Фактический порядок задаётся в `SimpleModuleCoordinator._create_integrations()` и `start()`:
1. `instance_manager`
2. `hardware_id`
3. `tray`
4. `mode_management`
5. `input`
6. `voice_recognition`
7. `network`
8. `interrupt`
9. `screenshot_capture`
10. `grpc`
11. `speech_playback`
12. `updater`
13. `signals`
14. `welcome_message`
15. `voiceover_ducking`
16. `autostart_manager`

Не меняй порядок без проверки зависимостей — он влияет на состояние режима и готовность сервисов.

## 5. EventBus, режимы и контракты
- Центральный источник режимов — `ModeManagementIntegration`; `ApplicationStateManager` публикует `app.mode_changed` и `app.state_changed`.
- Основные режимы: `AppMode.SLEEPING → LISTENING → PROCESSING`. Прямой переход `SLEEPING → PROCESSING` используется приветствием (см. `ModeManagementIntegration`).
- Смена режима инициируется событиями `mode.request`. В существующем коде не все события передают `session_id`; при новой разработке включай `session_id` и `source`, когда это возможно.
- Контракты событий пока не оформлены в виде констант `CONTRACT`. Документируй используемые события в README интеграции/модуля и поддерживай раздел «Event log».
- Используй `EventPriority` по аналогии с текущими реализациями (critical для `mode.request`, medium для мониторинга и т. п.).

## 6. Конфигурация
- Единый источник — `config/unified_config.yaml`. Загружается через `config/unified_config_loader.py`.
- Раздел `integrations` управляет наличием и настройкой обёрток (например, `integrations.voice_recognition`).
- Новые параметры добавляй в `unified_config.yaml` и документируй в соответствующем README.
- Секреты/ключи не хардкодим — используем окружение/Keychain.

## 7. Взаимодействие с сервером
- gRPC схемы лежат в `../server/modules/grpc_service/streaming.proto`; сгенерированные stubs — в `../server/modules/grpc_service/*`.
- `GrpcClientIntegration` агрегирует данные по `session_id`, опираясь на настройки `unified_config`.
- При изменениях на сервере обновляй stubs и прогоняй интеграционные проверки (см. `tests/test_grpc_connection.py`).

## 8. Логирование и диагностика
- Текущий формат логов задаётся в `main.py` через `logging.basicConfig('%(asctime)s - %(name)s - %(levelname)s - %(message)s')`. Сессии/идентификаторы добавляются вручную в сообщениях.
- `ErrorHandler` хранит историю по severity/category (`ErrorSeverity`, `ErrorCategory`) и публикует `error.occurred`. Стандартизированные коды (`E_INPUT_INVALID` и т. п.) пока не внедрены — используй поля `context` и понятные сообщения.
- Логируй смену режимов, сетевые изменения, ошибки устройств и обновлений. Избегай чувствительных данных.
- Для диагностики доступны скрипты `run_diagnostics.py`, `test_audio_recording.py`, `test_device_monitor.py`.

## 9. Разрешения и системные интеграции
- Проверки микрофона, screen capture и accessibility делаются через соответствующие модули/интеграции (`voice_recognition`, `screenshot_capture`, `voiceover_control`).
- Если UX запросов меняется, заводи отдельную запись в `Docs/CURRENT_STATUS_REPORT.md` и (при появлении файла) обновляй `Docs/PERMISSIONS_REPORT.md`.
- Для VoiceOver используй настройки `accessibility.voiceover_control` из `unified_config`.

## 10. Тестирование
- Юнит-тесты располагаем рядом с модулем/интеграцией (`modules/*/tests`, `integration/tests`).
- Обязательные ручные проверки: push-to-talk, переключение режимов, Tray-меню, автообновление (Sparkle), VoiceOver ducking.
- Для регрессии используй сценарии из `Docs/CURRENT_STATUS_REPORT.md` и тестовые скрипты в `tests/`.

## 11. Чек-лист изменения
**Перед началом**
- Изучи существующие модули/интеграции на предмет переиспользования.
- Проверь `unified_config.yaml`, включение нужных интеграций и их параметры.
- Определи список событий EventBus и влияние на режимы.

**Во время**
- Соблюдай границу «интеграция ↔ модуль»: модули не импортируют другие модули напрямую.
- Поддерживай порядок инициализации `SimpleModuleCoordinator`.
- Документируй новые события/поля в README модуля или интеграции.
- Добавляй `session_id`, `source`, `reason`, когда публикуешь события от имени новой функциональности.

**После**
- Обнови `Docs/CURRENT_STATUS_REPORT.md` кратким описанием изменений.
- При добавлении интеграции зарегистрируй её в `SimpleModuleCoordinator` и `unified_config.yaml`.
- Запусти профильные тесты и зафиксируй результаты (минимально — ручная проверка happy-path).
- При изменении gRPC контракта синхронизируйся с серверной командой.

## 12. Известные ограничения и план улучшений
- Контракты EventBus не формализованы. При добавлении новой интеграции создавай раздел «Events» в README и поддерживай тесты, эмулирующие ключевые события.
- Логирование не добавляет `session_id` автоматически. Рассмотри расширение форматтера или внедрение структурированных логов.
- Модуль `permissions` не интегрирован через отдельный адаптер. Если появится необходимость в централизованной проверке, добавь интеграцию и опиши в ADR.
- Для отслеживания разрешений необходимо завести `Docs/PERMISSIONS_REPORT.md` и поддерживать его вручную.

---
Эти правила должны помогать сохранять архитектурную целостность и соответствовать текущему состоянию кодовой базы. Перед релизами проверяй, что документ остаётся актуальным: изменения в порядках инициализации, формате логов или конфигурации нужно отражать здесь в первую очередь.
