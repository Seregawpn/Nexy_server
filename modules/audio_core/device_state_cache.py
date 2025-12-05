"""
DeviceStateCache - Кэш состояний устройств

Защищённый Lock + два DeviceDescriptor для input и output.
"""

import logging
import threading
from typing import Optional
from .types import DeviceDescriptor

logger = logging.getLogger(__name__)


class DeviceStateCache:
    """Кэш состояний устройств с thread-safe доступом"""
    
    def __init__(self):
        """Инициализация кэша"""
        self._lock = threading.Lock()
        self._input: Optional[DeviceDescriptor] = None
        self._output: Optional[DeviceDescriptor] = None
        
        logger.debug("DeviceStateCache создан")
    
    def update_default_input(self, desc: DeviceDescriptor) -> DeviceDescriptor:
        """
        Обновляет дефолтное INPUT устройство
        
        Args:
            desc: Дескриптор устройства
            
        Returns:
            Обновлённый дескриптор
        """
        with self._lock:
            old = self._input
            self._input = desc
            if old:
                logger.debug(f"INPUT устройство обновлено: {old.name} -> {desc.name}")
            else:
                logger.debug(f"INPUT устройство установлено: {desc.name}")
            return desc
    
    def update_default_output(self, desc: DeviceDescriptor) -> DeviceDescriptor:
        """
        Обновляет дефолтное OUTPUT устройство
        
        Args:
            desc: Дескриптор устройства
            
        Returns:
            Обновлённый дескриптор
        """
        with self._lock:
            old = self._output
            self._output = desc
            if old:
                logger.info(f"🔄 [CACHE] OUTPUT устройство обновлено: {old.name} -> {desc.name} (uid: {old.uid} -> {desc.uid})")
            else:
                logger.info(f"✅ [CACHE] OUTPUT устройство установлено: {desc.name} (uid: {desc.uid}, device_id: {desc.device_id})")
            return desc
    
    def get_default_input(self) -> DeviceDescriptor:
        """
        Получает дефолтное INPUT устройство
        
        Returns:
            Дескриптор устройства
            
        Raises:
            RuntimeError: Если устройство не инициализировано
        """
        with self._lock:
            if self._input is None:
                raise RuntimeError("Default input device is not initialized")
            return self._input
    
    def get_default_output(self) -> DeviceDescriptor:
        """
        Получает дефолтное OUTPUT устройство
        
        Returns:
            Дескриптор устройства
            
        Raises:
            RuntimeError: Если устройство не инициализировано
        """
        with self._lock:
            if self._output is None:
                # ✅ ДИАГНОСТИКА: Логируем, что кэш пуст
                logger.warning("⚠️ [CACHE] get_default_output: кэш пуст (self._output is None)")
                raise RuntimeError("Default output device is not initialized")
            # ✅ ДИАГНОСТИКА: Логируем успешное получение устройства из кэша
            logger.debug(
                f"✅ [CACHE] get_default_output: получено устройство \"{self._output.name}\" "
                f"(uid: {self._output.uid}, device_id: {self._output.device_id})"
            )
            return self._output
    
    def has_input(self) -> bool:
        """Проверяет, есть ли INPUT устройство в кэше"""
        with self._lock:
            return self._input is not None
    
    def has_output(self) -> bool:
        """Проверяет, есть ли OUTPUT устройство в кэше"""
        with self._lock:
            return self._output is not None


