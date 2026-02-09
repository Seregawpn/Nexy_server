"""
gRPC Interceptor с единой картой ошибок (PR-7)
Обеспечивает единообразную обработку ошибок и логирование
"""

import logging
import time
import asyncio
from typing import Callable, Any, Optional, TYPE_CHECKING
from contextlib import asynccontextmanager

import grpc
from grpc import aio


from utils.logging_formatter import log_rpc_error, log_decision
from utils.metrics_collector import record_metric, record_decision_metric

logger = logging.getLogger(__name__)

# Совместимость с разными версиями grpcio
# HandlerCallDetails может отсутствовать в старых версиях
if TYPE_CHECKING:
    from grpc.aio import HandlerCallDetails  # type: ignore[attr-defined]
else:
    # В runtime используем Any для совместимости
    HandlerCallDetails = Any  # type: ignore


class ErrorCodeMapper:
    """
    Единая карта ошибок для gRPC
    
    Преобразует различные типы ошибок в стандартные коды
    и логирует их структурированно.
    """
    
    # Карта ошибок: тип ошибки → gRPC код
    ERROR_MAP = {
        # Сетевые ошибки
        ConnectionError: grpc.StatusCode.UNAVAILABLE,
        TimeoutError: grpc.StatusCode.DEADLINE_EXCEEDED,
        asyncio.TimeoutError: grpc.StatusCode.DEADLINE_EXCEEDED,
        
        # Валидация
        ValueError: grpc.StatusCode.INVALID_ARGUMENT,
        TypeError: grpc.StatusCode.INVALID_ARGUMENT,
        
        # Ресурсы
        MemoryError: grpc.StatusCode.RESOURCE_EXHAUSTED,
        RuntimeError: grpc.StatusCode.INTERNAL,
        
        # По умолчанию
        Exception: grpc.StatusCode.INTERNAL,
    }
    
    @classmethod
    def map_error(cls, error: Exception) -> grpc.StatusCode:
        """
        Преобразование ошибки в gRPC код
        
        Args:
            error: Исключение
        
        Returns:
            gRPC StatusCode
        """
        error_type = type(error)
        
        # Проверяем точное совпадение типа
        if error_type in cls.ERROR_MAP:
            return cls.ERROR_MAP[error_type]
        
        # Проверяем по базовым классам
        for error_class, status_code in cls.ERROR_MAP.items():
            if isinstance(error, error_class):
                return status_code
        
        # По умолчанию
        return grpc.StatusCode.INTERNAL
    
    @classmethod
    def is_transient_error(cls, error_code: grpc.StatusCode) -> bool:
        """
        Проверка, является ли ошибка временной (transient)
        
        Args:
            error_code: gRPC код ошибки
        
        Returns:
            True если ошибка временная, False иначе
        """
        transient_codes = [
            grpc.StatusCode.UNAVAILABLE,
            grpc.StatusCode.DEADLINE_EXCEEDED,
            grpc.StatusCode.RESOURCE_EXHAUSTED,
            grpc.StatusCode.ABORTED,
        ]
        return error_code in transient_codes


