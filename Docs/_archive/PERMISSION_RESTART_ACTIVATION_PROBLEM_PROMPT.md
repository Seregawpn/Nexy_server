# ПРОМПТ ДЛЯ РЕШЕНИЯ ПРОБЛЕМЫ ПЕРЕЗАПУСКА И АКТИВАЦИИ ПРИЛОЖЕНИЯ

## КОНТЕКСТ ПРОБЛЕМЫ

В проекте **Nexy AI Assistant** обнаружены две критические проблемы, связанные с процессом запроса разрешений и перезапуском приложения:

### ПРОБЛЕМА 1: Приложение не перезапускается после предоставления разрешений
**Симптомы:**
- После завершения процедуры запроса разрешений при первом запуске приложение не перезапускается автоматически
- Пользователь остается в том же экземпляре приложения без перезапуска
- Система не переходит к нормальному режиму работы после получения разрешений
- В логах отсутствуют записи о планировании или выполнении перезапуска

**Ожидаемое поведение:**
- После выдачи всех критических разрешений приложение должно автоматически перезапуститься
- Перезапуск должен произойти через `PermissionRestartIntegration` и `RestartScheduler`
- После перезапуска приложение должно работать в нормальном режиме

### ПРОБЛЕМА 2: Ассистент активируется во время запроса разрешений
**Симптомы:**
- VoiceRecognitionIntegration может начать работу (переход в LISTENING режим) во время процесса запроса разрешений
- Приложение может активировать микрофон или другие функции до завершения first_run flow
- В логах видны события активации voice recognition до завершения `permissions.first_run_completed`

**Ожидаемое поведение:**
- Ассистент должен быть полностью заблокирован до завершения процедуры первого запуска
- Переход в LISTENING режим должен быть запрещён пока `permissions.first_run_completed` не опубликовано
- Все интеграции должны уважать флаг `permissions_in_progress` или состояние first_run

---

## ТРЕБОВАНИЯ К АНАЛИЗУ

**⚠️ КРИТИЧЕСКИ ВАЖНО:** Прежде чем предлагать решения, выполни **ПОЛНЫЙ ДИАГНОСТИЧЕСКИЙ АНАЛИЗ** согласно структуре ниже. Решения предлагаются ТОЛЬКО после того, как найден корень проблемы и проанализированы все затронутые компоненты.

---

## ЭТАП 1: АНАЛИЗ АРХИТЕКТУРЫ СИСТЕМЫ РАЗРЕШЕНИЙ И ПЕРЕЗАПУСКА

### 1.1 Изучение потока запроса разрешений

Проанализируй:

#### Порядок инициализации интеграций
**Файл**: `integration/core/simple_module_coordinator.py:492-512`

**Ключевые позиции:**
1. `instance_manager` (позиция 1) - блокирующий
2. `hardware_id` (позиция 2)
3. `first_run_permissions` (позиция 3) - **БЛОКИРУЮЩИЙ** - запрос разрешений при первом запуске
4. `permission_restart` (позиция 4) - автоматический перезапуск после выдачи критических разрешений
5. `voice_recognition` (позиция 8) - распознавание речи

**Критический код**: `simple_module_coordinator.py:526-530`
```python
if name == "first_run_permissions" and success:
    print("⏳ Ожидание завершения запроса разрешений...")
    await self._wait_for_permissions_completion()
    print("✅ Запрос разрешений завершен, продолжаем запуск...")
```

**Вопросы для анализа:**
- [ ] Как работает `_wait_for_permissions_completion()`? Он действительно ждет завершения или просто проверяет флаг?
- [ ] Блокирует ли он запуск остальных интеграций (включая voice_recognition)?
- [ ] Что происходит если `first_run_permissions` завершается быстро, но `permissions.first_run_completed` публикуется позже?

#### Процесс запроса разрешений
**Файл**: `integration/integrations/first_run_permissions_integration.py`

