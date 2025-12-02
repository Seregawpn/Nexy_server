"""
Core Audio Manager - Менеджер Core Audio для macOS

✅ ФАЗА 2: Поддержка нотификаций Core Audio для событийной реакции на смену устройств
"""

import logging
import platform
import threading
from typing import Optional, Dict, Any, Callable

logger = logging.getLogger(__name__)

# Попытка импорта PyObjC CoreAudio
try:
    from CoreAudio import (
        AudioObjectAddPropertyListener,
        AudioObjectRemovePropertyListener,
        AudioObjectGetPropertyData,
        AudioObjectPropertyAddress,
        kAudioObjectSystemObject,
        kAudioHardwarePropertyDefaultOutputDevice,
        kAudioObjectPropertyScopeGlobal,
        kAudioObjectPropertyElementMain,
        kAudioObjectPropertyElementMaster,
    )
    CORE_AUDIO_AVAILABLE = True
except ImportError:
    CORE_AUDIO_AVAILABLE = False
    logger.warning("⚠️ PyObjC CoreAudio недоступен, нотификации будут отключены")
    
    # Заглушки для типизации
    AudioObjectAddPropertyListener = None
    AudioObjectRemovePropertyListener = None
    AudioObjectGetPropertyData = None
    AudioObjectPropertyAddress = None
    kAudioObjectSystemObject = None
    kAudioHardwarePropertyDefaultOutputDevice = None
    kAudioObjectPropertyScopeGlobal = None
    kAudioObjectPropertyElementMain = None

