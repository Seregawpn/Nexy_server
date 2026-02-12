"""
WhatsApp Client Configuration
"""

from dataclasses import dataclass
import logging
import os

logger = logging.getLogger(__name__)


@dataclass
class WhatsappConfig:
    """Configuration for WhatsApp Module"""

    enabled: bool = False
    node_path: str = "node"  # Path to node executable
    service_script_path: str = ""  # set dynamically or via env
    keep_alive: bool = True

    @classmethod
    def from_env(cls):
        # Allow override from env
        return cls(
            enabled=os.getenv("WHATSAPP_ENABLED", "false").lower() == "true",
            node_path=os.getenv("NODE_PATH", "node"),
            service_script_path=os.getenv("WHATSAPP_SERVICE_PATH", ""),  # Should point to index.js
            keep_alive=os.getenv("WHATSAPP_KEEP_ALIVE", "true").lower() == "true",
        )


# Global config instance can be managed here or injected