**Ключевой поток**:
1. Проверка флага `permissions_first_run_completed.flag` (строка 110)
2. Если флага нет → первый запуск
3. Публикация `permissions.first_run_started` (строка 119)
4. Запрос разрешений последовательно: Microphone → Accessibility → Input Monitoring → Screen Capture
5. Сохранение флага (строка 133)
6. Публикация `permissions.first_run_completed` (строка 139)
7. Установка `_permissions_in_progress = False` (строка 280)

**Вопросы для анализа:**
- [ ] Когда именно публикуется `permissions.first_run_completed`? Сразу после запроса или после паузы?
- [ ] Есть ли задержка между завершением запроса и публикацией события?
- [ ] Может ли `_permissions_in_progress` стать False до публикации события?

### 1.2 Изучение механизма перезапуска

Проанализируй:

#### PermissionRestartIntegration
**Файл**: `integration/integrations/permission_restart_integration.py`

**Подписки на события**:
- `permissions.changed` (строка 109) - изменения разрешений
- `permissions.status_checked` (строка 110) - проверка статуса
- `permissions.first_run_completed` (строка 111) - **КЛЮЧЕВОЕ** событие завершения первого запуска
- `updater.update_started` (строка 112)
- `updater.update_completed` (строка 113)

**Обработчик first_run_completed**: `permission_restart_integration.py:164-204`

```python
async def _on_first_run_completed(self, event: Dict[str, Any]) -> None:
    # Планируем перезапуск для критических разрешений
    # Создаём синтетические transition события
    for perm in (PermissionType.ACCESSIBILITY, PermissionType.INPUT_MONITORING):
        payload = {
            "permission": perm.value,
            "old_status": PermissionStatus.NOT_DETERMINED.value,
            "new_status": PermissionStatus.GRANTED.value,
            ...
        }
        transitions = self._detector.process_event("permissions.synthetic", payload)
        for transition in transitions:
            await self._handle_transition(transition)
```

**Вопросы для анализа:**
- [ ] Почему создаются синтетические события вместо проверки реального статуса разрешений?
- [ ] Может ли `_handle_transition()` не вызвать `scheduler.maybe_schedule_restart()`?
- [ ] Есть ли условия, при которых событие `permissions.first_run_completed` не обрабатывается?

#### RestartScheduler
**Файл**: `modules/permission_restart/core/restart_scheduler.py`

**Ключевой метод**: `maybe_schedule_restart()` (строка 64)

**Условия блокировки перезапуска**:
1. `_config.enabled == False` (строка 69) → немедленный отказ
2. `_attempts >= max_restart_attempts` (строка 74) → немедленный отказ
3. Если перезапуск уже запланирован → обновление метаданных (строка 89)

**Метод выполнения**: `_run_when_safe()` (строка 125)

**Условия ожидания** (до 10 минут):
1. `respect_updates && _is_update_in_progress()` (строка 140) → ждёт завершения обновления
2. `respect_active_sessions && !_is_idle_mode()` (строка 144) → **КРИТИЧЕСКОЕ** - ждёт режима SLEEPING

**Метод проверки режима**: `_is_idle_mode()` (строка 224)
```python
def _is_idle_mode(self) -> bool:
    current_mode = self._state_manager.get_current_mode()
    return current_mode == AppMode.SLEEPING  # ← Только SLEEPING = idle
```

**Вопросы для анализа:**
- [ ] Какой режим приложения после завершения first_run? Может быть не SLEEPING?
- [ ] Может ли приложение быть в LISTENING или PROCESSING режиме после first_run?
- [ ] Что происходит если режим не становится SLEEPING в течение 10 минут?
- [ ] Есть ли логи о планировании перезапуска в `permission_restart_integration.py`?

#### PermissionsRestartHandler
**Файл**: `modules/permission_restart/macos/permissions_restart_handler.py`

**Метод перезапуска**: `trigger_restart()` (строка 36)

**Проверки**:
- `_dry_run == True` (строка 39) → пропуск перезапуска
- Переменная окружения `NEXY_DISABLE_AUTO_RESTART` (строка 31)

**Выполнение**: `_perform_restart()` (строка 57)
- Production: `open -a Nexy.app` + `os._exit(0)` (строка 84-86)
- Development: `subprocess.Popen([python_executable] + argv)` + `os._exit(0)` (строка 112)

