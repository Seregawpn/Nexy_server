from datetime import datetime, timedelta
import logging
import psycopg2
from typing import Dict, List, Optional, Any
from psycopg2.extras import RealDictCursor

logger = logging.getLogger(__name__)

class TokenUsageRepository:
    """
    Repository for managing token usage records in the database.
    """
    
    def __init__(self, db_url: Optional[str] = None):
        """
        Initialize the repository.
        
        Args:
            db_url: Database connection URL (optional)
        """
        import os
        from dotenv import load_dotenv
        
        # Ensure env is loaded
        load_dotenv('config.env')
        
        self.db_url = db_url or os.getenv('DATABASE_URL')
        
        # If DATABASE_URL is not set, try to construct it from components
        if not self.db_url:
            host = os.getenv('DB_HOST')
            port = os.getenv('DB_PORT', '5432')
            name = os.getenv('DB_NAME')
            user = os.getenv('DB_USER')
            password = os.getenv('DB_PASSWORD')
            
            if host and name and user:
                # Construct DSN
                self.db_url = f"postgresql://{user}:{password}@{host}:{port}/{name}"
        
        if not self.db_url:
            logger.warning("DATABASE_URL or DB credentials not found, TokenUsageRepository will not work")

    def _get_connection(self):
        """Get database connection."""
        if not self.db_url:
            raise ValueError("Database URL is not set")
        return psycopg2.connect(self.db_url, cursor_factory=RealDictCursor)

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
        Record token usage for a specific user and source.
        
        Args:
            hardware_id: Device/User ID
            source: Source of tokens ('main_llm', 'memory_analyzer', 'browser_agent')
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
            session_id: Associated session ID (optional)
            model_name: Name of the model used (optional)
            
        Returns:
            True if successful, False otherwise
        """
        if not self.db_url:
            return False
            
        try:
            conn = self._get_connection()
            cur = conn.cursor()
            
            query = """
                INSERT INTO token_usage (
                    hardware_id, session_id, source, 
                    input_tokens, output_tokens, model_name
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """
            
            cur.execute(query, (
                hardware_id, 
                session_id, 
                source, 
                input_tokens, 
                output_tokens, 
                model_name
            ))
            
            conn.commit()
            return True
            
        except Exception as e:
            logger.error(f"Error recording token usage: {e}")
            if 'conn' in locals(): conn.rollback()
            return False
        finally:
            if 'cur' in locals(): cur.close()
            if 'conn' in locals(): conn.close()

    def get_aggregated_stats(self, hardware_id: str, period: str = 'daily') -> Dict[str, Any]:
        """
        Get aggregated token usage statistics for a user.
        
        Args:
            hardware_id: User/Device ID
            period: Aggregation period ('daily', 'weekly', 'monthly', 'all')
            
        Returns:
            Dictionary with usage stats by source
        """
        if not self.db_url:
            return {}
            
        try:
            conn = self._get_connection()
            cur = conn.cursor()
            
            # Determine time filter
            now = datetime.now()
            if period == 'daily':
                start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
            elif period == 'weekly':
                # Start of week (Monday)
                start_date = (now - timedelta(days=now.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
            elif period == 'monthly':
                start_date = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            else:
                # 'all' or default -> very old date
                start_date = datetime(2000, 1, 1)
            
            query = """
                SELECT 
                    source,
                    SUM(input_tokens) as input_tokens,
                    SUM(output_tokens) as output_tokens,
                    SUM(total_tokens) as total_tokens,
                    COUNT(*) as request_count
                FROM token_usage
                WHERE hardware_id = %s AND created_at >= %s
                GROUP BY source
            """
            
            cur.execute(query, (hardware_id, start_date))
            results = cur.fetchall()
            
            stats = {
                'period': period,
                'start_date': start_date.isoformat(),
                'total_usage': 0,
                'by_source': {}
            }
            
            total_tokens = 0
            for row in results:
                source = row['source']
                row_total = row['total_tokens'] or 0
                total_tokens += row_total
                
                stats['by_source'][source] = {
                    'input': row['input_tokens'] or 0,
                    'output': row['output_tokens'] or 0,
                    'total': row_total,
                    'requests': row['request_count']
                }
            
            stats['total_usage'] = total_tokens
            return stats
            
        except Exception as e:
            logger.error(f"Error getting token usage stats: {e}")
            return {}
    def get_global_stats(self, period: str = 'daily') -> List[Dict[str, Any]]:
        """
        Get global token usage statistics grouped by user and model.
        
        Args:
            period: Aggregation period ('daily', 'weekly', 'monthly', 'all')
            
        Returns:
            List of usage records
        """
        if not self.db_url:
            return []
            
        try:
            conn = self._get_connection()
            cur = conn.cursor()
            
            # Determine time filter
            now = datetime.now()
            if period == 'daily':
                start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
            elif period == 'weekly':
                start_date = (now - timedelta(days=now.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
            elif period == 'monthly':
                start_date = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            else:
                start_date = datetime(2000, 1, 1)
            
            query = """
                SELECT 
                    hardware_id, 
                    model_name,
                    SUM(input_tokens) as input_tokens,
                    SUM(output_tokens) as output_tokens,
                    SUM(total_tokens) as total_tokens,
                    COUNT(*) as request_count
                FROM token_usage
                WHERE created_at >= %s
                GROUP BY hardware_id, model_name
                ORDER BY total_tokens DESC
            """
            
            cur.execute(query, (start_date,))
            results = cur.fetchall()
            
            return [dict(row) for row in results]
            
        except Exception as e:
            logger.error(f"Error getting global stats: {e}")
            return []
        finally:
            if 'cur' in locals(): cur.close()
            if 'conn' in locals(): conn.close()
