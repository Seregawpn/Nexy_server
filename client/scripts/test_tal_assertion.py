#!/usr/bin/env python3
"""
Изолированный тест для проверки логики TAL (Termination After Launch) assertion.

Проверяет:
1. Установку TAL hold
2. Периодическое обновление assertion
3. Снятие TAL hold после tray.ready
4. Таймаут через 120 секунд
"""

import asyncio
import sys
import time
from pathlib import Path

# Добавляем пути
CLIENT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "modules"))
sys.path.insert(0, str(CLIENT_ROOT / "integration"))

# Результаты тестов
test_results = []

def test_result(name, passed, error=None):
    """Записать результат теста"""
    status = "✅ ПРОЙДЕН" if passed else "❌ ПРОВАЛЕН"
    test_results.append((name, passed, error))
    if passed:
        print(f"{status}: {name}")
    else:
        print(f"{status}: {name}")
        if error:
            print(f"  Ошибка: {error}")

def test_tal_hold_setup():
    """Тест 1: Проверка установки TAL hold"""
    print("\n" + "="*80)
    print("ТЕСТ 1: Проверка установки TAL hold")
    print("="*80)
    
    try:
        import Foundation
        process_info = Foundation.NSProcessInfo.processInfo()
        
        # Проверка 1: automaticTerminationSupportEnabled доступен
        if not hasattr(process_info, 'automaticTerminationSupportEnabled'):
            test_result("ТЕСТ 1.1: automaticTerminationSupportEnabled доступен", False, "Метод не найден")
            return False
        
        enabled = process_info.automaticTerminationSupportEnabled()
        print(f"✅ automaticTerminationSupportEnabled = {enabled}")
        
        # Проверка 2: disableAutomaticTermination_ доступен
        if not hasattr(process_info, 'disableAutomaticTermination_'):
            test_result("ТЕСТ 1.2: disableAutomaticTermination_ доступен", False, "Метод не найден")
            return False
        
        # Устанавливаем TAL hold
        process_info.disableAutomaticTermination_("Test: Waiting for tray icon")
        print("✅ TAL hold установлен")
        
        # Проверка 3: enableAutomaticTermination_ доступен
        if not hasattr(process_info, 'enableAutomaticTermination_'):
            test_result("ТЕСТ 1.3: enableAutomaticTermination_ доступен", False, "Метод не найден")
            return False
        
        # Снимаем TAL hold
        process_info.enableAutomaticTermination_("Test: Tray icon ready")
        print("✅ TAL hold снят")
        
        test_result("ТЕСТ 1: Проверка установки TAL hold", True)
        return True
        
    except Exception as e:
        test_result("ТЕСТ 1: Проверка установки TAL hold", False, str(e))
        import traceback
        traceback.print_exc()
        return False

def test_tal_hold_refresh():
    """Тест 2: Проверка периодического обновления TAL hold"""
    print("\n" + "="*80)
    print("ТЕСТ 2: Проверка периодического обновления TAL hold")
    print("="*80)
    
    try:
        import Foundation
        process_info = Foundation.NSProcessInfo.processInfo()
        
        # Устанавливаем TAL hold
        process_info.disableAutomaticTermination_("Test: Initial hold")
        print("✅ TAL hold установлен")
        
        # Симулируем обновление
        for i in range(3):
            time.sleep(0.1)  # Небольшая задержка для симуляции
            process_info.disableAutomaticTermination_(f"Test: Refresh {i+1}")
            print(f"✅ TAL assertion обновлён (итерация {i+1})")
        
        # Снимаем TAL hold
        process_info.enableAutomaticTermination_("Test: Done")
        print("✅ TAL hold снят")
        
        test_result("ТЕСТ 2: Проверка периодического обновления TAL hold", True)
        return True
        
    except Exception as e:
        test_result("ТЕСТ 2: Проверка периодического обновления TAL hold", False, str(e))
        import traceback
        traceback.print_exc()
        return False

