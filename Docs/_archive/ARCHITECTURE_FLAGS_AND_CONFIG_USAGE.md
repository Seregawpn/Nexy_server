# 🚩 Использование Флагов и Конфигураций

**Дата:** 2025-12-13  
**Статус:** Полное руководство по использованию флагов и конфигураций

---

## 📊 Часть 1: Feature Flags и Kill-Switches

### 1.1 Источники флагов

**Требование REQ-FLAGS-SOURCE-001: Источники feature flags**
- ✅ `config/unified_config.yaml` — основной источник
- ✅ Переменные окружения (`os.getenv()`) — переопределение
- ✅ Приоритет: env переменные > unified_config.yaml

**Пример:**
```python
class AVFManager:
    def __init__(self, config: AVFConfig):
        self._config = config
        # ✅ Проверка feature flag из unified_config
        avf_enabled = config.enabled
        
        # ✅ Проверка kill-switch из env переменных (приоритет выше)
        ks_avf_enabled = os.getenv("NEXY_KS_AVF_ENABLED", "false").lower() == "true"
        
        # ✅ Проверка kill-switch из unified_config (fallback)
        if not ks_avf_enabled:
            loader = UnifiedConfigLoader()
            ks_config = loader.get_audio_avf_config().get("ks_avf", {})
            ks_avf_enabled = ks_config.get("enabled", False)
        
        # ✅ Финальное решение
        self._enabled = avf_enabled and not ks_avf_enabled
```

**Проверка:**
- [ ] Feature flags из unified_config.yaml
- [ ] Kill-switches из env переменных (приоритет)
- [ ] Kill-switches из unified_config.yaml (fallback)
- [ ] Приоритет: env > unified_config

---

### 1.2 Загрузка и проверка флагов

**Требование REQ-FLAGS-LOAD-001: Загрузка feature flags**
- ✅ Загрузка через `UnifiedConfigLoader`
- ✅ Проверка env переменных
- ✅ Логирование загрузки флагов
- ✅ Валидация значений флагов

**Пример:**
```python
class VoiceRecognitionIntegration:
    async def initialize(self) -> bool:
        logger.info("🔍 [VOICE] Загрузка feature flags...")
        
        # ✅ Загрузка через UnifiedConfigLoader
        loader = UnifiedConfigLoader()
        config_dict = loader._load_config()
        
        # ✅ Проверка feature flag для AVF
        audio_config = loader.get_audio_config_object()
        avf_config = loader.get_audio_avf_config()
        avf_enabled = avf_config.get("enabled", False)
        
        # ✅ Проверка kill-switch из env (приоритет)
        disable_avf_env = os.getenv("NEXY_KS_AVF_ENABLED", "false").lower() == "true"
        
        # ✅ Проверка kill-switch из unified_config (fallback)
        ks_avf_enabled = avf_config.get("ks_avf", {}).get("enabled", False)
        
        # ✅ Финальное решение
        self._use_avf = avf_enabled and not ks_avf_enabled and not disable_avf_env
        
        logger.info(f"🔍 [VOICE] Feature flags загружены: _use_avf={self._use_avf}")
        logger.info(f"🔍 [VOICE] Источники: avf_enabled={avf_enabled}, ks_avf_enabled={ks_avf_enabled}, disable_avf_env={disable_avf_env}")
        
        return True
```

**Проверка:**
- [ ] Загрузка через UnifiedConfigLoader
- [ ] Проверка env переменных
- [ ] Логирование загрузки
- [ ] Валидация значений

---

### 1.3 Использование флагов в коде

**Требование REQ-FLAGS-USE-001: Использование feature flags**
- ✅ Проверка флагов перед использованием функциональности
- ✅ Логирование использования флагов
- ✅ Fallback на legacy путь при отключенном флаге
- ✅ Документация флагов в `Docs/FEATURE_FLAGS.md`

**Пример:**
```python
class VoiceRecognitionIntegration:
    async def _on_recording_start(self, event: Dict[str, Any]):
        # ✅ Проверка feature flag перед использованием
        if self._use_avf and self._avf_engine is not None:
            logger.info("✅ [VOICE] Использование AVF (feature flag включен)")
            # Новая логика с AVF
            device_info = await self._avf_manager.activate(duration_sec=1.0)
        else:
            logger.warning("⚠️ [VOICE] AVF отключен, используем legacy путь")
            # Legacy логика (fallback)
            # ...
```