**Вопросы для анализа:**
- [ ] Может ли `trigger_restart()` быть вызван, но перезапуск не выполниться?
- [ ] Есть ли ошибки в `_launch_packaged_app()` или `_launch_dev_process()`?
- [ ] Вызывается ли `os._exit(0)` гарантированно?

### 1.3 Изучение механизма блокировки активации ассистента

Проанализируй:

#### VoiceRecognitionIntegration
**Файл**: `integration/integrations/voice_recognition_integration.py`

**Подписки на события**:
- `voice.recording_start` (строка 132)
- `voice.recording_stop` (строка 133)
- `keyboard.short_press` (строка 134)
- `app.mode_changed` (строка 137) - **КРИТИЧЕСКОЕ** для защиты

**Обработчик mode_changed**: `voice_recognition_integration.py:371-387`
```python
async def _on_app_mode_changed(self, event: Dict[str, Any]):
    new_mode = data.get("mode")
    if new_mode in (AppMode.SLEEPING, AppMode.PROCESSING):
        await self._cancel_recognition(reason="mode_changed")
```

**Вопросы для анализа:**
- [ ] Есть ли проверка `permissions_in_progress` или `first_run` состояния перед активацией?
- [ ] Может ли `voice.recording_start` быть вызван во время first_run?
- [ ] Защищает ли `app.mode_changed` от активации во время first_run?

#### Gateways и Selectors
**Файл**: `integration/core/gateways.py`

**Метод принятия решений**: `decide_start_listening()` (строка 39)

**Проверяемые оси состояния**:
- `perm_mic` - разрешение микрофона
- `device_input` - состояние устройства
- `network` - состояние сети
- `firstRun` - **КРИТИЧЕСКОЕ** - флаг первого запуска
- `appMode` - режим приложения

**Вопросы для анализа:**
- [ ] Есть ли проверка `firstRun == true` в `decide_start_listening()`?
- [ ] Блокируется ли переход в LISTENING если `firstRun == true`?
- [ ] Как определяется `firstRun` в `Snapshot`?

**Файл**: `integration/core/selectors.py`

**Вопросы для анализа:**
- [ ] Как создаётся `Snapshot`? Где берётся информация о `firstRun`?
- [ ] Обновляется ли `firstRun` в реальном времени или только при старте?

#### ModeManagementIntegration
**Файл**: `integration/integrations/mode_management_integration.py`

**Вопросы для анализа:**
- [ ] Как происходит переход в LISTENING режим?
- [ ] Есть ли проверка `permissions_in_progress` перед переходом?
- [ ] Какие события триггерят переход в LISTENING?

---

## ЭТАП 2: АНАЛИЗ ЛОГОВ И СОБЫТИЙ

### 2.1 Анализ предоставленного log.md

**Файл**: `log.md`

**Ключевые временные метки для анализа:**

**11:17:19** - Запуск приложения
```
default  11:17:19.010221-0400  runningboardd  Launch request for app<application.com.nexy.assistant
```

**11:17:22-24** - Запрос разрешения микрофона
```
default  11:17:22.811098-0400  tccd  AUTHREQ_PROMPTING: msgID=401.5681, service=kTCCServiceMicrophone
default  11:17:24.208461-0400  tccd  Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone
```

**11:17:24** - Начало записи аудио (ПРОБЛЕМА!)
```
default  11:17:24.380862-0400  Nexy  SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input
default  11:17:24.419744-0400  audiomxd  -[MXCoreSession updateIsRecording:]: MXCoreSession starting recording
```

**11:17:25** - Остановка записи
```
default  11:17:25.622782-0400  Nexy  SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input
```

**11:17:39** - Запрос разрешений Screen Capture и Accessibility
```
default  11:17:39.878887-0400  tccd  Notifying for access  kTCCServiceScreenCapture
default  11:17:53.089322-0400  tccd  attempted to call TCCAccessRequest for kTCCServiceAccessibility
default  11:17:53.139107-0400  tccd  Notifying for access  kTCCServiceListenEvent
```

