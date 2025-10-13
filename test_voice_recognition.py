#!/usr/bin/env python3
"""
Тест VoiceRecognitionIntegration и SpeechRecognizer - проверка активации микрофона
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
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
from modules.voice_recognition.core.speech_recognizer import SpeechRecognizer
from modules.voice_recognition.core.types import RecognitionState

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MockConfig:
    """Мок-конфигурация для тестирования"""
    def __init__(self):
        self.simulate = False  # Важно: не симулируем, используем реальный SpeechRecognizer
        self.language = "en-US"  # Добавляем язык для SpeechRecognizer
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

class VoiceRecognitionTester:
    """Тестер VoiceRecognitionIntegration"""
    
    def __init__(self):
        self.event_bus = EventBus()
        self.state_manager = ApplicationStateManager()
        self.error_handler = ErrorHandler(self.event_bus)
        self.integration = None
        self.received_events = []
        self.test_results = {}
        
    async def setup(self):
        """Настройка тестера"""
        logger.info("🔧 Настройка VoiceRecognitionIntegration...")
        
        # Подписываемся на события для мониторинга
        await self.event_bus.subscribe("voice.recording_start", self._on_recording_start)
        await self.event_bus.subscribe("voice.recording_stop", self._on_recording_stop)
        await self.event_bus.subscribe("voice.recognition_started", self._on_recognition_started)
        await self.event_bus.subscribe("voice.recognition_completed", self._on_recognition_completed)
        await self.event_bus.subscribe("voice.mic_opened", self._on_mic_opened)
        await self.event_bus.subscribe("voice.mic_closed", self._on_mic_closed)
        await self.event_bus.subscribe("audio.input_device_selected", self._on_input_device_selected)
        
        # Создаем интеграцию
        config = MockConfig()
        self.integration = VoiceRecognitionIntegration(
            self.event_bus, 
            self.state_manager, 
            self.error_handler, 
            config
        )
        
        logger.info("✅ VoiceRecognitionIntegration настроен")
        
    async def _on_recording_start(self, event_data):
        """Обработчик события начала записи"""
        logger.info(f"📡 Получено событие voice.recording_start")
        self.received_events.append(("voice.recording_start", event_data))
        
    async def _on_recording_stop(self, event_data):
        """Обработчик события остановки записи"""
        logger.info(f"📡 Получено событие voice.recording_stop")
        self.received_events.append(("voice.recording_stop", event_data))
        
    async def _on_recognition_started(self, event_data):
        """Обработчик события начала распознавания"""
        logger.info(f"📡 Получено событие voice.recognition_started")
        self.received_events.append(("voice.recognition_started", event_data))
        
    async def _on_recognition_completed(self, event_data):
        """Обработчик события завершения распознавания"""
        logger.info(f"📡 Получено событие voice.recognition_completed")
        self.received_events.append(("voice.recognition_completed", event_data))
        
    async def _on_mic_opened(self, event_data):
        """Обработчик события открытия микрофона"""
        logger.info(f"📡 Получено событие voice.mic_opened")
        self.received_events.append(("voice.mic_opened", event_data))
        
    async def _on_mic_closed(self, event_data):
        """Обработчик события закрытия микрофона"""
        logger.info(f"📡 Получено событие voice.mic_closed")
        self.received_events.append(("voice.mic_closed", event_data))
        
    async def _on_input_device_selected(self, event_data):
        """Обработчик события выбора INPUT устройства"""
        logger.info(f"📡 Получено событие audio.input_device_selected: {event_data.get('data', event_data).get('name')}")
        self.received_events.append(("audio.input_device_selected", event_data))
    
    async def test_initialization(self):
        """Тест инициализации"""
        logger.info("🔧 ТЕСТ: Инициализация")
        
        try:
            await self.integration.initialize()
            
            # Проверяем что SpeechRecognizer создан
            recognizer_created = self.integration._recognizer is not None
            logger.info(f"📊 SpeechRecognizer создан: {'✅' if recognizer_created else '❌'}")
            
            if recognizer_created:
                # Проверяем состояние SpeechRecognizer
                state = self.integration._recognizer.state
                logger.info(f"📊 Состояние SpeechRecognizer: {state}")
                
                # Проверяем что EventBus настроен
                event_bus_set = self.integration._recognizer.event_bus is not None
                logger.info(f"📊 EventBus настроен: {'✅' if event_bus_set else '❌'}")
            
            self.test_results['initialization'] = {
                'recognizer_created': recognizer_created,
                'event_bus_set': event_bus_set if recognizer_created else False,
                'success': recognizer_created
            }
            
            return recognizer_created
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации: {e}")
            self.test_results['initialization'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_device_selection(self):
        """Тест выбора устройства"""
        logger.info("🎤 ТЕСТ: Выбор устройства")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Симулируем выбор INPUT устройства
            await self.event_bus.publish("audio.input_device_selected", {
                "data": {
                    "device_id": "test_airpods",
                    "name": "Sergiy's AirPods",
                    "type": "both",
                    "channels": 2,
                    "priority": 1,
                    "status": "available",
                    "portaudio_index": 0
                }
            })
            await asyncio.sleep(0.5)
            
            # Проверяем что SpeechRecognizer получил устройство
            if self.integration._recognizer:
                device_index = self.integration._recognizer.input_device_index
                portaudio_index = self.integration._recognizer._portaudio_index
                logger.info(f"📊 input_device_index: {device_index}")
                logger.info(f"📊 _portaudio_index: {portaudio_index}")
                
                success = device_index is not None and portaudio_index is not None
            else:
                success = False
            
            self.test_results['device_selection'] = {
                'device_index': device_index if self.integration._recognizer else None,
                'portaudio_index': portaudio_index if self.integration._recognizer else None,
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка выбора устройства: {e}")
            self.test_results['device_selection'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_recording_start(self):
        """Тест начала записи"""
        logger.info("🎙️ ТЕСТ: Начало записи")
        
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
            device_events = [e for e in self.received_events if e[0] == "audio.input_device_selected"]
            
            logger.info(f"📊 Событий начала записи: {len(recording_events)}")
            logger.info(f"📊 Событий открытия микрофона: {len(mic_events)}")
            logger.info(f"📊 Событий выбора устройства: {len(device_events)}")
            
            # Проверяем состояние SpeechRecognizer
            if self.integration._recognizer:
                state = self.integration._recognizer.state
                logger.info(f"📊 Состояние после начала записи: {state}")
                state_correct = state == RecognitionState.LISTENING
            else:
                state_correct = False
            
            success = len(recording_events) > 0 and state_correct
            
            self.test_results['recording_start'] = {
                'recording_events': len(recording_events),
                'mic_events': len(mic_events),
                'device_events': len(device_events),
                'state_correct': state_correct,
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка начала записи: {e}")
            self.test_results['recording_start'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_recording_stop(self):
        """Тест остановки записи"""
        logger.info("🛑 ТЕСТ: Остановка записи")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Симулируем остановку записи
            await self.event_bus.publish("voice.recording_stop", {
                "session_id": "test_session",
                "source": "test"
            })
            await asyncio.sleep(1)
            
            # Проверяем что получили события
            recording_events = [e for e in self.received_events if e[0] == "voice.recording_stop"]
            mic_events = [e for e in self.received_events if e[0] == "voice.mic_closed"]
            
            logger.info(f"📊 Событий остановки записи: {len(recording_events)}")
            logger.info(f"📊 Событий закрытия микрофона: {len(mic_events)}")
            
            # Проверяем состояние SpeechRecognizer
            if self.integration._recognizer:
                state = self.integration._recognizer.state
                logger.info(f"📊 Состояние после остановки записи: {state}")
                state_correct = state == RecognitionState.IDLE
            else:
                state_correct = False
            
            success = len(recording_events) > 0 and state_correct
            
            self.test_results['recording_stop'] = {
                'recording_events': len(recording_events),
                'mic_events': len(mic_events),
                'state_correct': state_correct,
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка остановки записи: {e}")
            self.test_results['recording_stop'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_microphone_activation(self):
        """Тест активации микрофона"""
        logger.info("🎤 ТЕСТ: Активация микрофона")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Проверяем что SpeechRecognizer может активировать микрофон
            if self.integration._recognizer:
                # Пытаемся запустить прослушивание
                result = await self.integration._recognizer.start_listening()
                logger.info(f"📊 Результат start_listening: {result}")
                
                if result:
                    # Проверяем состояние
                    state = self.integration._recognizer.state
                    logger.info(f"📊 Состояние после start_listening: {state}")
                    
                    # Останавливаем прослушивание
                    await self.integration._recognizer.stop_listening()
                    logger.info("📊 stop_listening выполнен")
                    
                    success = state == RecognitionState.LISTENING
                else:
                    success = False
            else:
                success = False
            
            self.test_results['microphone_activation'] = {
                'start_listening_result': result if self.integration._recognizer else False,
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка активации микрофона: {e}")
            self.test_results['microphone_activation'] = {'success': False, 'error': str(e)}
            return False
    
    async def run_all_tests(self):
        """Запуск всех тестов"""
        logger.info("🚀 ЗАПУСК ТЕСТОВ VoiceRecognitionIntegration")
        
        await self.setup()
        
        tests = [
            ("Инициализация", self.test_initialization),
            ("Выбор устройства", self.test_device_selection),
            ("Начало записи", self.test_recording_start),
            ("Остановка записи", self.test_recording_stop),
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
    tester = VoiceRecognitionTester()
    success = await tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
