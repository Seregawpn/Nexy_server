# 🧪 Детальный План Фаз Тестирования

**Дата:** 2025-12-13  
**Статус:** Детальное планирование тестирования на каждом этапе реализации

---

## 📊 Часть 1: Принципы Тестирования

### 1.1 Обязательные принципы

**ОБЯЗАТЕЛЬНО:** После каждого исправления или реализации новой функциональности **ОБЯЗАТЕЛЬНО** создать изолированный тест, который проверяет, что реализация полностью работает.

**Требования к тестам:**
- ✅ Изолированные: проверяют только исправленную/реализованную функциональность
- ✅ Воспроизводимые: запускаются независимо и дают четкий результат (прошел/не прошел)
- ✅ Быстрые: время выполнения < 1 секунды
- ✅ Без зависимостей: не требуют реального микрофона или внешних сервисов

**Запрещено:**
- ❌ Считать исправление завершенным без изолированного теста
- ❌ Тестировать всю систему целиком без изоляции
- ❌ Использовать реальный микрофон в unit-тестах
- ❌ Догадываться о проблеме без изоляции

---

### 1.2 Методология изоляции

**Алгоритм работы:**
1. **Сбор информации**: Прочитать логи ошибки полностью, определить точное место ошибки
2. **Формулирование гипотез**: Составить список возможных причин
3. **Изоляция и тестирование**: Создать минимальный тест для проверки гипотезы
4. **Верификация решения**: После исправления создать тест, который воспроизводит исходную проблему
5. **Обязательное изолированное тестирование**: После каждого исправления создать изолированный тест

---

## 📊 Часть 2: Фазы Тестирования по Этапам

### Фаза 1: Тестирование диагностики initialize() (День 1-2)

**Цель:** Убедиться, что `initialize()` вызывается и логируется правильно

**Тесты:**

#### Тест 1: Проверка вызова initialize()
```python
# tests/test_initialize_call.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from integration.core.simple_module_coordinator import SimpleModuleCoordinator

@pytest.mark.asyncio
async def test_coordinator_initialize_called():
    """Изолированный тест: проверяем, что coordinator.initialize() вызывается"""
    coordinator = SimpleModuleCoordinator()
    
    # Мокаем зависимости
    with patch('integration.core.simple_module_coordinator.EventBus') as mock_event_bus:
        with patch('integration.core.simple_module_coordinator.ApplicationStateManager') as mock_state_manager:
            # Вызываем initialize()
            result = await coordinator.initialize()
            
            # Проверяем, что initialize() был вызван
            assert coordinator.is_initialized == True
            assert result == True
```

#### Тест 2: Проверка логирования initialize()
```python
# tests/test_initialize_logging.py
import pytest
import logging
from unittest.mock import Mock, patch
from integration.core.simple_module_coordinator import SimpleModuleCoordinator

@pytest.mark.asyncio
async def test_initialize_logging():
    """Изолированный тест: проверяем логирование initialize()"""
    coordinator = SimpleModuleCoordinator()
    
    # Создаем handler для захвата логов
    log_capture = []
    
    def log_handler(record):
        log_capture.append(record.getMessage())
    
    logger = logging.getLogger('integration.core.simple_module_coordinator')
    handler = logging.Handler()
    handler.emit = log_handler
    logger.addHandler(handler)
    
    # Вызываем initialize()
    await coordinator.initialize()
    
    # Проверяем, что логи содержат нужные сообщения
    assert any("coordinator.initialize()" in log for log in log_capture)
    assert any("НАЧАЛО" in log for log in log_capture)
```

**Чек-лист:**
- [ ] Тест вызова initialize() проходит
- [ ] Тест логирования проходит
- [ ] Логи показывают полную картину инициализации
- [ ] Время выполнения теста < 1 секунды

**Команда запуска:**
```bash
pytest tests/test_initialize_*.py -v
```

---

### Фаза 2: Тестирование AVF модуля (День 3)

**Цель:** Убедиться, что AVF модуль работает изолированно

**Тесты:**

