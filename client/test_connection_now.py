#!/usr/bin/env python3
"""Быстрый тест подключения к gRPC серверу"""

import asyncio
import sys
import logging
from pathlib import Path

project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def test():
    try:
        from modules.grpc_client.core.grpc_client import GrpcClient
        from config.unified_config_loader import UnifiedConfigLoader
        from config.server_manager import get_default_server
        
        logger.info("=" * 60)
        logger.info("🔍 ТЕСТ ПОДКЛЮЧЕНИЯ К gRPC СЕРВЕРУ")
        logger.info("=" * 60)
        
        # Загружаем конфигурацию
        config_loader = UnifiedConfigLoader.get_instance()
        network_config = config_loader.get_network_config()
        default_server = get_default_server() or 'production'
        
        logger.info(f"\n📋 Сервер: {default_server}")
        if default_server not in network_config.grpc_servers:
            logger.error(f"❌ Сервер '{default_server}' не найден")
            return False
        
        server = network_config.grpc_servers[default_server]
        logger.info(f"   Host: {server.host}")
        logger.info(f"   Port: {server.port}")
        logger.info(f"   SSL: {server.ssl}")
        logger.info(f"   SSL Verify: {server.ssl_verify}")
        
        # Создаем клиент
        servers_cfg = {}
        for name, s in network_config.grpc_servers.items():
            servers_cfg[name] = {
                'address': s.host,
                'port': s.port,
                'use_ssl': s.ssl,
                'ssl_verify': s.ssl_verify,
                'use_http2': s.use_http2,
                'keepalive': s.keepalive,
                'timeout': s.timeout,
                'retry_attempts': s.retry_attempts,
                'retry_delay': s.retry_delay,
            }
        
        client = GrpcClient(config={'servers': servers_cfg})
        logger.info("\n✅ gRPC клиент создан")
        
        # Подключаемся
        logger.info(f"\n🔌 Подключение к {server.host}:{server.port}...")
        try:
            connected = await asyncio.wait_for(
                client.connection_manager.connect(default_server),
                timeout=30.0
            )
            
            if connected:
                state = client.connection_manager.get_connection_state()
                logger.info(f"\n✅ ПОДКЛЮЧЕНИЕ УСТАНОВЛЕНО!")
                logger.info(f"   Состояние: {state.value}")
                
                # Проверяем канал
                channel = client.connection_manager.channel
                if channel:
                    channel_state = channel.get_state()
                    state_names = {
                        0: "IDLE",
                        1: "CONNECTING", 
                        2: "READY",
                        3: "TRANSIENT_FAILURE",
                        4: "SHUTDOWN"
                    }
                    logger.info(f"   Канал: {state_names.get(channel_state, channel_state)} ({channel_state})")
                
                # Метрики
                metrics = client.connection_manager.get_metrics()
                logger.info(f"   Успешных подключений: {metrics.successful_connections}")
                logger.info(f"   Неудачных подключений: {metrics.failed_connections}")
                
                # Отключаемся
                await client.connection_manager.disconnect()
                logger.info(f"\n✅ Отключено")
                
                logger.info("\n" + "=" * 60)
                logger.info("✅ ТЕСТ ПРОЙДЕН УСПЕШНО")
                logger.info("=" * 60)
                return True
            else:
                logger.error("\n❌ ПОДКЛЮЧЕНИЕ НЕ УДАЛОСЬ")
                metrics = client.connection_manager.get_metrics()
                if metrics.last_error:
                    logger.error(f"   Ошибка: {metrics.last_error}")
                return False
                
        except asyncio.TimeoutError:
            logger.error("\n⏰ ТАЙМАУТ ПОДКЛЮЧЕНИЯ (>30 сек)")
            return False
        except Exception as e:
            logger.error(f"\n❌ ОШИБКА: {e}")
            import traceback
            traceback.print_exc()
            return False
            
    except Exception as e:
        logger.error(f"❌ КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    result = asyncio.run(test())
    sys.exit(0 if result else 1)
