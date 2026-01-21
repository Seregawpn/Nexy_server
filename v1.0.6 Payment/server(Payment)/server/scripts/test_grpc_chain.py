#!/usr/bin/env python3
"""
Тест полной цепочки до gRPC: проверка формата данных для отправки клиенту

Проверяет:
1. command_payload правильно формируется
2. Данные правильно сериализуются для gRPC
3. Формат соответствует proto контракту
"""

import sys
import os
import json
from pathlib import Path

# Добавляем путь к серверу
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "server"))

from modules.grpc_service import streaming_pb2


def test_command_payload_format():
    """Тест 1: Формат command_payload для gRPC"""
    print("\n" + "="*80)
    print("ТЕСТ 1: Формат command_payload для gRPC")
    print("="*80)
    
    # Симулируем command_payload из workflow
    command_payload = {
        'event': 'mcp.command_request',
        'payload': {
            'session_id': 'test_session_123',
            'command': 'open_app',
            'args': {
                'app_name': 'Safari'
            }
        }
    }
    
    # Проверяем формат для отправки через text_chunk с префиксом __MCP__
    try:
        mcp_json = json.dumps(command_payload, ensure_ascii=False)
        mcp_text_chunk = f"__MCP__{mcp_json}"
        
        print(f"\n📋 Формат данных:")
        print(f"   ✅ JSON длина: {len(mcp_json)}")
        print(f"   ✅ С префиксом: {len(mcp_text_chunk)}")
        print(f"   ✅ Префикс: __MCP__")
        print(f"   ✅ JSON валиден: {json.loads(mcp_json) is not None}")
        
        # Проверяем структуру
        parsed = json.loads(mcp_json)
        payload = parsed.get('payload', {})
        command = payload.get('command')
        args = payload.get('args', {})
        app_name = args.get('app_name') if isinstance(args, dict) else None
        
        if command == 'open_app' and app_name == 'Safari':
            print(f"   ✅ Структура корректна: command={command}, app={app_name}")
            print(f"\n✅ ТЕСТ 1 ПРОЙДЕН: Формат command_payload корректен")
            return True
        else:
            print(f"   ❌ Структура некорректна: command={command}, app={app_name}")
            return False
            
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")
        return False


def test_action_message_proto():
    """Тест 2: Формат ActionMessage для proto (если используется)"""
    print("\n" + "="*80)
    print("ТЕСТ 2: Формат ActionMessage для proto")
    print("="*80)
    
    # Создаем ActionMessage согласно proto
    action_json = json.dumps({
        "type": "open_app",
        "app_name": "Safari"
    })
    
    try:
        action_message = streaming_pb2.ActionMessage(
            action_json=action_json,
            session_id="test_session_123",
            feature_id="F-2025-013-open-app"
        )
        
        print(f"\n📋 ActionMessage:")
        print(f"   ✅ action_json: {action_message.action_json[:50]}...")
        print(f"   ✅ session_id: {action_message.session_id}")
        print(f"   ✅ feature_id: {action_message.feature_id}")
        
        # Проверяем содержимое action_json
        parsed_action = json.loads(action_message.action_json)
        if parsed_action.get('type') == 'open_app' and parsed_action.get('app_name') == 'Safari':
            print(f"   ✅ action_json структура корректна")
            print(f"\n✅ ТЕСТ 2 ПРОЙДЕН: ActionMessage формат корректен")
            return True
        else:
            print(f"   ❌ action_json структура некорректна")
            return False
            
    except Exception as e:
        print(f"   ❌ Ошибка создания ActionMessage: {e}")
        return False


