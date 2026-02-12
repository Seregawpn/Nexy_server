#!/usr/bin/env python3
"""
Тест для проверки WebP функциональности скриншотов
"""

import asyncio
import base64
from pathlib import Path
import sys

import pytest

# Добавляем путь к модулям
sys.path.insert(0, str(Path(__file__).parent.parent))

from modules.screenshot_capture.core.screenshot_capture import ScreenshotCapture
from modules.screenshot_capture.core.types import (
    ScreenshotConfig,
    ScreenshotFormat,
    ScreenshotQuality,
    ScreenshotRegion,
)

pytestmark = pytest.mark.asyncio


def _skip_if_capture_unavailable(error: str | None) -> None:
    if not error:
        return
    markers = (
        "CGDisplayCreateImage failed",
        "screen recording permission",
        "permission denied",
    )
    lowered = error.lower()
    if any(marker.lower() in lowered for marker in markers):
        pytest.skip(f"Screenshot environment unavailable: {error}")


async def test_webp_capture():
    """Тест захвата скриншота в формате WebP"""
    print("🧪 Тест WebP захвата скриншотов")
    print("=" * 60)

    # Создаем конфигурацию для WebP
    config = ScreenshotConfig(
        format=ScreenshotFormat.WEBP,
        quality=ScreenshotQuality.MEDIUM,  # Должно быть 80
        region=ScreenshotRegion.FULL_SCREEN,
        max_width=1280,
        max_height=720,
        timeout=5.0,
    )

    print(f"📋 Конфигурация:")
    print(f"   Формат: {config.format.value}")
    print(f"   Качество: {config.quality.value}")
    print(f"   Макс. размер: {config.max_width}x{config.max_height}")
    print()

    # Создаем захватчик
    try:
        capture = ScreenshotCapture(config)
        print("✅ ScreenshotCapture инициализирован")
    except Exception as e:
        raise AssertionError(f"Ошибка инициализации: {e}") from e

    # Проверяем статус
    status = capture.get_status()
    print(f"📊 Статус модуля:")
    print(f"   Инициализирован: {status['initialized']}")
    print(f"   Bridge доступен: {status['bridge_available']}")
    print(f"   Формат: {status['config']['format']}")
    print(f"   Качество: {status['config']['quality']}")
    print()

    # Тестируем захват
    print("📸 Захват скриншота...")
    result = await capture.capture_screenshot()
    _skip_if_capture_unavailable(result.error)
    assert result.success, f"Захват не удался: {result.error}"

    print(f"✅ Скриншот захвачен успешно!")
    print(f"   Формат: {result.data.format.value}")
    print(f"   Размеры: {result.data.width}x{result.data.height}")
    print(f"   Размер файла: {result.data.size_bytes} bytes")
    print(f"   MIME-тип: {result.data.mime_type}")
    print(f"   Время захвата: {result.capture_time:.3f}s")
    print()

    # Проверяем формат
    if result.data.format != ScreenshotFormat.WEBP:
        raise AssertionError(f"Ожидался WebP, получен {result.data.format.value}")

    # Проверяем Base64
    if not result.data.base64_data:
        raise AssertionError("Base64 данные отсутствуют")

    # Декодируем и проверяем WebP сигнатуру
    webp_data = base64.b64decode(result.data.base64_data)

    # WebP файл начинается с "RIFF" и содержит "WEBP"
    if webp_data[:4] != b"RIFF":
        raise AssertionError("Неверная сигнатура WebP (ожидается RIFF)")

    if b"WEBP" not in webp_data[:12]:
        raise AssertionError("Неверная сигнатура WebP (ожидается WEBP)")

    print("✅ WebP сигнатура корректна")
    print(f"   Размер декодированных данных: {len(webp_data)} bytes")

    # Проверяем качество из метаданных
    if "quality" in result.data.metadata:
        quality = result.data.metadata["quality"]
        print(f"   Качество: {quality}")
        if quality != 80:
            raise AssertionError(f"Ожидалось качество 80, получено {quality}")

    print()
    print("✅ Все проверки пройдены успешно!")


async def test_jpeg_fallback():
    """Тест fallback на JPEG при проблемах с WebP"""
    print("\n🧪 Тест fallback на JPEG")
    print("=" * 60)

    # Создаем конфигурацию для WebP
    config = ScreenshotConfig(
        format=ScreenshotFormat.WEBP,
        quality=ScreenshotQuality.MEDIUM,
        region=ScreenshotRegion.FULL_SCREEN,
        timeout=5.0,
    )

    capture = ScreenshotCapture(config)

    # Захватываем (должен работать с fallback если нужно)
    result = await capture.capture_screenshot()
    _skip_if_capture_unavailable(result.error)
    assert result.success, f"Захват не удался: {result.error}"
    print(f"✅ Захват выполнен: {result.data.format.value}")


async def test_quality_levels():
    """Тест различных уровней качества"""
    print("\n🧪 Тест уровней качества WebP")
    print("=" * 60)

    quality_levels = [
        (ScreenshotQuality.LOW, 50),
        (ScreenshotQuality.MEDIUM, 80),
        (ScreenshotQuality.HIGH, 85),
        (ScreenshotQuality.MAXIMUM, 95),
    ]

    for quality_enum, expected_quality in quality_levels:
        config = ScreenshotConfig(
            format=ScreenshotFormat.WEBP,
            quality=quality_enum,
            region=ScreenshotRegion.FULL_SCREEN,
            max_width=640,
            max_height=480,
            timeout=5.0,
        )

        capture = ScreenshotCapture(config)
        result = await capture.capture_screenshot()
        _skip_if_capture_unavailable(result.error)
        assert result.success, f"{quality_enum.value}: захват не удался: {result.error}"
        assert result.data.format == ScreenshotFormat.WEBP, (
            f"{quality_enum.value}: ожидался WebP, получен {result.data.format.value}"
        )
        actual_quality = result.data.metadata.get("quality", 0)
        size = result.data.size_bytes
        assert actual_quality == expected_quality, (
            f"{quality_enum.value}: качество={actual_quality}, ожидалось {expected_quality}"
        )
        print(
            f"✅ {quality_enum.value:8s}: качество={actual_quality:3d} "
            f"(ожидается {expected_quality}), размер={size:6d} bytes"
        )


async def main():
    """Главная функция тестирования"""
    print("\n" + "=" * 60)
    print("🚀 Запуск тестов WebP функциональности")
    print("=" * 60 + "\n")

    results = []

    # Тест 1: Основной тест WebP
    results.append(await test_webp_capture())

    # Тест 2: Fallback на JPEG
    results.append(await test_jpeg_fallback())

    # Тест 3: Уровни качества
    await test_quality_levels()

    # Итоги
    print("\n" + "=" * 60)
    print("📊 Итоги тестирования")
    print("=" * 60)

    passed = sum(results)
    total = len(results)

    print(f"✅ Пройдено: {passed}/{total}")
    print(f"❌ Провалено: {total - passed}/{total}")

    if passed == total:
        print("\n🎉 Все тесты пройдены успешно!")
        return 0
    else:
        print("\n⚠️ Некоторые тесты провалены")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
