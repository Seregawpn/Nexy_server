#!/usr/bin/env python3
"""
Скрипт для проверки стоимости Azure TTS

Использование:
    python check_azure_tts_pricing.py
    python check_azure_tts_pricing.py --chars 10000
    python check_azure_tts_pricing.py --text "Hello, this is a test message"
"""

import sys
import os
import argparse
import json
from pathlib import Path
from typing import Dict, Any

# Добавляем путь к корню проекта
project_root = Path(__file__).parent.parent.parent
server_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(server_root))

# Прямой импорт без server. префикса
from modules.audio_generation.providers.azure_tts_provider import AzureTTSProvider


def get_character_examples() -> Dict[str, Any]:
    """
    Возвращает примеры того, сколько это 1 000 000 символов
    
    Returns:
        Словарь с примерами
    """
    examples = {
        "1_million_characters": {
            "description": "1 000 000 символов это примерно:",
            "examples": [
                "~200-250 страниц книги (формат A4, 12pt шрифт, одинарный интервал)",
                "~400-500 страниц книги (формат A4, 12pt шрифт, двойной интервал)",
                "~150-200 тысяч слов (английский текст)",
                "~100-150 тысяч слов (русский текст, так как слова длиннее)",
                "~2-3 часа чтения вслух (со скоростью ~150 слов/минуту)",
                "~50-70 средних статей (по 2000-3000 слов каждая)",
                "~10-15 глав книги среднего размера",
                "~1-2 полных романа (короткие)",
            ],
            "real_world_examples": [
                "Война и мир (Л. Толстой) - ~3.5 миллиона символов",
                "Гарри Поттер и философский камень - ~1.1 миллиона символов",
                "Властелин колец (одна книга) - ~1.2-1.5 миллиона символов",
                "Средняя новелла - ~200-500 тысяч символов",
                "Средний рассказ - ~50-100 тысяч символов",
            ],
            "comparison": {
                "tweets": "~50,000 твитов (по 20 символов каждый)",
                "sms": "~25,000 SMS (по 40 символов каждое)",
                "whatsapp_messages": "~10,000 сообщений (по 100 символов каждое)",
                "email": "~2,000 средних email (по 500 символов каждый)",
                "blog_posts": "~100-200 постов в блоге (по 5,000-10,000 символов каждый)",
            }
        }
    }
    return examples


def print_character_examples():
    """Выводит примеры того, сколько это 1 000 000 символов"""
    examples = get_character_examples()
    info = examples["1_million_characters"]
    
    print("=" * 70)
    print("Что такое 1 000 000 символов?")
    print("=" * 70)
    print(f"\n{info['description']}\n")
    
    print("📚 В пересчете на текст:")
    for example in info['examples']:
        print(f"  • {example}")
    
    print("\n📖 Примеры из литературы:")
    for example in info['real_world_examples']:
        print(f"  • {example}")
    
    print("\n💬 В пересчете на сообщения:")
    for key, value in info['comparison'].items():
        label = key.replace('_', ' ').title()
        print(f"  • {label}: {value}")
    
    print("\n" + "=" * 70)
    print("Практические примеры для Azure TTS:")
    print("=" * 70)
    print("""
  • 1 час аудио (со скоростью ~150 слов/мин) ≈ 1,000,000 символов = $15 USD
  • 30 минут аудио ≈ 500,000 символов = БЕСПЛАТНО (в пределах лимита)
  • 10 минут аудио ≈ 170,000 символов = БЕСПЛАТНО
  • 1 минута аудио ≈ 17,000 символов = БЕСПЛАТНО
  
  💡 Бесплатный лимит (500,000 символов/месяц) = ~30 минут аудио в месяц
    """)


def main():
    parser = argparse.ArgumentParser(description="Проверка стоимости Azure TTS")
    parser.add_argument(
        "--chars",
        type=int,
        help="Количество символов для расчета стоимости"
    )
    parser.add_argument(
        "--text",
        type=str,
        help="Текст для расчета стоимости (будет подсчитано количество символов)"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Вывести результат в формате JSON"
    )
    parser.add_argument(
        "--examples",
        action="store_true",
        help="Показать примеры того, сколько это 1 000 000 символов"
    )
    
    args = parser.parse_args()
    
    # Если запрошены примеры, показываем их и выходим
    if args.examples:
        print_character_examples()
        return
    
    # Создаем конфигурацию (можно использовать значения по умолчанию)
    config = {
        "speech_key": os.getenv("AZURE_SPEECH_KEY", ""),
        "speech_region": os.getenv("AZURE_SPEECH_REGION", ""),
        "voice_name": os.getenv("AZURE_VOICE_NAME", "en-US-AriaNeural"),
    }
    
    # Создаем провайдер
    provider = AzureTTSProvider(config)
    
    # Получаем информацию о ценах
    pricing_info = provider.get_pricing_info()
    
    if args.json:
        # JSON вывод
        if args.chars or args.text:
            char_count = args.chars if args.chars else len(args.text)
            cost_info = provider.calculate_cost(char_count)
            output = {
                "pricing_info": pricing_info,
                "cost_calculation": cost_info
            }
        else:
            output = {"pricing_info": pricing_info}
        
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        # Человекочитаемый вывод
        print("=" * 70)
        print("Azure TTS Pricing Information")
        print("=" * 70)
        print(f"\nГолос: {pricing_info['voice_name']}")
        print(f"Тип голоса: {pricing_info['voice_type']}")
        print(f"Цена: ${pricing_info['price_per_million_characters_usd']:.2f} USD за 1 миллион символов")
        print(f"Бесплатный лимит: {pricing_info['free_tier_characters_per_month']:,} символов/месяц")
        print(f"\nПримеры стоимости:")
        examples = pricing_info['calculation_examples']
        for key, value in examples.items():
            print(f"  {key.replace('_', ' ').title()}: ${value:.6f} USD")
        
        print(f"\nПримечания:")
        for note in pricing_info['notes']:
            print(f"  • {note}")
        
        print(f"\nИсточник: {pricing_info['pricing_source']}")
        
        # Показываем краткую информацию о том, что такое 1 миллион символов
        print("\n" + "=" * 70)
        print("💡 Что такое 1 000 000 символов?")
        print("=" * 70)
        print("  • ~200-250 страниц книги (A4, одинарный интервал)")
        print("  • ~150-200 тысяч слов (английский текст)")
        print("  • ~2-3 часа чтения вслух")
        print("  • ~1 час аудио (со скоростью ~150 слов/мин)")
        print("  • Примерно как одна книга 'Гарри Поттер и философский камень'")
        print("\n  💰 Бесплатный лимит (500,000 символов) = ~30 минут аудио в месяц")
        print("     Используйте --examples для подробной информации")
        
        # Расчет стоимости для конкретного количества символов
        if args.chars or args.text:
            char_count = args.chars if args.chars else len(args.text)
            cost_info = provider.calculate_cost(char_count)
            
            print("\n" + "=" * 70)
            print(f"Расчет стоимости для {char_count:,} символов")
            print("=" * 70)
            print(f"Количество символов: {cost_info['character_count']:,}")
            print(f"Стоимость: ${cost_info['cost_usd']:.6f} USD")
            print(f"Стоимость (примерно): {cost_info['cost_rub']:.2f} RUB")
            print(f"Остаток бесплатного лимита: {cost_info['free_tier_remaining']:,} символов")
            print(f"Статус: {cost_info['message']}")
            
            if args.text:
                print(f"\nТекст: {args.text[:100]}{'...' if len(args.text) > 100 else ''}")


if __name__ == "__main__":
    main()

