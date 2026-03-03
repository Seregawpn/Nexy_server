"""
Session Registry - Централизованное хранилище активных сессий
"""

import logging
import time
import threading
from typing import Dict, Any, Optional, List, Set
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

@dataclass
class SessionData:
    """Данные сессии"""
    session_id: str
    hardware_id: str
    created_at: float
    last_activity: float
    status: str = "active"  # active, interrupted, completed, expired
    user_agent: Optional[str] = None
    ip_address: Optional[str] = None
    context: Dict[str, Any] = field(default_factory=dict)
    interrupt_flag: bool = False
    interrupt_reason: Optional[str] = None

class SessionRegistry:
    """
    Централизованный реестр сессий.
    Обеспечивает thread-safe доступ к данным сессий для всех компонентов.
    Использует threading.RLock для поддержки синхронных методов (get_status).
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SessionRegistry, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance
    
    def __init__(self):
        if self.initialized:
            return
            
        self._lock = threading.RLock()
        self._active_sessions: Dict[str, SessionData] = {}
        self._interrupted_sessions: Set[str] = set()
        self._inflight_sessions: Set[str] = set()
        self._inflight_hardware_sessions: Dict[str, Set[str]] = {}
        self.initialized = True
        
        logger.info("SessionRegistry initialized")
    
    def register_session(self, session_data: SessionData) -> bool:
        """Регистрация новой сессии"""
        with self._lock:
            if session_data.session_id in self._active_sessions:
                logger.warning(f"Session {session_data.session_id} already exists")
                return False
                
            self._active_sessions[session_data.session_id] = session_data
            logger.debug(f"Session registered: {session_data.session_id[:8]}...")
            return True
    
    def unregister_session(self, session_id: str) -> Optional[SessionData]:
        """Удаление сессии"""
        with self._lock:
            if session_id in self._active_sessions:
                session = self._active_sessions.pop(session_id)
                logger.debug(f"Session unregistered: {session_id[:8]}...")
                return session
            return None
            
    def get_session(self, session_id: str) -> Optional[SessionData]:
        """Получение сессии по ID"""
        with self._lock:
            return self._active_sessions.get(session_id)
            
    def get_sessions_by_hardware_id(self, hardware_id: str) -> List[SessionData]:
        """Получение всех сессий для hardware_id"""
        with self._lock:
            return [
                s for s in self._active_sessions.values() 
                if s.hardware_id == hardware_id
            ]
            
    def update_last_activity(self, session_id: str) -> bool:
        """Обновление времени последней активности"""
        with self._lock:
            if session_id in self._active_sessions:
                self._active_sessions[session_id].last_activity = time.time()
                return True
            return False
            
    def interrupt_session(self, session_id: str, reason: str) -> bool:
        """Прерывание конкретной сессии"""
        with self._lock:
            if session_id in self._active_sessions:
                session = self._active_sessions[session_id]
                session.interrupt_flag = True
                session.interrupt_reason = reason
                session.status = "interrupted"
                self._interrupted_sessions.add(session_id)
                logger.info(f"Session {session_id[:8]} interrupted. Reason: {reason}")
                return True
            return False

    def get_all_sessions(self) -> List[SessionData]:
        """Получение копии списка всех сессий"""
        with self._lock:
            return list(self._active_sessions.values())

    def try_acquire_inflight(
        self,
        session_id: str,
        hardware_id: str,
        prevent_concurrent_hardware: bool = False
    ) -> Dict[str, Any]:
        """
        Атомарная регистрация in-flight запроса.
        Возвращает решение и контекст для диагностики/ошибки.
        """
        with self._lock:
            if session_id in self._inflight_sessions:
                return {
                    "ok": False,
                    "reason": "concurrent_request",
                    "active_sessions": [session_id]
                }

            active_sessions = list(self._inflight_hardware_sessions.get(hardware_id, set()))
            if prevent_concurrent_hardware and active_sessions:
                return {
                    "ok": False,
                    "reason": "concurrent_hardware_id",
                    "active_sessions": active_sessions
                }

            self._inflight_sessions.add(session_id)
            if hardware_id not in self._inflight_hardware_sessions:
                self._inflight_hardware_sessions[hardware_id] = set()
            self._inflight_hardware_sessions[hardware_id].add(session_id)

            return {"ok": True, "active_sessions": active_sessions}

    def release_inflight(self, session_id: str, hardware_id: Optional[str]) -> bool:
        """
        Освобождает in-flight регистрацию.
        Возвращает True, если session_id присутствовал.
        """
        with self._lock:
            was_present = session_id in self._inflight_sessions
            self._inflight_sessions.discard(session_id)

            if hardware_id and hardware_id in self._inflight_hardware_sessions:
                self._inflight_hardware_sessions[hardware_id].discard(session_id)
                if not self._inflight_hardware_sessions[hardware_id]:
                    del self._inflight_hardware_sessions[hardware_id]

            return was_present

    def get_inflight_sessions_by_hardware_id(self, hardware_id: str) -> List[str]:
        """Возвращает копию in-flight session_id для hardware_id."""
        with self._lock:
            return list(self._inflight_hardware_sessions.get(hardware_id, set()))

    def get_inflight_session_ids(self) -> List[str]:
        """Возвращает копию всех in-flight session_id."""
        with self._lock:
            return list(self._inflight_sessions)

    def clear(self):
        """Очистка всех сессий"""
        with self._lock:
            self._active_sessions.clear()
            self._interrupted_sessions.clear()
            self._inflight_sessions.clear()
            self._inflight_hardware_sessions.clear()
            logger.info("SessionRegistry cleared")
