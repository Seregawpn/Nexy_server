import os
import sys
print("✅ SUCCESS: You are running python from the correct directory!")
print(f"Current Directory: {os.getcwd()}")
try:
    with open('client/integration/integrations/whatsapp_integration.py', 'r') as f:
        content = f.read()
        if "DEBUG: RUNNING NEW WHATSAPP INTEGRATION" in content:
            print("✅ File Check: whatsapp_integration.py contains the new debug code.")
        else:
            print("❌ File Check: whatsapp_integration.py DOES NOT contain the new debug code (File on disk is old!).")
except Exception as e:
    print(f"❌ File Check Failed: {e}")