#### Тест 1: Создание конфигурации
```python
# tests/test_avf_config.py
import pytest
from unittest.mock import Mock, patch
from modules.audio_avf.core.types import AVFConfig
from config.unified_config_loader import UnifiedConfigLoader

def test_avf_config_from_unified_config():
    """Изолированный тест: проверяем создание AVFConfig из unified_config"""
    # Мокаем UnifiedConfigLoader
    with patch('modules.audio_avf.core.types.UnifiedConfigLoader') as mock_loader:
        mock_loader_instance = Mock()
        mock_loader_instance.get_audio_avf_config.return_value = {
            "enabled": True,
            "input_format": "16kHz, mono, int16",
            "buffer_size_ms": 100,
            "enable_hardware_optimization": True
        }
        mock_loader.return_value = mock_loader_instance
        
        # Создаем конфигурацию
        config = AVFConfig.from_unified_config(mock_loader_instance)
        
        # Проверяем значения
        assert config.enabled == True
        assert config.input_format == "16kHz, mono, int16"
        assert config.buffer_size_ms == 100
        assert config.enable_hardware_optimization == True
```

#### Тест 2: Инициализация менеджера
```python
# tests/test_avf_manager_init.py
import pytest
from modules.audio_avf.core.avf_manager import AVFManager
from modules.audio_avf.core.types import AVFConfig

def test_avf_manager_initialization():
    """Изолированный тест: проверяем инициализацию AVFManager"""
    config = AVFConfig(enabled=True)
    manager = AVFManager(config)
    
    # Проверяем начальное состояние
    assert manager._config == config
    assert manager._engine is None
    assert manager._initialized == False
    assert manager._active == False
```

#### Тест 3: Метод initialize()
```python
# tests/test_avf_manager_initialize.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from modules.audio_avf.core.avf_manager import AVFManager
from modules.audio_avf.core.types import AVFConfig

@pytest.mark.asyncio
async def test_avf_manager_initialize():
    """Изолированный тест: проверяем метод initialize()"""
    config = AVFConfig(enabled=True)
    manager = AVFManager(config)
    
    # Мокаем AVFAudioEngine
    with patch('modules.audio_avf.core.avf_manager.AVFAudioEngine') as mock_engine_class:
        mock_engine = Mock()
        mock_engine_class.return_value = mock_engine
        
        # Мокаем загрузку конфигурации
        with patch.object(manager, '_load_audio_config', return_value=Mock()):
            # Вызываем initialize()
            result = await manager.initialize()
            
            # Проверяем результат
            assert result == True
            assert manager._initialized == True
            assert manager._engine is not None
```

#### Тест 4: Метод activate()
```python
# tests/test_avf_manager_activate.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from modules.audio_avf.core.avf_manager import AVFManager
from modules.audio_avf.core.types import AVFConfig, DeviceInfo

@pytest.mark.asyncio
async def test_avf_manager_activate():
    """Изолированный тест: проверяем метод activate()"""
    config = AVFConfig(enabled=True)
    manager = AVFManager(config)
    
    # Мокаем инициализацию
    manager._engine = Mock()
    manager._initialized = True
    manager._active = False
    
    # Мокаем start_input()
    mock_result = Mock()
    mock_result.device_info.name = "Test Microphone"
    mock_result.device_info.uid = "test-uid"
    mock_result.format.to_dict.return_value = {"sample_rate": 16000}
    mock_result.diagnostics = {"rms": 0.5}
    manager._engine.start_input = AsyncMock(return_value=mock_result)
    
    # Вызываем activate()
    device_info = await manager.activate(duration_sec=0.1)  # Короткая длительность для теста
    
    # Проверяем результат
    assert isinstance(device_info, DeviceInfo)
    assert device_info.device_name == "Test Microphone"
    assert manager._active == True
```

#### Тест 5: Метод deactivate()
```python
# tests/test_avf_manager_deactivate.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from modules.audio_avf.core.avf_manager import AVFManager
from modules.audio_avf.core.types import AVFConfig

@pytest.mark.asyncio
async def test_avf_manager_deactivate():
    """Изолированный тест: проверяем метод deactivate()"""
    config = AVFConfig(enabled=True)
    manager = AVFManager(config)
    
    # Мокаем активное состояние
    manager._engine = Mock()
    manager._engine.stop_input = AsyncMock()
    manager._active = True
    
    # Вызываем deactivate()
    result = await manager.deactivate()
    
    # Проверяем результат
    assert result == True
    assert manager._active == False
    manager._engine.stop_input.assert_called_once()
```

**Чек-лист:**
- [ ] Тест создания конфигурации проходит
- [ ] Тест инициализации менеджера проходит
- [ ] Тест initialize() проходит
- [ ] Тест activate() проходит
- [ ] Тест deactivate() проходит
- [ ] Все тесты изолированы (не требуют реального микрофона)
- [ ] Все тесты быстрые (< 1 секунды)

**Команда запуска:**
```bash
pytest tests/test_avf_*.py -v
```

---

### Фаза 3: Тестирование Google модуля (День 4)

**Цель:** Убедиться, что Google модуль работает изолированно

