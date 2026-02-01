# 🚀 Поэтапный План Реализации Инициализации

**Дата:** 2025-12-13  
**Статус:** Детальный поэтапный план реализации с фазами, проверками и критериями готовности

---

## 📊 Часть 1: Принципы Реализации

### 1.1 Принципы поэтапной реализации

**Ключевые принципы:**
1. ✅ **Постепенная миграция:** Каждая фаза добавляет функциональность без ломания существующей
2. ✅ **Изолированное тестирование:** После каждой фазы создаются изолированные тесты
3. ✅ **Обратная совместимость:** Старая реализация работает параллельно с новой
4. ✅ **Проверка на каждом этапе:** Каждая фаза имеет четкие критерии готовности
5. ✅ **Откат:** Возможность отката на любом этапе

---

### 1.2 Последовательность фаз

**Фазы реализации:**
1. **Фаза 0: Подготовка и анализ** — проверка текущего состояния
2. **Фаза 1: Конфигурация** — создание конфигурации инициализаций
3. **Фаза 2: InitializationManager (базовая версия)** — создание менеджера без интеграции
4. **Фаза 3: Интеграция InitializationManager** — подключение к SimpleModuleCoordinator
5. **Фаза 4: Миграция создания интеграций** — упрощение `_create_integrations()`
6. **Фаза 5: Миграция инициализации** — замена `_initialize_integrations()` на `InitializationManager`
7. **Фаза 6: Удаление старого кода** — удаление неиспользуемого кода
8. **Фаза 7: Финальная проверка** — полное тестирование и валидация

---

## 📊 Часть 2: Фаза 0 - Подготовка и Анализ

### 2.1 Цель фазы

**Цель:** Убедиться, что текущая реализация работает корректно и мы понимаем все зависимости

**Критерии готовности:**
- [ ] Текущая инициализация работает без ошибок
- [ ] Все существующие тесты проходят
- [ ] Задокументированы все зависимости
- [ ] Задокументирован порядок инициализации

---

### 2.2 Задачи

**Задача 1: Проверка текущего состояния**
```bash
# Запустить все существующие тесты
pytest tests/ -v

# Запустить приложение и проверить инициализацию
python main.py
```

**Задача 2: Документирование зависимостей**
- [ ] Создать список всех интеграций с их зависимостями
- [ ] Задокументировать специальную обработку (AVF engine, критичные подписки)
- [ ] Задокументировать условную инициализацию (tray, action_execution)

**Задача 3: Создание baseline тестов**
- [ ] Создать тест текущей инициализации (baseline)
- [ ] Зафиксировать порядок инициализации
- [ ] Зафиксировать время выполнения

**Выходные артефакты:**
- `tests/test_initialization_baseline.py` — baseline тест
- `Docs/INITIALIZATION_DEPENDENCIES.md` — документ с зависимостями

---

### 2.3 Чек-лист фазы 0

- [ ] Все существующие тесты проходят
- [ ] Приложение запускается и инициализируется корректно
- [ ] Задокументированы все зависимости
- [ ] Создан baseline тест
- [ ] Зафиксирован порядок инициализации

**Время:** 2-3 часа

---

## 📊 Часть 3: Фаза 1 - Конфигурация

### 3.1 Цель фазы

**Цель:** Создать конфигурацию инициализаций в `unified_config.yaml` и загрузчик конфигурации

**Критерии готовности:**
- [ ] Секция `initialization` добавлена в `unified_config.yaml`
- [ ] `initialization_config.py` создан и работает
- [ ] Конфигурация валидируется корректно
- [ ] Тесты конфигурации проходят

---

### 3.2 Задачи

**Задача 1: Добавить секцию initialization в unified_config.yaml**

**Файл:** `config/unified_config.yaml`

**Место вставки:** В конец файла (после всех существующих секций)

