#!/usr/bin/env python3
"""
Проверка конфигурации MCP end-to-end
"""

import sys
import os
from pathlib import Path

# Добавляем путь к серверу
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "server"))

def check_server_config():
    """Проверка конфигурации сервера"""
    print("\n" + "="*80)
    print("ПРОВЕРКА КОНФИГУРАЦИИ СЕРВЕРА")
    print("="*80)
    
    try:
        from config.unified_config import get_config
        config = get_config()
        
        # Проверяем фича-флаг
        forward_enabled = config.features.forward_assistant_actions
        kill_switch_disabled = not config.kill_switches.disable_forward_assistant_actions
        
        print(f"\n📋 Фича-флаги:")
        print(f"   forward_assistant_actions: {forward_enabled} {'✅' if forward_enabled else '❌'}")
        print(f"   disable_forward_assistant_actions (kill-switch): {config.kill_switches.disable_forward_assistant_actions} {'❌' if config.kill_switches.disable_forward_assistant_actions else '✅'}")
        
        if forward_enabled and kill_switch_disabled:
            print("\n✅ Сервер настроен правильно!")
            return True
        else:
            print("\n❌ Сервер настроен неправильно!")
            if not forward_enabled:
                print("   → Установите FORWARD_ASSISTANT_ACTIONS=true в config.env")
            if not kill_switch_disabled:
                print("   → Убедитесь, что NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS не установлен")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка проверки конфигурации сервера: {e}")
        import traceback
        traceback.print_exc()
        return False

def check_system_prompt():
    """Проверка системного промпта"""
    print("\n" + "="*80)
    print("ПРОВЕРКА СИСТЕМНОГО ПРОМПТА")
    print("="*80)
    
    gemini_prompt_env = os.getenv('GEMINI_SYSTEM_PROMPT')
    
    if gemini_prompt_env:
        print(f"⚠️  GEMINI_SYSTEM_PROMPT установлен в переменных окружения")
        print(f"   Длина: {len(gemini_prompt_env)} символов")
        print(f"   Начало: {gemini_prompt_env[:150]}...")
        print("\n💡 РЕКОМЕНДАЦИЯ:")
        print("   Если это старый промпт без инструкций по JSON, удалите переменную:")
        print("   unset GEMINI_SYSTEM_PROMPT")
        print("   Или обновите её новым промптом из unified_config.py")
        return False
    else:
        print("✅ GEMINI_SYSTEM_PROMPT не установлен в env")
        print("   Используется промпт из unified_config.py (с инструкциями по JSON)")
        
        # Проверяем, что промпт содержит инструкции по JSON
        try:
            from config.unified_config import get_config
            config = get_config()
            prompt = config.text_processing.gemini_system_prompt
            
            keywords = ['command', 'open_app', 'args', 'app_name', 'JSON', 'session_id']
            found_keywords = [kw for kw in keywords if kw.lower() in prompt.lower()]
            
            if len(found_keywords) >= 3:
                print(f"✅ Промпт содержит инструкции по JSON ({len(found_keywords)}/{len(keywords)} ключевых слов)")
                return True
            else:
                print(f"⚠️  Промпт может не содержать полных инструкций по JSON ({len(found_keywords)}/{len(keywords)} ключевых слов)")
                return False
        except Exception as e:
            print(f"⚠️  Не удалось проверить промпт: {e}")
            return False

def check_client_config():
    """Проверка конфигурации клиента"""
    print("\n" + "="*80)
    print("ПРОВЕРКА КОНФИГУРАЦИИ КЛИЕНТА")
    print("="*80)
    
    # Путь к клиенту: используем абсолютный путь
    # project_root = server/server, поэтому нужно подняться на 2 уровня до Nexy/
    nexy_root = project_root.parent.parent  # Nexy/
    client_config_path = nexy_root / "client" / "config" / "unified_config.yaml"
    
    # Альтернативный путь (если структура другая)
    if not client_config_path.exists():
        # Пробуем относительно текущего скрипта
        script_dir = Path(__file__).parent  # server/server/scripts
        alt_path = script_dir.parent.parent.parent / "client" / "config" / "unified_config.yaml"
        if alt_path.exists():
            client_config_path = alt_path
    
    if not client_config_path.exists():
        print(f"❌ Файл конфигурации не найден: {client_config_path}")
        return False
    
    try:
        import yaml
        with open(client_config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        actions_config = config.get('actions', {})
        open_app_config = actions_config.get('open_app', {})
        
        enabled = open_app_config.get('enabled', False)
        timeout = open_app_config.get('timeout_sec', 10.0)
        binary = open_app_config.get('binary', '/usr/bin/open')
        allowed_apps = open_app_config.get('allowed_apps', [])
        
        print(f"\n📋 Конфигурация actions.open_app:")
        print(f"   enabled: {enabled} {'✅' if enabled else '❌'}")
        print(f"   timeout_sec: {timeout}")
        print(f"   binary: {binary}")
        print(f"   allowed_apps: {allowed_apps if allowed_apps else '[] (все разрешены)'}")
        
        if enabled:
            print("\n✅ Клиент настроен правильно!")
            return True
        else:
            print("\n❌ Клиент не настроен!")
            print("   → Установите actions.open_app.enabled: true в client/config/unified_config.yaml")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка проверки конфигурации клиента: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Основная функция"""
    print("\n" + "="*80)
    print("ПРОВЕРКА КОНФИГУРАЦИИ MCP END-TO-END")
    print("="*80)
    
    results = []
    
    # Проверка сервера
    results.append(("Сервер: фича-флаги", check_server_config()))
    
    # Проверка системного промпта
    results.append(("Сервер: системный промпт", check_system_prompt()))
    
    # Проверка клиента
    results.append(("Клиент: actions.open_app", check_client_config()))
    
    # Итоги
    print("\n\n" + "="*80)
    print("ИТОГИ ПРОВЕРКИ")
    print("="*80)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    print(f"\n📊 Результат: {passed}/{total} проверок пройдено")
    
    if passed == total:
        print("\n🎉 Все проверки пройдены! MCP готов к работе.")
        print("\n💡 Следующие шаги:")
        print("   1. Перезапустите сервер")
        print("   2. Перезапустите клиент")
        print("   3. Протестируйте запрос 'open Safari'")
        return 0
    else:
        print("\n⚠️  Некоторые проверки не пройдены. Исправьте конфигурацию и повторите.")
        return 1

if __name__ == "__main__":
    sys.exit(main())

