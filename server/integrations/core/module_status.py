"""
ModuleStatus - dataclass для статуса модуля
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum


class ModuleState(Enum):
    """Состояние модуля"""

    INIT = "init"
    INITIALIZING = "initializing"
    READY = "ready"
    PROCESSING = "processing"
    ERROR = "error"
    STOPPED = "stopped"


@dataclass
class ModuleStatus:
    """
    Статус модуля
    
    Attributes:
        state: Текущее состояние модуля
        last_error: Последняя ошибка (если есть)
        since: Время последнего изменения состояния
        health: Общее состояние здоровья модуля (ok, degraded, down)
    """
    state: ModuleState = ModuleState.INIT
    last_error: Optional[str] = None
    since: datetime = field(default_factory=datetime.now)
    health: str = "unknown"  # ok, degraded, down
    
    def __post_init__(self):
        """Пост-инициализация"""
        if self.health == "unknown":
            self.health = "ok" if self.state == ModuleState.READY else "down"
    
    def to_dict(self) -> dict:
        """Преобразование в словарь"""
        return {
            "state": self.state.value,
            "last_error": self.last_error,
            "since": self.since.isoformat(),
            "health": self.health
        }

    def is_ready(self) -> bool:
        """Проверка, готов ли модуль к работе"""
        return self.state == ModuleState.READY and self.health == "ok"

    def is_error(self) -> bool:
        """Проверка, есть ли ошибка"""
        return self.state == ModuleState.ERROR or self.health == "down"

    @classmethod
    def for_state(
        cls,
        state: ModuleState,
        *,
        health: Optional[str] = None,
        last_error: Optional[str] = None,
    ) -> "ModuleStatus":
        """Фабрика для создания статуса по состоянию.

        Args:
            state: Целевое состояние модуля.
            health: Пользовательское значение здоровья (если None — выводится автоматически).
            last_error: Сообщение об ошибке (опционально).

        Returns:
            ModuleStatus с корректно выставленным health.
        """

        if health is None:
            if state == ModuleState.READY:
                health = "ok"
            elif state in (ModuleState.ERROR, ModuleState.STOPPED):
                health = "down"
            else:
                health = "degraded"

        return cls(state=state, health=health, last_error=last_error)

