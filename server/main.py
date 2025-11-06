import asyncio
import inspect
import logging
import signal
import sys
import os
from contextlib import suppress
from dataclasses import asdict
from typing import Awaitable, Callable, List

from aiohttp import web
from modules.grpc_service.core.grpc_server import run_server as serve
from dotenv import load_dotenv
from config.unified_config import get_config
from utils.logging_formatter import (
    setup_structured_logging,
    log_server_start,
    log_server_stop,
    log_degradation
)
from utils.metrics_collector import get_metrics_collector
from modules.grpc_service.core.backpressure import get_backpressure_manager

# 🚀 Тест автоматического деплоя - 30 сентября 2025

# Загружаем config.env
load_dotenv('config.env')

# Загружаем конфигурацию
unified_config = get_config()
server_metadata = unified_config.get_server_metadata()

# Настройка структурированного логирования (PR-4)
log_level = unified_config.logging.level if hasattr(unified_config, 'logging') else 'INFO'
setup_structured_logging(level=log_level)
logger = logging.getLogger(__name__)

# Версия сервера (единая точка истины для health/status эндпоинтов)
SERVER_VERSION = server_metadata.version
SERVER_BUILD = server_metadata.build

# Импорт системы обновлений
try:
    from modules.update.core.update_manager import UpdateManager
    from modules.update.config import UpdateConfig
    UPDATE_SERVER_AVAILABLE = True
    logger.info("Update Server module found", extra={'scope': 'update', 'decision': 'init'})
except ImportError as e:
    logger.warning(f"Update Server not found: {e}", extra={'scope': 'update', 'decision': 'degrade'})
    UPDATE_SERVER_AVAILABLE = False
 
async def health_handler(request):
    """
    Health check для Container Apps (PR-7 compliance)

    Returns:
        JSON response with:
        - status: "OK"
        - latest_version: string (must match SERVER_VERSION)
        - latest_build: string (must equal latest_version per Section 11)
    """
    return web.json_response({
        "status": "OK",
        "latest_version": SERVER_VERSION,
        "latest_build": SERVER_BUILD
    })

async def root_handler(request):
    """Корневой endpoint"""
    return web.Response(text="Voice Assistant Server is running!", status=200)

async def status_handler(request):
    """
    Статус сервера (PR-7 compliance)

    Returns:
        JSON response with:
        - status: "running"
        - version: string (renamed from 'version' to 'latest_version' for consistency)
        - latest_build: string (must equal version per Section 11)
        - service info and endpoints
    """
    return web.json_response({
        "status": "running",
        "service": "voice-assistant",
        "latest_version": SERVER_VERSION,
        "latest_build": SERVER_BUILD,
        "update_server": "enabled" if UPDATE_SERVER_AVAILABLE else "disabled",
        "endpoints": {
            "health": "/health",
            "status": "/status",
            "grpc": "port 50051",
            "updates": (
                f"port {unified_config.get_update_service_config().port}"
                if UPDATE_SERVER_AVAILABLE
                else "disabled"
            )
        }
    })

async def periodic_metrics_logging():
    """Периодическое логирование метрик (PR-4)"""
    collector = get_metrics_collector(aggregation_interval=60)
    
    while True:
        try:
            await asyncio.sleep(60)  # Логируем каждые 60 секунд
            collector.log_metrics()
        except asyncio.CancelledError:
            break
        except Exception as e:
            logger.error(f"Ошибка логирования метрик: {e}", extra={
                'scope': 'metrics',
                'decision': 'error',
                'ctx': {'error': str(e)}
            })

# Глобальные переменные для graceful shutdown
CleanupCallback = Callable[[], Awaitable[None] | None]
shutdown_event = asyncio.Event()
servers_cleanup: List[CleanupCallback] = []


def register_cleanup(callback: CleanupCallback) -> None:
    """Регистрирует функцию очистки для graceful shutdown"""

    servers_cleanup.append(callback)


async def cancel_task(task: asyncio.Task) -> None:
    """Отменяет asyncio.Task с подавлением CancelledError"""

    task.cancel()
    with suppress(asyncio.CancelledError):
        await task


def setup_signal_handlers():
    """Настройка обработчиков сигналов для graceful shutdown (PR-7)"""
    def signal_handler(signum, frame):
        logger.info(f"Received signal {signum}, initiating graceful shutdown...", extra={
            'scope': 'server',
            'decision': 'shutdown',
            'ctx': {'signal': signum}
        })
        shutdown_event.set()
    
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)


