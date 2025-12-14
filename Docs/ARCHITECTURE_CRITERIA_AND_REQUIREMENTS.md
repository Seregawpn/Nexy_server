# 🎯 Критерии и Требования к Идеальной Архитектуре

**Дата:** 2025-12-13  
**Статус:** Комплексные критерии и требования

---

## 📋 Часть 1: Критерии Идеальной Архитектуры

### 1.1 Критерий #1: Разделение ответственности (Separation of Concerns)

**Требование:**
- ✅ Каждый модуль отвечает за **одну** конкретную задачу
- ✅ Модули **не знают** о других модулях (кроме явных зависимостей)
- ✅ Интеграции **только координируют** через EventBus
- ✅ Логика **изолирована** в модулях

**Проверка:**
```python
# ✅ ПРАВИЛЬНО: Модуль отвечает за одну задачу
class AVFManager:
    """Управление AVF жизненным циклом - ТОЛЬКО AVF"""
    async def initialize(self) -> bool: ...
    async def activate(self) -> DeviceInfo: ...
    async def deactivate(self) -> bool: ...

# ❌ НЕПРАВИЛЬНО: Модуль смешивает ответственности
class AudioManager:
    """Управление AVF И Google - СМЕШАНО"""
    async def initialize_avf(self) -> bool: ...
    async def initialize_google(self) -> bool: ...
    async def activate_avf(self) -> DeviceInfo: ...
    async def activate_google(self) -> bool: ...
```

**Метрики:**
- Размер модуля: ≤ 500 строк
- Количество ответственностей: 1
- Зависимости от других модулей: минимальные

---

### 1.2 Критерий #2: Единый источник истины (Single Source of Truth)

**Требование:**
- ✅ Только `ApplicationStateManager` управляет состоянием
- ✅ Нет локальных флагов состояния в интеграциях/модулях
- ✅ Все изменения состояния через `state_manager.set_*()`
- ✅ Все проверки состояния через `state_manager.is_*()`

**Проверка:**
```python
# ✅ ПРАВИЛЬНО: Единый источник истины
class VoiceRecognitionIntegration:
    def __init__(self):
        # ❌ УДАЛЕНО: Локальные флаги
        # self._recording_active = False
        # self._google_recording_active = False
        
        self.state_manager = ...  # ✅ ЕДИНЫЙ источник истины
    
    async def _on_recording_start(self):
        # ✅ Обновляем только state_manager
        self.state_manager.set_microphone_state("active", session_id)
    
    def is_recording(self):
        # ✅ Проверяем только state_manager
        return self.state_manager.is_microphone_active()

# ❌ НЕПРАВИЛЬНО: Множественные источники истины
class VoiceRecognitionIntegration:
    def __init__(self):
        self._recording_active = False  # ❌ Локальный флаг
        self._google_recording_active = False  # ❌ Локальный флаг
        self.state_manager = ...  # ❌ Еще один источник
    
    def is_recording(self):
        # ❌ Конфликт между источниками
        if self._recording_active or self.state_manager.is_microphone_active():
            return True
```

**Метрики:**
- Количество источников истины: 1
- Локальные флаги состояния: 0
- Атомарные операции: 100%

---

### 1.3 Критерий #3: Изоляция и тестируемость

**Требование:**
- ✅ Модули изолированы друг от друга
- ✅ Легко тестировать изолированно (без зависимостей)
- ✅ Легко мокать зависимости
- ✅ Тесты запускаются быстро (< 1 секунды)

**Проверка:**
```python
# ✅ ПРАВИЛЬНО: Изолированный модуль
class AVFManager:
    def __init__(self, config: AVFConfig):
        self._config = config  # ✅ Зависимость через конструктор
        self._engine: Optional[AVFAudioEngine] = None
    
    async def initialize(self) -> bool:
        # ✅ Логика изолирована
        self._engine = AVFAudioEngine(self._config)
        return True

# ✅ ПРАВИЛЬНО: Легко тестировать
def test_avf_manager():
    config = AVFConfig(enabled=True)
    manager = AVFManager(config)
    result = await manager.initialize()
    assert result == True

# ❌ НЕПРАВИЛЬНО: Зависимости от глобального состояния
class AVFManager:
    def __init__(self):
        self._config = UnifiedConfigLoader().get_audio_config()  # ❌ Глобальная зависимость
    
    async def initialize(self) -> bool:
        # ❌ Сложно тестировать (нужно мокать UnifiedConfigLoader)
        pass
```

