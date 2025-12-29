# Полный план реализации аудиосистемы на AVFoundation

**Дата**: 2025-01-XX  
**Версия**: 1.0  
**Статус**: Готов к реализации  
**Готовность**: 100%

---

## 📋 Обзор плана

Этот документ содержит **полный, детальный план реализации** новой аудиосистемы на AVFoundation с учетом всех обсуждений, требований и схем.

**Структура плана**:
- 9 этапов реализации
- 42 дня работы
- 18 новых файлов
- 9 изменений существующих файлов
- Полное покрытие тестами

---

## 🎯 Этап 1: Базовые компоненты (Неделя 1)

### День 1-2: Типы данных и контракты

#### Задача 1.1: Создать `contracts.py`

**Файл**: `modules/voice_recognition/core/avfoundation/contracts.py`

**Содержимое**:
```python
"""
Audio system contracts and types.

Defines DeviceSignature, RouteSnapshot, MappingResult, and related enums.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Confidence(Enum):
    """Confidence level for device mapping."""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    NONE = "none"


class DeviceTransport(Enum):
    """Device transport type."""
    BLUETOOTH = "bluetooth"
    USB = "usb"
    BUILT_IN = "built_in"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class DeviceSignature:
    """Normalized device signature for comparison."""
    normalized_name: str
    transport: DeviceTransport
    channels: int
    manufacturer_hint: Optional[str] = None
    
    def __str__(self) -> str:
        return f"{self.normalized_name} ({self.transport.value}, {self.channels}ch)"


@dataclass(frozen=True)
class RouteSnapshot:
    """Snapshot of current audio routing state."""
    system_default_input: Optional[DeviceSignature]
    desired_input: Optional[DeviceSignature]
    active_input: Optional[DeviceSignature]
    active_output: Optional[DeviceSignature]
    
    def input_changed(self) -> bool:
        """Check if input route changed."""
        if self.desired_input is None:
            return False
        if self.active_input is None:
            return True
        return self.desired_input != self.active_input
    
    def output_changed(self) -> bool:
        """Check if output route changed."""
        # Output всегда следует system default, поэтому проверяем только active
        return self.active_output is None


@dataclass(frozen=True)
class MappingResult:
    """Result of AVFoundation → PortAudio mapping."""
    device_index: Optional[int]
    confidence: Confidence
    reason: str
    
    def is_usable(self) -> bool:
        """Check if mapping result is usable."""
        return self.confidence in (Confidence.HIGH, Confidence.MEDIUM) and self.device_index is not None
```

**Критерии готовности**:
- [ ] Файл создан
- [ ] Все типы определены
- [ ] Методы `__str__`, `input_changed`, `output_changed`, `is_usable` реализованы
- [ ] Линтер проходит без ошибок

**Тесты**: `tests/test_avfoundation_contracts.py`
- [ ] Тест создания DeviceSignature
- [ ] Тест создания RouteSnapshot
- [ ] Тест создания MappingResult
- [ ] Тест input_changed()
- [ ] Тест output_changed()
- [ ] Тест is_usable()
- [ ] Покрытие ≥80%

---

### День 3-4: Маппинг устройств

#### Задача 1.2: Создать `mapping.py`

**Файл**: `modules/voice_recognition/core/avfoundation/mapping.py`

**Содержимое** (структура):
```python
"""
Device mapping: AVFoundation → PortAudio.

Normalizes device names, calculates confidence, caches mappings.
"""

import logging
import re
import time
from typing import Dict, List, Optional, Tuple
import sounddevice as sd

from .contracts import DeviceSignature, DeviceTransport, Confidence, MappingResult

logger = logging.getLogger(__name__)

# Bluetooth aliases for normalization
BT_ALIASES = {
    "AirPods": ["AirPods", "AirPods (Hands-Free)", "AirPods HFP", "AirPods Pro"],
    "Beats": ["Beats", "Beats Studio", "Beats Solo"],
    # Добавить другие по мере необходимости
}

# Суффиксы для удаления при нормализации
BT_SUFFIXES = [
    " (Hands-Free)",
    " HFP",
    " Hands-Free",
    " Bluetooth",
]


class DeviceMapper:
    """Maps AVFoundation devices to PortAudio device_index."""
    
    def __init__(self, cache_ttl_sec: int = 86400):
        """
        Initialize DeviceMapper.
        
        Args:
            cache_ttl_sec: TTL для кэша маппингов (по умолчанию 24 часа)
        """
        self._cache: Dict[str, MappingResult] = {}
        self._cache_timestamps: Dict[str, float] = {}
        self._cache_ttl_sec = cache_ttl_sec
    
    def normalize_device_name(self, name: str) -> str:
        """
        Normalize device name (remove Bluetooth suffixes, etc.).
        
        Args:
            name: Исходное имя устройства
            
        Returns:
            Нормализованное имя
        """
        normalized = name.strip()
        
        # Удаляем Bluetooth суффиксы
        for suffix in BT_SUFFIXES:
            if normalized.endswith(suffix):
                normalized = normalized[:-len(suffix)]
                break
        
        # Применяем aliases
        for canonical, aliases in BT_ALIASES.items():
            if normalized in aliases:
                normalized = canonical
                break
        
        return normalized
    
    def detect_transport(self, name: str, avf_info: dict) -> DeviceTransport:
        """
        Detect device transport type.
        
        Args:
            name: Имя устройства
            avf_info: Информация от AVFoundation
            
        Returns:
            DeviceTransport
        """
        name_lower = name.lower()
        
        if "bluetooth" in name_lower or "airpods" in name_lower or "beats" in name_lower:
            return DeviceTransport.BLUETOOTH
        elif "usb" in name_lower:
            return DeviceTransport.USB
        elif "built-in" in name_lower or "internal" in name_lower or "macbook" in name_lower:
            return DeviceTransport.BUILT_IN
        else:
            return DeviceTransport.UNKNOWN
    
    def build_signature(self, avf_device_info: dict) -> DeviceSignature:
        """
        Build DeviceSignature from AVFoundation device info.
        
        Args:
            avf_device_info: Словарь с информацией об устройстве от AVFoundation
                - name: str
                - channels: int (опционально)
                - manufacturer: str (опционально)
                
        Returns:
            DeviceSignature
        """
        name = avf_device_info.get("name", "Unknown")
        normalized_name = self.normalize_device_name(name)
        transport = self.detect_transport(name, avf_device_info)
        channels = avf_device_info.get("channels", 1)
        manufacturer_hint = avf_device_info.get("manufacturer")
        
        return DeviceSignature(
            normalized_name=normalized_name,
            transport=transport,
            channels=channels,
            manufacturer_hint=manufacturer_hint
        )
    
    def find_portaudio_match(self, signature: DeviceSignature) -> MappingResult:
        """
        Find PortAudio device matching signature.
        
        Args:
            signature: DeviceSignature для поиска
            
        Returns:
            MappingResult
        """
        try:
            all_devices = sd.query_devices()
        except Exception as e:
            logger.error(f"Ошибка получения списка устройств PortAudio: {e}")
            return MappingResult(
                device_index=None,
                confidence=Confidence.NONE,
                reason=f"PortAudio query failed: {e}"
            )
        
        candidates: List[Tuple[int, float]] = []  # (device_index, score)
        
        for idx, device in enumerate(all_devices):
            if device.get('max_input_channels', 0) == 0:
                continue  # Пропускаем output-only устройства
            
            device_name = device.get('name', '')
            device_channels = device.get('max_input_channels', 0)
            
            # Вычисляем score
            score = 0.0
            
            # Exact name match
            if device_name == signature.normalized_name:
                score += 10.0
            elif signature.normalized_name.lower() in device_name.lower():
                score += 5.0
            
            # Channels match
            if device_channels == signature.channels:
                score += 5.0
            elif abs(device_channels - signature.channels) <= 1:
                score += 2.0
            
            # Transport hint (если есть)
            if signature.transport == DeviceTransport.BLUETOOTH:
                if "bluetooth" in device_name.lower() or "airpods" in device_name.lower():
                    score += 3.0
            
            if score > 0:
                candidates.append((idx, score))
        
        if not candidates:
            return MappingResult(
                device_index=None,
                confidence=Confidence.NONE,
                reason="No matching devices found in PortAudio"
            )
        
        # Сортируем по score
        candidates.sort(key=lambda x: x[1], reverse=True)
        best_idx, best_score = candidates[0]
        
        # Определяем confidence
        if best_score >= 15.0 and len(candidates) == 1:
            confidence = Confidence.HIGH
        elif best_score >= 10.0:
            confidence = Confidence.MEDIUM
        elif best_score >= 5.0:
            confidence = Confidence.LOW
        else:
            confidence = Confidence.NONE
        
        # Если есть несколько кандидатов с близким score - снижаем confidence
        if len(candidates) > 1 and candidates[1][1] >= best_score * 0.8:
            if confidence == Confidence.HIGH:
                confidence = Confidence.MEDIUM
            elif confidence == Confidence.MEDIUM:
                confidence = Confidence.LOW
        
        return MappingResult(
            device_index=best_idx,
            confidence=confidence,
            reason=f"Matched device '{sd.query_devices(best_idx)['name']}' with score {best_score:.1f}"
        )
    
    def get_device_index(self, avf_device_info: dict) -> MappingResult:
        """
        Get PortAudio device_index for AVFoundation device.
        
        Args:
            avf_device_info: Информация об устройстве от AVFoundation
            
        Returns:
            MappingResult
        """
        # Строим signature
        signature = self.build_signature(avf_device_info)
        cache_key = f"{signature.normalized_name}_{signature.channels}_{signature.transport.value}"
        
        # Проверяем кэш
        if cache_key in self._cache:
            cache_time = self._cache_timestamps.get(cache_key, 0)
            if time.time() - cache_time < self._cache_ttl_sec:
                cached_result = self._cache[cache_key]
                logger.debug(f"Использован кэшированный маппинг: {signature} → {cached_result.device_index}")
                return cached_result
        
        # Ищем совпадение
        result = self.find_portaudio_match(signature)
        
        # Кэшируем только успешные маппинги
        if result.is_usable():
            self._cache[cache_key] = result
            self._cache_timestamps[cache_key] = time.time()
            logger.info(f"Кэширован маппинг: {signature} → {result.device_index} ({result.confidence.value})")
        
        return result
    
    def clear_cache(self):
        """Clear mapping cache."""
        self._cache.clear()
        self._cache_timestamps.clear()
        logger.debug("Кэш маппингов очищен")
```