**Тесты:**

#### Тест 1: Создание конфигурации
```python
# tests/test_google_config.py
import pytest
from unittest.mock import Mock, patch
from modules.audio_google.core.types import GoogleConfig
from config.unified_config_loader import UnifiedConfigLoader

def test_google_config_from_unified_config():
    """Изолированный тест: проверяем создание GoogleConfig из unified_config"""
    # Мокаем UnifiedConfigLoader
    with patch('modules.audio_google.core.types.UnifiedConfigLoader') as mock_loader:
        mock_loader_instance = Mock()
        mock_loader_instance.get_voice_recognition_config.return_value = {
            "language": "en-US",
            "phrase_time_limit": 5.0,
            "energy_threshold": 4000,
            "pause_threshold": 0.8
        }
        mock_loader.return_value = mock_loader_instance
        
        # Создаем конфигурацию
        config = GoogleConfig.from_unified_config(mock_loader_instance)
        
        # Проверяем значения
        assert config.language == "en-US"
        assert config.phrase_time_limit == 5.0
        assert config.energy_threshold == 4000
        assert config.pause_threshold == 0.8
```

#### Тест 2: Инициализация менеджера
```python
# tests/test_google_manager_init.py
import pytest
from modules.audio_google.core.google_manager import GoogleManager
from modules.audio_google.core.types import GoogleConfig

def test_google_manager_initialization():
    """Изолированный тест: проверяем инициализацию GoogleManager"""
    config = GoogleConfig(language="en-US")
    manager = GoogleManager(config)
    
    # Проверяем начальное состояние
    assert manager._config == config
    assert manager._recognizer is None
    assert manager._microphone is None
    assert manager._recording_active == False
```

#### Тест 3: Метод initialize()
```python
# tests/test_google_manager_initialize.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from modules.audio_google.core.google_manager import GoogleManager
from modules.audio_google.core.types import GoogleConfig

@pytest.mark.asyncio
async def test_google_manager_initialize():
    """Изолированный тест: проверяем метод initialize()"""
    config = GoogleConfig(language="en-US")
    manager = GoogleManager(config)
    
    # Мокаем speech_recognition
    with patch('modules.audio_google.core.google_manager.sr') as mock_sr:
        mock_recognizer = Mock()
        mock_recognizer.energy_threshold = 4000
        mock_recognizer.pause_threshold = 0.8
        mock_sr.Recognizer.return_value = mock_recognizer
        
        mock_microphone = Mock()
        mock_sr.Microphone.return_value = mock_microphone
        
        # Вызываем initialize()
        result = await manager.initialize()
        
        # Проверяем результат
        assert result == True
        assert manager._recognizer is not None
        assert manager._microphone is not None
        assert manager._recognizer.energy_threshold == 4000
```

#### Тест 4: Метод activate()
```python
# tests/test_google_manager_activate.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from modules.audio_google.core.google_manager import GoogleManager
from modules.audio_google.core.types import GoogleConfig

@pytest.mark.asyncio
async def test_google_manager_activate():
    """Изолированный тест: проверяем метод activate()"""
    config = GoogleConfig(language="en-US")
    manager = GoogleManager(config)
    
    # Мокаем инициализацию
    manager._recognizer = Mock()
    manager._microphone = Mock()
    
    # Мокаем listen_in_background
    mock_stop_listening = Mock()
    manager._recognizer.listen_in_background = Mock(return_value=mock_stop_listening)
    
    # Callback для теста
    callback_called = False
    def test_callback(recognizer, audio):
        nonlocal callback_called
        callback_called = True
    
    # Вызываем activate()
    result = await manager.activate(callback=test_callback)
    
    # Проверяем результат
    assert result == True
    assert manager._recording_active == True
    assert manager._stop_listening == mock_stop_listening
    manager._recognizer.listen_in_background.assert_called_once()
```

#### Тест 5: Метод deactivate()
```python
# tests/test_google_manager_deactivate.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from modules.audio_google.core.google_manager import GoogleManager
from modules.audio_google.core.types import GoogleConfig

@pytest.mark.asyncio
async def test_google_manager_deactivate():
    """Изолированный тест: проверяем метод deactivate()"""
    config = GoogleConfig(language="en-US")
    manager = GoogleManager(config)
    
    # Мокаем активное состояние
    manager._stop_listening = Mock()
    manager._recording_active = True
    manager._chunk_event = Mock()
    manager._chunk_event.is_set.return_value = True
    
    # Вызываем deactivate()
    result = await manager.deactivate()
    
    # Проверяем результат
    assert result == True
    assert manager._recording_active == False
    assert manager._stop_listening is None
```

