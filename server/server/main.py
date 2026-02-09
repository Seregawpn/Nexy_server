import asyncio
import logging
import os
import signal
import sys
from urllib.parse import quote
from dataclasses import asdict
from aiohttp import web
# Ленивый импорт для избежания циклических зависимостей
# run_server будет импортирован позже, когда он действительно нужен
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

# Загружаем config.env (определяем путь относительно расположения main.py)
from pathlib import Path
MAIN_DIR = Path(__file__).parent
SERVER_ROOT = MAIN_DIR.parent
PRIMARY_CONFIG_ENV = SERVER_ROOT / "config.env"
FALLBACK_CONFIG_ENV = MAIN_DIR / "config.env"
CONFIG_ENV_PATH = PRIMARY_CONFIG_ENV if PRIMARY_CONFIG_ENV.exists() else FALLBACK_CONFIG_ENV
load_dotenv(CONFIG_ENV_PATH)

# Загружаем конфигурацию
unified_config = get_config()
server_metadata = unified_config.get_server_metadata()
grpc_config = unified_config.grpc
http_config = unified_config.http

# Настройка структурированного логирования (PR-4)
log_level = unified_config.logging.level if hasattr(unified_config, 'logging') else 'INFO'
setup_structured_logging(level=log_level)
logger = logging.getLogger(__name__)
if CONFIG_ENV_PATH == FALLBACK_CONFIG_ENV:
    logger.warning(
        "⚠️ Using fallback config.env at %s (primary missing at %s)",
        FALLBACK_CONFIG_ENV,
        PRIMARY_CONFIG_ENV,
    )

# Валидация конфигурации БД перед запуском
def validate_database_config():
    """
    Валидация конфигурации базы данных перед запуском сервера
    
    Проверяет наличие плейсхолдеров и выдает понятные сообщения об ошибках.
    Если конфигурация невалидна, сервер может продолжить работу без БД
    (если модуль database помечен как опциональный).
    """
    try:
        from modules.database.config import DatabaseConfig
        
        db_config_dict = unified_config.get_module_config('database')
        db_config = DatabaseConfig(db_config_dict)
        
        if not db_config.validate():
            logger.warning(
                "⚠️ Конфигурация базы данных невалидна. "
                "Сервер попытается запуститься, но модуль database может быть недоступен. "
                "Проверьте файл config.env и убедитесь, что все параметры БД заполнены корректно.",
                extra={
                    'scope': 'database',
                    'decision': 'degrade',
                    'ctx': {
                        'host': db_config.host,
                        'port': db_config.port,
                        'database': db_config.database,
                        'username': db_config.username,
                        'password_set': bool(db_config.password)
                    }
                }
            )
            return False
        return True
    except Exception as e:
        logger.warning(
            f"⚠️ Не удалось проверить конфигурацию БД: {e}. "
            "Сервер попытается запуститься, но модуль database может быть недоступен.",
            extra={
                'scope': 'database',
                'decision': 'degrade',
                'ctx': {'error': str(e)}
            }
        )
        return False

# Выполняем валидацию конфигурации БД
validate_database_config()

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
    try:
        return web.json_response({
            "status": "OK",
            "latest_version": SERVER_VERSION,
            "latest_build": SERVER_BUILD
        }, headers={
            'Cache-Control': 'public, max-age=30',  # 30 секунд для health (PR-7)
            'Pragma': 'no-cache',
            'Expires': '0'
        })
    except Exception as e:
        logger.error(f"❌ Ошибка health check: {e}", extra={
            'scope': 'server',
            'decision': 'error',
            'ctx': {'error': str(e)}
        })
        return web.json_response({
            "status": "unhealthy",
            "error": str(e)
        }, status=500, headers={
            'Cache-Control': 'no-cache, no-store, must-revalidate'
        })

async def root_handler(request):
    """Корневой endpoint"""
    return web.Response(text="Voice Assistant Server is running!", status=200)

async def portal_handler(request):
    """
    Создание сессии Customer Portal
    Endpoint: POST /api/subscription/portal
    Payload: { "hardware_id": "..." }
    """
    try:
        data = await request.json()
        hardware_id = data.get('hardware_id')
        
        if not hardware_id:
            return web.json_response({'error': 'hardware_id required'}, status=400)
        
        # Lazy import to get singleton
        from modules.subscription import get_subscription_module
        subscription_module = get_subscription_module()
        
        if not subscription_module:
             return web.json_response({'error': 'Subscription module disabled'}, status=503)
             
        result = await subscription_module.create_portal_session(hardware_id)
        
        if not result:
             return web.json_response({'error': 'Could not create portal session (no subscription?)'}, status=404)
             
        return web.json_response(result)
        
    except Exception as e:
        logger.error(f"[F-2025-017] Portal creation error: {e}")
        return web.json_response({'error': str(e)}, status=500)

