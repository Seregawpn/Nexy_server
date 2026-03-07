import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
# /Users/sergiyzasorin/Fix_new/server
server_dir = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, server_dir)

print(f"Added to path: {server_dir}")
print("sys.path:", sys.path)

try:
    import server
    print(f"✅ Imported server: {server}")
    print(f"server path: {server.__path__}")
except Exception as e:
    print(f"❌ Import server failed: {e}")

try:
    import server.modules
    print(f"✅ Imported server.modules: {server.modules}")
except Exception as e:
    print(f"❌ Import server.modules failed: {e}")

try:
    import server.server.modules
    print(f"✅ Imported server.server.modules: {server.server.modules}")
except Exception as e:
    print(f"❌ Import server.server.modules failed: {e}")
