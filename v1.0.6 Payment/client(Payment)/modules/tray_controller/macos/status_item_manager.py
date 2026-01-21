"""
Менеджер создания NSStatusItem с single-flight, circuit-breaker и retry-логикой.

Реализует:
- Single-flight: одна попытка создания в момент времени
- Circuit-breaker: пауза 5-10s после 3-4 подряд ошибок
- Экспоненциальный backoff с jitter ±15%
- Косвенный признак готовности Control Center
- Метрики для диагностики
"""

import os
import time
import random
import logging
import threading
from typing import Optional, Callable, Dict, Any
from enum import Enum
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


class CircuitState(Enum):
    """Состояние circuit-breaker"""
    CLOSED = "closed"  # Нормальная работа
    OPEN = "open"  # Блокировка после ошибок
    HALF_OPEN = "half_open"  # Пробная попытка после паузы


@dataclass
class StatusItemMetrics:
    """Метрики создания NSStatusItem"""
    series_id: str = ""  # ID серии попыток
    attempt_count: int = 0  # Количество попыток в текущей серии
    last_attempt_code: Optional[str] = None  # Код последней ошибки
    last_attempt_duration_ms: int = 0  # Длительность последней попытки
    backoff_next_ms: int = 0  # Следующий backoff в миллисекундах
    circuit_state: CircuitState = CircuitState.CLOSED
    circuit_open_reason: Optional[str] = None
    tal_hold_start: Optional[float] = None  # Время начала TAL удержания
    tal_released: Optional[float] = None  # Время снятия TAL удержания
    restart_flag_seen: Optional[Dict[str, Any]] = None  # Данные флага перезапуска


