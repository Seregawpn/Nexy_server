#!/usr/bin/env python3
"""
Тест подключения к production серверу через клиентский модуль
"""
import sys
import asyncio
import logging
from pathlib import Path

# Добавляем пути
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "client"))

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def test_production_connection():
    """Тест подключения к production серверу"""
    try:
        from modules.grpc_client.core.grpc_client import GrpcClient
        
        logger.info("=" * 60)
        logger.info("Тест подключения к production серверу")
        logger.info("=" * 60)
        
        # Создаем клиент с конфигурацией для production
        config = {
            'servers': {
                'production': {
                    'address': '20.151.51.172',
                    'port': 443,
                    'use_ssl': True,
                    'ssl_verify': False,  # Временно отключено для self-signed
                    'use_http2': True,
                    'timeout': 300,
                    'retry_attempts': 1,  # Одна попытка для быстрого теста
                    'retry_delay': 1.0,
                    'keepalive': True
                }
            },
            'auto_fallback': False,
            'connection_timeout': 60,
            'max_retry_attempts': 1
        }
        
        client = GrpcClient(config)
        
        logger.info(f"🔌 Попытка подключения к production серверу...")
        logger.info(f"   Адрес: 20.151.51.172:443")
        logger.info(f"   SSL: True")
        logger.info(f"   Таймаут: 60 секунд")
        
        # Переключаемся на production сервер и подключаемся
        await client.switch_server('production')
        connected = await client.connect('production')
        
        if connected:
            logger.info("✅ Подключение к production серверу успешно!")
            
            # Пробуем простой RPC вызов
            try:
                logger.info("🧪 Тестирование InterruptSession...")
                from modules.grpc_client.proto import streaming_pb2
                
                request = streaming_pb2.InterruptRequest(
                    hardware_id="test_connection"
                )
                
                # Получаем stub из connection_manager
                if not hasattr(client.connection_manager, 'stub') or not client.connection_manager.stub:
                    logger.error("❌ Stub недоступен")
                    return False
                
                stub = client.connection_manager.stub
                
                # Вызываем RPC напрямую
                result = await stub.InterruptSession(request, timeout=10.0)
                
                if result and result.success:
                    logger.info("✅ InterruptSession успешен!")
                else:
                    logger.warning("⚠️ InterruptSession вернул неожиданный результат")
                    
            except Exception as e:
                logger.error(f"❌ Ошибка при тестировании RPC: {e}")
            
            # Отключаемся
            await client.disconnect()
            logger.info("🔌 Отключено от сервера")
            
            return True
        else:
            logger.error("❌ Не удалось подключиться к production серверу")
            return False
            
    except Exception as e:
        logger.error(f"❌ Ошибка при тестировании: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False

async def main():
    """Главная функция"""
    success = await test_production_connection()
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
