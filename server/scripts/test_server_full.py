#!/usr/bin/env python3
"""
Полный тест сервера: инициализация и обработка запросов
Проверяет:
1. Инициализацию TextProcessor с LangChain провайдером
2. Обработку запросов через StreamingWorkflowIntegration
3. Формат ответов (текст и JSON команды)
"""

import sys
import os
import asyncio
import json
from pathlib import Path

# Добавляем путь к серверу
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "server"))

async def test_text_processor_initialization():
    """Тест 1: Инициализация TextProcessor"""
    print("\n" + "="*80)
    print("ТЕСТ 1: ИНИЦИАЛИЗАЦИЯ TEXTPROCESSOR")
    print("="*80)
    
    try:
        from modules.text_processing.module import TextProcessingModule
        from config.unified_config import get_config
        
        config = get_config()
        print(f"✅ Конфигурация загружена")
        print(f"   API ключ: {config.text_processing.gemini_api_key[:10]}...{config.text_processing.gemini_api_key[-4:]}")
        print(f"   Модель: {config.text_processing.langchain_model}")
        
        # Создаем модуль
        module = TextProcessingModule()
        print(f"✅ TextProcessingModule создан")
        
        # Инициализируем с полным конфигом модуля
        # TextProcessingConfig использует unified_config как fallback,
        # поэтому можно передать пустой dict или конфиг провайдера
        module_config = config.get_module_config('text_processing')
        try:
            await module.initialize(module_config)
            print(f"✅ TextProcessingModule инициализирован успешно")
            
            # Проверяем внутренний процессор
            processor = getattr(module, '_processor', None)
            if processor:
                is_init = getattr(processor, 'is_initialized', False)
                print(f"   _processor.is_initialized: {is_init}")
                if is_init:
                    return True, module
                else:
                    print(f"   ⚠️  Процессор не инициализирован")
                    return False, None
            else:
                print(f"   ⚠️  Процессор не найден")
                return False, None
        except Exception as e:
            print(f"❌ Ошибка инициализации: {e}")
            import traceback
            traceback.print_exc()
            return False, None
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False, None

async def test_streaming_workflow(text_module, audio_module=None):
    """Тест 2: Обработка запросов через StreamingWorkflowIntegration"""
    print("\n" + "="*80)
    print("ТЕСТ 2: ОБРАБОТКА ЗАПРОСОВ ЧЕРЕЗ STREAMINGWORKFLOWINTEGRATION")
    print("="*80)
    
    try:
        from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration
        
        # Создаем интеграцию
        workflow = StreamingWorkflowIntegration(
            text_processor=text_module,
            audio_processor=audio_module
        )
        print(f"✅ StreamingWorkflowIntegration создан")
        
        # Инициализируем
        init_success = await workflow.initialize()
        if not init_success:
            print(f"❌ StreamingWorkflowIntegration не инициализирован")
            return False
        
        print(f"✅ StreamingWorkflowIntegration инициализирован")
        
        # Тестовые запросы
        test_cases = [
            {
                "name": "Простой текстовый запрос",
                "text": "Привет! Как дела?",
                "expect_command": False
            },
            {
                "name": "Запрос на открытие Safari",
                "text": "open Safari application please",
                "expect_command": True
            },
            {
                "name": "Запрос на открытие Calculator",
                "text": "open Calculator",
                "expect_command": True
            }
        ]
        
        results = []
        for i, test_case in enumerate(test_cases, 1):
            print(f"\n--- Тест {i}: {test_case['name']} ---")
            print(f"Запрос: {test_case['text']}")
            
            request_data = {
                'session_id': f'test_session_{i}',
                'hardware_id': 'test_hardware',
                'text': test_case['text'],
                'screenshot': None
            }
            
            try:
                text_responses = []
                command_payloads = []
                errors = []
                
                async for result in workflow.process_request_streaming(request_data):
                    if not result.get('success', True):
                        error = result.get('error', 'Unknown error')
                        errors.append(error)
                        print(f"   ❌ Ошибка: {error}")
                    
                    if 'text_response' in result:
                        text = result['text_response']
                        if text:
                            text_responses.append(text)
                            print(f"   📝 Текст: {text[:100]}...")
                    
                    if 'command_payload' in result:
                        cmd = result['command_payload']
                        command_payloads.append(cmd)
                        print(f"   🎯 Команда: {cmd}")
                
                # Анализ результатов
                has_text = len(text_responses) > 0
                has_command = len(command_payloads) > 0
                
                if has_text or has_command:
                    print(f"   ✅ Ответ получен")
                    if has_text:
                        print(f"      - Текст: {len(text_responses)} сегмент(ов)")
                    if has_command:
                        print(f"      - Команды: {len(command_payloads)}")
                        
                        # Проверяем формат команды
                        for cmd in command_payloads:
                            if isinstance(cmd, dict):
                                payload = cmd.get('payload', {})
                                command = payload.get('command', '')
                                args = payload.get('args', {})
                                print(f"         Команда: {command}, Аргументы: {args}")
                else:
                    print(f"   ⚠️  Ответ не получен")
                
                # Проверяем ожидания
                if test_case['expect_command']:
                    if has_command:
                        print(f"   ✅ Команда найдена (как ожидалось)")
                        results.append(True)
                    else:
                        print(f"   ⚠️  Команда не найдена (ожидалась)")
                        results.append(False)
                else:
                    if has_text and not has_command:
                        print(f"   ✅ Только текст (как ожидалось)")
                        results.append(True)
                    else:
                        print(f"   ⚠️  Неожиданный формат ответа")
                        results.append(False)
                
                if errors:
                    print(f"   ❌ Ошибки: {errors}")
                    results.append(False)
                
            except Exception as e:
                print(f"   ❌ Исключение: {e}")
                import traceback
                traceback.print_exc()
                results.append(False)
            
            # Пауза между запросами
            if i < len(test_cases):
                await asyncio.sleep(1)
        
        # Итоги
        passed = sum(1 for r in results if r)
        total = len(results)
        print(f"\n📊 Результат: {passed}/{total} тестов пройдено")
        
        return passed == total
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    """Основная функция"""
    print("\n" + "="*80)
    print("ПОЛНЫЙ ТЕСТ СЕРВЕРА")
    print("="*80)
    
    # Тест 1: Инициализация
    success, text_module = await test_text_processor_initialization()
    if not success:
        print("\n❌ Тест 1 провален - невозможно продолжить")
        return 1
    
    # Тест 2: Обработка запросов
    success = await test_streaming_workflow(text_module)
    if not success:
        print("\n⚠️  Тест 2 провален")
        return 1
    
    # Итоги
    print("\n" + "="*80)
    print("ИТОГИ")
    print("="*80)
    print("✅ Все тесты пройдены успешно!")
    print("\n🎉 Сервер готов к работе:")
    print("   - TextProcessor инициализирован")
    print("   - StreamingWorkflowIntegration работает")
    print("   - Запросы обрабатываются корректно")
    print("   - Команды извлекаются правильно")
    
    return 0

if __name__ == "__main__":
    sys.exit(asyncio.run(main()))

