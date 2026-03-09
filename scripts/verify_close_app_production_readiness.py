#!/usr/bin/env python3
"""
Проверка готовности close_app к production.

Проверяет:
1. Фича-флаги в окружении
2. Источник системного промпта
3. Наличие close_app в промпте
4. Конфигурацию MCP сервера

Использование:
    python verify_close_app_production_readiness.py [--project-root PATH]

Требования:
    - Скрипт должен запускаться из структуры репозитория:
      /path/to/Nexy/server/server/scripts/
    - Или указать --project-root для кастомной структуры
"""

import sys
import os
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
    # Скрипт находится в: server/server/scripts/verify_close_app_production_readiness.py
    script_path = Path(__file__).resolve()
    
    # Поднимаемся на 3 уровня: scripts -> server -> server -> Nexy root
    potential_root = script_path.parent.parent.parent
    
    # Проверяем, что это действительно корень Nexy (есть server/ и client/)
    if (potential_root / "server").exists() and (potential_root / "client").exists():
        return potential_root
    
    # Если не нашли, используем текущую директорию
    print("⚠️  Не удалось автоматически определить корень проекта")
    print(f"   Используется: {potential_root}")
    print("   Если структура другая, используйте --project-root")
    return potential_root


# Парсим аргументы
parser = argparse.ArgumentParser(description='Проверка готовности close_app к production')
parser.add_argument('--project-root', type=str, help='Путь к корню проекта Nexy')
args = parser.parse_args()

# Определяем корень проекта
project_root = get_project_root(args.project_root)

# Добавляем путь к серверу (структура: Nexy/server/server/)
server_path = project_root / "server" / "server"
if not server_path.exists():
    # Альтернативная структура: Nexy/server/
    server_path = project_root / "server"
sys.path.insert(0, str(server_path))

from config.unified_config import get_config


def check_feature_flags():
    """Проверка 1: Фича-флаги в окружении"""
    print("\n" + "="*80)
    print("ПРОВЕРКА 1: Фича-флаги для command forwarding")
    print("="*80)
    
    config = get_config()
    forward_config = config.features.forward_assistant_actions
    kill_switch_config = config.kill_switches.disable_forward_assistant_actions
    
    print(f"\n📋 Значения из конфигурации:")
    print(f"   features.forward_assistant_actions: {forward_config}")
    print(f"   kill_switches.disable_forward_assistant_actions: {kill_switch_config}")
    print(f"\n📋 Финальные значения:")
    print(f"   forward_assistant_actions: {forward_config}")
    print(f"   disable_forward_assistant_actions: {kill_switch_config}")
    
    if forward_config and not kill_switch_config:
        print("\n✅ Фича-флаги настроены правильно!")
        print("   → command_payload будет форвардиться на клиент")
        return True
    else:
        print("\n❌ Фича-флаги настроены неправильно!")
        if not forward_config:
            print("   → Включите features.actions=true в client/config/unified_config.yaml")
        if kill_switch_config:
            print("   → Установите NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS=false")
        print("\n   Без правильных флагов close_app не будет доходить до клиента!")
        return False


def check_system_prompt_source():
    """Проверка 2: Источник системного промпта"""
    print("\n" + "="*80)
    print("ПРОВЕРКА 2: Источник системного промпта")
    print("="*80)
    
    gemini_prompt_env = os.getenv('GEMINI_SYSTEM_PROMPT', '')
    config = get_config()
    prompt_from_config = config.text_processing.gemini_system_prompt
    
    print(f"\n📋 GEMINI_SYSTEM_PROMPT в окружении:")
    if gemini_prompt_env:
        print(f"   ✅ Установлен (длина: {len(gemini_prompt_env)} символов)")
        print(f"   ⚠️  ВНИМАНИЕ: Используется промпт из env, а не из unified_config.py!")
        print(f"   → Нужно убедиться, что env-промпт содержит close_app")
        prompt_to_check = gemini_prompt_env
        source = "GEMINI_SYSTEM_PROMPT (env)"
    else:
        print(f"   ❌ Не установлен")
        print(f"   ✅ Используется промпт из unified_config.py")
        prompt_to_check = prompt_from_config
        source = "unified_config.py"
    
    print(f"\n📋 Источник промпта: {source}")
    print(f"   Длина промпта: {len(prompt_to_check)} символов")
    
    # Проверяем наличие close_app в промпте
    prompt_lower = prompt_to_check.lower()
    has_close_app = 'close_app' in prompt_lower
    has_open_app = 'open_app' in prompt_lower
    has_action_intent = 'action intent' in prompt_lower or 'action intent' in prompt_lower
    has_json_format = 'json' in prompt_lower and 'command' in prompt_lower
    
    print(f"\n📋 Проверка содержания промпта:")
    print(f"   ✅ 'close_app' присутствует: {has_close_app}")
    print(f"   ✅ 'open_app' присутствует: {has_open_app}")
    print(f"   ✅ 'Action Intent' присутствует: {has_action_intent}")
    print(f"   ✅ JSON формат описан: {has_json_format}")
    
    if has_close_app and has_open_app and has_action_intent and has_json_format:
        print("\n✅ Промпт содержит все необходимые инструкции для close_app!")
        return True, source
    else:
        print("\n❌ Промпт не содержит всех необходимых инструкций!")
        if not has_close_app:
            print("   → Отсутствует 'close_app' в промпте")
        if not has_open_app:
            print("   → Отсутствует 'open_app' в промпте")
        if not has_action_intent:
            print("   → Отсутствует раздел 'Action Intent'")
        if not has_json_format:
            print("   → Отсутствует описание JSON формата")
        return False, source


