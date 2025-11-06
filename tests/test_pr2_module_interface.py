#!/usr/bin/env python3
"""
Тесты для PR-2: модули и интерфейсы
"""

import sys
import asyncio
from pathlib import Path

# Добавляем корневую директорию в путь
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState
from integrations.service_integrations.module_coordinator import ModuleCoordinator


class MockModule(UniversalModuleInterface):
    """Мок-модуль для тестирования"""
    
    def __init__(self, name: str = "mock_module"):
        super().__init__(name)
        self._config = {}
        self._status = ModuleStatus(state=ModuleState.INIT)
        self._initialized = False
    
    async def initialize(self, config: dict) -> None:
        """Инициализация мок-модуля"""
        self._config = config
        self._status = ModuleStatus(state=ModuleState.READY, health="ok")
        self._initialized = True
    
    async def process(self, request):
        """Обработка запроса"""
        self._status = ModuleStatus(state=ModuleState.PROCESSING, health="ok")
        result = {"processed": True, "request": request}
        self._status = ModuleStatus(state=ModuleState.READY, health="ok")
        return result
    
    async def cleanup(self) -> None:
        """Очистка мок-модуля"""
        self._status = ModuleStatus(state=ModuleState.STOPPED, health="down")
        self._initialized = False
    
    def status(self) -> ModuleStatus:
        """Статус мок-модуля"""
        return self._status


async def test_module_interface():
    """Тест: модуль реализует UniversalModuleInterface"""
    print("📋 Тест: модуль реализует UniversalModuleInterface...")
    
    module = MockModule("test_module")
    
    # Проверяем, что это экземпляр интерфейса
    assert isinstance(module, UniversalModuleInterface), "Модуль должен быть экземпляром UniversalModuleInterface"
    
    # Проверяем начальный статус
    status = module.status()
    assert status.state == ModuleState.INIT, f"Начальный статус должен быть INIT, получен {status.state}"
    
    print("✅ Модуль реализует UniversalModuleInterface")


async def test_module_initialize():
    """Тест: инициализация модуля"""
    print("📋 Тест: инициализация модуля...")
    
    module = MockModule("test_module")
    config = {"test_param": "test_value"}
    
    await module.initialize(config)
    
    status = module.status()
    assert status.state == ModuleState.READY, f"После инициализации статус должен быть READY, получен {status.state}"
    assert status.is_ready(), "Модуль должен быть готов после инициализации"
    
    print("✅ Модуль инициализируется корректно")


async def test_module_process():
    """Тест: обработка запроса"""
    print("📋 Тест: обработка запроса...")
    
    module = MockModule("test_module")
    await module.initialize({"test": "config"})
    
    request = {"data": "test"}
    result = await module.process(request)
    
    assert result["processed"] == True, "Результат должен содержать processed=True"
    assert result["request"] == request, "Результат должен содержать исходный запрос"
    
    # Проверяем, что статус вернулся в READY
    status = module.status()
    assert status.state == ModuleState.READY, "После обработки статус должен быть READY"
    
    print("✅ Модуль обрабатывает запросы корректно")


async def test_module_cleanup():
    """Тест: очистка модуля"""
    print("📋 Тест: очистка модуля...")
    
    module = MockModule("test_module")
    await module.initialize({"test": "config"})
    
    await module.cleanup()
    
    status = module.status()
    assert status.state == ModuleState.STOPPED, f"После очистки статус должен быть STOPPED, получен {status.state}"
    
    print("✅ Модуль очищается корректно")


async def test_module_coordinator_register():
    """Тест: регистрация модуля в координаторе"""
    print("📋 Тест: регистрация модуля в координаторе...")
    
    coordinator = ModuleCoordinator()
    module = MockModule("test_module")
    
    await coordinator.register("test_capability", module, {"test": "config"})
    
    assert coordinator.has("test_capability"), "Capability должен быть зарегистрирован"
    assert coordinator.get("test_capability") == module, "Полученный модуль должен совпадать с зарегистрированным"
    
    print("✅ Модуль регистрируется в координаторе")


async def test_module_coordinator_get():
    """Тест: получение модуля по capability"""
    print("📋 Тест: получение модуля по capability...")
    
    coordinator = ModuleCoordinator()
    module = MockModule("test_module")
    
    await coordinator.register("test_capability", module, {"test": "config"})
    
    retrieved_module = coordinator.get("test_capability")
    assert retrieved_module == module, "Полученный модуль должен совпадать с зарегистрированным"
    
    # Проверяем, что несуществующий capability вызывает ошибку
    try:
        coordinator.get("non_existent")
        assert False, "Должна быть вызвана ошибка KeyError"
    except KeyError:
        pass  # Ожидаемо
    
    print("✅ Модуль получается по capability")


async def test_module_coordinator_cleanup():
    """Тест: очистка всех модулей в координаторе"""
    print("📋 Тест: очистка всех модулей в координаторе...")
    
    coordinator = ModuleCoordinator()
    module1 = MockModule("module1")
    module2 = MockModule("module2")
    
    await coordinator.register("capability1", module1, {"test": "config"})
    await coordinator.register("capability2", module2, {"test": "config"})
    
    await coordinator.cleanup_all()
    
    # Проверяем, что модули очищены
    assert module1.status().state == ModuleState.STOPPED, "Модуль 1 должен быть очищен"
    assert module2.status().state == ModuleState.STOPPED, "Модуль 2 должен быть очищен"
    
    # Проверяем, что координатор очищен
    assert len(coordinator.list_modules()) == 0, "Координатор должен быть пуст после очистки"
    
    print("✅ Все модули очищаются через координатор")


async def run_all_tests():
    """Запуск всех тестов"""
    print("=" * 60)
    print("🧪 Тесты для PR-2: модули и интерфейсы")
    print("=" * 60)
    print()
    
    tests = [
        ("Модуль реализует UniversalModuleInterface", test_module_interface),
        ("Инициализация модуля", test_module_initialize),
        ("Обработка запроса", test_module_process),
        ("Очистка модуля", test_module_cleanup),
        ("Регистрация модуля в координаторе", test_module_coordinator_register),
        ("Получение модуля по capability", test_module_coordinator_get),
        ("Очистка всех модулей в координаторе", test_module_coordinator_cleanup),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            await test_func()
            passed += 1
        except AssertionError as e:
            print(f"❌ Тест провален: {e}")
            failed += 1
        except Exception as e:
            print(f"❌ Неожиданная ошибка: {e}")
            failed += 1
    
    print()
    print("=" * 60)
    print(f"📊 Результаты: {passed} пройдено, {failed} провалено")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = asyncio.run(run_all_tests())
    sys.exit(0 if success else 1)

