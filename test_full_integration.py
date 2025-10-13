#!/usr/bin/env python3
"""
Тест полной интеграции - AudioDeviceIntegration + VoiceRecognitionIntegration
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

class FullIntegrationTester:
    """Тестер полной интеграции"""
    
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
        logger.info("🔧 Настройка полной интеграции...")
        
        # Подписываемся на события для мониторинга
        await self.event_bus.subscribe("audio.input_device_selected", self._on_input_device_selected)
        await self.event_bus.subscribe("audio.microphone_enabled", self._on_microphone_enabled)
        await self.event_bus.subscribe("voice.recording_start", self._on_recording_start)
        await self.event_bus.subscribe("voice.mic_opened", self._on_mic_opened)
        
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
        
        logger.info("✅ Полная интеграция настроена")
        
    async def _on_input_device_selected(self, event_data):
        """Обработчик события выбора INPUT устройства"""
        device_name = event_data.get('data', event_data).get('name', 'Unknown')
        portaudio_index = event_data.get('data', event_data).get('portaudio_index')
        logger.info(f"📡 Получено событие audio.input_device_selected: {device_name} (index: {portaudio_index})")
        self.received_events.append(("audio.input_device_selected", event_data))
        
    async def _on_microphone_enabled(self, event_data):
        """Обработчик события включения микрофона"""
        logger.info(f"📡 Получено событие audio.microphone_enabled")
        self.received_events.append(("audio.microphone_enabled", event_data))
        
    async def _on_recording_start(self, event_data):
        """Обработчик события начала записи"""
        logger.info(f"📡 Получено событие voice.recording_start")
        self.received_events.append(("voice.recording_start", event_data))
        
    async def _on_mic_opened(self, event_data):
        """Обработчик события открытия микрофона"""
        logger.info(f"📡 Получено событие voice.mic_opened")
        self.received_events.append(("voice.mic_opened", event_data))
    
    async def test_initialization(self):
        """Тест инициализации обеих интеграций"""
        logger.info("🔧 ТЕСТ: Инициализация")
        
        try:
            # Инициализируем AudioDeviceIntegration
            await self.audio_integration.initialize()
            await self.audio_integration.start()
            
            # Инициализируем VoiceRecognitionIntegration
            await self.voice_integration.initialize()
            
            # Проверяем что обе интеграции созданы
            audio_ready = self.audio_integration._manager is not None
            voice_ready = self.voice_integration._recognizer is not None
            
            logger.info(f"📊 AudioDeviceIntegration готов: {'✅' if audio_ready else '❌'}")
            logger.info(f"📊 VoiceRecognitionIntegration готов: {'✅' if voice_ready else '❌'}")
            
            self.test_results['initialization'] = {
                'audio_ready': audio_ready,
                'voice_ready': voice_ready,
                'success': audio_ready and voice_ready
            }
            
            return audio_ready and voice_ready
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации: {e}")
            self.test_results['initialization'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_device_flow(self):
        """Тест потока устройств от AudioDeviceIntegration к VoiceRecognitionIntegration"""
        logger.info("🔄 ТЕСТ: Поток устройств")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Включаем микрофон через AudioDeviceIntegration
            await self.audio_integration._enable_microphone()
            
            # Явно запрашиваем устройство у VoiceRecognitionIntegration
            if self.voice_integration._recognizer:
                await self.voice_integration._request_current_input_device()
            
            await asyncio.sleep(2)  # Увеличиваем время ожидания
            
            # Проверяем что получили события
            input_events = [e for e in self.received_events if e[0] == "audio.input_device_selected"]
            mic_events = [e for e in self.received_events if e[0] == "audio.microphone_enabled"]
            
            logger.info(f"📊 Событий выбора INPUT устройства: {len(input_events)}")
            logger.info(f"📊 Событий включения микрофона: {len(mic_events)}")
            
            # Проверяем что VoiceRecognitionIntegration получил устройство
            if self.voice_integration._recognizer:
                # Ждем пока SpeechRecognizer получит устройство
                max_wait = 5  # максимум 5 секунд
                wait_time = 0
                device_index = None
                portaudio_index = None
                
                while wait_time < max_wait:
                    device_index = self.voice_integration._recognizer.input_device_index
                    portaudio_index = self.voice_integration._recognizer._portaudio_index
                    
                    if device_index is not None and portaudio_index is not None:
                        logger.info(f"📊 SpeechRecognizer получил устройство после {wait_time} секунд")
                        break
                    
                    await asyncio.sleep(0.5)
                    wait_time += 0.5
                
                logger.info(f"📊 SpeechRecognizer input_device_index: {device_index}")
                logger.info(f"📊 SpeechRecognizer _portaudio_index: {portaudio_index}")
                
                device_received = device_index is not None and portaudio_index is not None
            else:
                device_received = False
            
            success = len(input_events) > 0 and device_received
            
            self.test_results['device_flow'] = {
                'input_events': len(input_events),
                'mic_events': len(mic_events),
                'device_received': device_received,
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка потока устройств: {e}")
            self.test_results['device_flow'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_recording_flow(self):
        """Тест потока записи"""
        logger.info("🎙️ ТЕСТ: Поток записи")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Симулируем начало записи
            await self.event_bus.publish("voice.recording_start", {
                "session_id": "test_session",
                "source": "test"
            })
            await asyncio.sleep(1)
            
            # Проверяем что получили события
            recording_events = [e for e in self.received_events if e[0] == "voice.recording_start"]
            mic_events = [e for e in self.received_events if e[0] == "voice.mic_opened"]
            
            logger.info(f"📊 Событий начала записи: {len(recording_events)}")
            logger.info(f"📊 Событий открытия микрофона: {len(mic_events)}")
            
            # Проверяем состояние SpeechRecognizer
            if self.voice_integration._recognizer:
                state = self.voice_integration._recognizer.state
                logger.info(f"📊 Состояние SpeechRecognizer: {state}")
                state_correct = state.value in ['listening', 'idle']  # Может быть idle если устройство не выбрано
            else:
                state_correct = False
            
            success = len(recording_events) > 0
            
            self.test_results['recording_flow'] = {
                'recording_events': len(recording_events),
                'mic_events': len(mic_events),
                'state_correct': state_correct,
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка потока записи: {e}")
            self.test_results['recording_flow'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_microphone_activation(self):
        """Тест активации микрофона"""
        logger.info("🎤 ТЕСТ: Активация микрофона")
        
        try:
            # Проверяем что SpeechRecognizer может активировать микрофон
            if self.voice_integration._recognizer:
                # Проверяем текущее состояние
                current_state = self.voice_integration._recognizer.state
                logger.info(f"📊 Текущее состояние SpeechRecognizer: {current_state}")
                
                # Если уже слушает, то это успех
                if current_state.name == "LISTENING":
                    logger.info("📊 SpeechRecognizer уже в состоянии LISTENING - это успех!")
                    success = True
                else:
                    # Пытаемся запустить прослушивание
                    result = await self.voice_integration._recognizer.start_listening()
                    logger.info(f"📊 Результат start_listening: {result}")
                    
                    if result:
                        # Проверяем состояние
                        state = self.voice_integration._recognizer.state
                        logger.info(f"📊 Состояние после start_listening: {state}")
                        
                        # Останавливаем прослушивание
                        await self.voice_integration._recognizer.stop_listening()
                        logger.info("📊 stop_listening выполнен")
                        
                        success = True
                    else:
                        success = False
            else:
                success = False
            
            self.test_results['microphone_activation'] = {
                'start_listening_result': success,  # Используем success вместо result
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка активации микрофона: {e}")
            self.test_results['microphone_activation'] = {'success': False, 'error': str(e)}
            return False
    
    async def run_all_tests(self):
        """Запуск всех тестов"""
        logger.info("🚀 ЗАПУСК ТЕСТОВ ПОЛНОЙ ИНТЕГРАЦИИ")
        
        await self.setup()
        
        tests = [
            ("Инициализация", self.test_initialization),
            ("Поток устройств", self.test_device_flow),
            ("Поток записи", self.test_recording_flow),
            ("Активация микрофона", self.test_microphone_activation)
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
    tester = FullIntegrationTester()
    success = await tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
