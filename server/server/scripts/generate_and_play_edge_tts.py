#!/usr/bin/env python3
"""
Генерация и воспроизведение речи через Edge TTS
"""

import asyncio
import sys
import subprocess
from pathlib import Path

try:
    import edge_tts
except ImportError:
    print("❌ edge-tts не установлен")
    sys.exit(1)


async def generate_and_play(text: str, voice: str = "en-US-AriaNeural"):
    """
    Генерирует аудио и воспроизводит его
    
    Args:
        text: Текст для генерации
        voice: Голос для использования
    """
    print(f"🎤 Генерация речи...")
    print(f"   Текст: {text}")
    print(f"   Голос: {voice}")
    
    # Создаем временный файл
    output_file = Path("/tmp/edge_tts_playback.mp3")
    
    try:
        # Генерируем аудио
        communicate = edge_tts.Communicate(text, voice)
        communicate.save_sync(str(output_file))
        
        if not output_file.exists():
            print("❌ Файл не был создан")
            return False
        
        file_size = output_file.stat().st_size
        print(f"✅ Аудио сгенерировано: {file_size} байт ({file_size / 1024:.2f} KB)")
        print(f"   Файл: {output_file}")
        
        # Воспроизводим на macOS
        print(f"\n🔊 Воспроизведение...")
        try:
            # Используем afplay для macOS
            result = subprocess.run(
                ["afplay", str(output_file)],
                check=True,
                capture_output=True,
                text=True
            )
            print("✅ Воспроизведение завершено")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Ошибка воспроизведения: {e}")
            print(f"   Попробуйте открыть файл вручную: {output_file}")
            return False
        except FileNotFoundError:
            # Если afplay не найден, пробуем open
            try:
                subprocess.run(["open", str(output_file)], check=True)
                print("✅ Файл открыт в медиаплеере")
                return True
            except Exception as e2:
                print(f"❌ Не удалось воспроизвести: {e2}")
                print(f"   Файл сохранен: {output_file}")
                return False
        
    except Exception as e:
        print(f"❌ Ошибка генерации: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Основная функция"""
    # Разные варианты текста для демонстрации
    test_texts = [
        "Hello! This is a test of Edge TTS text-to-speech system. The voice sounds natural and clear.",
        "The quick brown fox jumps over the lazy dog.",
        "Welcome to the future of speech synthesis. Edge TTS provides high-quality neural voices.",
    ]
    
    # Используем первый текст
    text = test_texts[0]
    
    print("=" * 60)
    print("EDGE TTS - ГЕНЕРАЦИЯ И ВОСПРОИЗВЕДЕНИЕ")
    print("=" * 60)
    print()
    
    # Генерируем и воспроизводим
    success = await generate_and_play(text)
    
    if success:
        print("\n🎉 Успешно!")
    else:
        print("\n⚠️  Произошла ошибка")
    
    return 0 if success else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)

