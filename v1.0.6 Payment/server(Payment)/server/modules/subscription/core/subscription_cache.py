#!/usr/bin/env python3
"""
Subscription Cache - кэширование контекста подписки

Feature ID: F-2025-017-stripe-payment
Оптимизация производительности
"""
import logging
from typing import Dict, Optional
from datetime import datetime, timedelta
from threading import Lock

logger = logging.getLogger(__name__)


class SubscriptionCache:
    """
    Кэш для контекста подписки
    
    TTL: 30 секунд
    Автоматическая инвалидация при изменениях
    """
    
    TTL_SECONDS = 30
    
    def __init__(self):
        """Инициализация кэша"""
        self._cache: Dict[str, Dict] = {}
        self._lock = Lock()
        logger.info("[SubscriptionCache] Initialized")
    
    def get(self, hardware_id: str) -> Optional[Dict]:
        """
        Получить контекст подписки из кэша
        
        Args:
            hardware_id: ID устройства
        
        Returns:
            Dict с контекстом подписки или None, если кэш истек/не найден
        """
        with self._lock:
            if hardware_id not in self._cache:
                return None
            
            cached_data = self._cache[hardware_id]
            cached_at = cached_data.get('cached_at')
            
            if not cached_at:
                # Некорректные данные в кэше
                del self._cache[hardware_id]
                return None
            
            # Проверяем TTL
            if isinstance(cached_at, datetime):
                age = (datetime.now() - cached_at).total_seconds()
            else:
                # Если это timestamp
                age = (datetime.now() - datetime.fromtimestamp(cached_at)).total_seconds()
            
            if age > self.TTL_SECONDS:
                # Кэш истек
                del self._cache[hardware_id]
                logger.debug(f"[SubscriptionCache] Cache expired for {hardware_id[:8]}... (age={age:.1f}s)")
                return None
            
            logger.debug(f"[SubscriptionCache] Cache hit for {hardware_id[:8]}... (age={age:.1f}s)")
            return cached_data.get('context')
    
    def set(self, hardware_id: str, context: Dict):
        """
        Сохранить контекст подписки в кэш
        
        Args:
            hardware_id: ID устройства
            context: Контекст подписки
        """
        with self._lock:
            self._cache[hardware_id] = {
                'context': context,
                'cached_at': datetime.now()
            }
            logger.debug(f"[SubscriptionCache] Cache set for {hardware_id[:8]}...")
    
    def invalidate(self, hardware_id: str):
        """
        Инвалидировать кэш для конкретного hardware_id
        
        Args:
            hardware_id: ID устройства
        """
        with self._lock:
            if hardware_id in self._cache:
                del self._cache[hardware_id]
                logger.debug(f"[SubscriptionCache] Cache invalidated for {hardware_id[:8]}...")
    
    def invalidate_all(self):
        """Инвалидировать весь кэш"""
        with self._lock:
            count = len(self._cache)
            self._cache.clear()
            logger.info(f"[SubscriptionCache] Cache invalidated (cleared {count} entries)")
    
    def clear_expired(self):
        """Очистить истекшие записи из кэша"""
        with self._lock:
            now = datetime.now()
            expired = []
            
            for hardware_id, cached_data in self._cache.items():
                cached_at = cached_data.get('cached_at')
                if not cached_at:
                    expired.append(hardware_id)
                    continue
                
                if isinstance(cached_at, datetime):
                    age = (now - cached_at).total_seconds()
                else:
                    age = (now - datetime.fromtimestamp(cached_at)).total_seconds()
                
                if age > self.TTL_SECONDS:
                    expired.append(hardware_id)
            
            for hardware_id in expired:
                del self._cache[hardware_id]
            
            if expired:
                logger.debug(f"[SubscriptionCache] Cleared {len(expired)} expired entries")
    
    def get_stats(self) -> Dict:
        """
        Получить статистику кэша
        
        Returns:
            Dict со статистикой
        """
        with self._lock:
            return {
                'total_entries': len(self._cache),
                'ttl_seconds': self.TTL_SECONDS
            }

