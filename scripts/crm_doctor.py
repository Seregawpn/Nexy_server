#!/usr/bin/env python3
"""
CRM Doctor - Diagnostic script for CRM data integrity.

Checks:
- Schema and invariants
- blockedBy cycles
- Broken registry_ref
- ID ↔ workspace mismatch
- WIP limits exceeded
- Broken file_path and responsible_docs

Usage:
    python3 scripts/crm_doctor.py [--fix]
    
Options:
    --fix    Attempt to fix simple issues (like missing workspace field)
"""

import json
import os
import sys
import re
from datetime import datetime
from pathlib import Path
from typing import Any

# Configuration
ROOT_DIR = Path(__file__).parent.parent
KANBAN_PATH = ROOT_DIR / "Docs" / "PROJECT_KANBAN.json"
REGISTRY_PATH = ROOT_DIR / "Docs" / "CRM_INSTRUCTION_REGISTRY.md"
CLIENT_TASKS_PATH = ROOT_DIR / "client" / ".crm" / "TASKS.json"
SERVER_TASKS_PATH = ROOT_DIR / "server" / ".crm" / "TASKS.json"

# WIP Limits
MAX_IN_PROGRESS_PER_WORKSPACE = 1
MAX_TESTING_PER_WORKSPACE = 1

# Colors for output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


def load_json(path: Path) -> dict | None:
    """Load JSON file safely."""
    if not path.exists():
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"{Colors.RED}[ERROR]{Colors.RESET} Invalid JSON in {path}: {e}")
        return None


def load_registry() -> dict[str, str]:
    """Parse registry file and return INS-XXX -> file path mapping."""
    registry = {}
    if not REGISTRY_PATH.exists():
        return registry
    
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match table rows: | **INS-XXX** | Title | [File](./path) | Description |
    pattern = r'\|\s*\*?\*?(INS-\d+)\*?\*?\s*\|[^|]+\|\s*\[([^\]]+)\]\(([^)]+)\)'
    for match in re.finditer(pattern, content):
        ins_id = match.group(1)
        file_path = match.group(3)
        # Remove leading ./
        if file_path.startswith('./'):
            file_path = file_path[2:]
        registry[ins_id] = file_path
    
    return registry


