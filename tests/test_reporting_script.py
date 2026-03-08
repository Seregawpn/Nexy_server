import sys
import os
from unittest.mock import MagicMock, patch

# Add server path to sys.path
current_dir = os.getcwd()
server_dir = os.path.join(current_dir, 'server', 'server')
if server_dir not in sys.path:
    sys.path.insert(0, server_dir)

# Mock psycopg2 module structure BEFORE importing repository
# This is crucial because TokenUsageRepository imports from it at module level
psycopg2 = MagicMock()
psycopg2.__path__ = [] 
sys.modules['psycopg2'] = psycopg2

extras = MagicMock()
psycopg2.extras = extras
sys.modules['psycopg2.extras'] = extras

pool = MagicMock()
psycopg2.pool = pool
sys.modules['psycopg2.pool'] = pool

# Add RealDictCursor to extras
class MockRealDictCursor:
    pass
extras.RealDictCursor = MockRealDictCursor

# Mock dotenv
sys.modules['dotenv'] = MagicMock()

# Now we can import
try:
    # We want to test logic in report_token_costs.py
    # But it's a script. We can just import its functions if we refactor it or just copy logic here?
    # Better: import the script as a module.
    # But the script has `if __name__ == "__main__": main()`
    # We can import it.
    
    # We need to add scripts dir to path?
    scripts_dir = os.path.join(current_dir, 'server', 'scripts')
    sys.path.insert(0, scripts_dir)
    
    import report_token_costs
except ImportError as e:
    print(f"ImportError: {e}")
    sys.exit(1)

def test_reporting_logic():
    print("=== Testing Token Usage Reporting Logic ===\n")
    
    # Mock TokenUsageRepository in the report script module
    with patch('report_token_costs.TokenUsageRepository') as MockRepo:
        instance = MockRepo.return_value
        instance.db_url = "mock://url"
        
        # Setup mock data for get_global_stats
        mock_stats = [
            {
                'hardware_id': 'user_A_1234567890',
                'model_name': 'gemini-3-flash-preview',
                'request_count': 10,
                'input_tokens': 1_000_000,
                'output_tokens': 1_000_000,
                'total_tokens': 2_000_000
            },
            {
                'hardware_id': 'user_B_12345',
                'model_name': 'gemini-1.5-pro',
                'request_count': 5,
                'input_tokens': 1_000_000,
                'output_tokens': 1_000_000,
                'total_tokens': 2_000_000
            }
        ]
        instance.get_global_stats.return_value = mock_stats
        
        # Capture stdout
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            # Run main
            report_token_costs.main()
        except SystemExit:
            pass
        finally:
            sys.stdout = sys.__stdout__
            
        output = captured_output.getvalue()
        print("Captured Output:")
        print(output)
        
        # Verify calculations
        # User A (Flash): Input $0.10 + Output $0.40 = $0.50
        # User B (Pro):   Input $3.50 + Output $10.50 = $14.00
        # Total: $14.50
        
        print("\n=== Validation ===")
        if "$0.5000" in output:
             print("✅ User A cost correct ($0.5000)")
        else:
             print("❌ User A cost incorrect")
             
        if "$14.0000" in output:
             print("✅ User B cost correct ($14.0000)")
        else:
             print("❌ User B cost incorrect")
             
        if "$14.5000" in output:
             print("✅ Total cost correct ($14.5000)")
        else:
             print("❌ Total cost incorrect")

if __name__ == "__main__":
    test_reporting_logic()
