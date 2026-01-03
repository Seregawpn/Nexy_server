#!/usr/bin/env python3
"""
Тест конвертации MP3 → PCM через ffmpeg
Проверяет работу EdgeTTSProvider с альтернативной конвертацией
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


async def test_edge_tts_with_ffmpeg():
    """Тест EdgeTTSProvider с конвертацией через ffmpeg"""
    print("="*60)
    print("ТЕСТ: EdgeTTSProvider с конвертацией MP3 → PCM (ffmpeg)")
    print("="*60)
    
    try:
        from modules.audio_generation.core.audio_processor import AudioProcessor
        
        # Создаем AudioProcessor (он сам загрузит конфигурацию)
        print("\n1. Создание AudioProcessor...")
        audio_processor = AudioProcessor()
        await audio_processor.initialize()
        print("   ✅ AudioProcessor инициализирован")
        
        # Проверяем статус
        print("\n3. Проверка статуса провайдера...")
        status = audio_processor.get_status()
        provider_status = status.get('provider', {})
        print(f"   Провайдер: {provider_status.get('name', 'N/A')}")
        print(f"   Доступен: {provider_status.get('available', False)}")
        print(f"   Конвертация в PCM: {provider_status.get('convert_to_pcm', False)}")
        
        # Проверяем информацию об аудио
        print("\n4. Информация об аудио формате...")
        audio_info = audio_processor.get_audio_info()
        print(f"   Формат: {audio_info.get('format', 'N/A')}")
        print(f"   Sample rate: {audio_info.get('sample_rate', 'N/A')} Hz")
        print(f"   Channels: {audio_info.get('channels', 'N/A')}")
        print(f"   Bits per sample: {audio_info.get('bits_per_sample', 'N/A')}")
        print(f"   Voice: {audio_info.get('voice_name', 'N/A')}")
        
        # Тест генерации аудио
        test_text = "Hello! This is a test of Edge TTS with ffmpeg conversion."
        print(f"\n5. Генерация аудио для текста:")
        print(f"   '{test_text}'")
        
        chunks = []
        total_bytes = 0
        first_chunk = None
        
        async for chunk in audio_processor.generate_speech_streaming(test_text):
            if not first_chunk:
                first_chunk = chunk
            chunks.append(chunk)
            total_bytes += len(chunk)
            print(f"   🔊 Чанк #{len(chunks)}: {len(chunk)} байт")
        
        print(f"\n6. Результаты генерации:")
        print(f"   Всего чанков: {len(chunks)}")
        print(f"   Всего байт: {total_bytes} ({total_bytes / 1024:.2f} KB)")
        
        # Анализ первого чанка
        print(f"\n7. Анализ формата данных:")
        if first_chunk:
            print(f"   Размер первого чанка: {len(first_chunk)} байт")
            header = first_chunk[:20]
            print(f"   Первые 20 байт (hex): {header.hex()}")
            
            # Проверка на PCM (raw данные, не MP3)
            # MP3 обычно начинается с ID3 или FF FB / FF F3
            if header.startswith(b'ID3') or header.startswith(b'\xff\xfb') or header.startswith(b'\xff\xf3'):
                print("   ⚠️  Обнаружен MP3 формат (конвертация не сработала)")
                return False
            else:
                print("   ✅ Похоже на raw PCM данные (конвертация работает)")
        
        # Проверка размера данных
        expected_pcm_size = len(test_text) * 1000 * 2  # Примерная оценка
        if total_bytes < 10000:
            print(f"   ⚠️  Размер данных слишком мал ({total_bytes} байт)")
            print(f"      Возможно, это MP3, а не PCM")
            return False
        
        print(f"\n8. Итоговая проверка:")
        if total_bytes > 0 and len(chunks) > 0:
            print("   ✅ Аудио сгенерировано успешно")
            print("   ✅ Конвертация MP3 → PCM работает")
            return True
        else:
            print("   ❌ Аудио не сгенерировано")
            return False
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        if 'audio_processor' in locals():
            await audio_processor.cleanup()


async def test_direct_provider():
    """Прямой тест EdgeTTSProvider"""
    print("\n" + "="*60)
    print("ТЕСТ: Прямое использование EdgeTTSProvider")
    print("="*60)
    
    try:
        from modules.audio_generation.providers.edge_tts_provider import EdgeTTSProvider
        from modules.audio_generation.config import AudioGenerationConfig
        
        # Конфигурация
        audio_config = AudioGenerationConfig()
        edge_tts_config = audio_config.get_edge_tts_config()
        
        # Создаем провайдер
        print("\n1. Создание EdgeTTSProvider...")
        provider = EdgeTTSProvider(edge_tts_config)
        await provider.initialize()
        print("   ✅ Провайдер инициализирован")
        
        # Проверяем доступность ffmpeg
        import shutil
        ffmpeg_available = shutil.which("ffmpeg") is not None
        print(f"\n2. Проверка ffmpeg:")
        print(f"   Доступен: {ffmpeg_available}")
        
        # Тест генерации
        test_text = "Test audio generation with ffmpeg."
        print(f"\n3. Генерация аудио: '{test_text}'")
        
        chunks = []
        total_bytes = 0
        
        async for chunk in provider.process(test_text):
            chunks.append(chunk)
            total_bytes += len(chunk)
        
        print(f"\n4. Результаты:")
        print(f"   Чанков: {len(chunks)}")
        print(f"   Байт: {total_bytes} ({total_bytes / 1024:.2f} KB)")
        
        if total_bytes > 0:
            print("   ✅ Генерация работает")
            return True
        else:
            print("   ❌ Генерация не работает")
            return False
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Основная функция тестирования"""
    print("="*60)
    print("ТЕСТИРОВАНИЕ КОНВЕРТАЦИИ MP3 → PCM (FFMPEG)")
    print("="*60)
    
    results = {
        "direct_provider": False,
        "audio_processor": False,
    }
    
    # Тест 1: Прямой провайдер
    results["direct_provider"] = await test_direct_provider()
    
    # Тест 2: Через AudioProcessor
    results["audio_processor"] = await test_edge_tts_with_ffmpeg()
    
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
        print("\n🎉 Все тесты пройдены! Конвертация MP3 → PCM работает через ffmpeg.")
        return 0
    else:
        print("\n⚠️  Некоторые тесты провалены. Проверьте ошибки выше.")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)

