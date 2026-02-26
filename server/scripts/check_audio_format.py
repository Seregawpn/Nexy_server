#!/usr/bin/env python3
"""
Проверка формата аудио, который возвращается из EdgeTTSProvider
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import asyncio
from modules.audio_generation.core.audio_processor import AudioProcessor

async def check_format():
    """Проверка формата аудио"""
    print("="*60)
    print("ПРОВЕРКА ФОРМАТА АУДИО")
    print("="*60)
    
    # Используем конфигурацию по умолчанию
    processor = AudioProcessor()
    
    print("\n1. Инициализация AudioProcessor...")
    await processor.initialize()
    
    print("\n2. Информация об аудио формате:")
    audio_info = processor.get_audio_info()
    
    print(f"   Формат: {audio_info.get('format', 'N/A')}")
    print(f"   Sample rate: {audio_info.get('sample_rate', 'N/A')} Hz")
    print(f"   Channels: {audio_info.get('channels', 'N/A')} (моно/стерео)")
    print(f"   Bits per sample: {audio_info.get('bits_per_sample', 'N/A')} бит")
    print(f"   Конвертация в PCM: {audio_info.get('convert_to_pcm', 'N/A')}")
    
    print("\n3. Генерация тестового аудио...")
    test_text = "This is a format test."
    
    chunks = []
    total_bytes = 0
    async for chunk in processor.generate_speech(test_text):
        chunks.append(chunk)
        total_bytes += len(chunk)
        if len(chunks) == 1:
            # Анализируем первый чанк
            print(f"\n4. Анализ первого чанка:")
            print(f"   Размер: {len(chunk)} байт")
            print(f"   Первые 20 байт (hex): {chunk[:20].hex()}")
            
            # Проверяем, это MP3 или PCM
            if chunk[:3] == b'ID3' or chunk[:2] == b'\xff\xfb':
                print(f"   ⚠️  Похоже на MP3 формат (не конвертировано)")
            elif len(chunk) > 0:
                print(f"   ✅ Похоже на raw PCM данные")
    
    print(f"\n5. Итоговая статистика:")
    print(f"   Всего чанков: {len(chunks)}")
    print(f"   Всего байт: {total_bytes} ({total_bytes / 1024:.2f} KB)")
    
    # Проверяем конфигурацию провайдера
    if processor.provider:
        provider_status = processor.provider.get_status()
        print(f"\n6. Статус провайдера:")
        print(f"   Провайдер: {provider_status.get('provider_type', 'N/A')}")
        print(f"   Конвертация в PCM: {provider_status.get('convert_to_pcm', 'N/A')}")
        print(f"   Audio format: {provider_status.get('audio_format', 'N/A')}")
        print(f"   Sample rate: {provider_status.get('sample_rate', 'N/A')}")
        print(f"   Channels: {provider_status.get('channels', 'N/A')}")
        print(f"   Bits per sample: {provider_status.get('bits_per_sample', 'N/A')}")
    
    print("\n" + "="*60)
    print("ВЫВОД:")
    print("="*60)
    
    if audio_info.get('convert_to_pcm', False):
        print("✅ Формат: RAW PCM (конвертировано из MP3)")
        print(f"   - Sample rate: {audio_info.get('sample_rate')} Hz")
        print(f"   - Channels: {audio_info.get('channels')} (моно)")
        print(f"   - Bits per sample: {audio_info.get('bits_per_sample')} бит")
        print(f"   - Размер данных: {total_bytes} байт")
    else:
        print("⚠️  Формат: MP3 (без конвертации)")
        print(f"   - Размер данных: {total_bytes} байт")
    
    await processor.cleanup()

if __name__ == "__main__":
    asyncio.run(check_format())

