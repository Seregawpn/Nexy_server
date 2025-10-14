"""
Тест интеграции DefaultAudioIntegration
"""

import asyncio
import logging
from integration.integrations.default_audio_integration import (
    DefaultAudioIntegration, DefaultAudioIntegrationConfig
)
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_default_audio_integration():
    """Тест DefaultAudioIntegration"""
    print("🚀 ТЕСТ DEFAULT AUDIO INTEGRATION")
    print("=" * 50)
    
    try:
        # Создаем компоненты
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler()
        
        # Создаем конфигурацию
        config = DefaultAudioIntegrationConfig(
            enabled=True,
            auto_start=True,
            publish_health_events=True,
            publish_stream_events=True,
            publish_metrics_events=True
        )
        
        # Создаем интеграцию
        integration = DefaultAudioIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            config=config
        )
        
        print("✅ Интеграция создана")
        
        # Инициализация
        print("\n🔄 Инициализация...")
        init_success = await integration.initialize()
        if not init_success:
            print("❌ Ошибка инициализации")
            return False
        
        print("✅ Инициализация успешна")
        
        # Запуск
        print("\n🔄 Запуск...")
        start_success = await integration.start()
        if not start_success:
            print("❌ Ошибка запуска")
            return False
        
        print("✅ Запуск успешен")
        
        # Тестируем функциональность
        print("\n🧪 Тестирование функциональности...")
        
        # Проверяем здоровье
        is_healthy = integration.is_healthy()
        health_status = integration.get_health_status()
        print(f"🏥 Здоровье: {health_status.value} (healthy: {is_healthy})")
        
        # Получаем метрики
        metrics = integration.get_metrics()
        print(f"📊 Метрики: RMS={metrics.rms_value:.6f}, Peak={metrics.peak_value:.6f}")
        
        # Получаем аудио данные
        audio_data = integration.get_audio_data(max_samples=1000)
        print(f"🎵 Аудио данных: {len(audio_data)} сэмплов")
        
        # Ждем немного для сбора данных
        print("\n🗣️ Говорите в микрофон 3 секунды...")
        await asyncio.sleep(3)
        
        # Проверяем обновленные метрики
        updated_metrics = integration.get_metrics()
        print(f"📊 Обновленные метрики: RMS={updated_metrics.rms_value:.6f}, Peak={updated_metrics.peak_value:.6f}")
        
        # Остановка
        print("\n🛑 Остановка...")
        stop_success = await integration.stop()
        if not stop_success:
            print("❌ Ошибка остановки")
            return False
        
        print("✅ Остановка успешна")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_context_manager():
    """Тест async context manager"""
    print("\n🧪 ТЕСТ ASYNC CONTEXT MANAGER")
    print("=" * 50)
    
    try:
        # Создаем компоненты
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler()
        
        # Создаем конфигурацию
        config = DefaultAudioIntegrationConfig()
        
        # Используем context manager
        async with DefaultAudioIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            config=config
        ) as integration:
            print("✅ Интеграция запущена через context manager")
            
            # Проверяем состояние
            is_healthy = integration.is_healthy()
            print(f"🏥 Здоровье: {is_healthy}")
            
            # Ждем немного
            await asyncio.sleep(2)
        
        print("✅ Context manager завершен успешно")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка в context manager: {e}")
        return False

async def main():
    """Основная функция тестирования"""
    print("🚀 ПОЛНОЕ ТЕСТИРОВАНИЕ DEFAULT AUDIO INTEGRATION")
    print("=" * 60)
    
    results = []
    
    # Тест 1: Базовая функциональность
    print("\n" + "="*60)
    print("ТЕСТ 1: Базовая функциональность")
    result1 = await test_default_audio_integration()
    results.append(("Базовая функциональность", result1))
    
    # Тест 2: Context manager
    print("\n" + "="*60)
    print("ТЕСТ 2: Async context manager")
    result2 = await test_context_manager()
    results.append(("Context manager", result2))
    
    # Итоговый отчет
    print("\n" + "="*60)
    print("📊 ИТОГОВЫЙ ОТЧЕТ")
    print("=" * 60)
    
    success_count = 0
    for test_name, success in results:
        status = "✅ УСПЕХ" if success else "❌ НЕУДАЧА"
        print(f"{test_name}: {status}")
        if success:
            success_count += 1
    
    print(f"\n🎯 Общий результат: {success_count}/{len(results)} тестов пройдено")
    
    if success_count == len(results):
        print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ! DefaultAudioIntegration работает отлично!")
    elif success_count >= len(results) * 0.8:
        print("👍 Большинство тестов пройдено. Интеграция работает хорошо!")
    else:
        print("⚠️ Много неудач. Нужна дополнительная отладка.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⏹ Тестирование прервано пользователем")
    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()