**Содержимое:**
```yaml
# Централизованная конфигурация инициализаций
initialization:
  order: auto  # auto|manual - автоматический или ручной порядок
  
  steps:
    # Core компоненты (создаются автоматически)
    core_components:
      description: "Создание core компонентов (EventBus, StateManager, ErrorHandler)"
      type: internal
      dependencies: []
      critical: true
      timeout_sec: 5.0
      enabled: true
    
    # Instance Manager (первый, блокирующий)
    instance_manager:
      description: "Инициализация InstanceManager (проверка единственного экземпляра)"
      type: integration
      integration_name: instance_manager
      dependencies: [core_components]
      critical: true
      timeout_sec: 10.0
      enabled: true
      config_source: instance_manager
    
    # Hardware ID
    hardware_id:
      description: "Инициализация HardwareId (идентификация устройства)"
      type: integration
      integration_name: hardware_id
      dependencies: [instance_manager]
      critical: true
      timeout_sec: 5.0
      enabled: true
      config_source: integrations.hardware_id
    
    # First Run Permissions (блокирующая)
    first_run_permissions:
      description: "Инициализация FirstRunPermissions (запрос разрешений при первом запуске)"
      type: integration
      integration_name: first_run_permissions
      dependencies: [hardware_id]
      critical: true
      timeout_sec: 60.0  # Может занять время (диалоги разрешений)
      enabled: true
      config_source: permissions.first_run
    
    # Permission Restart
    permission_restart:
      description: "Инициализация PermissionRestart (автоматический перезапуск после разрешений)"
      type: integration
      integration_name: permission_restart
      dependencies: [first_run_permissions]
      critical: false  # Не критично, если не работает
      timeout_sec: 10.0
      enabled: true
      config_source: integrations.permission_restart
    
    # Tray Controller
    tray_controller:
      description: "Инициализация TrayController (системный трей)"
      type: integration
      integration_name: tray
      dependencies: [permission_restart]
      critical: true
      timeout_sec: 10.0
      enabled: true  # Условно: проверяется integrations.tray_controller.enabled
      config_source: integrations.tray_controller
      conditional:
        config_check: integrations.tray_controller.enabled
    
    # Mode Management
    mode_management:
      description: "Инициализация ModeManagement (управление режимами приложения)"
      type: integration
      integration_name: mode_management
      dependencies: [tray_controller]
      critical: true
      timeout_sec: 5.0
      enabled: true
      config_source: integrations.mode_management
    
    # Input Processing
    input_processing:
      description: "Инициализация InputProcessing (обработка клавиатуры)"
      type: integration
      integration_name: input
      dependencies: [mode_management]
      critical: true
      timeout_sec: 10.0
      enabled: true
      config_source: integrations.input_processing
    
    # Voice Recognition (⚠️ ПРОБЛЕМА С AVF)
    voice_recognition:
      description: "Инициализация VoiceRecognition (распознавание речи, AVF, Google)"
      type: integration
      integration_name: voice_recognition
      dependencies: [input_processing]
      critical: true
      timeout_sec: 45.0  # Может занять время (AVF инициализация)
      enabled: true
      config_source: integrations.voice_recognition
      # Специальные параметры для диагностики
      diagnostics:
        log_avf_init: true
        log_google_init: true
        validate_avf_engine: true
    
    # Network Manager
    network_manager:
      description: "Инициализация NetworkManager (мониторинг сети)"
      type: integration
      integration_name: network
      dependencies: [voice_recognition]
      critical: false
      timeout_sec: 10.0
      enabled: true
      config_source: integrations.network_manager
    
    # Interrupt Management
    interrupt_management:
      description: "Инициализация InterruptManagement (прерывание воспроизведения)"
      type: integration
      integration_name: interrupt
      dependencies: [network_manager]
      critical: true
      timeout_sec: 5.0
      enabled: true
      config_source: integrations.interrupt_management
    
    # Screenshot Capture
    screenshot_capture:
      description: "Инициализация ScreenshotCapture (захват экрана)"
      type: integration
      integration_name: screenshot_capture
      dependencies: [interrupt_management]
      critical: true
      timeout_sec: 10.0
      enabled: true
      config_source: integrations.screenshot_capture
    
    # gRPC Client
    grpc_client:
      description: "Инициализация GrpcClient (соединение с сервером)"
      type: integration
      integration_name: grpc
      dependencies: [screenshot_capture]
      critical: true
      timeout_sec: 30.0
      enabled: true
      config_source: grpc
    
    # Speech Playback
    speech_playback:
      description: "Инициализация SpeechPlayback (воспроизведение речи)"
      type: integration
      integration_name: speech_playback
      dependencies: [grpc_client]
      critical: true
      timeout_sec: 10.0
      enabled: true
      config_source: integrations.speech_playback
      # Специальная обработка: получает AVF engine из voice_recognition
      special_params:
        avf_engine_source: voice_recognition
    
    # Signal Integration
    signal_integration:
      description: "Инициализация SignalIntegration (обработка сигналов)"
      type: integration
      integration_name: signals
      dependencies: [speech_playback]
      critical: false
      timeout_sec: 5.0
      enabled: true
      config_source: integrations.signals
    
    # Updater
    updater:
      description: "Инициализация Updater (автоматические обновления)"
      type: integration
      integration_name: updater
      dependencies: [signal_integration]
      critical: false
      timeout_sec: 10.0
      enabled: true
      config_source: updater
    
    # Autostart Manager
    autostart_manager:
      description: "Инициализация AutostartManager (автозапуск)"
      type: integration
      integration_name: autostart_manager
      dependencies: [updater]
      critical: false
      timeout_sec: 5.0
      enabled: true
      config_source: autostart
    
    # Welcome Message
    welcome_message:
      description: "Инициализация WelcomeMessage (приветственное сообщение)"
      type: integration
      integration_name: welcome_message
      dependencies: [autostart_manager]
      critical: false
      timeout_sec: 5.0
      enabled: true
      config_source: integrations.welcome_message
    
    # VoiceOver Ducking
    voiceover_ducking:
      description: "Инициализация VoiceOverDucking (снижение громкости VoiceOver)"
      type: integration
      integration_name: voiceover_ducking
      dependencies: [welcome_message]
      critical: false
      timeout_sec: 5.0
      enabled: true
      config_source: accessibility.voiceover_control
    
    # Action Execution
    action_execution:
      description: "Инициализация ActionExecution (выполнение действий)"
      type: integration
      integration_name: action_execution
      dependencies: [voiceover_ducking]
      critical: false
      timeout_sec: 5.0
      enabled: true
      config_source: actions.open_app
      # Условная инициализация (только в dev или если enabled)
      conditional:
        env_check: development
        config_check: enabled
    
    # Update Notification
    update_notification:
      description: "Инициализация UpdateNotification (уведомления об обновлениях)"
      type: integration
      integration_name: update_notification
      dependencies: [action_execution]
      critical: false
      timeout_sec: 5.0
      enabled: true
      config_source: integrations.update_notification
    
    # Workflows (инициализируются после всех интеграций)
    workflows:
      description: "Инициализация Workflows (координаторы режимов)"
      type: workflow
      dependencies: [update_notification]
      critical: true
      timeout_sec: 5.0
      enabled: true
      workflows:
        - listening
        - processing
```

