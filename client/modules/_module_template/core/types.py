"""
Template Types
Dataclasses and Enums for the module.
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, Any, Optional

class TemplateState(Enum):
    """Module operational states"""
    IDLE = auto()
    READY = auto()
    PROCESSING = auto()
    ERROR = auto()

@dataclass
class TemplateConfig:
    """Module configuration"""
    enabled: bool = True
    name: str = "template_module"
    # Add custom config fields here
    debug_mode: bool = False

@dataclass
class TemplateResult:
    """Standardized result object"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

class TemplateEvent:
    """
    Event topics this module publishes/subscribes to.
    ALL payloads must include 'session_id'.
    """
    # INPUT
    START_PROCESS = "template.start_process"
    
    # OUTPUT
    PROCESS_COMPLETED = "template.process_completed"
    ERROR_OCCURRED = "template.error"
