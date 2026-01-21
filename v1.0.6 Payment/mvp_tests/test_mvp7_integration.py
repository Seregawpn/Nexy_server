#!/usr/bin/env python3
"""
Тест интеграции MVP 7: Subscription Module в Workflow

Проверяет:
1. SubscriptionModule инициализируется корректно
2. _iter_processed_sentences не падает с AttributeError
3. Subscription context добавляется в prompt
4. Порядок контекста: subscription → memory → user text
"""
import sys
import os
import asyncio
from pathlib import Path

# Добавляем путь к серверу
server_path = Path(__file__).parent.parent / "server(Payment)" / "server"
sys.path.insert(0, str(server_path))

# Добавляем путь к mvp_tests для импорта компонентов
mvp_tests_path = Path(__file__).parent
sys.path.insert(0, str(mvp_tests_path))

import logging
from unittest.mock import Mock, AsyncMock

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MockTextModule:
    """Мок текстового модуля для тестирования"""
    
    def __init__(self):
        self.is_initialized = True
    
    async def process(self, request):
        """Имитация обработки текста"""
        text = request.get('text', '')
        # Возвращаем текст как есть (имитация LLM)
        yield {'text': text}


class MockAudioModule:
    """Мок аудио модуля"""
    
    def __init__(self):
        self.is_initialized = True


async def test_subscription_context_integration():
    """Тест интеграции subscription context в workflow"""
    print("=" * 60)
    print("🧪 Тест MVP 7: Subscription Context Integration")
    print("=" * 60)
    
    # Проверяем наличие yaml модуля
    try:
        import yaml
    except ImportError:
        print("⚠️  Модуль yaml не установлен, пропускаем тест")
        print("   Установите PyYAML: pip install pyyaml")
        print("   Или запустите тест в полном окружении сервера")
        return True  # Пропускаем тест, но не считаем это ошибкой
    
    try:
        from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration
        
        # Создаем моки модулей
        text_module = MockTextModule()
        audio_module = MockAudioModule()
        
        # Создаем workflow интеграцию
        workflow = StreamingWorkflowIntegration(
            text_processor=text_module,
            audio_processor=audio_module,
            memory_workflow=None,
            text_filter_manager=None,
            coordinator=None
        )
        
        print("✅ StreamingWorkflowIntegration создан")
        
        # Инициализируем
        init_success = await workflow.initialize()
        if not init_success:
            print("❌ StreamingWorkflowIntegration не инициализирован")
            return False
        
        print("✅ StreamingWorkflowIntegration инициализирован")
        
        # Проверяем, что subscription_module создан (если DATABASE_URL установлен)
        if workflow.subscription_module:
            print("✅ SubscriptionModule инициализирован")
        else:
            print("⚠️ SubscriptionModule не инициализирован (DATABASE_URL не установлен?)")
        
        # Тест 1: Проверка _enrich_with_subscription_and_memory
        print("\n📝 Тест 1: Проверка _enrich_with_subscription_and_memory")
        test_text = "Hello, how are you?"
        subscription_context = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nSubscription Information:\nStatus: paid_trial\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        memory_context = {'recent_context': 'User asked about weather yesterday'}
        
        enriched = workflow._enrich_with_subscription_and_memory(
            test_text,
            subscription_context,
            memory_context
        )
        
        print(f"   Исходный текст: {test_text[:50]}...")
        print(f"   Обогащенный текст (первые 200 символов): {enriched[:200]}...")
        
        # Проверяем порядок: subscription → memory → user text
        assert subscription_context in enriched, "Subscription context должен быть в тексте"
        assert "Memory context" in enriched or "Контекст" in enriched, "Memory context должен быть в тексте"
        assert test_text in enriched, "Текст пользователя должен быть в тексте"
        
        # Проверяем порядок (subscription должен быть первым)
        subscription_pos = enriched.find(subscription_context)
        memory_pos = enriched.find("Memory context") if "Memory context" in enriched else enriched.find("Контекст")
        user_pos = enriched.find(test_text)
        
        assert subscription_pos < memory_pos < user_pos, "Порядок должен быть: subscription → memory → user"
        
        print("   ✅ Порядок контекста корректен: subscription → memory → user")
        
        # Тест 2: Проверка _iter_processed_sentences без subscription context
        print("\n📝 Тест 2: _iter_processed_sentences без subscription context")
        sentences = []
        async for sentence in workflow._iter_processed_sentences(
            test_text,
            None,
            memory_context,
            ""  # Пустой subscription context
        ):
            sentences.append(sentence)
        
        assert len(sentences) > 0, "Должен быть хотя бы один sentence"
        print(f"   ✅ Получено {len(sentences)} предложений")
        
        # Тест 3: Проверка _iter_processed_sentences с subscription context
        print("\n📝 Тест 3: _iter_processed_sentences с subscription context")
        sentences_with_sub = []
        async for sentence in workflow._iter_processed_sentences(
            test_text,
            None,
            memory_context,
            subscription_context
        ):
            sentences_with_sub.append(sentence)
        
        assert len(sentences_with_sub) > 0, "Должен быть хотя бы один sentence"
        
        # Проверяем, что subscription context присутствует в первом предложении
        first_sentence = " ".join(sentences_with_sub)
        assert subscription_context in first_sentence or "Subscription Information" in first_sentence, \
            "Subscription context должен быть в ответе"
        
        print(f"   ✅ Получено {len(sentences_with_sub)} предложений с subscription context")
        
        # Тест 4: Проверка без subscription_context (fallback)
        print("\n📝 Тест 4: Fallback без subscription context")
        sentences_fallback = []
        async for sentence in workflow._iter_processed_sentences(
            test_text,
            None,
            memory_context
            # subscription_context не передается (используется значение по умолчанию)
        ):
            sentences_fallback.append(sentence)
        
        assert len(sentences_fallback) > 0, "Должен быть хотя бы один sentence"
        print(f"   ✅ Fallback работает: получено {len(sentences_fallback)} предложений")
        
        print("\n" + "=" * 60)
        print("✅ Все тесты пройдены успешно!")
        print("=" * 60)
        return True
        
    except AttributeError as e:
        print(f"\n❌ AttributeError: {e}")
        import traceback
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = asyncio.run(test_subscription_context_integration())
    sys.exit(0 if success else 1)