**Проверка:**
```bash
# Проверить синтаксис YAML
python -c "import yaml; yaml.safe_load(open('config/unified_config.yaml'))"
```

---

**Задача 2: Создать initialization_config.py**

**Файл:** `config/initialization_config.py`

**Содержимое:** (см. `INITIALIZATION_STRUCTURE_ANALYSIS.md` раздел 2.4)

**Проверка:**
```python
# Тест загрузки конфигурации
from config.initialization_config import load_initialization_config
from config.unified_config_loader import UnifiedConfigLoader

loader = UnifiedConfigLoader()
config = load_initialization_config(loader)
print(f"Загружено шагов: {len(config.steps)}")
```

---

**Задача 3: Обновить unified_config_loader.py**

**Файл:** `config/unified_config_loader.py`

**Добавить метод:**
```python
def get_initialization_config(self) -> Dict[str, Any]:
    """Загрузка конфигурации инициализаций"""
    config_data = self._load_config()
    return config_data.get("initialization", {})
```

**Место вставки:** После существующих методов `get_*_config()`

---

**Задача 4: Создать тесты конфигурации**

**Файл:** `tests/test_initialization_config.py`

**Тесты:**
1. Тест загрузки конфигурации
2. Тест валидации зависимостей
3. Тест обнаружения циклических зависимостей
4. Тест топологической сортировки

**Проверка:**
```bash
pytest tests/test_initialization_config.py -v
```

---

### 3.3 Чек-лист фазы 1

- [ ] Секция `initialization` добавлена в `unified_config.yaml`
- [ ] `initialization_config.py` создан
- [ ] Метод `get_initialization_config()` добавлен
- [ ] Конфигурация загружается без ошибок
- [ ] Валидация зависимостей работает
- [ ] Тесты конфигурации проходят (100%)
- [ ] Все существующие тесты все еще проходят

**Время:** 4-6 часов

---

## 📊 Часть 4: Фаза 2 - InitializationManager (Базовая Версия)

### 4.1 Цель фазы

**Цель:** Создать `InitializationManager` с базовой функциональностью (без интеграции в SimpleModuleCoordinator)

