#!/usr/bin/env python3
"""
Тестовый скрипт для проверки edge-tts перед интеграцией
Проверяет базовую функциональность без внесения изменений в проект
"""

import asyncio
import sys
from pathlib import Path
from typing import List, Dict, Any

# Добавляем путь к серверу для импорта модулей
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    import edge_tts
    print("✅ edge-tts импортирован успешно")
except ImportError as e:
    print(f"❌ Ошибка импорта edge-tts: {e}")
    sys.exit(1)


async def test_list_voices():
    """Тест: получение списка доступных голосов"""
    print("\n" + "="*60)
    print("ТЕСТ 1: Получение списка голосов")
    print("="*60)
    
    try:
        voices = await edge_tts.list_voices()
        print(f"✅ Получено голосов: {len(voices)}")
        
        # Показываем несколько примеров
        print("\nПримеры голосов:")
        for i, voice in enumerate(voices[:5]):
            print(f"  {i+1}. {voice['ShortName']} ({voice['Locale']}) - {voice['Gender']}")
        
        # Группируем по языкам
        languages = {}
        for voice in voices:
            lang_code = voice['Locale'].split('-')[0]
            if lang_code not in languages:
                languages[lang_code] = []
            languages[lang_code].append(voice['ShortName'])
        
        print(f"\n✅ Найдено языков: {len(languages)}")
        print(f"Примеры языков: {', '.join(list(languages.keys())[:10])}")
        
        return voices, languages
        
    except Exception as e:
        print(f"❌ Ошибка получения голосов: {e}")
        return None, None