async def checkout_handler(request):
    """
    Создание сессии Checkout для покупки
    Endpoint: POST /api/subscription/checkout
    Payload: { "hardware_id": "..." }
    """
    try:
        data = await request.json()
        hardware_id = data.get('hardware_id')
        
        if not hardware_id:
            return web.json_response({'error': 'hardware_id required'}, status=400)
        
        from modules.subscription import get_subscription_module
        subscription_module = get_subscription_module()
        
        if not subscription_module:
             return web.json_response({'error': 'Subscription module disabled'}, status=503)
             
        # Определяем base_url для корректного success/cancel редиректа
        forwarded_host = request.headers.get("X-Forwarded-Host")
        forwarded_proto = request.headers.get("X-Forwarded-Proto")
        host = forwarded_host or request.host
        scheme = forwarded_proto or request.scheme
        base_url = f"{scheme}://{host}"

        # Вызываем create_checkout_session
        result = await subscription_module.create_checkout_session(
            hardware_id=hardware_id,
            base_url=base_url
        )
        
        if not result:
             return web.json_response({'error': 'Could not create checkout session'}, status=500)
             
        return web.json_response(result)
        
    except Exception as e:
        logger.error(f"[F-2025-017] Checkout creation error: {e}")
        return web.json_response({'error': str(e)}, status=500)

async def subscription_status_handler(request):
    """
    Получение статуса подписки (для поллинга)
    Endpoint: GET /api/subscription/status?hardware_id=...
    """
    try:
        hardware_id = request.query.get('hardware_id')
        
        if not hardware_id:
            return web.json_response({'error': 'hardware_id required'}, status=400)
        
        from modules.subscription import get_subscription_module
        subscription_module = get_subscription_module()
        
        if not subscription_module:
            return web.json_response({'error': 'Subscription module disabled'}, status=503)
            
        result = await subscription_module.get_subscription_status(hardware_id)
        return web.json_response(result)
        
    except Exception as e:
        logger.error(f"[F-2025-017] Subscription status error: {e}")
        return web.json_response({'error': str(e)}, status=500)

