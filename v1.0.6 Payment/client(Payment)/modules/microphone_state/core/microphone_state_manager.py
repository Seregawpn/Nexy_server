"""
MicrophoneStateManager - Централизованный менеджер состояния микрофона

Единый источник истины для управления состоянием микрофона в системе Nexy.
"""

import asyncio
import logging
import time
from typing import Optional, Dict, Any
from enum import Enum

from .types import MicrophoneState

logger = logging.getLogger(__name__)


class MicrophoneStateManager:
    """Централизованный менеджер состояния микрофона"""
    
    def __init__(
        self,
        event_bus,
        state_manager=None,
        open_timeout: float = 5.0,
        close_timeout: float = 3.0
    ):
        """
        Инициализация MicrophoneStateManager.
        
        Args:
            event_bus: EventBus для публикации событий
            state_manager: ApplicationStateManager (опционально, для обратной совместимости)
            open_timeout: Таймаут ожидания открытия микрофона (секунды)
            close_timeout: Таймаут ожидания закрытия микрофона (секунды)
        """
        self._event_bus = event_bus
        self._state_manager = state_manager
        
        # Состояние микрофона
        self._state = MicrophoneState.IDLE
        self._current_session_id: Optional[str] = None
        self._state_lock = asyncio.Lock()  # Асинхронная блокировка для защиты от race conditions
        self._last_state_change: float = 0.0
        self._error_count: int = 0
        
        # Таймауты
        self._open_timeout = open_timeout
        self._close_timeout = close_timeout
        
        # Ожидание подтверждений открытия/закрытия
        self._opened_event: Optional[asyncio.Event] = None
        self._closed_event: Optional[asyncio.Event] = None
        self._opened_session_id: Optional[str] = None
        self._closed_session_id: Optional[str] = None
        
        # Подписки на события
        self._setup_event_subscriptions()
    
    def _setup_event_subscriptions(self):
        """Настройка подписок на события микрофона"""
        # Подписки будут настроены в initialize() для async контекста
        pass
    
    async def initialize(self):
        """Инициализация менеджера (async)"""
        try:
            # Подписываемся на события подтверждения открытия/закрытия
            await self._event_bus.subscribe("microphone.opened", self._on_microphone_opened)
            await self._event_bus.subscribe("microphone.closed", self._on_microphone_closed)
            await self._event_bus.subscribe("microphone.error", self._on_microphone_error)
            
            logger.info("✅ MicrophoneStateManager инициализирован")
            return True
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации MicrophoneStateManager: {e}")
            return False
    
    async def request_open(self, session_id: str, timeout: Optional[float] = None) -> bool:
        """
        Запросить открытие микрофона.
        
        Args:
            session_id: ID сессии для которой открывается микрофон
            timeout: Таймаут ожидания открытия (секунды, None = использовать дефолт)
            
        Returns:
            True если микрофон успешно открыт, False в противном случае
        """
        timeout = timeout or self._open_timeout
        
        # ✅ FIX: Переменные для обработки зависшего состояния CLOSING
        closed_event = None
        wait_timeout = 0.0
        
        async with self._state_lock:
            if self._state == MicrophoneState.ACTIVE:
                if self._current_session_id == session_id:
                    logger.debug(f"✅ [MIC_STATE] Микрофон уже активен для session {session_id}")
                    return True  # Уже открыт для этой сессии
                else:
                    # Другая сессия - сначала закрываем
                    logger.warning(
                        f"⚠️ [MIC_STATE] Микрофон активен для другой сессии "
                        f"({self._current_session_id} != {session_id}), закрываем перед открытием"
                    )
                    await self._force_close_internal("session_mismatch")
            
            # ✅ FIX: Обработка зависшего состояния CLOSING
            if self._state == MicrophoneState.CLOSING:
                # Проверяем, не зависло ли закрытие (прошло больше таймаута)
                time_since_state_change = time.time() - self._last_state_change
                if time_since_state_change > self._close_timeout:
                    logger.warning(
                        f"⚠️ [MIC_STATE] Состояние CLOSING зависло ({time_since_state_change:.2f}s > {self._close_timeout}s), "
                        f"принудительно переводим в IDLE"
                    )
                    await self._force_close_internal("stuck_closing_state")
                else:
                    # Ждем завершения закрытия с таймаутом
                    logger.info(
                        f"⏳ [MIC_STATE] Ожидание завершения закрытия микрофона "
                        f"(прошло {time_since_state_change:.2f}s из {self._close_timeout}s)..."
                    )
                    wait_timeout = self._close_timeout - time_since_state_change
                    if wait_timeout > 0:
                        # Создаем событие для ожидания, если его еще нет
                        if self._closed_event is None:
                            self._closed_event = asyncio.Event()
                        closed_event = self._closed_event
                    else:
                        # Таймаут уже прошел, принудительно закрываем
                        await self._force_close_internal("closing_timeout")
            
            if self._state not in [MicrophoneState.IDLE, MicrophoneState.ERROR]:
                logger.warning(
                    f"⚠️ [MIC_STATE] Невозможно открыть микрофон в состоянии {self._state.value}"
                )
                return False
            
            # Переходим в OPENING
            await self._set_state(MicrophoneState.OPENING, session_id)
            
            # Создаем событие для ожидания подтверждения
            self._opened_event = asyncio.Event()
            self._opened_session_id = session_id
        
        # ✅ FIX: Если было ожидание закрытия, ждем его завершения
        if closed_event is not None:
            try:
                await asyncio.wait_for(closed_event.wait(), timeout=wait_timeout)
                logger.info("✅ [MIC_STATE] Закрытие микрофона завершено, продолжаем открытие")
            except asyncio.TimeoutError:
                logger.warning(f"⚠️ [MIC_STATE] Таймаут ожидания закрытия ({wait_timeout:.2f}s), принудительно переводим в IDLE")
                async with self._state_lock:
                    await self._force_close_internal("closing_wait_timeout")
        
        # КРИТИЧНО: Публикуем событие запроса открытия ПОСЛЕ освобождения блокировки
        # Это предотвращает deadlock, когда _on_microphone_opened вызывается синхронно
        await self._event_bus.publish("microphone.open_requested", {
            "session_id": session_id,
            "timeout": timeout
        })
        
        # Ждем подтверждения открытия с таймаутом
        try:
            opened = await asyncio.wait_for(
                self._wait_for_microphone_opened(session_id),
                timeout=timeout
            )
            
            if opened:
                logger.info(f"✅ [MIC_STATE] Микрофон успешно открыт для session {session_id}")
                return True
            else:
                logger.error(f"❌ [MIC_STATE] Таймаут ожидания открытия микрофона для session {session_id}")
                await self._force_close_internal("open_timeout")
                return False
                
        except asyncio.TimeoutError:
            logger.error(f"❌ [MIC_STATE] Таймаут ожидания открытия микрофона ({timeout}s) для session {session_id}")
            await self._force_close_internal("open_timeout")
            return False
        except Exception as e:
            logger.error(f"❌ [MIC_STATE] Ошибка ожидания открытия микрофона: {e}")
            await self._force_close_internal("open_error")
            return False
    
    async def request_close(self, session_id: Optional[str] = None, force: bool = False, timeout: Optional[float] = None) -> bool:
        """
        Запросить закрытие микрофона.
        
        Args:
            session_id: ID сессии (None для принудительного закрытия)
            force: Принудительное закрытие (игнорирует session_id)
            timeout: Таймаут ожидания закрытия (секунды, None = использовать дефолт)
            
        Returns:
            True если микрофон успешно закрыт, False в противном случае
        """
        timeout = timeout or self._close_timeout
        
        async with self._state_lock:
            if self._state == MicrophoneState.IDLE:
                logger.debug("✅ [MIC_STATE] Микрофон уже закрыт")
                return True  # Уже закрыт
            
            if not force and session_id is not None:
                if self._current_session_id != session_id:
                    logger.warning(
                        f"⚠️ [MIC_STATE] session_id mismatch: "
                        f"{self._current_session_id} != {session_id}"
                    )
                    if not force:
                        return False
            
            # ✅ КРИТИЧНО: Если _closed_event уже установлен (microphone.closed уже обработано),
            # значит микрофон уже закрыт, можно сразу вернуть True
            if self._closed_event is not None and self._closed_event.is_set():
                logger.debug("✅ [MIC_STATE] microphone.closed уже обработано, микрофон закрыт")
                return True
            
            # Переходим в CLOSING
            await self._set_state(MicrophoneState.CLOSING, None)
            
            # Создаем событие для ожидания подтверждения (если еще не создано)
            if self._closed_event is None:
                self._closed_event = asyncio.Event()
                self._closed_session_id = session_id
            # ✅ КРИТИЧНО: Если событие уже установлено (microphone.closed пришло раньше),
            # сразу возвращаем True без ожидания
            elif self._closed_event.is_set():
                logger.debug("✅ [MIC_STATE] microphone.closed уже обработано до request_close, микрофон закрыт")
                self._closed_event = None
                self._closed_session_id = None
                await self._set_state(MicrophoneState.IDLE, None)
                return True
            
            # Публикуем событие запроса закрытия
            await self._event_bus.publish("microphone.close_requested", {
                "session_id": session_id,
                "force": force
            })
        
        # Ждем подтверждения закрытия с таймаутом
        try:
            closed = await asyncio.wait_for(
                self._wait_for_microphone_closed(session_id),
                timeout=timeout
            )
            
            if closed:
                logger.info(f"✅ [MIC_STATE] Микрофон успешно закрыт для session {session_id}")
                return True
            else:
                logger.warning(f"⚠️ [MIC_STATE] Таймаут ожидания закрытия микрофона для session {session_id}")
                # При таймауте принудительно закрываем
                await self._force_close_internal("close_timeout")
                return True  # Все равно считаем успешным, так как принудительно закрыли
                
        except asyncio.TimeoutError:
            logger.warning(f"⚠️ [MIC_STATE] Таймаут ожидания закрытия микрофона ({timeout}s) для session {session_id}")
            # При таймауте принудительно закрываем
            await self._force_close_internal("close_timeout")
            return True  # Все равно считаем успешным, так как принудительно закрыли
        except Exception as e:
            logger.error(f"❌ [MIC_STATE] Ошибка ожидания закрытия микрофона: {e}")
            await self._force_close_internal("close_error")
            return True  # Все равно считаем успешным, так как принудительно закрыли
    
    async def force_close(self, reason: str = "unknown") -> bool:
        """
        Принудительно закрыть микрофон (восстановление при ошибках).
        
        Args:
            reason: Причина принудительного закрытия
            
        Returns:
            True если микрофон успешно закрыт
        """
        async with self._state_lock:
            logger.warning(f"⚠️ [MIC_STATE] Принудительное закрытие микрофона: {reason}")
            await self._force_close_internal(reason)
        return True
    
    async def _force_close_internal(self, reason: str):
        """Внутренний метод для принудительного закрытия"""
        old_state = self._state
        if old_state != MicrophoneState.IDLE:
            await self._set_state(MicrophoneState.IDLE, None)
            self._error_count += 1
            logger.warning(
                f"⚠️ [MIC_STATE] Принудительное закрытие: {old_state.value} → IDLE "
                f"(reason={reason}, error_count={self._error_count})"
            )
            
            # ✅ ЭТАП 1: Публикуем voice.mic_closed при принудительном закрытии
            await self._event_bus.publish("voice.mic_closed", {
                "session_id": None,
                "timestamp": time.time(),
                "source": "microphone_state_manager",
                "reason": reason
            })
            logger.info(f"✅ [MIC_STATE] voice.mic_closed опубликовано (принудительное закрытие: {reason})")
    
    async def _set_state(self, new_state: MicrophoneState, session_id: Optional[str] = None):
        """Внутренний метод для изменения состояния (с защитой от race conditions)"""
        old_state = self._state
        if old_state != new_state:
            self._state = new_state
            self._current_session_id = session_id
            self._last_state_change = time.time()
            
            # Публикуем событие изменения состояния
            await self._event_bus.publish("microphone.state_changed", {
                "old_state": old_state.value,
                "new_state": new_state.value,
                "session_id": session_id,
                "timestamp": self._last_state_change
            })
            
            logger.info(
                f"🔄 [MIC_STATE] {old_state.value} → {new_state.value} "
                f"(session={session_id})"
            )
            
            # Синхронизация с ApplicationStateManager (для обратной совместимости)
            if self._state_manager:
                try:
                    self._state_manager.set_microphone_state(
                        new_state.value,
                        session_id,
                        reason="microphone_state_manager"
                    )
                except Exception as e:
                    logger.debug(f"⚠️ [MIC_STATE] Ошибка синхронизации с state_manager: {e}")
    
    def get_state(self) -> MicrophoneState:
        """Получить текущее состояние микрофона"""
        return self._state
    
    def is_active(self) -> bool:
        """Проверить, активен ли микрофон"""
        return self._state == MicrophoneState.ACTIVE
    
    def get_current_session_id(self) -> Optional[str]:
        """Получить текущий session_id микрофона"""
        return self._current_session_id if self._state == MicrophoneState.ACTIVE else None
    
    async def _wait_for_microphone_opened(self, session_id: str) -> bool:
        """Ожидание подтверждения открытия микрофона"""
        if self._opened_event is None:
            return False
        
        await self._opened_event.wait()
        
        # Проверяем, что открытие было для правильной сессии
        if self._opened_session_id == session_id:
            self._opened_event = None
            self._opened_session_id = None
            return True
        else:
            logger.warning(
                f"⚠️ [MIC_STATE] session_id mismatch при открытии: "
                f"ожидали {session_id}, получили {self._opened_session_id}"
            )
            return False
    
    async def _wait_for_microphone_closed(self, session_id: Optional[str]) -> bool:
        """Ожидание подтверждения закрытия микрофона"""
        if self._closed_event is None:
            return False
        
        await self._closed_event.wait()
        
        # При закрытии session_id может быть None (принудительное закрытие)
        self._closed_event = None
        self._closed_session_id = None
        return True
    
    async def _on_microphone_opened(self, event: Dict[str, Any]):
        """Обработчик события открытия микрофона"""
        try:
            data = event.get("data", {}) or event
            session_id = data.get("session_id")
            
            logger.info(f"🔍 [MIC_STATE] _on_microphone_opened вызван: session={session_id}, текущее состояние={self._state.value}")
            
            # КРИТИЧНО: Используем timeout для получения блокировки, чтобы избежать deadlock
            async def _process_opened():
                async with self._state_lock:
                    logger.info(f"🔍 [MIC_STATE] _on_microphone_opened: состояние после lock={self._state.value}")
                    if self._state == MicrophoneState.OPENING:
                        await self._set_state(MicrophoneState.ACTIVE, session_id)
                        
                        # Уведомляем ожидающие задачи
                        if self._opened_event:
                            self._opened_event.set()
                        
                        # ✅ ЭТАП 1: Публикуем voice.mic_opened (ЕДИНСТВЕННЫЙ ИСТОЧНИК)
                        await self._event_bus.publish("voice.mic_opened", {
                            "session_id": session_id,
                            "timestamp": time.time(),
                            "source": "microphone_state_manager"
                        })
                        logger.info(f"✅ [MIC_STATE] voice.mic_opened опубликовано для session {session_id}")
                    else:
                        logger.warning(
                            f"⚠️ [MIC_STATE] Неожиданное состояние при opened: {self._state.value}"
                        )
            
            try:
                # Пытаемся получить блокировку с таймаутом 1 секунда
                await asyncio.wait_for(_process_opened(), timeout=1.0)
            except asyncio.TimeoutError:
                logger.error(f"❌ [MIC_STATE] Таймаут получения блокировки в _on_microphone_opened (возможен deadlock)")
                return
        except Exception as e:
            logger.error(f"❌ [MIC_STATE] Ошибка обработки microphone.opened: {e}")
    
    async def _on_microphone_closed(self, event: Dict[str, Any]):
        """Обработчик события закрытия микрофона"""
        try:
            data = event.get("data", {}) or event
            session_id = data.get("session_id")
            
            async with self._state_lock:
                if self._state in [MicrophoneState.ACTIVE, MicrophoneState.CLOSING]:
                    await self._set_state(MicrophoneState.IDLE, None)
                    
                    # Уведомляем ожидающие задачи
                    if self._closed_event:
                        self._closed_event.set()
                    
                    # ✅ ЭТАП 1: Публикуем voice.mic_closed (ЕДИНСТВЕННЫЙ ИСТОЧНИК)
                    await self._event_bus.publish("voice.mic_closed", {
                        "session_id": session_id,
                        "timestamp": time.time(),
                        "source": "microphone_state_manager"
                    })
                    logger.info(f"✅ [MIC_STATE] voice.mic_closed опубликовано для session {session_id}")
                else:
                    logger.debug(
                        f"ℹ️ [MIC_STATE] Закрытие микрофона в состоянии {self._state.value} "
                        f"(возможно, уже закрыт)"
                    )
                    # Все равно уведомляем ожидающие задачи
                    if self._closed_event:
                        self._closed_event.set()
        except Exception as e:
            logger.error(f"❌ [MIC_STATE] Ошибка обработки microphone.closed: {e}")
    
    async def _on_microphone_error(self, event: Dict[str, Any]):
        """Обработчик события ошибки микрофона"""
        try:
            data = event.get("data", {}) or event
            session_id = data.get("session_id")
            error = data.get("error", "unknown")
            
            async with self._state_lock:
                await self._set_state(MicrophoneState.ERROR, None)
                self._error_count += 1
                
                logger.error(
                    f"❌ [MIC_STATE] Ошибка микрофона: {error} "
                    f"(session={session_id}, error_count={self._error_count})"
                )
                
                # Уведомляем ожидающие задачи об ошибке
                if self._opened_event:
                    self._opened_event.set()
                if self._closed_event:
                    self._closed_event.set()
        except Exception as e:
            logger.error(f"❌ [MIC_STATE] Ошибка обработки microphone.error: {e}")
    
    def get_status(self) -> Dict[str, Any]:
        """Получить статус менеджера"""
        return {
            "state": self._state.value,
            "session_id": self._current_session_id,
            "last_state_change": self._last_state_change,
            "error_count": self._error_count,
            "open_timeout": self._open_timeout,
            "close_timeout": self._close_timeout,
        }