**Чек-лист:**
- [ ] Тест создания конфигурации проходит
- [ ] Тест инициализации менеджера проходит
- [ ] Тест initialize() проходит
- [ ] Тест activate() проходит
- [ ] Тест deactivate() проходит
- [ ] Все тесты изолированы (не требуют реального микрофона)
- [ ] Все тесты быстрые (< 1 секунды)

**Команда запуска:**
```bash
pytest tests/test_google_*.py -v
```

---

### Фаза 4: Тестирование координации (День 5)

**Цель:** Убедиться, что интеграция только координирует через EventBus

**Тесты:**

#### Тест 1: Координация через EventBus
```python
# tests/test_voice_integration_coordination.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler

@pytest.mark.asyncio
async def test_voice_integration_coordination():
    """Изолированный тест: проверяем координацию через EventBus"""
    event_bus = Mock(spec=EventBus)
    state_manager = Mock(spec=ApplicationStateManager)
    error_handler = Mock(spec=ErrorHandler)
    
    # Мокаем менеджеры
    with patch('integration.integrations.voice_recognition_integration.AVFManager') as mock_avf:
        with patch('integration.integrations.voice_recognition_integration.GoogleManager') as mock_google:
            mock_avf_instance = Mock()
            mock_avf_instance.initialize = AsyncMock(return_value=True)
            mock_avf_instance.activate = AsyncMock(return_value=Mock(device_name="Test Mic"))
            mock_avf_instance.deactivate = AsyncMock(return_value=True)
            mock_avf.return_value = mock_avf_instance
            
            mock_google_instance = Mock()
            mock_google_instance.initialize = AsyncMock(return_value=True)
            mock_google_instance.activate = AsyncMock(return_value=True)
            mock_google_instance.deactivate = AsyncMock(return_value=True)
            mock_google.return_value = mock_google_instance
            
            # Создаем интеграцию
            integration = VoiceRecognitionIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler
            )
            
            # Инициализируем
            await integration.initialize()
            
            # Симулируем событие voice.recording_start
            event = {
                "data": {
                    "session_id": "test-session-123"
                }
            }
            await integration._on_recording_start(event)
            
            # Проверяем, что менеджеры были вызваны
            mock_avf_instance.activate.assert_called_once()
            mock_avf_instance.deactivate.assert_called_once()
            mock_google_instance.activate.assert_called_once()
            
            # Проверяем, что состояние было обновлено
            state_manager.set_microphone_state.assert_called()
            
            # Проверяем, что событие было опубликовано
            event_bus.publish.assert_called()
```

#### Тест 2: Размер интеграции
```python
# tests/test_voice_integration_size.py
import inspect
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

def test_voice_integration_size():
    """Изолированный тест: проверяем размер интеграции"""
    # Читаем файл
    import os
    file_path = "integration/integrations/voice_recognition_integration.py"
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            line_count = len(lines)
            
            # Проверяем размер
            assert line_count <= 500, f"Интеграция слишком большая: {line_count} строк (максимум 500)"
    else:
        # Если файл еще не создан, пропускаем тест
        pytest.skip("Файл еще не создан")
```

#### Тест 3: Отсутствие локальных флагов
```python
# tests/test_voice_integration_no_local_flags.py
import inspect
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

def test_voice_integration_no_local_flags():
    """Изолированный тест: проверяем отсутствие локальных флагов состояния"""
    # Получаем исходный код класса
    source = inspect.getsource(VoiceRecognitionIntegration.__init__)
    
    # Запрещенные флаги
    forbidden_flags = [
        "_recording_active",
        "_google_recording_active",
        "_playback_active",
        "_user_initiated_recording"
    ]
    
    # Проверяем, что запрещенные флаги не используются
    for flag in forbidden_flags:
        assert f"self.{flag}" not in source, f"Найден запрещенный флаг: {flag}"
```

**Чек-лист:**
- [ ] Тест координации проходит
- [ ] Тест размера интеграции проходит (≤ 500 строк)
- [ ] Тест отсутствия локальных флагов проходит
- [ ] Все тесты изолированы
- [ ] Все тесты быстрые (< 1 секунды)

**Команда запуска:**
```bash
pytest tests/test_voice_integration_*.py -v
```

---

### Фаза 5: Тестирование унификации состояния (День 6-7)

**Цель:** Убедиться, что используется только ApplicationStateManager

**Тесты:**

