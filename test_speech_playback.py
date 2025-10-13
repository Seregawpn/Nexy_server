#!/usr/bin/env python3
"""
Тест SpeechPlaybackIntegration и SequentialSpeechPlayer - проверка воспроизведения
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
from integration.integrations.speech_playback_integration import SpeechPlaybackIntegration
from modules.speech_playback.core.player import SequentialSpeechPlayer

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

class SpeechPlaybackTester:
    """Тестер SpeechPlaybackIntegration"""
    
    def __init__(self):
        self.event_bus = EventBus()
        self.state_manager = ApplicationStateManager()
        self.error_handler = ErrorHandler(self.event_bus)
        self.integration = None
        self.received_events = []
        self.test_results = {}
        
    async def setup(self):
        """Настройка тестера"""
        logger.info("🔧 Настройка SpeechPlaybackIntegration...")
        
        # Подписываемся на события для мониторинга
        await self.event_bus.subscribe("audio.output_device_selected", self._on_output_device_selected)
        await self.event_bus.subscribe("speech.playback_started", self._on_playback_started)
        await self.event_bus.subscribe("speech.playback_completed", self._on_playback_completed)
        await self.event_bus.subscribe("speech.playback_error", self._on_playback_error)
        
        # Создаем интеграцию
        self.integration = SpeechPlaybackIntegration(
            self.event_bus, 
            self.state_manager, 
            self.error_handler
        )
        
        logger.info("✅ SpeechPlaybackIntegration настроен")
        
    async def _on_output_device_selected(self, event_data):
        """Обработчик события выбора OUTPUT устройства"""
        device_name = event_data.get('data', event_data).get('name', 'Unknown')
        portaudio_index = event_data.get('data', event_data).get('portaudio_index')
        logger.info(f"📡 Получено событие audio.output_device_selected: {device_name} (index: {portaudio_index})")
        self.received_events.append(("audio.output_device_selected", event_data))
        
    async def _on_playback_started(self, event_data):
        """Обработчик события начала воспроизведения"""
        logger.info(f"📡 Получено событие speech.playback_started")
        self.received_events.append(("speech.playback_started", event_data))
        
    async def _on_playback_completed(self, event_data):
        """Обработчик события завершения воспроизведения"""
        logger.info(f"📡 Получено событие speech.playback_completed")
        self.received_events.append(("speech.playback_completed", event_data))
        
    async def _on_playback_error(self, event_data):
        """Обработчик события ошибки воспроизведения"""
        logger.info(f"📡 Получено событие speech.playback_error")
        self.received_events.append(("speech.playback_error", event_data))
    
    async def test_initialization(self):
        """Тест инициализации"""
        logger.info("🔧 ТЕСТ: Инициализация")
        
        try:
            await self.integration.initialize()
            
            # Проверяем что SequentialSpeechPlayer создан
            player_created = self.integration._player is not None
            logger.info(f"📊 SequentialSpeechPlayer создан: {'✅' if player_created else '❌'}")
            
            if player_created:
                # Проверяем что EventBus настроен
                event_bus_set = self.integration._player.event_bus is not None
                logger.info(f"📊 EventBus настроен: {'✅' if event_bus_set else '❌'}")
                
                # Проверяем состояние плеера
                is_initialized = self.integration._player.is_initialized
                logger.info(f"📊 Плеер инициализирован: {'✅' if is_initialized else '❌'}")
            else:
                event_bus_set = False
                is_initialized = False
            
            self.test_results['initialization'] = {
                'player_created': player_created,
                'event_bus_set': event_bus_set,
                'is_initialized': is_initialized,
                'success': player_created and event_bus_set and is_initialized
            }
            
            return player_created and event_bus_set and is_initialized
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации: {e}")
            self.test_results['initialization'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_device_selection(self):
        """Тест выбора устройства"""
        logger.info("🔊 ТЕСТ: Выбор устройства")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Симулируем выбор OUTPUT устройства
            await self.event_bus.publish("audio.output_device_selected", {
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
            
            # Проверяем что SequentialSpeechPlayer получил устройство
            if self.integration._player:
                device_index = self.integration._player.output_device_index
                portaudio_index = self.integration._player._portaudio_index
                logger.info(f"📊 output_device_index: {device_index}")
                logger.info(f"📊 _portaudio_index: {portaudio_index}")
                
                success = device_index is not None and portaudio_index is not None
            else:
                success = False
            
            self.test_results['device_selection'] = {
                'device_index': device_index if self.integration._player else None,
                'portaudio_index': portaudio_index if self.integration._player else None,
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка выбора устройства: {e}")
            self.test_results['device_selection'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_playback_flow(self):
        """Тест потока воспроизведения"""
        logger.info("🎵 ТЕСТ: Поток воспроизведения")
        
        try:
            # Очищаем предыдущие события
            self.received_events.clear()
            
            # Симулируем запрос на воспроизведение
            await self.event_bus.publish("speech.playback_request", {
                "session_id": "test_session",
                "source": "test",
                "text": "Hello, this is a test message.",
                "voice": "default"
            })
            await asyncio.sleep(1)
            
            # Проверяем что получили события
            playback_events = [e for e in self.received_events if e[0] == "speech.playback_started"]
            completed_events = [e for e in self.received_events if e[0] == "speech.playback_completed"]
            error_events = [e for e in self.received_events if e[0] == "speech.playback_error"]
            
            logger.info(f"📊 Событий начала воспроизведения: {len(playback_events)}")
            logger.info(f"📊 Событий завершения воспроизведения: {len(completed_events)}")
            logger.info(f"📊 Событий ошибок воспроизведения: {len(error_events)}")
            
            # Проверяем состояние плеера
            if self.integration._player:
                is_playing = self.integration._player.is_playing
                logger.info(f"📊 Плеер воспроизводит: {'✅' if is_playing else '❌'}")
            else:
                is_playing = False
            
            success = len(playback_events) > 0 or len(completed_events) > 0
            
            self.test_results['playback_flow'] = {
                'playback_events': len(playback_events),
                'completed_events': len(completed_events),
                'error_events': len(error_events),
                'is_playing': is_playing,
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка потока воспроизведения: {e}")
            self.test_results['playback_flow'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_audio_stream(self):
        """Тест аудио потока"""
        logger.info("🎧 ТЕСТ: Аудио поток")
        
        try:
            # Проверяем что SequentialSpeechPlayer может создать аудио поток
            if self.integration._player:
                # Пытаемся инициализировать аудио поток
                stream_initialized = await self.integration._player._initialize_audio_stream()
                logger.info(f"📊 Аудио поток инициализирован: {'✅' if stream_initialized else '❌'}")
                
                if stream_initialized:
                    # Проверяем что поток создан
                    stream_exists = self.integration._player._audio_stream is not None
                    logger.info(f"📊 Аудио поток существует: {'✅' if stream_exists else '❌'}")
                    
                    # Останавливаем поток
                    await self.integration._player._cleanup_audio_stream()
                    logger.info("📊 Аудио поток остановлен")
                    
                    success = stream_exists
                else:
                    success = False
            else:
                success = False
            
            self.test_results['audio_stream'] = {
                'stream_initialized': stream_initialized if self.integration._player else False,
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка аудио потока: {e}")
            self.test_results['audio_stream'] = {'success': False, 'error': str(e)}
            return False
    
    async def run_all_tests(self):
        """Запуск всех тестов"""
        logger.info("🚀 ЗАПУСК ТЕСТОВ SpeechPlaybackIntegration")
        
        await self.setup()
        
        tests = [
            ("Инициализация", self.test_initialization),
            ("Выбор устройства", self.test_device_selection),
            ("Поток воспроизведения", self.test_playback_flow),
            ("Аудио поток", self.test_audio_stream)
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
    tester = SpeechPlaybackTester()
    success = await tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