**Критерии готовности**:
- [ ] Файл создан
- [ ] Все методы реализованы
- [ ] Нормализация имен работает
- [ ] Confidence модель работает
- [ ] Кэширование работает
- [ ] Линтер проходит без ошибок

**Тесты**: `tests/test_avfoundation_mapping.py`
- [ ] Тест normalize_device_name()
- [ ] Тест detect_transport()
- [ ] Тест build_signature()
- [ ] Тест find_portaudio_match() (HIGH confidence)
- [ ] Тест find_portaudio_match() (MEDIUM confidence)
- [ ] Тест find_portaudio_match() (LOW confidence)
- [ ] Тест find_portaudio_match() (NONE confidence)
- [ ] Тест get_device_index() с кэшем
- [ ] Тест clear_cache()
- [ ] Покрытие ≥80%

---

## 🎯 Этап 2: State Machines (Неделя 2)

### День 5-6: Input State Machine

#### Задача 2.1: Создать `input_state_machine.py`

**Файл**: `modules/voice_recognition/core/avfoundation/input_state_machine.py`

**Содержимое** (структура):
```python
"""
Input State Machine for audio input routing.

States: STOPPED → STARTING → ACTIVE → STOPPING → STOPPED
                              ↓
                           FAILED
"""

import logging
import time
from enum import Enum
from typing import Optional, Callable
from dataclasses import dataclass

logger = logging.getLogger(__name__)


class InputState(Enum):
    """Input state enumeration."""
    STOPPED = "stopped"
    STARTING = "starting"
    ACTIVE = "active"
    STOPPING = "stopping"
    FAILED = "failed"


@dataclass
class InputStateMachine:
    """State machine for input audio routing."""
    
    state: InputState = InputState.STOPPED
    last_heartbeat_ts: Optional[float] = None
    start_timeout_sec: float = 2.5
    heartbeat_timeout_sec: float = 10.0
    max_retries: int = 3
    retry_count: int = 0
    max_restarts_per_period: int = 6
    restart_period_sec: float = 600.0  # 10 минут
    restart_timestamps: list = None
    
    def __post_init__(self):
        if self.restart_timestamps is None:
            self.restart_timestamps = []
    
    def transition_to(self, new_state: InputState, reason: str = ""):
        """
        Transition to new state.
        
        Args:
            new_state: Новое состояние
            reason: Причина перехода
        """
        old_state = self.state
        self.state = new_state
        
        logger.info(
            f"InputStateMachine: {old_state.value} → {new_state.value}"
            + (f" ({reason})" if reason else "")
        )
        
        if new_state == InputState.STARTING:
            self.restart_timestamps.append(time.monotonic())
            # Очищаем старые таймстемпы (старше restart_period_sec)
            cutoff = time.monotonic() - self.restart_period_sec
            self.restart_timestamps = [ts for ts in self.restart_timestamps if ts > cutoff]
        
        if new_state == InputState.ACTIVE:
            self.last_heartbeat_ts = time.monotonic()
            self.retry_count = 0
    
    def update_heartbeat(self):
        """Update heartbeat timestamp."""
        self.last_heartbeat_ts = time.monotonic()
    
    def check_heartbeat(self) -> bool:
        """
        Check if heartbeat is still valid.
        
        Returns:
            True if heartbeat is valid, False otherwise
        """
        if self.state != InputState.ACTIVE:
            return True
        
        if self.last_heartbeat_ts is None:
            return False
        
        elapsed = time.monotonic() - self.last_heartbeat_ts
        return elapsed < self.heartbeat_timeout_sec
    
    def can_retry(self) -> bool:
        """
        Check if retry is allowed.
        
        Returns:
            True if retry is allowed, False otherwise
        """
        if self.retry_count >= self.max_retries:
            return False
        
        # Проверяем лимит рестартов за период
        if len(self.restart_timestamps) >= self.max_restarts_per_period:
            return False
        
        return True
    
    def get_retry_backoff_sec(self) -> float:
        """
        Get retry backoff delay in seconds.
        
        Returns:
            Backoff delay
        """
        backoffs = [1.0, 2.0, 4.0]
        idx = min(self.retry_count, len(backoffs) - 1)
        return backoffs[idx]
    
    def should_rollback(self) -> bool:
        """
        Check if should rollback to fallback device.
        
        Returns:
            True if should rollback
        """
        return self.state == InputState.FAILED and not self.can_retry()
```

**Критерии готовности**:
- [ ] Файл создан
- [ ] State Machine реализована
- [ ] Все переходы состояний работают
- [ ] Heartbeat проверка работает
- [ ] Retry логика работает
- [ ] Линтер проходит без ошибок

**Тесты**: `tests/test_avfoundation_state_machines.py` (input часть)
- [ ] Тест переходов: STOPPED → STARTING → ACTIVE
- [ ] Тест переходов: ACTIVE → STOPPING → STOPPED
- [ ] Тест перехода: STARTING → FAILED (timeout)
- [ ] Тест перехода: ACTIVE → FAILED (heartbeat lost)
- [ ] Тест retry логики
- [ ] Тест heartbeat проверки
- [ ] Тест rollback логики
- [ ] Покрытие ≥80%

---

### День 7-8: Output State Machine

#### Задача 2.2: Создать `output_state_machine.py`

**Файл**: `modules/voice_recognition/core/avfoundation/output_state_machine.py`

**Содержимое** (структура):
```python
"""
Output State Machine for audio output routing.

States: READY → RECREATING → READY
              ↓
           ERROR
"""

import logging
import time
from enum import Enum
from typing import Optional
from dataclasses import dataclass

logger = logging.getLogger(__name__)


class OutputState(Enum):
    """Output state enumeration."""
    READY = "ready"
    RECREATING = "recreating"
    ERROR = "error"


@dataclass
class OutputStateMachine:
    """State machine for output audio routing."""
    
    state: OutputState = OutputState.READY
    recreate_timeout_sec: float = 1.5
    max_retries: int = 2
    retry_count: int = 0
    recreate_start_ts: Optional[float] = None
    
    def transition_to(self, new_state: OutputState, reason: str = ""):
        """
        Transition to new state.
        
        Args:
            new_state: Новое состояние
            reason: Причина перехода
        """
        old_state = self.state
        self.state = new_state
        
        logger.info(
            f"OutputStateMachine: {old_state.value} → {new_state.value}"
            + (f" ({reason})" if reason else "")
        )
        
        if new_state == OutputState.RECREATING:
            self.recreate_start_ts = time.monotonic()
        elif new_state == OutputState.READY:
            self.recreate_start_ts = None
            self.retry_count = 0
    
    def check_recreate_timeout(self) -> bool:
        """
        Check if recreate timeout exceeded.
        
        Returns:
            True if timeout exceeded, False otherwise
        """
        if self.state != OutputState.RECREATING:
            return False
        
        if self.recreate_start_ts is None:
            return False
        
        elapsed = time.monotonic() - self.recreate_start_ts
        return elapsed > self.recreate_timeout_sec
    
    def can_retry(self) -> bool:
        """
        Check if retry is allowed.
        
        Returns:
            True if retry is allowed, False otherwise
        """
        return self.retry_count < self.max_retries
    
    def get_retry_backoff_sec(self) -> float:
        """
        Get retry backoff delay in seconds.
        
        Returns:
            Backoff delay
        """
        backoffs = [0.25, 0.75]
        idx = min(self.retry_count, len(backoffs) - 1)
        return backoffs[idx]
```

**Критерии готовности**:
- [ ] Файл создан
- [ ] State Machine реализована
- [ ] Все переходы состояний работают
- [ ] Timeout проверка работает
- [ ] Retry логика работает
- [ ] Линтер проходит без ошибок

**Тесты**: `tests/test_avfoundation_state_machines.py` (output часть)
- [ ] Тест переходов: READY → RECREATING → READY
- [ ] Тест перехода: RECREATING → ERROR (timeout)
- [ ] Тест перехода: ERROR → RECREATING (retry)
- [ ] Тест retry логики
- [ ] Тест timeout проверки
- [ ] Покрытие ≥80%

---

## 🎯 Этап 3: Route Manager Core (Недели 3-4)