**Метрики:**
- Время выполнения теста: < 1 секунды
- Количество зависимостей: минимальные
- Изоляция: 100%

---

### 1.4 Критерий #4: Четкая инициализация

**Требование:**
- ✅ Понятная последовательность инициализации
- ✅ Диагностическое логирование на каждом этапе
- ✅ Обработка ошибок инициализации
- ✅ Документация процесса

**Проверка:**
```python
# ✅ ПРАВИЛЬНО: Четкая инициализация
class VoiceRecognitionIntegration:
    async def initialize(self) -> bool:
        logger.info("🔍 [VOICE] Начало инициализации")
        
        # 1. Инициализация AVF
        logger.info("🔍 [VOICE] Инициализация AVF...")
        avf_ok = await self._avf_manager.initialize()
        if not avf_ok:
            logger.error("❌ [VOICE] AVF инициализация не удалась")
            return False
        
        # 2. Инициализация Google
        logger.info("🔍 [VOICE] Инициализация Google...")
        google_ok = await self._google_manager.initialize()
        if not google_ok:
            logger.error("❌ [VOICE] Google инициализация не удалась")
            return False
        
        # 3. Подписки на события
        logger.info("🔍 [VOICE] Подписки на события...")
        await self.event_bus.subscribe(...)
        
        logger.info("✅ [VOICE] Инициализация завершена")
        return True

# ❌ НЕПРАВИЛЬНО: Непонятная инициализация
class VoiceRecognitionIntegration:
    async def initialize(self) -> bool:
        # ❌ Нет логирования
        # ❌ Вся логика смешана
        # ❌ Непонятно, что инициализируется
        pass
```

**Метрики:**
- Логирование на каждом этапе: 100%
- Обработка ошибок: 100%
- Документация: есть

---

### 1.5 Критерий #5: Четкая координация через EventBus

**Требование:**
- ✅ Интеграции **только координируют** через EventBus
- ✅ Логика **в модулях**, не в интеграциях
- ✅ Подписки и публикации событий **документированы**
- ✅ Контракты событий **валидируются**

**Проверка:**
```python
# ✅ ПРАВИЛЬНО: Только координация
class VoiceRecognitionIntegration:
    async def _on_recording_start(self, event: Dict[str, Any]):
        """Обработка события voice.recording_start - координация"""
        session_id = event.get("data", {}).get("session_id")
        
        # ✅ Координация: Вызовы менеджеров
        device_info = await self._avf_manager.activate(duration_sec=1.0)
        await self._avf_manager.deactivate()
        await asyncio.sleep(0.2)
        await self._google_manager.activate(callback=self._on_google_audio_chunk)
        
        # ✅ Координация: Обновление состояния
        self.state_manager.set_microphone_state("active", session_id)
        
        # ✅ Координация: Публикация событий
        await self.event_bus.publish("microphone.opened", {...})

# ❌ НЕПРАВИЛЬНО: Логика в интеграции
class VoiceRecognitionIntegration:
    async def _on_recording_start(self, event: Dict[str, Any]):
        # ❌ Логика AVF в интеграции
        self._avf_engine = AVFAudioEngine(...)
        await self._avf_engine.start_input()
        # ❌ Логика Google в интеграции
        self._google_recognizer = sr.Recognizer()
        self._google_microphone = sr.Microphone()
        # ❌ Слишком много логики в интеграции!
```

**Метрики:**
- Размер интеграции: ≤ 500 строк
- Логика в модулях: 100%
- Координация в интеграции: 100%

---

## 📋 Часть 2: Требования к Централизации

### 2.1 Централизация состояния

**Требование:**
- ✅ Только `ApplicationStateManager` управляет состоянием
- ✅ Все изменения состояния через `state_manager.set_*()`
- ✅ Все проверки состояния через `state_manager.is_*()`
- ✅ Атомарные операции с lock

**Реализация:**
```python
# ✅ ПРАВИЛЬНО: Централизованное состояние
class ApplicationStateManager:
    def __init__(self):
        self._lock = threading.Lock()
        self._microphone_state: MicrophoneState = MicrophoneState.IDLE
        self._current_session_id: Optional[str] = None
    
    def set_microphone_state(self, state: MicrophoneState, session_id: str):
        """Атомарное изменение состояния"""
        with self._lock:
            self._microphone_state = state
            self._current_session_id = session_id
            logger.info(f"✅ [STATE] Микрофон: {state}, session_id={session_id}")
    
    def is_microphone_active(self) -> bool:
        """Проверка состояния микрофона"""
        with self._lock:
            return self._microphone_state == MicrophoneState.ACTIVE
```

