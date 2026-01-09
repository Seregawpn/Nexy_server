#!/usr/bin/env python3
"""
CRM Housekeeper - Automated cleanup and maintenance for CRM.

Actions:
- Mark stale tasks (in_progress > 7d, testing > 14d)
- Archive old plan tasks (> 30d without updates)
- Check for broken links (responsible_docs, file_path, registry_ref)
- Create problem tasks for anomalies

Usage:
    python3 scripts/crm_housekeeper.py [--dry-run]
    
Options:
    --dry-run    Show what would be done without making changes
"""

import json
import os
import sys
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

# Configuration
ROOT_DIR = Path(__file__).parent.parent
KANBAN_PATH = ROOT_DIR / "Docs" / "PROJECT_KANBAN.json"
REGISTRY_PATH = ROOT_DIR / "Docs" / "CRM_INSTRUCTION_REGISTRY.md"
AUDIT_LOG_PATH = ROOT_DIR / "Docs" / "CRM_AUDIT_LOG.ndjson"

# Housekeeping thresholds (from CRM_CONSOLIDATED_RULES.md)
STALE_IN_PROGRESS_DAYS = 7
STALE_TESTING_DAYS = 14
STALE_PLAN_DAYS = 30

# Colors for output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
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


def save_json(path: Path, data: dict) -> bool:
    """Save JSON with atomic write."""
    temp_path = path.with_suffix('.tmp')
    backup_path = path.with_suffix('.bak')
    
    try:
        # Increment revision
        if 'meta' not in data:
            data['meta'] = {}
        current_rev = data['meta'].get('revision', 0)
        data['meta']['revision'] = current_rev + 1
        data['meta']['updated_at'] = datetime.now().isoformat()
        
        # Write to temp
        with open(temp_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        # Backup existing
        if path.exists():
            import shutil
            shutil.copy2(path, backup_path)
        
        # Atomic rename
        os.replace(temp_path, path)
        return True
    except Exception as e:
        print(f"{Colors.RED}[ERROR]{Colors.RESET} Failed to save: {e}")
        if temp_path.exists():
            temp_path.unlink()
        return False


def log_audit(action: str, details: dict = None):
    """Append to audit log."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "user": "housekeeper",
        "details": details or {}
    }
    try:
        with open(AUDIT_LOG_PATH, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    except Exception as e:
        print(f"{Colors.YELLOW}[WARN]{Colors.RESET} Failed to log: {e}")


def load_registry() -> dict[str, str]:
    """Parse registry file and return INS-XXX -> file path mapping."""
    registry = {}
    if not REGISTRY_PATH.exists():
        return registry
    
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'\|\s*\*?\*?(INS-\d+)\*?\*?\s*\|[^|]+\|\s*\[([^\]]+)\]\(([^)]+)\)'
    for match in re.finditer(pattern, content):
        ins_id = match.group(1)
        file_path = match.group(3)
        if file_path.startswith('./'):
            file_path = file_path[2:]
        registry[ins_id] = file_path
    
    return registry


def parse_date(date_str: str) -> datetime | None:
    """Parse ISO date string to datetime."""
    if not date_str:
        return None
    try:
        if 'T' in date_str:
            # Remove timezone suffix for simplicity
            date_str = date_str.split('+')[0].split('-05:00')[0].split('Z')[0]
            return datetime.fromisoformat(date_str)
        else:
            return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        return None


def get_next_nexy_id(cards: list) -> str:
    """Get next available NEXY-XXX ID."""
    max_num = 0
    for card in cards:
        card_id = card.get('id', '')
        if card_id.startswith('NEXY-'):
            try:
                num = int(card_id.split('-')[1])
                max_num = max(max_num, num)
            except:
                pass
    return f"NEXY-{max_num + 1:03d}"


class CRMHousekeeper:
    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self.data: dict | None = None
        self.registry: dict[str, str] = {}
        self.actions: list[str] = []
        self.problems: list[dict] = []
        
    def run(self) -> bool:
        """Run all housekeeping tasks."""
        print(f"\n{Colors.BLUE}═══════════════════════════════════════════════════════════════{Colors.RESET}")
        print(f"{Colors.BLUE}                  CRM Housekeeper v1.0                          {Colors.RESET}")
        if self.dry_run:
            print(f"{Colors.YELLOW}                     (DRY RUN MODE)                             {Colors.RESET}")
        print(f"{Colors.BLUE}═══════════════════════════════════════════════════════════════{Colors.RESET}\n")
        
        # Load data
        self.data = load_json(KANBAN_PATH)
        if not self.data:
            print(f"{Colors.RED}[FATAL]{Colors.RESET} Cannot load {KANBAN_PATH}")
            return False
        
        self.registry = load_registry()
        
        # Run tasks
        self.mark_stale_tasks()
        self.archive_old_tasks()
        self.check_broken_links()
        self.create_problem_tasks()
        
        # Save if not dry run
        if not self.dry_run and self.actions:
            if save_json(KANBAN_PATH, self.data):
                log_audit("housekeeper_run", {
                    "actions_count": len(self.actions),
                    "problems_found": len(self.problems)
                })
                print(f"\n{Colors.GREEN}✓ Changes saved.{Colors.RESET}")
            else:
                print(f"\n{Colors.RED}✗ Failed to save changes.{Colors.RESET}")
                return False
        
        # Print summary
        self.print_summary()
        return True
    
    def mark_stale_tasks(self):
        """Mark tasks as stale based on updated_at."""
        print(f"[TASK] Checking for stale tasks...")
        now = datetime.now()
        
        for card in self.data.get('cards', []):
            card_id = card.get('id', '')
            status = card.get('status', '')
            updated_at = parse_date(card.get('updated_at', ''))
            
            if not updated_at:
                continue
            
            days_since = (now - updated_at).days
            
            # Skip already stale or archived
            if card.get('stale') or card.get('archived'):
                continue
            
            stale_reason = None
            
            if status == 'in_progress' and days_since > STALE_IN_PROGRESS_DAYS:
                stale_reason = f"no_updates_{days_since}d"
                # Return to plan
                if not self.dry_run:
                    card['status'] = 'plan'
                    card['stale'] = True
                    card['stale_since'] = now.isoformat()
                    card['stale_reason'] = stale_reason
                    # Add note to description
                    note = f"\n\n**[{now.strftime('%Y-%m-%d')}] Auto-marked stale:** " \
                           f"No updates for {days_since} days. Returned to plan."
                    card['description'] = card.get('description', '') + note
                
                action = f"STALE: {card_id} (in_progress > {STALE_IN_PROGRESS_DAYS}d) → plan"
                self.actions.append(action)
                print(f"  {Colors.YELLOW}⚠{Colors.RESET} {action}")
            
            elif status == 'testing' and days_since > STALE_TESTING_DAYS:
                stale_reason = f"no_updates_{days_since}d"
                if not self.dry_run:
                    card['stale'] = True
                    card['stale_since'] = now.isoformat()
                    card['stale_reason'] = stale_reason
                
                action = f"STALE: {card_id} (testing > {STALE_TESTING_DAYS}d)"
                self.actions.append(action)
                print(f"  {Colors.YELLOW}⚠{Colors.RESET} {action}")
    
    def archive_old_tasks(self):
        """Archive plan tasks with no updates > 30 days."""
        print(f"[TASK] Checking for archivable tasks...")
        now = datetime.now()
        
        for card in self.data.get('cards', []):
            card_id = card.get('id', '')
            status = card.get('status', '')
            updated_at = parse_date(card.get('updated_at', ''))
            
            if not updated_at:
                continue
            
            # Skip already archived
            if card.get('archived'):
                continue
            
            days_since = (now - updated_at).days
            
            if status == 'plan' and days_since > STALE_PLAN_DAYS:
                if not self.dry_run:
                    card['archived'] = True
                    card['archived_at'] = now.isoformat()
                    card['archive_reason'] = f"stale_plan_{days_since}d"
                
                action = f"ARCHIVE: {card_id} (plan > {STALE_PLAN_DAYS}d)"
                self.actions.append(action)
                print(f"  {Colors.MAGENTA}📦{Colors.RESET} {action}")
    
    def check_broken_links(self):
        """Check for broken file_path, responsible_docs, registry_ref."""
        print(f"[TASK] Checking for broken links...")
        
        for card in self.data.get('cards', []):
            card_id = card.get('id', '')
            
            # Check file_path
            file_path = card.get('file_path')
            if file_path:
                full_path = ROOT_DIR / file_path
                if not full_path.exists():
                    self.problems.append({
                        'type': 'broken_file_path',
                        'task': card_id,
                        'path': file_path
                    })
                    print(f"  {Colors.RED}✗{Colors.RESET} {card_id}: broken file_path '{file_path}'")
            
            # Check responsible_docs
            for doc in card.get('responsible_docs', []):
                doc_path = doc.get('path', '')
                if doc_path:
                    full_path = ROOT_DIR / doc_path
                    if not full_path.exists():
                        self.problems.append({
                            'type': 'broken_responsible_doc',
                            'task': card_id,
                            'path': doc_path
                        })
                        print(f"  {Colors.RED}✗{Colors.RESET} {card_id}: broken responsible_doc '{doc_path}'")
            
            # Check registry_ref
            ref = card.get('registry_ref')
            if ref and ref not in self.registry:
                self.problems.append({
                    'type': 'broken_registry_ref',
                    'task': card_id,
                    'ref': ref
                })
                print(f"  {Colors.RED}✗{Colors.RESET} {card_id}: broken registry_ref '{ref}'")
    
    def create_problem_tasks(self):
        """Create NEXY-* problem task if anomalies found."""
        if not self.problems:
            return
        
        print(f"[TASK] Creating problem task for {len(self.problems)} issues...")
        
        # Build description
        desc = "## Обнаруженные проблемы\n\n"
        desc += f"Найдено **{len(self.problems)}** проблем при запуске housekeeper:\n\n"
        
        for p in self.problems:
            if p['type'] == 'broken_file_path':
                desc += f"- **{p['task']}**: Broken `file_path`: `{p['path']}`\n"
            elif p['type'] == 'broken_responsible_doc':
                desc += f"- **{p['task']}**: Broken `responsible_doc`: `{p['path']}`\n"
            elif p['type'] == 'broken_registry_ref':
                desc += f"- **{p['task']}**: Broken `registry_ref`: `{p['ref']}`\n"
        
        desc += "\n## Рекомендации\n\n"
        desc += "1. Проверить существование указанных файлов\n"
        desc += "2. Обновить ссылки или удалить битые поля\n"
        desc += "3. Запустить `crm_doctor.py` для полной диагностики\n"
        
        new_id = get_next_nexy_id(self.data.get('cards', []))
        
        problem_task = {
            "id": new_id,
            "type": "problem",
            "title": "CRM Link Rot / Broken References",
            "status": "plan",
            "priority": "P2",
            "workspace": "master",
            "created_by": "Housekeeper",
            "modified_by": "Housekeeper",
            "updated_at": datetime.now().isoformat(),
            "description": desc
        }
        
        if not self.dry_run:
            self.data['cards'].append(problem_task)
        
        action = f"CREATE: {new_id} (type: problem) - {len(self.problems)} issues"
        self.actions.append(action)
        print(f"  {Colors.GREEN}+{Colors.RESET} {action}")
    
    def print_summary(self):
        """Print summary of actions."""
        print(f"\n{Colors.BLUE}═══════════════════════════════════════════════════════════════{Colors.RESET}")
        print(f"{Colors.BLUE}                         SUMMARY                                {Colors.RESET}")
        print(f"{Colors.BLUE}═══════════════════════════════════════════════════════════════{Colors.RESET}\n")
        
        if self.actions:
            print(f"Actions performed: {len(self.actions)}")
            for action in self.actions:
                print(f"  • {action}")
        else:
            print(f"{Colors.GREEN}✓ No housekeeping needed. CRM is clean.{Colors.RESET}")
        
        if self.dry_run and self.actions:
            print(f"\n{Colors.YELLOW}[DRY RUN] No changes were saved.{Colors.RESET}")
            print(f"{Colors.YELLOW}Run without --dry-run to apply changes.{Colors.RESET}")


def main():
    dry_run = "--dry-run" in sys.argv
    
    housekeeper = CRMHousekeeper(dry_run=dry_run)
    success = housekeeper.run()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