### День 9-10: Debounce Manager

#### Задача 3.1: Создать `debounce_manager.py`

**Файл**: `modules/voice_recognition/core/avfoundation/debounce_manager.py`

**Содержимое** (структура):
```python
"""
Debounce manager for device change events.

Per-device debounce with configurable delays.
"""

import logging
import time
from typing import Dict, Optional
from dataclasses import dataclass

from .contracts import DeviceTransport, DeviceSignature

logger = logging.getLogger(__name__)


@dataclass
class DebounceConfig:
    """Debounce configuration for a transport type."""
    initial_ms: int
    increment_ms: int
    max_ms: int


class DebounceManager:
    """Manages debounce delays for device changes."""
    
    # Конфигурация debounce по типам транспорта
    DEFAULT_CONFIG = {
        DeviceTransport.BLUETOOTH: DebounceConfig(
            initial_ms=200,
            increment_ms=200,
            max_ms=1200
        ),
        DeviceTransport.USB: DebounceConfig(
            initial_ms=100,
            increment_ms=100,
            max_ms=600
        ),
        DeviceTransport.BUILT_IN: DebounceConfig(
            initial_ms=100,
            increment_ms=0,  # Нет инкремента для built-in
            max_ms=200
        ),
        DeviceTransport.UNKNOWN: DebounceConfig(
            initial_ms=200,  # Используем Bluetooth worst-case
            increment_ms=200,
            max_ms=1200
        ),
    }
    
    def __init__(self, config: Optional[Dict[DeviceTransport, DebounceConfig]] = None):
        """
        Initialize DebounceManager.
        
        Args:
            config: Кастомная конфигурация (опционально)
        """
        self._config = config or self.DEFAULT_CONFIG
        self._device_timestamps: Dict[str, float] = {}
        self._device_counts: Dict[str, int] = {}
    
    def get_debounce_delay_ms(self, signature: DeviceSignature) -> int:
        """
        Get debounce delay for device.
        
        Args:
            signature: DeviceSignature устройства
            
        Returns:
            Debounce delay in milliseconds
        """
        config = self._config.get(signature.transport, self.DEFAULT_CONFIG[DeviceTransport.UNKNOWN])
        device_key = f"{signature.normalized_name}_{signature.transport.value}"
        
        # Получаем количество событий для этого устройства
        count = self._device_counts.get(device_key, 0)
        
        # Вычисляем задержку
        delay_ms = config.initial_ms + (count * config.increment_ms)
        delay_ms = min(delay_ms, config.max_ms)
        
        # Увеличиваем счетчик
        self._device_counts[device_key] = count + 1
        self._device_timestamps[device_key] = time.monotonic()
        
        logger.debug(
            f"Debounce для {signature.normalized_name} ({signature.transport.value}): "
            f"{delay_ms}ms (счетчик: {count + 1})"
        )
        
        return delay_ms
    
    def reset_device(self, signature: DeviceSignature):
        """
        Reset debounce state for device.
        
        Args:
            signature: DeviceSignature устройства
        """
        device_key = f"{signature.normalized_name}_{signature.transport.value}"
        self._device_counts.pop(device_key, None)
        self._device_timestamps.pop(device_key, None)
        logger.debug(f"Debounce сброшен для {signature.normalized_name}")
    
    def clear_all(self):
        """Clear all debounce state."""
        self._device_timestamps.clear()
        self._device_counts.clear()
        logger.debug("Все debounce состояния очищены")
```

**Критерии готовности**:
- [ ] Файл создан
- [ ] Debounce логика реализована
- [ ] Per-device счетчики работают
- [ ] Конфигурация по транспортам работает
- [ ] Линтер проходит без ошибок

**Тесты**: `tests/test_avfoundation_route_manager.py` (debounce часть)
- [ ] Тест get_debounce_delay_ms() для Bluetooth
- [ ] Тест get_debounce_delay_ms() для USB
- [ ] Тест get_debounce_delay_ms() для Built-in
- [ ] Тест инкремента счетчика
- [ ] Тест reset_device()
- [ ] Тест clear_all()
- [ ] Покрытие ≥80%

---

### День 11-12: Decision Engine

#### Задача 3.2: Создать `decision_engine.py`

**Файл**: `modules/voice_recognition/core/avfoundation/decision_engine.py`

**Содержимое** (структура):
```python
"""
Decision engine for route manager.

Implements rules from interaction_matrix.yaml.
"""

import logging
from enum import Enum
from typing import Optional
from dataclasses import dataclass

from .contracts import RouteSnapshot, MappingResult

logger = logging.getLogger(__name__)


class Decision(Enum):
    """Decision enumeration."""
    START = "start"
    ABORT = "abort"
    RETRY = "retry"
    DEGRADE = "degrade"
    NOOP = "noop"


@dataclass
class DecisionContext:
    """Context for decision making."""
    first_run: bool
    restart_pending: bool
    update_in_progress: bool
    device_busy: bool
    network_offline: bool
    mic_permission_granted: bool
    app_mode: str  # SLEEPING, LISTENING, PROCESSING


class DecisionEngine:
    """Engine for making routing decisions."""
    
    def decide_route_manager_reconcile(
        self,
        snapshot: RouteSnapshot,
        mapping_result: Optional[MappingResult],
        context: DecisionContext
    ) -> Decision:
        """
        Decide action for route manager reconcile.
        
        Implements rules from interaction_matrix.yaml:
        - hard_stop: first_run, restart_pending, update_in_progress
        - graceful: device_busy → retry, network_offline → degrade
        
        Args:
            snapshot: RouteSnapshot текущего состояния
            mapping_result: Результат маппинга (если есть)
            context: DecisionContext с системными состояниями
            
        Returns:
            Decision
        """
        # Hard stop: first_run
        if context.first_run:
            logger.warning("Decision: ABORT (first_run in progress)")
            return Decision.ABORT
        
        # Hard stop: restart_pending
        if context.restart_pending:
            logger.warning("Decision: ABORT (restart_pending)")
            return Decision.ABORT
        
        # Hard stop: update_in_progress
        if context.update_in_progress:
            logger.warning("Decision: ABORT (update_in_progress)")
            return Decision.ABORT
        
        # Hard stop: mic permission denied
        if not context.mic_permission_granted:
            logger.warning("Decision: ABORT (mic permission denied)")
            return Decision.ABORT
        
        # Graceful: device_busy → retry
        if context.device_busy and context.app_mode == "LISTENING":
            logger.info("Decision: RETRY (device busy)")
            return Decision.RETRY
        
        # Graceful: network_offline → degrade
        if context.network_offline and context.app_mode == "LISTENING":
            logger.info("Decision: DEGRADE (network offline)")
            return Decision.DEGRADE
        
        # Проверяем, нужно ли действие
        if not snapshot.input_changed() and not snapshot.output_changed():
            logger.debug("Decision: NOOP (no changes)")
            return Decision.NOOP
        
        # Если appMode не LISTENING, не начинаем input
        if context.app_mode != "LISTENING" and snapshot.input_changed():
            logger.debug("Decision: NOOP (appMode not LISTENING)")
            return Decision.NOOP
        
        # Проверяем mapping result
        if mapping_result and not mapping_result.is_usable():
            if mapping_result.confidence.value == "none":
                logger.warning("Decision: ABORT (no device mapping)")
                return Decision.ABORT
            # LOW confidence - используем system default
            logger.info("Decision: START (using system default due to LOW confidence)")
        
        logger.info("Decision: START")
        return Decision.START
    
    def format_decision_log(
        self,
        decision: Decision,
        context: DecisionContext,
        duration_ms: int
    ) -> str:
        """
        Format decision log in canonical format.
        
        Format: decision=<start|abort|retry|degrade> ctx={...} source=route_manager duration_ms=<int>
        
        Args:
            decision: Decision
            context: DecisionContext
            duration_ms: Duration in milliseconds
            
        Returns:
            Formatted log string
        """
        ctx_str = (
            f"mic={'granted' if context.mic_permission_granted else 'denied'},"
            f"device={'busy' if context.device_busy else 'idle'},"
            f"network={'offline' if context.network_offline else 'online'},"
            f"firstRun={'true' if context.first_run else 'false'},"
            f"appMode={context.app_mode}"
        )
        
        return (
            f"decision={decision.value} "
            f"ctx={{{ctx_str}}} "
            f"source=route_manager "
            f"duration_ms={duration_ms}"
        )
```

**Критерии готовности**:
- [ ] Файл создан
- [ ] Decision логика реализована
- [ ] Правила из interaction_matrix.yaml реализованы
- [ ] Канонический формат логов работает
- [ ] Линтер проходит без ошибок

**Тесты**: `tests/test_avfoundation_route_manager.py` (decision часть)
- [ ] Тест ABORT при first_run
- [ ] Тест ABORT при restart_pending
- [ ] Тест ABORT при update_in_progress
- [ ] Тест ABORT при mic denied
- [ ] Тест RETRY при device_busy
- [ ] Тест DEGRADE при network_offline
- [ ] Тест NOOP при отсутствии изменений
- [ ] Тест START при нормальных условиях
- [ ] Тест format_decision_log()
- [ ] Pairwise тесты (≥12 комбинаций)
- [ ] Негативные тесты (≥2)
- [ ] Покрытие ≥80%

---

### День 13-14: Reconcile Engine

#### Задача 3.3: Создать `reconcile_engine.py`

