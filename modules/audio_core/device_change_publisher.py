"""
DeviceChangePublisher - Единый монитор устройств

Отвечает за публикацию событий device.default_input_changed /
device.default_output_changed и ведёт кэш текущих устройств.
"""

import asyncio
import logging
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Any, Dict

from integration.core.event_bus import EventBus, EventPriority

logger = logging.getLogger(__name__)


class DeviceChangeSource(str, Enum):
    """Источник события смены устройства"""
    CORE_AUDIO = "core_audio"
    POLLING = "polling"
    UNKNOWN = "unknown"

    @classmethod
    def from_str(cls, value: Optional[str]) -> "DeviceChangeSource":
        if not value:
            return cls.UNKNOWN
        normalized = value.strip().lower()
        for member in cls:
            if member.value == normalized:
                return member
        return cls.UNKNOWN


@dataclass
class DeviceInfo:
    """Информация об устройстве"""
    name: str
    device_id: Optional[int]
    is_bluetooth: bool
    source: DeviceChangeSource = DeviceChangeSource.UNKNOWN
    timestamp: float = field(default_factory=time.time)


try:
    from modules.audio_core import (
        CoreAudioDeviceBus,
        DeviceStateCache,
        CoreAudioDeviceManager,
        DevicePollingWatcher,
    )
    AUDIO_CORE_AVAILABLE = True
except ImportError as exc:
    CoreAudioDeviceBus = None
    DeviceStateCache = None
    CoreAudioDeviceManager = None
    DevicePollingWatcher = None
    AUDIO_CORE_AVAILABLE = False
    logger.warning(f"⚠️ DeviceChangePublisher: AudioCore components unavailable ({exc})")