**Проверка:**
- ❌ Локальные флаги состояния: 0
- ✅ Использование state_manager: 100%
- ✅ Атомарные операции: 100%

---

### 2.2 Централизация конфигурации

**Требование:**
- ✅ Единый источник конфигурации: `config/unified_config.yaml`
- ✅ Загрузка через `UnifiedConfigLoader`
- ✅ Валидация конфигурации через схемы
- ✅ Документация конфигурации

**Реализация:**
```python
# ✅ ПРАВИЛЬНО: Централизованная конфигурация
class UnifiedConfigLoader:
    def __init__(self):
        self._config = self._load_config()
        self._validate_config()
    
    def get_audio_avf_config(self) -> Dict[str, Any]:
        """Получение конфигурации AVF"""
        return self._config.get("audio", {}).get("avf", {})
    
    def get_audio_google_config(self) -> Dict[str, Any]:
        """Получение конфигурации Google"""
        return self._config.get("voice_recognition", {})

# ✅ ПРАВИЛЬНО: Использование конфигурации
class AVFManager:
    def __init__(self, config: AVFConfig):
        self._config = config  # ✅ Конфигурация через конструктор
    
    @classmethod
    def from_unified_config(cls, loader: UnifiedConfigLoader) -> "AVFManager":
        """Создание из unified_config"""
        avf_config = loader.get_audio_avf_config()
        return cls(AVFConfig.from_dict(avf_config))
```

**Проверка:**
- ❌ Хардкод конфигурации: 0
- ✅ Использование unified_config: 100%
- ✅ Валидация конфигурации: 100%

---

### 2.3 Централизация обработки ошибок

**Требование:**
- ✅ Все ошибки через `ErrorHandler`
- ✅ Структурированные коды ошибок
- ✅ Логирование ошибок с контекстом
- ✅ Восстановление состояния после ошибок

**Реализация:**
```python
# ✅ ПРАВИЛЬНО: Централизованная обработка ошибок
class VoiceRecognitionIntegration:
    async def _on_recording_start(self, event: Dict[str, Any]):
        try:
            # Логика активации
            device_info = await self._avf_manager.activate(duration_sec=1.0)
        except Exception as e:
            # ✅ Централизованная обработка ошибок
            await self.error_handler.handle_error(
                error_code="E_MIC_ACTIVATION_FAILED",
                error_message=str(e),
                context={
                    "session_id": session_id,
                    "source": "voice_recognition_integration",
                    "action": "activate_microphone"
                }
            )
            # ✅ Восстановление состояния
            self.state_manager.set_microphone_state("idle", session_id)
```

**Проверка:**
- ❌ Прямые исключения: 0
- ✅ Использование ErrorHandler: 100%
- ✅ Восстановление состояния: 100%

---

## 📋 Часть 3: Конфигурации (Что Учесть и Централизовать)

### 3.1 Конфигурации, которые нужно централизовать

#### 3.1.1 AVF Конфигурация

**Источник:** `config/unified_config.yaml`
```yaml
audio:
  avf:
    enabled: true
    rollout_percentage: 0
    input_format: "16kHz, mono, int16"
    output_format: "auto"
    buffer_size_ms: 100
    enable_hardware_optimization: true
  
  ks_avf:
    enabled: false  # Kill-switch для AVF
```

**Требования:**
- ✅ Загрузка через `UnifiedConfigLoader.get_audio_avf_config()`
- ✅ Валидация через схему `config/schemas/audio_avf_schema.yaml`
- ✅ Использование в `AVFManager` через `AVFConfig`

**Реализация:**
```python
@dataclass
class AVFConfig:
    enabled: bool = True
    input_format: str = "16kHz, mono, int16"
    buffer_size_ms: int = 100
    enable_hardware_optimization: bool = True
    
    @classmethod
    def from_unified_config(cls, loader: UnifiedConfigLoader) -> "AVFConfig":
        """Создание из unified_config"""
        avf_config = loader.get_audio_avf_config()
        return cls(
            enabled=avf_config.get("enabled", True),
            input_format=avf_config.get("input_format", "16kHz, mono, int16"),
            buffer_size_ms=avf_config.get("buffer_size_ms", 100),
            enable_hardware_optimization=avf_config.get("enable_hardware_optimization", True)
        )
```