**Файл**: `modules/voice_recognition/core/avfoundation/reconcile_engine.py`

**Содержимое** (структура):
```python
"""
Reconcile engine for route manager.

Compares desired state with active state and determines actions.
"""

import logging
from typing import Optional
from dataclasses import dataclass

from .contracts import RouteSnapshot, DeviceSignature, MappingResult
from .mapping import DeviceMapper

logger = logging.getLogger(__name__)


@dataclass
class ReconcileResult:
    """Result of reconcile operation."""
    input_changed: bool
    output_changed: bool
    desired_input: Optional[DeviceSignature]
    desired_output: Optional[DeviceSignature]
    mapping_result: Optional[MappingResult]
    action_required: bool


class ReconcileEngine:
    """Engine for reconciling audio routes."""
    
    def __init__(self, device_mapper: DeviceMapper):
        """
        Initialize ReconcileEngine.
        
        Args:
            device_mapper: DeviceMapper instance
        """
        self.device_mapper = device_mapper
    
    def create_snapshot(
        self,
        system_default_input: Optional[dict],
        desired_input: Optional[dict],
        active_input: Optional[DeviceSignature],
        active_output: Optional[DeviceSignature]
    ) -> RouteSnapshot:
        """
        Create RouteSnapshot from current state.
        
        Args:
            system_default_input: System default input device info (from AVFoundation)
            desired_input: Desired input device info (user selection or system default)
            active_input: Currently active input device
            active_output: Currently active output device
            
        Returns:
            RouteSnapshot
        """
        # Преобразуем system_default_input в DeviceSignature
        system_input_sig = None
        if system_default_input:
            system_input_sig = self.device_mapper.build_signature(system_default_input)
        
        # Преобразуем desired_input в DeviceSignature
        desired_input_sig = None
        if desired_input:
            desired_input_sig = self.device_mapper.build_signature(desired_input)
        elif system_input_sig:
            # Если desired не указан, используем system default
            desired_input_sig = system_input_sig
        
        return RouteSnapshot(
            system_default_input=system_input_sig,
            desired_input=desired_input_sig,
            active_input=active_input,
            active_output=active_output
        )
    
    def determine_desired_route(
        self,
        snapshot: RouteSnapshot,
        user_selection: Optional[dict] = None
    ) -> tuple[Optional[DeviceSignature], Optional[MappingResult]]:
        """
        Determine desired input route.
        
        Priority:
        1. User selection (manual mode)
        2. System default input
        3. Fallback (None - use system default in PortAudio)
        
        Args:
            snapshot: RouteSnapshot
            user_selection: User-selected device (optional)
            
        Returns:
            Tuple of (desired_input_signature, mapping_result)
        """
        # Priority 1: User selection
        if user_selection:
            signature = self.device_mapper.build_signature(user_selection)
            mapping_result = self.device_mapper.get_device_index(user_selection)
            return signature, mapping_result
        
        # Priority 2: System default
        if snapshot.system_default_input:
            # Получаем mapping для system default
            system_info = {
                "name": snapshot.system_default_input.normalized_name,
                "channels": snapshot.system_default_input.channels,
            }
            mapping_result = self.device_mapper.get_device_index(system_info)
            return snapshot.system_default_input, mapping_result
        
        # Priority 3: Fallback (None - use system default in PortAudio)
        return None, None
    
    def compare_routes(
        self,
        snapshot: RouteSnapshot,
        desired_input: Optional[DeviceSignature],
        desired_output: Optional[DeviceSignature]
    ) -> ReconcileResult:
        """
        Compare desired routes with active routes.
        
        Args:
            snapshot: RouteSnapshot
            desired_input: Desired input device
            desired_output: Desired output device
            
        Returns:
            ReconcileResult
        """
        input_changed = False
        if desired_input is not None:
            input_changed = desired_input != snapshot.active_input
        elif snapshot.active_input is not None:
            # Если desired None, но active есть - нужно остановить
            input_changed = True
        
        output_changed = False
        if desired_output is not None:
            output_changed = desired_output != snapshot.active_output
        elif snapshot.active_output is not None:
            # Если desired None, но active есть - нужно остановить
            output_changed = True
        
        action_required = input_changed or output_changed
        
        return ReconcileResult(
            input_changed=input_changed,
            output_changed=output_changed,
            desired_input=desired_input,
            desired_output=desired_output,
            mapping_result=None,  # Будет заполнено позже
            action_required=action_required
        )
```

**Критерии готовности**:
- [ ] Файл создан
- [ ] Reconcile логика реализована
- [ ] create_snapshot() работает
- [ ] determine_desired_route() работает
- [ ] compare_routes() работает
- [ ] Линтер проходит без ошибок

**Тесты**: `tests/test_avfoundation_route_manager.py` (reconcile часть)
- [ ] Тест create_snapshot()
- [ ] Тест determine_desired_route() с user_selection
- [ ] Тест determine_desired_route() с system_default
- [ ] Тест determine_desired_route() fallback
- [ ] Тест compare_routes() input_changed
- [ ] Тест compare_routes() output_changed
- [ ] Тест compare_routes() no_changes
- [ ] Покрытие ≥80%

---

### День 15-16: Route Manager (основной)

#### Задача 3.4: Создать `route_manager.py`

**Файл**: `modules/voice_recognition/core/avfoundation/route_manager.py`

**Содержимое** (структура - очень большой файл, показываю ключевые части):

```python
"""
Audio Route Manager - центральный координатор аудио маршрутизации.

Управляет переключением между input/output устройствами через reconcile loop.
"""

import asyncio
import logging
import time
from typing import Optional, Dict, Any, Callable
from threading import Lock

from .contracts import RouteSnapshot, DeviceSignature, MappingResult, Decision
from .mapping import DeviceMapper
from .reconcile_engine import ReconcileEngine, ReconcileResult
from .decision_engine import DecisionEngine, DecisionContext
from .debounce_manager import DebounceManager
from .input_state_machine import InputStateMachine, InputState
from .output_state_machine import OutputStateMachine, OutputState

logger = logging.getLogger(__name__)


class AudioRouteManager:
    """Central manager for audio routing."""
    
    def __init__(
        self,
        device_mapper: DeviceMapper,
        get_system_devices: Callable[[], Dict[str, Any]],
        config: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize AudioRouteManager.
        
        Args:
            device_mapper: DeviceMapper instance
            get_system_devices: Callable для получения списка устройств от AVFoundation
            config: Configuration dictionary
        """
        self.device_mapper = device_mapper
        self.get_system_devices = get_system_devices
        self.config = config or {}
        
        # Engines
        self.reconcile_engine = ReconcileEngine(device_mapper)
        self.decision_engine = DecisionEngine()
        self.debounce_manager = DebounceManager()
        
        # State machines
        self.input_sm = InputStateMachine()
        self.output_sm = OutputStateMachine()
        
        # State
        self.active_input: Optional[DeviceSignature] = None
        self.active_output: Optional[DeviceSignature] = None
        self.user_selection: Optional[dict] = None
        
        # Single-flight механизм
        self._reconcile_lock = Lock()
        self._reconcile_in_progress = False
        self._pending_reconcile = False
        
        # Callbacks
        self._on_input_start: Optional[Callable[[int, DeviceSignature], None]] = None
        self._on_input_stop: Optional[Callable[[], None]] = None
        self._on_output_recreate: Optional[Callable[[], None]] = None
        
        # Event loop для async операций
        self._event_loop: Optional[asyncio.AbstractEventLoop] = None
    
    def set_event_loop(self, loop: asyncio.AbstractEventLoop):
        """Set event loop for async operations."""
        self._event_loop = loop
    
    def set_callbacks(
        self,
        on_input_start: Optional[Callable[[int, DeviceSignature], None]] = None,
        on_input_stop: Optional[Callable[[], None]] = None,
        on_output_recreate: Optional[Callable[[], None]] = None
    ):
        """Set callbacks for route changes."""
        self._on_input_start = on_input_start
        self._on_input_stop = on_input_stop
        self._on_output_recreate = on_output_recreate
    
    def reconcile_routes(
        self,
        context: DecisionContext,
        user_selection: Optional[dict] = None
    ) -> bool:
        """
        Reconcile audio routes.
        
        Single-flight механизм: только один reconcile выполняется одновременно.
        Новые события устанавливают pending флаг.
        
        Args:
            context: DecisionContext с системными состояниями
            user_selection: User-selected device (optional)
            
        Returns:
            True if reconcile was executed, False if skipped (pending)
        """
        # Проверяем single-flight
        with self._reconcile_lock:
            if self._reconcile_in_progress:
                self._pending_reconcile = True
                logger.debug("Reconcile уже выполняется, установлен pending флаг")
                return False
            
            self._reconcile_in_progress = True
            self._pending_reconcile = False
        
        try:
            start_time = time.monotonic()
            
            # Получаем текущие устройства от AVFoundation
            system_devices = self.get_system_devices()
            system_default_input = system_devices.get("default_input")
            
            # Создаем snapshot
            snapshot = self.reconcile_engine.create_snapshot(
                system_default_input=system_default_input,
                desired_input=user_selection or self.user_selection,
                active_input=self.active_input,
                active_output=self.active_output
            )
            
            # Определяем desired route
            desired_input, mapping_result = self.reconcile_engine.determine_desired_route(
                snapshot,
                user_selection or self.user_selection
            )
            
            # Сравниваем routes
            reconcile_result = self.reconcile_engine.compare_routes(
                snapshot,
                desired_input,
                None  # Output всегда следует system default
            )
            
            # Принимаем решение
            decision = self.decision_engine.decide_route_manager_reconcile(
                snapshot,
                mapping_result,
                context
            )
            
            # Форматируем decision log
            duration_ms = int((time.monotonic() - start_time) * 1000)
            decision_log = self.decision_engine.format_decision_log(
                decision,
                context,
                duration_ms
            )
            logger.info(decision_log)
            
            # Применяем решение
            if decision == Decision.START:
                if reconcile_result.input_changed:
                    self._apply_input_change(mapping_result, desired_input)
                if reconcile_result.output_changed:
                    self._apply_output_change()
            elif decision == Decision.ABORT:
                logger.warning("Reconcile aborted by decision engine")
            elif decision == Decision.RETRY:
                # Retry будет обработан через debounce
                logger.info("Reconcile retry scheduled")
            elif decision == Decision.DEGRADE:
                logger.info("Reconcile degraded (continuing with limited functionality)")
            elif decision == Decision.NOOP:
                logger.debug("Reconcile: no action required")
            
            return True
            
        finally:
            with self._reconcile_lock:
                self._reconcile_in_progress = False
                pending = self._pending_reconcile
                self._pending_reconcile = False
            
            # Если были pending события, запускаем новый reconcile
            if pending:
                logger.debug("Запуск pending reconcile")
                # Здесь можно вызвать reconcile_routes снова, но нужно быть осторожным с рекурсией
                # Лучше через event loop или отдельный поток
    
    def _apply_input_change(self, mapping_result: Optional[MappingResult], desired_input: DeviceSignature):
        """Apply input route change."""
        if mapping_result and mapping_result.is_usable():
            device_index = mapping_result.device_index
        else:
            # Fallback: use system default (None = system default в PortAudio)
            device_index = None
        
        # Останавливаем текущий input
        if self.active_input is not None:
            self.input_sm.transition_to(InputState.STOPPING, "route change")
            if self._on_input_stop:
                self._on_input_stop()
            self.input_sm.transition_to(InputState.STOPPED, "stopped")
        
        # Запускаем новый input
        self.input_sm.transition_to(InputState.STARTING, "route change")
        if self._on_input_start:
            self._on_input_start(device_index, desired_input)
        
        self.active_input = desired_input
    
    def _apply_output_change(self):
        """Apply output route change."""
        self.output_sm.transition_to(OutputState.RECREATING, "route change")
        if self._on_output_recreate:
            self._on_output_recreate()
        # Output всегда следует system default, поэтому просто пересоздаем
        self.output_sm.transition_to(OutputState.READY, "recreated")
    
    def get_active_input_device(self) -> Optional[DeviceSignature]:
        """Get currently active input device."""
        return self.active_input
    
    def get_active_output_device(self) -> Optional[DeviceSignature]:
        """Get currently active output device."""
        return self.active_output
```

