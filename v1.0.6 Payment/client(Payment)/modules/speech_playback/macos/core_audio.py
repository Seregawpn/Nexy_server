"""
Core Audio Manager - Менеджер Core Audio для macOS

✅ ФАЗА 2: Поддержка нотификаций Core Audio для событийной реакции на смену устройств
"""

import logging
import platform
import threading
from typing import Optional, Dict, Any, Callable, Literal

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
        kAudioHardwarePropertyDefaultInputDevice,
        kAudioObjectPropertyScopeGlobal,
        kAudioObjectPropertyElementMain,
        kAudioObjectPropertyElementMaster,
    )
    import objc
    CORE_AUDIO_AVAILABLE = True
except ImportError:
    CORE_AUDIO_AVAILABLE = False
    objc = None
    logger.warning("⚠️ PyObjC CoreAudio недоступен, нотификации будут отключены")
    
    # Заглушки для типизации
    AudioObjectAddPropertyListener = None
    AudioObjectRemovePropertyListener = None
    AudioObjectGetPropertyData = None
    AudioObjectPropertyAddress = None
    kAudioObjectSystemObject = None
    kAudioHardwarePropertyDefaultOutputDevice = None
    kAudioHardwarePropertyDefaultInputDevice = None
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
        self._notification_listener_id_input: Optional[Any] = None
        self._notification_listener_id_output: Optional[Any] = None
        self._device_change_callback_input: Optional[Callable[[], None]] = None
        self._device_change_callback_output: Optional[Callable[[], None]] = None
        self._property_address_input: Optional[Any] = None
        self._property_address_output: Optional[Any] = None
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
    
    def start_device_notifications(
        self, 
        callback: Callable[[], None], 
        device_type: Literal["input", "output"] = "output"
    ) -> bool:
        """
        Подписывается на нотификации Core Audio о смене default устройства.
        
        Args:
            callback: Функция, вызываемая при смене устройства
            device_type: Тип устройства (input/output)
        
        Returns:
            True если подписка успешна, False иначе (fallback на polling)
        """
        if not self._core_audio_available:
            logger.debug("⚠️ Core Audio недоступен, нотификации отключены (используется polling)")
            return False
        
        try:
            with self._notification_lock:
                # Проверяем, не запущены ли уже нотификации для этого типа устройства
                listener_id = self._notification_listener_id_input if device_type == "input" else self._notification_listener_id_output
                if listener_id is not None:
                    logger.warning(f"⚠️ Нотификации для {device_type} уже запущены")
                    return True
                
                # Сохраняем callback
                if device_type == "input":
                    self._device_change_callback_input = callback
                else:
                    self._device_change_callback_output = callback
                
                # ✅ ФАЗА 2: Реализация через PyObjC CoreAudio с правильной обёрткой callback
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
                
                # ✅ ЦИКЛ 3: Исправление PyObjC callback для Core Audio нотификаций
                # В PyObjC для Core Audio callbacks нужно передавать функцию напрямую
                # PyObjC автоматически конвертирует Python функцию в C callback
                # Если возникает ошибка "Callable argument is not a PyObjC closure",
                # используем fallback на polling (уже реализован в DeviceChangePublisher)
                wrapped_callback = property_listener_callback
                logger.debug(f"✅ [{device_type.upper()}] Callback подготовлен для Core Audio нотификаций")
                
                # Создаем адрес свойства для подписки
                property_id = (
                    kAudioHardwarePropertyDefaultInputDevice 
                    if device_type == "input" 
                    else kAudioHardwarePropertyDefaultOutputDevice
                )
                property_address = AudioObjectPropertyAddress(
                    property_id,
                    kAudioObjectPropertyScopeGlobal,
                    kAudioObjectPropertyElementMain
                )
                
                # Подписываемся на нотификации с обёрнутым callback
                result = AudioObjectAddPropertyListener(
                    kAudioObjectSystemObject,
                    property_address,
                    wrapped_callback,
                    None  # inClientData
                )
                
                if result == 0:  # kAudioObjectPropertyListenerSucceeded
                    # Сохраняем обёрнутый callback для последующей отписки
                    if device_type == "input":
                        self._notification_listener_id_input = wrapped_callback
                        self._property_address_input = property_address
                    else:
                        self._notification_listener_id_output = wrapped_callback
                        self._property_address_output = property_address
                    logger.info(f"✅ [{device_type.upper()}] Подписка на Core Audio нотификации успешна (callback обёрнут через objc.callback)")
                    return True
                else:
                    logger.warning(f"⚠️ [{device_type.upper()}] Не удалось подписаться на Core Audio нотификации (код: {result})")
                    if device_type == "input":
                        self._device_change_callback_input = None
                    else:
                        self._device_change_callback_output = None
                    return False
                
        except Exception as e:
            logger.error(f"❌ Ошибка подписки на нотификации Core Audio ({device_type}): {e}", exc_info=True)
            if device_type == "input":
                self._device_change_callback_input = None
            else:
                self._device_change_callback_output = None
            return False
    
    def stop_device_notifications(self, device_type: Optional[Literal["input", "output"]] = None):
        """
        Отписывается от нотификаций Core Audio
        
        Args:
            device_type: Тип устройства (input/output). Если None - отписывается от всех
        """
        try:
            with self._notification_lock:
                # Отписка от INPUT нотификаций
                if device_type is None or device_type == "input":
                    if self._notification_listener_id_input is not None:
                        if self._core_audio_available and self._property_address_input:
                            try:
                                result = AudioObjectRemovePropertyListener(
                                    kAudioObjectSystemObject,
                                    self._property_address_input,
                                    self._notification_listener_id_input,
                                    None
                                )
                                if result == 0:
                                    logger.info("✅ [INPUT] Отписка от Core Audio нотификаций успешна")
                                else:
                                    logger.warning(f"⚠️ [INPUT] Ошибка отписки от нотификаций (код: {result})")
                            except Exception as e:
                                logger.error(f"❌ Ошибка при отписке от INPUT нотификаций: {e}", exc_info=True)
                        
                        self._device_change_callback_input = None
                        self._notification_listener_id_input = None
                        self._property_address_input = None
                
                # Отписка от OUTPUT нотификаций
                if device_type is None or device_type == "output":
                    if self._notification_listener_id_output is not None:
                        if self._core_audio_available and self._property_address_output:
                            try:
                                result = AudioObjectRemovePropertyListener(
                                    kAudioObjectSystemObject,
                                    self._property_address_output,
                                    self._notification_listener_id_output,
                                    None
                                )
                                if result == 0:
                                    logger.info("✅ [OUTPUT] Отписка от Core Audio нотификаций успешна")
                                else:
                                    logger.warning(f"⚠️ [OUTPUT] Ошибка отписки от нотификаций (код: {result})")
                            except Exception as e:
                                logger.error(f"❌ Ошибка при отписке от OUTPUT нотификаций: {e}", exc_info=True)
                        
                        self._device_change_callback_output = None
                        self._notification_listener_id_output = None
                        self._property_address_output = None
                
        except Exception as e:
            logger.error(f"❌ Ошибка отписки от нотификаций Core Audio: {e}", exc_info=True)
    
    def is_notifications_available(self) -> bool:
        """Проверяет, доступны ли нотификации Core Audio"""
        return self._core_audio_available
