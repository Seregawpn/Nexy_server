#!/usr/bin/env python3
"""
Тест потока событий между модулями - проверка корректной передачи событий
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
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
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
        self.language = "en-US"
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

class EventFlowTester:
    """Тестер потока событий"""
    
    def __init__(self):
        self.event_bus = EventBus()
        self.state_manager = ApplicationStateManager()
        self.error_handler = ErrorHandler(self.event_bus)
        self.audio_integration = None
        self.voice_integration = None
        self.received_events = []
        self.test_results = {}
        
    async def setup(self):
        """Настройка тестера"""
        logger.info("🔧 Настройка тестера потока событий...")
        
        # Подписываемся на все ключевые события
        await self.event_bus.subscribe("audio.input_device_selected", self._on_input_device_selected)
        await self.event_bus.subscribe("audio.output_device_selected", self._on_output_device_selected)
        await self.event_bus.subscribe("audio.microphone_enabled", self._on_microphone_enabled)
        await self.event_bus.subscribe("audio.microphone_disabled", self._on_microphone_disabled)
        await self.event_bus.subscribe("voice.recording_start", self._on_recording_start)
        await self.event_bus.subscribe("voice.recording_stop", self._on_recording_stop)
        await self.event_bus.subscribe("voice.mic_opened", self._on_mic_opened)
        await self.event_bus.subscribe("voice.mic_closed", self._on_mic_closed)
        await self.event_bus.subscribe("app.mode_changed", self._on_mode_changed)
        
        # Создаем интеграции
        config = MockConfig()
        self.audio_integration = AudioDeviceIntegration(
            self.event_bus, 
            self.state_manager, 
            self.error_handler, 
            config
        )
        self.voice_integration = VoiceRecognitionIntegration(
            self.event_bus, 
            self.state_manager, 
            self.error_handler, 
            config
        )
        
        logger.info("✅ Тестер потока событий настроен")
        
    async def _on_input_device_selected(self, event_data):
        """Обработчик события выбора INPUT устройства"""
        device_name = event_data.get('data', event_data).get('name', 'Unknown')
        portaudio_index = event_data.get('data', event_data).get('portaudio_index')
        logger.info(f"📡 [EVENT_FLOW] audio.input_device_selected: {device_name} (index: {portaudio_index})")
        self.received_events.append(("audio.input_device_selected", event_data))
        
    async def _on_output_device_selected(self, event_data):
        """Обработчик события выбора OUTPUT устройства"""
        device_name = event_data.get('data', event_data).get('name', 'Unknown')
        portaudio_index = event_data.get('data', event_data).get('portaudio_index')
        logger.info(f"📡 [EVENT_FLOW] audio.output_device_selected: {device_name} (index: {portaudio_index})")
        self.received_events.append(("audio.output_device_selected", event_data))
        
    async def _on_microphone_enabled(self, event_data):
        """Обработчик события включения микрофона"""
        logger.info(f"📡 [EVENT_FLOW] audio.microphone_enabled")
        self.received_events.append(("audio.microphone_enabled", event_data))
        
    async def _on_microphone_disabled(self, event_data):
        """Обработчик события выключения микрофона"""
        logger.info(f"📡 [EVENT_FLOW] audio.microphone_disabled")
        self.received_events.append(("audio.microphone_disabled", event_data))
        
    async def _on_recording_start(self, event_data):
        """Обработчик события начала записи"""
        logger.info(f"📡 [EVENT_FLOW] voice.recording_start")
        self.received_events.append(("voice.recording_start", event_data))
        
    async def _on_recording_stop(self, event_data):
        """Обработчик события остановки записи"""
        logger.info(f"📡 [EVENT_FLOW] voice.recording_stop")
        self.received_events.append(("voice.recording_stop", event_data))
        
    async def _on_mic_opened(self, event_data):
        """Обработчик события открытия микрофона"""
        logger.info(f"📡 [EVENT_FLOW] voice.mic_opened")
        self.received_events.append(("voice.mic_opened", event_data))
        
    async def _on_mic_closed(self, event_data):
        """Обработчик события закрытия микрофона"""
        logger.info(f"📡 [EVENT_FLOW] voice.mic_closed")
        self.received_events.append(("voice.mic_closed", event_data))
        
    async def _on_mode_changed(self, event_data):
        """Обработчик события изменения режима"""
        mode = event_data.get('mode', 'unknown')
        logger.info(f"📡 [EVENT_FLOW] app.mode_changed: {mode}")
        self.received_events.append(("app.mode_changed", event_data))
    
    async def test_initialization_flow(self):
        """Тест потока событий при инициализации"""
        logger.info("🔧 ТЕСТ: Поток событий при инициализации")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Инициализируем интеграции
            await self.audio_integration.initialize()
            await self.audio_integration.start()
            await self.voice_integration.initialize()
            
            # Ждем события инициализации
            await asyncio.sleep(2)
            
            # Анализируем полученные события
            input_events = [e for e in self.received_events if e[0] == "audio.input_device_selected"]
            output_events = [e for e in self.received_events if e[0] == "audio.output_device_selected"]
            mic_enabled_events = [e for e in self.received_events if e[0] == "audio.microphone_enabled"]
            mic_disabled_events = [e for e in self.received_events if e[0] == "audio.microphone_disabled"]
            mode_events = [e for e in self.received_events if e[0] == "app.mode_changed"]
            
            logger.info(f"📊 Событий выбора INPUT устройства: {len(input_events)}")
            logger.info(f"📊 Событий выбора OUTPUT устройства: {len(output_events)}")
            logger.info(f"📊 Событий включения микрофона: {len(mic_enabled_events)}")
            logger.info(f"📊 Событий выключения микрофона: {len(mic_disabled_events)}")
            logger.info(f"📊 Событий изменения режима: {len(mode_events)}")
            
            # Проверяем что получили события устройств
            success = len(input_events) > 0 and len(output_events) > 0
            
            self.test_results['initialization_flow'] = {
                'input_events': len(input_events),
                'output_events': len(output_events),
                'mic_enabled_events': len(mic_enabled_events),
                'mic_disabled_events': len(mic_disabled_events),
                'mode_events': len(mode_events),
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка потока инициализации: {e}")
            self.test_results['initialization_flow'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_microphone_flow(self):
        """Тест потока событий микрофона"""
        logger.info("🎤 ТЕСТ: Поток событий микрофона")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Включаем микрофон
            await self.audio_integration._enable_microphone()
            await asyncio.sleep(0.5)
            
            # Выключаем микрофон
            await self.audio_integration._disable_microphone()
            await asyncio.sleep(0.5)
            
            # Анализируем полученные события
            input_events = [e for e in self.received_events if e[0] == "audio.input_device_selected"]
            mic_enabled_events = [e for e in self.received_events if e[0] == "audio.microphone_enabled"]
            mic_disabled_events = [e for e in self.received_events if e[0] == "audio.microphone_disabled"]
            
            logger.info(f"📊 Событий выбора INPUT устройства: {len(input_events)}")
            logger.info(f"📊 Событий включения микрофона: {len(mic_enabled_events)}")
            logger.info(f"📊 Событий выключения микрофона: {len(mic_disabled_events)}")
            
            # Проверяем что получили события включения и выключения
            success = len(mic_enabled_events) > 0 and len(mic_disabled_events) > 0
            
            self.test_results['microphone_flow'] = {
                'input_events': len(input_events),
                'mic_enabled_events': len(mic_enabled_events),
                'mic_disabled_events': len(mic_disabled_events),
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка потока микрофона: {e}")
            self.test_results['microphone_flow'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_recording_flow(self):
        """Тест потока событий записи"""
        logger.info("🎙️ ТЕСТ: Поток событий записи")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Симулируем начало записи
            await self.event_bus.publish("voice.recording_start", {
                "session_id": "test_session",
                "source": "test"
            })
            await asyncio.sleep(1)
            
            # Симулируем остановку записи
            await self.event_bus.publish("voice.recording_stop", {
                "session_id": "test_session",
                "source": "test"
            })
            await asyncio.sleep(1)
            
            # Анализируем полученные события
            recording_start_events = [e for e in self.received_events if e[0] == "voice.recording_start"]
            recording_stop_events = [e for e in self.received_events if e[0] == "voice.recording_stop"]
            mic_opened_events = [e for e in self.received_events if e[0] == "voice.mic_opened"]
            mic_closed_events = [e for e in self.received_events if e[0] == "voice.mic_closed"]
            
            logger.info(f"📊 Событий начала записи: {len(recording_start_events)}")
            logger.info(f"📊 Событий остановки записи: {len(recording_stop_events)}")
            logger.info(f"📊 Событий открытия микрофона: {len(mic_opened_events)}")
            logger.info(f"📊 Событий закрытия микрофона: {len(mic_closed_events)}")
            
            # Проверяем что получили события записи
            success = len(recording_start_events) > 0 and len(recording_stop_events) > 0
            
            self.test_results['recording_flow'] = {
                'recording_start_events': len(recording_start_events),
                'recording_stop_events': len(recording_stop_events),
                'mic_opened_events': len(mic_opened_events),
                'mic_closed_events': len(mic_closed_events),
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка потока записи: {e}")
            self.test_results['recording_flow'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_mode_change_flow(self):
        """Тест потока событий изменения режима"""
        logger.info("🔄 ТЕСТ: Поток событий изменения режима")
        
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
            
            # Анализируем полученные события
            mode_events = [e for e in self.received_events if e[0] == "app.mode_changed"]
            mic_enabled_events = [e for e in self.received_events if e[0] == "audio.microphone_enabled"]
            mic_disabled_events = [e for e in self.received_events if e[0] == "audio.microphone_disabled"]
            
            logger.info(f"📊 Событий изменения режима: {len(mode_events)}")
            logger.info(f"📊 Событий включения микрофона: {len(mic_enabled_events)}")
            logger.info(f"📊 Событий выключения микрофона: {len(mic_disabled_events)}")
            
            # Проверяем что получили события изменения режима
            success = len(mode_events) >= 2
            
            self.test_results['mode_change_flow'] = {
                'mode_events': len(mode_events),
                'mic_enabled_events': len(mic_enabled_events),
                'mic_disabled_events': len(mic_disabled_events),
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка потока изменения режима: {e}")
            self.test_results['mode_change_flow'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_device_request_flow(self):
        """Тест потока событий запроса устройств"""
        logger.info("🔍 ТЕСТ: Поток событий запроса устройств")
        
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
            
            # Анализируем полученные события
            input_events = [e for e in self.received_events if e[0] == "audio.input_device_selected"]
            output_events = [e for e in self.received_events if e[0] == "audio.output_device_selected"]
            
            logger.info(f"📊 Ответов на запрос INPUT устройства: {len(input_events)}")
            logger.info(f"📊 Ответов на запрос OUTPUT устройства: {len(output_events)}")
            
            # Проверяем что получили ответы на запросы
            success = len(input_events) > 0 or len(output_events) > 0
            
            self.test_results['device_request_flow'] = {
                'input_events': len(input_events),
                'output_events': len(output_events),
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка потока запроса устройств: {e}")
            self.test_results['device_request_flow'] = {'success': False, 'error': str(e)}
            return False
    
    async def run_all_tests(self):
        """Запуск всех тестов"""
        logger.info("🚀 ЗАПУСК ТЕСТОВ ПОТОКА СОБЫТИЙ")
        
        await self.setup()
        
        tests = [
            ("Поток инициализации", self.test_initialization_flow),
            ("Поток микрофона", self.test_microphone_flow),
            ("Поток записи", self.test_recording_flow),
            ("Поток изменения режима", self.test_mode_change_flow),
            ("Поток запроса устройств", self.test_device_request_flow)
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
    tester = EventFlowTester()
    success = await tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