**Критерии готовности**:
- [ ] Файл создан
- [ ] Route Manager реализован
- [ ] Single-flight механизм работает
- [ ] Reconcile loop работает
- [ ] Применение решений работает
- [ ] Линтер проходит без ошибок

**Тесты**: `tests/test_avfoundation_route_manager.py` (основной)
- [ ] Тест reconcile_routes() single-flight
- [ ] Тест reconcile_routes() pending
- [ ] Тест _apply_input_change()
- [ ] Тест _apply_output_change()
- [ ] Тест get_active_input_device()
- [ ] Тест get_active_output_device()
- [ ] Интеграционные тесты
- [ ] Покрытие ≥80%

---

## 🎯 Этап 4: Адаптеры (Неделя 5)

### День 17-18: AVFoundation Monitor

#### Задача 4.1: Создать `avf_monitor.py`

**Файл**: `modules/voice_recognition/core/avfoundation/adapters/avf_monitor.py`

**Содержимое** (структура - требует PyObjC):
```python
"""
AVFoundation device monitor.

Dual mechanism: NSNotificationCenter (instant) + Polling (fallback).
"""

import logging
import threading
import time
from typing import Dict, List, Optional, Callable
from dataclasses import dataclass

try:
    from Foundation import NSNotificationCenter, NSObject
    from AVFoundation import AVAudioSession
    PYOBJC_AVAILABLE = True
except ImportError:
    PYOBJC_AVAILABLE = False
    logger.warning("PyObjC not available, AVFoundation monitoring disabled")

from ..contracts import DeviceSignature
from ..mapping import DeviceMapper

logger = logging.getLogger(__name__)


@dataclass
class DeviceInfo:
    """Device information from AVFoundation."""
    name: str
    uid: str
    channels: int
    manufacturer: Optional[str] = None


class AVFoundationDeviceMonitor:
    """Monitor for AVFoundation audio devices."""
    
    def __init__(
        self,
        device_mapper: DeviceMapper,
        check_interval_sec: float = 1.5,
        use_notifications: bool = True
    ):
        """
        Initialize AVFoundationDeviceMonitor.
        
        Args:
            device_mapper: DeviceMapper instance
            check_interval_sec: Polling interval in seconds
            use_notifications: Use NSNotificationCenter for instant detection
        """
        if not PYOBJC_AVAILABLE:
            raise RuntimeError("PyObjC not available, cannot use AVFoundation")
        
        self.device_mapper = device_mapper
        self.check_interval_sec = check_interval_sec
        self.use_notifications = use_notifications
        
        self._monitoring = False
        self._monitor_thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        
        self._device_cache: Dict[str, DeviceInfo] = {}
        self._last_device_list: List[DeviceSignature] = []
        
        self._on_device_changed: Optional[Callable[[DeviceSignature], None]] = None
        
        # Notification observer
        self._notification_observer = None
        if self.use_notifications:
            self._setup_notifications()
    
    def _setup_notifications(self):
        """Setup NSNotificationCenter observers."""
        if not PYOBJC_AVAILABLE:
            return
        
        try:
            center = NSNotificationCenter.defaultCenter()
            
            # Observer для изменений маршрута
            center.addObserver_selector_name_object_(
                self,
                "routeChanged:",
                "AVAudioSessionRouteChangeNotification",
                None
            )
            
            logger.info("NSNotificationCenter observers установлены")
        except Exception as e:
            logger.error(f"Ошибка установки notifications: {e}")
            self.use_notifications = False
    
    def routeChanged_(self, notification):
        """Handle route change notification."""
        if not self._monitoring:
            return
        
        logger.info("Получено уведомление об изменении маршрута")
        # Триггерим проверку устройств
        self._check_devices_instant()
    
    def _check_devices_instant(self):
        """Check devices immediately (triggered by notification)."""
        devices = self._query_devices()
        self._process_device_changes(devices)
    
    def _query_devices(self) -> List[DeviceInfo]:
        """Query devices from AVFoundation."""
        if not PYOBJC_AVAILABLE:
            return []
        
        try:
            session = AVAudioSession.sharedInstance()
            # Получаем список input устройств
            # Это упрощенная версия, реальная реализация требует больше кода
            devices = []
            # TODO: Реализовать получение списка устройств через AVAudioSession
            return devices
        except Exception as e:
            logger.error(f"Ошибка получения устройств от AVFoundation: {e}")
            return []
    
    def _process_device_changes(self, devices: List[DeviceInfo]):
        """Process device changes and trigger callbacks."""
        current_signatures = []
        for device in devices:
            signature = self.device_mapper.build_signature({
                "name": device.name,
                "channels": device.channels,
                "manufacturer": device.manufacturer
            })
            current_signatures.append(signature)
        
        # Сравниваем с кэшем
        if current_signatures != self._last_device_list:
            logger.info(f"Обнаружено изменение устройств: {len(current_signatures)} устройств")
            
            # Находим новое/измененное устройство
            if current_signatures:
                new_device = current_signatures[0]  # Упрощенно - берем первое
                if new_device not in self._last_device_list:
                    if self._on_device_changed:
                        self._on_device_changed(new_device)
            
            self._last_device_list = current_signatures
    
    def start_monitoring(self, on_device_changed: Optional[Callable[[DeviceSignature], None]] = None):
        """Start monitoring devices."""
        if self._monitoring:
            return
        
        self._on_device_changed = on_device_changed
        self._monitoring = True
        self._stop_event.clear()
        
        # Запускаем polling thread
        self._monitor_thread = threading.Thread(
            target=self._monitor_loop,
            name="AVFoundationDeviceMonitor",
            daemon=True
        )
        self._monitor_thread.start()
        
        logger.info("AVFoundationDeviceMonitor запущен")
    
    def _monitor_loop(self):
        """Main monitoring loop (polling)."""
        while not self._stop_event.is_set():
            devices = self._query_devices()
            self._process_device_changes(devices)
            
            # Ждем до следующей проверки
            self._stop_event.wait(self.check_interval_sec)
    
    def stop_monitoring(self):
        """Stop monitoring devices."""
        if not self._monitoring:
            return
        
        self._monitoring = False
        self._stop_event.set()
        
        if self._monitor_thread:
            self._monitor_thread.join(timeout=5.0)
        
        # Удаляем notification observer
        if self._notification_observer and PYOBJC_AVAILABLE:
            try:
                center = NSNotificationCenter.defaultCenter()
                center.removeObserver_(self._notification_observer)
            except Exception as e:
                logger.error(f"Ошибка удаления observer: {e}")
        
        logger.info("AVFoundationDeviceMonitor остановлен")
    
    def get_current_devices(self) -> Dict[str, any]:
        """Get current devices info."""
        devices = self._query_devices()
        default_input = devices[0] if devices else None
        
        return {
            "default_input": {
                "name": default_input.name,
                "channels": default_input.channels,
                "manufacturer": default_input.manufacturer
            } if default_input else None,
            "all_devices": [
                {
                    "name": d.name,
                    "channels": d.channels,
                    "manufacturer": d.manufacturer
                }
                for d in devices
            ]
        }
```