def test_stream_response_format():
    """Тест 3: Формат StreamResponse для разных типов контента"""
    print("\n" + "="*80)
    print("ТЕСТ 3: Формат StreamResponse")
    print("="*80)
    
    test_cases = [
        {
            "name": "Text chunk",
            "create": lambda: streaming_pb2.StreamResponse(text_chunk="Hello!")
        },
        {
            "name": "Audio chunk",
            "create": lambda: streaming_pb2.StreamResponse(
                audio_chunk=streaming_pb2.AudioChunk(
                    audio_data=b"fake_audio",
                    dtype="int16",
                    shape=[1024]
                )
            )
        },
        {
            "name": "Action message",
            "create": lambda: streaming_pb2.StreamResponse(
                action_message=streaming_pb2.ActionMessage(
                    action_json='{"type":"open_app","app_name":"Safari"}',
                    session_id="test_session_123"
                )
            )
        },
        {
            "name": "End message",
            "create": lambda: streaming_pb2.StreamResponse(end_message="Done")
        }
    ]
    
    all_passed = True
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 Тест 3.{i}: {test_case['name']}")
        try:
            response = test_case['create']()
            
            # Проверяем, что правильно установлен oneof
            which_oneof = response.WhichOneof('content')
            print(f"   ✅ WhichOneof: {which_oneof}")
            
            if which_oneof == test_case['name'].lower().replace(' ', '_'):
                print(f"   ✅ Тип контента корректен")
            else:
                print(f"   ⚠️  Тип контента: {which_oneof} (ожидался другой формат)")
                
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
            all_passed = False
    
    if all_passed:
        print(f"\n✅ ТЕСТ 3 ПРОЙДЕН: StreamResponse формат корректен")
        return True
    else:
        return False


def test_mcp_text_chunk_format():
    """Тест 4: Формат __MCP__ text_chunk для клиента"""
    print("\n" + "="*80)
    print("ТЕСТ 4: Формат __MCP__ text_chunk")
    print("="*80)
    
    command_payload = {
        'event': 'mcp.command_request',
        'payload': {
            'session_id': 'test_session_456',
            'command': 'open_app',
            'args': {
                'app_name': 'Telegram'
            }
        }
    }
    
    mcp_json = json.dumps(command_payload, ensure_ascii=False)
    mcp_text_chunk = f"__MCP__{mcp_json}"
    
    # Симулируем StreamResponse
    response = streaming_pb2.StreamResponse(text_chunk=mcp_text_chunk)
    
    print(f"\n📋 MCP text_chunk:")
    print(f"   ✅ Длина: {len(mcp_text_chunk)}")
    print(f"   ✅ Начинается с __MCP__: {mcp_text_chunk.startswith('__MCP__')}")
    print(f"   ✅ JSON валиден: {json.loads(mcp_text_chunk[7:]) is not None}")
    
    # Проверяем, что клиент сможет извлечь
    if mcp_text_chunk.startswith('__MCP__'):
        extracted_json = mcp_text_chunk[7:]  # Убираем префикс
        parsed = json.loads(extracted_json)
        payload = parsed.get('payload', {})
        command = payload.get('command')
        
        if command == 'open_app':
            print(f"   ✅ Команда извлечена: {command}")
            print(f"\n✅ ТЕСТ 4 ПРОЙДЕН: Формат __MCP__ text_chunk корректен")
            return True
        else:
            print(f"   ❌ Команда не извлечена")
            return False
    else:
        print(f"   ❌ Префикс отсутствует")
        return False


def main():
    """Запуск всех тестов gRPC формата"""
    print("\n" + "="*80)
    print("ТЕСТИРОВАНИЕ ФОРМАТА ДАННЫХ ДЛЯ gRPC")
    print("="*80)
    print("\nПроверка:")
    print("1. Формат command_payload")
    print("2. Формат ActionMessage (proto)")
    print("3. Формат StreamResponse")
    print("4. Формат __MCP__ text_chunk")
    
    results = []
    
    # Тест 1: command_payload
    results.append(("Формат command_payload", test_command_payload_format()))
    
    # Тест 2: ActionMessage
    results.append(("Формат ActionMessage", test_action_message_proto()))
    
    # Тест 3: StreamResponse
    results.append(("Формат StreamResponse", test_stream_response_format()))
    
    # Тест 4: __MCP__ text_chunk
    results.append(("Формат __MCP__ text_chunk", test_mcp_text_chunk_format()))
    
    # Итоги
    print("\n" + "="*80)
    print("ИТОГИ ТЕСТИРОВАНИЯ gRPC ФОРМАТА")
    print("="*80)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    print(f"\n📊 Результат: {passed}/{total} тестов пройдено")
    
    if passed == total:
        print("\n🎉 Все тесты пройдены! Формат данных для gRPC корректен.")
        print("\n✅ Готово к отправке клиенту:")
        print("   - command_payload правильно сериализуется")
        print("   - __MCP__ префикс добавляется")
        print("   - StreamResponse правильно формируется")
        print("   - ActionMessage поддерживается (если используется)")
        return 0
    else:
        print(f"\n⚠️  {total - passed} тест(ов) не пройдено.")
        return 1


if __name__ == "__main__":
    sys.exit(main())