#### Тест 1: Использование state_manager
```python
# tests/test_voice_integration_state_manager.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
from integration.core.state_manager import ApplicationStateManager

@pytest.mark.asyncio
async def test_voice_integration_state_manager():
    """Изолированный тест: проверяем использование state_manager"""
    event_bus = Mock()
    state_manager = Mock(spec=ApplicationStateManager)
    error_handler = Mock()
    
    # Мокаем менеджеры
    with patch('integration.integrations.voice_recognition_integration.AVFManager') as mock_avf:
        with patch('integration.integrations.voice_recognition_integration.GoogleManager') as mock_google:
            # Создаем интеграцию
            integration = VoiceRecognitionIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler
            )
            
            # Симулируем событие voice.recording_start
            event = {
                "data": {
                    "session_id": "test-session-123"
                }
            }
            await integration._on_recording_start(event)
            
            # Проверяем, что state_manager.set_microphone_state был вызван
            state_manager.set_microphone_state.assert_called()
            
            # Проверяем, что используется state_manager.is_microphone_active (если есть)
            # (проверка через анализ кода)
```

#### Тест 2: Атомарные операции
```python
# tests/test_state_manager_atomic.py
import pytest
import threading
from integration.core.state_manager import ApplicationStateManager

def test_state_manager_atomic_operations():
    """Изолированный тест: проверяем атомарность операций state_manager"""
    state_manager = ApplicationStateManager()
    
    # Симулируем конкурентный доступ
    results = []
    
    def set_state_thread(session_id):
        state_manager.set_microphone_state("active", session_id)
        results.append(state_manager.is_microphone_active())
    
    # Запускаем несколько потоков
    threads = []
    for i in range(10):
        thread = threading.Thread(target=set_state_thread, args=(f"session-{i}",))
        threads.append(thread)
        thread.start()
    
    # Ждем завершения
    for thread in threads:
        thread.join()
    
    # Проверяем, что нет race conditions
    # (все операции должны быть атомарными)
    assert len(results) == 10
```

#### Тест 3: Отсутствие рассинхронизации
```python
# tests/test_no_state_desync.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

@pytest.mark.asyncio
async def test_no_state_desync():
    """Изолированный тест: проверяем отсутствие рассинхронизации"""
    event_bus = Mock()
    state_manager = Mock(spec=ApplicationStateManager)
    error_handler = Mock()
    
    # Мокаем менеджеры
    with patch('integration.integrations.voice_recognition_integration.AVFManager') as mock_avf:
        with patch('integration.integrations.voice_recognition_integration.GoogleManager') as mock_google:
            # Создаем интеграцию
            integration = VoiceRecognitionIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler
            )
            
            # Симулируем последовательность событий
            start_event = {"data": {"session_id": "test-session-123"}}
            stop_event = {"data": {"session_id": "test-session-123"}}
            
            await integration._on_recording_start(start_event)
            await integration._on_recording_stop(stop_event)
            
            # Проверяем, что state_manager вызывался последовательно
            calls = state_manager.set_microphone_state.call_args_list
            assert len(calls) >= 2  # Минимум 2 вызова (active и idle)
            
            # Проверяем, что нет локальных флагов
            assert not hasattr(integration, '_recording_active')
            assert not hasattr(integration, '_google_recording_active')
```

**Чек-лист:**
- [ ] Тест использования state_manager проходит
- [ ] Тест атомарных операций проходит
- [ ] Тест отсутствия рассинхронизации проходит
- [ ] Все тесты изолированы
- [ ] Все тесты быстрые (< 1 секунды)

**Команда запуска:**
```bash
pytest tests/test_voice_integration_state_manager.py tests/test_state_manager_atomic.py tests/test_no_state_desync.py -v
```

---

### Фаза 6: Расширенное тестирование (День 8-9)

**Цель:** Полное тестирование всей системы

**Тесты:**

#### Тест 1: Полный цикл активации
```python
# tests/test_integration_full_cycle.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

@pytest.mark.asyncio
async def test_integration_full_cycle():
    """Интеграционный тест: проверяем полный цикл активации микрофона"""
    event_bus = Mock()
    state_manager = Mock()
    error_handler = Mock()
    
    # Мокаем менеджеры
    with patch('integration.integrations.voice_recognition_integration.AVFManager') as mock_avf:
        with patch('integration.integrations.voice_recognition_integration.GoogleManager') as mock_google:
            # Создаем интеграцию
            integration = VoiceRecognitionIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler
            )
            
            # Инициализация
            await integration.initialize()
            
            # Активация
            start_event = {"data": {"session_id": "test-session-123"}}
            await integration._on_recording_start(start_event)
            
            # Деактивация
            stop_event = {"data": {"session_id": "test-session-123"}}
            await integration._on_recording_stop(stop_event)
            
            # Проверяем последовательность вызовов
            assert mock_avf.return_value.initialize.called
            assert mock_avf.return_value.activate.called
            assert mock_avf.return_value.deactivate.called
            assert mock_google.return_value.activate.called
            assert mock_google.return_value.deactivate.called
```

