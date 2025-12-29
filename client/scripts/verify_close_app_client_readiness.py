#!/usr/bin/env python3
"""
Проверка готовности клиента к close_app.

Проверяет:
1. Конфигурацию MCP close_app
2. Существование MCP сервера
3. Наличие ActionExecutionIntegration

Использование:
    python verify_close_app_client_readiness.py [--project-root PATH]

Требования:
    - Скрипт должен запускаться из структуры репозитория:
      /path/to/Nexy/client/scripts/
    - Или указать --project-root для кастомной структуры
"""

import sys
import yaml
import argparse
from pathlib import Path
from typing import Optional


def get_project_root(custom_root: Optional[str] = None) -> Path:
    """
    Определяет корень проекта.
    
    Args:
        custom_root: Кастомный путь к корню проекта (если указан)
    
    Returns:
        Path к корню проекта Nexy
    """
    if custom_root:
        return Path(custom_root).resolve()
    
    # Пытаемся определить автоматически
    # Скрипт находится в: client/scripts/verify_close_app_client_readiness.py
    script_path = Path(__file__).resolve()
    
    # Поднимаемся на 2 уровня: scripts -> client -> Nexy root
    potential_root = script_path.parent.parent
    
    # Проверяем, что это действительно корень Nexy (есть server/ и client/)
    if (potential_root / "server").exists() and (potential_root / "client").exists():
        return potential_root
    
    # Если не нашли, используем текущую директорию
    print("⚠️  Не удалось автоматически определить корень проекта")
    print(f"   Используется: {potential_root}")
    print("   Если структура другая, используйте --project-root")
    return potential_root


# Парсим аргументы
parser = argparse.ArgumentParser(description='Проверка готовности клиента к close_app')
parser.add_argument('--project-root', type=str, help='Путь к корню проекта Nexy')
args = parser.parse_args()

# Определяем корень проекта
project_root = get_project_root(args.project_root)

# Добавляем корень проекта в путь
sys.path.insert(0, str(project_root / "client"))

from config.unified_config_loader import UnifiedConfigLoader


def check_mcp_config():
    """Проверка 1: Конфигурация MCP close_app"""
    print("\n" + "="*80)
    print("ПРОВЕРКА 1: Конфигурация MCP close_app")
    print("="*80)
    
    try:
        loader = UnifiedConfigLoader.get_instance()
        mcp_config = loader.get_mcp_config()
        close_app_config = mcp_config.get('close_app', {})
        
        enabled = close_app_config.get('enabled', False)
        server_path = close_app_config.get('server_path', '')
        timeout = close_app_config.get('timeout_sec', 10.0)
        
        print(f"\n📋 Конфигурация MCP close_app:")
        print(f"   enabled: {enabled}")
        print(f"   server_path: {server_path}")
        print(f"   timeout_sec: {timeout}")
        
        if not enabled:
            print("\n❌ MCP close_app выключен!")
            print("   → Установите mcp.close_app.enabled: true в unified_config.yaml")
            return False
        
        if not server_path:
            print("\n❌ Путь к MCP серверу не указан!")
            return False
        
        # Проверяем существование файла
        if server_path.startswith('/'):
            server_file = Path(server_path)
        else:
            # Относительный путь от корня проекта Nexy
            server_file = project_root / server_path
        
        if server_file.exists():
            print(f"\n✅ Файл MCP сервера существует: {server_file}")
            print(f"   Размер: {server_file.stat().st_size} байт")
            
            # Проверяем, что это Python файл
            if server_file.suffix == '.py':
                print(f"   ✅ Это Python файл")
            else:
                print(f"   ⚠️  Это не Python файл (.py)")
            
            return True
        else:
            print(f"\n❌ Файл MCP сервера не найден: {server_file}")
            print(f"   → Проверьте путь в unified_config.yaml")
            return False
            
    except Exception as e:
        print(f"\n❌ Ошибка при проверке конфигурации: {e}")
        import traceback
        traceback.print_exc()
        return False