**Проверка:**
- [ ] Проверка флагов перед использованием
- [ ] Логирование использования
- [ ] Fallback на legacy путь
- [ ] Документация в Docs/FEATURE_FLAGS.md

---

## 📊 Часть 2: Конфигурации

### 2.1 Загрузка конфигурации

**Требование REQ-CONFIG-LOAD-001: Загрузка через UnifiedConfigLoader**
- ✅ Все загрузки конфигурации через `UnifiedConfigLoader`
- ✅ Кэширование конфигурации
- ✅ Логирование загрузки
- ✅ Валидация через схемы

**Пример:**
```python
class AVFManager:
    @classmethod
    def from_unified_config(cls, loader: UnifiedConfigLoader) -> "AVFManager":
        """Создание из unified_config"""
        logger.info("🔍 [AVF] Загрузка конфигурации из unified_config...")
        
        # ✅ Загрузка через UnifiedConfigLoader
        avf_config = loader.get_audio_avf_config()
        
        # ✅ Валидация через схему
        validated_config = validate_avf_config(avf_config)
        
        # ✅ Создание конфигурации
        config = AVFConfig.from_dict(validated_config)
        
        logger.info("✅ [AVF] Конфигурация загружена и валидирована")
        return cls(config)
```

**Проверка:**
- [ ] Загрузка через UnifiedConfigLoader
- [ ] Кэширование конфигурации
- [ ] Логирование загрузки
- [ ] Валидация через схемы

---

### 2.2 Использование конфигурации

**Требование REQ-CONFIG-USE-001: Использование конфигурации**
- ✅ Конфигурация через конструктор модуля/интеграции
- ✅ Нет хардкода значений
- ✅ Использование значений из конфигурации
- ✅ Логирование использования конфигурации

**Пример:**
```python
class AVFManager:
    def __init__(self, config: AVFConfig):
        # ✅ Конфигурация через конструктор
        self._config = config
        logger.info(f"🔍 [AVF] Конфигурация: enabled={config.enabled}, input_format={config.input_format}")
    
    async def activate(self, duration_sec: float = 1.0) -> DeviceInfo:
        # ✅ Использование значений из конфигурации
        buffer_size_ms = self._config.buffer_size_ms
        input_format = self._config.input_format
        
        logger.info(f"🔍 [AVF] Использование конфигурации: buffer_size_ms={buffer_size_ms}, input_format={input_format}")
        
        # Логика активации с использованием конфигурации
        # ...
```

**Проверка:**
- [ ] Конфигурация через конструктор
- [ ] Нет хардкода значений
- [ ] Использование значений из конфигурации
- [ ] Логирование использования

---

### 2.3 Создание конфигурации из unified_config

**Требование REQ-CONFIG-CREATE-001: Создание из unified_config**
- ✅ Метод `from_unified_config()` для создания конфигурации
- ✅ Валидация через схемы
- ✅ Обработка ошибок валидации
- ✅ Логирование создания

**Пример:**
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
        logger.info("🔍 [AVF] Создание конфигурации из unified_config...")
        
        try:
            # ✅ Загрузка из unified_config
            avf_config = loader.get_audio_avf_config()
            
            # ✅ Валидация через схему
            validated_config = validate_avf_config(avf_config)
            
            # ✅ Создание конфигурации
            config = cls(
                enabled=validated_config.get("enabled", True),
                input_format=validated_config.get("input_format", "16kHz, mono, int16"),
                buffer_size_ms=validated_config.get("buffer_size_ms", 100),
                enable_hardware_optimization=validated_config.get("enable_hardware_optimization", True)
            )
            
            logger.info("✅ [AVF] Конфигурация создана из unified_config")
            return config
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка создания конфигурации: {e}")
            logger.exception("❌ [AVF] Детали исключения:")
            # ✅ Fallback на значения по умолчанию
            return cls()