**Критерии готовности:**
- [ ] `InitializationManager` создан и работает изолированно
- [ ] Может регистрировать шаги
- [ ] Может выполнять инициализации в правильном порядке
- [ ] Тесты менеджера проходят

---

### 4.2 Задачи

**Задача 1: Создать initialization_manager.py**

**Файл:** `integration/core/initialization_manager.py`

**Содержимое:** (см. `INITIALIZATION_CENTRALIZATION_PROPOSAL.md` раздел 2.2)

**Ключевые компоненты:**
1. `InitializationStatus` enum
2. `InitializationStep` dataclass
3. `InitializationManager` class:
   - `register_step()`
   - `_calculate_execution_order()`
   - `initialize_all()`
   - `_execute_step()`
   - `_generate_report()`
   - `get_status()`

**Проверка:**
```python
# Изолированный тест
from integration.core.initialization_manager import InitializationManager
from unittest.mock import Mock

event_bus = Mock()
state_manager = Mock()
error_handler = Mock()
config_loader = Mock()

manager = InitializationManager(event_bus, state_manager, error_handler, config_loader)

# Регистрация шага
async def test_init():
    return True

manager.register_step(
    name="test",
    description="Test step",
    init_func=test_init,
    dependencies=[],
    critical=True
)

# Выполнение
success = await manager.initialize_all()
assert success == True
```

---

**Задача 2: Интеграция с конфигурацией**

**Обновить `InitializationManager.__init__()`:**
```python
def __init__(self, event_bus, state_manager, error_handler, config_loader):
    self.event_bus = event_bus
    self.state_manager = state_manager
    self.error_handler = error_handler
    
    # Загружаем конфигурацию инициализаций
    self.init_config = load_initialization_config(config_loader)
    
    # Реестр шагов
    self.steps: Dict[str, InitializationStep] = {}
    self.execution_order: List[str] = []
    self.results: Dict[str, Any] = {}
```

---

**Задача 3: Создать тесты менеджера**

**Файл:** `tests/test_initialization_manager.py`

**Тесты:**
1. Тест регистрации шагов
2. Тест топологической сортировки
3. Тест выполнения шагов
4. Тест обработки ошибок
5. Тест таймаутов
6. Тест критичных/некритичных шагов
7. Тест циклических зависимостей

**Проверка:**
```bash
pytest tests/test_initialization_manager.py -v
```

---

### 4.3 Чек-лист фазы 2

- [ ] `InitializationManager` создан
- [ ] Может регистрировать шаги
- [ ] Может вычислять порядок выполнения
- [ ] Может выполнять инициализации
- [ ] Обрабатывает ошибки корректно
- [ ] Тесты менеджера проходят (100%)
- [ ] Все существующие тесты все еще проходят

**Время:** 6-8 часов

---

## 📊 Часть 5: Фаза 3 - Интеграция InitializationManager

### 5.1 Цель фазы

**Цель:** Интегрировать `InitializationManager` в `SimpleModuleCoordinator` параллельно со старой реализацией

**Критерии готовности:**
- [ ] `InitializationManager` используется в `SimpleModuleCoordinator`
- [ ] Старая реализация все еще работает
- [ ] Можно переключаться между старой и новой реализацией через флаг
- [ ] Тесты координатора проходят

---

### 5.2 Задачи

**Задача 1: Добавить InitializationManager в SimpleModuleCoordinator**

**Файл:** `integration/core/simple_module_coordinator.py`

**Добавить импорт:**
```python
from integration.core.initialization_manager import InitializationManager
```

**Добавить поле:**
```python
def __init__(self):
    # ... существующий код ...
    self.init_manager: Optional[InitializationManager] = None
    self._use_new_initialization: bool = False  # Флаг для переключения
```

**Добавить метод для создания менеджера:**
```python
def _create_initialization_manager(self):
    """Создание менеджера инициализации"""
    if self._use_new_initialization:
        self.init_manager = InitializationManager(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config_loader=self.config
        )
        logger.info("✅ [COORDINATOR] InitializationManager создан")
```

---

**Задача 2: Добавить флаг для переключения**

**Файл:** `config/unified_config.yaml`

**Добавить:**
```yaml
app:
  # ... существующие настройки ...
  use_new_initialization: false  # Флаг для переключения на новую инициализацию
```