def check_mcp_server_path():
    """Проверка 3: Путь к MCP серверу (клиентская часть)"""
    print("\n" + "="*80)
    print("ПРОВЕРКА 3: Путь к MCP серверу close_app")
    print("="*80)
    
    # Проверяем клиентский конфиг
    client_config_path = project_root / "client" / "config" / "unified_config.yaml"
    
    if not client_config_path.exists():
        print(f"\n⚠️  Клиентский конфиг не найден: {client_config_path}")
        print("   → Проверьте путь вручную")
        return False
    
    import yaml
    with open(client_config_path, 'r', encoding='utf-8') as f:
        client_config = yaml.safe_load(f)
    
    mcp_config = client_config.get('mcp', {}).get('close_app', {})
    enabled = mcp_config.get('enabled', False)
    server_path = mcp_config.get('server_path', '')
    
    print(f"\n📋 Конфигурация MCP close_app:")
    print(f"   enabled: {enabled}")
    print(f"   server_path: {server_path}")
    
    if not enabled:
        print("\n❌ MCP close_app выключен!")
        print("   → Установите mcp.close_app.enabled: true")
        return False
    
    if not server_path:
        print("\n❌ Путь к MCP серверу не указан!")
        return False
    
    # Проверяем, является ли путь тестовым
    is_test_path = 'test' in server_path.lower() or 'mcp_close_app_test' in server_path
    
    if is_test_path:
        print(f"\n⚠️  ВНИМАНИЕ: Используется тестовый путь!")
        print(f"   Текущий путь: {server_path}")
        print(f"   → Для production нужен реальный путь к MCP серверу")
        print(f"   → Проверьте, что сервер доступен по этому пути")
    else:
        print(f"\n✅ Путь выглядит как production путь")
    
    # Проверяем существование файла
    if server_path.startswith('/'):
        # Абсолютный путь
        server_file = Path(server_path)
    else:
        # Относительный путь от корня проекта
        server_file = project_root / server_path
    
    if server_file.exists():
        print(f"\n✅ Файл MCP сервера существует: {server_file}")
        if server_file.is_file():
            print(f"   Размер: {server_file.stat().st_size} байт")
            return True
        else:
            print(f"   ⚠️  Это директория, а не файл!")
            return False
    else:
        print(f"\n❌ Файл MCP сервера не найден: {server_file}")
        print(f"   → Проверьте путь в unified_config.yaml")
        return False


def main():
    """Запуск всех проверок"""
    print("\n" + "="*80)
    print("ПРОВЕРКА ГОТОВНОСТИ close_app К PRODUCTION")
    print("="*80)
    print("\nПроверяются:")
    print("1. Фича-флаги для command forwarding")
    print("2. Источник системного промпта и наличие close_app")
    print("3. Путь к MCP серверу close_app")
    
    results = []
    
    # Проверка 1: Фича-флаги
    results.append(("Фича-флаги", check_feature_flags()))
    
    # Проверка 2: Промпт
    prompt_ok, prompt_source = check_system_prompt_source()
    results.append(("Системный промпт", prompt_ok))
    
    # Проверка 3: MCP путь
    results.append(("MCP сервер", check_mcp_server_path()))
    
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
        print("\n🎉 Все проверки пройдены! close_app готов к production.")
        print("\n📝 Следующие шаги:")
        print("   1. Запустить E2E тест: python client/scripts/test_close_app_e2e.py")
        print("   2. Проверить логи на наличие events: actions.close_app.started/completed")
        return 0
    else:
        print(f"\n⚠️  {total - passed} проверка(ок) не пройдено.")
        print("   Исправьте проблемы перед деплоем в production!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