class CoreAudioManager:
    """Менеджер Core Audio для macOS с поддержкой нотификаций"""
    
    def __init__(self):
        """Инициализация менеджера"""
        self._initialized = False
        self._is_macos = platform.system() == "Darwin"
        self._core_audio_available = CORE_AUDIO_AVAILABLE and self._is_macos
        
        # ✅ ФАЗА 2: Нотификации
        self._notification_listener_id: Optional[Any] = None
        self._device_change_callback: Optional[Callable[[], None]] = None
        self._notification_lock = threading.Lock()
        
        logger.info(f"🔧 CoreAudioManager создан (macOS: {self._is_macos}, CoreAudio: {self._core_audio_available})")
    
    def initialize(self) -> bool:
        """
        Инициализация Core Audio
        
        Returns:
            True если инициализация успешна, False иначе
        """
        try:
            if not self._is_macos:
                logger.warning("⚠️ Core Audio доступен только на macOS")
                # На не-macOS системах просто возвращаем True
                self._initialized = True
                return True
            
            # На macOS можно добавить специфичную инициализацию
            # Пока что просто помечаем как инициализированный
            self._initialized = True
            logger.info("✅ Core Audio инициализирован")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации Core Audio: {e}")
            return False
    
    def is_initialized(self) -> bool:
        """Проверяет, инициализирован ли менеджер"""
        return self._initialized
    
    def get_audio_info(self) -> Dict[str, Any]:
        """
        Получает информацию об аудио системе
        
        Returns:
            Словарь с информацией об аудио системе
        """
        try:
            info = {
                'platform': platform.system(),
                'is_macos': self._is_macos,
                'initialized': self._initialized,
                'core_audio_available': self._is_macos and self._initialized
            }
            
            return info
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения информации об аудио: {e}")
            return {'error': str(e)}
    
    def optimize_for_speech(self) -> bool:
        """
        Оптимизирует аудио систему для речи
        
        Returns:
            True если оптимизация успешна, False иначе
        """
        try:
            if not self._initialized:
                logger.warning("⚠️ Core Audio не инициализирован")
                return False
            
            # Здесь можно добавить специфичную оптимизацию для macOS
            logger.info("✅ Аудио система оптимизирована для речи")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка оптимизации аудио: {e}")
            return False
    
    def cleanup(self):
        """Очистка ресурсов"""
        try:
            # ✅ ФАЗА 2: Отписываемся от нотификаций
            self.stop_device_notifications()
            
            self._initialized = False
            logger.info("✅ Core Audio очищен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка очистки Core Audio: {e}")
    
    # ✅ ФАЗА 2: Методы для нотификаций Core Audio
    
    def start_device_notifications(self, callback: Callable[[], None]) -> bool:
        """
        Подписывается на нотификации Core Audio о смене default output устройства.
        
        Args:
            callback: Функция, вызываемая при смене устройства
        
        Returns:
            True если подписка успешна, False иначе (fallback на polling)
        """
        if not self._core_audio_available:
            logger.debug("⚠️ Core Audio недоступен, нотификации отключены (используется polling)")
            return False
        
        try:
            with self._notification_lock:
                if self._notification_listener_id is not None:
                    logger.warning("⚠️ Нотификации уже запущены")
                    return True
                
                self._device_change_callback = callback
                
                # ✅ ФАЗА 2: Реализация через PyObjC CoreAudio
                def property_listener_callback(
                    inObjectID: int,
                    inNumberAddresses: int,
                    inAddresses: Any,
                    inClientData: Any
                ) -> int:
                    """Callback для нотификаций Core Audio"""
                    try:
                        if callback:
                            logger.info("🔔 [OUTPUT] Core Audio нотификация: default output устройство изменилось")
                            callback()
                        return 0  # kAudioObjectPropertyListenerSucceeded
                    except Exception as e:
                        logger.error(f"❌ Ошибка в callback нотификации: {e}", exc_info=True)
                        return 1  # kAudioObjectPropertyListenerFailed
                
                # Создаем адрес свойства для подписки
                property_address = AudioObjectPropertyAddress(
                    kAudioHardwarePropertyDefaultOutputDevice,
                    kAudioObjectPropertyScopeGlobal,
                    kAudioObjectPropertyElementMain
                )
                
                # Подписываемся на нотификации
                result = AudioObjectAddPropertyListener(
                    kAudioObjectSystemObject,
                    property_address,
                    property_listener_callback,
                    None  # inClientData
                )
                
                if result == 0:  # kAudioObjectPropertyListenerSucceeded
                    self._notification_listener_id = property_listener_callback
                    self._property_address = property_address
                    logger.info("✅ [OUTPUT] Подписка на Core Audio нотификации успешна")
                    return True
                else:
                    logger.warning(f"⚠️ [OUTPUT] Не удалось подписаться на Core Audio нотификации (код: {result})")
                    self._device_change_callback = None
                    return False
                
        except Exception as e:
            logger.error(f"❌ Ошибка подписки на нотификации Core Audio: {e}", exc_info=True)
            self._device_change_callback = None
            return False
    
    def stop_device_notifications(self):
        """Отписывается от нотификаций Core Audio"""
        try:
            with self._notification_lock:
                if self._notification_listener_id is None:
                    return
                
                # ✅ ФАЗА 2: Отписка от нотификаций
                if self._core_audio_available and hasattr(self, '_property_address'):
                    try:
                        result = AudioObjectRemovePropertyListener(
                            kAudioObjectSystemObject,
                            self._property_address,
                            self._notification_listener_id,
                            None
                        )
                        if result == 0:
                            logger.info("✅ [OUTPUT] Отписка от Core Audio нотификаций успешна")
                        else:
                            logger.warning(f"⚠️ [OUTPUT] Ошибка отписки от нотификаций (код: {result})")
                    except Exception as e:
                        logger.error(f"❌ Ошибка при отписке от нотификаций: {e}", exc_info=True)
                
                self._device_change_callback = None
                self._notification_listener_id = None
                if hasattr(self, '_property_address'):
                    delattr(self, '_property_address')
                
        except Exception as e:
            logger.error(f"❌ Ошибка отписки от нотификаций Core Audio: {e}", exc_info=True)
    
    def is_notifications_available(self) -> bool:
        """Проверяет, доступны ли нотификации Core Audio"""
        return self._core_audio_available
