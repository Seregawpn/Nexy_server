"""
Template Logic
Isolated business logic for the module.
Does NOT depend on EventBus or other Integrations.
"""

import logging
from typing import Any

from .types import TemplateConfig, TemplateResult, TemplateState

logger = logging.getLogger(__name__)


class TemplateLogic:
    """
    Main logic class for the module.
    Should be testable in isolation.
    """

    def __init__(self, config: TemplateConfig):
        self.config = config
        self.state = TemplateState.IDLE
        logger.info(f"[{self.config.name}] Initialized with config: {self.config}")

    async def initialize(self) -> bool:
        """Async initialization if needed"""
        logger.info(f"[{self.config.name}] Initializing...")
        self.state = TemplateState.READY
        return True

    async def process_data(self, data: dict[str, Any]) -> TemplateResult:
        """
        Main processing method.
        Args:
            data: Input data
        Returns:
            TemplateResult
        """
        if self.state != TemplateState.READY:
            logger.warning(f"[{self.config.name}] Not ready (state={self.state})")
            return TemplateResult(success=False, error="Module not ready")

        try:
            self.state = TemplateState.PROCESSING
            logger.info(f"[{self.config.name}] Processing data: {data}")

            # --- BUSINESS LOGIC HERE ---
            # result = await do_something(data)
            processed_value = data.get("value", "default")
            # ---------------------------

            self.state = TemplateState.READY
            return TemplateResult(success=True, data={"processed": processed_value})

        except Exception as e:
            logger.error(f"[{self.config.name}] Error processing: {e}")
            self.state = TemplateState.ERROR
            return TemplateResult(success=False, error=str(e))
