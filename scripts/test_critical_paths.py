#!/usr/bin/env python3
"""
Изолированное тестирование критических участков кода перед упаковкой.

Тестирует:
1. Tray controller - логика завершения приложения
2. NSApplication activation - правильная настройка для menu bar
3. First run permissions - проверка флагов и логики
4. Permission restart - логика перезапуска
5. Instance manager - проверка дублирования
"""

import sys
import os
import tempfile
import asyncio
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Добавляем пути к модулям
CLIENT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "integration"))

import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Результаты тестов
test_results = []

def test_result(name, passed, error=None):
    """Записать результат теста"""
    test_results.append((name, passed, error))
    status = "✅ ПРОЙДЕН" if passed else "❌ ПРОВАЛЕН"
    print(f"{name}: {status}")
    if error:
        print(f"  Ошибка: {error}")

def test_tray_termination_logic():
    """Тест 1: Логика завершения tray controller"""
    print("\n" + "="*80)
    print("ТЕСТ 1: Логика завершения tray controller")
    print("="*80)
    
    try:
        from modules.tray_controller.macos.menu_handler import MacOSTrayMenu
        
        # Создаём временную иконку
        icon_path = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
        try:
            from PIL import Image
            img = Image.new('RGB', (32, 32), color='gray')
            img.save(icon_path)
        except ImportError:
            Path(icon_path).touch()
        
        # Создаём tray menu
        tray_menu = MacOSTrayMenu(app_name="TestApp")
        app = tray_menu.create_app(icon_path)
        
        # Проверка 1: applicationShouldTerminate установлен
        if not hasattr(app, 'applicationShouldTerminate'):
            test_result("ТЕСТ 1.1: applicationShouldTerminate установлен", False, "Метод не установлен")
            return False
        
        # Проверка 2: applicationShouldTerminate возвращает False
        result = app.applicationShouldTerminate(None)
        if result != False:
            test_result("ТЕСТ 1.2: applicationShouldTerminate возвращает False", False, f"Возвращает {result}")
            return False
        
        # Проверка 3: _setup_quit_handler доступен
        if not hasattr(tray_menu, '_setup_quit_handler'):
            test_result("ТЕСТ 1.3: _setup_quit_handler доступен", False, "Метод не найден")
            return False
        
        # Очистка
        try:
            os.unlink(icon_path)
        except:
            pass
        
        test_result("ТЕСТ 1: Логика завершения tray controller", True)
        return True
        
    except Exception as e:
        test_result("ТЕСТ 1: Логика завершения tray controller", False, str(e))
        import traceback
        traceback.print_exc()
        return False

def test_nsapplication_activation():
    """Тест 2: NSApplication activation для menu bar"""
    print("\n" + "="*80)
    print("ТЕСТ 2: NSApplication activation")
    print("="*80)
    
    try:
        import AppKit
        
        # Проверка 1: NSApplication доступен
        nsapp = AppKit.NSApplication.sharedApplication()
        if nsapp is None:
            test_result("ТЕСТ 2.1: NSApplication доступен", False, "NSApplication не создан")
            return False
        
        # Проверка 2: Можно установить activation policy
        # ВАЖНО: setActivationPolicy может вернуть False если уже установлен, это нормально
        try:
            result = nsapp.setActivationPolicy_(AppKit.NSApplicationActivationPolicyAccessory)
            # result может быть True или False - оба варианта нормальны
            print(f"  setActivationPolicy вернул: {result}")
        except Exception as e:
            test_result("ТЕСТ 2.2: Установка activation policy", False, str(e))
            return False
        
        # Проверка 3: Activation policy установлен
        policy = nsapp.activationPolicy()
        if policy != AppKit.NSApplicationActivationPolicyAccessory:
            test_result("ТЕСТ 2.3: Activation policy установлен", False, f"Policy = {policy}")
            return False
        
        # Проверка 4: Можно активировать приложение
        try:
            nsapp.activateIgnoringOtherApps_(True)
        except Exception as e:
            test_result("ТЕСТ 2.4: Активация приложения", False, str(e))
            return False
        
        test_result("ТЕСТ 2: NSApplication activation", True)
        return True
        
    except Exception as e:
        test_result("ТЕСТ 2: NSApplication activation", False, str(e))
        import traceback
        traceback.print_exc()
        return False

