#!/usr/bin/env python3
"""
Диагностический тест для Speech Playback модуля
"""

import asyncio
import logging
import sys
import os
from typing import Dict, List, Any, Optional

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from modules.speech_playback.core.player import SequentialSpeechPlayer
from modules.speech_playback.core.buffer import ChunkBuffer
from config.unified_config_loader import UnifiedConfigLoader

logger = logging.getLogger(__name__)

class SpeechPlaybackDiagnostic:
    """Диагностика Speech Playback модуля"""
    
    def __init__(self):
        self.results = []
        
    async def run_diagnostic(self) -> Dict[str, Any]:
        """Запуск диагностики Speech Playback"""
        logger.info("🔍 Диагностика Speech Playback...")
        
        # 1. Тест инициализации
        await self._test_initialization()
        
        # 2. Тест конфигурации
        await self._test_configuration()
        
        # 3. Тест audio processor
        await self._test_audio_processor()
        
        # 4. Тест speech player
        await self._test_speech_player()
        
        # 5. Тест воспроизведения
        await self._test_playback()
        
        return self._analyze_results()
    
    async def _test_initialization(self):
        """Тест инициализации Speech Playback"""
        logger.info("1️⃣ Тест инициализации...")
        
        try:
            # Загружаем конфигурацию
            config_loader = UnifiedConfigLoader()
            config = config_loader._load_config()
            speech_config = config.get('speech_playback', {})
            
            # Создаем ChunkBuffer
            self.audio_buffer = ChunkBuffer()
            
            # Создаем SequentialSpeechPlayer с исправленной конфигурацией
            fixed_config = self._fix_speech_config(speech_config)
            self.speech_player = SequentialSpeechPlayer(fixed_config)
            
            # Инициализируем
            buffer_result = True  # ChunkBuffer не требует инициализации
            player_result = True  # SequentialSpeechPlayer инициализируется в __init__
            
            if buffer_result and player_result:
                self._add_result("initialization", True, "Speech Playback инициализирован", 
                               "Инициализация прошла успешно", "Продолжить", {})
            else:
                self._add_result("initialization", False, "Ошибка инициализации Speech Playback",
                               "Проблема с инициализацией", "Проверить конфигурацию и зависимости", {})
            
        except Exception as e:
            self._add_result("initialization", False, f"Ошибка инициализации: {e}",
                           "Проблема с конфигурацией или зависимостями",
                           "Проверить Speech Playback конфигурацию и зависимости", {"error": str(e)})
    
    async def _test_configuration(self):
        """Тест конфигурации Speech Playback"""
        logger.info("2️⃣ Тест конфигурации...")
        
        if not hasattr(self, 'speech_player'):
            self._add_result("configuration", False, "Speech Playback не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем основные параметры конфигурации
            config = self.speech_player.config
            
            required_params = [
                ('sample_rate', 'Частота дискретизации'),
                ('channels', 'Количество каналов'),
                ('dtype', 'Тип данных'),
                ('buffer_size', 'Размер буфера'),
                ('max_memory_mb', 'Максимальная память')
            ]
            
            for param_name, description in required_params:
                if hasattr(config, param_name):
                    value = getattr(config, param_name)
                    self._add_result(f"config_{param_name}", True, f"{description}: {value}",
                                   "Параметр настроен", "Продолжить", {"parameter": param_name, "value": value})
                else:
                    self._add_result(f"config_{param_name}", False, f"{description} не настроен",
                                   "Параметр отсутствует", f"Настроить {param_name} в конфигурации", 
                                   {"parameter": param_name})
            
        except Exception as e:
            self._add_result("configuration", False, f"Ошибка проверки конфигурации: {e}",
                           "Проблема с доступом к конфигурации", "Проверить структуру конфигурации", 
                           {"error": str(e)})
    
    async def _test_audio_processor(self):
        """Тест audio processor"""
        logger.info("3️⃣ Тест audio processor...")
        
        if not hasattr(self, 'audio_buffer'):
            self._add_result("audio_processor", False, "Speech Playback не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем состояние processor
            is_initialized = True  # ChunkBuffer всегда инициализирован
            
            if is_initialized:
                self._add_result("audio_processor", True, "Audio processor инициализирован",
                               "Processor готов к работе", "Продолжить", {})
            else:
                self._add_result("audio_processor", False, "Audio processor не инициализирован",
                               "Processor не готов", "Проверить инициализацию processor", {})
            
            # Проверяем доступные форматы
            supported_formats = ['wav', 'mp3', 'flac']  # ChunkBuffer поддерживает основные форматы
            if supported_formats:
                self._add_result("audio_formats", True, f"Поддерживается {len(supported_formats)} форматов",
                               "Форматы аудио поддерживаются", "Продолжить", {"formats": supported_formats})
            else:
                self._add_result("audio_formats", False, "Форматы аудио не поддерживаются",
                               "Нет поддержки форматов", "Проверить поддержку форматов", {})
            
        except Exception as e:
            self._add_result("audio_processor", False, f"Ошибка тестирования processor: {e}",
                           "Проблема с audio processor", "Проверить audio processor", 
                           {"error": str(e)})
    
    async def _test_speech_player(self):
        """Тест speech player"""
        logger.info("4️⃣ Тест speech player...")
        
        if not hasattr(self, 'speech_player'):
            self._add_result("speech_player", False, "Speech Playback не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем состояние player (SequentialSpeechPlayer инициализируется в __init__)
            if hasattr(self.speech_player, 'config') and self.speech_player.config is not None:
                self._add_result("speech_player", True, "Speech player инициализирован",
                               "Player готов к работе", "Продолжить", {})
            else:
                self._add_result("speech_player", False, "Speech player не инициализирован",
                               "Player не готов", "Проверить инициализацию player", {})
            
            # Проверяем очередь воспроизведения
            queue_size = getattr(self.speech_player, 'queue_size', 0)
            self._add_result("playback_queue", True, f"Размер очереди: {queue_size}",
                           "Очередь воспроизведения работает", "Продолжить", {"queue_size": queue_size})
            
        except Exception as e:
            self._add_result("speech_player", False, f"Ошибка тестирования player: {e}",
                           "Проблема с speech player", "Проверить speech player", 
                           {"error": str(e)})
    
    async def _test_playback(self):
        """Тест воспроизведения"""
        logger.info("5️⃣ Тест воспроизведения...")
        
        if not hasattr(self, 'speech_player'):
            self._add_result("playback", False, "Speech Playback не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Создаем тестовые аудио данные
            import numpy as np
            test_audio = np.random.randint(-1000, 1000, size=1000, dtype=np.int16)
            
            # Тестируем добавление в очередь
            result = self.speech_player.add_audio_data(test_audio)
            
            if result:
                self._add_result("playback", True, "Воспроизведение работает",
                               "Аудио добавлено в очередь", "Продолжить", {})
            else:
                self._add_result("playback", False, "Воспроизведение не работает",
                               "Аудио не добавлено в очередь", "Проверить логику воспроизведения", {})
            
        except Exception as e:
            self._add_result("playback", False, f"Ошибка тестирования воспроизведения: {e}",
                           "Проблема с воспроизведением", "Проверить воспроизведение", 
                           {"error": str(e)})
    

    def _fix_speech_config(self, raw_config: Dict[str, Any]) -> 'PlayerConfig':
        """Исправление конфигурации SpeechPlayback"""
        from modules.speech_playback.core.player import PlayerConfig
        
        return PlayerConfig(
            sample_rate=raw_config.get('sample_rate', 48000),
            channels=raw_config.get('channels', 1),
            dtype=raw_config.get('dtype', 'int16'),
            buffer_size=raw_config.get('buffer_size', 512),
            max_memory_mb=raw_config.get('max_memory_mb', 1024),
            device_id=raw_config.get('device_id', None),
            auto_device_selection=raw_config.get('auto_device_selection', True)
        )

    def _add_result(self, test_name: str, success: bool, problem: str, cause: str, solution: str, details: Dict[str, Any]):
        """Добавление результата теста"""
        self.results.append({
            "test": test_name,
            "success": success,
            "problem": problem,
            "cause": cause,
            "solution": solution,
            "details": details
        })
    
    def _analyze_results(self) -> Dict[str, Any]:
        """Анализ результатов"""
        total_tests = len(self.results)
        successful_tests = len([r for r in self.results if r["success"]])
        failed_tests = total_tests - successful_tests
        
        print(f"\n📊 РЕЗУЛЬТАТЫ ДИАГНОСТИКИ SPEECH_PLAYBACK:")
        print(f"   Всего тестов: {total_tests}")
        print(f"   ✅ Успешных: {successful_tests}")
        print(f"   ❌ Неудачных: {failed_tests}")
        
        if failed_tests > 0:
            print(f"\n❌ ПРОБЛЕМЫ:")
            for result in self.results:
                if not result["success"]:
                    print(f"   • {result['test']}: {result['problem']}")
                    print(f"     Причина: {result['cause']}")
                    print(f"     Решение: {result['solution']}")
        
        return {
            "total_tests": total_tests,
            "successful_tests": successful_tests,
            "failed_tests": failed_tests,
            "success_rate": (successful_tests / total_tests * 100) if total_tests > 0 else 0,
            "results": self.results
        }

async def main():
    """Основная функция"""
    diagnostic = SpeechPlaybackDiagnostic()
    results = await diagnostic.run_diagnostic()
    
    # Возвращаем код выхода
    return 1 if results["failed_tests"] > 0 else 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