**Вопросы для анализа:**
- [ ] Видны ли в логах события `permissions.first_run_started` и `permissions.first_run_completed`?
- [ ] Видны ли в логах события `permission_restart.scheduled` и `permission_restart.executing`?
- [ ] Почему аудио запись начинается в 11:17:24, хотя запрос разрешений ещё идёт?
- [ ] Когда именно завершается first_run flow? Видно ли это в логах?

### 2.2 Поиск отсутствующих событий в логах

**Проверь наличие в логах:**
- [ ] `[FIRST_RUN_PERMISSIONS] Первый запуск обнаружен`
- [ ] `[FIRST_RUN_PERMISSIONS] Первый запуск завершён`
- [ ] `permissions.first_run_started` (публикация события)
- [ ] `permissions.first_run_completed` (публикация события)
- [ ] `[PERMISSION_RESTART] First run completed, scheduling restart`
- [ ] `[PERMISSION_RESTART] Scheduling application restart`
- [ ] `[PERMISSION_RESTART] Restart scheduled`
- [ ] `[PERMISSION_RESTART] Restart requested`
- [ ] `[PERMISSION_RESTART] Relaunching packaged app`
- [ ] `permission_restart.scheduled` (публикация события)
- [ ] `permission_restart.executing` (публикация события)

**Если событий нет - почему?**
- [ ] Может быть интеграция не инициализирована?
- [ ] Может быть подписка не работает?
- [ ] Может быть событие не публикуется?
- [ ] Может быть обработчик не вызывается?

---

## ЭТАП 3: ОПРЕДЕЛЕНИЕ КОРНЕВОЙ ПРИЧИНЫ

### 3.1 Гипотезы для Проблемы 1 (Не перезапускается)

**Гипотеза 1.1: Событие `permissions.first_run_completed` не публикуется**
- Проверь: публикуется ли событие в `first_run_permissions_integration.py:139`?
- Может быть: исключение до публикации события?
- Решение: убедиться что событие публикуется всегда, даже при ошибках

**Гипотеза 1.2: Событие не доходит до `PermissionRestartIntegration`**
- Проверь: подписан ли обработчик `_on_first_run_completed` на событие?
- Может быть: порядок инициализации - интеграция ещё не подписана?
- Решение: проверить порядок инициализации и подписок

**Гипотеза 1.3: `RestartScheduler` блокируется условиями**
- Проверь: режим приложения после first_run - SLEEPING или нет?
- Может быть: приложение остаётся в активном режиме и ждёт SLEEPING?
- Решение: изменить логику ожидания или форсировать SLEEPING после first_run

**Гипотеза 1.4: Перезапуск запланирован, но не выполняется**
- Проверь: вызывается ли `trigger_restart()` в `RestartScheduler`?
- Может быть: `_dry_run == True` или `NEXY_DISABLE_AUTO_RESTART` установлен?
- Решение: проверить флаги и переменные окружения

**Гипотеза 1.5: Ошибка при выполнении перезапуска**
- Проверь: есть ли ошибки в `_perform_restart()`?
- Может быть: `open -a Nexy.app` не работает или `os._exit(0)` не вызывается?
- Решение: добавить логирование и обработку ошибок

### 3.2 Гипотезы для Проблемы 2 (Активация во время запроса)

**Гипотеза 2.1: VoiceRecognitionIntegration запускается до завершения first_run**
- Проверь: блокирует ли `_wait_for_permissions_completion()` запуск voice_recognition?
- Может быть: ожидание завершается до публикации `permissions.first_run_completed`?
- Решение: убедиться что voice_recognition запускается только после завершения first_run

**Гипотеза 2.2: Переход в LISTENING режим происходит независимо от first_run**
- Проверь: проверяет ли `decide_start_listening()` флаг `firstRun`?
- Может быть: переход в LISTENING происходит через другой механизм?
- Решение: добавить проверку `firstRun` в gateways и блокировать переход

