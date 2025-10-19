#!/usr/bin/env python3
"""
Простой тест gRPC соединения для диагностики
"""

import asyncio
import grpc
import grpc.aio
import logging
import time
from typing import Optional

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class GrpcConnectionTest:
    """Тест gRPC соединения"""
    
    def __init__(self, host: str = "20.151.51.172", port: int = 50051):
        self.host = host
        self.port = port
        self.address = f"{host}:{port}"
        self.channel: Optional[grpc.aio.Channel] = None
        
    async def test_connection(self) -> bool:
        """Тестирует gRPC соединение"""
        try:
            logger.info(f"🔄 Тестируем соединение с {self.address}")
            
            # Создаем insecure канал
            self.channel = grpc.aio.insecure_channel(
                self.address,
                options=[
                    ('grpc.keepalive_time_ms', 10000),
                    ('grpc.keepalive_timeout_ms', 5000),
                    ('grpc.keepalive_permit_without_calls', True),
                    ('grpc.http2.max_pings_without_data', 0),
                    ('grpc.http2.min_time_between_pings_ms', 10000),
                    ('grpc.http2.min_ping_interval_without_data_ms', 300000)
                ]
            )
            
            logger.info(f"📡 Канал создан, проверяем готовность...")
            
            # Ждем готовности канала с таймаутом
            try:
                await asyncio.wait_for(
                    self.channel.channel_ready(),
                    timeout=30.0
                )
                logger.info(f"✅ Соединение с {self.address} установлено успешно!")
                return True
                
            except asyncio.TimeoutError:
                logger.error(f"⏰ Таймаут соединения с {self.address}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Ошибка соединения с {self.address}: {e}")
            return False
            
    async def test_health_check(self) -> bool:
        """Тестирует health check"""
        try:
            if not self.channel:
                logger.error("❌ Канал не создан")
                return False
                
            logger.info(f"🏥 Тестируем health check...")
            
            # Здесь можно добавить реальный health check
            # Пока просто проверяем, что канал активен
            state = self.channel.get_state()
            logger.info(f"📊 Состояние канала: {state}")
            
            return state == grpc.ChannelConnectivity.READY
            
        except Exception as e:
            logger.error(f"❌ Ошибка health check: {e}")
            return False
            
    async def cleanup(self):
        """Очистка ресурсов"""
        if self.channel:
            try:
                await self.channel.close()
                logger.info("🧹 Канал закрыт")
            except Exception as e:
                logger.error(f"❌ Ошибка закрытия канала: {e}")

async def main():
    """Основная функция теста"""
    logger.info("🚀 Запуск теста gRPC соединения")
    
    test = GrpcConnectionTest()
    
    try:
        # Тест соединения
        connection_ok = await test.test_connection()
        
        if connection_ok:
            # Тест health check
            health_ok = await test.test_health_check()
            
            if health_ok:
                logger.info("🎉 Все тесты пройдены успешно!")
            else:
                logger.warning("⚠️ Соединение установлено, но health check не прошел")
        else:
            logger.error("💥 Тест соединения не прошел")
            
    except Exception as e:
        logger.error(f"💥 Критическая ошибка: {e}")
        
    finally:
        await test.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
