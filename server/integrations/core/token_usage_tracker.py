
import logging
from typing import Optional, Dict, Any
from modules.database.repository.token_usage_repository import TokenUsageRepository

logger = logging.getLogger(__name__)

class TokenUsageTracker:
    """
    Centralized service for tracking token usage from all sources.
    
    Sources:
    - main_llm: Text processing (Gemini/LangChain)
    - memory_analyzer: Memory extraction (Gemini)
    - browser_agent: Browser automation (Gemini via client)
    """
    
    def __init__(self, repository: Optional[TokenUsageRepository] = None):
        if repository:
            self.repository = repository
        else:
            try:
                self.repository = TokenUsageRepository()
            except Exception as e:
                logger.error(f"Failed to initialize TokenUsageRepository: {e}")
                self.repository = None
        
    def record_usage(
        self,
        hardware_id: str,
        source: str,
        input_tokens: int,
        output_tokens: int,
        session_id: Optional[str] = None,
        model_name: Optional[str] = None
    ) -> bool:
        """
        Record token usage.
        
        Args:
            hardware_id: User ID
            source: 'main_llm', 'memory_analyzer', 'browser_agent'
            input_tokens: Input token count
            output_tokens: Output token count
            session_id: Session ID involved
            model_name: Name of the model used
        """
        if not self.repository:
            return False
            
        if input_tokens == 0 and output_tokens == 0:
            return True
            
        try:
            success = self.repository.record_usage(
                hardware_id=hardware_id,
                source=source,
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                session_id=session_id,
                model_name=model_name
            )
            
            if success:
                logger.debug(f"[TokenUsage] Recorded {input_tokens}+{output_tokens} tokens for {source} (user: {hardware_id[:8]})")
            else:
                logger.warning(f"[TokenUsage] Failed to record usage for {source}")
                
            return success
            
        except Exception as e:
            logger.error(f"[TokenUsage] Error recording usage: {e}")
            return False

    def get_stats(self, hardware_id: str, period: str = 'daily') -> Dict[str, Any]:
        """Get token usage statistics."""
        if not self.repository:
            return {}
        return self.repository.get_aggregated_stats(hardware_id, period)