class DeviceChangePublisher:
    """Публикует события смены default устройств INPUT/OUTPUT"""

    def __init__(self, event_bus: EventBus, core_integration: Optional[Any] = None):
        self.event_bus = event_bus
        self._core_integration = core_integration

        self._bus = None
        self._cache = None
        self._manager = None
        self._polling_watcher = None
        self._owns_manager = False

        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._input_debounce_handle: Optional[asyncio.TimerHandle] = None
        self._output_debounce_handle: Optional[asyncio.TimerHandle] = None

        self._monitoring_input = False
        self._monitoring_output = False
        self._initialized = False

        self._current_input_device: Optional[DeviceInfo] = None
        self._current_output_device: Optional[DeviceInfo] = None
        self._debounce_delay = 0.3

        logger.info("DeviceChangePublisher создан")

    async def initialize(self) -> bool:
        """Инициализация компонента"""
        try:
            if self._core_integration:
                manager = getattr(self._core_integration, "get_device_manager", None)
                cache = getattr(self._core_integration, "get_device_cache", None)
                self._manager = manager() if manager else None
                self._cache = cache() if cache else None
                if self._manager is None:
                    logger.warning("⚠️ DeviceChangePublisher: core integration не предоставила manager")
                else:
                    logger.info("✅ DeviceChangePublisher использует CoreAudioIntegration manager")
            if self._manager is None:
                if not AUDIO_CORE_AVAILABLE or not CoreAudioDeviceBus:
                    logger.warning("⚠️ У AudioCore нет необходимых компонентов, DeviceChangePublisher ограничен")
                    return False
                self._bus = CoreAudioDeviceBus()
                self._cache = DeviceStateCache()
                self._manager = CoreAudioDeviceManager(
                    bus=self._bus,
                    cache=self._cache,
                    event_bus=self.event_bus
                )
                self._polling_watcher = DevicePollingWatcher(
                    bus=self._bus,
                    cache=self._cache,
                    manager=self._manager,
                )
                self._manager.set_polling_watcher(self._polling_watcher)
                self._owns_manager = True
                logger.info("✅ DeviceChangePublisher инициализировал собственный CoreAudioManager")

            self._loop = asyncio.get_event_loop()
            await self._subscribe_event_handlers()
            self._initialized = True
            logger.info("✅ DeviceChangePublisher инициализирован")
            return True
        except Exception as exc:
            logger.error(f"❌ Ошибка инициализации DeviceChangePublisher: {exc}", exc_info=True)
            return False

    async def _subscribe_event_handlers(self):
        await self.event_bus.subscribe(
            "device.default_input_changed",
            self._on_input_changed,
            EventPriority.MEDIUM
        )
        await self.event_bus.subscribe(
            "device.default_output_changed",
            self._on_output_changed,
            EventPriority.MEDIUM
        )

    async def start_monitoring(self, monitor_input: bool = True, monitor_output: bool = True) -> bool:
        """Запуск мониторинга устройств"""
        if not self._initialized or not self._manager:
            logger.warning("⚠️ DeviceChangePublisher не инициализирован")
            return False

        if self._owns_manager:
            success = self._manager.start_monitoring(monitor_input, monitor_output)
        else:
            success = True

        self._monitoring_input = monitor_input
        self._monitoring_output = monitor_output
        logger.info(f"✅ DeviceChangePublisher.monitoring -> input={monitor_input}, output={monitor_output}")
        return success

    async def stop_monitoring(self) -> bool:
        """Остановка мониторинга"""
        if self._manager and self._owns_manager:
            self._manager.stop_monitoring()
        if self._polling_watcher:
            self._polling_watcher.stop()
        if self._bus:
            try:
                self._bus.cleanup()
            except Exception:
                pass
        self._monitoring_input = False
        self._monitoring_output = False
        self._cancel_debounce("input")
        self._cancel_debounce("output")
        logger.info("✅ DeviceChangePublisher остановлен")
        return True

    def get_current_input_device(self) -> Optional[DeviceInfo]:
        return self._current_input_device

    def get_current_output_device(self) -> Optional[DeviceInfo]:
        return self._current_output_device

    def is_core_audio_available(self) -> bool:
        return AUDIO_CORE_AVAILABLE

    async def _on_input_changed(self, event: Dict[str, Any]):
        data = (event or {}).get("data", event)
        device = self._build_device_info(data)
        self._handle_device_change("input", device)

    async def _on_output_changed(self, event: Dict[str, Any]):
        data = (event or {}).get("data", event)
        device = self._build_device_info(data)
        self._handle_device_change("output", device)

    def _build_device_info(self, data: Dict[str, Any]) -> DeviceInfo:
        source = DeviceChangeSource.from_str(data.get("source"))
        return DeviceInfo(
            name=data.get("device_name", "Unknown"),
            device_id=data.get("device_id"),
            is_bluetooth=bool(data.get("is_bluetooth", False)),
            source=source
        )

    def _handle_device_change(self, direction: str, device: DeviceInfo):
        handle_attr = "_input_debounce_handle" if direction == "input" else "_output_debounce_handle"
        self._cancel_debounce(direction)
        if not self._loop:
            try:
                self._loop = asyncio.get_event_loop()
            except RuntimeError:
                self._loop = asyncio.new_event_loop()
                asyncio.set_event_loop(self._loop)

        handle = self._loop.call_later(self._debounce_delay, self._apply_device_change, direction, device)
        setattr(self, handle_attr, handle)
        logger.debug(f"⏳ DeviceChangePublisher: debounce scheduled for {direction} -> {device.name}")

    def _apply_device_change(self, direction: str, device: DeviceInfo):
        if direction == "input":
            self._current_input_device = device
        else:
            self._current_output_device = device
        logger.info(f"🔔 DeviceChangePublisher: {direction} updated to \"{device.name}\" (id={device.device_id})")
        attr = "_input_debounce_handle" if direction == "input" else "_output_debounce_handle"
        setattr(self, attr, None)

    def _cancel_debounce(self, direction: str):
        handle = self._input_debounce_handle if direction == "input" else self._output_debounce_handle
        if handle:
            handle.cancel()
            setattr(self, "_input_debounce_handle" if direction == "input" else "_output_debounce_handle", None)