class CRMDoctor:
    def __init__(self, fix_mode: bool = False):
        self.fix_mode = fix_mode
        self.errors: list[dict] = []
        self.warnings: list[dict] = []
        self.fixes_applied: list[str] = []
        self.kanban_data: dict | None = None
        self.registry: dict[str, str] = {}
        
    def add_error(self, category: str, task_id: str, message: str, fix_hint: str = ""):
        self.errors.append({
            "category": category,
            "task_id": task_id,
            "message": message,
            "fix_hint": fix_hint
        })
        
    def add_warning(self, category: str, task_id: str, message: str):
        self.warnings.append({
            "category": category,
            "task_id": task_id,
            "message": message
        })
    
    def run_all_checks(self) -> bool:
        """Run all diagnostic checks. Returns True if no errors."""
        print(f"\n{Colors.BLUE}═══════════════════════════════════════════════════════════════{Colors.RESET}")
        print(f"{Colors.BLUE}                    CRM Doctor v1.0                             {Colors.RESET}")
        print(f"{Colors.BLUE}═══════════════════════════════════════════════════════════════{Colors.RESET}\n")
        
        # Load data
        self.kanban_data = load_json(KANBAN_PATH)
        if not self.kanban_data:
            print(f"{Colors.RED}[FATAL]{Colors.RESET} Cannot load {KANBAN_PATH}")
            return False
        
        self.registry = load_registry()
        
        # Run checks
        self.check_schema()
        self.check_required_fields()
        self.check_id_workspace_match()
        self.check_blocked_by_cycles()
        self.check_registry_refs()
        self.check_file_paths()
        self.check_responsible_docs()
        self.check_wip_limits()
        self.check_decision_invariant()
        self.check_stale_tasks()
        
        # Print results
        self.print_results()
        
        return len(self.errors) == 0
    
    def check_schema(self):
        """Check that required top-level keys exist."""
        print(f"[CHECK] Schema validation...")
        required_keys = ["meta", "config", "epics", "cards", "releases"]
        for key in required_keys:
            if key not in self.kanban_data:
                self.add_error("schema", "N/A", f"Missing required key: {key}")
    
    def check_required_fields(self):
        """Check required fields on each card."""
        print(f"[CHECK] Required fields...")
        required = ["id", "title", "status"]
        recommended = ["created_by", "modified_by", "updated_at"]
        
        for card in self.kanban_data.get("cards", []):
            card_id = card.get("id", "UNKNOWN")
            
            for field in required:
                if field not in card:
                    self.add_error("required_field", card_id, f"Missing required field: {field}")
            
            for field in recommended:
                if field not in card:
                    self.add_warning("recommended_field", card_id, f"Missing recommended field: {field}")
    
    def check_id_workspace_match(self):
        """Check that ID prefix matches workspace."""
        print(f"[CHECK] ID ↔ workspace match...")
        prefix_workspace = {
            "NEXY-": "master",
            "CLI-": "client",
            "SRV-": "server"
        }
        
        for card in self.kanban_data.get("cards", []):
            card_id = card.get("id", "")
            workspace = card.get("workspace")
            
            for prefix, expected_ws in prefix_workspace.items():
                if card_id.startswith(prefix):
                    if workspace and workspace != expected_ws and expected_ws != "master":
                        self.add_error(
                            "id_workspace_mismatch", 
                            card_id, 
                            f"ID prefix '{prefix}' expects workspace '{expected_ws}', got '{workspace}'",
                            f"Set workspace to '{expected_ws}'"
                        )
                    break
    
    def check_blocked_by_cycles(self):
        """Detect cycles in blockedBy relationships."""
        print(f"[CHECK] Dependency cycles...")
        
        # Build adjacency list
        graph: dict[str, list[str]] = {}
        for card in self.kanban_data.get("cards", []):
            card_id = card.get("id", "")
            blockers = card.get("blockedBy", [])
            graph[card_id] = blockers
        
        # DFS cycle detection
        visited = set()
        rec_stack = set()
        
        def has_cycle(node: str, path: list[str]) -> list[str] | None:
            if node in rec_stack:
                return path + [node]
            if node in visited:
                return None
            
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in graph.get(node, []):
                cycle = has_cycle(neighbor, path + [node])
                if cycle:
                    return cycle
            
            rec_stack.remove(node)
            return None
        
        for card_id in graph:
            if card_id not in visited:
                cycle = has_cycle(card_id, [])
                if cycle:
                    cycle_str = " → ".join(cycle)
                    self.add_error("cycle", card_id, f"Dependency cycle detected: {cycle_str}")
    
    def check_registry_refs(self):
        """Check that registry_ref values exist in registry."""
        print(f"[CHECK] Registry references...")
        
        for card in self.kanban_data.get("cards", []):
            card_id = card.get("id", "")
            ref = card.get("registry_ref")
            
            if ref and ref not in self.registry:
                self.add_error(
                    "broken_registry_ref",
                    card_id,
                    f"registry_ref '{ref}' not found in CRM_INSTRUCTION_REGISTRY.md"
                )
    
    def check_file_paths(self):
        """Check that file_path exists."""
        print(f"[CHECK] File paths...")
        
        for card in self.kanban_data.get("cards", []):
            card_id = card.get("id", "")
            file_path = card.get("file_path")
            
            if file_path:
                full_path = ROOT_DIR / file_path
                if not full_path.exists():
                    self.add_warning("broken_file_path", card_id, f"file_path '{file_path}' does not exist")
    
    def check_responsible_docs(self):
        """Check that responsible_docs paths exist."""
        print(f"[CHECK] Responsible docs...")
        
        for card in self.kanban_data.get("cards", []):
            card_id = card.get("id", "")
            docs = card.get("responsible_docs", [])
            
            for doc in docs:
                doc_path = doc.get("path", "")
                if doc_path:
                    full_path = ROOT_DIR / doc_path
                    if not full_path.exists():
                        self.add_warning("broken_responsible_doc", card_id, f"responsible_doc '{doc_path}' does not exist")
    
    def check_wip_limits(self):
        """Check WIP limits per workspace."""
        print(f"[CHECK] WIP limits...")
        
        wip_count: dict[str, dict[str, int]] = {
            "master": {"in_progress": 0, "testing": 0},
            "client": {"in_progress": 0, "testing": 0},
            "server": {"in_progress": 0, "testing": 0}
        }
        
        for card in self.kanban_data.get("cards", []):
            card_id = card.get("id", "")
            status = card.get("status", "")
            workspace = card.get("workspace", "master")
            
            # Infer workspace from ID if not set
            if not workspace:
                if card_id.startswith("CLI-"):
                    workspace = "client"
                elif card_id.startswith("SRV-"):
                    workspace = "server"
                else:
                    workspace = "master"
            
            if workspace in wip_count and status in wip_count[workspace]:
                wip_count[workspace][status] += 1
        
        for ws, counts in wip_count.items():
            if counts["in_progress"] > MAX_IN_PROGRESS_PER_WORKSPACE:
                self.add_error(
                    "wip_limit",
                    f"workspace:{ws}",
                    f"WIP limit exceeded: {counts['in_progress']} in_progress (max {MAX_IN_PROGRESS_PER_WORKSPACE})"
                )
            if counts["testing"] > MAX_TESTING_PER_WORKSPACE:
                self.add_error(
                    "wip_limit",
                    f"workspace:{ws}",
                    f"WIP limit exceeded: {counts['testing']} testing (max {MAX_TESTING_PER_WORKSPACE})"
                )
    
    def check_decision_invariant(self):
        """Check that decisions don't have in_progress status."""
        print(f"[CHECK] Decision invariant...")
        
        for card in self.kanban_data.get("cards", []):
            card_id = card.get("id", "")
            card_type = card.get("type", "task")
            status = card.get("status", "")
            
            if card_type == "decision" and status == "in_progress":
                self.add_error(
                    "decision_invariant",
                    card_id,
                    "Decision type cannot have status 'in_progress' (must be plan → released)"
                )
    
    def check_stale_tasks(self):
        """Check for stale tasks based on updated_at."""
        print(f"[CHECK] Stale tasks...")
        
        now = datetime.now()
        
        for card in self.kanban_data.get("cards", []):
            card_id = card.get("id", "")
            status = card.get("status", "")
            updated_str = card.get("updated_at", "")
            
            if not updated_str:
                continue
            
            try:
                # Parse ISO date (handle various formats)
                if 'T' in updated_str:
                    updated = datetime.fromisoformat(updated_str.replace('Z', '+00:00'))
                else:
                    updated = datetime.strptime(updated_str, "%Y-%m-%d")
                
                days_since = (now - updated.replace(tzinfo=None)).days
                
                if status == "in_progress" and days_since > 7:
                    self.add_warning("stale", card_id, f"in_progress without updates for {days_since} days (>7d)")
                elif status == "testing" and days_since > 14:
                    self.add_warning("stale", card_id, f"testing without updates for {days_since} days (>14d)")
                    
            except (ValueError, AttributeError):
                pass  # Skip invalid dates
    
    def print_results(self):
        """Print diagnostic results."""
        print(f"\n{Colors.BLUE}═══════════════════════════════════════════════════════════════{Colors.RESET}")
        print(f"{Colors.BLUE}                         RESULTS                                {Colors.RESET}")
        print(f"{Colors.BLUE}═══════════════════════════════════════════════════════════════{Colors.RESET}\n")
        
        if self.errors:
            print(f"{Colors.RED}ERRORS ({len(self.errors)}):{Colors.RESET}\n")
            for err in self.errors:
                print(f"  {Colors.RED}✗{Colors.RESET} [{err['category']}] {err['task_id']}: {err['message']}")
                if err.get('fix_hint'):
                    print(f"    → Fix: {err['fix_hint']}")
            print()
        
        if self.warnings:
            print(f"{Colors.YELLOW}WARNINGS ({len(self.warnings)}):{Colors.RESET}\n")
            for warn in self.warnings:
                print(f"  {Colors.YELLOW}⚠{Colors.RESET} [{warn['category']}] {warn['task_id']}: {warn['message']}")
            print()
        
        if self.fixes_applied:
            print(f"{Colors.GREEN}FIXES APPLIED ({len(self.fixes_applied)}):{Colors.RESET}\n")
            for fix in self.fixes_applied:
                print(f"  {Colors.GREEN}✓{Colors.RESET} {fix}")
            print()
        
        # Summary
        if not self.errors and not self.warnings:
            print(f"{Colors.GREEN}✓ All checks passed! CRM is healthy.{Colors.RESET}\n")
        elif not self.errors:
            print(f"{Colors.YELLOW}⚠ No errors, but {len(self.warnings)} warnings found.{Colors.RESET}\n")
        else:
            print(f"{Colors.RED}✗ {len(self.errors)} errors, {len(self.warnings)} warnings found.{Colors.RESET}")
            print(f"{Colors.RED}  CRM is NOT healthy. Fix errors before proceeding.{Colors.RESET}\n")


def main():
    fix_mode = "--fix" in sys.argv
    
    doctor = CRMDoctor(fix_mode=fix_mode)
    success = doctor.run_all_checks()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
