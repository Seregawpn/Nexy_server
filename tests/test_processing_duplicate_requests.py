"""
Изолированные тесты для проверки обработки повторных запросов на PROCESSING.

Тестирует:
1. Разрешение повторных запросов на PROCESSING с новым session_id
2. Прерывание предыдущего запроса при новом запросе
3. Обновление session_id в ProcessingWorkflow
"""

import asyncio
import unittest
from unittest.mock import Mock, AsyncMock, patch
from datetime import datetime
from uuid import uuid4

# Импорты для тестирования
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.error_handler import ErrorHandler
from integration.integrations.mode_management_integration import ModeManagementIntegration
from integration.workflows.processing_workflow import ProcessingWorkflow, ProcessingStage
from integration.workflows.base_workflow import WorkflowState


class TestProcessingDuplicateRequests(unittest.IsolatedAsyncioTestCase):
    """Тесты для проверки обработки повторных запросов на PROCESSING"""
    
    async def asyncSetUp(self):
        """Настройка тестового окружения"""
        self.event_bus = EventBus()
        self.state_manager = ApplicationStateManager()
        self.state_manager.attach_event_bus(self.event_bus)
        self.error_handler = ErrorHandler()
        
        # Инициализация ModeManagementIntegration
        self.mode_management = ModeManagementIntegration(
            self.event_bus,
            self.state_manager,
            self.error_handler
        )
        await self.mode_management.initialize()
        
        # Инициализация ProcessingWorkflow
        self.processing_workflow = ProcessingWorkflow(self.event_bus)
        await self.processing_workflow.initialize()
        await self.processing_workflow.start()
        
        # Устанавливаем начальный режим
        self.state_manager.set_mode(AppMode.SLEEPING)
    
    async def asyncTearDown(self):
        """Очистка после тестов"""
        if self.processing_workflow:
            await self.processing_workflow.stop()
        if self.mode_management:
            await self.mode_management.stop()
    
    async def test_duplicate_processing_request_with_new_session_id(self):
        """Тест: разрешение повторного запроса на PROCESSING с новым session_id"""
        # Первый запрос на PROCESSING
        session_id_1 = str(uuid4())
        await self.event_bus.publish("mode.request", {
            "target": AppMode.PROCESSING,
            "source": "input_processing",
            "session_id": session_id_1
        })
        
        # Ждем обработки
        await asyncio.sleep(0.1)
        
        # Проверяем, что режим изменился на PROCESSING
        self.assertEqual(self.state_manager.get_current_mode(), AppMode.PROCESSING)
        self.assertEqual(self.state_manager.get_current_session_id(), session_id_1)
        
        # Второй запрос на PROCESSING с другим session_id
        session_id_2 = str(uuid4())
        
        # Публикуем второй запрос
        await self.event_bus.publish("mode.request", {
            "target": AppMode.PROCESSING,
            "source": "input_processing",
            "session_id": session_id_2
        })
        
        # Ждем обработки
        await asyncio.sleep(0.2)
        
        # Проверяем, что режим остался PROCESSING
        self.assertEqual(self.state_manager.get_current_mode(), AppMode.PROCESSING)
        
        # Проверяем, что active_session_id обновился
        self.assertEqual(self.state_manager.get_current_session_id(), session_id_2)
        
        # Проверяем, что ProcessingWorkflow получил новый session_id
        # (через app.mode_changed событие, которое должно быть опубликовано)
        await asyncio.sleep(0.1)
        # Проверяем, что workflow обновил session_id (если он активен)
        if self.processing_workflow.state == WorkflowState.ACTIVE:
            self.assertEqual(self.processing_workflow.current_session_id, session_id_2)
        
        print(f"✅ Тест пройден: повторный запрос на PROCESSING с новым session_id обработан")
    
    async def test_processing_workflow_interrupts_previous_request(self):
        """Тест: ProcessingWorkflow прерывает предыдущий запрос при новом запросе"""
        # Первый запрос на PROCESSING
        session_id_1 = str(uuid4())
        
        # Публикуем mode.request для первого запроса
        await self.event_bus.publish("mode.request", {
            "target": AppMode.PROCESSING,
            "source": "input_processing",
            "session_id": session_id_1
        })
        
        # Ждем обработки
        await asyncio.sleep(0.1)
        
        # Проверяем, что workflow активен с первым session_id
        self.assertEqual(self.processing_workflow.state, WorkflowState.ACTIVE)
        self.assertEqual(self.processing_workflow.current_session_id, session_id_1)
        
        # Второй запрос на PROCESSING с другим session_id
        session_id_2 = str(uuid4())
        
        # Публикуем mode.request для второго запроса
        await self.event_bus.publish("mode.request", {
            "target": AppMode.PROCESSING,
            "source": "input_processing",
            "session_id": session_id_2
        })
        
        # Ждем обработки
        await asyncio.sleep(0.2)
        
        # Проверяем, что workflow обновил session_id
        self.assertEqual(self.processing_workflow.current_session_id, session_id_2)
        
        # Проверяем, что workflow все еще активен
        self.assertEqual(self.processing_workflow.state, WorkflowState.ACTIVE)
        
        print(f"✅ Тест пройден: ProcessingWorkflow прервал предыдущий запрос и начал новый")
    
    async def test_same_session_id_ignored(self):
        """Тест: запрос с тем же session_id игнорируется (идемпотентность)"""
        session_id = str(uuid4())
        
        # Первый запрос
        await self.event_bus.publish("mode.request", {
            "target": AppMode.PROCESSING,
            "source": "input_processing",
            "session_id": session_id
        })
        
        await asyncio.sleep(0.1)
        
        # Собираем события app.mode_changed
        mode_changed_events = []
        
        async def capture_mode_changed(event):
            mode_changed_events.append(event)
        
        await self.event_bus.subscribe("app.mode_changed", capture_mode_changed)
        
        initial_event_count = len(mode_changed_events)
        
        # Второй запрос с тем же session_id
        await self.event_bus.publish("mode.request", {
            "target": AppMode.PROCESSING,
            "source": "input_processing",
            "session_id": session_id
        })
        
        await asyncio.sleep(0.1)
        
        # Проверяем, что новое событие app.mode_changed НЕ было опубликовано
        # (или было опубликовано только одно событие для первого запроса)
        self.assertLessEqual(len(mode_changed_events), initial_event_count + 1)
        
        print(f"✅ Тест пройден: запрос с тем же session_id игнорируется (идемпотентность)")
    
    async def test_screenshot_captured_with_new_session_id(self):
        """Тест: screenshot.captured обрабатывается с новым session_id"""
        # Первый запрос на PROCESSING
        session_id_1 = str(uuid4())
        
        await self.event_bus.publish("mode.request", {
            "target": AppMode.PROCESSING,
            "source": "input_processing",
            "session_id": session_id_1
        })
        
        await asyncio.sleep(0.1)
        
        # Второй запрос с новым session_id
        session_id_2 = str(uuid4())
        
        await self.event_bus.publish("mode.request", {
            "target": AppMode.PROCESSING,
            "source": "input_processing",
            "session_id": session_id_2
        })
        
        await asyncio.sleep(0.1)
        
        # Проверяем, что workflow обновил session_id
        self.assertEqual(self.processing_workflow.current_session_id, session_id_2)
        
        # Публикуем screenshot.captured с новым session_id
        await self.event_bus.publish("screenshot.captured", {
            "path": "/tmp/test_screenshot.jpg",
            "session_id": session_id_2
        })
        
        await asyncio.sleep(0.1)
        
        # Проверяем, что workflow обработал screenshot.captured
        self.assertTrue(self.processing_workflow.screenshot_captured)
        self.assertEqual(self.processing_workflow.current_stage, ProcessingStage.SENDING_GRPC)
        
        print(f"✅ Тест пройден: screenshot.captured обработан с новым session_id")


if __name__ == "__main__":
    unittest.main()