async def test_basic_synthesis(text: str = "Hello, this is a test of Edge TTS."):
    """Тест: базовая генерация речи"""
    print("\n" + "="*60)
    print("ТЕСТ 2: Базовая генерация речи")
    print("="*60)
    
    try:
        voice = "en-US-AriaNeural"
        print(f"Используемый голос: {voice}")
        print(f"Текст: {text}")
        
        communicate = edge_tts.Communicate(text, voice)
        
        # Пробуем save_sync (синхронный метод)
        test_file = Path(__file__).parent / "test_edge_tts_output.mp3"
        try:
            communicate.save_sync(str(test_file))
            if test_file.exists():
                file_size = test_file.stat().st_size
                print(f"✅ Аудио файл создан (save_sync): {test_file}")
                print(f"   Размер: {file_size} байт ({file_size / 1024:.2f} KB)")
                return True
        except Exception as sync_error:
            print(f"⚠️  save_sync не сработал: {sync_error}")
            # Пробуем асинхронный save
            try:
                await communicate.save(str(test_file))
                if test_file.exists():
                    file_size = test_file.stat().st_size
                    print(f"✅ Аудио файл создан (save): {test_file}")
                    print(f"   Размер: {file_size} байт ({file_size / 1024:.2f} KB)")
                    return True
            except Exception as async_error:
                print(f"⚠️  save также не сработал: {async_error}")
        
        # Пробуем через stream и ручное сохранение
        try:
            print("Пробуем через stream...")
            chunks = []
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    chunks.append(chunk["data"])
            
            if chunks:
                with open(test_file, 'wb') as f:
                    for chunk in chunks:
                        f.write(chunk)
                if test_file.exists():
                    file_size = test_file.stat().st_size
                    print(f"✅ Аудио файл создан (stream): {test_file}")
                    print(f"   Размер: {file_size} байт ({file_size / 1024:.2f} KB)")
                    return True
        except Exception as stream_error:
            print(f"⚠️  stream не сработал: {stream_error}")
        
        print("❌ Все методы не сработали")
        return False
            
    except Exception as e:
        print(f"❌ Ошибка генерации речи: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_streaming_synthesis(text: str = "This is a streaming test. The audio should be generated in chunks."):
    """Тест: потоковая генерация речи"""
    print("\n" + "="*60)
    print("ТЕСТ 3: Потоковая генерация речи")
    print("="*60)
    
    try:
        voice = "en-US-AriaNeural"
        print(f"Используемый голос: {voice}")
        print(f"Текст: {text}")
        
        communicate = edge_tts.Communicate(text, voice)
        
        chunks = []
        total_bytes = 0
        
        print("\nПолучение аудио чанков:")
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                chunk_data = chunk["data"]
                chunks.append(chunk_data)
                total_bytes += len(chunk_data)
                print(f"  Чанк #{len(chunks)}: {len(chunk_data)} байт")
            elif chunk["type"] == "WordBoundary":
                print(f"  WordBoundary: {chunk.get('offset', 'N/A')}")
        
        print(f"\n✅ Получено чанков: {len(chunks)}")
        print(f"   Всего байт: {total_bytes} ({total_bytes / 1024:.2f} KB)")
        
        # Сохраняем объединенные чанки
        if chunks:
            test_file = Path(__file__).parent / "test_edge_tts_streaming.mp3"
            with open(test_file, 'wb') as f:
                for chunk in chunks:
                    f.write(chunk)
            
            if test_file.exists():
                file_size = test_file.stat().st_size
                print(f"✅ Файл из чанков создан: {test_file}")
                print(f"   Размер: {file_size} байт")
                return True
        
        return False
        
    except Exception as e:
        print(f"❌ Ошибка потоковой генерации: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_different_voices():
    """Тест: генерация с разными голосами"""
    print("\n" + "="*60)
    print("ТЕСТ 4: Генерация с разными голосами")
    print("="*60)
    
    test_voices = [
        "en-US-AriaNeural",  # Женский, английский
        "en-US-GuyNeural",   # Мужской, английский
        "ru-RU-SvetlanaNeural",  # Женский, русский
    ]
    
    text = "Hello, this is a test."
    
    results = []
    for voice in test_voices:
        try:
            print(f"\nТестирование голоса: {voice}")
            communicate = edge_tts.Communicate(text, voice)
            
            chunks = []
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    chunks.append(chunk["data"])
            
            if chunks:
                total_bytes = sum(len(c) for c in chunks)
                print(f"  ✅ Успешно: {len(chunks)} чанков, {total_bytes} байт")
                results.append((voice, True, total_bytes))
            else:
                print(f"  ❌ Нет данных")
                results.append((voice, False, 0))
                
        except Exception as e:
            print(f"  ❌ Ошибка: {e}")
            results.append((voice, False, 0))
    
    success_count = sum(1 for _, success, _ in results if success)
    print(f"\n✅ Успешно протестировано голосов: {success_count}/{len(test_voices)}")
    
    return results


async def test_audio_format():
    """Тест: проверка формата аудио данных"""
    print("\n" + "="*60)
    print("ТЕСТ 5: Анализ формата аудио")
    print("="*60)
    
    try:
        voice = "en-US-AriaNeural"
        text = "Test audio format."
        
        communicate = edge_tts.Communicate(text, voice)
        
        # Получаем первый чанк
        first_chunk = None
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                first_chunk = chunk["data"]
                break
        
        if first_chunk:
            print(f"Размер первого чанка: {len(first_chunk)} байт")
            
            # Проверяем заголовок (MP3 обычно начинается с ID3 или FF)
            header = first_chunk[:20]
            print(f"Первые 20 байт (hex): {header.hex()}")
            
            # Проверяем, является ли это MP3
            if first_chunk.startswith(b'ID3') or first_chunk.startswith(b'\xff\xfb'):
                print("✅ Похоже на MP3 формат")
            elif first_chunk.startswith(b'RIFF'):
                print("✅ Похоже на WAV формат (RIFF)")
            else:
                print("⚠️  Неизвестный формат заголовка")
            
            return True
        else:
            print("❌ Не удалось получить аудио данные")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка анализа формата: {e}")
        return False


async def test_rate_volume_pitch():
    """Тест: настройки rate, volume, pitch"""
    print("\n" + "="*60)
    print("ТЕСТ 6: Настройки rate, volume, pitch")
    print("="*60)
    
    try:
        voice = "en-US-AriaNeural"
        text = "This is a test with custom settings."
        
        # Тест с разными настройками
        settings = [
            {"rate": "+0%", "volume": "+0%", "pitch": "+0Hz"},
            {"rate": "-20%", "volume": "+0%", "pitch": "+0Hz"},
            {"rate": "+0%", "volume": "-20%", "pitch": "+0Hz"},
            {"rate": "+0%", "volume": "+0%", "pitch": "-20Hz"},
        ]
        
        results = []
        for i, setting in enumerate(settings):
            try:
                print(f"\nТест {i+1}: rate={setting['rate']}, volume={setting['volume']}, pitch={setting['pitch']}")
                communicate = edge_tts.Communicate(
                    text, 
                    voice,
                    rate=setting['rate'],
                    volume=setting['volume'],
                    pitch=setting['pitch']
                )
                
                chunks = []
                async for chunk in communicate.stream():
                    if chunk["type"] == "audio":
                        chunks.append(chunk["data"])
                
                if chunks:
                    total_bytes = sum(len(c) for c in chunks)
                    print(f"  ✅ Успешно: {len(chunks)} чанков, {total_bytes} байт")
                    results.append(True)
                else:
                    print(f"  ❌ Нет данных")
                    results.append(False)
                    
            except Exception as e:
                print(f"  ❌ Ошибка: {e}")
                results.append(False)
        
        success_count = sum(1 for r in results if r)
        print(f"\n✅ Успешно протестировано настроек: {success_count}/{len(settings)}")
        
        return success_count == len(settings)
        
    except Exception as e:
        print(f"❌ Ошибка тестирования настроек: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Основная функция тестирования"""
    print("="*60)
    print("ТЕСТИРОВАНИЕ EDGE-TTS")
    print("="*60)
    print("\nПроверка базовой функциональности edge-tts перед интеграцией")
    
    results = {
        "list_voices": False,
        "basic_synthesis": False,
        "streaming_synthesis": False,
        "different_voices": False,
        "audio_format": False,
        "rate_volume_pitch": False,
    }
    
    # Тест 1: Список голосов
    voices, languages = await test_list_voices()
    results["list_voices"] = voices is not None
    
    # Тест 2: Базовая генерация
    results["basic_synthesis"] = await test_basic_synthesis()
    
    # Тест 3: Потоковая генерация
    results["streaming_synthesis"] = await test_streaming_synthesis()
    
    # Тест 4: Разные голоса
    voice_results = await test_different_voices()
    results["different_voices"] = any(success for _, success, _ in voice_results)
    
    # Тест 5: Формат аудио
    results["audio_format"] = await test_audio_format()
    
    # Тест 6: Настройки
    results["rate_volume_pitch"] = await test_rate_volume_pitch()
    
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
        print("\n🎉 Все тесты пройдены! edge-tts готов к интеграции.")
        return 0
    else:
        print("\n⚠️  Некоторые тесты провалены. Проверьте ошибки выше.")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)