```

**Проверка:**
- [ ] Метод from_unified_config() создан
- [ ] Валидация через схемы
- [ ] Обработка ошибок
- [ ] Логирование создания

---

## 📊 Часть 3: Полная Последовательность Загрузки

### 3.1 Последовательность загрузки флагов и конфигурации

**Требование REQ-LOAD-SEQ-001: Последовательность загрузки**
- ✅ 1. Загрузка unified_config через UnifiedConfigLoader
- ✅ 2. Проверка env переменных (приоритет)
- ✅ 3. Проверка unified_config (fallback)
- ✅ 4. Валидация через схемы
- ✅ 5. Создание конфигурации
- ✅ 6. Логирование загрузки

**Пример:**
```python
class VoiceRecognitionIntegration:
    async def initialize(self) -> bool:
        logger.info("🔍 [VOICE] Начало загрузки флагов и конфигурации...")
        
        # ✅ Шаг 1: Загрузка unified_config
        loader = UnifiedConfigLoader()
        logger.info("✅ [VOICE] UnifiedConfigLoader создан")
        
        # ✅ Шаг 2: Проверка env переменных (приоритет)
        disable_avf_env = os.getenv("NEXY_KS_AVF_ENABLED", "false").lower() == "true"
        logger.info(f"🔍 [VOICE] Env переменные: NEXY_KS_AVF_ENABLED={disable_avf_env}")
        
        # ✅ Шаг 3: Проверка unified_config (fallback)
        avf_config = loader.get_audio_avf_config()
        avf_enabled = avf_config.get("enabled", False)
        ks_avf_enabled = avf_config.get("ks_avf", {}).get("enabled", False)
        logger.info(f"🔍 [VOICE] Unified config: avf_enabled={avf_enabled}, ks_avf_enabled={ks_avf_enabled}")
        
        # ✅ Шаг 4: Валидация через схемы
        validated_config = validate_avf_config(avf_config)
        logger.info("✅ [VOICE] Конфигурация валидирована")
        
        # ✅ Шаг 5: Создание конфигурации
        avf_config_obj = AVFConfig.from_unified_config(loader)
        google_config_obj = GoogleConfig.from_unified_config(loader)
        logger.info("✅ [VOICE] Конфигурации созданы")
        
        # ✅ Шаг 6: Финальное решение
        self._use_avf = avf_enabled and not ks_avf_enabled and not disable_avf_env
        logger.info(f"✅ [VOICE] Финальное решение: _use_avf={self._use_avf}")
        
        # ✅ Шаг 7: Создание менеджеров
        self._avf_manager = AVFManager(avf_config_obj)
        self._google_manager = GoogleManager(google_config_obj)
        logger.info("✅ [VOICE] Менеджеры созданы")
        
        return True
```

**Проверка:**
- [ ] Последовательность загрузки соблюдена
- [ ] Приоритеты учтены (env > unified_config)
- [ ] Валидация выполнена
- [ ] Логирование на каждом этапе

---

## 📊 Часть 4: Конкретные Примеры Использования

### 4.1 Пример: AVF Feature Flag

**Текущая реализация:**
```python
# integration/integrations/voice_recognition_integration.py (строки 228-280)
async def initialize(self) -> bool:
    try:
        # ✅ Загрузка unified_config
        loader = UnifiedConfigLoader()
        audio_config = loader.get_audio_config_object()
        avf_config = loader.get_audio_avf_config()
        
        # ✅ Проверка feature flag
        avf_enabled = avf_config.get("enabled", False)
        
        # ✅ Проверка kill-switch из env (приоритет)
        disable_avf_env = os.getenv("NEXY_KS_AVF_ENABLED", "false").lower() == "true"
        
        # ✅ Проверка kill-switch из unified_config (fallback)
        ks_avf_enabled = avf_config.get("ks_avf", {}).get("enabled", False)
        
        # ✅ Финальное решение
        self._use_avf = avf_enabled and not ks_avf_enabled and not disable_avf_env
        
        if self._use_avf:
            self._avf_engine = AVFAudioEngine(audio_config)
    except Exception as e:
        self._use_avf = False
```

**Идеальная реализация:**
```python
# modules/audio_avf/core/avf_manager.py
class AVFManager:
    def __init__(self, config: AVFConfig):
        self._config = config
        # ✅ Проверка feature flag
        self._enabled = self._check_feature_flag()
    
    def _check_feature_flag(self) -> bool:
        """Проверка feature flag с учетом приоритетов"""
        # ✅ Проверка kill-switch из env (приоритет)
        ks_env = os.getenv("NEXY_KS_AVF_ENABLED", "false").lower() == "true"
        if ks_env:
            logger.warning("⚠️ [AVF] Kill-switch включен через env переменную")
            return False
        
        # ✅ Проверка kill-switch из unified_config (fallback)
        loader = UnifiedConfigLoader()
        ks_config = loader.get_audio_avf_config().get("ks_avf", {})
        ks_unified = ks_config.get("enabled", False)
        if ks_unified:
            logger.warning("⚠️ [AVF] Kill-switch включен через unified_config")
            return False
        
        # ✅ Проверка feature flag
        return self._config.enabled