async def payment_success_handler(request):
    """Страница успешной оплаты (redirect target для Stripe Checkout)."""
    deep_link_base = os.getenv("DEEP_LINK_BASE_URL", "nexy://payment/")
    session_id = request.query.get("session_id")
    if session_id:
        deep_link = f"{deep_link_base}success?session_id={quote(session_id)}"
    else:
        deep_link = f"{deep_link_base}success"
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Payment Successful</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; margin: 40px; }}
    .card {{ max-width: 540px; padding: 24px; border: 1px solid #e5e5e5; border-radius: 12px; }}
    .btn {{ display: inline-block; padding: 10px 16px; background: #111; color: #fff; border-radius: 8px; text-decoration: none; }}
  </style>
  <script>
    setTimeout(function() {{
      try {{ window.close(); }} catch (e) {{}}
    }}, 1200);
  </script>
</head>
<body>
  <div class="card">
    <h2>Payment Successful ✅</h2>
    <p>You can close this page. Your subscription is now active.</p>
    <a class="btn" href="{deep_link}">Open App</a>
  </div>
</body>
</html>"""
    return web.Response(text=html, content_type="text/html")

async def payment_cancel_handler(request):
    """Страница отмены оплаты (redirect target для Stripe Checkout)."""
    deep_link = os.getenv("DEEP_LINK_BASE_URL", "nexy://payment/") + "cancel"
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Payment Cancelled</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; margin: 40px; }}
    .card {{ max-width: 540px; padding: 24px; border: 1px solid #e5e5e5; border-radius: 12px; }}
    .btn {{ display: inline-block; padding: 10px 16px; background: #111; color: #fff; border-radius: 8px; text-decoration: none; }}
  </style>
</head>
<body>
  <div class="card">
    <h2>Payment Cancelled</h2>
    <p>If you changed your mind, you can try again.</p>
    <a class="btn" href="{deep_link}">Return to App</a>
  </div>
</body>
</html>"""
    return web.Response(text=html, content_type="text/html")

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


def get_port_process_info(port: int) -> str:
    """Получение информации о процессе, занимающем порт (macOS/Linux)"""
    try:
        import subprocess
        # Для macOS используем lsof
        result = subprocess.run(
            ['lsof', '-ti', f':{port}'],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0 and result.stdout.strip():
            pid = result.stdout.strip()
            # Получаем имя процесса
            proc_info = subprocess.run(
                ['ps', '-p', pid, '-o', 'comm='],
                capture_output=True,
                text=True,
                timeout=2
            )
            proc_name = proc_info.stdout.strip() if proc_info.returncode == 0 else 'unknown'
            return f"PID {pid} ({proc_name})"
    except Exception:
        pass
    return "unknown process"


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
    
    # Останавливаем subscription scheduler (F-2025-017)
    try:
        from modules.subscription import get_subscription_module
        subscription_module = get_subscription_module()
        if subscription_module:
            subscription_module.stop_scheduler()
    except ImportError:
        pass
    except Exception as e:
        logger.debug(f"[F-2025-017] Error stopping subscription scheduler: {e}")
    
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
    app.router.add_get('/payment/success', payment_success_handler)
    app.router.add_get('/payment/cancel', payment_cancel_handler)
    app.router.add_post('/api/subscription/portal', portal_handler)
    app.router.add_post('/api/subscription/checkout', checkout_handler)
    app.router.add_get('/api/subscription/status', subscription_status_handler)
    
    # ⭐ SUBSCRIPTION MODULE: инициализация и webhook routes
    # Feature ID: F-2025-017-stripe-payment
    subscription_module = None
    try:
        from modules.subscription import initialize_subscription_module, get_subscription_module
        
        # Инициализируем subscription модуль (если enabled)
        subscription_module = await initialize_subscription_module()
        
        if subscription_module:
            # Добавляем webhook routes
            from api.webhooks import get_webhook_routes
            for route in get_webhook_routes():
                app.router.add_route(route.method, route.path, route.handler)
            
            logger.info("[F-2025-017] Subscription module initialized, webhook routes added", extra={
                'scope': 'subscription',
                'decision': 'init',
                'ctx': {'routes': ['/webhook/stripe']}
            })
            
            # Запускаем scheduler
            subscription_module.start_scheduler()
        else:
            logger.info("[F-2025-017] Subscription module disabled by config", extra={
                'scope': 'subscription',
                'decision': 'skip'
            })
    except ImportError as e:
        logger.debug(f"[F-2025-017] Subscription module not available: {e}")
    except Exception as e:
        logger.warning(f"[F-2025-017] Failed to initialize subscription module: {e}", extra={
            'scope': 'subscription',
            'decision': 'degrade',
            'ctx': {'error': str(e)}
        })
    

    # Запускаем HTTP сервер на порту 8080
    try:
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
    except OSError as e:
        if e.errno == 48:  # Address already in use
            port_info = get_port_process_info(http_config.port)
            error_msg = (
                f"Не удалось запустить HTTP сервер на {http_config.host}:{http_config.port}. "
                f"Порт занят процессом {port_info}. "
                f"Решение: установите HTTP_PORT=<другой_порт> или остановите процесс: "
                f"lsof -ti :{http_config.port} | xargs kill"
            )
            logger.error(error_msg, extra={
                'scope': 'server',
                'decision': 'error',
                'ctx': {
                    'host': http_config.host,
                    'port': http_config.port,
                    'port_info': port_info,
                    'error': str(e)
                }
            })
        raise
    
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
            # Сохраняем ссылку на update_manager для cleanup функции
            manager_ref = update_manager
            async def stop_update_manager():
                if manager_ref is not None:
                    await manager_ref.stop()
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
    
    shutdown_wait_task: asyncio.Task[object] | None = None
    try:
        # Ленивый импорт run_server для избежания циклических зависимостей
        from modules.grpc_service.core.grpc_server import run_server as serve
        
        # Обертка для правильной типизации: run_server может вернуть False,
        # но create_task ожидает корутину, поэтому оборачиваем в async функцию
        async def run_grpc_server():
            """Обертка для запуска gRPC сервера с обработкой ошибок инициализации"""
            result = await serve(
                host=grpc_config.host,
                port=grpc_config.port,
                max_workers=grpc_config.max_workers
            )
            if result is False:
                logger.error("gRPC server initialization failed", extra={
                    'scope': 'grpc',
                    'decision': 'error',
                    'ctx': {'error': 'initialization_failed'}
                })
                raise RuntimeError("gRPC server initialization failed")
            return result
        
        # Запускаем gRPC сервер в фоне
        serve_task = asyncio.create_task(run_grpc_server())
        shutdown_wait_task = asyncio.create_task(shutdown_event.wait())
        wait_tasks: list[asyncio.Task[object]] = [serve_task, shutdown_wait_task]

        # Регистрируем cleanup функцию
        servers_cleanup.append(lambda: cancel_task(serve_task))

        # Ждем сигнала завершения или ошибки
        await asyncio.wait(wait_tasks, return_when=asyncio.FIRST_COMPLETED)
        
    finally:
        # Graceful shutdown
        await graceful_shutdown()
        
        # Останавливаем периодическое логирование метрик
        metrics_task.cancel()
        try:
            await metrics_task
        except asyncio.CancelledError:
            pass
        
        if shutdown_wait_task is not None and not shutdown_wait_task.done():
            shutdown_wait_task.cancel()
            try:
                await shutdown_wait_task
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
