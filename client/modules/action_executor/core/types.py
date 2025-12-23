from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ActionExecutorConfig:
    """Конфигурация исполнителя действий."""

    enabled: bool = False  # По умолчанию выключено для безопасности
    timeout_sec: float = 10.0
    allowed_apps: List[str] = field(default_factory=list)  # Пустой список = все разрешены
    binary: str = "/usr/bin/open"


@dataclass
class ActionResult:
    """Результат выполнения действия."""

    success: bool
    message: str
    error: Optional[str] = None
    app_name: Optional[str] = None

