"""
Core components для gRPC Service Module
"""

from .grpc_service_manager import GrpcServiceManager

# Ленивые импорты для избежания циклических зависимостей
# grpc_server импортирует streaming_pb2_grpc, который может создать цикл

__all__ = ['GrpcServiceManager']

# Ленивые импорты для run_server и NewStreamingServicer
def _lazy_import_grpc_server():
    """Ленивый импорт grpc_server для избежания циклических зависимостей"""
    from .grpc_server import run_server, NewStreamingServicer
    return run_server, NewStreamingServicer

def get_run_server():
    """Получить run_server функцию (ленивый импорт)"""
    run_server, _ = _lazy_import_grpc_server()
    return run_server

def get_new_streaming_servicer():
    """Получить NewStreamingServicer класс (ленивый импорт)"""
    _, NewStreamingServicer = _lazy_import_grpc_server()
    return NewStreamingServicer
