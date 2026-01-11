"""
gRPC Service Module

Универсальный gRPC сервис для интеграции всех модулей
"""

# GrpcServiceManager можно импортировать сразу, он не зависит от grpc_server
from .core.grpc_service_manager import GrpcServiceManager

# Protobuf файлы импортируем лениво, чтобы избежать проблем с путями импорта
# streaming_pb2_grpc использует абсолютный импорт 'from server.modules.grpc_service',
# который не работает при запуске из директории server/

__all__ = ['GrpcServiceManager']

# Ленивые импорты для protobuf файлов
def _lazy_import_protobuf():
    """Ленивый импорт protobuf файлов для избежания проблем с путями"""
    from . import streaming_pb2
    from . import streaming_pb2_grpc
    return streaming_pb2, streaming_pb2_grpc

def get_streaming_pb2():
    """Получить streaming_pb2 модуль (ленивый импорт)"""
    streaming_pb2, _ = _lazy_import_protobuf()
    return streaming_pb2

def get_streaming_pb2_grpc():
    """Получить streaming_pb2_grpc модуль (ленивый импорт)"""
    _, streaming_pb2_grpc = _lazy_import_protobuf()
    return streaming_pb2_grpc

# Ленивые импорты для run_server и NewStreamingServicer
def _lazy_import_grpc_server():
    """Ленивый импорт grpc_server для избежания циклических зависимостей"""
    from .core.grpc_server import run_server, NewStreamingServicer
    return run_server, NewStreamingServicer

def get_run_server():
    """Получить run_server функцию (ленивый импорт)"""
    run_server, _ = _lazy_import_grpc_server()
    return run_server

def get_new_streaming_servicer():
    """Получить NewStreamingServicer класс (ленивый импорт)"""
    _, NewStreamingServicer = _lazy_import_grpc_server()
    return NewStreamingServicer
