#!/usr/bin/env python3
"""
Тест извлечения JSON из ответов LLM
"""

import sys
import os
from pathlib import Path

# Добавляем путь к серверу
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "server"))

from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration


def test_json_extraction():
    """Тест извлечения JSON из различных форматов ответов"""
    
    # Создаем временный экземпляр для доступа к методу
    workflow = StreamingWorkflowIntegration(None, None, None, None)
    
    test_cases = [
        {
            "name": "JSON в markdown блоке",
            "input": '```json\n{\n  "text": "Opening Safari.",\n  "command": "open_app",\n  "args": {\n    "app_name": "Safari"\n  },\n  "session_id": "session_123"\n}\n```',
            "expected_command": "open_app",
            "expected_app": "Safari"
        },
        {
            "name": "Чистый JSON",
            "input": '{\n  "text": "Opening Safari.",\n  "command": "open_app",\n  "args": {\n    "app_name": "Safari"\n  },\n  "session_id": "session_123"\n}',
            "expected_command": "open_app",
            "expected_app": "Safari"
        },
        {
            "name": "JSON с текстом до и после",
            "input": 'Here is the response:\n```json\n{\n  "text": "Opening Safari.",\n  "command": "open_app",\n  "args": {\n    "app_name": "Safari"\n  }\n}\n```\nDone!',
            "expected_command": "open_app",
            "expected_app": "Safari"
        },
        {
            "name": "Обычный текст без JSON",
            "input": "I can help you with that.",
            "expected_command": None
        }
    ]
    
    print("\n" + "="*80)
    print("ТЕСТ ИЗВЛЕЧЕНИЯ JSON ИЗ ОТВЕТОВ LLM")
    print("="*80)
    
    all_passed = True
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 Тест {i}: {test_case['name']}")
        print("-" * 80)
        
        try:
            json_data = workflow._extract_json_from_response(test_case['input'])
            
            if json_data:
                print(f"   ✅ JSON извлечен: {list(json_data.keys())}")
                command = json_data.get('command')
                args = json_data.get('args', {})
                app_name = args.get('app_name') if isinstance(args, dict) else None
                
                if command == test_case['expected_command'] and app_name == test_case.get('expected_app'):
                    print(f"   ✅ Команда корректна: command={command}, app={app_name}")
                else:
                    print(f"   ❌ Ожидалось: command={test_case['expected_command']}, app={test_case.get('expected_app')}")
                    print(f"      Получено: command={command}, app={app_name}")
                    all_passed = False
            else:
                if test_case['expected_command'] is None:
                    print(f"   ✅ JSON не найден (как и ожидалось для обычного текста)")
                else:
                    print(f"   ❌ JSON не извлечен, но ожидался!")
                    all_passed = False
                    
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
            import traceback
            traceback.print_exc()
            all_passed = False
    
    print("\n" + "="*80)
    if all_passed:
        print("✅ Все тесты пройдены!")
        return 0
    else:
        print("❌ Некоторые тесты не пройдены")
        return 1


if __name__ == "__main__":
    sys.exit(test_json_extraction())



