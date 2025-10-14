"""
Тест нового модуля DefaultAudioManager
"""

import asyncio
import time
from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig

async def test_basic_functionality():
    """Базовый тест функциональности"""
    print("🚀 ТЕСТ DEFAULT AUDIO MANAGER")
    print("=" * 50)
    
    # Создаем конфигурацию
    config = DefaultAudioConfig(
        input_sample_rate=16000,
        output_sample_rate=48000,
        health_check_interval=1.0,
        health_check_duration=0.3,
        enable_debug_logging=True,
        log_health_checks=True,
        log_stream_events=True
    )
    
    # Callback функции
    def on_state_change(state):
        print(f"🔄 [STATE] {state.value}")
    
    def on_health_change(status):
        print(f"🏥 [HEALTH] {status.value}")
    
    def on_metrics(metrics):
        print(f"📊 [METRICS] RMS: {metrics.rms_value:.6f}, Peak: {metrics.peak_value:.6f}")
    
    def on_error(error):
        print(f"❌ [ERROR] {error.error_type}: {error.error_message}")
    
    # Устанавливаем callbacks
    config.on_stream_state_change = on_state_change
    config.on_health_status_change = on_health_change
    config.on_metrics_update = on_metrics
    config.on_error = on_error
    
    # Создаем менеджер
    manager = DefaultAudioManager(config)
    
    try:
        print("\n🔄 Запуск менеджера...")
        success = await manager.start()
        
        if not success:
            print("❌ Не удалось запустить менеджер")
            return False
        
        print("✅ Менеджер запущен успешно")
        
        # Ждем несколько секунд для сбора данных
        print("\n🗣️ Говорите в микрофон 5 секунд...")
        for i in range(5):
            await asyncio.sleep(1)
            
            # Получаем аудио данные
            audio_data = manager.get_audio_data()
            if len(audio_data) > 0:
                print(f"   {i+1}s: Получено {len(audio_data)} сэмплов")
            
            # Проверяем здоровье
            is_healthy = manager.is_healthy()
            health_status = manager.get_health_status()
            print(f"   {i+1}s: Здоровье: {health_status.value} (healthy: {is_healthy})")
        
        # Получаем финальные метрики
        metrics = manager.get_metrics()
        print(f"\n📊 Финальные метрики:")
        print(f"   RMS: {metrics.rms_value:.6f}")
        print(f"   Peak: {metrics.peak_value:.6f}")
        print(f"   Samples: {metrics.sample_count}")
        print(f"   Errors: {metrics.error_count}")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False
        
    finally:
        print("\n🛑 Остановка менеджера...")
        await manager.stop()
        print("✅ Менеджер остановлен")

async def test_context_manager():
    """Тест async context manager"""
    print("\n🧪 ТЕСТ ASYNC CONTEXT MANAGER")
    print("=" * 50)
    
    config = DefaultAudioConfig(
        health_check_interval=0.5,
        health_check_duration=0.2
    )
    
    try:
        async with DefaultAudioManager(config) as manager:
            print("✅ Менеджер запущен через context manager")
            
            # Проверяем состояние
            state = manager.get_current_state()
            print(f"📊 Состояние: {state.value}")
            
            # Ждем немного
            await asyncio.sleep(2)
            
            # Проверяем здоровье
            is_healthy = manager.is_healthy()
            print(f"🏥 Здоровье: {is_healthy}")
            
        print("✅ Context manager завершен успешно")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка в context manager: {e}")
        return False

async def test_error_handling():
    """Тест обработки ошибок"""
    print("\n🧪 ТЕСТ ОБРАБОТКИ ОШИБОК")
    print("=" * 50)
    
    config = DefaultAudioConfig(
        auto_reopen_on_error=True,
        max_retry_attempts=2,
        retry_delay=0.5,
        error_cooldown=1.0
    )
    
    error_count = 0
    
    def on_error(error):
        nonlocal error_count
        error_count += 1
        print(f"❌ [ERROR] {error.error_type}: {error.error_message}")
    
    config.on_error = on_error
    
    manager = DefaultAudioManager(config)
    
    try:
        await manager.start()
        print("✅ Менеджер запущен")
        
        # Ждем и наблюдаем за ошибками
        await asyncio.sleep(3)
        
        print(f"📊 Количество ошибок: {error_count}")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False
        
    finally:
        await manager.stop()

async def main():
    """Основная функция тестирования"""
    print("🚀 ПОЛНОЕ ТЕСТИРОВАНИЕ DEFAULT AUDIO MANAGER")
    print("=" * 60)
    
    results = []
    
    # Тест 1: Базовая функциональность
    print("\n" + "="*60)
    print("ТЕСТ 1: Базовая функциональность")
    result1 = await test_basic_functionality()
    results.append(("Базовая функциональность", result1))
    
    # Тест 2: Context manager
    print("\n" + "="*60)
    print("ТЕСТ 2: Async context manager")
    result2 = await test_context_manager()
    results.append(("Context manager", result2))
    
    # Тест 3: Обработка ошибок
    print("\n" + "="*60)
    print("ТЕСТ 3: Обработка ошибок")
    result3 = await test_error_handling()
    results.append(("Обработка ошибок", result3))
    
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
        print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ! DefaultAudioManager работает отлично!")
    elif success_count >= len(results) * 0.8:
        print("👍 Большинство тестов пройдено. Модуль работает хорошо!")
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