**Критерии готовности**:
- [ ] Файл создан
- [ ] Мониторинг реализован
- [ ] NSNotificationCenter работает
- [ ] Polling fallback работает
- [ ] Линтер проходит без ошибок

**Тесты**: `tests/test_avfoundation_adapters.py` (monitor часть)
- [ ] Тест start_monitoring()
- [ ] Тест stop_monitoring()
- [ ] Тест _query_devices()
- [ ] Тест _process_device_changes()
- [ ] Тест get_current_devices()
- [ ] Покрытие ≥80%

---

### День 19-20: AVFoundation Output

#### Задача 4.2: Создать `avf_output.py`

**Файл**: `modules/voice_recognition/core/avfoundation/adapters/avf_output.py`

**Содержимое** (структура - требует PyObjC):
```python
"""
AVFoundation audio playback.

Uses AVAudioEngine and AVAudioPlayerNode for output.
"""

import logging
import numpy as np
from typing import Optional, List, Tuple
from dataclasses import dataclass
from queue import Queue
import threading

try:
    from AVFoundation import AVAudioEngine, AVAudioPlayerNode, AVAudioFormat, AVAudioPCMBuffer
    from Foundation import NSRunLoop
    PYOBJC_AVAILABLE = True
except ImportError:
    PYOBJC_AVAILABLE = False

from ..contracts import DeviceSignature

logger = logging.getLogger(__name__)


@dataclass
class ChunkInfo:
    """Audio chunk information."""
    chunk_id: str
    audio_data: np.ndarray
    sample_rate: int
    channels: int
    enqueue_ts: float
    priority: int = 0


class AVFoundationAudioPlayback:
    """AVFoundation-based audio playback."""
    
    def __init__(
        self,
        max_queue_ms: int = 5000,
        max_queue_bytes: int = 5242880,  # 5MB
        sample_rate_conversion: bool = True
    ):
        """
        Initialize AVFoundationAudioPlayback.
        
        Args:
            max_queue_ms: Maximum queue duration in milliseconds
            max_queue_bytes: Maximum queue size in bytes
            sample_rate_conversion: Enable sample rate conversion (16kHz → 48kHz)
        """
        if not PYOBJC_AVAILABLE:
            raise RuntimeError("PyObjC not available, cannot use AVFoundation")
        
        self.max_queue_ms = max_queue_ms
        self.max_queue_bytes = max_queue_bytes
        self.sample_rate_conversion = sample_rate_conversion
        
        self._engine: Optional[AVAudioEngine] = None
        self._player_node: Optional[AVAudioPlayerNode] = None
        self._queue: Queue = Queue()
        self._playing = False
        self._lock = threading.Lock()
        
        self._active_output: Optional[DeviceSignature] = None
    
    def initialize(self) -> bool:
        """Initialize AVAudioEngine."""
        try:
            self._engine = AVAudioEngine.alloc().init()
            self._player_node = AVAudioPlayerNode.alloc().init()
            
            # Attach player node to engine
            self._engine.attachNode_(self._player_node)
            
            # Connect to main mixer
            main_mixer = self._engine.mainMixerNode()
            self._engine.connect_to_format_(
                self._player_node,
                main_mixer,
                None  # Use engine's format
            )
            
            # Start engine
            if not self._engine.startAndReturnError_(None):
                logger.error("Ошибка запуска AVAudioEngine")
                return False
            
            logger.info("AVAudioEngine инициализирован")
            return True
            
        except Exception as e:
            logger.error(f"Ошибка инициализации AVAudioEngine: {e}")
            return False
    
    def play_chunk(
        self,
        audio_data: np.ndarray,
        sample_rate: int = 16000,
        channels: int = 1
    ) -> bool:
        """
        Play audio chunk.
        
        Args:
            audio_data: Audio data as numpy array
            sample_rate: Sample rate (default 16kHz)
            channels: Number of channels (default 1 = mono)
            
        Returns:
            True if chunk was queued, False otherwise
        """
        if not self._engine or not self._player_node:
            logger.warning("AVAudioEngine не инициализирован")
            return False
        
        try:
            # Конвертируем numpy в AVAudioPCMBuffer
            pcm_buffer = self._numpy_to_pcm_buffer(audio_data, sample_rate, channels)
            
            if not pcm_buffer:
                logger.error("Ошибка конвертации numpy в PCM buffer")
                return False
            
            # Schedule buffer
            self._player_node.scheduleBuffer_completionHandler_(
                pcm_buffer,
                None  # No completion handler
            )
            
            # Start playing if not already
            if not self._playing:
                self._player_node.play()
                self._playing = True
            
            return True
            
        except Exception as e:
            logger.error(f"Ошибка воспроизведения чанка: {e}")
            return False
    
    def _numpy_to_pcm_buffer(
        self,
        audio_data: np.ndarray,
        sample_rate: int,
        channels: int
    ) -> Optional[AVAudioPCMBuffer]:
        """
        Convert numpy array to AVAudioPCMBuffer.
        
        Args:
            audio_data: Audio data as numpy array
            sample_rate: Sample rate
            channels: Number of channels
            
        Returns:
            AVAudioPCMBuffer or None
        """
        try:
            # Получаем формат engine
            engine_format = self._engine.outputNode().outputFormatForBus_(0)
            target_sample_rate = int(engine_format.sampleRate())
            target_channels = engine_format.channelCount()
            
            # Конвертируем sample rate если нужно
            if self.sample_rate_conversion and sample_rate != target_sample_rate:
                # TODO: Реализовать sample rate conversion
                logger.warning(f"Sample rate conversion {sample_rate} → {target_sample_rate} не реализовано")
            
            # Конвертируем channels если нужно
            if channels != target_channels:
                # TODO: Реализовать channel conversion
                logger.warning(f"Channel conversion {channels} → {target_channels} не реализовано")
            
            # Создаем формат
            audio_format = AVAudioFormat.alloc().initWithCommonFormat_sampleRate_channels_interleaved_(
                1,  # pcmFormatFloat32
                target_sample_rate,
                target_channels,
                False  # non-interleaved
            )
            
            # Создаем buffer
            frame_count = len(audio_data)
            pcm_buffer = AVAudioPCMBuffer.alloc().initWithFormat_frameCapacity_(
                audio_format,
                frame_count
            )
            
            # Копируем данные
            # TODO: Реализовать копирование numpy → AVAudioPCMBuffer
            # Это требует работы с ObjC memory management
            
            return pcm_buffer
            
        except Exception as e:
            logger.error(f"Ошибка конвертации numpy в PCM buffer: {e}")
            return None
    
    def stop_playback(self):
        """Stop playback."""
        if self._player_node:
            self._player_node.stop()
            self._playing = False
    
    def shutdown(self):
        """Shutdown AVAudioEngine."""
        if self._engine:
            self._engine.stop()
            self._engine = None
            self._player_node = None
            self._playing = False
            logger.info("AVAudioEngine остановлен")
```

**Критерии готовности**:
- [ ] Файл создан
- [ ] Output реализован
- [ ] AVAudioEngine инициализация работает
- [ ] Конвертация numpy → AVAudioPCMBuffer работает
- [ ] Sample rate conversion работает
- [ ] Линтер проходит без ошибок

**Тесты**: `tests/test_avfoundation_adapters.py` (output часть)
- [ ] Тест initialize()
- [ ] Тест play_chunk()
- [ ] Тест _numpy_to_pcm_buffer()
- [ ] Тест stop_playback()
- [ ] Тест shutdown()
- [ ] Покрытие ≥80%

---

### День 21: Google Input Adapter

#### Задача 4.3: Создать `google_input.py`

**Файл**: `modules/voice_recognition/core/avfoundation/adapters/google_input.py`

**Содержимое**:
```python
"""
Google Input Controller - адаптер для SpeechRecognizer.

Получает device_index от RouteManager и передает в speech_recognition.Microphone.
"""

import logging
from typing import Optional

import speech_recognition as sr

from ..contracts import DeviceSignature

logger = logging.getLogger(__name__)


class GoogleInputController:
    """Adapter for Google Speech Recognition input."""
    
    def __init__(self):
        """Initialize GoogleInputController."""
        self._current_device_index: Optional[int] = None
        self._current_signature: Optional[DeviceSignature] = None
    
    def get_microphone(self, device_index: Optional[int] = None) -> sr.Microphone:
        """
        Get Microphone instance with device_index.
        
        Args:
            device_index: PortAudio device index (None = system default)
            
        Returns:
            speech_recognition.Microphone instance
        """
        if device_index is not None:
            logger.info(f"Использование устройства с индексом {device_index}")
            return sr.Microphone(device_index=device_index)
        else:
            logger.info("Использование системного устройства по умолчанию")
            return sr.Microphone()  # System default
    
    def update_device(self, device_index: Optional[int], signature: DeviceSignature):
        """
        Update current device.
        
        Args:
            device_index: PortAudio device index
            signature: DeviceSignature
        """
        self._current_device_index = device_index
        self._current_signature = signature
        logger.info(f"Устройство обновлено: {signature} (index: {device_index})")
    
    def get_current_device(self) -> tuple[Optional[int], Optional[DeviceSignature]]:
        """Get current device."""
        return self._current_device_index, self._current_signature
```