```

---

### 4.2 Пример: Google Конфигурация

**Идеальная реализация:**
```python
# modules/audio_google/core/google_manager.py
@dataclass
class GoogleConfig:
    language: str = "en-US"
    phrase_time_limit: Optional[float] = None
    energy_threshold: int = 4000
    pause_threshold: float = 0.8
    
    @classmethod
    def from_unified_config(cls, loader: UnifiedConfigLoader) -> "GoogleConfig":
        """Создание из unified_config"""
        logger.info("🔍 [Google] Загрузка конфигурации из unified_config...")
        
        try:
            # ✅ Загрузка из unified_config
            voice_config = loader.get_voice_recognition_config()
            
            # ✅ Валидация через схему
            validated_config = validate_google_config(voice_config)
            
            # ✅ Создание конфигурации
            config = cls(
                language=validated_config.get("language", "en-US"),
                phrase_time_limit=validated_config.get("phrase_time_limit"),
                energy_threshold=validated_config.get("energy_threshold", 4000),
                pause_threshold=validated_config.get("pause_threshold", 0.8)
            )
            
            logger.info(f"✅ [Google] Конфигурация создана: language={config.language}")
            return config
        except Exception as e:
            logger.error(f"❌ [Google] Ошибка создания конфигурации: {e}")
            logger.exception("❌ [Google] Детали исключения:")
            # ✅ Fallback на значения по умолчанию
            return cls()

class GoogleManager:
    def __init__(self, config: GoogleConfig):
        # ✅ Конфигурация через конструктор
        self._config = config
        logger.info(f"🔍 [Google] Конфигурация: language={config.language}, energy_threshold={config.energy_threshold}")
    
    async def initialize(self) -> bool:
        # ✅ Использование значений из конфигурации
        self._recognizer.energy_threshold = self._config.energy_threshold
        self._recognizer.pause_threshold = self._config.pause_threshold
        logger.info(f"✅ [Google] Параметры настроены из конфигурации")
```

---

## 📊 Часть 5: Чек-лист Использования Флагов и Конфигураций

### 5.1 Чек-лист feature flags

- [ ] Feature flags загружаются через UnifiedConfigLoader
- [ ] Kill-switches проверяются из env переменных (приоритет)
- [ ] Kill-switches проверяются из unified_config (fallback)
- [ ] Приоритет: env > unified_config
- [ ] Логирование загрузки флагов
- [ ] Валидация значений флагов
- [ ] Проверка флагов перед использованием
- [ ] Fallback на legacy путь при отключенном флаге
- [ ] Документация в Docs/FEATURE_FLAGS.md

---

### 5.2 Чек-лист конфигурации

- [ ] Конфигурация загружается через UnifiedConfigLoader
- [ ] Метод from_unified_config() создан
- [ ] Валидация через схемы
- [ ] Кэширование конфигурации
- [ ] Логирование загрузки
- [ ] Конфигурация через конструктор
- [ ] Нет хардкода значений
- [ ] Использование значений из конфигурации
- [ ] Логирование использования
- [ ] Обработка ошибок валидации

---

### 5.3 Чек-лист последовательности загрузки

- [ ] Загрузка unified_config через UnifiedConfigLoader
- [ ] Проверка env переменных (приоритет)
- [ ] Проверка unified_config (fallback)
- [ ] Валидация через схемы
- [ ] Создание конфигурации
- [ ] Логирование на каждом этапе
- [ ] Обработка ошибок

---

## 📊 Часть 6: Требования к Импорту и Использованию

### 6.1 Импорт UnifiedConfigLoader

**Требование REQ-IMPORT-CONFIG-001: Импорт UnifiedConfigLoader**
- ✅ Импорт в начале файла
- ✅ Использование только через UnifiedConfigLoader
- ✅ Нет прямого доступа к файлам конфигурации

**Пример:**
```python
# ✅ ПРАВИЛЬНО: Импорт в начале файла
from config.unified_config_loader import UnifiedConfigLoader

class AVFManager:
    @classmethod
    def from_unified_config(cls, loader: UnifiedConfigLoader) -> "AVFManager":
        # ✅ Использование через UnifiedConfigLoader
        avf_config = loader.get_audio_avf_config()
        return cls(AVFConfig.from_dict(avf_config))

