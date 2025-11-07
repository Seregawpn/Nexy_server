#!/usr/bin/env python3
"""
Изолированный тест gRPC коммуникации с production сервером.
Тестирует только StreamAudio RPC без остального функционала клиента.
"""

import asyncio
import sys
import logging
from pathlib import Path

# Настраиваем логирование
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Добавляем пути для импорта
client_dir = Path(__file__).parent
sys.path.insert(0, str(client_dir))

from modules.grpc_client.core.grpc_client import GrpcClient


async def test_grpc_stream():
    """Тестирует gRPC стрим с production сервером"""

    # Конфигурация для production сервера
    config = {
        'servers': {
            'production': {
                'address': '20.151.51.172',
                'port': 443,
                'use_ssl': True,
                'ssl_verify': False,
                'use_http2': True,
                'timeout': 300,
                'retry_attempts': 3,
                'retry_delay': 1.0,
                'keepalive': True,
                'max_message_size': 50 * 1024 * 1024,
            }
        },
        'auto_fallback': False,
        'connection_timeout': 30,
        'max_retry_attempts': 3,
        'retry_delay': 1.0,
    }

    # Создаем клиент
    logger.info("=" * 80)
    logger.info("🚀 Создание gRPC клиента")
    client = GrpcClient(config=config)

    try:
        # Подключаемся к production серверу
        logger.info("=" * 80)
        logger.info("🔌 Подключение к production серверу: 20.151.51.172:443")
        success = await client.connect('production')

        if not success:
            logger.error("❌ Не удалось подключиться к серверу")
            return False

        logger.info("✅ Подключение установлено")

        # Тестовые данные
        test_prompt = "Hello, how are you?"
        test_hardware_id = "E03D24552A85439BB41CD02E6F62BB75"  # Ваш hardware ID
        test_screenshot = ""  # Без скриншота для простоты
        screen_info = {"width": 1920, "height": 1080}

        logger.info("=" * 80)
        logger.info(f"📤 Отправка запроса:")
        logger.info(f"   Prompt: '{test_prompt}'")
        logger.info(f"   Hardware ID: {test_hardware_id[:8]}...")
        logger.info(f"   Screenshot: {'Yes' if test_screenshot else 'No'}")
        logger.info(f"   Screen: {screen_info['width']}x{screen_info['height']}")

        # Счетчики для статистики
        response_count = 0
        text_chunks = []
        audio_chunks = []
        audio_bytes_total = 0

        logger.info("=" * 80)
        logger.info("📥 Получение ответов от сервера:")

        # Стримим ответы
        async for resp in client.stream_audio(
            prompt=test_prompt,
            screenshot_base64=test_screenshot,
            screen_info=screen_info,
            hardware_id=test_hardware_id,
        ):
            response_count += 1

            # Определяем тип ответа
            which_oneof = resp.WhichOneof('content') if hasattr(resp, 'WhichOneof') else None

            logger.info(f"   Response #{response_count}: type={which_oneof}")

            if which_oneof == 'text_chunk':
                text = resp.text_chunk
                text_chunks.append(text)
                logger.info(f"      📝 Text chunk: '{text[:100]}{'...' if len(text) > 100 else ''}'")

            elif which_oneof == 'audio_chunk':
                ch = resp.audio_chunk
                data = bytes(ch.audio_data) if ch.audio_data else b""
                dtype = ch.dtype or 'int16'
                shape = list(ch.shape) if ch.shape else []

                if len(data) > 0:
                    audio_chunks.append(data)
                    audio_bytes_total += len(data)
                    logger.info(f"      🔊 Audio chunk: {len(data)} bytes, dtype={dtype}, shape={shape}")
                else:
                    logger.warning(f"      ⚠️  Empty audio chunk (skipping)")

            elif which_oneof == 'end_message':
                end_msg = resp.end_message
                logger.info(f"      ✅ End message: '{end_msg}'")
                break

            elif which_oneof == 'error_message':
                err_msg = resp.error_message
                logger.error(f"      ❌ Error message: '{err_msg}'")
                return False

            else:
                logger.warning(f"      ⚠️  Unknown response type: {which_oneof}")

        # Итоговая статистика
        logger.info("=" * 80)
        logger.info("📊 Статистика:")
        logger.info(f"   Всего ответов: {response_count}")
        logger.info(f"   Текстовых чанков: {len(text_chunks)}")
        logger.info(f"   Аудио чанков: {len(audio_chunks)}")
        logger.info(f"   Аудио байтов: {audio_bytes_total}")

        if len(text_chunks) > 0:
            full_text = ''.join(text_chunks)
            logger.info(f"   Полный текст: '{full_text}'")

        # Проверка результата
        logger.info("=" * 80)
        if audio_bytes_total > 0:
            logger.info("✅ ТЕСТ УСПЕШЕН: Получены аудио данные")
            return True
        else:
            logger.error("❌ ТЕСТ НЕ ПРОЙДЕН: Аудио данные НЕ получены")
            logger.error("   Сервер завершил обработку без отправки аудио!")
            return False

    except Exception as e:
        logger.error(f"❌ Ошибка во время теста: {e}", exc_info=True)
        return False

    finally:
        # Очистка
        await client.cleanup()
        logger.info("=" * 80)
        logger.info("🧹 Очистка завершена")


async def main():
    """Главная функция"""
    logger.info("=" * 80)
    logger.info("🧪 ИЗОЛИРОВАННЫЙ ТЕСТ gRPC КОММУНИКАЦИИ")
    logger.info("=" * 80)

    success = await test_grpc_stream()

    logger.info("=" * 80)
    if success:
        logger.info("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ")
        sys.exit(0)
    else:
        logger.error("❌ ТЕСТЫ НЕ ПРОЙДЕНЫ")
        sys.exit(1)


if __name__ == '__main__':
    asyncio.run(main())