**В `SimpleModuleCoordinator.initialize()`:**
```python
# Проверяем флаг
config_data = self.config._load_config()
self._use_new_initialization = config_data.get('app', {}).get('use_new_initialization', False)

if self._use_new_initialization:
    logger.info("🔄 [COORDINATOR] Используется новая система инициализации")
    # Создаем менеджер
    self._create_initialization_manager()
else:
    logger.info("🔄 [COORDINATOR] Используется старая система инициализации")
```

---

**Задача 3: Создать тесты координатора**

**Файл:** `tests/test_coordinator_initialization.py`

**Тесты:**
1. Тест старой инициализации (флаг = false)
2. Тест новой инициализации (флаг = true)
3. Тест переключения между старой и новой
4. Тест порядка инициализации

**Проверка:**
```bash
pytest tests/test_coordinator_initialization.py -v
```

---

### 5.3 Чек-лист фазы 3

- [ ] `InitializationManager` интегрирован в `SimpleModuleCoordinator`
- [ ] Флаг переключения работает
- [ ] Старая реализация все еще работает
- [ ] Новая реализация работает (пока только создание менеджера)
- [ ] Тесты координатора проходят
- [ ] Все существующие тесты все еще проходят

**Время:** 4-6 часов

---

## 📊 Часть 6: Фаза 4 - Миграция Создания Интеграций

### 6.1 Цель фазы

**Цель:** Упростить `_create_integrations()` и использовать конфигурацию для определения порядка

**Критерии готовности:**
- [ ] `_create_integrations_simple()` создан
- [ ] Порядок создания не важен (порядок инициализации определяется конфигурацией)
- [ ] Все интеграции создаются корректно
- [ ] Тесты создания проходят

---

### 6.2 Задачи

**Задача 1: Создать _create_integrations_simple()**

**Файл:** `integration/core/simple_module_coordinator.py`

**Создать новый метод:**
```python
async def _create_integrations_simple(self):
    """Упрощенное создание интеграций (без жесткого порядка)"""
    config_data = self.config._load_config()
    
    # Создаем все интеграции (порядок не важен при создании)
    # Порядок инициализации определяется конфигурацией
    
    # Instance Manager (первый, блокирующий)
    instance_config = config_data.get('instance_manager', {})
    self.integrations['instance_manager'] = InstanceManagerIntegration(
        event_bus=self.event_bus,
        state_manager=self.state_manager,
        error_handler=self.error_handler,
        config=instance_config
    )
    
    # Hardware ID
    self.integrations['hardware_id'] = HardwareIdIntegration(
        event_bus=self.event_bus,
        state_manager=self.state_manager,
        error_handler=self.error_handler,
        config=None
    )
    
    # ... (все остальные интеграции, но БЕЗ жесткого порядка)
    # Порядок создания не важен, порядок инициализации определяется конфигурацией
    
    # Workflows
    self.workflows['listening'] = ListeningWorkflow(event_bus=self.event_bus)
    self.workflows['processing'] = ProcessingWorkflow(event_bus=self.event_bus)
```

**Важно:** Порядок создания не важен, так как порядок инициализации определяется конфигурацией

---

**Задача 2: Обновить initialize() для использования нового метода**

**Файл:** `integration/core/simple_module_coordinator.py`

**Обновить метод `initialize()`:**
```python
async def initialize(self) -> bool:
    """Инициализация всех компонентов"""
    try:
        # ... существующий код для core компонентов ...
        
        # Проверяем флаг
        config_data = self.config._load_config()
        self._use_new_initialization = config_data.get('app', {}).get('use_new_initialization', False)
        
        if self._use_new_initialization:
            # Новая система: используем упрощенное создание
            await self._create_integrations_simple()
        else:
            # Старая система: используем старый метод
            await self._create_integrations()
        
        # ... остальной код ...
```

---

**Задача 3: Создать тесты создания интеграций**

**Файл:** `tests/test_integration_creation.py`

**Тесты:**
1. Тест создания всех интеграций
2. Тест условного создания (tray, action_execution)
3. Тест зависимостей при создании (permission_restart → updater)

**Проверка:**
```bash
pytest tests/test_integration_creation.py -v
```

---

### 6.3 Чек-лист фазы 4

- [ ] `_create_integrations_simple()` создан
- [ ] Все интеграции создаются корректно
- [ ] Порядок создания не важен
- [ ] Условное создание работает (tray, action_execution)
- [ ] Тесты создания проходят
- [ ] Все существующие тесты все еще проходят

**Время:** 4-6 часов

---

## 📊 Часть 7: Фаза 5 - Миграция Инициализации

