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

    def clear(self):
        """Очистка всех сессий"""
        with self._lock:
            self._active_sessions.clear()
            self._interrupted_sessions.clear()
            logger.info("SessionRegistry cleared")
