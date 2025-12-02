#!/usr/bin/env python3
"""
Тест голосового фидбека при ошибках открытия приложений (F-2025-016).

Проверяет, что при попытке открыть несуществующее приложение
система публикует speech.playback.request с правильным текстом.

Feature ID: F-2025-016-mcp-app-opening-integration
"""

import asyncio
import sys
import os
import json
import logging
from pathlib import Path

# Добавляем путь к модулям
sys.path.insert(0, str(Path(__file__).parent.parent))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.action_execution_integration import ActionExecutionIntegration, FEATURE_ID
from modules.action_executor import ActionResult

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(name)s] - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SpeechFeedbackTester:
    """Тестер голосового фидбека при ошибках."""
    
    def __init__(self):
        self.event_bus = EventBus()
        self.state_manager = ApplicationStateManager()
        self.error_handler = ErrorHandler()
        self.integration = None
        self.received_events = []
        self.speech_events = []
        
    async def setup(self):
        """Инициализация интеграции."""
        logger.info("🔧 Инициализация ActionExecutionIntegration...")
        self.integration = ActionExecutionIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
        )
        
        await self.integration.initialize()
        await self.integration.start()
        
        # Подписываемся на события для проверки
        await self.event_bus.subscribe("actions.open_app.failed", self._on_failed)
        await self.event_bus.subscribe("speech.playback.request", self._on_speech_request)
        
        logger.info("✅ Интеграция инициализирована")
        
    async def _on_failed(self, event):
        """Обработчик события failed."""
        data = event.get("data", event)
        logger.info(f"📢 Получено событие actions.open_app.failed: {data}")
        self.received_events.append(("actions.open_app.failed", data))
        
    async def _on_speech_request(self, event):
        """Обработчик события speech.playback.request."""
        data = event.get("data", event)
        logger.info(f"🔊 Получено событие speech.playback.request: {data}")
        self.speech_events.append(data)
        
    async def test_nonexistent_app(self, app_name: str = "FooBarNonExistentApp"):
        """Тест: попытка открыть несуществующее приложение."""
        logger.info(f"\n{'='*60}")
        logger.info(f"🧪 ТЕСТ: Попытка открыть несуществующее приложение '{app_name}'")
        logger.info(f"{'='*60}\n")
        
        # Очищаем предыдущие события
        self.received_events.clear()
        self.speech_events.clear()
        
        # Создаём событие как будто от gRPC клиента
        session_id = f"test-session-{int(asyncio.get_event_loop().time() * 1000)}"
        event = {
            "session_id": session_id,
            "action_json": json.dumps({
                "command": "open_app",
                "args": {"app_name": app_name}
            }),
            "feature_id": FEATURE_ID,
        }
        
        logger.info(f"📤 Отправляем событие grpc.response.action для '{app_name}'...")
        
        # Мокаем executor чтобы он возвращал ошибку app_not_found
        from unittest.mock import patch
        with patch.object(self.integration._executor, 'execute') as mock_execute:
            mock_execute.return_value = ActionResult(
                success=False,
                message=f"Application '{app_name}' not found",
                error="app_not_found",
                app_name=app_name
            )
            
            # Публикуем событие
            await self.event_bus.publish("grpc.response.action", event)
            
            # Ждём обработки
            await asyncio.sleep(0.5)
            
        # Проверяем результаты
        logger.info(f"\n{'='*60}")
        logger.info("📊 РЕЗУЛЬТАТЫ ТЕСТА")
        logger.info(f"{'='*60}\n")
        
        # Проверка 1: Событие failed должно быть опубликовано
        failed_events = [e for e in self.received_events if e[0] == "actions.open_app.failed"]
        if failed_events:
            logger.info("✅ Событие actions.open_app.failed опубликовано")
            failed_data = failed_events[0][1]
            logger.info(f"   - error: {failed_data.get('error')}")
            logger.info(f"   - session_id: {failed_data.get('session_id')}")
            logger.info(f"   - feature_id: {failed_data.get('feature_id')}")
            
            if failed_data.get('error') == "app_not_found":
                logger.info("   ✅ Код ошибки правильный: app_not_found")
            else:
                logger.error(f"   ❌ Неправильный код ошибки: {failed_data.get('error')}")
        else:
            logger.error("❌ Событие actions.open_app.failed НЕ опубликовано!")
            
        # Проверка 2: Событие speech.playback.request должно быть опубликовано
        if self.speech_events:
            logger.info("✅ Событие speech.playback.request опубликовано")
            speech_data = self.speech_events[0]
            logger.info(f"   - text: '{speech_data.get('text')}'")
            logger.info(f"   - session_id: {speech_data.get('session_id')}")
            logger.info(f"   - feature_id: {speech_data.get('feature_id')}")
            logger.info(f"   - source: {speech_data.get('source')}")
            logger.info(f"   - priority: {speech_data.get('priority')}")
            logger.info(f"   - voice: {speech_data.get('voice')}")
            
            # Проверяем правильность текста
            expected_text = f"The app {app_name} isn't installed on this Mac."
            actual_text = speech_data.get('text', '')
            if actual_text == expected_text:
                logger.info(f"   ✅ Текст сообщения правильный!")
            else:
                logger.error(f"   ❌ Неправильный текст!")
                logger.error(f"      Ожидалось: '{expected_text}'")
                logger.error(f"      Получено:  '{actual_text}'")
                
            # Проверяем метаданные
            checks = [
                (speech_data.get('session_id') == session_id, "session_id"),
                (speech_data.get('feature_id') == FEATURE_ID, "feature_id"),
                (speech_data.get('source') == "actions.open_app", "source"),
                (speech_data.get('priority') == "high", "priority"),
                (speech_data.get('voice') == "en-US", "voice"),
            ]
            
            for check, name in checks:
                if check:
                    logger.info(f"   ✅ {name} правильный")
                else:
                    logger.error(f"   ❌ {name} неправильный: {speech_data.get(name)}")
        else:
            logger.error("❌ Событие speech.playback.request НЕ опубликовано!")
            logger.error("   Проверьте, что speak_errors=True в конфиге")
            
        # Итоговый результат
        success = len(failed_events) > 0 and len(self.speech_events) > 0
        if success:
            logger.info(f"\n🎉 ТЕСТ ПРОЙДЕН: Голосовой фидбек работает корректно!")
        else:
            logger.error(f"\n❌ ТЕСТ НЕ ПРОЙДЕН: Проблемы с публикацией событий")
            
        return success
        
    async def cleanup(self):
        """Очистка ресурсов."""
        if self.integration:
            await self.integration.stop()
        logger.info("🧹 Очистка завершена")


async def main():
    """Главная функция."""
    tester = SpeechFeedbackTester()
    
    try:
        await tester.setup()
        
        # Тест 1: Несуществующее приложение
        result1 = await tester.test_nonexistent_app("FooBarNonExistentApp")
        
        # Небольшая пауза между тестами
        await asyncio.sleep(0.5)
        
        # Тест 2: Другое несуществующее приложение
        result2 = await tester.test_nonexistent_app("AnotherNonExistentApp")
        
        # Итоговый результат
        logger.info(f"\n{'='*60}")
        logger.info("📋 ИТОГОВЫЙ РЕЗУЛЬТАТ")
        logger.info(f"{'='*60}\n")
        
        if result1 and result2:
            logger.info("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО")
            return 0
        else:
            logger.error("❌ НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОЙДЕНЫ")
            return 1
            
    except Exception as e:
        logger.error(f"❌ Ошибка при выполнении тестов: {e}", exc_info=True)
        return 1
    finally:
        await tester.cleanup()


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)



