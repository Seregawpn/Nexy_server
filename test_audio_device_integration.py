#!/usr/bin/env python3
"""
Тест AudioDeviceIntegration - проверка событий и публикации устройств
"""

import asyncio
import logging
import sys
import os
from typing import Dict, Any, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.audio_device_integration import AudioDeviceIntegration
from modules.mode_management.core.types import AppMode

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MockConfig:
    """Мок-конфигурация для тестирования"""
    def __init__(self):
        self.simulate = False
        self.auto_switch_enabled = True
        self.monitoring_interval = 1.0
        self.switch_delay = 0.5
        self.input_device_priorities = {
            'airpods': 1,
            'macbook air microphone': 7,
            'iphone microphone': 10,
        }
        self.output_device_priorities = {
            'airpods': 1,
            'macbook air speakers': 8,
        }
        self.device_manager = {
            'device_priorities': {
                'airpods': 1,
                'beats': 2,
                'bluetooth_headphones': 3,
                'bluetooth_speakers': 4,
                'usb_headphones': 5,
                'usb_microphone': 6,
                'builtin_microphone': 7,
                'wireless_microphone': 8,
                'external_microphone': 9,
                'iphone_microphone': 10,
                'default_input': 11,
                'macbook_air_microphone': 7
            }
        }

class AudioDeviceIntegrationTester:
    """Тестер AudioDeviceIntegration"""
    
    def __init__(self):
        self.event_bus = EventBus()
        self.state_manager = ApplicationStateManager()
        self.error_handler = ErrorHandler(self.event_bus)
        self.integration = None
        self.received_events = []
        self.test_results = {}
        
    async def setup(self):
        """Настройка тестера"""
        logger.info("🔧 Настройка AudioDeviceIntegration...")
        
        # Подписываемся на события для мониторинга
        await self.event_bus.subscribe("audio.input_device_selected", self._on_input_device_selected)
        await self.event_bus.subscribe("audio.output_device_selected", self._on_output_device_selected)
        await self.event_bus.subscribe("audio.microphone_enabled", self._on_microphone_enabled)
        await self.event_bus.subscribe("audio.microphone_disabled", self._on_microphone_disabled)
        await self.event_bus.subscribe("audio.unified_device_selected", self._on_unified_device_selected)
        
        # Создаем интеграцию
        config = MockConfig()
        self.integration = AudioDeviceIntegration(
            self.event_bus, 
            self.state_manager, 
            self.error_handler, 
            config
        )
        
        logger.info("✅ AudioDeviceIntegration настроен")
        
    async def _on_input_device_selected(self, event_data):
        """Обработчик события выбора INPUT устройства"""
        logger.info(f"📡 Получено событие audio.input_device_selected: {event_data.get('data', event_data).get('name')}")
        self.received_events.append(("audio.input_device_selected", event_data))
        
    async def _on_output_device_selected(self, event_data):
        """Обработчик события выбора OUTPUT устройства"""
        logger.info(f"📡 Получено событие audio.output_device_selected: {event_data.get('data', event_data).get('name')}")
        self.received_events.append(("audio.output_device_selected", event_data))
        
    async def _on_microphone_enabled(self, event_data):
        """Обработчик события включения микрофона"""
        logger.info(f"📡 Получено событие audio.microphone_enabled")
        self.received_events.append(("audio.microphone_enabled", event_data))
        
    async def _on_microphone_disabled(self, event_data):
        """Обработчик события выключения микрофона"""
        logger.info(f"📡 Получено событие audio.microphone_disabled")
        self.received_events.append(("audio.microphone_disabled", event_data))
        
    async def _on_unified_device_selected(self, event_data):
        """Обработчик события выбора унифицированного устройства"""
        logger.info(f"📡 Получено событие audio.unified_device_selected")
        self.received_events.append(("audio.unified_device_selected", event_data))
    
    async def test_initialization(self):
        """Тест инициализации"""
        logger.info("🔧 ТЕСТ: Инициализация")
        
        try:
            await self.integration.initialize()
            
            # Проверяем что AudioDeviceManager создан
            manager_created = self.integration._manager is not None
            logger.info(f"📊 AudioDeviceManager создан: {'✅' if manager_created else '❌'}")
            
            self.test_results['initialization'] = {
                'manager_created': manager_created,
                'success': manager_created
            }
            
            return manager_created
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации: {e}")
            self.test_results['initialization'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_startup(self):
        """Тест запуска"""
        logger.info("🚀 ТЕСТ: Запуск")
        
        try:
            await self.integration.start()
            
            # Проверяем что интеграция запущена
            is_running = self.integration._manager.is_running if self.integration._manager else False
            logger.info(f"📊 Интеграция запущена: {'✅' if is_running else '❌'}")
            
            self.test_results['startup'] = {
                'is_running': is_running,
                'success': is_running
            }
            
            return is_running
            
        except Exception as e:
            logger.error(f"❌ Ошибка запуска: {e}")
            self.test_results['startup'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_device_events(self):
        """Тест событий устройств"""
        logger.info("📡 ТЕСТ: События устройств")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Ждем немного для получения событий инициализации
            await asyncio.sleep(2)
            
            # Проверяем что получили события
            input_events = [e for e in self.received_events if e[0] == "audio.input_device_selected"]
            output_events = [e for e in self.received_events if e[0] == "audio.output_device_selected"]
            
            logger.info(f"📊 INPUT событий получено: {len(input_events)}")
            logger.info(f"📊 OUTPUT событий получено: {len(output_events)}")
            
            # Проверяем что события содержат правильные данные
            events_valid = True
            for event_type, event_data in self.received_events:
                device_data = event_data.get('data', event_data)
                if 'portaudio_index' not in device_data:
                    logger.warning(f"⚠️ Событие {event_type} не содержит portaudio_index")
                    events_valid = False
            
            success = len(input_events) > 0 and len(output_events) > 0 and events_valid
            
            self.test_results['device_events'] = {
                'input_events': len(input_events),
                'output_events': len(output_events),
                'events_valid': events_valid,
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования событий: {e}")
            self.test_results['device_events'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_microphone_control(self):
        """Тест управления микрофоном"""
        logger.info("🎤 ТЕСТ: Управление микрофоном")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Включаем микрофон
            await self.integration._enable_microphone()
            await asyncio.sleep(0.5)
            
            # Проверяем что получили событие включения
            enabled_events = [e for e in self.received_events if e[0] == "audio.microphone_enabled"]
            input_events = [e for e in self.received_events if e[0] == "audio.input_device_selected"]
            
            logger.info(f"📊 Событий включения микрофона: {len(enabled_events)}")
            logger.info(f"📊 Событий выбора INPUT устройства: {len(input_events)}")
            
            # Выключаем микрофон
            await self.integration._disable_microphone()
            await asyncio.sleep(0.5)
            
            # Проверяем что получили событие выключения
            disabled_events = [e for e in self.received_events if e[0] == "audio.microphone_disabled"]
            
            logger.info(f"📊 Событий выключения микрофона: {len(disabled_events)}")
            
            success = len(enabled_events) > 0 and len(disabled_events) > 0 and len(input_events) > 0
            
            self.test_results['microphone_control'] = {
                'enabled_events': len(enabled_events),
                'disabled_events': len(disabled_events),
                'input_events': len(input_events),
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка управления микрофоном: {e}")
            self.test_results['microphone_control'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_mode_changes(self):
        """Тест изменений режимов"""
        logger.info("🔄 ТЕСТ: Изменения режимов")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Симулируем изменение режима на LISTENING
            await self.event_bus.publish("app.mode_changed", {
                "mode": AppMode.LISTENING.value,
                "previous_mode": AppMode.SLEEPING.value
            })
            await asyncio.sleep(0.5)
            
            # Симулируем изменение режима на PROCESSING
            await self.event_bus.publish("app.mode_changed", {
                "mode": AppMode.PROCESSING.value,
                "previous_mode": AppMode.LISTENING.value
            })
            await asyncio.sleep(0.5)
            
            # Проверяем что получили события
            enabled_events = [e for e in self.received_events if e[0] == "audio.microphone_enabled"]
            disabled_events = [e for e in self.received_events if e[0] == "audio.microphone_disabled"]
            
            logger.info(f"📊 Событий включения микрофона: {len(enabled_events)}")
            logger.info(f"📊 Событий выключения микрофона: {len(disabled_events)}")
            
            # Микрофон должен включаться в LISTENING и выключаться в PROCESSING
            success = len(enabled_events) > 0 and len(disabled_events) > 0
            
            self.test_results['mode_changes'] = {
                'enabled_events': len(enabled_events),
                'disabled_events': len(disabled_events),
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования изменений режимов: {e}")
            self.test_results['mode_changes'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_device_requests(self):
        """Тест запросов устройств"""
        logger.info("🔍 ТЕСТ: Запросы устройств")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Запрашиваем текущее INPUT устройство
            await self.event_bus.publish("audio.request_current_input_device", {
                "session_id": "test_session",
                "source": "test"
            })
            await asyncio.sleep(0.5)
            
            # Запрашиваем унифицированное устройство
            await self.event_bus.publish("audio.request_unified_device", {
                "session_id": "test_session",
                "source": "test"
            })
            await asyncio.sleep(0.5)
            
            # Проверяем что получили ответы
            input_events = [e for e in self.received_events if e[0] == "audio.input_device_selected"]
            unified_events = [e for e in self.received_events if e[0] == "audio.unified_device_selected"]
            
            logger.info(f"📊 Ответов на запрос INPUT устройства: {len(input_events)}")
            logger.info(f"📊 Ответов на запрос унифицированного устройства: {len(unified_events)}")
            
            success = len(input_events) > 0 and len(unified_events) > 0
            
            self.test_results['device_requests'] = {
                'input_responses': len(input_events),
                'unified_responses': len(unified_events),
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования запросов устройств: {e}")
            self.test_results['device_requests'] = {'success': False, 'error': str(e)}
            return False
    
    async def run_all_tests(self):
        """Запуск всех тестов"""
        logger.info("🚀 ЗАПУСК ТЕСТОВ AudioDeviceIntegration")
        
        await self.setup()
        
        tests = [
            ("Инициализация", self.test_initialization),
            ("Запуск", self.test_startup),
            ("События устройств", self.test_device_events),
            ("Управление микрофоном", self.test_microphone_control),
            ("Изменения режимов", self.test_mode_changes),
            ("Запросы устройств", self.test_device_requests)
        ]
        
        results = {}
        for test_name, test_func in tests:
            logger.info(f"\n{'='*50}")
            logger.info(f"🧪 {test_name}")
            logger.info(f"{'='*50}")
            
            try:
                result = await test_func()
                results[test_name] = result
                logger.info(f"✅ {test_name}: {'ПРОЙДЕН' if result else 'ПРОВАЛЕН'}")
            except Exception as e:
                logger.error(f"❌ {test_name}: ОШИБКА - {e}")
                results[test_name] = False
        
        # Итоговый отчет
        logger.info(f"\n{'='*50}")
        logger.info("📊 ИТОГОВЫЙ ОТЧЕТ")
        logger.info(f"{'='*50}")
        
        passed = sum(1 for result in results.values() if result)
        total = len(results)
        
        for test_name, result in results.items():
            status = "✅ ПРОЙДЕН" if result else "❌ ПРОВАЛЕН"
            logger.info(f"  {test_name}: {status}")
        
        logger.info(f"\n🎯 РЕЗУЛЬТАТ: {passed}/{total} тестов пройдено")
        
        if passed == total:
            logger.info("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
        else:
            logger.warning(f"⚠️ {total - passed} тестов провалено")
        
        return passed == total

async def main():
    """Главная функция"""
    tester = AudioDeviceIntegrationTester()
    success = await tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