---

#### 3.1.2 Google Конфигурация

**Источник:** `config/unified_config.yaml`
```yaml
voice_recognition:
  enabled: true
  language: en-US
  max_alternatives: 3
  phrase_timeout: 0.3
  silence_timeout: 0.8

voice:
  start_retry_delay_ms: 300
```

**Требования:**
- ✅ Загрузка через `UnifiedConfigLoader.get_voice_recognition_config()`
- ✅ Валидация через схему `config/schemas/voice_recognition_schema.yaml`
- ✅ Использование в `GoogleManager` через `GoogleConfig`

**Реализация:**
```python
@dataclass
class GoogleConfig:
    language: str = "en-US"
    phrase_time_limit: Optional[float] = None
    energy_threshold: int = 4000
    pause_threshold: float = 0.8
    
    @classmethod
    def from_unified_config(cls, loader: UnifiedConfigLoader) -> "GoogleConfig":
        """Создание из unified_config"""
        voice_config = loader.get_voice_recognition_config()
        return cls(
            language=voice_config.get("language", "en-US"),
            phrase_time_limit=voice_config.get("phrase_time_limit"),
            energy_threshold=voice_config.get("energy_threshold", 4000),
            pause_threshold=voice_config.get("pause_threshold", 0.8)
        )
```

---

#### 3.1.3 Feature Flags и Kill-Switches

**Источник:** `config/unified_config.yaml` или переменные окружения
```yaml
audio:
  avf:
    enabled: true
    rollout_percentage: 0
  
  ks_avf:
    enabled: false  # Kill-switch для AVF

voice_recognition:
  enabled: true
```

**Требования:**
- ✅ Feature flags через `unified_config.yaml`
- ✅ Kill-switches через переменные окружения или `unified_config.yaml`
- ✅ Документация в `Docs/FEATURE_FLAGS.md`

**Реализация:**
```python
class AVFManager:
    def __init__(self, config: AVFConfig):
        self._config = config
        # ✅ Проверка feature flag
        self._enabled = config.enabled and not self._is_kill_switch_enabled()
    
    def _is_kill_switch_enabled(self) -> bool:
        """Проверка kill-switch"""
        # Проверка переменной окружения
        if os.getenv("NEXY_KS_AVF_ENABLED", "false").lower() == "true":
            return True
        # Проверка unified_config
        loader = UnifiedConfigLoader()
        ks_config = loader.get_audio_avf_config().get("ks_avf", {})
        return ks_config.get("enabled", False)
```

---

### 3.2 Конфигурации, которые нужно учесть

#### 3.2.1 Конфигурация инициализации

**Требования:**
- ✅ Последовательность инициализации в `SimpleModuleCoordinator`
- ✅ Зависимости между модулями
- ✅ Порядок подписок на события

**Реализация:**
```python
class SimpleModuleCoordinator:
    def _create_integrations(self):
        """Создание интеграций в правильном порядке"""
        # ✅ Порядок инициализации:
        # 1. InstanceManager (базовые зависимости)
        # 2. HardwareId (идентификация)
        # 3. FirstRunPermissions (разрешения)
        # 4. PermissionRestart (перезапуск)
        # 5. Tray (интерфейс)
        # 6. ModeManagement (режимы)
        # 7. InputProcessing (ввод)
        # 8. VoiceRecognition (аудио) ← Здесь
        # 9. NetworkManager (сеть)
        # ...
        integrations = [
            InstanceManagerIntegration(...),
            HardwareIdIntegration(...),
            FirstRunPermissionsIntegration(...),
            PermissionRestartIntegration(...),
            TrayIntegration(...),
            ModeManagementIntegration(...),
            InputProcessingIntegration(...),
            VoiceRecognitionIntegration(...),  # ← После InputProcessing
            NetworkManagerIntegration(...),
            # ...
        ]
        return integrations
```

---

#### 3.2.2 Конфигурация EventBus

**Требования:**
- ✅ Приоритеты событий (`EventPriority`)
- ✅ Контракты событий (payload схемы)
- ✅ Подписки и публикации документированы