**Гипотеза 2.3: Флаг `permissions_in_progress` не проверяется**
- Проверь: используется ли `permissions_in_progress` в `VoiceRecognitionIntegration`?
- Может быть: интеграция не знает о состоянии first_run?
- Решение: подписаться на `permissions.first_run_started/completed` и блокировать активацию

**Гипотеза 2.4: События активации публикуются до завершения first_run**
- Проверь: кто публикует `voice.recording_start` во время first_run?
- Может быть: другой компонент триггерит активацию?
- Решение: найти источник активации и добавить проверку

---

## ЭТАП 4: РЕШЕНИЕ ПРОБЛЕМ

### 4.1 Требования к решению

**Архитектурные принципы** (см. `.cursorrules` раздел 17):
- ✅ Соблюдать разделение ответственности (Separation of Concerns)
- ✅ Использовать EventBus для всех коммуникаций
- ✅ Не нарушать изоляцию модулей
- ✅ Следовать паттерну интеграций (BaseIntegration)
- ✅ Использовать selectors/gateways для проверки состояний
- ✅ Сохранять порядок инициализации компонентов

**Требования к коду** (см. `.cursorrules` раздел 11):
- ✅ Валидация payload на границе интеграции
- ✅ Обработка ошибок через ErrorHandler
- ✅ Логирование с session_id
- ✅ Структурированные события EventBus
- ✅ Обратная совместимость

**Требования к тестированию** (см. `.cursorrules` раздел 10):
- ✅ Модульные тесты для core логики
- ✅ Contract тесты для EventBus событий
- ✅ Интеграционные тесты для полного flow
- ✅ Ручные проверки критических сценариев

### 4.2 Дизайн решения

**Компоненты затронутые решением:**

1. **FirstRunPermissionsIntegration**
   - Обеспечить гарантированную публикацию `permissions.first_run_completed`
   - Добавить явную установку состояния `permissions_in_progress = False` после публикации

2. **PermissionRestartIntegration**
   - Проверить обработку события `permissions.first_run_completed`
   - Убедиться что `RestartScheduler` действительно планирует перезапуск
   - Добавить fallback механизм если перезапуск не планируется

3. **RestartScheduler**
   - Проверить логику ожидания режима SLEEPING
   - Добавить возможность форсировать перезапуск после first_run
   - Улучшить логирование для диагностики

4. **VoiceRecognitionIntegration**
   - Добавить проверку состояния first_run перед активацией
   - Подписаться на `permissions.first_run_started/completed` для блокировки
   - Блокировать активацию если `permissions_in_progress == True`

5. **Gateways/Selectors**
   - Добавить проверку `firstRun` в `decide_start_listening()`
   - Обновить `Snapshot` для включения состояния first_run
   - Добавить правило в `interaction_matrix.yaml` если нужно

6. **ModeManagementIntegration**
   - Добавить проверку `permissions_in_progress` перед переходом в LISTENING
   - Блокировать переход если first_run не завершён

### 4.3 План реализации

**Шаг 1: Диагностика и логирование**
- [ ] Добавить детальное логирование в `first_run_permissions_integration.py`
- [ ] Добавить логирование в `permission_restart_integration.py` для отслеживания событий
- [ ] Добавить логирование в `restart_scheduler.py` для отслеживания условий ожидания
- [ ] Проверить наличие всех событий в логах при тестовом запуске

**Шаг 2: Исправление перезапуска**
- [ ] Убедиться что `permissions.first_run_completed` публикуется всегда
- [ ] Проверить обработку события в `PermissionRestartIntegration`
- [ ] Исправить логику ожидания режима SLEEPING (возможно добавить форсирование)
- [ ] Добавить fallback механизм если перезапуск не выполняется в течение N минут

**Шаг 3: Блокировка активации во время first_run**
- [ ] Добавить проверку `permissions_in_progress` в `VoiceRecognitionIntegration`
- [ ] Обновить `decide_start_listening()` для проверки `firstRun`
- [ ] Добавить блокировку в `ModeManagementIntegration`
- [ ] Обновить `Snapshot` для включения состояния first_run

