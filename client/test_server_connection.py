#!/usr/bin/env python3
"""Тест подключения к gRPC серверу"""

import asyncio
import sys
import logging
from pathlib import Path

project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def test_connection():
    try:
        from modules.grpc_client.core.grpc_client import GrpcClient
        from config.unified_config_loader import UnifiedConfigLoader
        from config.server_manager import get_default_server
        
        logger.info("=" * 70)
        logger.info("🔌 ПОДКЛЮЧЕНИЕ К gRPC СЕРВЕРУ")
        logger.info("=" * 70)
        
        # Загружаем конфигурацию
        config_loader = UnifiedConfigLoader.get_instance()
        network_config = config_loader.get_network_config()
        default_server = get_default_server() or 'production'
        
        logger.info(f"\n📋 Конфигурация:")
        logger.info(f"   Сервер по умолчанию: {default_server}")
        
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
        logger.info("   Ожидание...")
        
        try:
            connected = await asyncio.wait_for(
                client.connection_manager.connect(default_server),
                timeout=30.0
            )
            
            if connected:
                state = client.connection_manager.get_connection_state()
                logger.info(f"\n{'='*70}")
                logger.info("✅ ПОДКЛЮЧЕНИЕ УСТАНОВЛЕНО УСПЕШНО!")
                logger.info(f"{'='*70}")
                logger.info(f"\n📊 Статус:")
                logger.info(f"   Состояние: {state.value}")
                
                # Проверяем канал
                channel = client.connection_manager.channel
                if channel:
                    channel_state = channel.get_state()
                    state_names = {
                        0: "IDLE",
                        1: "CONNECTING", 
                        2: "READY ✅",
                        3: "TRANSIENT_FAILURE",
                        4: "SHUTDOWN"
                    }
                    logger.info(f"   Канал: {state_names.get(channel_state, channel_state)}")
                
                # Метрики
                metrics = client.connection_manager.get_metrics()
                logger.info(f"\n📈 Метрики:")
                logger.info(f"   Успешных подключений: {metrics.successful_connections}")
                logger.info(f"   Неудачных подключений: {metrics.failed_connections}")
                if metrics.last_connection_time:
                    logger.info(f"   Последнее подключение: {metrics.last_connection_time}")
                
                # Проверяем, что канал действительно работает
                logger.info(f"\n🔍 Проверка работоспособности...")
                if channel and channel.get_state() == 2:  # READY
                    logger.info("   ✅ Канал готов к использованию")
                    logger.info("   ✅ Можно отправлять gRPC запросы")
                else:
                    logger.warning("   ⚠️ Канал не готов")
                
                # Отключаемся
                logger.info(f"\n🔌 Отключение...")
                await client.connection_manager.disconnect()
                logger.info("   ✅ Отключено")
                
                logger.info(f"\n{'='*70}")
                logger.info("✅ ТЕСТ ЗАВЕРШЕН УСПЕШНО")
                logger.info(f"{'='*70}\n")
                return True
            else:
                logger.error(f"\n{'='*70}")
                logger.error("❌ ПОДКЛЮЧЕНИЕ НЕ УДАЛОСЬ")
                logger.error(f"{'='*70}")
                metrics = client.connection_manager.get_metrics()
                if metrics.last_error:
                    logger.error(f"\n   Ошибка: {metrics.last_error}")
                logger.error("\n   Возможные причины:")
                logger.error("   - Сервер недоступен")
                logger.error("   - Проблемы с сетью")
                logger.error("   - Неверный сертификат")
                logger.error("   - Файрвол блокирует соединение\n")
                return False
                
        except asyncio.TimeoutError:
            logger.error(f"\n{'='*70}")
            logger.error("⏰ ТАЙМАУТ ПОДКЛЮЧЕНИЯ (>30 сек)")
            logger.error(f"{'='*70}")
            logger.error("\n   Сервер не отвечает в течение 30 секунд")
            logger.error("   Проверьте доступность сервера\n")
            return False
        except Exception as e:
            logger.error(f"\n{'='*70}")
            logger.error(f"❌ ОШИБКА: {e}")
            logger.error(f"{'='*70}")
            import traceback
            logger.error("\nДетали ошибки:")
            traceback.print_exc()
            logger.error("")
            return False
            
    except Exception as e:
        logger.error(f"❌ КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    result = asyncio.run(test_connection())
    sys.exit(0 if result else 1)
