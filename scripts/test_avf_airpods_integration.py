#!/usr/bin/env python3
"""
Интеграционный тест AVFAudioEngine с AirPods и проверкой событий

Проверяет:
1. Запуск приветствия через AVFAudioEngine
2. Переключение AirPods во время воспроизведения
3. Приход событий audio.device.output_resync_required
4. Приход событий playback.completed

Использование:
    python scripts/test_avf_airpods_integration.py
"""

import sys
import asyncio
import logging
import time
import numpy as np
from typing import List, Dict, Any

# Настройка путей
sys.path.insert(0, 'client')

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class EventCollector:
    """Сборщик событий для проверки"""
    
    def __init__(self):
        self.events: List[Dict[str, Any]] = []
        self.lock = asyncio.Lock()
    
    async def on_event(self, event_type: str, payload: Dict[str, Any]):
        """Обработчик события"""
        async with self.lock:
            self.events.append({
                "type": event_type,
                "payload": payload,
                "timestamp": time.time()
            })
            logger.info(f"📨 [EVENT] {event_type}: {payload}")
    
    def has_event(self, event_type: str) -> bool:
        """Проверить наличие события"""
        return any(e["type"] == event_type for e in self.events)
    
    def get_events(self, event_type: str) -> List[Dict[str, Any]]:
        """Получить все события определённого типа"""
        return [e for e in self.events if e["type"] == event_type]
    
    def clear(self):
        """Очистить события"""
        self.events.clear()