**Критерии готовности**:
- [ ] Файл создан
- [ ] Адаптер реализован
- [ ] get_microphone() работает
- [ ] update_device() работает
- [ ] Линтер проходит без ошибок

**Тесты**: `tests/test_avfoundation_adapters.py` (input часть)
- [ ] Тест get_microphone() с device_index
- [ ] Тест get_microphone() без device_index (system default)
- [ ] Тест update_device()
- [ ] Тест get_current_device()
- [ ] Покрытие ≥80%

---

## 🎯 Этап 5: Интеграция (Неделя 6)

### День 22-23: AudioRouteManagerIntegration

#### Задача 5.1: Создать `audio_route_manager_integration.py`

**Файл**: `integration/integrations/audio_route_manager_integration.py`

**Содержимое** (структура - большой файл):
```python
"""
AudioRouteManagerIntegration - интеграция RouteManager с EventBus.

Центральный координатор аудио маршрутизации.
"""

import asyncio
import logging
from typing import Optional, Dict, Any

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.core.selectors import Snapshot
from integration.core.gateways import decide_route_manager_reconcile

from modules.voice_recognition.core.avfoundation.route_manager import AudioRouteManager
from modules.voice_recognition.core.avfoundation.mapping import DeviceMapper
from modules.voice_recognition.core.avfoundation.adapters.avf_monitor import AVFoundationDeviceMonitor
from modules.voice_recognition.core.avfoundation.adapters.avf_output import AVFoundationAudioPlayback
from modules.voice_recognition.core.avfoundation.adapters.google_input import GoogleInputController

from config.unified_config_loader import UnifiedConfigLoader

logger = logging.getLogger(__name__)


class AudioRouteManagerIntegration:
    """Integration for AudioRouteManager."""
    
    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: Optional[Dict[str, Any]] = None,
        voice_recognition_integration=None,
        speech_playback_integration=None
    ):
        """
        Initialize AudioRouteManagerIntegration.
        
        Args:
            event_bus: EventBus instance
            state_manager: ApplicationStateManager instance
            error_handler: ErrorHandler instance
            config: Configuration dictionary
            voice_recognition_integration: VoiceRecognitionIntegration instance (optional)
            speech_playback_integration: SpeechPlaybackIntegration instance (optional)
        """
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.config = config or {}
        
        self.voice_recognition_integration = voice_recognition_integration
        self.speech_playback_integration = speech_playback_integration
        
        # Проверяем feature flags
        unified_config = UnifiedConfigLoader().get_all()
        audio_system_cfg = unified_config.get("audio_system", {})
        
        self.avfoundation_enabled = audio_system_cfg.get("avfoundation_enabled", False)
        self.route_manager_enabled = audio_system_cfg.get("avfoundation_route_manager_enabled", False)
        self.ks_route_manager = audio_system_cfg.get("ks_avfoundation_route_manager", False)
        
        # Components
        self.device_mapper: Optional[DeviceMapper] = None
        self.device_monitor: Optional[AVFoundationDeviceMonitor] = None
        self.route_manager: Optional[AudioRouteManager] = None
        self.avf_output: Optional[AVFoundationAudioPlayback] = None
        self.google_input: Optional[GoogleInputController] = None
        
        self._initialized = False
        self._running = False
    
    async def initialize(self) -> bool:
        """Initialize integration."""
        # Проверяем kill-switch
        if self.ks_route_manager:
            logger.warning("AudioRouteManager отключен kill-switch")
            return False
        
        # Проверяем feature flags
        if not self.avfoundation_enabled or not self.route_manager_enabled:
            logger.info("AudioRouteManager отключен feature flags")
            return False
        
        try:
            # Инициализируем компоненты
            self.device_mapper = DeviceMapper()
            
            # Инициализируем device monitor
            monitor_config = self.config.get("input_monitor", {})
            self.device_monitor = AVFoundationDeviceMonitor(
                device_mapper=self.device_mapper,
                check_interval_sec=monitor_config.get("check_interval_sec", 1.5),
                use_notifications=monitor_config.get("use_notifications", True)
            )
            
            # Инициализируем route manager
            self.route_manager = AudioRouteManager(
                device_mapper=self.device_mapper,
                get_system_devices=self.device_monitor.get_current_devices,
                config=self.config.get("route_manager", {})
            )
            
            # Устанавливаем callbacks
            self.route_manager.set_callbacks(
                on_input_start=self._on_input_start,
                on_input_stop=self._on_input_stop,
                on_output_recreate=self._on_output_recreate
            )
            
            # Инициализируем адаптеры
            self.google_input = GoogleInputController()
            
            output_config = self.config.get("output", {})
            self.avf_output = AVFoundationAudioPlayback(
                max_queue_ms=output_config.get("max_queue_ms", 5000),
                max_queue_bytes=output_config.get("max_queue_bytes", 5242880),
                sample_rate_conversion=output_config.get("sample_rate_conversion", True)
            )
            
            # Подписываемся на события
            await self.event_bus.subscribe(
                "audio.route.reconcile_requested",
                self._on_reconcile_requested,
                EventPriority.HIGH
            )
            await self.event_bus.subscribe(
                "permissions.first_run_started",
                self._on_first_run_started,
                EventPriority.CRITICAL
            )
            await self.event_bus.subscribe(
                "permissions.restart_pending",
                self._on_restart_pending,
                EventPriority.CRITICAL
            )
            await self.event_bus.subscribe(
                "app.update_in_progress",
                self._on_update_in_progress,
                EventPriority.CRITICAL
            )
            await self.event_bus.subscribe(
                "app.mode_changed",
                self._on_mode_changed,
                EventPriority.MEDIUM
            )
            
            # Запускаем мониторинг устройств
            self.device_monitor.start_monitoring(on_device_changed=self._on_device_changed)
            
            self._initialized = True
            logger.info("AudioRouteManagerIntegration инициализирован")
            return True
            
        except Exception as e:
            logger.error(f"Ошибка инициализации AudioRouteManagerIntegration: {e}")
            await self.error_handler.handle_error(
                severity="error",
                category="audio_route_manager",
                message=f"Ошибка инициализации: {e}",
                context={"where": "audio_route_manager.initialize"}
            )
            return False
    
    async def start(self) -> bool:
        """Start integration."""
        if not self._initialized:
            return False
        
        self._running = True
        
        # Инициализируем output
        if self.avf_output:
            self.avf_output.initialize()
        
        return True
    
    async def stop(self) -> bool:
        """Stop integration."""
        if self.device_monitor:
            self.device_monitor.stop_monitoring()
        
        if self.avf_output:
            self.avf_output.shutdown()
        
        self._running = False
        return True
    
    def _on_input_start(self, device_index: Optional[int], signature):
        """Callback for input start."""
        if self.google_input:
            self.google_input.update_device(device_index, signature)
        
        # Публикуем событие
        asyncio.run_coroutine_threadsafe(
            self.event_bus.publish(
                "audio.input.started",
                {
                    "device_index": device_index,
                    "signature": {
                        "normalized_name": signature.normalized_name,
                        "transport": signature.transport.value,
                        "channels": signature.channels
                    }
                }
            ),
            asyncio.get_event_loop()
        )
    
    def _on_input_stop(self):
        """Callback for input stop."""
        asyncio.run_coroutine_threadsafe(
            self.event_bus.publish("audio.input.stopped", {}),
            asyncio.get_event_loop()
        )
    
    def _on_output_recreate(self):
        """Callback for output recreate."""
        asyncio.run_coroutine_threadsafe(
            self.event_bus.publish("audio.output.recreating", {}),
            asyncio.get_event_loop()
        )
    
    async def _on_reconcile_requested(self, event):
        """Handle reconcile request."""
        if not self.route_manager:
            return
        
        # Создаем DecisionContext из state_manager
        snapshot = self._create_snapshot()
        context = self._create_decision_context(snapshot)
        
        # Вызываем reconcile
        self.route_manager.reconcile_routes(context)
    
    def _create_snapshot(self) -> Snapshot:
        """Create Snapshot from state_manager."""
        # TODO: Реализовать создание Snapshot из state_manager
        # Это требует доступа к selectors
        pass
    
    def _create_decision_context(self, snapshot: Snapshot):
        """Create DecisionContext from Snapshot."""
        from modules.voice_recognition.core.avfoundation.decision_engine import DecisionContext
        
        return DecisionContext(
            first_run=snapshot.first_run,
            restart_pending=snapshot.restart_pending,
            update_in_progress=snapshot.update_in_progress,
            device_busy=snapshot.device_input == "busy",
            network_offline=snapshot.network == "offline",
            mic_permission_granted=snapshot.perm_mic == "granted",
            app_mode=snapshot.app_mode.value
        )
    
    async def _on_device_changed(self, signature):
        """Handle device change."""
        await self.event_bus.publish(
            "audio.input.device_changed",
            {
                "signature": {
                    "normalized_name": signature.normalized_name,
                    "transport": signature.transport.value,
                    "channels": signature.channels
                }
            }
        )
        
        # Триггерим reconcile
        await self.event_bus.publish("audio.route.reconcile_requested", {})
    
    async def _on_first_run_started(self, event):
        """Handle first run started."""
        # Блокируем RouteManager
        await self.event_bus.publish("audio.route.reconcile_requested", {})
    
    async def _on_restart_pending(self, event):
        """Handle restart pending."""
        # Блокируем RouteManager
        await self.event_bus.publish("audio.route.reconcile_requested", {})
    
    async def _on_update_in_progress(self, event):
        """Handle update in progress."""
        # Блокируем RouteManager
        await self.event_bus.publish("audio.route.reconcile_requested", {})
    
    async def _on_mode_changed(self, event):
        """Handle mode change."""
        await self.event_bus.publish("audio.route.reconcile_requested", {})
    
    def get_active_input_device(self):
        """Get active input device."""
        if self.route_manager:
            return self.route_manager.get_active_input_device()
        return None
    
    def get_active_output_device(self):
        """Get active output device."""
        if self.route_manager:
            return self.route_manager.get_active_output_device()
        return None
```