**Реализация:**
```python
class VoiceRecognitionIntegration:
    async def initialize(self) -> bool:
        # ✅ Подписки с приоритетами
        await self.event_bus.subscribe(
            "voice.recording_start",
            self._on_recording_start,
            EventPriority.HIGH  # ✅ Высокий приоритет
        )
        await self.event_bus.subscribe(
            "voice.recording_stop",
            self._on_recording_stop,
            EventPriority.HIGH
        )
        await self.event_bus.subscribe(
            "app.mode_changed",
            self._on_app_mode_changed,
            EventPriority.MEDIUM  # ✅ Средний приоритет
        )
```

---

## 📋 Часть 4: Правильное Распределение Ответственности

### 4.1 Распределение между модулями

**Модуль `audio_avf`:**
- ✅ Инициализация AVF (создание AVFAudioEngine)
- ✅ Активация микрофона для диагностики (~1 сек)
- ✅ Деактивация микрофона
- ✅ Получение информации об устройстве
- ❌ НЕ управляет Google Speech Recognition
- ❌ НЕ координирует через EventBus

**Модуль `audio_google`:**
- ✅ Инициализация Google Speech Recognition
- ✅ Активация записи
- ✅ Деактивация записи
- ✅ Распознавание речи
- ❌ НЕ управляет AVF
- ❌ НЕ координирует через EventBus

**Интеграция `voice_recognition_integration`:**
- ✅ Координация через EventBus
- ✅ Подписки и публикации событий
- ✅ Вызовы менеджеров (AVF и Google)
- ✅ Обновление состояния через state_manager
- ❌ НЕ содержит логику AVF
- ❌ НЕ содержит логику Google

---

### 4.2 Распределение между Core компонентами

**ApplicationStateManager:**
- ✅ Управление состоянием приложения
- ✅ Атомарные операции с lock
- ✅ Единый источник истины
- ❌ НЕ содержит бизнес-логику

**EventBus:**
- ✅ Публикация и подписка на события
- ✅ Приоритеты событий
- ✅ Валидация контрактов
- ❌ НЕ содержит бизнес-логику

**ErrorHandler:**
- ✅ Обработка ошибок
- ✅ Структурированные коды ошибок
- ✅ Логирование ошибок
- ❌ НЕ содержит бизнес-логику

---

## 📋 Часть 5: Правильное Соединение Компонентов

### 5.1 Соединение модулей с интеграциями

**Правило:**
- ✅ Модули **не знают** о EventBus
- ✅ Интеграции **координируют** через EventBus
- ✅ Модули **возвращают** результаты
- ✅ Интеграции **публикуют** события

**Реализация:**
```python
# ✅ ПРАВИЛЬНО: Модуль не знает о EventBus
class AVFManager:
    async def activate(self, duration_sec: float = 1.0) -> DeviceInfo:
        """Активация микрофона - возвращает результат"""
        # Логика активации
        device_info = DeviceInfo(...)
        return device_info  # ✅ Возвращает результат

# ✅ ПРАВИЛЬНО: Интеграция координирует через EventBus
class VoiceRecognitionIntegration:
    async def _on_recording_start(self, event: Dict[str, Any]):
        # ✅ Вызов модуля
        device_info = await self._avf_manager.activate(duration_sec=1.0)
        
        # ✅ Публикация события
        await self.event_bus.publish("microphone.opened", {
            "session_id": session_id,
            "device_info": device_info.to_dict()
        })
```

---

### 5.2 Соединение модулей друг с другом

**Правило:**
- ✅ Модули **не зависят** друг от друга напрямую
- ✅ Соединение через **интеграции** и **EventBus**
- ✅ Явные зависимости через **конструктор**

**Реализация:**
```python
# ✅ ПРАВИЛЬНО: Модули независимы
class AVFManager:
    def __init__(self, config: AVFConfig):
        self._config = config  # ✅ Зависимость через конструктор
        # ❌ НЕТ зависимости от GoogleManager

class GoogleManager:
    def __init__(self, config: GoogleConfig):
        self._config = config  # ✅ Зависимость через конструктор
        # ❌ НЕТ зависимости от AVFManager

# ✅ ПРАВИЛЬНО: Соединение через интеграцию
class VoiceRecognitionIntegration:
    def __init__(self, ...):
        self._avf_manager = AVFManager(avf_config)
        self._google_manager = GoogleManager(google_config)
        # ✅ Соединение через интеграцию
```

