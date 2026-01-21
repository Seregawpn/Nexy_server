"""
Улучшенный кэш устройств с TTL (Time To Live)

Улучшения по сравнению с baseline:
- TTL для записей кэша
- Метаданные о времени обновления
- Автоматическая инвалидация при истечении TTL
- Логирование состояния кэша
"""

import logging
import time
from typing import Dict, Optional, Any
from dataclasses import dataclass
import sounddevice as sd

logger = logging.getLogger(__name__)


@dataclass
class CacheEntry:
    """Запись в кэше с метаданными"""
    device_id: int
    timestamp: float  # Время создания записи
    device_name: str
    sample_rate: Optional[int] = None
    channels: Optional[int] = None


class DeviceCacheWithTTL:
    """
    Кэш устройств с TTL и метаданными
    
    Улучшения:
    - TTL для каждой записи
    - Метаданные о времени обновления
    - Автоматическая инвалидация при истечении TTL
    - Хранение параметров устройства (частота, каналы)
    """
    
    def __init__(self, ttl_seconds: float = 5.0):
        """
        Инициализация кэша
        
        Args:
            ttl_seconds: Время жизни записей в секундах (по умолчанию 5 сек)
        """
        self.ttl_seconds = ttl_seconds
        self._cache: Dict[str, CacheEntry] = {}  # name → CacheEntry
        self._last_update_time: Optional[float] = None
        self._cache_valid: bool = False
        
        logger.info(f"🔧 DeviceCacheWithTTL создан (TTL: {ttl_seconds}с)")
    
    def invalidate(self):
        """Пометить кэш как невалидный"""
        logger.debug("🔍 [CACHE] Кэш помечен как невалидный")
        self._cache_valid = False
        self._cache.clear()
        self._last_update_time = None
    
    def is_valid(self) -> bool:
        """Проверить валидность кэша"""
        if not self._cache_valid:
            return False
        
        # Проверяем TTL
        if self._last_update_time is None:
            return False
        
        elapsed = time.time() - self._last_update_time
        if elapsed > self.ttl_seconds:
            logger.debug(f"🔍 [CACHE] TTL истёк ({elapsed:.2f}с > {self.ttl_seconds}с)")
            return False
        
        return True
    
    def refresh(self):
        """Обновить кэш из PortAudio"""
        logger.debug("🔍 [CACHE] Обновление кэша...")
        
        try:
            devices = sd.query_devices()
            self._cache.clear()
            
            for idx, dev in enumerate(devices):
                if dev.get('max_input_channels', 0) > 0:
                    name = dev.get('name', '')
                    if name:
                        sample_rate = dev.get('default_samplerate', 0)
                        channels = dev.get('max_input_channels', 0)
                        
                        entry = CacheEntry(
                            device_id=idx,
                            timestamp=time.time(),
                            device_name=name,
                            sample_rate=int(sample_rate) if sample_rate > 0 else None,
                            channels=int(channels) if channels > 0 else None
                        )
                        
                        # Сохраняем по имени
                        self._cache[name] = entry
                        logger.debug(f"🔍 [CACHE] Добавлено: \"{name}\" → ID {idx}")
            
            self._last_update_time = time.time()
            self._cache_valid = True
            
            logger.info(f"✅ [CACHE] Кэш обновлён: {len(self._cache)} записей")
            
        except Exception as e:
            logger.error(f"❌ [CACHE] Ошибка обновления кэша: {e}")
            self._cache_valid = False
    
    def get(self, device_name: str, auto_refresh: bool = True) -> Optional[CacheEntry]:
        """
        Получить запись из кэша
        
        Args:
            device_name: Имя устройства
            auto_refresh: Автоматически обновлять кэш если невалиден (по умолчанию True)
            
        Returns:
            CacheEntry или None если не найдено или истёк TTL
        """
        # Проверяем валидность кэша
        if not self.is_valid():
            if auto_refresh:
                logger.debug("🔍 [CACHE] Кэш невалиден, обновляем...")
                self.refresh()
            else:
                logger.debug("🔍 [CACHE] Кэш невалиден, но auto_refresh=False")
                return None
        
        # Ищем в кэше
        entry = self._cache.get(device_name)
        if entry:
            # Проверяем TTL записи
            elapsed = time.time() - entry.timestamp
            if elapsed > self.ttl_seconds:
                logger.debug(f"🔍 [CACHE] Запись для \"{device_name}\" истекла ({elapsed:.2f}с > {self.ttl_seconds}с)")
                # Удаляем истёкшую запись
                del self._cache[device_name]
                return None
            
            logger.debug(f"✅ [CACHE] Найдено в кэше: \"{device_name}\" → ID {entry.device_id}")
            return entry
        
        logger.debug(f"⚠️ [CACHE] Не найдено в кэше: \"{device_name}\"")
        return None
    
    def put(self, device_name: str, device_id: int, 
            sample_rate: Optional[int] = None, channels: Optional[int] = None):
        """
        Добавить запись в кэш
        
        Args:
            device_name: Имя устройства
            device_id: ID устройства
            sample_rate: Частота (опционально)
            channels: Количество каналов (опционально)
        """
        entry = CacheEntry(
            device_id=device_id,
            timestamp=time.time(),
            device_name=device_name,
            sample_rate=sample_rate,
            channels=channels
        )
        
        self._cache[device_name] = entry
        self._cache_valid = True
        if self._last_update_time is None:
            self._last_update_time = time.time()
        
        logger.debug(f"✅ [CACHE] Добавлено в кэш: \"{device_name}\" → ID {device_id}")
    
    def get_stats(self) -> Dict[str, Any]:
        """Получить статистику кэша"""
        now = time.time()
        valid_entries = 0
        expired_entries = 0
        
        for entry in self._cache.values():
            elapsed = now - entry.timestamp
            if elapsed <= self.ttl_seconds:
                valid_entries += 1
            else:
                expired_entries += 1
        
        return {
            'total_entries': len(self._cache),
            'valid_entries': valid_entries,
            'expired_entries': expired_entries,
            'cache_valid': self._cache_valid,
            'last_update_time': self._last_update_time,
            'ttl_seconds': self.ttl_seconds
        }

