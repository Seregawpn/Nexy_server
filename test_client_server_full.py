#!/usr/bin/env python3
"""
Полный тест клиент-сервер: имитация реального запроса от клиента к серверу
Инициализирует систему так же, как реальное приложение, и отправляет запрос
"""
import sys
import asyncio
import logging
import uuid
from pathlib import Path

# Добавляем пути (как в main.py)
project_root = Path(__file__).parent
client_root = project_root / "client"

# Добавляем пути для импортов
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(client_root))
sys.path.insert(0, str(client_root / "integration"))
sys.path.insert(0, str(client_root / "modules"))
sys.path.insert(0, str(client_root / "config"))

# Устанавливаем рабочую директорию для правильного поиска конфигурации
import os
os.chdir(str(client_root))

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Отключаем избыточное логирование
logging.getLogger('grpc').setLevel(logging.WARNING)

async def test_full_client_request():
    """Полный тест: инициализация как в реальном приложении и отправка запроса"""
    try:
        logger.info("=" * 80)
        logger.info("ПОЛНЫЙ ТЕСТ КЛИЕНТ-СЕРВЕР: Имитация реального запроса")
        logger.info("=" * 80)
        logger.info("")
        
        # 1. Инициализация core компонентов (как в SimpleModuleCoordinator)
        logger.info("🔧 Шаг 1: Инициализация core компонентов...")
        from integration.core.event_bus import EventBus, EventPriority
        from integration.core.state_manager import ApplicationStateManager
        from integration.core.error_handler import ErrorHandler
        
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler(event_bus)
        
        # Подключаем state_manager к event_bus
        state_manager.attach_event_bus(event_bus)
        
        logger.info("✅ Core компоненты инициализированы")
        logger.info("")
        
        # 2. Инициализация GrpcClientIntegration (как в SimpleModuleCoordinator)
        logger.info("🔧 Шаг 2: Инициализация GrpcClientIntegration...")
        from integration.integrations.grpc_client_integration import GrpcClientIntegration, GrpcClientIntegrationConfig
        
        # Конфигурация для production сервера
        config = GrpcClientIntegrationConfig(
            aggregate_timeout_sec=0.0,  # Отправлять сразу
            request_timeout_sec=60.0,   # Увеличенный таймаут для production
            max_retries=2,              # Меньше попыток для теста
            retry_delay_sec=1.0,
            server="production",        # Production сервер
            use_network_gate=False        # Отключаем network gate для теста
        )
        
        grpc_integration = GrpcClientIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            config=config
        )
        
        # Инициализация интеграции
        init_success = await grpc_integration.initialize()
        if not init_success:
            logger.error("❌ Не удалось инициализировать GrpcClientIntegration")
            return False
        
        logger.info("✅ GrpcClientIntegration инициализирован")
        logger.info("")
        
        # 3. Запуск интеграции (подключение к серверу)
        logger.info("🔧 Шаг 3: Запуск интеграции и подключение к серверу...")
        start_success = await grpc_integration.start()
        if not start_success:
            logger.error("❌ Не удалось запустить GrpcClientIntegration")
            return False
        
        # Ждём подключения (eager connect)
        logger.info("⏳ Ожидание подключения к серверу...")
        await asyncio.sleep(3)  # Даём время на подключение
        
        logger.info("✅ Интеграция запущена")
        logger.info("")
        
        # 4. Подготовка данных для запроса (как в реальном приложении)
        logger.info("🔧 Шаг 4: Подготовка данных для запроса...")
        session_id = str(uuid.uuid4())
        test_text = "Привет, это тестовый запрос от клиента"
        
        # Устанавливаем hardware_id через событие (как в реальном приложении)
        hardware_id = "test_hardware_id_" + session_id[:8]
        await event_bus.publish("hardware.id_obtained", {
            "uuid": hardware_id  # GrpcClientIntegration ожидает поле "uuid"
        })
        
        # Ждём немного, чтобы событие обработалось
        await asyncio.sleep(0.5)
        
        logger.info(f"   Session ID: {session_id}")
        logger.info(f"   Hardware ID: {hardware_id}")
        logger.info(f"   Текст: {test_text}")
        logger.info("")
        
        # 5. Отправка события voice.recognition_completed (как в реальном приложении)
        logger.info("🔧 Шаг 5: Отправка события voice.recognition_completed...")
        
        # Создаём событие как в реальном приложении
        voice_event = {
            "session_id": session_id,
            "text": test_text,
            "confidence": 0.95,
            "language": "ru-RU",
            "duration_ms": 1000
        }
        
        # Публикуем событие
        await event_bus.publish("voice.recognition_completed", voice_event)
        logger.info("✅ Событие voice.recognition_completed отправлено")
        logger.info("")
        
        # 6. Ожидание ответа от сервера
        logger.info("🔧 Шаг 6: Ожидание ответа от сервера...")
        logger.info("   (Это может занять некоторое время...)")
        
        # Создаём Future для отслеживания ответа
        response_received = asyncio.Future()
        audio_chunks_received = []
        error_received = None
        
        async def on_audio_chunk(event):
            """Обработчик аудио чанков от сервера"""
            try:
                data = event.get("data", {}) if isinstance(event, dict) else (event or {})
                chunk_bytes = data.get("bytes")
                if chunk_bytes:
                    audio_chunks_received.append(len(chunk_bytes))
                    logger.info(f"   📦 Получен аудио чанк: {len(chunk_bytes)} байт")
            except Exception as e:
                logger.error(f"   ❌ Ошибка обработки аудио чанка: {e}")
        
        async def on_audio_complete(event):
            """Обработчик завершения аудио"""
            logger.info("   ✅ Запрос завершён успешно")
            if not response_received.done():
                response_received.set_result(True)
        
        async def on_error(event):
            """Обработчик ошибок"""
            nonlocal error_received
            data = event.get("data", {}) if isinstance(event, dict) else (event or {})
            error_received = data.get("error") or "Unknown error"
            logger.error(f"   ❌ Ошибка от сервера: {error_received}")
            if not response_received.done():
                response_received.set_result(False)
        
        # Подписываемся на события ответа (правильные имена событий из grpc_client_integration)
        await event_bus.subscribe("grpc.response.audio", on_audio_chunk, EventPriority.HIGH)
        await event_bus.subscribe("grpc.request_completed", on_audio_complete, EventPriority.HIGH)
        await event_bus.subscribe("grpc.request_failed", on_error, EventPriority.HIGH)
        
        # Ждём ответа (без таймаута)
        try:
            result = await response_received
            logger.info("")
            if result:
                logger.info("✅ Ответ от сервера получен успешно!")
                logger.info(f"   Получено аудио чанков: {len(audio_chunks_received)}")
                if audio_chunks_received:
                    total_bytes = sum(audio_chunks_received)
                    logger.info(f"   Всего байт: {total_bytes}")
            else:
                logger.error("❌ Получена ошибка от сервера")
                return False
        except asyncio.TimeoutError:
            logger.error("❌ Таймаут ожидания ответа от сервера (60 секунд)")
            return False
        except Exception as e:
            logger.error(f"❌ Ошибка при ожидании ответа: {e}")
            return False
        
        logger.info("")
        
        # 7. Остановка интеграции
        logger.info("🔧 Шаг 7: Остановка интеграции...")
        await grpc_integration.stop()
        logger.info("✅ Интеграция остановлена")
        logger.info("")
        
        logger.info("=" * 80)
        logger.info("✅ ТЕСТ ЗАВЕРШЁН УСПЕШНО")
        logger.info("=" * 80)
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Критическая ошибка в тесте: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False

async def main():
    """Главная функция"""
    success = await test_full_client_request()
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
