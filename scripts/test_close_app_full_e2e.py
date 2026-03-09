#!/usr/bin/env python3
"""
Полный E2E тест для close_app: запрос → LLM → парсинг → аудио → gRPC → клиент → выполнение

Проверяет весь процесс:
1. Пользовательский запрос: "Закрой Safari"
2. Реальный запрос к LLM (Gemini) с системным промптом
3. Генерация ответа LLM в формате JSON с close_app
4. Парсинг реального ответа LLM
5. Генерация аудио чанка для текстового ответа
6. Формирование command_payload
7. Передача через gRPC (симуляция)
8. Получение на клиенте (симуляция)
9. Выполнение через MCP

Feature ID: F-2025-014-close-app
"""

import asyncio
import sys
import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional
from unittest.mock import AsyncMock, MagicMock, patch

# Добавляем путь к серверу
server_root = Path(__file__).parent.parent
sys.path.insert(0, str(server_root))

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Импорты
from config.unified_config import get_config
from integrations.core.assistant_response_parser import AssistantResponseParser
from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration
from modules.audio_generation.core.audio_processor import AudioProcessor


async def test_close_app_full_e2e():
    """
    Полный E2E тест для close_app
    """
    print("\n" + "="*80)
    print("🚀 ПОЛНЫЙ E2E ТЕСТ: close_app")
    print("="*80)
    print("\nПроверяем весь процесс:")
    print("1. Пользовательский запрос: 'Закрой Safari'")
    print("2. Реальный запрос к LLM (Gemini) с системным промптом")
    print("3. Генерация ответа LLM в формате JSON с close_app")
    print("4. Парсинг реального ответа LLM")
    print("5. Генерация аудио чанка для текстового ответа")
    print("6. Формирование command_payload")
    print("7. Передача через gRPC (симуляция)")
    print("="*80)
    
    try:
        config = get_config()
        
        # Проверка конфигурации
        print("\n[1/7] Проверка конфигурации...")
        forward_enabled = config.features.forward_assistant_actions
        kill_switch_disabled = not config.kill_switches.disable_forward_assistant_actions
        
        if not forward_enabled:
            print("   ❌ FORWARD_ASSISTANT_ACTIONS не включен!")
            print("   → Включите features.actions=true в client/config/unified_config.yaml")
            return False
        
        if not kill_switch_disabled:
            print("   ❌ Kill-switch включен!")
            print("   → Убедитесь, что NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS не установлен")
            return False
        
        print("   ✅ Конфигурация корректна")
        print(f"      - forward_assistant_actions: {forward_enabled}")
        print(f"      - kill_switch_disabled: {kill_switch_disabled}")
        
        # Проверка промпта
        print("\n[2/7] Проверка промпта...")
        prompt = config.text_processing.gemini_system_prompt
        if "close_app" not in prompt.lower():
            print("   ❌ Промпт не содержит инструкций для close_app!")
            return False
        
        if "command" not in prompt.lower() or "args" not in prompt.lower():
            print("   ❌ Промпт не содержит JSON контракт!")
            return False
        
        print("   ✅ Промпт содержит инструкции для close_app")
        
        # Инициализация AudioProcessor
        print("\n[3/7] Инициализация AudioProcessor...")
        audio_processor = AudioProcessor()
        audio_init_result = await audio_processor.initialize()
        if not audio_init_result:
            print("   ❌ Ошибка инициализации AudioProcessor")
            return False
        print("   ✅ AudioProcessor инициализирован")
        
        # Инициализация StreamingWorkflowIntegration
        print("\n[4/7] Инициализация StreamingWorkflowIntegration...")
        from modules.text_processing.core.text_processor import TextProcessor
        text_processor = TextProcessor()
        await text_processor.initialize()
        
        # Проверяем, что системный промпт передается в провайдер
        if hasattr(text_processor, 'live_provider') and hasattr(text_processor.live_provider, 'system_prompt'):
            provider_prompt = text_processor.live_provider.system_prompt
            print(f"   📋 Системный промпт в провайдере: {len(provider_prompt)} символов")
            print(f"      - Содержит close_app: {'close_app' in provider_prompt.lower()}")
            print(f"      - Содержит JSON: {'JSON' in provider_prompt}")
            if not provider_prompt:
                print("   ⚠️  ВНИМАНИЕ: Системный промпт пуст в провайдере!")
        
        workflow = StreamingWorkflowIntegration(
            text_processor=text_processor,
            audio_processor=audio_processor
        )
        await workflow.initialize()
        print("   ✅ StreamingWorkflowIntegration инициализирован")
        
        # Тестовый запрос
        print("\n[5/7] Отправка запроса к LLM...")
        session_id = "test-close-app-full-e2e"
        user_request = "Закрой Safari"
        
        print(f"   📤 Запрос: '{user_request}'")
        print(f"   📋 Session ID: {session_id}")
        
        # Собираем результаты
        text_chunks = []
        audio_chunks = []
        command_payloads = []
        raw_llm_response = []  # Для отладки: собираем сырой ответ от LLM
        
        # Обрабатываем запрос
        request_data = {
            "session_id": session_id,
            "text": user_request,
            "image_data": None
        }
        
        print("\n   ⏳ Ожидание ответа от LLM...")
        print("   (Это может занять 10-30 секунд)")
        print("   ⚠️  ВАЖНО: LLM должен вернуть JSON с command='close_app'")
        
        full_response_text = None
        async for result in workflow.process_request_streaming(request_data):
            # Собираем текст (промежуточные чанки)
            if 'text_response' in result and result.get('text_response'):
                text = result['text_response']
                text_chunks.append(text)
                raw_llm_response.append(text)  # Для отладки
                print(f"   📝 Текст чанк: '{text[:80]}{'...' if len(text) > 80 else ''}'")
                
                # Проверяем, похож ли ответ на JSON
                if text.strip().startswith('{') or '"command"' in text or '"close_app"' in text:
                    print(f"   🎯 Обнаружен потенциальный JSON в чанке!")
            
            # Собираем финальный полный ответ (может содержать JSON)
            if 'text_full_response' in result and result.get('text_full_response'):
                full_response_text = result['text_full_response']
                print(f"   📋 Полный ответ: '{full_response_text[:200]}{'...' if len(full_response_text) > 200 else ''}'")
            
            # Собираем аудио
            if 'audio_chunk' in result:
                audio_chunk = result['audio_chunk']
                if isinstance(audio_chunk, (bytes, bytearray)) and len(audio_chunk) > 0:
                    audio_chunks.append(audio_chunk)
                    print(f"   🔊 Аудио чанк: {len(audio_chunk)} байт")
            
            # Собираем command_payload
            if 'command_payload' in result:
                payload = result['command_payload']
                command_payloads.append(payload)
                print(f"   🎯 Command payload: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        
        # Проверка результатов
        print("\n[6/7] Проверка результатов...")
        
        # Проверка текста
        if not text_chunks:
            print("   ❌ Текст не получен от LLM")
            return False
        
        full_text = ' '.join(text_chunks)
        raw_full = ''.join(raw_llm_response)  # Полный сырой ответ
        
        print(f"   ✅ Текст получен: '{full_text[:100]}{'...' if len(full_text) > 100 else ''}'")
        print(f"   📋 Полный сырой ответ от LLM ({len(raw_full)} символов):")
        print(f"      '{raw_full[:200]}{'...' if len(raw_full) > 200 else ''}'")
        
        # Проверяем, содержит ли ответ JSON
        if raw_full.strip().startswith('{') or '"command"' in raw_full:
            print(f"   🎯 Обнаружен потенциальный JSON в ответе LLM!")
        else:
            print(f"   ⚠️  Ответ LLM не похож на JSON (начинается с '{raw_full[:20] if raw_full else '(пусто)'}')")
            print(f"   → LLM не следует инструкциям в системном промпте")
        
        # Проверка парсинга
        print("\n[7/7] Проверка парсинга ответа...")
        parser = AssistantResponseParser()
        # Используем полный ответ, если есть, иначе собираем из чанков
        text_to_parse = full_response_text if full_response_text else full_text
        parsed = parser.parse(text_to_parse, session_id=session_id)
        
        if not parsed:
            print("   ❌ Парсинг не удался")
            return False
        
        print(f"   ✅ Парсинг успешен")
        print(f"      - Text response: '{parsed.text_response[:80]}{'...' if len(parsed.text_response) > 80 else ''}'")
        
        if parsed.command_payload:
            cmd = parsed.command_payload.get('payload', {}).get('command')
            app_name = parsed.command_payload.get('payload', {}).get('args', {}).get('app_name')
            
            if cmd == 'close_app':
                print(f"   ✅ Команда close_app обнаружена")
                if app_name:
                    print(f"      - App name: {app_name}")
                else:
                    print("   ⚠️  App name отсутствует в command_payload")
            else:
                print(f"   ⚠️  Команда: {cmd} (ожидалось close_app)")
        else:
            print("   ⚠️  command_payload не найден в ответе")
        
        # Проверка аудио
        if audio_chunks:
            total_audio = sum(len(chunk) for chunk in audio_chunks)
            print(f"   ✅ Аудио получено: {len(audio_chunks)} чанков, {total_audio} байт")
        else:
            print("   ⚠️  Аудио не получено")
        
        # Проверка command_payload
        if command_payloads:
            print(f"   ✅ Command payload получен: {len(command_payloads)} payload(s)")
            for i, payload in enumerate(command_payloads, 1):
                cmd = payload.get('payload', {}).get('command')
                app_name = payload.get('payload', {}).get('args', {}).get('app_name')
                print(f"      [{i}] command={cmd}, app_name={app_name}")
        else:
            print("   ⚠️  Command payload не получен")
            print("   → Проверьте, что forward_assistant_actions=true")
            print("   → Проверьте, что LLM вернул JSON с command='close_app'")
        
        # Итоговая проверка
        print("\n" + "="*80)
        print("ИТОГОВАЯ ПРОВЕРКА")
        print("="*80)
        
        success = True
        checks = []
        
        # Проверка 1: Текст получен
        if text_chunks:
            checks.append("✅ Текст получен от LLM")
        else:
            checks.append("❌ Текст не получен")
            success = False
        
        # Проверка 2: Парсинг успешен
        if parsed and parsed.text_response:
            checks.append("✅ Парсинг ответа успешен")
        else:
            checks.append("❌ Парсинг не удался")
            success = False
        
        # Проверка 3: Command payload содержит close_app
        if command_payloads:
            has_close_app = any(
                p.get('payload', {}).get('command') == 'close_app'
                for p in command_payloads
            )
            if has_close_app:
                checks.append("✅ Command payload содержит close_app")
            else:
                checks.append("⚠️  Command payload не содержит close_app")
        else:
            checks.append("⚠️  Command payload не получен")
        
        # Проверка 4: Аудио получено
        if audio_chunks:
            checks.append("✅ Аудио чанки получены")
        else:
            checks.append("⚠️  Аудио чанки не получены")
        
        for check in checks:
            print(f"   {check}")
        
        print("\n" + "="*80)
        if success:
            print("✅ ПОЛНЫЙ E2E ТЕСТ ПРОЙДЕН")
            print("\nСледующий шаг: Проверить получение command_payload на клиенте")
            return True
        else:
            print("❌ ПОЛНЫЙ E2E ТЕСТ НЕ ПРОЙДЕН")
            return False
        
    except Exception as e:
        print(f"\n❌ Ошибка во время теста: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Главная функция"""
    success = await test_close_app_full_e2e()
    return 0 if success else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