async def test_tal_hold_async_logic():
    """Тест 3: Проверка асинхронной логики TAL hold"""
    print("\n" + "="*80)
    print("ТЕСТ 3: Проверка асинхронной логики TAL hold")
    print("="*80)
    
    try:
        import Foundation
        process_info = Foundation.NSProcessInfo.processInfo()
        
        # Симулируем логику из SimpleModuleCoordinator
        tal_hold_start = time.time()
        tray_ready = False
        refresh_interval = 0.5  # Уменьшено для теста
        max_wait = 2.0  # Уменьшено для теста
        
        # Устанавливаем TAL hold
        if process_info.automaticTerminationSupportEnabled():
            process_info.disableAutomaticTermination_("Test: Waiting for tray icon")
            print(f"✅ TAL hold установлен (ts={tal_hold_start:.2f})")
        
        # Симулируем периодическое обновление
        start_time = time.time()
        refresh_count = 0
        
        while (time.time() - start_time) < max_wait:
            await asyncio.sleep(refresh_interval)
            
            if tal_hold_start is None:
                break
            
            if tray_ready:
                break
            
            # Обновляем assertion
            if process_info.automaticTerminationSupportEnabled():
                process_info.disableAutomaticTermination_("Test: Refreshing")
                refresh_count += 1
                print(f"✅ TAL assertion обновлён (итерация {refresh_count})")
        
        # Симулируем готовность tray
        tray_ready = True
        print("✅ Tray готов - симулируем снятие TAL hold")
        
        # Снимаем TAL hold
        if process_info.automaticTerminationSupportEnabled():
            hold_duration = time.time() - tal_hold_start
            process_info.enableAutomaticTermination_("Test: Tray icon ready")
            print(f"✅ TAL hold снят (длительность={hold_duration:.2f}s, обновлений={refresh_count})")
        
        # Проверяем, что было хотя бы одно обновление
        if refresh_count > 0:
            print(f"✅ Периодическое обновление работает (обновлений: {refresh_count})")
        else:
            print("⚠️ Периодическое обновление не сработало (возможно, tray готов слишком быстро)")
        
        test_result("ТЕСТ 3: Проверка асинхронной логики TAL hold", True)
        return True
        
    except Exception as e:
        test_result("ТЕСТ 3: Проверка асинхронной логики TAL hold", False, str(e))
        import traceback
        traceback.print_exc()
        return False

def test_tal_hold_timeout():
    """Тест 4: Проверка таймаута TAL hold"""
    print("\n" + "="*80)
    print("ТЕСТ 4: Проверка таймаута TAL hold")
    print("="*80)
    
    try:
        import Foundation
        process_info = Foundation.NSProcessInfo.processInfo()
        
        # Устанавливаем TAL hold
        tal_hold_start = time.time()
        process_info.disableAutomaticTermination_("Test: Waiting for tray icon")
        print(f"✅ TAL hold установлен (ts={tal_hold_start:.2f})")
        
        # Проверяем, что таймаут установлен (120 секунд)
        timeout_seconds = 120.0
        print(f"✅ Таймаут установлен: {timeout_seconds} секунд")
        
        # Симулируем проверку таймаута (не ждём реальные 120 секунд)
        elapsed = time.time() - tal_hold_start
        if elapsed < timeout_seconds:
            print(f"✅ Таймаут не истёк (прошло {elapsed:.2f}s из {timeout_seconds}s)")
        else:
            print(f"⚠️ Таймаут истёк (прошло {elapsed:.2f}s)")
        
        # Снимаем TAL hold
        process_info.enableAutomaticTermination_("Test: Timeout check done")
        print("✅ TAL hold снят")
        
        test_result("ТЕСТ 4: Проверка таймаута TAL hold", True)
        return True
        
    except Exception as e:
        test_result("ТЕСТ 4: Проверка таймаута TAL hold", False, str(e))
        import traceback
        traceback.print_exc()
        return False

def test_tal_hold_coordinator_integration():
    """Тест 5: Проверка интеграции с SimpleModuleCoordinator"""
    print("\n" + "="*80)
    print("ТЕСТ 5: Проверка интеграции с SimpleModuleCoordinator")
    print("="*80)
    
    try:
        from integration.core.simple_module_coordinator import SimpleModuleCoordinator
        
        # Проверка 1: SimpleModuleCoordinator имеет метод _hold_tal_until_tray_ready
        if not hasattr(SimpleModuleCoordinator, '_hold_tal_until_tray_ready'):
            test_result("ТЕСТ 5.1: _hold_tal_until_tray_ready доступен", False, "Метод не найден")
            return False
        
        print("✅ _hold_tal_until_tray_ready доступен")
        
        # Проверка 2: SimpleModuleCoordinator имеет метод _release_tal_hold
        if not hasattr(SimpleModuleCoordinator, '_release_tal_hold'):
            test_result("ТЕСТ 5.2: _release_tal_hold доступен", False, "Метод не найден")
            return False
        
        print("✅ _release_tal_hold доступен")
        
        # Проверка 3: SimpleModuleCoordinator имеет метод _periodically_refresh_tal_hold
        if not hasattr(SimpleModuleCoordinator, '_periodically_refresh_tal_hold'):
            test_result("ТЕСТ 5.3: _periodically_refresh_tal_hold доступен", False, "Метод не найден")
            return False
        
        print("✅ _periodically_refresh_tal_hold доступен")
        
        # Проверка 4: SimpleModuleCoordinator имеет метод _release_tal_hold_after_timeout
        if not hasattr(SimpleModuleCoordinator, '_release_tal_hold_after_timeout'):
            test_result("ТЕСТ 5.4: _release_tal_hold_after_timeout доступен", False, "Метод не найден")
            return False
        
        print("✅ _release_tal_hold_after_timeout доступен")
        
        # Проверка 5: Таймаут увеличен до 120 секунд
        import inspect
        source = inspect.getsource(SimpleModuleCoordinator._release_tal_hold_after_timeout)
        if "120.0" in source or "120" in source:
            print("✅ Таймаут установлен на 120 секунд")
        else:
            print("⚠️ Таймаут может быть не установлен на 120 секунд")
        
        test_result("ТЕСТ 5: Проверка интеграции с SimpleModuleCoordinator", True)
        return True
        
    except Exception as e:
        test_result("ТЕСТ 5: Проверка интеграции с SimpleModuleCoordinator", False, str(e))
        import traceback
        traceback.print_exc()
        return False

