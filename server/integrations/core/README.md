# Core Interfaces - Базовые интерфейсы для модулей и интеграций

## Обзор

Этот пакет содержит базовые интерфейсы и классы для единообразного взаимодействия модулей и интеграций в серверной части Nexy.

## Основные компоненты

### UniversalModuleInterface

Универсальный интерфейс для всех модулей сервера.

**Обязательные методы:**
- `initialize(config: dict) -> None` - инициализация модуля
- `process(request: Any) -> Any | AsyncIterator[Any]` - обработка запроса
- `cleanup() -> None` - очистка ресурсов
- `status() -> ModuleStatus` - получение статуса модуля

**Пример использования:**
```python
from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState

class MyModule(UniversalModuleInterface):
    def __init__(self):
        super().__init__(name="my_module")
        self._status = ModuleStatus(state=ModuleState.INIT)
    
    async def initialize(self, config: dict) -> None:
        # Инициализация модуля
        self._status = ModuleStatus(state=ModuleState.READY, health="ok")
    
    async def process(self, request):
        # Обработка запроса
        return {"result": "processed"}
    
    async def cleanup(self) -> None:
        # Очистка ресурсов
        self._status = ModuleStatus(state=ModuleState.STOPPED)
    
    def status(self) -> ModuleStatus:
        return self._status
```

### ModuleStatus

Dataclass для статуса модуля.

**Состояния:**
- `INIT` - модуль создан, но не инициализирован
- `READY` - модуль готов к работе
- `PROCESSING` - модуль обрабатывает запрос
- `ERROR` - модуль в состоянии ошибки
- `STOPPED` - модуль остановлен

**Методы:**
- `is_ready() -> bool` - проверка готовности модуля
- `is_error() -> bool` - проверка наличия ошибки
- `to_dict() -> dict` - преобразование в словарь

### ModuleCoordinator

Координатор модулей для управления жизненным циклом и получением модулей по capability.

**Основные методы:**
- `register(capability: str, module: UniversalModuleInterface, config: dict) -> None` - регистрация модуля
- `get(capability: str) -> UniversalModuleInterface` - получение модуля по capability
- `has(capability: str) -> bool` - проверка наличия capability
- `cleanup_all() -> None` - очистка всех модулей

**Пример использования:**
```python
from integrations.service_integrations.module_coordinator import ModuleCoordinator
from modules.text_processing.module import TextProcessingModule

coordinator = ModuleCoordinator()

# Регистрация модуля
module = TextProcessingModule()
await coordinator.register("text_processing", module, config)

# Получение модуля
module = coordinator.get("text_processing")

# Очистка всех модулей
await coordinator.cleanup_all()
```

## Диаграмма потоков

```
Client → gRPC → GrpcServiceIntegration → ModuleCoordinator → Module
                                                              ↓
                                                         WorkflowIntegration
                                                              ↓
                                                         Module (next)
```

**Правила:**
1. Модули не знают друг о друге напрямую
2. Все взаимодействие идет через координатор
3. Workflow-интеграции оркестрируют несколько модулей
4. gRPC интеграция делегирует в координатор

## UniversalProviderInterface

Интерфейс для внешних провайдеров (например, Gemini API, Azure TTS).

**Используется в модулях для взаимодействия с внешними сервисами.**

## UniversalFallbackManager

Менеджер fallback-логики для переключения между провайдерами при ошибках.

**Реализует circuit breaker паттерн.**

## Запрещенные практики

❌ **Прямые межмодульные импорты:**
```python
# НЕПРАВИЛЬНО
from modules.audio_generation import AudioProcessor

# ПРАВИЛЬНО
module = coordinator.get("audio_generation")
```

❌ **Прямые вызовы между модулями:**
```python
# НЕПРАВИЛЬНО
text_module.call_audio_module()

# ПРАВИЛЬНО
audio_module = coordinator.get("audio_generation")
await audio_module.process(request)
```

## Проверка

Используйте скрипт для проверки отсутствия прямых межмодульных вызовов:

```bash
python3 scripts/verify_no_direct_module_calls.py
```