---

### 5.3 Соединение с ApplicationStateManager

**Правило:**
- ✅ Все изменения состояния через `state_manager.set_*()`
- ✅ Все проверки состояния через `state_manager.is_*()`
- ✅ Атомарные операции с lock

**Реализация:**
```python
# ✅ ПРАВИЛЬНО: Использование state_manager
class VoiceRecognitionIntegration:
    async def _on_recording_start(self, event: Dict[str, Any]):
        # ✅ Обновление состояния
        self.state_manager.set_microphone_state("active", session_id)
        
        # ✅ Проверка состояния
        if self.state_manager.is_microphone_active():
            logger.info("✅ Микрофон активен")
```

---

## 📋 Часть 6: Правильная Интеграция в Общий Проект

### 6.1 Интеграция в SimpleModuleCoordinator

**Требования:**
- ✅ Правильный порядок инициализации
- ✅ Зависимости между интеграциями
- ✅ Обработка ошибок инициализации

**Реализация:**
```python
class SimpleModuleCoordinator:
    def _create_integrations(self):
        """Создание интеграций в правильном порядке"""
        integrations = [
            # 1. Базовые зависимости
            InstanceManagerIntegration(...),
            HardwareIdIntegration(...),
            
            # 2. Разрешения (блокирующие)
            FirstRunPermissionsIntegration(...),
            PermissionRestartIntegration(...),
            
            # 3. Интерфейс
            TrayIntegration(...),
            
            # 4. Режимы
            ModeManagementIntegration(...),
            
            # 5. Ввод (ДО voice_recognition)
            InputProcessingIntegration(...),
            
            # 6. Аудио (ПОСЛЕ input_processing)
            VoiceRecognitionIntegration(...),  # ← Здесь
            
            # 7. Сеть
            NetworkManagerIntegration(...),
            
            # 8. Остальные
            # ...
        ]
        return integrations
    
    async def _initialize_integrations(self):
        """Инициализация интеграций"""
        for integration in self._integrations:
            try:
                logger.info(f"🔍 [INIT] Инициализация {integration.__class__.__name__}...")
                success = await integration.initialize()
                if not success:
                    logger.error(f"❌ [INIT] {integration.__class__.__name__} не инициализирован")
            except Exception as e:
                logger.error(f"❌ [INIT] Ошибка инициализации {integration.__class__.__name__}: {e}")
                logger.exception("❌ [INIT] Детали исключения:")
```

---

### 6.2 Интеграция в EventBus

**Требования:**
- ✅ Контракты событий документированы
- ✅ Валидация payload
- ✅ Приоритеты событий

**Реализация:**
```python
# ✅ ПРАВИЛЬНО: Контракт EventBus
VOICE_RECOGNITION_CONTRACT = {
    "module": "voice_recognition",
    "version": "1.0",
    "events": {
        "input": {
            "voice.recording_start": {
                "payload": {
                    "session_id": "string (uuid4)",
                    "source": "string (keyboard|automatic)"
                },
                "required": ["session_id"]
            },
            "voice.recording_stop": {
                "payload": {
                    "session_id": "string (uuid4)"
                },
                "required": ["session_id"]
            }
        },
        "output": {
            "microphone.opened": {
                "payload": {
                    "session_id": "string (uuid4)",
                    "device_info": "dict"
                },
                "required": ["session_id", "device_info"]
            },
            "microphone.closed": {
                "payload": {
                    "session_id": "string (uuid4)"
                },
                "required": ["session_id"]
            }
        }
    }
}

class VoiceRecognitionIntegration:
    async def initialize(self) -> bool:
        # ✅ Подписки с приоритетами
        await self.event_bus.subscribe(
            "voice.recording_start",
            self._on_recording_start,
            EventPriority.HIGH
        )
        # ...
```

---

### 6.3 Интеграция в конфигурацию

**Требования:**
- ✅ Использование `UnifiedConfigLoader`
- ✅ Валидация через схемы
- ✅ Документация конфигурации

**Реализация:**
```python
# ✅ ПРАВИЛЬНО: Использование unified_config
class VoiceRecognitionIntegration:
    def __init__(self, event_bus, state_manager, error_handler, config=None):
        # ✅ Загрузка конфигурации
        loader = UnifiedConfigLoader()
        
        # ✅ Создание менеджеров из конфигурации
        avf_config = AVFConfig.from_unified_config(loader)
        google_config = GoogleConfig.from_unified_config(loader)
        
        self._avf_manager = AVFManager(avf_config)
        self._google_manager = GoogleManager(google_config)
```

