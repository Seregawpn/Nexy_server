import asyncio
import os
import sys

# Add server directory to path PRIORITY
server_path = os.path.join(os.getcwd(), 'server', 'server')
sys.path.insert(0, server_path)
print(f"Added {server_path} to sys.path[0]")

# Mock config
class MockConfig:
    def get(self, key, default=None):
        if key == 'keep_browser_open':
            return True
        return default

class MockContext:
    async def close(self, force=False):
        print(f"MockContext closed (force={force})")

class MockBrowserSession:
    def __init__(self):
        self.context = MockContext()
        self.browser = "MockBrowser"
    def __repr__(self):
        return f"<MockBrowserSession id={id(self)}>"

# Mock Agent to intercept initialization
class MockAgent:
    def __init__(self, task, llm, browser_session=None, browser_profile=None, **kwargs):
        self.browser_session = browser_session or MockBrowserSession()
        self.browser_profile = browser_profile
        print(f"Agent initialized. Reuse Session: {browser_session is not None}")
        if browser_session:
             print(f"Session ID: {id(browser_session)}")
        else:
             print(f"New Session Created: {id(self.browser_session)}")

        if browser_profile:
            print(f"browser_profile.keep_alive: {browser_profile.keep_alive}")
    
    async def run(self, max_steps=10):
        print("Agent running...")
        pass

# Patch modules
import builtins
builtins.BROWSER_USE_AVAILABLE = True

# Mock browser_use imports
import types
browser_use = types.ModuleType('browser_use')
browser_use.Agent = MockAgent
browser_use.ChatGoogle = lambda **kwargs: "MockLLM"
sys.modules['browser_use'] = browser_use

browser_use_profile = types.ModuleType('browser_use.browser.profile')
class MockBrowserProfile:
    def __init__(self, keep_alive=False):
        self.keep_alive = keep_alive
    def __repr__(self):
        return f"BrowserProfile(keep_alive={self.keep_alive})"
browser_use_profile.BrowserProfile = MockBrowserProfile
sys.modules['browser_use.browser.profile'] = browser_use_profile

# Import module under test
from modules.browser_use.module import BrowserUseModule
import inspect

async def test_module_init():
    print(f"Loaded BrowserUseModule from: {sys.modules['modules.browser_use.module'].__file__}")
    try:
        print("Source of close_browser:")
        print(inspect.getsource(BrowserUseModule.close_browser))
        print("Source of __init__:")
        print(inspect.getsource(BrowserUseModule.__init__))
    except Exception as e:
        print(f"Could not get source: {e}")

    print("Testing BrowserUseModule initialization...")
    module = BrowserUseModule()
    # Mock config loading/injection
    module._config = {'keep_browser_open': True}
    module._keep_browser_open = True  # CRITICAL: Set the flag manually since we skip initialize()
    
    print("\n--- Test 1: First Task (Should create new session with keep_alive=True) ---")
    module._create_llm = lambda: "MockLLM"
    
    # We need to access the async generator
    async for _ in module.process({'args': {'task': 'test1'}, 'session_id': 'test-session'}):
        pass
        
    print("\n--- Test 2: Second Task (Should REUSE session) ---")
    async for _ in module.process({'args': {'task': 'test2'}, 'session_id': 'test-session'}):
        pass

    print("\n--- Test 3: Explicit Close ---")
    await module.close_browser()

if __name__ == "__main__":
    asyncio.run(test_module_init())
