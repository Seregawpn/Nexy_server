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
import shutil

PORT = 8000
AGGREGATOR_INTERVAL = 300  # 5 minutes
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(ROOT_DIR, 'Docs')
HTML_PATH = os.path.join(DOCS_DIR, 'PROJECT_KANBAN.html')
JSON_PATH = os.path.join(DOCS_DIR, 'PROJECT_KANBAN.json')
AGGREGATOR_SCRIPT = os.path.join(ROOT_DIR, 'scripts', 'task_aggregator.py')
AUDIT_LOG_PATH = os.path.join(DOCS_DIR, 'CRM_AUDIT_LOG.ndjson')

# Thread lock for atomic operations
save_lock = threading.Lock()

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


def log_audit(action: str, details: dict = None, user: str = "system"):
    """Append entry to audit log (NDJSON format)."""
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "action": action,
        "user": user,
        "details": details or {}
    }
    try:
        with open(AUDIT_LOG_PATH, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    except Exception as e:
        print(f"[Audit] Failed to log: {e}")


def get_current_revision() -> int:
    """Get current revision from JSON file."""
    if not os.path.exists(JSON_PATH):
        return 0
    try:
        with open(JSON_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('meta', {}).get('revision', 0)
    except:
        return 0


def atomic_save(data: dict) -> bool:
    """Atomically save JSON with backup."""
    temp_path = JSON_PATH + '.tmp'
    backup_path = JSON_PATH + '.bak'
    
    try:
        # 1. Increment revision
        if 'meta' not in data:
            data['meta'] = {}
        current_rev = data['meta'].get('revision', 0)
        data['meta']['revision'] = current_rev + 1
        data['meta']['updated_at'] = datetime.datetime.now().isoformat()
        
        # 2. Write to temp file
        with open(temp_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        # 3. Backup existing file
        if os.path.exists(JSON_PATH):
            shutil.copy2(JSON_PATH, backup_path)
        
        # 4. Atomic rename
        os.replace(temp_path, JSON_PATH)
        
        return True
    except Exception as e:
        print(f"[AtomicSave] Error: {e}")
        # Cleanup temp if exists
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return False

def sync_master_to_workspaces(master_data):
    """Sync changes from Master JSON back to Workspace TASKS.json based on Owner field."""
    workspaces = {
        'client': os.path.join(ROOT_DIR, 'client', '.crm', 'TASKS.json'),
        'server': os.path.join(ROOT_DIR, 'server', '.crm', 'TASKS.json')
    }
    
    master_cards = master_data.get('cards', [])
    # Build a map of task ID -> owner for quick lookup
    master_owner_map = {c['id']: c.get('owner') for c in master_cards if c.get('id')}
    
    for ws_name, ws_path in workspaces.items():
        if not os.path.exists(ws_path):
            continue
            
        try:
            with open(ws_path, 'r', encoding='utf-8') as f:
                ws_data = json.load(f)
            
            local_tasks = ws_data.get('tasks', [])
            local_tasks_map = {t['id']: t for t in local_tasks}
            
            updates_count = 0
            removed_count = 0
            
            # 1. Remove tasks that no longer belong to this workspace (Owner changed)
            for tid in list(local_tasks_map.keys()):
                master_owner = master_owner_map.get(tid)
                if master_owner and master_owner != ws_name:
                    # Owner changed to different workspace, remove from here
                    ws_data['tasks'] = [t for t in ws_data['tasks'] if t['id'] != tid]
                    del local_tasks_map[tid]
                    removed_count += 1
            
            # 2. Add/Update tasks that belong to this workspace (based on Owner)
            ws_master_cards = [c for c in master_cards if c.get('owner') == ws_name]
            
            for card in ws_master_cards:
                tid = card['id']
                if tid in local_tasks_map:
                    # Update existing task
                    local_tasks_map[tid].update(card)
                    updates_count += 1
                else:
                    # Add new task to this workspace
                    ws_data['tasks'].append(card)
                    local_tasks_map[tid] = card
                    updates_count += 1
            
            if updates_count > 0 or removed_count > 0:
                with open(ws_path, 'w', encoding='utf-8') as f:
                    json.dump(ws_data, f, indent=4, ensure_ascii=False)
                print(f"[Sync] {ws_name}: Updated {updates_count}, Removed {removed_count}")
                
        except Exception as e:
            print(f"[Sync] Error syncing {ws_name}: {e}")

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
            # Save data to JSON with Schema Validation and Conflict Detection
            try:
                # Validation: Minimal Schema Check
                required_keys = {'meta', 'config', 'epics', 'cards', 'releases'}
                if not isinstance(payload, dict) or not required_keys.issubset(payload.keys()):
                    self.send_error(400, f"Invalid JSON Schema. Missing keys: {required_keys - payload.keys()}")
                    return
                
                # Conflict Detection: Check revision
                client_revision = payload.get('meta', {}).get('revision', 0)
                
                with save_lock:
                    current_revision = get_current_revision()
                    
                    if client_revision < current_revision:
                        # Conflict: client has stale data
                        self.send_response(409)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        self.wfile.write(json.dumps({
                            "error": "conflict",
                            "message": f"Revision conflict. Your revision: {client_revision}, Current: {current_revision}. Please reload and retry.",
                            "current_revision": current_revision
                        }).encode('utf-8'))
                        log_audit("save_conflict", {
                            "client_revision": client_revision,
                            "server_revision": current_revision
                        })
                        return
                    
                    # Atomic save with backup
                    if not atomic_save(payload):
                        self.send_error(500, "Failed to save data")
                        return
                    
                    new_revision = payload['meta']['revision']
                
                # Audit log
                log_audit("save", {
                    "revision": new_revision,
                    "cards_count": len(payload.get('cards', []))
                })
                
                # Sync to workspace files based on Owner field
                threading.Thread(target=sync_master_to_workspaces, args=(payload,), daemon=True).start()
                
                self.send_success({"status": "ok", "message": "Saved", "revision": new_revision})
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