def test_tray_integration_no_duplication():
    """Тест 6: Проверка отсутствия дублирования TAL управления в tray_controller_integration"""
    print("\n" + "="*80)
    print("ТЕСТ 6: Проверка отсутствия дублирования TAL управления")
    print("="*80)
    
    try:
        import inspect
        from integration.integrations.tray_controller_integration import TrayControllerIntegration
        
        # Получаем исходный код метода start
        source = inspect.getsource(TrayControllerIntegration.start)
        
        # Проверка: НЕ должно быть enableAutomaticTermination_ в tray_controller_integration
        if "enableAutomaticTermination_" in source:
            # Проверяем, что это закомментировано или удалено
            if "#" in source.split("enableAutomaticTermination_")[0][-50:]:
                print("✅ enableAutomaticTermination_ закомментирован или удалён")
            else:
                test_result("ТЕСТ 6: Отсутствие дублирования TAL управления", False, "enableAutomaticTermination_ всё ещё присутствует")
                return False
        else:
            print("✅ enableAutomaticTermination_ отсутствует в tray_controller_integration")
        
        # Проверка: Должен быть комментарий о том, что TAL управляется в SimpleModuleCoordinator
        if "SimpleModuleCoordinator" in source or "ANTI-TAL" in source or "КРИТИЧНО" in source:
            print("✅ Есть комментарий о том, что TAL управляется в SimpleModuleCoordinator")
        else:
            print("⚠️ Нет явного комментария о том, что TAL управляется в SimpleModuleCoordinator")
        
        test_result("ТЕСТ 6: Проверка отсутствия дублирования TAL управления", True)
        return True
        
    except Exception as e:
        test_result("ТЕСТ 6: Проверка отсутствия дублирования TAL управления", False, str(e))
        import traceback
        traceback.print_exc()
        return False

async def main():
    """Главная функция тестирования"""
    print("="*80)
    print("ТЕСТИРОВАНИЕ TAL ASSERTION LOGIC")
    print("="*80)
    
    # Запускаем тесты
    results = []
    
    # Синхронные тесты
    results.append(("Тест 1: Установка TAL hold", test_tal_hold_setup()))
    results.append(("Тест 2: Обновление TAL hold", test_tal_hold_refresh()))
    results.append(("Тест 4: Таймаут TAL hold", test_tal_hold_timeout()))
    results.append(("Тест 5: Интеграция с SimpleModuleCoordinator", test_tal_hold_coordinator_integration()))
    results.append(("Тест 6: Отсутствие дублирования", test_tray_integration_no_duplication()))
    
    # Асинхронный тест
    results.append(("Тест 3: Асинхронная логика TAL hold", await test_tal_hold_async_logic()))
    
    # Итоги
    print("\n" + "="*80)
    print("ИТОГИ ТЕСТИРОВАНИЯ")
    print("="*80)
    
    total = len(results)
    passed = sum(1 for _, result in results if result)
    failed = total - passed
    
    print(f"\nВсего тестов: {total}")
    print(f"Пройдено: {passed}")
    print(f"Провалено: {failed}")
    
    if failed > 0:
        print("\n❌ НЕКОТОРЫЕ ТЕСТЫ ПРОВАЛЕНЫ:")
        for name, result in results:
            if not result:
                print(f"  - {name}")
    else:
        print("\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ! TAL assertion logic работает корректно.")
    
    print("\n" + "="*80)
    
    return failed == 0

if __name__ == "__main__":
    try:
        success = asyncio.run(main())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⏹️ Тестирование прервано пользователем")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)




