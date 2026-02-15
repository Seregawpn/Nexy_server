"""
Сборщик метрик поверх логов (PR-4)
Собирает p95 latency, error-rate, decision_rate из структурированных логов

Использование: метрики сохраняются в логах как агрегаты, которые можно
извлекать из CI/CloudWatch/Log Analytics без необходимости Prometheus.
"""

import time
import logging
from collections import defaultdict
from typing import Dict, List, Optional
from datetime import datetime
from dataclasses import dataclass, field
from threading import Lock

logger = logging.getLogger(__name__)


@dataclass
class MetricSnapshot:
    """Снапшот метрик"""
    timestamp: datetime = field(default_factory=datetime.utcnow)
    p95_latency: Dict[str, float] = field(default_factory=dict)  # method -> p95_ms
    error_rate: Dict[str, float] = field(default_factory=dict)  # method -> error_rate
    decision_rate: Dict[str, Dict[str, int]] = field(default_factory=dict)  # method -> decision -> count
    total_requests: Dict[str, int] = field(default_factory=dict)  # method -> count
    total_errors: Dict[str, int] = field(default_factory=dict)  # method -> count


class MetricsCollector:
    """
    Сборщик метрик из структурированных логов
    
    Собирает:
    - p95 latency по RPC методам
    - error-rate по методам
    - decision_rate (start/abort/retry/degrade/complete)
    """
    
    def __init__(self, aggregation_interval: int = 60):
        """
        Инициализация сборщика метрик
        
        Args:
            aggregation_interval: Интервал агрегации в секундах (по умолчанию 60)
        """
        self.aggregation_interval = aggregation_interval
        self.lock = Lock()
        
        # Хранилище метрик
        self.latencies: Dict[str, List[float]] = defaultdict(list)  # method -> [latencies_ms]
        self.errors: Dict[str, int] = defaultdict(int)  # method -> error_count
        self.requests: Dict[str, int] = defaultdict(int)  # method -> request_count
        self.decisions: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))  # method -> decision -> count
        
        # Последний снапшот
        self.last_snapshot_time = time.time()

    @staticmethod
    def _normalize_method_name(method: str) -> str:
        """
        Нормализация имени RPC метода до канонического ключа.

        Примеры:
        - "/streaming.StreamingService/StreamAudio" -> "StreamAudio"
        - "StreamAudio" -> "StreamAudio"
        """
        if not method:
            return method
        if "/" in method:
            tail = method.rsplit("/", 1)[-1]
            return tail or method
        return method
    
    def record_request(self, method: str, duration_ms: float, is_error: bool = False) -> None:
        """
        Запись метрики запроса
        
        Args:
            method: Имя метода (StreamAudio, InterruptSession)
            duration_ms: Длительность в миллисекундах
            is_error: Является ли запрос ошибкой
        """
        method = self._normalize_method_name(method)
        with self.lock:
            self.requests[method] += 1
            self.latencies[method].append(duration_ms)
            
            if is_error:
                self.errors[method] += 1
            
            # Ограничиваем размер списка (храним последние 1000 запросов)
            if len(self.latencies[method]) > 1000:
                self.latencies[method] = self.latencies[method][-1000:]
    
    def record_decision(self, method: str, decision: str) -> None:
        """
        Запись решения (decision)
        
        Args:
            method: Имя метода
            decision: Решение (start, abort, retry, degrade, complete, error)
        """
        method = self._normalize_method_name(method)
        with self.lock:
            self.decisions[method][decision] += 1
    
    def _calculate_p95(self, latencies: List[float]) -> float:
        """Вычисление p95 latency"""
        if not latencies:
            return 0.0
        
        sorted_latencies = sorted(latencies)
        index = int(len(sorted_latencies) * 0.95)
        return sorted_latencies[index] if index < len(sorted_latencies) else sorted_latencies[-1]
    
    def _calculate_error_rate(self, errors: int, requests: int) -> float:
        """Вычисление error rate"""
        if requests == 0:
            return 0.0
        return errors / requests
    
    def get_snapshot(self) -> MetricSnapshot:
        """
        Получение снапшота текущих метрик
        
        Returns:
            MetricSnapshot с текущими метриками
        """
        with self.lock:
            snapshot = MetricSnapshot()
            
            # Вычисляем метрики для каждого метода
            for method in self.requests.keys():
                # p95 latency
                if self.latencies[method]:
                    snapshot.p95_latency[method] = self._calculate_p95(self.latencies[method])
                
                # error rate
                snapshot.error_rate[method] = self._calculate_error_rate(
                    self.errors[method],
                    self.requests[method]
                )
                
                # total requests/errors
                snapshot.total_requests[method] = self.requests[method]
                snapshot.total_errors[method] = self.errors[method]
                
                # decision rate
                snapshot.decision_rate[method] = dict(self.decisions[method])
            
            return snapshot
    
    def log_metrics(self) -> None:
        """
        Логирование метрик в структурированном формате
        
        Метрики логируются как агрегаты, которые можно извлекать из CI/CloudWatch/Log Analytics
        """
        snapshot = self.get_snapshot()
        
        # Логируем метрики в структурированном формате
        logger.info(
            "Metrics snapshot",
            extra={
                'scope': 'metrics',
                'decision': 'snapshot',
                'ctx': {
                    'p95_latency': snapshot.p95_latency,
                    'error_rate': snapshot.error_rate,
                    'decision_rate': snapshot.decision_rate,
                    'total_requests': snapshot.total_requests,
                    'total_errors': snapshot.total_errors,
                    'timestamp': snapshot.timestamp.isoformat()
                }
            }
        )
    
    def should_aggregate(self) -> bool:
        """
        Проверка, нужно ли выполнить агрегацию
        
        Returns:
            True если прошло достаточно времени для агрегации
        """
        current_time = time.time()
        if current_time - self.last_snapshot_time >= self.aggregation_interval:
            self.last_snapshot_time = current_time
            return True
        return False
    
    def reset(self) -> None:
        """Сброс метрик (для тестирования)"""
        with self.lock:
            self.latencies.clear()
            self.errors.clear()
            self.requests.clear()
            self.decisions.clear()
            self.last_snapshot_time = time.time()


# Глобальный экземпляр сборщика метрик
_metrics_collector: Optional[MetricsCollector] = None


def get_metrics_collector(aggregation_interval: int = 60) -> MetricsCollector:
    """
    Получение глобального экземпляра сборщика метрик
    
    Args:
        aggregation_interval: Интервал агрегации в секундах
    
    Returns:
        Экземпляр MetricsCollector
    """
    global _metrics_collector
    if _metrics_collector is None:
        _metrics_collector = MetricsCollector(aggregation_interval=aggregation_interval)
    return _metrics_collector


def record_metric(method: str, duration_ms: float, is_error: bool = False) -> None:
    """
    Запись метрики (удобная функция)
    
    Args:
        method: Имя метода
        duration_ms: Длительность в миллисекундах
        is_error: Является ли запрос ошибкой
    """
    collector = get_metrics_collector()
    collector.record_request(method, duration_ms, is_error)
    
    # Проверяем, нужно ли логировать агрегаты
    if collector.should_aggregate():
        collector.log_metrics()


def record_decision_metric(method: str, decision: str) -> None:
    """
    Запись метрики решения (удобная функция)
    
    Args:
        method: Имя метода
        decision: Решение (start, abort, retry, degrade, complete, error)
    """
    collector = get_metrics_collector()
    collector.record_decision(method, decision)
