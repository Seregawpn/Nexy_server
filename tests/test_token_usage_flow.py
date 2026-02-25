import sys
import os
from unittest.mock import MagicMock, patch

# Add server path
current_dir = os.getcwd()
server_dir = os.path.join(current_dir, 'server', 'server')
sys.path.insert(0, server_dir)

# Mock psycopg2 before importing repository
psycopg2 = MagicMock()
psycopg2.__path__ = [] # Mark as package
sys.modules['psycopg2'] = psycopg2

extras = MagicMock()
psycopg2.extras = extras
sys.modules['psycopg2.extras'] = extras

pool = MagicMock()
psycopg2.pool = pool
sys.modules['psycopg2.pool'] = pool

# Mock RealDictCursor
class MockRealDictCursor:
    pass
extras.RealDictCursor = MockRealDictCursor

from psycopg2.extras import RealDictCursor

# Mock dotenv
sys.modules['dotenv'] = MagicMock()

try:
    from modules.database.repository.token_usage_repository import TokenUsageRepository
    from integrations.core.token_usage_tracker import TokenUsageTracker
except ImportError as e:
    print(f"ImportError: {e}")
    print(f"sys.path: {sys.path}")
    sys.exit(1)

def test_server_token_flow():
    print("=== Testing Server-Side Token Usage Flow ===")
    
    # 1. Setup Mock DB
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    # Patch psycopg2.connect to return our mock connection
    with patch('psycopg2.connect', return_value=mock_conn) as mock_connect:
        
        # 2. Initialize Repository
        print("Initializing TokenUsageRepository...")
        repo = TokenUsageRepository(db_url="postgres://fake:fake@localhost:5432/fake")
        
        # 3. Initialize Tracker
        print("Initializing TokenUsageTracker...")
        tracker = TokenUsageTracker(repository=repo)
        
        # 4. Simulate ReportUsage Call
        test_data = {
            "hardware_id": "hwd_12345",
            "source": "browser_agent",
            "input_tokens": 150,
            "output_tokens": 50,
            "session_id": "sess_abc",
            "model_name": "gemini-3-flash-preview"
        }
        
        print(f"Recording usage: {test_data}")
        success = tracker.record_usage(**test_data)
        
        # 5. Verify Results
        print("\n=== Verification Results ===")
        if success:
            print("Tracker returned Success.")
        else:
            print("❌ FAILED: Tracker returned False.")
            sys.exit(1)
            
        # Check if cursor.execute was called with correct SQL and params
        if mock_cursor.execute.called:
            args, _ = mock_cursor.execute.call_args
            query, params = args
            
            print("Executed SQL Query:")
            print(query.strip())
            print("\nParameters:")
            print(params)
            
            # Assertions
            expected_params = (
                test_data['hardware_id'],
                test_data['session_id'],
                test_data['source'],
                test_data['input_tokens'],
                test_data['output_tokens'],
                test_data['model_name']
            )
            
            # Note: repository might strip params or change order, let's verify precisely
            # The query in repository is:
            # INSERT INTO token_usage (hardware_id, session_id, source, input_tokens, output_tokens, model_name) VALUES ...
            # Params order matches
            
            if params == expected_params:
                print("\n✅ SUCCESS: Full server-side flow verified.")
                print("   Data correctly passed from Tracker -> Repository -> DB Driver.")
            else:
                print(f"\n❌ FAILED: Parameters mismatch.\nExpected: {expected_params}\nGot:      {params}")
        else:
            print("\n❌ FAILED: Cursor execution not called.")

if __name__ == "__main__":
    test_server_token_flow()