class LoggingInterceptor(aio.ServerInterceptor):
    """
    gRPC Interceptor для логирования и обработки ошибок
    
    Обеспечивает:
    - Единообразную обработку ошибок
    - Структурированное логирование
    - Метрики
    """
    
    def __init__(self):
        self.error_mapper = ErrorCodeMapper()
    
    async def intercept_service(
        self,
        continuation: Callable,
        handler_call_details: "HandlerCallDetails"
    ) -> Any:
        """
        Перехват вызова сервиса
        
        Args:
            continuation: Продолжение обработки
            handler_call_details: Детали вызова
        
        Returns:
            Обработчик с логированием
        """
        method_name = handler_call_details.method

        # Получаем оригинальный handler
        handler = await continuation(handler_call_details)
        if handler is None:
            return None

        # Извлекаем callables и сериализаторы из оригинального handler
        # RpcMethodHandler - это namedtuple, поэтому извлекаем напрямую
        unary_unary = handler.unary_unary
        unary_stream = handler.unary_stream
        stream_unary = handler.stream_unary
        stream_stream = handler.stream_stream
        
        # Обёртываем callables в логирующие обёртки
        wrapped_unary_unary = None
        wrapped_unary_stream = None
        wrapped_stream_unary = None
        wrapped_stream_stream = None

        if unary_unary:
            wrapped_unary_unary = self._wrap_unary(unary_unary, method_name)
        if unary_stream:
            wrapped_unary_stream = self._wrap_response_streaming(unary_stream, method_name)
        if stream_unary:
            wrapped_stream_unary = self._wrap_request_streaming(stream_unary, method_name)
        if stream_stream:
            wrapped_stream_stream = self._wrap_bidi_streaming(stream_stream, method_name)

        # Создаём новый handler через _replace() метод namedtuple
        new_handler = handler._replace(
            unary_unary=wrapped_unary_unary,
            unary_stream=wrapped_unary_stream,
            stream_unary=wrapped_stream_unary,
            stream_stream=wrapped_stream_stream
        )

        return new_handler
    
    def _wrap_unary(self, handler, method_name: str):
        """Обёртка для unary RPC"""
        async def wrapper(request, context):
            start_time = time.time()
            try:
                log_decision(logger, decision="start", method=method_name, ctx={"type": "unary"})
                
                response = await handler(request, context)
                
                dur_ms = (time.time() - start_time) * 1000
                log_decision(logger, decision="complete", method=method_name, dur_ms=dur_ms)
                record_metric(method_name, dur_ms, is_error=False)
                record_decision_metric(method_name, "complete")
                
                return response
            except Exception as e:
                dur_ms = (time.time() - start_time) * 1000
                error_code = self.error_mapper.map_error(e)
                is_transient = self.error_mapper.is_transient_error(error_code)
                
                # Структурированное логирование ошибки
                log_rpc_error(
                    logger,
                    method=method_name,
                    error_code=error_code.name,
                    error_message=str(e),
                    dur_ms=dur_ms,
                    ctx={
                        "error_classified": "transient" if is_transient else "permanent",
                        "error_type": type(e).__name__
                    }
                )
                record_metric(method_name, dur_ms, is_error=True)
                record_decision_metric(method_name, "error")
                
                # Преобразуем в gRPC ошибку
                context.set_code(error_code)
                context.set_details(str(e))
                raise grpc.RpcError()
        
        return wrapper
    
    def _wrap_response_streaming(self, handler, method_name: str):
        """Обёртка для response streaming RPC"""
        async def wrapper(request, context):
            start_time = time.time()
            try:
                log_decision(logger, decision="start", method=method_name, ctx={"type": "response_streaming"})
                
                async for response in handler(request, context):
                    yield response
                
                dur_ms = (time.time() - start_time) * 1000
                log_decision(logger, decision="complete", method=method_name, dur_ms=dur_ms)
                record_metric(method_name, dur_ms, is_error=False)
                record_decision_metric(method_name, "complete")
                
            except Exception as e:
                dur_ms = (time.time() - start_time) * 1000
                error_code = self.error_mapper.map_error(e)
                is_transient = self.error_mapper.is_transient_error(error_code)
                
                # Структурированное логирование ошибки
                log_rpc_error(
                    logger,
                    method=method_name,
                    error_code=error_code.name,
                    error_message=str(e),
                    dur_ms=dur_ms,
                    ctx={
                        "error_classified": "transient" if is_transient else "permanent",
                        "error_type": type(e).__name__
                    }
                )
                record_metric(method_name, dur_ms, is_error=True)
                record_decision_metric(method_name, "error")
                
                # Преобразуем в gRPC ошибку
                context.set_code(error_code)
                context.set_details(str(e))
                raise grpc.RpcError()
        
        return wrapper
    
    def _wrap_request_streaming(self, handler, method_name: str):
        """Обёртка для request streaming RPC"""
        async def wrapper(request_iterator, context):
            start_time = time.time()
            try:
                log_decision(logger, decision="start", method=method_name, ctx={"type": "request_streaming"})
                
                response = await handler(request_iterator, context)
                
                dur_ms = (time.time() - start_time) * 1000
                log_decision(logger, decision="complete", method=method_name, dur_ms=dur_ms)
                record_metric(method_name, dur_ms, is_error=False)
                record_decision_metric(method_name, "complete")
                
                return response
            except Exception as e:
                dur_ms = (time.time() - start_time) * 1000
                error_code = self.error_mapper.map_error(e)
                is_transient = self.error_mapper.is_transient_error(error_code)
                
                log_rpc_error(
                    logger,
                    method=method_name,
                    error_code=error_code.name,
                    error_message=str(e),
                    dur_ms=dur_ms,
                    ctx={
                        "error_classified": "transient" if is_transient else "permanent",
                        "error_type": type(e).__name__
                    }
                )
                record_metric(method_name, dur_ms, is_error=True)
                record_decision_metric(method_name, "error")
                
                context.set_code(error_code)
                context.set_details(str(e))
                raise grpc.RpcError()
        
        return wrapper
    
    def _wrap_bidi_streaming(self, handler, method_name: str):
        """Обёртка для bidirectional streaming RPC"""
        async def wrapper(request_iterator, context):
            start_time = time.time()
            try:
                log_decision(logger, decision="start", method=method_name, ctx={"type": "bidi_streaming"})
                
                async for response in handler(request_iterator, context):
                    yield response
                
                dur_ms = (time.time() - start_time) * 1000
                log_decision(logger, decision="complete", method=method_name, dur_ms=dur_ms)
                record_metric(method_name, dur_ms, is_error=False)
                record_decision_metric(method_name, "complete")
                
            except Exception as e:
                dur_ms = (time.time() - start_time) * 1000
                error_code = self.error_mapper.map_error(e)
                is_transient = self.error_mapper.is_transient_error(error_code)
                
                log_rpc_error(
                    logger,
                    method=method_name,
                    error_code=error_code.name,
                    error_message=str(e),
                    dur_ms=dur_ms,
                    ctx={
                        "error_classified": "transient" if is_transient else "permanent",
                        "error_type": type(e).__name__
                    }
                )
                record_metric(method_name, dur_ms, is_error=True)
                record_decision_metric(method_name, "error")
                
                context.set_code(error_code)
                context.set_details(str(e))
                raise grpc.RpcError()
        
        return wrapper


# Глобальный экземпляр интерцептора
_global_interceptor: Optional[LoggingInterceptor] = None


def get_interceptor() -> LoggingInterceptor:
    """
    Получение глобального экземпляра интерцептора
    
    Returns:
        Экземпляр LoggingInterceptor
    """
    global _global_interceptor
    if _global_interceptor is None:
        _global_interceptor = LoggingInterceptor()
    return _global_interceptor
