#!/usr/bin/env python3
"""
Тест полной интеграции - нажатие пробела до распознавания речи
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
from integration.integrations.input_processing_integration import InputProcessingIntegration
from integration.integrations.mode_management_integration import ModeManagementIntegration
from modules.mode_management.core.types import AppMode
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType

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

class FinalIntegrationTester:
    """Тестер полной интеграции"""
    
    def __init__(self):
        self.event_bus = EventBus()
        self.state_manager = ApplicationStateManager()
        self.error_handler = ErrorHandler(self.event_bus)
        self.audio_integration = None
        self.voice_integration = None
        self.input_integration = None
        self.mode_integration = None
        self.received_events = []
        self.test_results = {}
        
    async def setup(self):
        """Настройка тестера"""
        logger.info("🔧 Настройка полной интеграции...")
        
        # Подписываемся на все ключевые события
        await self.event_bus.subscribe("audio.input_device_selected", self._on_input_device_selected)
        await self.event_bus.subscribe("audio.microphone_enabled", self._on_microphone_enabled)
        await self.event_bus.subscribe("voice.recording_start", self._on_recording_start)
        await self.event_bus.subscribe("voice.recording_stop", self._on_recording_stop)
        await self.event_bus.subscribe("voice.mic_opened", self._on_mic_opened)
        await self.event_bus.subscribe("voice.mic_closed", self._on_mic_closed)
        await self.event_bus.subscribe("app.mode_changed", self._on_mode_changed)
        await self.event_bus.subscribe("keyboard.long_press", self._on_long_press)
        
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
        self.input_integration = InputProcessingIntegration(
            self.event_bus, 
            self.state_manager, 
            self.error_handler, 
            config
        )
        self.mode_integration = ModeManagementIntegration(
            self.event_bus, 
            self.state_manager, 
            self.error_handler
        )
        
        logger.info("✅ Полная интеграция настроена")
        
    async def _on_input_device_selected(self, event_data):
        """Обработчик события выбора INPUT устройства"""
        device_name = event_data.get('data', event_data).get('name', 'Unknown')
        portaudio_index = event_data.get('data', event_data).get('portaudio_index')
        logger.info(f"📡 [FINAL_INTEGRATION] audio.input_device_selected: {device_name} (index: {portaudio_index})")
        self.received_events.append(("audio.input_device_selected", event_data))
        
    async def _on_microphone_enabled(self, event_data):
        """Обработчик события включения микрофона"""
        logger.info(f"📡 [FINAL_INTEGRATION] audio.microphone_enabled")
        self.received_events.append(("audio.microphone_enabled", event_data))
        
    async def _on_recording_start(self, event_data):
        """Обработчик события начала записи"""
        logger.info(f"📡 [FINAL_INTEGRATION] voice.recording_start")
        self.received_events.append(("voice.recording_start", event_data))
        
    async def _on_recording_stop(self, event_data):
        """Обработчик события остановки записи"""
        logger.info(f"📡 [FINAL_INTEGRATION] voice.recording_stop")
        self.received_events.append(("voice.recording_stop", event_data))
        
    async def _on_mic_opened(self, event_data):
        """Обработчик события открытия микрофона"""
        logger.info(f"📡 [FINAL_INTEGRATION] voice.mic_opened")
        self.received_events.append(("voice.mic_opened", event_data))
        
    async def _on_mic_closed(self, event_data):
        """Обработчик события закрытия микрофона"""
        logger.info(f"📡 [FINAL_INTEGRATION] voice.mic_closed")
        self.received_events.append(("voice.mic_closed", event_data))
        
    async def _on_mode_changed(self, event_data):
        """Обработчик события изменения режима"""
        mode = event_data.get('mode', 'unknown')
        logger.info(f"📡 [FINAL_INTEGRATION] app.mode_changed: {mode}")
        self.received_events.append(("app.mode_changed", event_data))
        
    async def _on_long_press(self, event_data):
        """Обработчик события долгого нажатия"""
        logger.info(f"📡 [FINAL_INTEGRATION] keyboard.long_press")
        self.received_events.append(("keyboard.long_press", event_data))
    
    async def test_full_initialization(self):
        """Тест полной инициализации всех интеграций"""
        logger.info("🔧 ТЕСТ: Полная инициализация")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Инициализируем все интеграции
            await self.audio_integration.initialize()
            await self.audio_integration.start()
            await self.voice_integration.initialize()
            await self.input_integration.initialize()
            await self.mode_integration.initialize()
            
            # Ждем инициализации
            await asyncio.sleep(2)
            
            # Проверяем что все интеграции готовы
            audio_ready = self.audio_integration._manager is not None
            voice_ready = self.voice_integration._recognizer is not None
            input_ready = self.input_integration._processor is not None
            mode_ready = self.mode_integration._manager is not None
            
            logger.info(f"📊 AudioDeviceIntegration готов: {'✅' if audio_ready else '❌'}")
            logger.info(f"📊 VoiceRecognitionIntegration готов: {'✅' if voice_ready else '❌'}")
            logger.info(f"📊 InputProcessingIntegration готов: {'✅' if input_ready else '❌'}")
            logger.info(f"📊 ModeManagementIntegration готов: {'✅' if mode_ready else '❌'}")
            
            success = audio_ready and voice_ready and input_ready and mode_ready
            
            self.test_results['full_initialization'] = {
                'audio_ready': audio_ready,
                'voice_ready': voice_ready,
                'input_ready': input_ready,
                'mode_ready': mode_ready,
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка полной инициализации: {e}")
            self.test_results['full_initialization'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_spacebar_to_recording_flow(self):
        """Тест потока от нажатия пробела до записи"""
        logger.info("🔑 ТЕСТ: Поток от нажатия пробела до записи")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Симулируем долгое нажатие пробела
            long_press_event = KeyEvent(
                event_type=KeyEventType.LONG_PRESS,
                duration=1.5,
                timestamp=asyncio.get_event_loop().time()
            )
            
            await self.event_bus.publish("keyboard.long_press", {
                "event": long_press_event
            })
            
            # Ждем обработки событий
            await asyncio.sleep(3)
            
            # Анализируем полученные события
            long_press_events = [e for e in self.received_events if e[0] == "keyboard.long_press"]
            mode_events = [e for e in self.received_events if e[0] == "app.mode_changed"]
            mic_enabled_events = [e for e in self.received_events if e[0] == "audio.microphone_enabled"]
            recording_start_events = [e for e in self.received_events if e[0] == "voice.recording_start"]
            mic_opened_events = [e for e in self.received_events if e[0] == "voice.mic_opened"]
            
            logger.info(f"📊 Событий долгого нажатия: {len(long_press_events)}")
            logger.info(f"📊 Событий изменения режима: {len(mode_events)}")
            logger.info(f"📊 Событий включения микрофона: {len(mic_enabled_events)}")
            logger.info(f"📊 Событий начала записи: {len(recording_start_events)}")
            logger.info(f"📊 Событий открытия микрофона: {len(mic_opened_events)}")
            
            # Проверяем что получили события
            success = len(long_press_events) > 0 and len(recording_start_events) > 0
            
            self.test_results['spacebar_to_recording_flow'] = {
                'long_press_events': len(long_press_events),
                'mode_events': len(mode_events),
                'mic_enabled_events': len(mic_enabled_events),
                'recording_start_events': len(recording_start_events),
                'mic_opened_events': len(mic_opened_events),
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка потока от нажатия пробела: {e}")
            self.test_results['spacebar_to_recording_flow'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_microphone_activation_flow(self):
        """Тест потока активации микрофона"""
        logger.info("🎤 ТЕСТ: Поток активации микрофона")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Включаем микрофон
            await self.audio_integration._enable_microphone()
            await asyncio.sleep(0.5)
            
            # Проверяем что SpeechRecognizer получил устройство
            if self.voice_integration._recognizer:
                device_index = self.voice_integration._recognizer.input_device_index
                portaudio_index = self.voice_integration._recognizer._portaudio_index
                logger.info(f"📊 SpeechRecognizer input_device_index: {device_index}")
                logger.info(f"📊 SpeechRecognizer _portaudio_index: {portaudio_index}")
                
                device_received = device_index is not None and portaudio_index is not None
            else:
                device_received = False
            
            # Анализируем полученные события
            input_events = [e for e in self.received_events if e[0] == "audio.input_device_selected"]
            mic_enabled_events = [e for e in self.received_events if e[0] == "audio.microphone_enabled"]
            
            logger.info(f"📊 Событий выбора INPUT устройства: {len(input_events)}")
            logger.info(f"📊 Событий включения микрофона: {len(mic_enabled_events)}")
            
            success = device_received and len(input_events) > 0 and len(mic_enabled_events) > 0
            
            self.test_results['microphone_activation_flow'] = {
                'device_received': device_received,
                'input_events': len(input_events),
                'mic_enabled_events': len(mic_enabled_events),
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка потока активации микрофона: {e}")
            self.test_results['microphone_activation_flow'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_recording_to_stop_flow(self):
        """Тест потока от записи до остановки"""
        logger.info("🎙️ ТЕСТ: Поток от записи до остановки")
        
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
            
            success = len(recording_start_events) > 0 and len(recording_stop_events) > 0
            
            self.test_results['recording_to_stop_flow'] = {
                'recording_start_events': len(recording_start_events),
                'recording_stop_events': len(recording_stop_events),
                'mic_opened_events': len(mic_opened_events),
                'mic_closed_events': len(mic_closed_events),
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка потока от записи до остановки: {e}")
            self.test_results['recording_to_stop_flow'] = {'success': False, 'error': str(e)}
            return False
    
    async def run_all_tests(self):
        """Запуск всех тестов"""
        logger.info("🚀 ЗАПУСК ТЕСТОВ ПОЛНОЙ ИНТЕГРАЦИИ")
        
        await self.setup()
        
        tests = [
            ("Полная инициализация", self.test_full_initialization),
            ("Поток от нажатия пробела до записи", self.test_spacebar_to_recording_flow),
            ("Поток активации микрофона", self.test_microphone_activation_flow),
            ("Поток от записи до остановки", self.test_recording_to_stop_flow)
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
    tester = FinalIntegrationTester()
    success = await tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
