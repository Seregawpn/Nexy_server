import sys
import os
import asyncio
from unittest.mock import MagicMock, AsyncMock

import pytest

pytestmark = pytest.mark.skip(reason="Manual verification script, excluded from pytest suite")

# Add client to path so imports work
current_dir = os.getcwd()
client_dir = os.path.join(current_dir, 'client')
sys.path.insert(0, client_dir)

# Mock external dependencies
sys.modules['langchain_google_genai'] = MagicMock()
# Mock external dependencies with structure
browser_use = MagicMock()
sys.modules['browser_use'] = browser_use

llm = MagicMock()
views = MagicMock()
# We need to assign them to parent
browser_use.llm = llm
llm.views = views

# Register submodules
sys.modules['browser_use.llm'] = llm
sys.modules['browser_use.llm.views'] = views

# Mock classes used in ainvoke
class MockChatInvokeCompletion:
    def __init__(self, completion, usage, **kwargs):
        self.completion = completion
        self.usage = usage
        self.kwargs = kwargs

class MockChatInvokeUsage:
    def __init__(self, **kwargs):
        pass

views.ChatInvokeCompletion = MockChatInvokeCompletion
views.ChatInvokeUsage = MockChatInvokeUsage

# Now import the module
from modules.browser_automation.module import GeminiLLMAdapter

async def test_token_extraction():
    print("=== Testing Token Usage Extraction in GeminiLLMAdapter ===")
    
    # 1. Setup Mock LLM Response
    # Emulate the structure of a LangChain AIMessage with usage_metadata
    mock_response = MagicMock()
    mock_response.content = "Test response content"
    mock_response.usage_metadata = {
        'input_tokens': 123,
        'output_tokens': 45,
        'total_tokens': 168
    }
    
    # 2. Setup Adapter with Callback
    callback_mock = MagicMock()
    target_model = "gemini-3-flash-preview"
    
    print(f"Initializing adapter with model: {target_model}")
    adapter = GeminiLLMAdapter(
        api_key="fake_key",
        model=target_model,
        usage_callback=callback_mock
    )
    
    # Mock internal _llm.ainvoke to return our fake response
    adapter._llm.ainvoke = AsyncMock(return_value=mock_response)
    
    # 3. Execute
    print("Invoking adapter.ainvoke()...")
    # BrowserUse passes messages list
    messages = [{"role": "user", "content": "Hello"}] 
    await adapter.ainvoke(messages)
    
    # 4. Verify
    print("\n=== Verification Results ===")
    if callback_mock.called:
        args = callback_mock.call_args[0]
        # Signature: (input_tokens, output_tokens, model_name)
        input_tokens, output_tokens, model = args
        
        print(f"Callback invoked with:")
        print(f"  - Input Tokens:  {input_tokens}")
        print(f"  - Output Tokens: {output_tokens}")
        print(f"  - Model Name:    {model}")
        
        # Assertions
        try:
            assert input_tokens == 123, f"Expected 123 input tokens, got {input_tokens}"
            assert output_tokens == 45, f"Expected 45 output tokens, got {output_tokens}"
            assert model == target_model, f"Expected model '{target_model}', got '{model}'"
            print("\n✅ SUCCESS: Token usage information correctly extracted and reported.")
        except AssertionError as e:
            print(f"\n❌ FAILED assertion: {e}")
    else:
        print("\n❌ FAILED: Callback was NOT called.")

if __name__ == "__main__":
    asyncio.run(test_token_extraction())