**Критерии готовности**:
- [ ] Файл создан
- [ ] Интеграция реализована
- [ ] Подписки на события работают
- [ ] Публикация событий работает
- [ ] Интеграция с RouteManager работает
- [ ] Линтер проходит без ошибок

**Тесты**: `tests/integration/test_audio_route_manager.py`
- [ ] Тест initialize()
- [ ] Тест start()
- [ ] Тест stop()
- [ ] Тест _on_reconcile_requested()
- [ ] Тест _on_device_changed()
- [ ] Интеграционные тесты (happy_path, device_changed, blocking_conditions, fallback)
- [ ] Покрытие ≥80%

---

### День 24: Обновление SimpleModuleCoordinator

#### Задача 5.2: Обновить `simple_module_coordinator.py`

**Файл**: `integration/core/simple_module_coordinator.py`

**Изменения**:
1. Добавить импорт `AudioRouteManagerIntegration`
2. Добавить создание интеграции в `_create_integrations()`
3. Обновить `startup_order` (добавить `'audio_route_manager'` после `'speech_playback'`)

**Критерии готовности**:
- [ ] Файл обновлен
- [ ] RouteManager добавлен в порядок инициализации
- [ ] Зависимости проверяются (voice_recognition, speech_playback)
- [ ] Тесты порядка инициализации обновлены
- [ ] Линтер проходит без ошибок

---

## 🎯 Этап 6: Адаптация существующих (Неделя 7)

### День 25-26: VoiceRecognitionIntegration

#### Задача 6.1: Адаптировать `voice_recognition_integration.py`

**Файл**: `integration/integrations/voice_recognition_integration.py`

**Изменения**:
1. Добавить проверку feature flag `audio_system.avfoundation_route_manager_enabled`
2. Получать `device_index` от RouteManager вместо прямого использования
3. Использовать `GoogleInputController` для получения Microphone
4. Fallback на старую логику (если флаг выключен)

**Критерии готовности**:
- [ ] Файл обновлен
- [ ] RouteManager интеграция добавлена
- [ ] Fallback логика работает
- [ ] Тесты обновлены
- [ ] Линтер проходит без ошибок

---

### День 27-28: SpeechPlaybackIntegration

#### Задача 6.2: Адаптировать `speech_playback_integration.py`

**Файл**: `integration/integrations/speech_playback_integration.py`

**Изменения**:
1. Добавить проверку feature flag `audio_system.avfoundation_output_enabled`
2. Использовать `AVFoundationAudioPlayback` вместо `sounddevice.OutputStream`
3. Конвертация numpy → AVAudioPCMBuffer
4. Fallback на старую логику (если флаг выключен)

**Критерии готовности**:
- [ ] Файл обновлен
- [ ] AVFoundation output интеграция добавлена
- [ ] Fallback логика работает
- [ ] Тесты обновлены
- [ ] Линтер проходит без ошибок

---

## 🎯 Этап 7: Адаптация модулей (Неделя 8)

### День 29-30: SpeechRecognizer

#### Задача 7.1: Адаптировать `speech_recognizer.py`

**Файл**: `modules/voice_recognition/core/speech_recognizer.py`

**Изменения**:
1. Получать `device_index` от RouteManager вместо `AudioDeviceMonitor`
2. Убрать прямые вызовы `sd.default.device`
3. Использовать `GoogleInputController` для получения Microphone

**Критерии готовности**:
- [ ] Файл обновлен
- [ ] RouteManager интеграция добавлена
- [ ] Старая логика удалена/закомментирована
- [ ] Тесты обновлены
- [ ] Линтер проходит без ошибок

---

### День 31-32: SequentialSpeechPlayer

#### Задача 7.2: Адаптировать `player.py`

**Файл**: `modules/speech_playback/core/player.py`

**Изменения**:
1. Использовать `AVFoundationAudioPlayback` вместо `sounddevice.OutputStream`
2. Конвертация форматов
3. Fallback на старую логику (если флаг выключен)

**Критерии готовности**:
- [ ] Файл обновлен
- [ ] AVFoundation output интеграция добавлена
- [ ] Fallback логика работает
- [ ] Тесты обновлены
- [ ] Линтер проходит без ошибок

---

## 🎯 Этап 8: Gateways и State Catalog (Неделя 9)

### День 33-34: Gateways

#### Задача 8.1: Обновить `gateways.py`

**Файл**: `integration/core/gateways.py`

**Изменения**:
1. Добавить функцию `decide_route_manager_reconcile(snapshot: Snapshot) -> Decision`
2. Реализовать правила из `interaction_matrix.yaml`
3. Канонический формат decision-логов

**Критерии готовности**:
- [ ] Файл обновлен
- [ ] Gateway функция реализована
- [ ] Тесты созданы (≥12 pairwise + 2 негативных)
- [ ] Decision-логи в каноническом формате
- [ ] Линтер проходит без ошибок

---

### День 35: State Catalog

#### Задача 8.2: Обновить `STATE_CATALOG.md`

**Файл**: `Docs/STATE_CATALOG.md`

**Изменения**:
1. Добавить оси `audio.input.device` и `audio.output.device`
2. Обновить таблицу ownership
3. Обновить метрики

**Критерии готовности**:
- [ ] Файл обновлен
- [ ] Оси добавлены
- [ ] Таблица ownership обновлена
- [ ] Метрики обновлены

---

## 🎯 Этап 9: Тестирование и документация (Неделя 10)

### День 36-40: Интеграционное тестирование

#### Задача 9.1: Создать интеграционные тесты

**Файл**: `tests/integration/test_audio_route_manager.py`

**Сценарии**:
- [ ] Happy path: нормальный цикл работы
- [ ] Device changed: смена устройства
- [ ] Blocking conditions: first_run, restart_pending, update_in_progress
- [ ] Fallback: недоступность AVFoundation
- [ ] Mapping failures: LOW/NONE confidence
- [ ] Network offline: degrade режим
- [ ] Device busy: retry с backoff

**Критерии готовности**:
- [ ] Тесты созданы
- [ ] Все сценарии покрыты
- [ ] Метрики проверяются
- [ ] Decision-логи проверяются

---

### День 41-42: Документация

#### Задача 9.2: Обновить документацию

**Файлы**:
- [ ] `modules/voice_recognition/core/avfoundation/README.md`
- [ ] `Docs/AUDIO_SYSTEM_ARCHITECTURE.md`
- [ ] `modules/voice_recognition/INTEGRATION_GUIDE.md`
- [ ] `modules/speech_playback/INTEGRATION_GUIDE.md`

**Критерии готовности**:
- [ ] Документация обновлена
- [ ] Примеры добавлены
- [ ] API документирован

---

## 📋 Итоговый чек-лист

### Подготовка (выполнено ✅)
- [x] Feature flags созданы и зарегистрированы
- [x] Конфигурация добавлена
- [x] Правила добавлены
- [x] Метрики добавлены
- [x] ADR создан
- [x] Change Impact создан
- [x] Структура создана

### Реализация (0%)
- [ ] Этап 1: Базовые компоненты (0%)
- [ ] Этап 2: State Machines (0%)
- [ ] Этап 3: Route Manager Core (0%)
- [ ] Этап 4: Адаптеры (0%)
- [ ] Этап 5: Интеграция (0%)
- [ ] Этап 6: Адаптация существующих (0%)
- [ ] Этап 7: Адаптация модулей (0%)
- [ ] Этап 8: Gateways и State Catalog (0%)
- [ ] Этап 9: Тестирование и документация (0%)

---

## 🚀 Начало реализации

**Команды для начала**:
```bash
cd /Users/sergiyzasorin/Fix_new/client

# Проверить готовность
scripts/prepare_audio_migration.sh

# Проверить соответствие требованиям
python3 scripts/verify_audio_migration_compliance.py

# Создать ветку
git checkout -b feature/avfoundation-audio-migration

# Начать с Этапа 1, День 1-2: contracts.py
```

---

**Этот план содержит все детали для полной реализации аудиосистемы на AVFoundation.**