# ❌ НЕПРАВИЛЬНО: Прямой доступ к файлам
import yaml
with open("config/unified_config.yaml") as f:
    config = yaml.safe_load(f)  # ❌ ЗАПРЕЩЕНО
```

**Проверка:**
- [ ] Импорт в начале файла
- [ ] Использование только через UnifiedConfigLoader
- [ ] Нет прямого доступа к файлам

---

### 6.2 Импорт os для env переменных

**Требование REQ-IMPORT-ENV-001: Импорт os для env переменных**
- ✅ Импорт `os` в начале файла
- ✅ Использование `os.getenv()` для проверки env переменных
- ✅ Логирование проверки env переменных

**Пример:**
```python
# ✅ ПРАВИЛЬНО: Импорт os в начале файла
import os
from config.unified_config_loader import UnifiedConfigLoader

class AVFManager:
    def _check_feature_flag(self) -> bool:
        # ✅ Использование os.getenv()
        ks_env = os.getenv("NEXY_KS_AVF_ENABLED", "false").lower() == "true"
        logger.info(f"🔍 [AVF] Env переменная NEXY_KS_AVF_ENABLED={ks_env}")
        return not ks_env
```

**Проверка:**
- [ ] Импорт os в начале файла
- [ ] Использование os.getenv()
- [ ] Логирование проверки

---

### 6.3 Импорт типов конфигурации

**Требование REQ-IMPORT-TYPES-001: Импорт типов конфигурации**
- ✅ Импорт типов конфигурации из модуля
- ✅ Использование типов для валидации
- ✅ Документация типов

**Пример:**
```python
# ✅ ПРАВИЛЬНО: Импорт типов конфигурации
from modules.audio_avf.core.types import AVFConfig, DeviceInfo
from modules.audio_google.core.types import GoogleConfig

class VoiceRecognitionIntegration:
    def __init__(self, ...):
        # ✅ Использование типов
        avf_config = AVFConfig.from_unified_config(loader)
        google_config = GoogleConfig.from_unified_config(loader)
        
        self._avf_manager = AVFManager(avf_config)
        self._google_manager = GoogleManager(google_config)
```

**Проверка:**
- [ ] Импорт типов конфигурации
- [ ] Использование типов для валидации
- [ ] Документация типов

---

## 📊 Часть 7: Полная Последовательность Импорта и Использования

### 7.1 Последовательность импорта

**Требование REQ-IMPORT-SEQ-001: Порядок импортов**
- ✅ 1. Стандартные библиотеки (os, asyncio, logging)
- ✅ 2. Сторонние библиотеки
- ✅ 3. Core компоненты (EventBus, StateManager, ErrorHandler)
- ✅ 4. Конфигурация (UnifiedConfigLoader)
- ✅ 5. Типы конфигурации (AVFConfig, GoogleConfig)
- ✅ 6. Модули (AVFManager, GoogleManager)

**Пример:**
```python
# ✅ ПРАВИЛЬНО: Порядок импортов
# 1. Стандартные библиотеки
import os
import asyncio
import logging
from typing import Dict, Any, Optional

# 2. Сторонние библиотеки
import speech_recognition as sr

# 3. Core компоненты
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler

# 4. Конфигурация
from config.unified_config_loader import UnifiedConfigLoader

# 5. Типы конфигурации
from modules.audio_avf.core.types import AVFConfig, DeviceInfo
from modules.audio_google.core.types import GoogleConfig

# 6. Модули
from modules.audio_avf.core.avf_manager import AVFManager
from modules.audio_google.core.google_manager import GoogleManager
```

**Проверка:**
- [ ] Порядок импортов соблюден
- [ ] Группировка импортов
- [ ] Нет циклических зависимостей

---

### 7.2 Последовательность использования

**Требование REQ-USE-SEQ-001: Порядок использования**
- ✅ 1. Создание UnifiedConfigLoader
- ✅ 2. Загрузка конфигурации
- ✅ 3. Проверка env переменных
- ✅ 4. Валидация конфигурации
- ✅ 5. Создание конфигурации
- ✅ 6. Создание менеджеров
- ✅ 7. Использование менеджеров

**Пример:**
```python
class VoiceRecognitionIntegration:
    async def initialize(self) -> bool:
        # ✅ Шаг 1: Создание UnifiedConfigLoader
        loader = UnifiedConfigLoader()
        
        # ✅ Шаг 2: Загрузка конфигурации
        avf_config_dict = loader.get_audio_avf_config()
        google_config_dict = loader.get_voice_recognition_config()
        
        # ✅ Шаг 3: Проверка env переменных
        disable_avf_env = os.getenv("NEXY_KS_AVF_ENABLED", "false").lower() == "true"
        
        # ✅ Шаг 4: Валидация конфигурации
        validated_avf_config = validate_avf_config(avf_config_dict)
        validated_google_config = validate_google_config(google_config_dict)
        
        # ✅ Шаг 5: Создание конфигурации
        avf_config = AVFConfig.from_unified_config(loader)
        google_config = GoogleConfig.from_unified_config(loader)
        
        # ✅ Шаг 6: Создание менеджеров
        self._avf_manager = AVFManager(avf_config)
        self._google_manager = GoogleManager(google_config)
        
        # ✅ Шаг 7: Использование менеджеров
        await self._avf_manager.initialize()
        await self._google_manager.initialize()
        
        return True