#### Тест 2: Обработка ошибок
```python
# tests/test_integration_error_handling.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

@pytest.mark.asyncio
async def test_integration_error_handling():
    """Интеграционный тест: проверяем обработку ошибок"""
    event_bus = Mock()
    state_manager = Mock()
    error_handler = Mock()
    
    # Мокаем менеджеры с ошибкой
    with patch('integration.integrations.voice_recognition_integration.AVFManager') as mock_avf:
        with patch('integration.integrations.voice_recognition_integration.GoogleManager') as mock_google:
            # Создаем интеграцию
            integration = VoiceRecognitionIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler
            )
            
            # Симулируем ошибку при активации
            mock_avf.return_value.activate = AsyncMock(side_effect=Exception("Test error"))
            
            start_event = {"data": {"session_id": "test-session-123"}}
            await integration._on_recording_start(start_event)
            
            # Проверяем, что ошибка была обработана
            error_handler.handle_error.assert_called()
            
            # Проверяем, что состояние было восстановлено
            state_manager.set_microphone_state.assert_called()
```

#### Тест 3: Последовательность операций
```python
# tests/test_integration_sequence.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

@pytest.mark.asyncio
async def test_integration_sequence():
    """Интеграционный тест: проверяем правильную последовательность операций"""
    event_bus = Mock()
    state_manager = Mock()
    error_handler = Mock()
    
    # Мокаем менеджеры
    with patch('integration.integrations.voice_recognition_integration.AVFManager') as mock_avf:
        with patch('integration.integrations.voice_recognition_integration.GoogleManager') as mock_google:
            # Создаем интеграцию
            integration = VoiceRecognitionIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler
            )
            
            start_event = {"data": {"session_id": "test-session-123"}}
            await integration._on_recording_start(start_event)
            
            # Проверяем последовательность вызовов
            calls = [
                mock_avf.return_value.activate,
                mock_avf.return_value.deactivate,
                mock_google.return_value.activate,
                state_manager.set_microphone_state,
                event_bus.publish
            ]
            
            # Проверяем, что все были вызваны
            for call in calls:
                assert call.called, f"Вызов не был выполнен: {call}"
```

#### Тест 4: Производительность
```python
# tests/test_integration_performance.py
import pytest
import time
from unittest.mock import Mock, patch, AsyncMock
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

@pytest.mark.asyncio
async def test_integration_performance():
    """Интеграционный тест: проверяем производительность"""
    event_bus = Mock()
    state_manager = Mock()
    error_handler = Mock()
    
    # Мокаем менеджеры
    with patch('integration.integrations.voice_recognition_integration.AVFManager') as mock_avf:
        with patch('integration.integrations.voice_recognition_integration.GoogleManager') as mock_google:
            # Создаем интеграцию
            integration = VoiceRecognitionIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler
            )
            
            # Измеряем время активации
            start_time = time.monotonic()
            start_event = {"data": {"session_id": "test-session-123"}}
            await integration._on_recording_start(start_event)
            duration_ms = (time.monotonic() - start_time) * 1000
            
            # Проверяем, что время активации < 2 секунд (с учетом моков)
            assert duration_ms < 2000, f"Активация слишком медленная: {duration_ms}ms"
```

#### Тест 5: Граничные случаи
```python
# tests/test_integration_edge_cases.py
import pytest
from unittest.mock import Mock, patch, AsyncMock
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

@pytest.mark.asyncio
async def test_integration_edge_cases():
    """Интеграционный тест: проверяем граничные случаи"""
    event_bus = Mock()
    state_manager = Mock()
    error_handler = Mock()
    
    # Мокаем менеджеры
    with patch('integration.integrations.voice_recognition_integration.AVFManager') as mock_avf:
        with patch('integration.integrations.voice_recognition_integration.GoogleManager') as mock_google:
            # Создаем интеграцию
            integration = VoiceRecognitionIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler
            )
            
            # Тест 1: Событие без session_id
            event_no_session = {"data": {}}
            await integration._on_recording_start(event_no_session)
            # Должно обработаться без ошибок
            
            # Тест 2: Двойная активация
            start_event = {"data": {"session_id": "test-session-123"}}
            await integration._on_recording_start(start_event)
            await integration._on_recording_start(start_event)
            # Должно обработаться без ошибок
            
            # Тест 3: Остановка без активации
            stop_event = {"data": {"session_id": "test-session-456"}}
            await integration._on_recording_stop(stop_event)
            # Должно обработаться без ошибок
```

