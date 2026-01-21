#!/usr/bin/env python3
"""
Server main entry point with automatic venv redirection

This script automatically redirects to .venv/bin/python if it exists,
allowing you to run: python3 server/main.py
"""

# ⚠️ КРИТИЧНО: Автоматическое перенаправление должно быть ПЕРВЫМ, до всех импортов!
import sys
import os

# ⚠️ Автоматическое перенаправление на виртуальное окружение
def auto_redirect_to_venv():
    """
    Автоматически перенаправляет запуск на виртуальное окружение, если оно существует.
    Это позволяет запускать сервер обычной командой python server/main.py
    """
    python_path = sys.executable
    venv_indicators = ['.venv', 'venv', 'env']
    is_venv = any(indicator in python_path for indicator in venv_indicators)
    
    # Если уже в venv - ничего не делаем
    if is_venv:
        return
    
    # Определяем путь к main.py
    # __file__ может быть относительным, поэтому используем abspath
    main_py_path = os.path.abspath(__file__)
    # server_dir - это директория server(Messages), которая содержит .venv
    server_dir = os.path.dirname(os.path.dirname(main_py_path))  # server(Messages)
    venv_python = os.path.join(server_dir, '.venv', 'bin', 'python')
    
    # Проверяем, существует ли venv
    if os.path.exists(venv_python) and os.path.isfile(venv_python):
        # Выводим сообщение в stderr, чтобы оно было видно даже при перенаправлении
        sys.stderr.write("\n" + "="*80 + "\n")
        sys.stderr.write("🔄 Автоматическое перенаправление на виртуальное окружение...\n")
        sys.stderr.write("="*80 + "\n")
        sys.stderr.write(f"Текущий Python: {python_path}\n")
        sys.stderr.write(f"Перезапуск через: {venv_python}\n")
        sys.stderr.write("="*80 + "\n\n")
        sys.stderr.flush()
        
        # Перезапускаем через venv Python
        # Важно: execv заменяет текущий процесс, поэтому все импорты будут выполнены заново
        try:
            os.execv(venv_python, [venv_python] + sys.argv)
        except OSError as e:
            sys.stderr.write(f"❌ Ошибка при перезапуске через venv: {e}\n")
            sys.stderr.write("Продолжаем с текущим Python (может работать в stub режиме)\n")
            sys.stderr.flush()
            return
        # execv не возвращается, если успешно
    else:
        # Venv не найден - показываем предупреждение
        print("\n" + "="*80)
        print("⚠️  ВНИМАНИЕ: Сервер запущен не из виртуального окружения!")
        print("="*80)
        print(f"Python path: {python_path}")
        print(f"Ожидаемый venv: {venv_python}")
        print("\n❌ Виртуальное окружение .venv не найдено!")
        print("\n✅ СОЗДАЙТЕ ВЕНВ:")
        print("   cd server(Messages)")
        print("   python3 -m venv .venv")
        print("   .venv/bin/pip install browser-use playwright")
        print("   .venv/bin/playwright install chromium")
        print("\n   ИЛИ запустите через скрипт:")
        print("   ./start_server.sh")
        print("\n" + "="*80 + "\n")
        
        # Проверяем наличие browser-use в текущем окружении
        try:
            from browser_use import Agent
            print("✅ browser-use доступен в текущем окружении")
        except ImportError:
            print("❌ browser-use НЕ доступен в текущем окружении")
            print("   Сервер будет работать в stub режиме (браузер не будет работать)")
            print("\n" + "="*80 + "\n")

# Выполняем автоматическое перенаправление ПЕРЕД всеми импортами
auto_redirect_to_venv()

# Теперь импортируем остальные модули (после перенаправления)
import asyncio
import logging
import signal
from dataclasses import asdict
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
grpc_config = unified_config.grpc
http_config = unified_config.http

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
shutdown_event = asyncio.Event()
servers_cleanup = []


async def cancel_task(task: asyncio.Task):
    """Безопасная отмена асинхронной задачи."""
    if task.done():
        return
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass


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
            await cleanup_func()
        except Exception as e:
            logger.error(f"Error during cleanup: {e}", extra={
                'scope': 'server',
                'decision': 'error',
                'ctx': {'error': str(e)}
            })
    
    log_server_stop(logger, reason="graceful_shutdown")


async def main():
    """Запуск HTTP, gRPC и Update серверов одновременно"""
    # Настройка обработчиков сигналов (PR-7)
    setup_signal_handlers()
    
    # Запускаем backpressure manager (PR-7)
    backpressure_manager = get_backpressure_manager()
    await backpressure_manager.start()
    
    # Логируем старт сервера (PR-4)
    log_server_start(logger, port=http_config.port, version=SERVER_VERSION)
    
    # Запускаем периодическое логирование метрик (PR-4)
    metrics_task = asyncio.create_task(periodic_metrics_logging())
    
    # HTTP сервер для health checks (порт 8080)
    app = web.Application()
    app.router.add_get('/health', health_handler)
    app.router.add_get('/', root_handler)
    app.router.add_get('/status', status_handler)
    
    # Запускаем HTTP сервер на порту 8080
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, http_config.host, http_config.port)
    await site.start()
    servers_cleanup.append(runner.cleanup)
    
    logger.info("HTTP server started", extra={
        'scope': 'server',
        'decision': 'start',
        'ctx': {
            'host': http_config.host,
            'port': http_config.port,
            'endpoints': ['/health', '/status']
        }
    })
    
    # Запускаем сервер обновлений на порту 8081
    update_manager = None
    if UPDATE_SERVER_AVAILABLE:
        logger.info("Starting update server", extra={'scope': 'update', 'decision': 'start'})
        try:
            config = UpdateConfig.from_dict(asdict(unified_config.get_update_service_config()))
            update_manager = UpdateManager(config)
            await update_manager.initialize()
            await update_manager.start()
            logger.info("Update server started", extra={
                'scope': 'update',
                'decision': 'start',
                'ctx': {'host': update_manager.config.host, 'port': update_manager.config.port}
            })
            async def stop_update_manager():
                await update_manager.stop()
            servers_cleanup.append(stop_update_manager)
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
    logger.info("Starting gRPC server", extra={
        'scope': 'grpc',
        'decision': 'start',
        'ctx': {'host': grpc_config.host, 'port': grpc_config.port}
    })
    
    try:
        # Запускаем gRPC сервер в фоне
        serve_task = asyncio.create_task(serve(
            host=grpc_config.host,
            port=grpc_config.port,
            max_workers=grpc_config.max_workers
        ))
        
        # Регистрируем cleanup функцию
        servers_cleanup.append(lambda: cancel_task(metrics_task))
        servers_cleanup.append(lambda: cancel_task(serve_task))
        
        # Ждем сигнала завершения или ошибки
        await asyncio.wait(
            [serve_task, asyncio.create_task(shutdown_event.wait())],
            return_when=asyncio.FIRST_COMPLETED
        )
        
    finally:
        # Graceful shutdown
        await graceful_shutdown()
        
        # Останавливаем периодическое логирование метрик
        metrics_task.cancel()
        try:
            await metrics_task
        except asyncio.CancelledError:
            pass

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