```

**Проверка:**
- [ ] Порядок использования соблюден
- [ ] Логирование на каждом этапе
- [ ] Обработка ошибок

---

## 📊 Часть 8: Регистрация Флагов

### 8.1 Регистрация в Docs/FEATURE_FLAGS.md

**Требование REQ-FLAGS-REG-001: Регистрация флагов**
- ✅ Все feature flags зарегистрированы в `Docs/FEATURE_FLAGS.md`
- ✅ Все kill-switches зарегистрированы в `Docs/FEATURE_FLAGS.md`
- ✅ Документация включает: название, описание, источник, использование

**Пример:**
```markdown
# Docs/FEATURE_FLAGS.md

## AVF Feature Flags

### NEXY_FEATURE_AVF_V2
- **Описание**: Включить AVF аудиосистему (v2)
- **Источник**: `config/unified_config.yaml` → `audio.avf.enabled`
- **Использование**: `AVFManager._check_feature_flag()`
- **Kill-switch**: `NEXY_KS_AVF_ENABLED` (env или unified_config)

### NEXY_KS_AVF_ENABLED
- **Описание**: Kill-switch для мгновенного отключения AVF
- **Источник**: 
  - Приоритет: `os.getenv("NEXY_KS_AVF_ENABLED")`
  - Fallback: `config/unified_config.yaml` → `audio.ks_avf.enabled`
- **Использование**: `AVFManager._check_feature_flag()`
```

**Проверка:**
- [ ] Все флаги зарегистрированы
- [ ] Документация включает все поля
- [ ] Ссылки на использование

---

## ✅ Часть 9: Итоговые Требования

### 9.1 Обязательные требования

1. **Feature Flags:**
   - ✅ Загрузка через UnifiedConfigLoader
   - ✅ Проверка env переменных (приоритет)
   - ✅ Проверка unified_config (fallback)
   - ✅ Регистрация в Docs/FEATURE_FLAGS.md

2. **Конфигурация:**
   - ✅ Загрузка через UnifiedConfigLoader
   - ✅ Метод from_unified_config() создан
   - ✅ Валидация через схемы
   - ✅ Конфигурация через конструктор

3. **Импорт:**
   - ✅ Порядок импортов соблюден
   - ✅ Импорт UnifiedConfigLoader
   - ✅ Импорт os для env переменных
   - ✅ Импорт типов конфигурации

4. **Использование:**
   - ✅ Последовательность загрузки соблюдена
   - ✅ Логирование на каждом этапе
   - ✅ Обработка ошибок
   - ✅ Fallback на значения по умолчанию

---

### 9.2 Метрики использования

| Требование | Целевое значение | Проверка |
|------------|------------------|----------|
| Загрузка через UnifiedConfigLoader | 100% | ✅ |
| Проверка env переменных | 100% | ✅ |
| Валидация через схемы | 100% | ✅ |
| Регистрация в Docs/FEATURE_FLAGS.md | 100% | ✅ |
| Логирование загрузки | 100% | ✅ |

---

## 🎯 Заключение

**Все аспекты использования флагов и конфигураций учтены:**

1. ✅ **Загрузка** — через UnifiedConfigLoader
2. ✅ **Проверка** — env переменные (приоритет) > unified_config (fallback)
3. ✅ **Валидация** — через схемы
4. ✅ **Использование** — через конструктор модулей/интеграций
5. ✅ **Импорт** — правильный порядок и группировка
6. ✅ **Регистрация** — в Docs/FEATURE_FLAGS.md
7. ✅ **Логирование** — на каждом этапе

**Все требования проверяемы через чек-листы.**