def test_first_run_flags_logic():
    """Тест 3: Логика проверки флагов first run"""
    print("\n" + "="*80)
    print("ТЕСТ 3: Логика проверки флагов first run")
    print("="*80)
    
    try:
        from integration.utils.resource_path import get_user_data_dir, get_user_cache_dir
        from modules.permission_restart.core.atomic_flag import AtomicRestartFlag
        
        # Проверка 1: Пути к директориям доступны
        data_dir = get_user_data_dir("Nexy")
        cache_dir = get_user_cache_dir("Nexy")
        
        if not data_dir.exists():
            try:
                data_dir.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                test_result("ТЕСТ 3.1: Доступ к data_dir", False, str(e))
                return False
        
        if not cache_dir.exists():
            try:
                cache_dir.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                test_result("ТЕСТ 3.2: Доступ к cache_dir", False, str(e))
                return False
        
        # Проверка 2: AtomicRestartFlag работает
        restart_flag_path = cache_dir / "test_restart_completed.flag"
        restart_flag = AtomicRestartFlag(restart_flag_path)
        
        # Проверка 3: Можно записать и прочитать флаг
        try:
            restart_flag.write(reason="test", permissions=["mic", "screen"])
            flag_data = restart_flag.read_and_remove()
            
            if flag_data is None:
                test_result("ТЕСТ 3.3: Запись/чтение AtomicRestartFlag", False, "Флаг не прочитан")
                return False
            
            if flag_data.reason != "test":
                test_result("ТЕСТ 3.3: Запись/чтение AtomicRestartFlag", False, f"Reason не совпадает: {flag_data.reason}")
                return False
            
            if flag_data.permissions != ["mic", "screen"]:
                test_result("ТЕСТ 3.3: Запись/чтение AtomicRestartFlag", False, f"Permissions не совпадают: {flag_data.permissions}")
                return False
        except Exception as e:
            test_result("ТЕСТ 3.3: Запись/чтение AtomicRestartFlag", False, str(e))
            return False
        finally:
            # Очистка
            try:
                if restart_flag_path.exists():
                    restart_flag_path.unlink()
            except:
                pass
        
        # Проверка 4: Флаг удаляется после read_and_remove
        if restart_flag_path.exists():
            test_result("ТЕСТ 3.4: Флаг удаляется после read_and_remove", False, "Флаг не удалён")
            return False
        
        test_result("ТЕСТ 3: Логика проверки флагов first run", True)
        return True
        
    except Exception as e:
        test_result("ТЕСТ 3: Логика проверки флагов first run", False, str(e))
        import traceback
        traceback.print_exc()
        return False

def test_instance_manager_logic():
    """Тест 4: Логика проверки дублирования в InstanceManager"""
    print("\n" + "="*80)
    print("ТЕСТ 4: Логика проверки дублирования")
    print("="*80)
    
    try:
        from modules.instance_manager.core.instance_manager import InstanceManager, InstanceStatus
        from modules.instance_manager.core.config import InstanceManagerConfig
        
        # Создаём временный lock-файл
        temp_dir = Path(tempfile.gettempdir()) / "nexy_test_instance"
        temp_dir.mkdir(exist_ok=True)
        lock_file = temp_dir / "nexy_instance.lock"
        
        # Очищаем старый lock-файл если есть
        if lock_file.exists():
            lock_file.unlink()
        
        try:
            # Создаём InstanceManager с тестовым lock-файлом
            config = InstanceManagerConfig(
                lock_file=str(lock_file),
                pid_check=True,
                timeout_seconds=5
            )
            instance_manager = InstanceManager(config)
            
            # Проверка 1: Проверка дублирования на чистой системе
            async def check_single():
                status = await instance_manager.check_single_instance()
                return status
            
            status = asyncio.run(check_single())
            if status != InstanceStatus.SINGLE:
                test_result("ТЕСТ 4.1: Проверка на чистой системе", False, f"Статус: {status}")
                return False
            
            # Проверка 2: Захват блокировки
            async def acquire():
                return await instance_manager.acquire_lock()
            
            acquired = asyncio.run(acquire())
            if not acquired:
                test_result("ТЕСТ 4.2: Захват блокировки", False, "Блокировка не захвачена")
                return False
            
            # Проверка 3: Проверка дублирования при существующей блокировке
            status = asyncio.run(check_single())
            # Должно быть SINGLE, так как это тот же процесс
            if status == InstanceStatus.DUPLICATE:
                test_result("ТЕСТ 4.3: Проверка при существующей блокировке (тот же PID)", False, "Обнаружено ложное дублирование")
                return False
            
            # Очистка
            try:
                if lock_file.exists():
                    lock_file.unlink()
            except:
                pass
            
            test_result("ТЕСТ 4: Логика проверки дублирования", True)
            return True
            
        finally:
            # Очистка
            try:
                if lock_file.exists():
                    lock_file.unlink()
                if temp_dir.exists():
                    temp_dir.rmdir()
            except:
                pass
        
    except Exception as e:
        test_result("ТЕСТ 4: Логика проверки дублирования", False, str(e))
        import traceback
        traceback.print_exc()
        return False

def test_permission_restart_logic():
    """Тест 5: Логика permission restart"""
    print("\n" + "="*80)
    print("ТЕСТ 5: Логика permission restart")
    print("="*80)
    
    try:
        from modules.permission_restart.macos.restart_handler import MacOSRestartHandler
        
        # Проверка 1: RestartHandler создаётся
        try:
            handler = MacOSRestartHandler(dry_run=True)
            if handler is None:
                test_result("ТЕСТ 5.1: Создание RestartHandler", False, "Handler не создан")
                return False
        except Exception as e:
            test_result("ТЕСТ 5.1: Создание RestartHandler", False, str(e))
            return False
        
        # Проверка 2: Методы доступны
        if not hasattr(handler, 'trigger_restart'):
            test_result("ТЕСТ 5.2: Метод trigger_restart доступен", False, "Метод не найден")
            return False
        
        test_result("ТЕСТ 5: Логика permission restart", True)
        return True
        
    except Exception as e:
        test_result("ТЕСТ 5: Логика permission restart", False, str(e))
        import traceback
        traceback.print_exc()
        return False