### 7.1 Цель фазы

**Цель:** Заменить `_initialize_integrations()` на использование `InitializationManager`

**Критерии готовности:**
- [ ] `InitializationManager` используется для инициализации
- [ ] Порядок инициализации соответствует конфигурации
- [ ] AVF engine передается в speech_playback
- [ ] Все интеграции инициализируются корректно
- [ ] Тесты инициализации проходят

---

### 7.2 Задачи

**Задача 1: Реализовать _register_steps_from_config()**

**Файл:** `integration/core/initialization_manager.py`

**Добавить метод:**
```python
def _register_steps_from_config(self, coordinator):
    """Регистрация шагов из конфигурации"""
    for step_name, step_config in self.init_config.get_enabled_steps().items():
        # Определяем функцию инициализации в зависимости от типа
        if step_config.type == InitializationStepType.INTERNAL:
            init_func = self._get_internal_init_func(step_name, coordinator)
        elif step_config.type == InitializationStepType.INTEGRATION:
            init_func = self._get_integration_init_func(step_config, coordinator)
        elif step_config.type == InitializationStepType.WORKFLOW:
            init_func = self._get_workflow_init_func(step_config, coordinator)
        else:
            logger.warning(f"⚠️ [INIT] Неизвестный тип шага: {step_config.type}")
            continue
        
        # Регистрируем шаг
        self.register_step(
            name=step_name,
            description=step_config.description,
            init_func=init_func,
            dependencies=step_config.dependencies,
            critical=step_config.critical,
            timeout_sec=step_config.timeout_sec
        )
```

**Реализовать вспомогательные методы:**
```python
def _get_integration_init_func(self, step_config, coordinator):
    """Получение функции инициализации для интеграции"""
    integration_name = step_config.integration_name
    if not integration_name:
        raise ValueError(f"integration_name не указан для шага {step_config.name}")
    
    integration = coordinator.integrations.get(integration_name)
    if not integration:
        raise ValueError(f"Интеграция '{integration_name}' не найдена")
    
    # Специальная обработка для speech_playback (получает AVF engine)
    if step_config.special_params and "avf_engine_source" in step_config.special_params:
        avf_source = step_config.special_params["avf_engine_source"]
        avf_integration = coordinator.integrations.get(avf_source)
        if avf_integration and hasattr(avf_integration, '_avf_engine'):
            avf_engine = avf_integration._avf_engine
            return lambda: integration.initialize(avf_engine=avf_engine)
    
    return lambda: integration.initialize()
```

---

**Задача 2: Обновить initialize() для использования InitializationManager**

**Файл:** `integration/core/simple_module_coordinator.py`

**Обновить метод `initialize()`:**
```python
async def initialize(self) -> bool:
    """Инициализация всех компонентов"""
    try:
        # 1. Создаем core компоненты
        # ... существующий код ...
        
        # 2. Настраиваем критичные подписки (ДО инициализации)
        # ... существующий код ...
        
        # 3. Создаем интеграции
        config_data = self.config._load_config()
        self._use_new_initialization = config_data.get('app', {}).get('use_new_initialization', False)
        
        if self._use_new_initialization:
            # Новая система
            await self._create_integrations_simple()
            
            # Создаем менеджер инициализации
            self.init_manager = InitializationManager(
                event_bus=self.event_bus,
                state_manager=self.state_manager,
                error_handler=self.error_handler,
                config_loader=self.config
            )
            
            # Регистрируем шаги из конфигурации
            self.init_manager._register_steps_from_config(self)
            
            # Выполняем все инициализации
            success = await self.init_manager.initialize_all()
            
            if success:
                await self._setup_coordination()
                await self._setup_auto_audio_connections()
                self.is_initialized = True
                return True
            else:
                logger.error("❌ [COORDINATOR] Некоторые инициализации завершились с ошибками")
                return False
        else:
            # Старая система
            await self._create_integrations()
            await self._initialize_integrations()
            await self._setup_coordination()
            await self._setup_auto_audio_connections()
            self.is_initialized = True
            return True
            
    except Exception as e:
        logger.error(f"❌ [COORDINATOR] Критическая ошибка инициализации: {e}")
        return False
```

---

**Задача 3: Создать тесты инициализации**

**Файл:** `tests/test_initialization_execution.py`

**Тесты:**
1. Тест порядка инициализации (должен соответствовать конфигурации)
2. Тест передачи AVF engine в speech_playback
3. Тест обработки ошибок (критичных/некритичных)
4. Тест таймаутов
5. Тест условной инициализации