async def graceful_shutdown():
    """Graceful shutdown всех серверов (PR-7)"""
    logger.info("Starting graceful shutdown...", extra={
        'scope': 'server',
        'decision': 'shutdown',
        'ctx': {}
    })
    
    # Останавливаем backpressure manager
    backpressure_manager = get_backpressure_manager()
    await backpressure_manager.stop()
    
    # Логируем итоговые метрики
    collector = get_metrics_collector()
    collector.log_metrics()
    
    # Очищаем все серверы
    for cleanup_func in servers_cleanup:
        try:
            result = cleanup_func()
            if inspect.isawaitable(result):
                await result
        except Exception as e:
            logger.error(f"Error during cleanup: {e}", extra={
                'scope': 'server',
                'decision': 'error',
                'ctx': {'error': str(e)}
            })

    servers_cleanup.clear()
    
    log_server_stop(logger, reason="graceful_shutdown")


async def main():
    """Запуск HTTP, gRPC и Update серверов одновременно"""
    # Настройка обработчиков сигналов (PR-7)
    setup_signal_handlers()
    
    # Запускаем backpressure manager (PR-7)
    backpressure_manager = get_backpressure_manager()
    await backpressure_manager.start()
    
    # Логируем старт сервера (PR-4)
    log_server_start(logger, port=8080, version=SERVER_VERSION)
    
    # Запускаем периодическое логирование метрик (PR-4)
    metrics_task = asyncio.create_task(periodic_metrics_logging())
    register_cleanup(lambda: cancel_task(metrics_task))

    # HTTP сервер для health checks (порт 8080)
    app = web.Application()
    app.router.add_get('/health', health_handler)
    app.router.add_get('/', root_handler)
    app.router.add_get('/status', status_handler)
    
    # Запускаем HTTP сервер на порту 8080
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()
    register_cleanup(runner.cleanup)
    
    logger.info("HTTP server started", extra={
        'scope': 'server',
        'decision': 'start',
        'ctx': {'port': 8080, 'endpoints': ['/health', '/status']}
    })
    
    # Запускаем сервер обновлений на порту 8081
    update_manager = None
    if UPDATE_SERVER_AVAILABLE:
        logger.info("Starting update server", extra={'scope': 'update', 'decision': 'start'})
        try:
            update_config_dict = asdict(unified_config.get_update_service_config())
            update_config = UpdateConfig.from_dict(update_config_dict)
            update_manager = UpdateManager(update_config)
            await update_manager.initialize(update_config_dict)

            started = await update_manager.start()
            if started:
                register_cleanup(update_manager.cleanup)
                logger.info("Update server started", extra={
                    'scope': 'update',
                    'decision': 'start',
                    'ctx': {'port': update_config.port}
                })
            else:
                log_degradation(logger, "Update server failed to start")
                update_manager = None
        except Exception as e:
            logger.error(f"Update server startup failed: {e}", extra={
                'scope': 'update',
                'decision': 'error',
                'ctx': {'error': str(e)}
            })
            log_degradation(logger, f"Update server unavailable: {e}")
            update_manager = None
    else:
        log_degradation(logger, "Update server module not available")
    
    # Запускаем gRPC сервер на порту 50051
    grpc_port = getattr(unified_config.grpc, 'port', 50051)
    max_workers = getattr(unified_config.grpc, 'max_workers', 100)

    logger.info("Starting gRPC server", extra={
        'scope': 'grpc',
        'decision': 'start',
        'ctx': {'port': grpc_port}
    })

    try:
        # Запускаем gRPC сервер в фоне
        serve_task = asyncio.create_task(serve(port=grpc_port, max_workers=max_workers))
        register_cleanup(lambda: cancel_task(serve_task))

        def _on_serve_task_done(task: asyncio.Task) -> None:
            if shutdown_event.is_set():
                return
            try:
                result = task.result()
                if result is False:
                    log_degradation(logger, "gRPC server failed to start")
            except Exception as exc:
                logger.error(
                    f"Critical gRPC server failure: {exc}",
                    extra={'scope': 'grpc', 'decision': 'error', 'ctx': {'error': str(exc)}}
                )
            finally:
                shutdown_event.set()

        serve_task.add_done_callback(_on_serve_task_done)

        # Ждем сигнала завершения
        await shutdown_event.wait()

    finally:
        # Graceful shutdown
        await graceful_shutdown()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log_server_stop(logger, reason="keyboard_interrupt")
    except Exception as e:
        logger.error(f"Critical error: {e}", extra={
            'scope': 'server',
            'decision': 'error',
            'ctx': {'error': str(e)}
        })
        log_server_stop(logger, reason=f"error: {e}")
        raise