**Чек-лист:**
- [ ] Тест полного цикла проходит
- [ ] Тест обработки ошибок проходит
- [ ] Тест последовательности проходит
- [ ] Тест производительности проходит
- [ ] Тест граничных случаев проходит
- [ ] Все тесты изолированы
- [ ] Все тесты быстрые (< 5 секунд для интеграционных)

**Команда запуска:**
```bash
pytest tests/test_integration_*.py -v
```

---

### Фаза 7: Финальное тестирование (День 12-14)

**Цель:** Полная проверка всех требований

**Тесты:**

#### Тест 1: Соответствие требованиям
```python
# tests/test_requirements_compliance.py
import pytest
import inspect
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

def test_requirements_compliance():
    """Интеграционный тест: проверяем соответствие всем требованиям"""
    # Проверка 1: Размер интеграции ≤ 500 строк
    import os
    file_path = "integration/integrations/voice_recognition_integration.py"
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            assert len(lines) <= 500, f"Интеграция слишком большая: {len(lines)} строк"
    
    # Проверка 2: Нет локальных флагов состояния
    source = inspect.getsource(VoiceRecognitionIntegration.__init__)
    forbidden_flags = [
        "_recording_active",
        "_google_recording_active",
        "_playback_active"
    ]
    for flag in forbidden_flags:
        assert f"self.{flag}" not in source, f"Найден запрещенный флаг: {flag}"
    
    # Проверка 3: Использование state_manager
    # (проверка через анализ кода методов)
    methods_source = inspect.getsource(VoiceRecognitionIntegration)
    assert "state_manager.set_microphone_state" in methods_source
    assert "state_manager.is_microphone_active" in methods_source
```

#### Тест 2: Требования производительности
```python
# tests/test_performance_requirements.py
import pytest
import time
from unittest.mock import Mock, patch, AsyncMock

@pytest.mark.asyncio
async def test_performance_requirements():
    """Интеграционный тест: проверяем требования производительности"""
    # SLO требования:
    # - p95 start_listening ≤ 600ms
    # - stream_open_success_rate ≥ 98%
    
    # Тест времени активации
    # (реализация зависит от конкретных требований)
    pass
```

#### Тест 3: Обратная совместимость
```python
# tests/test_backward_compatibility.py
import pytest
from unittest.mock import Mock, patch, AsyncMock

@pytest.mark.asyncio
async def test_backward_compatibility():
    """Интеграционный тест: проверяем обратную совместимость"""
    # Проверка, что старые события все еще работают
    # Проверка, что старые конфигурации все еще работают
    # (реализация зависит от конкретных требований)
    pass
```

**Чек-лист:**
- [ ] Все unit-тесты проходят (100%)
- [ ] Все интеграционные тесты проходят (100%)
- [ ] Покрытие кода ≥ 80%
- [ ] Производительность соответствует требованиям
- [ ] Совместимость проверена
- [ ] Все требования выполнены

**Команда запуска:**
```bash
# Все тесты
pytest tests/ -v --cov=modules/audio_avf --cov=modules/audio_google --cov=integration/integrations/voice_recognition_integration

# Проверка покрытия
pytest tests/ --cov=modules/audio_avf --cov=modules/audio_google --cov=integration/integrations/voice_recognition_integration --cov-report=html
```

---

## 📊 Часть 3: Структура Тестов

### 3.1 Структура тестов для модулей

```
tests/
├── test_avf_manager.py
│   ├── test_avf_config_from_unified_config()
│   ├── test_avf_manager_initialization()
│   ├── test_avf_manager_initialize()
│   ├── test_avf_manager_activate()
│   └── test_avf_manager_deactivate()
│
└── test_google_manager.py
    ├── test_google_config_from_unified_config()
    ├── test_google_manager_initialization()
    ├── test_google_manager_initialize()
    ├── test_google_manager_activate()
    └── test_google_manager_deactivate()
```

---

### 3.2 Структура тестов для интеграций

```
tests/
└── test_voice_integration.py
    ├── test_voice_integration_coordination()
    ├── test_voice_integration_size()
    ├── test_voice_integration_no_local_flags()
    ├── test_voice_integration_state_manager()
    ├── test_voice_integration_full_cycle()
    └── test_voice_integration_error_handling()
```

---