def test_event_bus_integration():
    """Тест 6: Интеграция EventBus для критических событий"""
    print("\n" + "="*80)
    print("ТЕСТ 6: Интеграция EventBus")
    print("="*80)
    
    try:
        from integration.core.event_bus import EventBus, EventPriority
        
        # Создаём EventBus
        event_bus = EventBus()
        
        # Проверка 1: EventBus создан
        if event_bus is None:
            test_result("ТЕСТ 6.1: EventBus создан", False, "EventBus не создан")
            return False
        
        # Проверка 2: Можно подписаться на событие
        received_events = []
        async def test_handler(event):
            received_events.append(event)
        
        async def test_subscribe():
            await event_bus.subscribe("test.event", test_handler, EventPriority.HIGH)
            await event_bus.publish("test.event", {"data": "test"})
            # Даём время на обработку
            await asyncio.sleep(0.1)
        
        asyncio.run(test_subscribe())
        
        if len(received_events) == 0:
            test_result("ТЕСТ 6.2: Подписка и публикация событий", False, "Событие не получено")
            return False
        
        test_result("ТЕСТ 6: Интеграция EventBus", True)
        return True
        
    except Exception as e:
        test_result("ТЕСТ 6: Интеграция EventBus", False, str(e))
        import traceback
        traceback.print_exc()
        return False

def test_state_manager_integration():
    """Тест 7: Интеграция StateManager"""
    print("\n" + "="*80)
    print("ТЕСТ 7: Интеграция StateManager")
    print("="*80)
    
    try:
        from integration.core.state_manager import ApplicationStateManager, AppMode
        
        # Создаём StateManager
        state_manager = ApplicationStateManager()
        
        # Проверка 1: StateManager создан
        if state_manager is None:
            test_result("ТЕСТ 7.1: StateManager создан", False, "StateManager не создан")
            return False
        
        # Проверка 2: Можно установить режим
        state_manager.set_mode(AppMode.SLEEPING)
        if state_manager.current_mode != AppMode.SLEEPING:
            test_result("ТЕСТ 7.2: Установка режима", False, f"Режим = {state_manager.current_mode}")
            return False
        
        # Проверка 3: Можно установить данные состояния
        state_manager.set_state_data("test_key", "test_value")
        if state_manager.get_state_data("test_key") != "test_value":
            test_result("ТЕСТ 7.3: Установка данных состояния", False, "Данные не установлены")
            return False
        
        test_result("ТЕСТ 7: Интеграция StateManager", True)
        return True
        
    except Exception as e:
        test_result("ТЕСТ 7: Интеграция StateManager", False, str(e))
        import traceback
        traceback.print_exc()
        return False

def main():
    """Запуск всех тестов"""
    print("="*80)
    print("ИЗОЛИРОВАННОЕ ТЕСТИРОВАНИЕ КРИТИЧЕСКИХ УЧАСТКОВ КОДА")
    print("="*80)
    
    # Запускаем тесты
    results = []
    results.append(("ТЕСТ 1: Tray termination logic", test_tray_termination_logic()))
    results.append(("ТЕСТ 2: NSApplication activation", test_nsapplication_activation()))
    results.append(("ТЕСТ 3: First run flags logic", test_first_run_flags_logic()))
    results.append(("ТЕСТ 4: Instance manager logic", test_instance_manager_logic()))
    results.append(("ТЕСТ 5: Permission restart logic", test_permission_restart_logic()))
    results.append(("ТЕСТ 6: EventBus integration", test_event_bus_integration()))
    results.append(("ТЕСТ 7: StateManager integration", test_state_manager_integration()))
    
    # Итоги
    print("\n" + "="*80)
    print("ИТОГИ ТЕСТИРОВАНИЯ")
    print("="*80)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ ПРОЙДЕН" if result else "❌ ПРОВАЛЕН"
        print(f"{name}: {status}")
    
    print(f"\nВсего тестов: {total}")
    print(f"Пройдено: {passed}")
    print(f"Провалено: {total - passed}")
    
    # Детальные результаты (только для проваленных подтестов)
    failed_subtests = [(name, error) for name, passed, error in test_results if not passed]
    if failed_subtests:
        print("\n" + "="*80)
        print("ДЕТАЛЬНЫЕ РЕЗУЛЬТАТЫ (проваленные подтесты)")
        print("="*80)
        for name, error in failed_subtests:
            print(f"❌ {name}")
            if error:
                print(f"   Ошибка: {error}")
    
    if passed == total:
        print("\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ! Критические участки работают корректно.")
        print("✅ Готово к упаковке!")
        return 0
    else:
        print(f"\n❌ НЕКОТОРЫЕ ТЕСТЫ ПРОВАЛЕНЫ. Требуется исправление перед упаковкой.")
        return 1

if __name__ == "__main__":
    sys.exit(main())

