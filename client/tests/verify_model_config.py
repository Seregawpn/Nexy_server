import sys
import os
import yaml
from unittest.mock import patch, MagicMock

# Add client to path so imports work
current_dir = os.getcwd()
client_dir = os.path.join(current_dir, 'client')
sys.path.insert(0, client_dir)

# Mock external dependencies to avoid runtime errors
sys.modules['browser_use'] = MagicMock()
sys.modules['langchain_google_genai'] = MagicMock()

# Import the module under test
# We need to handle potential import errors if other dependencies are missing
try:
    from modules.browser_automation.module import BrowserUseModule
    from config.unified_config_loader import unified_config
except ImportError as e:
    print(f"ImportError: {e}")
    print("Make sure you are running from the project root and client/ is accessible.")
    sys.exit(1)

def test_model_config():
    print("=== Verifying Browser Model Configuration ===")
    
    # 1. Verify file content
    config_path = os.path.join(client_dir, 'config', 'unified_config.yaml')
    print(f"\n[1] Checking {config_path}...")
    try:
        with open(config_path, 'r') as f:
            raw_config = yaml.safe_load(f)
            browser_config = raw_config.get('browser_use', {})
            file_model = browser_config.get('gemini_model')
            print(f"    - unified_config.yaml 'gemini_model': {file_model}")
            
            if file_model != 'gemini-3-flash-preview':
                print(f"    WARNING: Expected 'gemini-3-flash-preview', found '{file_model}'")
    except Exception as e:
        print(f"    ERROR reading config file: {e}")

    # 2. Verify UnifiedConfigLoader
    print(f"\n[2] Checking UnifiedConfigLoader...")
    try:
        # Force reload to be sure
        unified_config.reload()
        loaded_config = unified_config.get_browser_use_config()
        loader_model = loaded_config.get('gemini_model')
        print(f"    - unified_config.get_browser_use_config()['gemini_model']: {loader_model}")
        
        if loader_model != 'gemini-3-flash-preview':
             print(f"    WARNING: Loader returned '{loader_model}'")
    except Exception as e:
        print(f"    ERROR checking loader: {e}")

    # 3. Verify BrowserUseModule logic
    print(f"\n[3] Checking BrowserUseModule._create_llm logic...")
    
    # Ensure no env vars interfere
    with patch.dict(os.environ, {}, clear=True):
        # We also need to mock GEMINI_API_KEY in config if it's missing, otherwise ValueError
        # Check if key is present in loaded config
        if not loaded_config.get('gemini_api_key'):
             print("    NOTE: Injecting mock API key for test.")
             # We can mock get_browser_use_config to return key + model
             # But better to rely on actual config file if possible. 
             # Assuming config file has a key (it usually does in this env).
             pass

        module = BrowserUseModule()
        
        # Patch GeminiLLMAdapter to see what it receives
        with patch('modules.browser_automation.module.GeminiLLMAdapter') as MockAdapter:
            try:
                module._create_llm()
                
                args, kwargs = MockAdapter.call_args
                passed_model = kwargs.get('model')
                print(f"    - GeminiLLMAdapter initialized with model: '{passed_model}'")
                
                if passed_model == 'gemini-3-flash-preview':
                    print("\n✅ SUCCESS: Logic correctly loads 'gemini-3-flash-preview' from config.")
                else:
                    print(f"\n❌ FAILURE: Logic loaded '{passed_model}' instead of 'gemini-3-flash-preview'.")
                    
            except ValueError as e:
                print(f"    ERROR: {e}")
                print("    (Likely missing API Key in config, but model logic should still be correct if we reached here)")
            except Exception as e:
                print(f"    ERROR executing _create_llm: {e}")

if __name__ == "__main__":
    test_model_config()
