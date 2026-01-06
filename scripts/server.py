#!/usr/bin/env python3
import http.server
import socketserver
import json
import os
import subprocess
import urllib.parse
import sys
import shlex
import datetime
import threading
import time

PORT = 8000
AGGREGATOR_INTERVAL = 300  # 5 minutes
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(ROOT_DIR, 'Docs')
HTML_PATH = os.path.join(DOCS_DIR, 'PROJECT_KANBAN.html')
JSON_PATH = os.path.join(DOCS_DIR, 'PROJECT_KANBAN.json')
AGGREGATOR_SCRIPT = os.path.join(ROOT_DIR, 'scripts', 'task_aggregator.py')

# Background aggregator thread
def run_aggregator():
    """Run task_aggregator.py to sync workspace tasks."""
    if os.path.exists(AGGREGATOR_SCRIPT):
        try:
            result = subprocess.run(
                [sys.executable, AGGREGATOR_SCRIPT],
                capture_output=True,
                text=True,
                cwd=ROOT_DIR
            )
            if result.returncode == 0:
                print(f"[Aggregator] Synced at {datetime.datetime.now().strftime('%H:%M:%S')}")
            else:
                print(f"[Aggregator] Error: {result.stderr}")
        except Exception as e:
            print(f"[Aggregator] Exception: {e}")

def aggregator_loop():
    """Background loop that runs aggregator periodically."""
    while True:
        run_aggregator()
        time.sleep(AGGREGATOR_INTERVAL)

class BridgeHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve the app at root
        if self.path == '/' or self.path == '/index.html':
            if os.path.exists(HTML_PATH):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                with open(HTML_PATH, 'rb') as f:
                    self.wfile.write(f.read())
                return
            else:
                self.send_error(404, f"File not found: {HTML_PATH}")
                return

        # API: Get Data
        if self.path == '/api/data':
            if os.path.exists(JSON_PATH):
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                with open(JSON_PATH, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(b'{}') # Empty JSON if file missing
            return

        # Allow serving other static files from Root (for images/screenshots)
        # Security: Normalize path to prevent escape
        safe_path = os.path.normpath(os.path.join(ROOT_DIR, self.path.lstrip('/')))
        if safe_path.startswith(ROOT_DIR) and os.path.exists(safe_path) and os.path.isfile(safe_path):
             super().do_GET()
             return
        
        self.send_error(404)

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode('utf-8')
        try:
            payload = json.loads(body)
        except:
            payload = {}

        if self.path == '/api/save':
            # Save data to JSON with Schema Validation
            try:
                # Validation: Minimal Schema Check
                required_keys = {'meta', 'config', 'epics', 'cards', 'releases'}
                if not isinstance(payload, dict) or not required_keys.issubset(payload.keys()):
                    self.send_error(400, f"Invalid JSON Schema. Missing keys: {required_keys - payload.keys()}")
                    return

                with open(JSON_PATH, 'w', encoding='utf-8') as f:
                    json.dump(payload, f, indent=4, ensure_ascii=False)
                self.send_success({"status": "ok", "message": "Saved"})
            except Exception as e:
                self.send_error(500, str(e))
            return

        if self.path == '/api/open_file':
            # Open file in editor (CRM_EDITOR_CMD or default)
            # Payload: {"path": "relative/path"}
            file_path = payload.get('path')
            if file_path:
                full_path = os.path.normpath(os.path.join(ROOT_DIR, file_path))
                if full_path.startswith(ROOT_DIR) and os.path.exists(full_path):
                    print(f"Opening file: {full_path}")
                    try:
                        editor_cmd = os.environ.get('CRM_EDITOR_CMD')
                        if editor_cmd:
                            # Use configured editor safely (no shell=True)
                            args = shlex.split(editor_cmd) + [full_path]
                            subprocess.run(args)
                        else:
                            # Fallback: macOS 'open'
                            subprocess.run(['open', full_path]) 
                        self.send_success({"status": "ok"})
                    except Exception as e:
                        self.send_error(500, str(e))
                else:
                    self.send_error(404, "File not found or invalid path")
            else:
                self.send_error(400, "Missing path")
            return

        if self.path == '/api/create_release':
            # Create Release: Archive cards, Update Changelog
            version = payload.get('version')
            if not version:
                self.send_error(400, "Missing version")
                return

            try:
                if not os.path.exists(JSON_PATH):
                    self.send_error(500, "Database not found")
                    return

                with open(JSON_PATH, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Filter 'released' cards
                active_cards = []
                released_cards = []
                for card in data.get('cards', []):
                    if card.get('status') == 'released':
                        released_cards.append(card)
                    else:
                        active_cards.append(card)

                if not released_cards:
                    self.send_error(400, "No cards in 'released' status")
                    return

                # Create Release Object
                new_release = {
                    "version": version,
                    "date": datetime.date.today().isoformat(),
                    "card_ids": [c['id'] for c in released_cards],
                    "count": len(released_cards)
                }
                
                # Update JSON
                data['cards'] = active_cards
                if 'releases' not in data: data['releases'] = []
                data['releases'].append(new_release)

                # Update CHANGELOG.md
                changelog_path = os.path.join(DOCS_DIR, 'CHANGELOG.md')
                date_str = datetime.date.today().isoformat()
                entry = f"\n## [{version}] - {date_str}\n"
                for c in released_cards:
                    owner = f" (@{c.get('owner', 'Unknown')})" if c.get('owner') else ""
                    entry += f"- **{c['id']}**: {c['title']}{owner}\n"
                
                existing_content = ""
                if os.path.exists(changelog_path):
                    with open(changelog_path, 'r', encoding='utf-8') as f:
                        existing_content = f.read()
                else:
                    existing_content = "# Changelog\n\nAll notable changes to this project will be documented in this file.\n"

                # Insert after header if possible, else append
                if "# Changelog" in existing_content:
                    parts = existing_content.split('\n', 2) # Split after header? No.
                    # Simple append for MVP might be safer? 
                    # User asked for standard format. 
                    # Let's Prepend logic: Newest first.
                    # Find first header line? 
                    # If start with # Changelog, insert after it.
                    if existing_content.startswith("# Changelog"):
                         # Split by first newline likely 
                         # A bit complex to regex. 
                         # Let's just append to top after first line.
                         lines = existing_content.splitlines()
                         lines.insert(2, entry) # Insert after Title + Empty line
                         final_content = "\n".join(lines)
                    else:
                         final_content = entry + "\n" + existing_content
                else:
                    final_content = "# Changelog\n" + entry + "\n" + existing_content

                with open(changelog_path, 'w', encoding='utf-8') as f:
                    f.write(final_content)

                # Save JSON
                with open(JSON_PATH, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                
                self.send_success({
                    "status": "ok", 
                    "message": f"Release {version} created with {len(released_cards)} tasks."
                })

            except Exception as e:
                self.send_error(500, str(e))
            return

        # /api/exec REMOVED for security compliance
        # Only open_file and save_json are allowed.
        if self.path == '/api/exec':
            self.send_error(403, "Execution disabled by policy")
            return

        self.send_error(404)

    def send_success(self, data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

# Set working directory to Root to allow relative path serving
os.chdir(ROOT_DIR)

print(f"Starting Local Bridge Server at http://localhost:{PORT}")
print(f"Root: {ROOT_DIR}")
print(f"Serving App: {HTML_PATH}")
print(f"Auto-aggregation: every {AGGREGATOR_INTERVAL}s")

# Start background aggregator thread
aggregator_thread = threading.Thread(target=aggregator_loop, daemon=True)
aggregator_thread.start()

with socketserver.TCPServer(("127.0.0.1", PORT), BridgeHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