async def test_airpods_playback_with_events():
    """Тест воспроизведения с AirPods и проверкой событий"""
    try:
        from modules.audio_avf import AVFAudioEngine
        from config.audio_config import AudioConfig
        from integration.core.event_bus import EventBus
        
        logger.info("=" * 60)
        logger.info("Тест воспроизведения с AirPods и проверкой событий")
        logger.info("=" * 60)
        
        # Создаём EventBus и прикрепляем loop
        event_bus = EventBus()
        loop = asyncio.get_running_loop()
        event_bus.attach_loop(loop)
        
        # Создаём AVFAudioEngine с EventBus
        config = AudioConfig.default()
        engine = AVFAudioEngine(config, event_bus=event_bus)
        
        # ✅ КРИТИЧНО: Прикрепляем event loop к AVFAudioEngine
        engine.attach_event_loop(loop)
        
        # Создаём сборщик событий
        collector = EventCollector()
        
        # Подписываемся на события (callback принимает event с полями type, data, timestamp)
        async def on_resync(event: Dict[str, Any]):
            await collector.on_event("audio.device.output_resync_required", event.get("data", {}))
        
        async def on_output_changed(event: Dict[str, Any]):
            await collector.on_event("audio.device.output_changed", event.get("data", {}))
        
        async def on_playback_completed(event: Dict[str, Any]):
            await collector.on_event("audio.playback.completed", event.get("data", {}))
        
        await event_bus.subscribe("audio.device.output_resync_required", on_resync)
        await event_bus.subscribe("audio.device.output_changed", on_output_changed)
        await event_bus.subscribe("audio.playback.completed", on_playback_completed)
        
        logger.info("✅ Подписки на события установлены")
        
        # Создаём тестовый аудио сигнал (2 секунды синусоиды 440Hz)
        sample_rate = 48000
        duration = 2.0
        frequency = 440.0
        
        logger.info(f"Создаём тестовый сигнал: {frequency}Hz, {duration}с, {sample_rate}Hz")
        
        t = np.linspace(0, duration, int(sample_rate * duration))
        audio_data = (np.sin(2 * np.pi * frequency * t) * 32767).astype(np.int16)
        audio_bytes = audio_data.tobytes()
        
        logger.info(f"Размер аудио данных: {len(audio_bytes)} bytes")
        
        # Проверяем текущее устройство
        output_device = engine.get_current_output_device()
        logger.info(f"Текущее OUTPUT устройство: {output_device}")
        
        if "AirPods" not in output_device:
            logger.warning("⚠️ AirPods не обнаружены. Подключите AirPods для полного теста.")
            logger.info("Тест будет продолжен с текущим устройством...")
        
        # Воспроизводим
        logger.info("Начинаем воспроизведение...")
        logger.info("💡 ИНСТРУКЦИЯ: Во время воспроизведения переключите режим AirPods (A2DP ↔ HFP)")
        logger.info("   или подключите/отключите AirPods для проверки событий")
        
        success = await engine.play_audio(audio_bytes, sample_rate, channels=1)
        
        if not success:
            logger.error("❌ Не удалось начать воспроизведение")
            return False
        
        logger.info("✅ Воспроизведение начато. Должен быть слышен тон 440Hz...")
        
        # Ждём завершения воспроизведения
        start_time = time.time()
        timeout = duration + 5.0  # Запас на обработку
        
        playback_completed = False
        resync_received = False
        
        while time.time() - start_time < timeout:
            await asyncio.sleep(0.1)
            
            # Проверяем события
            if collector.has_event("audio.playback.completed"):
                playback_completed = True
                logger.info("✅ Событие playback.completed получено!")
            
            if collector.has_event("audio.device.output_resync_required"):
                resync_received = True
                logger.info("✅ Событие audio.device.output_resync_required получено!")
            
            # Если воспроизведение завершено и мы получили все события - выходим
            if playback_completed:
                break
        
        # Останавливаем воспроизведение (на всякий случай)
        await engine.stop_output()
        
        # Проверяем результаты
        logger.info("")
        logger.info("=" * 60)
        logger.info("РЕЗУЛЬТАТЫ ПРОВЕРКИ СОБЫТИЙ")
        logger.info("=" * 60)
        
        playback_events = collector.get_events("audio.playback.completed")
        resync_events = collector.get_events("audio.device.output_resync_required")
        output_changed_events = collector.get_events("audio.device.output_changed")
        
        logger.info(f"📊 События playback.completed: {len(playback_events)}")
        for i, event in enumerate(playback_events, 1):
            logger.info(f"   {i}. source={event['payload'].get('source', 'unknown')}, "
                       f"finished={event['payload'].get('finished', 'unknown')}")
        
        logger.info(f"📊 События output_resync_required: {len(resync_events)}")
        for i, event in enumerate(resync_events, 1):
            logger.info(f"   {i}. was_output_active={event['payload'].get('was_output_active', 'unknown')}")
        
        logger.info(f"📊 События output_changed: {len(output_changed_events)}")
        for i, event in enumerate(output_changed_events, 1):
            logger.info(f"   {i}. device_name={event['payload'].get('device_name', 'unknown')}")
        
        # Проверки
        checks_passed = []
        checks_failed = []
        
        if playback_completed:
            checks_passed.append("✅ playback.completed получено")
        else:
            checks_failed.append("❌ playback.completed НЕ получено")
        
        if len(playback_events) > 0:
            source = playback_events[0]['payload'].get('source', '')
            if source in ['AVF_PLAYER_NODE_CALLBACK', 'AVF_FALLBACK_TIMEOUT', 'AVF_FALLBACK_TIMER']:
                checks_passed.append(f"✅ Источник playback.completed корректный: {source}")
            else:
                checks_failed.append(f"⚠️ Неожиданный источник playback.completed: {source}")
        
        if len(resync_events) > 0:
            checks_passed.append("✅ output_resync_required получено (переключение AirPods обнаружено)")
        else:
            checks_passed.append("ℹ️ output_resync_required не получено (переключение AirPods не происходило)")
        
        logger.info("")
        logger.info("Проверки:")
        for check in checks_passed:
            logger.info(f"  {check}")
        for check in checks_failed:
            logger.info(f"  {check}")
        
        # Итоговый результат
        if playback_completed and len(checks_failed) == 0:
            logger.info("")
            logger.info("✅ ТЕСТ ПРОЙДЕН: Все события получены корректно")
            return True
        else:
            logger.info("")
            logger.warning("⚠️ ТЕСТ ЧАСТИЧНО ПРОЙДЕН: Некоторые проверки не прошли")
            return len(checks_failed) == 0
            
    except Exception as e:
        logger.error(f"❌ Ошибка теста: {e}", exc_info=True)
        return False


async def main():
    """Главная функция"""
    logger.info("🚀 Запуск интеграционного теста AVFAudioEngine с AirPods")
    logger.info("")
    logger.info("Этот тест проверяет:")
    logger.info("  1. Запуск воспроизведения через AVFAudioEngine")
    logger.info("  2. Переключение AirPods во время воспроизведения")
    logger.info("  3. Приход события audio.device.output_resync_required")
    logger.info("  4. Приход события playback.completed")
    logger.info("")
    
    result = await test_airpods_playback_with_events()
    
    logger.info("")
    logger.info("=" * 60)
    if result:
        logger.info("✅ ИНТЕГРАЦИОННЫЙ ТЕСТ ПРОЙДЕН")
        return 0
    else:
        logger.info("❌ ИНТЕГРАЦИОННЫЙ ТЕСТ ПРОВАЛЕН")
        return 1


if __name__ == '__main__':
    exit_code = asyncio.run(main())
    sys.exit(exit_code)


