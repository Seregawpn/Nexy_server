
import asyncio
from typing import Dict, Any, Optional
import json

# Mocking the dependencies
class MockLogger:
    def info(self, msg, extra=None): print(f"[INFO] {msg}")
    def warning(self, msg, extra=None): print(f"[WARN] {msg}")
    def debug(self, msg, extra=None): print(f"[DEBUG] {msg}")
    def error(self, msg, extra=None): print(f"[ERROR] {msg}")

logger = MockLogger()

class AssistantResponseParser:
    def _extract_json_from_markdown(self, text: str) -> str:
        # Simplified version of the one in server code
        text = str(text).strip()
        if text.startswith("```"):
            text = text[3:].lstrip()
            if text.lower().startswith("json"): text = text[4:].lstrip()
            if text.endswith("```"): text = text[:-3]
        
        first_brace = text.find("{")
        last_brace = text.rfind("}")
        if first_brace != -1 and last_brace != -1 and first_brace < last_brace:
            return text[first_brace:last_brace+1]
        return text

    def parse(self, response, session_id=None):
        return self._parse_string(response, session_id)

    def _parse_string(self, response_str, session_id=None):
        # Very simplified mock
        cleaned = self._extract_json_from_markdown(response_str)
        try:
            data = json.loads(cleaned)
            return type('ParsedResponse', (), {'text_response': data.get('text', ''), 'command_payload': {'msg': 'mock_command'} if 'command' in data else None})
        except:
             return type('ParsedResponse', (), {'text_response': response_str, 'command_payload': None})

# Simplified Logic from StreamingWorkflowIntegration to test buffering
async def simulate_streaming(chunks):
    parser = AssistantResponseParser()
    json_buffer = ""
    MAX_JSON_BUFFER_SIZE = 1000
    
    print("\n--- Starting Simulation ---")
    for sentence in chunks:
        print(f"\nProcessing chunk: '{sentence}'")
        
        if len(json_buffer) + len(sentence) > MAX_JSON_BUFFER_SIZE:
             print("buffer full")
             json_buffer = ""
        else:
            json_buffer += sentence
            
            cleaned_buffer = parser._extract_json_from_markdown(json_buffer)
            is_potential_json = cleaned_buffer.strip().startswith('{')
            
            print(f"Current Buffer: '{json_buffer}'")
            print(f"Cleaned Buffer: '{cleaned_buffer}'")
            print(f"Is Potential JSON: {is_potential_json}")
            
            if is_potential_json:
                try:
                    parsed_json = json.loads(cleaned_buffer)
                    print("✅ JSON Parsed Successfully!")
                    print(f"Parsed Command: {parsed_json.get('command')}")
                    json_buffer = "" # Clear after success
                except json.JSONDecodeError:
                    print(f"⏳ JSON incomplete, buffering...")
            else:
                print(f"❌ Not JSON. Flushing as text: '{json_buffer}'")
                json_buffer = ""

async def main():
    # Scenario 3: Partial Mixed Text + JSON
    print("\n--- Starting Simulation (Partial Mixed Chunk) ---")
    chunks = [
        "Opening Telegram. { \"command\": \"open_app\", ",
        "\"text\": \"Opening Telegram\" }"
    ]
    await simulate_streaming(chunks)

if __name__ == "__main__":
    asyncio.run(main())