**Шаг 4: Тестирование**
- [ ] Unit тесты для исправленной логики
- [ ] Integration тесты для полного flow
- [ ] Ручная проверка: первый запуск → запрос разрешений → перезапуск
- [ ] Ручная проверка: блокировка активации во время first_run

---

## ЭТАП 5: КОНТРОЛЬНЫЙ СПИСОК ПЕРЕД РЕАЛИЗАЦИЕЙ

### 5.1 Понимание проблемы
- [ ] Корневая причина Проблемы 1 определена
- [ ] Корневая причина Проблемы 2 определена
- [ ] Все затронутые компоненты идентифицированы
- [ ] Поток событий прослежен полностью
- [ ] Логи проанализированы и отсутствующие события найдены

### 5.2 Дизайн решения
- [ ] Решение не нарушает архитектурные принципы
- [ ] Все затронутые компоненты учтены
- [ ] Риски идентифицированы и минимизированы
- [ ] Обратная совместимость обеспечена
- [ ] План тестирования создан

### 5.3 Реализация
- [ ] Изменения минимальны и сфокусированы
- [ ] Логирование добавлено для диагностики
- [ ] Обработка ошибок улучшена
- [ ] Тесты добавлены/обновлены
- [ ] Документация обновлена (если нужно)

---

## КЛЮЧЕВЫЕ ФАЙЛЫ ДЛЯ АНАЛИЗА

### Основные компоненты
1. `integration/integrations/first_run_permissions_integration.py` - Запрос разрешений
2. `integration/integrations/permission_restart_integration.py` - Перезапуск после разрешений
3. `modules/permission_restart/core/restart_scheduler.py` - Планирование перезапуска
4. `modules/permission_restart/macos/permissions_restart_handler.py` - Выполнение перезапуска
5. `integration/integrations/voice_recognition_integration.py` - Распознавание речи
6. `integration/core/gateways.py` - Принятие решений о запуске
7. `integration/core/selectors.py` - Проверка состояний
8. `integration/integrations/mode_management_integration.py` - Управление режимами
9. `integration/core/simple_module_coordinator.py` - Координатор интеграций

### Конфигурация
1. `config/unified_config.yaml` - Основная конфигурация
2. `config/interaction_matrix.yaml` - Матрица взаимодействий

### Документация
1. `Docs/PERMISSION_RESTART_LOGIC.md` - Логика перезапуска
2. `Docs/PERMISSION_RESTART_BLOCKERS.md` - Условия блокировки
3. `Docs/PERMISSION_RESTART_KEY_POINTS.md` - Ключевые моменты
4. `.cursorrules` - Правила разработки

---

## ИНСТРУКЦИИ ПО РАБОТЕ

### Обязательно выполнить:
1. ✅ Прочитать и понять архитектуру системы разрешений (раздел 1)
2. ✅ Проанализировать логи и найти отсутствующие события (раздел 2)
3. ✅ Определить корневую причину каждой проблемы (раздел 3)
4. ✅ Спроектировать решение с учётом всех компонентов (раздел 4)
5. ✅ Создать детальный план реализации с чек-листами (раздел 4.3)
6. ✅ Пройти контрольный список перед реализацией (раздел 5)

### После решения проблемы:
- Обновить `Docs/CURRENT_STATUS_REPORT.md` с описанием исправления
- Обновить `Docs/PERMISSION_RESTART_BLOCKERS.md` если обнаружены новые условия блокировки
- Добавить тесты в `tests/` для предотвращения регрессии
- Проверить что логи теперь содержат все необходимые события

---

## ФОРМАТ ОТЧЕТА

После анализа и решения, предоставь:

1. **Отчет об анализе** - найденные корневые причины, прослеженные потоки событий, идентифицированные компоненты
2. **Дизайн решения** - описание изменений, диаграммы потоков (если нужно), обоснование выбора
3. **План реализации** - пошаговый план с чек-листами, оценка сложности, риски
4. **Код изменений** - конкретные изменения в файлах с комментариями
5. **План тестирования** - какие тесты добавить, какие сценарии проверить вручную

---

**ВАЖНО:** Не предлагай решения до завершения полного анализа. Все гипотезы должны быть проверены через анализ кода и логов.

