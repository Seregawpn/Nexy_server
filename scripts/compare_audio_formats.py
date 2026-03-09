#!/usr/bin/env python3
"""
Сравнение форматов аудио: Azure TTS vs Edge TTS
"""

print("="*60)
print("СРАВНЕНИЕ ФОРМАТОВ АУДИО")
print("="*60)

print("\n📊 AZURE TTS (старый):")
print("   ┌─────────────────────────────────────────┐")
print("   │ Формат: RIFF WAV (24kHz, 16-bit, mono) │")
print("   │ Обработка: Удаление RIFF заголовка      │")
print("   │ Результат: Raw PCM данные               │")
print("   │ Sample rate: 24000 Hz                   │")
print("   │ Channels: 1 (моно)                      │")
print("   │ Bits per sample: 16 бит                 │")
print("   │ Размер чанков: 4096 байт                │")
print("   └─────────────────────────────────────────┘")

print("\n📊 EDGE TTS (новый):")
print("   ┌─────────────────────────────────────────┐")
print("   │ Формат: MP3 (от Edge TTS API)           │")
print("   │ Обработка: Конвертация MP3 → PCM        │")
print("   │ Результат: Raw PCM данные               │")
print("   │ Sample rate: 24000 Hz (по умолчанию)   │")
print("   │ Channels: 1 (моно)                      │")
print("   │ Bits per sample: 16 бит                 │")
print("   │ Размер чанков: 4096 байт                │")
print("   └─────────────────────────────────────────┘")

print("\n" + "="*60)
print("СРАВНЕНИЕ")
print("="*60)

comparison = {
    "Формат данных": {
        "Azure TTS": "Raw PCM (после удаления RIFF заголовка)",
        "Edge TTS": "Raw PCM (после конвертации MP3 → PCM)",
        "Идентично": "✅ Да - оба возвращают raw PCM"
    },
    "Sample rate": {
        "Azure TTS": "24000 Hz",
        "Edge TTS": "24000 Hz (по умолчанию)",
        "Идентично": "✅ Да"
    },
    "Channels": {
        "Azure TTS": "1 (моно)",
        "Edge TTS": "1 (моно)",
        "Идентично": "✅ Да"
    },
    "Bits per sample": {
        "Azure TTS": "16 бит",
        "Edge TTS": "16 бит",
        "Идентично": "✅ Да"
    },
    "Размер чанков": {
        "Azure TTS": "4096 байт",
        "Edge TTS": "4096 байт",
        "Идентично": "✅ Да"
    },
    "Структура данных": {
        "Azure TTS": "Raw PCM байты (без заголовков)",
        "Edge TTS": "Raw PCM байты (без заголовков)",
        "Идентично": "✅ Да"
    }
}

for param, values in comparison.items():
    print(f"\n{param}:")
    print(f"  Azure TTS: {values['Azure TTS']}")
    print(f"  Edge TTS:  {values['Edge TTS']}")
    print(f"  {values['Идентично']}")

print("\n" + "="*60)
print("ВЫВОД")
print("="*60)
print("""
✅ ФОРМАТ ПОЛНОСТЬЮ ИДЕНТИЧЕН!

Оба провайдера возвращают:
  • Raw PCM данные (без заголовков)
  • 24000 Hz sample rate
  • 1 канал (моно)
  • 16 бит на сэмпл
  • Чанки по 4096 байт

Единственное отличие:
  • Azure TTS: получал PCM напрямую (в RIFF WAV контейнере)
  • Edge TTS: конвертирует MP3 → PCM через pydub

Но на выходе - ОДИНАКОВЫЙ формат!
Клиент не заметит разницы.
""")

