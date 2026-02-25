#!/usr/bin/env python3
"""
Тестирование интеграции Edge TTS в систему
Проверяет весь flow от AudioProcessor до EdgeTTSProvider
"""

import asyncio
import sys
from pathlib import Path

# Добавляем путь к серверу
sys.path.insert(0, str(Path(__file__).parent.parent))

import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


async def test_edge_tts_provider_direct():
    """Тест 1: Прямое использование EdgeTTSProvider"""
    print("\n" + "="*60)
    print("ТЕСТ 1: Прямое использование EdgeTTSProvider")
    print("="*60)
    
    try:
        from modules.audio_generation.providers.edge_tts_provider import EdgeTTSProvider
        
        config = {
            'voice_name': 'en-US-AriaNeural',
            'rate': '+0%',
            'volume': '+0%',
            'pitch': '+0Hz',
            'sample_rate': 24000,
            'channels': 1,
            'bits_per_sample': 16,
            'streaming_chunk_size': 4096,
            'convert_to_pcm': True
        }
        
        provider = EdgeTTSProvider(config)
        print(f"✅ EdgeTTSProvider создан")
        
        # Инициализация
        init_result = await provider.initialize()
        if not init_result:
            print("❌ Инициализация провайдера не удалась")
            return False
        print(f"✅ Провайдер инициализирован")
        
        # Тест генерации речи
        test_text = "Hello, this is a test of Edge TTS provider."
        print(f"\nГенерация речи для текста: '{test_text}'")
        
        chunks = []
        total_bytes = 0
        async for chunk in provider.process(test_text):
            chunks.append(chunk)
            total_bytes += len(chunk)
            print(f"  Получен чанк: {len(chunk)} байт")
        
        print(f"\n✅ Генерация завершена:")
        print(f"   Чанков: {len(chunks)}")
        print(f"   Всего байт: {total_bytes} ({total_bytes / 1024:.2f} KB)")
        
        if total_bytes > 0:
            print("✅ Тест пройден")
            return True
        else:
            print("❌ Не получено аудио данных")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_audio_processor_integration():
    """Тест 2: Интеграция через AudioProcessor"""
    print("\n" + "="*60)
    print("ТЕСТ 2: Интеграция через AudioProcessor")
    print("="*60)
    
    try:
        from modules.audio_generation.core.audio_processor import AudioProcessor
        
        # Конфигурация (использует значения по умолчанию из unified_config)
        config = {
            'edge_tts_voice_name': 'en-US-AriaNeural',
            'edge_tts_rate': '+0%',
            'edge_tts_volume': '+0%',
            'edge_tts_pitch': '+0Hz',
            'sample_rate': 24000,
            'channels': 1,
            'bits_per_sample': 16,
            'streaming_chunk_size': 4096,
            'convert_to_pcm': True
        }
        
        processor = AudioProcessor(config)
        print(f"✅ AudioProcessor создан")
        
        # Инициализация
        init_result = await processor.initialize()
        if not init_result:
            print("❌ Инициализация AudioProcessor не удалась")
            return False
        print(f"✅ AudioProcessor инициализирован")
        
        # Проверка статуса
        status = processor.get_status()
        print(f"\nСтатус процессора:")
        print(f"  Инициализирован: {status.get('is_initialized', False)}")
        print(f"  Провайдер: {status.get('provider_name', 'N/A')}")
        print(f"  Провайдер доступен: {status.get('provider_available', False)}")
        
        # Тест генерации речи
        test_text = "This is a test of AudioProcessor with Edge TTS integration."
        print(f"\nГенерация речи для текста: '{test_text}'")
        
        chunks = []
        total_bytes = 0
        async for chunk in processor.generate_speech(test_text):
            chunks.append(chunk)
            total_bytes += len(chunk)
            print(f"  Получен чанк: {len(chunk)} байт")
        
        print(f"\n✅ Генерация завершена:")
        print(f"   Чанков: {len(chunks)}")
        print(f"   Всего байт: {total_bytes} ({total_bytes / 1024:.2f} KB)")
        
        # Тест потоковой генерации
        print(f"\nТест потоковой генерации...")
        streaming_chunks = []
        streaming_total = 0
        async for chunk in processor.generate_speech_streaming(test_text):
            streaming_chunks.append(chunk)
            streaming_total += len(chunk)
        
        print(f"✅ Потоковая генерация завершена:")
        print(f"   Чанков: {len(streaming_chunks)}")
        print(f"   Всего байт: {streaming_total} ({streaming_total / 1024:.2f} KB)")
        
        # Проверка аудио информации
        audio_info = processor.get_audio_info()
        print(f"\nИнформация об аудио:")
        print(f"  Формат: {audio_info.get('format', 'N/A')}")
        print(f"  Sample rate: {audio_info.get('sample_rate', 'N/A')}")
        print(f"  Channels: {audio_info.get('channels', 'N/A')}")
        print(f"  Bits per sample: {audio_info.get('bits_per_sample', 'N/A')}")
        print(f"  Voice: {audio_info.get('voice_name', 'N/A')}")
        
        if total_bytes > 0 and streaming_total > 0:
            print("\n✅ Тест пройден")
            return True
        else:
            print("\n❌ Не получено аудио данных")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_different_voices():
    """Тест 3: Разные голоса"""
    print("\n" + "="*60)
    print("ТЕСТ 3: Тестирование разных голосов")
    print("="*60)
    
    try:
        from modules.audio_generation.core.audio_processor import AudioProcessor
        
        test_voices = [
            ('en-US-AriaNeural', 'English female'),
            ('en-US-GuyNeural', 'English male'),
            ('ru-RU-SvetlanaNeural', 'Russian female'),
        ]
        
        test_text = "Hello, this is a voice test."
        results = []
        
        for voice_name, description in test_voices:
            try:
                print(f"\nТестирование: {voice_name} ({description})")
                
                config = {
                    'edge_tts_voice_name': voice_name,
                    'edge_tts_rate': '+0%',
                    'edge_tts_volume': '+0%',
                    'edge_tts_pitch': '+0Hz',
                    'sample_rate': 24000,
                    'channels': 1,
                    'bits_per_sample': 16,
                    'streaming_chunk_size': 4096,
                    'convert_to_pcm': True
                }
                
                processor = AudioProcessor(config)
                await processor.initialize()
                
                chunks = []
                total_bytes = 0
                async for chunk in processor.generate_speech(test_text):
                    chunks.append(chunk)
                    total_bytes += len(chunk)
                
                print(f"  ✅ Успешно: {len(chunks)} чанков, {total_bytes} байт")
                results.append((voice_name, True, total_bytes))
                
                await processor.cleanup()
                
            except Exception as e:
                print(f"  ❌ Ошибка: {e}")
                results.append((voice_name, False, 0))
        
        success_count = sum(1 for _, success, _ in results if success)
        print(f"\n✅ Успешно протестировано голосов: {success_count}/{len(test_voices)}")
        
        return success_count == len(test_voices)
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_rate_volume_pitch():
    """Тест 4: Настройки rate, volume, pitch"""
    print("\n" + "="*60)
    print("ТЕСТ 4: Тестирование настроек rate, volume, pitch")
    print("="*60)
    
    try:
        from modules.audio_generation.core.audio_processor import AudioProcessor
        
        test_settings = [
            {'rate': '+0%', 'volume': '+0%', 'pitch': '+0Hz', 'name': 'Default'},
            {'rate': '-20%', 'volume': '+0%', 'pitch': '+0Hz', 'name': 'Slow rate'},
            {'rate': '+0%', 'volume': '-20%', 'pitch': '+0Hz', 'name': 'Lower volume'},
            {'rate': '+0%', 'volume': '+0%', 'pitch': '-20Hz', 'name': 'Lower pitch'},
        ]
        
        test_text = "This is a test with different settings."
        results = []
        
        for setting in test_settings:
            try:
                print(f"\nТестирование: {setting['name']}")
                print(f"  rate={setting['rate']}, volume={setting['volume']}, pitch={setting['pitch']}")
                
                config = {
                    'edge_tts_voice_name': 'en-US-AriaNeural',
                    'edge_tts_rate': setting['rate'],
                    'edge_tts_volume': setting['volume'],
                    'edge_tts_pitch': setting['pitch'],
                    'sample_rate': 24000,
                    'channels': 1,
                    'bits_per_sample': 16,
                    'streaming_chunk_size': 4096,
                    'convert_to_pcm': True
                }
                
                processor = AudioProcessor(config)
                await processor.initialize()
                
                chunks = []
                total_bytes = 0
                async for chunk in processor.generate_speech(test_text):
                    chunks.append(chunk)
                    total_bytes += len(chunk)
                
                print(f"  ✅ Успешно: {len(chunks)} чанков, {total_bytes} байт")
                results.append((setting['name'], True, total_bytes))
                
                await processor.cleanup()
                
            except Exception as e:
                print(f"  ❌ Ошибка: {e}")
                results.append((setting['name'], False, 0))
        
        success_count = sum(1 for _, success, _ in results if success)
        print(f"\n✅ Успешно протестировано настроек: {success_count}/{len(test_settings)}")
        
        return success_count == len(test_settings)
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_mp3_to_pcm_conversion():
    """Тест 5: Конвертация MP3 в PCM"""
    print("\n" + "="*60)
    print("ТЕСТ 5: Тестирование конвертации MP3 в PCM")
    print("="*60)
    
    try:
        from modules.audio_generation.providers.edge_tts_provider import EdgeTTSProvider
        
        # Тест с конвертацией
        print("\nТест 1: С конвертацией MP3 → PCM")
        config_with_convert = {
            'voice_name': 'en-US-AriaNeural',
            'rate': '+0%',
            'volume': '+0%',
            'pitch': '+0Hz',
            'sample_rate': 24000,
            'channels': 1,
            'bits_per_sample': 16,
            'streaming_chunk_size': 4096,
            'convert_to_pcm': True
        }
        
        provider1 = EdgeTTSProvider(config_with_convert)
        await provider1.initialize()
        
        chunks1 = []
        total1 = 0
        async for chunk in provider1.process("Test conversion to PCM."):
            chunks1.append(chunk)
            total1 += len(chunk)
        
        print(f"  ✅ С конвертацией: {len(chunks1)} чанков, {total1} байт")
        
        # Тест без конвертации
        print("\nТест 2: Без конвертации (MP3)")
        config_without_convert = {
            'voice_name': 'en-US-AriaNeural',
            'rate': '+0%',
            'volume': '+0%',
            'pitch': '+0Hz',
            'sample_rate': 24000,
            'channels': 1,
            'bits_per_sample': 16,
            'streaming_chunk_size': 4096,
            'convert_to_pcm': False
        }
        
        provider2 = EdgeTTSProvider(config_without_convert)
        await provider2.initialize()
        
        chunks2 = []
        total2 = 0
        async for chunk in provider2.process("Test without conversion."):
            chunks2.append(chunk)
            total2 += len(chunk)
        
        print(f"  ✅ Без конвертации: {len(chunks2)} чанков, {total2} байт")
        
        if total1 > 0 and total2 > 0:
            print(f"\n✅ Оба режима работают")
            print(f"   PCM размер: {total1} байт")
            print(f"   MP3 размер: {total2} байт")
            return True
        else:
            print(f"\n❌ Один из режимов не работает")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_provider_status_and_metrics():
    """Тест 6: Статус и метрики провайдера"""
    print("\n" + "="*60)
    print("ТЕСТ 6: Статус и метрики провайдера")
    print("="*60)
    
    try:
        from modules.audio_generation.providers.edge_tts_provider import EdgeTTSProvider
        
        config = {
            'voice_name': 'en-US-AriaNeural',
            'rate': '+0%',
            'volume': '+0%',
            'pitch': '+0Hz',
            'sample_rate': 24000,
            'channels': 1,
            'bits_per_sample': 16,
            'streaming_chunk_size': 4096,
            'convert_to_pcm': True
        }
        
        provider = EdgeTTSProvider(config)
        
        # Статус до инициализации
        status_before = provider.get_status()
        print(f"\nСтатус до инициализации:")
        print(f"  Инициализирован: {status_before['is_initialized']}")
        print(f"  Доступен: {status_before['is_available']}")
        
        # Инициализация
        await provider.initialize()
        
        # Статус после инициализации
        status_after = provider.get_status()
        print(f"\nСтатус после инициализации:")
        print(f"  Инициализирован: {status_after['is_initialized']}")
        print(f"  Доступен: {status_after['is_available']}")
        print(f"  Провайдер: {status_after['provider_type']}")
        print(f"  Голос: {status_after['voice_name']}")
        print(f"  Sample rate: {status_after['sample_rate']}")
        print(f"  Конвертация в PCM: {status_after['convert_to_pcm']}")
        
        # Генерация для увеличения метрик
        async for _ in provider.process("Test metrics."):
            pass
        
        # Метрики
        metrics = provider.get_metrics()
        print(f"\nМетрики:")
        print(f"  Всего запросов: {metrics['total_requests']}")
        print(f"  Успешных: {metrics['successful_requests']}")
        print(f"  Проваленных: {metrics['failed_requests']}")
        print(f"  Процент успеха: {metrics['success_rate']*100:.1f}%")
        
        # Аудио информация
        audio_info = provider.get_audio_info()
        print(f"\nАудио информация:")
        for key, value in audio_info.items():
            print(f"  {key}: {value}")
        
        # Информация о стоимости (должна быть 0 для Edge TTS)
        pricing = provider.get_pricing_info()
        print(f"\nИнформация о стоимости:")
        print(f"  Стоимость: {pricing['cost']}")
        print(f"  Цена за миллион символов: ${pricing['price_per_million_characters_usd']}")
        
        cost_calc = provider.calculate_cost(10000)
        print(f"\nРасчет стоимости для 10000 символов:")
        print(f"  Стоимость: ${cost_calc['cost_usd']}")
        print(f"  Сообщение: {cost_calc['message']}")
        
        print("\n✅ Тест пройден")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Основная функция тестирования"""
    print("="*60)
    print("ТЕСТИРОВАНИЕ ИНТЕГРАЦИИ EDGE TTS")
    print("="*60)
    print("\nПроверка всего flow от EdgeTTSProvider до AudioProcessor")
    
    results = {
        "edge_tts_provider_direct": False,
        "audio_processor_integration": False,
        "different_voices": False,
        "rate_volume_pitch": False,
        "mp3_to_pcm_conversion": False,
        "provider_status_and_metrics": False,
    }
    
    # Запускаем тесты
    results["edge_tts_provider_direct"] = await test_edge_tts_provider_direct()
    results["audio_processor_integration"] = await test_audio_processor_integration()
    results["different_voices"] = await test_different_voices()
    results["rate_volume_pitch"] = await test_rate_volume_pitch()
    results["mp3_to_pcm_conversion"] = await test_mp3_to_pcm_conversion()
    results["provider_status_and_metrics"] = await test_provider_status_and_metrics()
    
    # Итоговый отчет
    print("\n" + "="*60)
    print("ИТОГОВЫЙ ОТЧЕТ")
    print("="*60)
    
    for test_name, success in results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    total_tests = len(results)
    passed_tests = sum(1 for s in results.values() if s)
    
    print(f"\nВсего тестов: {total_tests}")
    print(f"Пройдено: {passed_tests}")
    print(f"Провалено: {total_tests - passed_tests}")
    
    if passed_tests == total_tests:
        print("\n🎉 Все тесты пройдены! Edge TTS интеграция работает корректно.")
        return 0
    else:
        print("\n⚠️  Некоторые тесты провалены. Проверьте ошибки выше.")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)