**Проверка:**
```bash
pytest tests/test_initialization_execution.py -v
```

---

### 7.3 Чек-лист фазы 5

- [ ] `_register_steps_from_config()` реализован
- [ ] `InitializationManager` используется для инициализации
- [ ] Порядок инициализации соответствует конфигурации
- [ ] AVF engine передается в speech_playback
- [ ] Все интеграции инициализируются корректно
- [ ] Тесты инициализации проходят
- [ ] Все существующие тесты все еще проходят

**Время:** 8-10 часов

---

## 📊 Часть 8: Фаза 6 - Удаление Старого Кода

### 8.1 Цель фазы

**Цель:** Удалить неиспользуемый код после проверки, что новая реализация работает корректно

**Критерии готовности:**
- [ ] Новая реализация работает стабильно
- [ ] Все тесты проходят
- [ ] Старый код удален
- [ ] Флаг переключения удален (новая реализация по умолчанию)

---

### 8.2 Задачи

**Задача 1: Включить новую реализацию по умолчанию**

**Файл:** `config/unified_config.yaml`

**Изменить:**
```yaml
app:
  # ... существующие настройки ...
  use_new_initialization: true  # ✅ Изменить на true
```

---

**Задача 2: Удалить старый код**

**Файл:** `integration/core/simple_module_coordinator.py`

**Удалить:**
1. ❌ Метод `_create_integrations()` (строки 188-457)
2. ❌ Метод `_initialize_integrations()` (строки 473-535)
3. ❌ Флаг `_use_new_initialization`
4. ❌ Условную логику в `initialize()`

**Оставить:**
- ✅ `_create_integrations_simple()`
- ✅ Использование `InitializationManager`

---

**Задача 3: Упростить initialize()**

**Файл:** `integration/core/simple_module_coordinator.py`

**Упрощенный метод:**
```python
async def initialize(self) -> bool:
    """Инициализация всех компонентов через InitializationManager"""
    try:
        # 1. Создаем core компоненты
        self.event_bus = EventBus()
        self.state_manager = ApplicationStateManager()
        self.error_handler = ErrorHandler(self.event_bus)
        
        # 2. Запускаем фоновый loop
        self._start_background_loop()
        
        # 3. Настраиваем критичные подписки (ДО инициализации)
        self.state_manager.attach_event_bus(self.event_bus)
        self.event_bus.attach_loop(self._bg_loop)
        await self._setup_critical_subscriptions()
        
        # 4. Создаем интеграции (упрощенный метод)
        await self._create_integrations_simple()
        
        # 5. Создаем менеджер инициализации
        self.init_manager = InitializationManager(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config_loader=self.config
        )
        
        # 6. Регистрируем шаги из конфигурации
        self.init_manager._register_steps_from_config(self)
        
        # 7. Выполняем все инициализации
        success = await self.init_manager.initialize_all()
        
        if success:
            # 8. Настраиваем координацию
            await self._setup_coordination()
            
            # 9. Настраиваем авто-всё связи
            await self._setup_auto_audio_connections()
            
            self.is_initialized = True
            return True
        else:
            logger.error("❌ [COORDINATOR] Некоторые инициализации завершились с ошибками")
            return False
            
    except Exception as e:
        logger.error(f"❌ [COORDINATOR] Критическая ошибка инициализации: {e}")
        logger.exception("❌ [COORDINATOR] Детали ошибки:")
        return False
```

---

**Задача 4: Удалить флаг из конфигурации**

**Файл:** `config/unified_config.yaml`

**Удалить:**
```yaml
app:
  # use_new_initialization: true  # ❌ Удалить, новая реализация по умолчанию
```

---

### 8.3 Чек-лист фазы 6

- [ ] Новая реализация включена по умолчанию
- [ ] Старый код удален
- [ ] Флаг переключения удален
- [ ] `initialize()` упрощен
- [ ] Все тесты проходят
- [ ] Приложение работает корректно

**Время:** 2-3 часа

---

## 📊 Часть 9: Фаза 7 - Финальная Проверка

### 9.1 Цель фазы

**Цель:** Полная проверка новой реализации, сравнение с baseline, финальная валидация

**Критерии готовности:**
- [ ] Все тесты проходят (100%)
- [ ] Порядок инициализации соответствует baseline
- [ ] Производительность не ухудшилась
- [ ] Логирование работает корректно
- [ ] Документация обновлена