---

## 📋 Часть 7: Чек-лист Проверки Архитектуры

### 7.1 Чек-лист модулей

- [ ] Модуль отвечает за одну задачу
- [ ] Размер модуля ≤ 500 строк
- [ ] Модуль не знает о EventBus
- [ ] Модуль не знает о других модулях (кроме явных зависимостей)
- [ ] Зависимости через конструктор
- [ ] Легко тестировать изолированно
- [ ] README модуля документирован

---

### 7.2 Чек-лист интеграций

- [ ] Размер интеграции ≤ 500 строк
- [ ] Интеграция только координирует через EventBus
- [ ] Логика в модулях, не в интеграции
- [ ] Нет локальных флагов состояния
- [ ] Использование только state_manager
- [ ] Контракты EventBus документированы
- [ ] Подписки и публикации с приоритетами

---

### 7.3 Чек-лист централизации

- [ ] Только ApplicationStateManager управляет состоянием
- [ ] Нет локальных флагов состояния
- [ ] Все изменения состояния через state_manager.set_*()
- [ ] Все проверки состояния через state_manager.is_*()
- [ ] Конфигурация через UnifiedConfigLoader
- [ ] Ошибки через ErrorHandler
- [ ] Атомарные операции с lock

---

### 7.4 Чек-лист конфигурации

- [ ] Конфигурация в unified_config.yaml
- [ ] Загрузка через UnifiedConfigLoader
- [ ] Валидация через схемы
- [ ] Feature flags документированы
- [ ] Kill-switches документированы
- [ ] Документация конфигурации

---

## ✅ Часть 8: Итоговые Критерии

### 8.1 Обязательные критерии

1. **Разделение ответственности:**
   - ✅ Модули: одна задача
   - ✅ Интеграции: только координация
   - ✅ Размер: ≤ 500 строк

2. **Единый источник истины:**
   - ✅ Только ApplicationStateManager
   - ✅ Нет локальных флагов
   - ✅ Атомарные операции

3. **Изоляция и тестируемость:**
   - ✅ Модули изолированы
   - ✅ Легко тестировать
   - ✅ Быстрые тесты (< 1 сек)

4. **Четкая инициализация:**
   - ✅ Понятная последовательность
   - ✅ Диагностическое логирование
   - ✅ Обработка ошибок

5. **Централизация:**
   - ✅ Состояние: ApplicationStateManager
   - ✅ Конфигурация: UnifiedConfigLoader
   - ✅ Ошибки: ErrorHandler

---

### 8.2 Метрики качества

| Критерий | Целевое значение | Текущее значение |
|----------|------------------|------------------|
| Размер модуля | ≤ 500 строк | 3260 строк ❌ |
| Размер интеграции | ≤ 500 строк | 3260 строк ❌ |
| Источники истины | 1 | 4 ❌ |
| Локальные флаги | 0 | 15+ ❌ |
| Время теста | < 1 сек | > 10 сек ❌ |
| Изоляция | 100% | 0% ❌ |

---

## 🎯 Заключение

**Критерии идеальной архитектуры:**
1. ✅ Разделение ответственности (модули ≤ 500 строк)
2. ✅ Единый источник истины (только ApplicationStateManager)
3. ✅ Изоляция и тестируемость (легко тестировать)
4. ✅ Четкая инициализация (понятная последовательность)
5. ✅ Централизация (состояние, конфигурация, ошибки)

**Требования к централизации:**
1. ✅ Состояние: только ApplicationStateManager
2. ✅ Конфигурация: только UnifiedConfigLoader
3. ✅ Ошибки: только ErrorHandler

**Правильное распределение:**
1. ✅ Модули: одна задача
2. ✅ Интеграции: только координация
3. ✅ Core: инфраструктура

**Правильное соединение:**
1. ✅ Модули → Интеграции → EventBus
2. ✅ Интеграции → ApplicationStateManager
3. ✅ Интеграции → ErrorHandler

**Правильная интеграция:**
1. ✅ SimpleModuleCoordinator (порядок инициализации)
2. ✅ EventBus (контракты, приоритеты)
3. ✅ UnifiedConfigLoader (конфигурация)