def check_action_integration():
    """Проверка 2: Наличие ActionExecutionIntegration"""
    print("\n" + "="*80)
    print("ПРОВЕРКА 2: ActionExecutionIntegration")
    print("="*80)
    
    try:
        from integration.integrations.action_execution_integration import ActionExecutionIntegration
        
        print("\n✅ ActionExecutionIntegration импортирован успешно")
        
        # Проверяем, что интеграция поддерживает close_app
        import inspect
        source = inspect.getsource(ActionExecutionIntegration)
        
        has_close_app = 'close_app' in source
        has_mcp_executor = 'McpActionExecutor' in source or 'mcp_executor' in source
        
        print(f"\n📋 Проверка поддержки close_app:")
        print(f"   ✅ 'close_app' в коде: {has_close_app}")
        print(f"   ✅ MCP executor используется: {has_mcp_executor}")
        
        if has_close_app and has_mcp_executor:
            print("\n✅ ActionExecutionIntegration поддерживает close_app!")
            return True
        else:
            print("\n❌ ActionExecutionIntegration не поддерживает close_app!")
            return False
            
    except ImportError as e:
        print(f"\n❌ Не удалось импортировать ActionExecutionIntegration: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Ошибка при проверке интеграции: {e}")
        import traceback
        traceback.print_exc()
        return False


def check_actions_config():
    """Проверка 3: Конфигурация actions.close_app"""
    print("\n" + "="*80)
    print("ПРОВЕРКА 3: Конфигурация actions.close_app")
    print("="*80)
    
    try:
        loader = UnifiedConfigLoader.get_instance()
        actions_config = loader.get_actions_config()
        close_app_action = actions_config.get('close_app')
        
        if not close_app_action:
            print("\n❌ Конфигурация actions.close_app не найдена!")
            return False
        
        # OpenAppActionConfig - это dataclass, обращаемся к атрибутам напрямую
        enabled = close_app_action.enabled
        timeout = close_app_action.timeout_sec
        speak_errors = close_app_action.speak_errors
        
        print(f"\n📋 Конфигурация actions.close_app:")
        print(f"   enabled: {enabled}")
        print(f"   timeout_sec: {timeout}")
        print(f"   speak_errors: {speak_errors}")
        
        if not enabled:
            print("\n❌ actions.close_app выключен!")
            print("   → Установите actions.close_app.enabled: true в unified_config.yaml")
            return False
        
        print("\n✅ Конфигурация actions.close_app корректна!")
        return True
        
    except Exception as e:
        print(f"\n❌ Ошибка при проверке конфигурации actions: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Запуск всех проверок"""
    print("\n" + "="*80)
    print("ПРОВЕРКА ГОТОВНОСТИ КЛИЕНТА К close_app")
    print("="*80)
    print("\nПроверяются:")
    print("1. Конфигурация MCP close_app")
    print("2. Наличие ActionExecutionIntegration")
    print("3. Конфигурация actions.close_app")
    
    results = []
    
    # Проверка 1: MCP конфиг
    results.append(("MCP конфигурация", check_mcp_config()))
    
    # Проверка 2: Интеграция
    results.append(("ActionExecutionIntegration", check_action_integration()))
    
    # Проверка 3: Actions конфиг
    results.append(("Actions конфигурация", check_actions_config()))
    
    # Итоги
    print("\n" + "="*80)
    print("ИТОГИ ПРОВЕРКИ")
    print("="*80)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    print(f"\n📊 Результат: {passed}/{total} проверок пройдено")
    
    if passed == total:
        print("\n🎉 Все проверки пройдены! Клиент готов к close_app.")
        print("\n📝 Следующие шаги:")
        print("   1. Запустить E2E тест: python scripts/test_close_app_e2e.py")
        print("   2. Проверить события: actions.close_app.started/completed")
        return 0
    else:
        print(f"\n⚠️  {total - passed} проверка(ок) не пройдено.")
        print("   Исправьте проблемы перед использованием close_app!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