---

### 9.2 Задачи

**Задача 1: Запустить все тесты**

```bash
# Все тесты
pytest tests/ -v

# Тесты инициализации
pytest tests/test_initialization_*.py -v

# Тесты координатора
pytest tests/test_coordinator_*.py -v
```

**Проверка:**
- [ ] Все тесты проходят (100%)
- [ ] Нет регрессий

---

**Задача 2: Сравнить порядок инициализации с baseline**

**Создать тест сравнения:**
```python
def test_initialization_order_matches_baseline():
    """Проверка, что порядок инициализации соответствует baseline"""
    # Загрузить baseline порядок
    baseline_order = load_baseline_order()
    
    # Загрузить текущий порядок из конфигурации
    current_order = load_current_order()
    
    # Сравнить
    assert current_order == baseline_order, "Порядок инициализации не соответствует baseline"
```

---

**Задача 3: Проверить производительность**

**Создать тест производительности:**
```python
def test_initialization_performance():
    """Проверка производительности инициализации"""
    import time
    
    start_time = time.monotonic()
    # Выполнить инициализацию
    success = await coordinator.initialize()
    duration = time.monotonic() - start_time
    
    assert success == True
    assert duration < 60.0  # Инициализация должна занимать < 60 секунд
```

---

**Задача 4: Обновить документацию**

**Обновить:**
- [ ] `CURRENT_INITIALIZATION_REQUIREMENTS.md` — отметить, что требования выполнены
- [ ] `INITIALIZATION_MIGRATION_PLAN.md` — отметить завершение миграции
- [ ] `AUDIO_SYSTEM_REFACTORING_MASTER_PLAN.md` — обновить статус

---

### 9.3 Чек-лист фазы 7

- [ ] Все тесты проходят (100%)
- [ ] Порядок инициализации соответствует baseline
- [ ] Производительность не ухудшилась
- [ ] Логирование работает корректно
- [ ] Документация обновлена
- [ ] Приложение работает стабильно

**Время:** 4-6 часов

---

## 📊 Часть 10: Итоговая Таблица Фаз

| Фаза | Название | Время | Критерии готовности | Тесты |
|------|----------|-------|---------------------|-------|
| 0 | Подготовка и анализ | 2-3ч | Baseline создан, зависимости задокументированы | test_initialization_baseline.py |
| 1 | Конфигурация | 4-6ч | Конфигурация создана и валидируется | test_initialization_config.py |
| 2 | InitializationManager (базовая) | 6-8ч | Менеджер работает изолированно | test_initialization_manager.py |
| 3 | Интеграция менеджера | 4-6ч | Менеджер интегрирован, флаг работает | test_coordinator_initialization.py |
| 4 | Миграция создания | 4-6ч | Упрощенное создание работает | test_integration_creation.py |
| 5 | Миграция инициализации | 8-10ч | Новая инициализация работает | test_initialization_execution.py |
| 6 | Удаление старого кода | 2-3ч | Старый код удален | Все тесты |
| 7 | Финальная проверка | 4-6ч | Все проверки пройдены | Все тесты |

**ИТОГО:** 34-48 часов (4-6 рабочих дней)

---

## 📊 Часть 11: Критерии Успеха

### 11.1 Функциональные критерии

- ✅ Все интеграции инициализируются в правильном порядке
- ✅ AVF engine передается в speech_playback
- ✅ Критичные подписки настраиваются ДО инициализации
- ✅ Условная инициализация работает (tray, action_execution)
- ✅ Обработка ошибок работает корректно
- ✅ Таймауты работают

---

### 11.2 Качественные критерии

- ✅ Порядок инициализации определяется конфигурацией
- ✅ Зависимости явные в конфигурации
- ✅ Централизованное логирование
- ✅ Детальные отчеты о инициализации
- ✅ Легко диагностировать проблемы

---

### 11.3 Технические критерии

- ✅ Все тесты проходят (100%)
- ✅ Производительность не ухудшилась
- ✅ Обратная совместимость сохранена
- ✅ Код упрощен (удалено ~331 строка)

---

## ✅ Заключение

**Поэтапный план реализации:**
1. ✅ 7 фаз с четкими критериями готовности
2. ✅ Изолированное тестирование на каждом этапе
3. ✅ Постепенная миграция без ломания существующей функциональности
4. ✅ Возможность отката на любом этапе
5. ✅ Финальная проверка и валидация

**Готов к реализации!**