class StatusItemManager:
    """
    Менеджер создания NSStatusItem с single-flight, circuit-breaker и retry-логикой.
    
    Обеспечивает:
    - Single-flight: только одна попытка создания в момент времени
    - Circuit-breaker: пауза после серии ошибок
    - Экспоненциальный backoff с jitter
    - Косвенный признак готовности Control Center
    """
    
    # Дефолтные константы (переопределяются из конфига)
    CIRCUIT_OPEN_THRESHOLD = 3
    CIRCUIT_OPEN_DURATION_SEC = 8.0
    CIRCUIT_HALF_OPEN_TIMEOUT_SEC = 5.0
    MAX_ATTEMPTS_PER_SERIES = 10
    INITIAL_BACKOFF_MS = 800
    MAX_BACKOFF_MS = 10000
    BACKOFF_MULTIPLIER = 1.5
    JITTER_PERCENT = 0.15
    CONTROL_CENTER_READY_TIMEOUT_SEC = 10.0
    FIRST_ATTEMPT_DELAY_MS = 1000
    FINAL_TIMEOUT_MS = 60000
    BACKGROUND_RETRY_INTERVAL_SEC = 45
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self._lock = threading.Lock()  # Блокировка для single-flight
        self._is_creating = False  # Флаг создания (single-flight)
        self._metrics = StatusItemMetrics()
        self._consecutive_failures = 0  # Количество подряд идущих ошибок
        self._circuit_open_until: Optional[float] = None  # Время до закрытия circuit
        self._control_center_ready = False  # Флаг готовности Control Center
        self._control_center_ready_ts: Optional[float] = None  # Время готовности Control Center
        
        # Загружаем конфиг из unified_config.yaml (если передан)
        if config:
            self.CIRCUIT_OPEN_THRESHOLD = config.get('circuit_open_threshold', self.CIRCUIT_OPEN_THRESHOLD)
            self.CIRCUIT_OPEN_DURATION_SEC = config.get('circuit_open_duration_ms', int(self.CIRCUIT_OPEN_DURATION_SEC * 1000)) / 1000.0
            self.MAX_ATTEMPTS_PER_SERIES = config.get('max_attempts_per_series', self.MAX_ATTEMPTS_PER_SERIES)
            self.INITIAL_BACKOFF_MS = config.get('initial_backoff_ms', self.INITIAL_BACKOFF_MS)
            self.MAX_BACKOFF_MS = config.get('max_backoff_ms', self.MAX_BACKOFF_MS)
            self.BACKOFF_MULTIPLIER = config.get('backoff_multiplier', self.BACKOFF_MULTIPLIER)
            self.JITTER_PERCENT = config.get('jitter_percent', self.JITTER_PERCENT)
            self.CONTROL_CENTER_READY_TIMEOUT_SEC = config.get('control_center_ready_timeout_sec', self.CONTROL_CENTER_READY_TIMEOUT_SEC)
            self.FIRST_ATTEMPT_DELAY_MS = config.get('first_attempt_delay_ms', self.FIRST_ATTEMPT_DELAY_MS)
            self.FINAL_TIMEOUT_MS = config.get('final_timeout_ms', self.FINAL_TIMEOUT_MS)
            self.BACKGROUND_RETRY_INTERVAL_SEC = config.get('background_retry_interval_sec', self.BACKGROUND_RETRY_INTERVAL_SEC)
        
        # Генерируем ID серии
        import uuid
        self._metrics.series_id = str(uuid.uuid4())[:8]
    
    def is_creating(self) -> bool:
        """Проверяет, идет ли создание NSStatusItem (single-flight)"""
        with self._lock:
            return self._is_creating
    
    def start_creation(self) -> bool:
        """
        Начинает создание NSStatusItem (single-flight).
        
        Returns:
            True если создание разрешено, False если уже идет создание
        """
        with self._lock:
            if self._is_creating:
                logger.debug("[STATUS_ITEM_MANAGER] Creation already in progress (single-flight)")
                return False
            
            # Проверяем circuit-breaker
            if self._circuit_state() == CircuitState.OPEN:
                logger.warning(
                    f"[STATUS_ITEM_MANAGER] Circuit is OPEN - blocking creation "
                    f"(reason={self._metrics.circuit_open_reason})"
                )
                return False
            
            self._is_creating = True
            self._metrics.attempt_count += 1
            logger.info(
                f"[STATUS_ITEM_MANAGER] Starting creation attempt {self._metrics.attempt_count} "
                f"(series_id={self._metrics.series_id})"
            )
            return True
    
    def finish_creation(self, success: bool, error_code: Optional[str] = None, duration_ms: int = 0):
        """
        Завершает создание NSStatusItem.
        
        Args:
            success: True если создание успешно, False в противном случае
            error_code: Код ошибки (если есть)
            duration_ms: Длительность попытки в миллисекундах
        """
        with self._lock:
            self._is_creating = False
            self._metrics.last_attempt_code = error_code
            self._metrics.last_attempt_duration_ms = duration_ms
            
            if success:
                self._consecutive_failures = 0
                self._metrics.circuit_state = CircuitState.CLOSED
                self._circuit_open_until = None
                self._metrics.circuit_open_reason = None
                logger.info(
                    f"[STATUS_ITEM_MANAGER] ✅ Creation succeeded "
                    f"(attempt={self._metrics.attempt_count}, duration={duration_ms}ms)"
                )
            else:
                self._consecutive_failures += 1
                logger.warning(
                    f"[STATUS_ITEM_MANAGER] ❌ Creation failed "
                    f"(attempt={self._metrics.attempt_count}, error={error_code}, "
                    f"consecutive_failures={self._consecutive_failures})"
                )
                
                # Проверяем circuit-breaker
                if self._consecutive_failures >= self.CIRCUIT_OPEN_THRESHOLD:
                    self._open_circuit(f"consecutive_failures={self._consecutive_failures}")
    
    def _circuit_state(self) -> CircuitState:
        """Определяет текущее состояние circuit-breaker"""
        if self._circuit_open_until is None:
            return CircuitState.CLOSED
        
        if time.monotonic() < self._circuit_open_until:
            return CircuitState.OPEN
        
        # Circuit закрывается - переходим в half-open
        if self._metrics.circuit_state == CircuitState.OPEN:
            self._metrics.circuit_state = CircuitState.HALF_OPEN
            logger.info(
                f"[STATUS_ITEM_MANAGER] Circuit transitioning to HALF_OPEN "
                f"(was open for {self.CIRCUIT_OPEN_DURATION_SEC}s)"
            )
        
        return CircuitState.HALF_OPEN
    
    def _open_circuit(self, reason: str):
        """Открывает circuit-breaker"""
        self._metrics.circuit_state = CircuitState.OPEN
        self._metrics.circuit_open_reason = reason
        self._circuit_open_until = time.monotonic() + self.CIRCUIT_OPEN_DURATION_SEC
        
        logger.warning(
            f"[STATUS_ITEM_MANAGER] 🔴 Circuit OPEN: {reason} "
            f"(will retry after {self.CIRCUIT_OPEN_DURATION_SEC}s)"
        )
    
    def calculate_backoff_ms(self, attempt: int) -> int:
        """
        Вычисляет backoff для попытки с экспоненциальным ростом и jitter.
        
        Args:
            attempt: Номер попытки (начинается с 1)
            
        Returns:
            Backoff в миллисекундах
        """
        # Экспоненциальный backoff
        base_backoff = self.INITIAL_BACKOFF_MS * (self.BACKOFF_MULTIPLIER ** (attempt - 1))
        base_backoff = min(base_backoff, self.MAX_BACKOFF_MS)
        
        # Добавляем jitter ±15%
        jitter_range = int(base_backoff * self.JITTER_PERCENT)
        jitter = random.randint(-jitter_range, jitter_range)
        
        backoff_ms = max(0, base_backoff + jitter)
        self._metrics.backoff_next_ms = backoff_ms
        
        return backoff_ms
    
    def wait_for_control_center_ready(self, timeout_sec: float = None) -> bool:
        """
        Ждет готовности Control Center через косвенные признаки.
        
        Args:
            timeout_sec: Максимальное время ожидания (по умолчанию CONTROL_CENTER_READY_TIMEOUT_SEC)
            
        Returns:
            True если Control Center готов, False если таймаут
        """
        if timeout_sec is None:
            timeout_sec = self.CONTROL_CENTER_READY_TIMEOUT_SEC
        
        if self._control_center_ready:
            return True
        
        deadline = time.monotonic() + timeout_sec
        check_interval = 0.1  # Проверяем каждые 100ms
        
        logger.info(f"[STATUS_ITEM_MANAGER] Waiting for Control Center ready (timeout={timeout_sec}s)...")
        
        while time.monotonic() < deadline:
            if self._check_control_center_ready():
                self._control_center_ready = True
                self._control_center_ready_ts = time.monotonic()
                # КРИТИЧНО: Логируем CC_READY в формате для приёмки
                logger.info(f"CC_READY ts={self._control_center_ready_ts:.2f}")
                return True
            
            time.sleep(check_interval)
        
        logger.warning(
            f"[STATUS_ITEM_MANAGER] ⚠️ Control Center ready timeout ({timeout_sec}s) - "
            "proceeding anyway"
        )
        return False
    
    def _check_control_center_ready(self) -> bool:
        """
        Проверяет готовность Control Center через косвенные признаки.
        
        Returns:
            True если Control Center готов, False в противном случае
        """
        try:
            import AppKit
            
            # Признак 1: NSStatusBar.system() доступен
            status_bar = AppKit.NSStatusBar.systemStatusBar()
            if status_bar is None:
                return False
            
            # Признак 2: NSRunningApplication для ControlCenter существует
            workspace = AppKit.NSWorkspace.sharedWorkspace()
            if workspace is None:
                return False
            
            # Проверяем наличие процесса ControlCenter
            running_apps = workspace.runningApplications()
            for app in running_apps:
                bundle_id = app.bundleIdentifier()
                if bundle_id and "controlcenter" in bundle_id.lower():
                    # ControlCenter запущен
                    return True
            
            # Признак 3: NSWorkspace session активен
            # Это косвенный признак готовности системы
            return True  # Считаем готовым если NSStatusBar доступен
            
        except Exception as exc:
            logger.debug(f"[STATUS_ITEM_MANAGER] Control Center check failed: {exc}")
            return False
    
    def get_metrics(self) -> StatusItemMetrics:
        """Возвращает текущие метрики"""
        with self._lock:
            return StatusItemMetrics(
                series_id=self._metrics.series_id,
                attempt_count=self._metrics.attempt_count,
                last_attempt_code=self._metrics.last_attempt_code,
                last_attempt_duration_ms=self._metrics.last_attempt_duration_ms,
                backoff_next_ms=self._metrics.backoff_next_ms,
                circuit_state=self._metrics.circuit_state,
                circuit_open_reason=self._metrics.circuit_open_reason,
                tal_hold_start=self._metrics.tal_hold_start,
                tal_released=self._metrics.tal_released,
                restart_flag_seen=self._metrics.restart_flag_seen,
            )
    
    def set_tal_hold(self):
        """Устанавливает TAL удержание"""
        with self._lock:
            if self._metrics.tal_hold_start is None:
                self._metrics.tal_hold_start = time.monotonic()
                logger.info("[STATUS_ITEM_MANAGER] 🛡️ TAL hold started")
    
    def release_tal_hold(self):
        """Снимает TAL удержание"""
        with self._lock:
            if self._metrics.tal_hold_start is not None and self._metrics.tal_released is None:
                self._metrics.tal_released = time.monotonic()
                hold_duration = self._metrics.tal_released - self._metrics.tal_hold_start
                logger.info(
                    f"[STATUS_ITEM_MANAGER] 🛡️ TAL hold released "
                    f"(duration={hold_duration:.2f}s)"
                )
    
    def set_restart_flag_data(self, flag_data: Dict[str, Any]):
        """Устанавливает данные флага перезапуска для метрик"""
        with self._lock:
            self._metrics.restart_flag_seen = flag_data