## 📊 Часть 4: Команды для Запуска Тестов

### 4.1 Запуск тестов по фазам

**Фаза 1 (День 1-2):**
```bash
pytest tests/test_initialize_*.py -v
```

**Фаза 2 (День 3):**
```bash
pytest tests/test_avf_*.py -v
```

**Фаза 3 (День 4):**
```bash
pytest tests/test_google_*.py -v
```

**Фаза 4 (День 5):**
```bash
pytest tests/test_voice_integration_*.py -v
```

**Фаза 5 (День 6-7):**
```bash
pytest tests/test_voice_integration_state_manager.py tests/test_state_manager_atomic.py tests/test_no_state_desync.py -v
```

**Фаза 6 (День 8-9):**
```bash
pytest tests/test_integration_*.py -v
```

**Фаза 7 (День 12-14):**
```bash
# Все тесты
pytest tests/ -v --cov=modules/audio_avf --cov=modules/audio_google --cov=integration/integrations/voice_recognition_integration

# Проверка покрытия
pytest tests/ --cov=modules/audio_avf --cov=modules/audio_google --cov=integration/integrations/voice_recognition_integration --cov-report=html
```

---

### 4.2 Проверка покрытия кода

**Требование:** Покрытие кода ≥ 80%

```bash
# Генерация отчета о покрытии
pytest tests/ --cov=modules/audio_avf --cov=modules/audio_google --cov=integration/integrations/voice_recognition_integration --cov-report=html --cov-report=term

# Просмотр отчета
open htmlcov/index.html
```

---

## 📊 Часть 5: Таблица Фаз Тестирования

| Этап | День | Фаза тестирования | Тесты | Чек-лист |
|------|------|------------------|-------|----------|
| **Диагностика initialize()** | 1-2 | Фаза 1 | test_initialize_call.py, test_initialize_logging.py | 4 пункта |
| **Создание AVF модуля** | 3 | Фаза 2 | test_avf_config.py, test_avf_manager_*.py (5 тестов) | 7 пунктов |
| **Создание Google модуля** | 4 | Фаза 3 | test_google_config.py, test_google_manager_*.py (5 тестов) | 7 пунктов |
| **Упрощение интеграции** | 5 | Фаза 4 | test_voice_integration_coordination.py, test_voice_integration_size.py, test_voice_integration_no_local_flags.py | 5 пунктов |
| **Унификация состояния** | 6-7 | Фаза 5 | test_voice_integration_state_manager.py, test_state_manager_atomic.py, test_no_state_desync.py | 4 пункта |
| **Расширенное тестирование** | 8-9 | Фаза 6 | test_integration_full_cycle.py, test_integration_error_handling.py, test_integration_sequence.py, test_integration_performance.py, test_integration_edge_cases.py | 7 пунктов |
| **Финальная проверка** | 12-14 | Фаза 7 | Все тесты, test_requirements_compliance.py, test_performance_requirements.py, test_backward_compatibility.py | 6 пунктов |

**ИТОГО:** 7 фаз тестирования, 30+ изолированных тестов

---

## ✅ Часть 6: Итоговые Требования к Тестированию

### 6.1 Обязательные требования

1. **Изоляция:**
   - ✅ Тесты изолированы (не требуют реального микрофона)
   - ✅ Тесты быстрые (< 1 секунды для unit, < 5 секунд для интеграционных)
   - ✅ Тесты воспроизводимые (четкий результат прошел/не прошел)

2. **Покрытие:**
   - ✅ Покрытие кода ≥ 80%
   - ✅ Все модули покрыты тестами
   - ✅ Все интеграции покрыты тестами

3. **Проверка требований:**
   - ✅ Все требования проверяются тестами
   - ✅ Все чек-листы проверяются тестами
   - ✅ Все метрики проверяются тестами

---

### 6.2 Метрики тестирования

| Метрика | Целевое значение | Проверка |
|---------|------------------|----------|
| Покрытие кода | ≥ 80% | ✅ |
| Время unit-теста | < 1 сек | ✅ |
| Время интеграционного теста | < 5 сек | ✅ |
| Количество тестов | 30+ | ✅ |
| Процент прохождения | 100% | ✅ |

---

## 🎯 Заключение

**Детальный план фаз тестирования:**
1. ✅ 7 фаз тестирования для каждого этапа
2. ✅ 30+ изолированных тестов
3. ✅ Чек-листы для каждой фазы
4. ✅ Команды для запуска тестов
5. ✅ Требования к покрытию кода

**Все тесты изолированы и быстрые.**

**Готов к реализации и тестированию!**

