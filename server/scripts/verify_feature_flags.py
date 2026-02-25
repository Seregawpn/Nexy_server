#!/usr/bin/env python3
"""
Verify feature flags and kill-switches are registered in FEATURE_FLAGS.md (Server).

**Цель**: Автоматическая проверка, что все флаги в коде зарегистрированы в реестре.

**Логика**:
1. Парсит FEATURE_FLAGS.md и извлекает все name (первая колонка таблицы)
2. Ищет в коде:
   - env-флаги: NEXY_KS_*, NEXY_DISABLE_* (regex)
   - config-флаги: features.* и kill_switches.* в unified_config.yaml и в Python коде
3. Если в коде есть флаг, которого нет в реестре — скрипт падает с ошибкой и путём файла

**Использование**:
    # Проверка регистрации всех флагов
    python scripts/verify_feature_flags.py
    
    # Discovery режим: найти все флаги в указанном модуле/пути
    python scripts/verify_feature_flags.py --module <path>
    python scripts/verify_feature_flags.py --module modules/grpc_service/core/grpc_server.py

**Exit codes**:
    0 — все флаги зарегистрированы (или discovery успешно выполнен)
    1 — найдены незарегистрированные флаги

See Docs/SERVER_DEVELOPMENT_RULES.md section 8 for requirements.
"""
import re
import sys
import yaml
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from dataclasses import dataclass

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Root directory (server/server/)
ROOT = Path(__file__).parent.parent

# Excluded directories from search
EXCLUDED_DIRS = {".git", ".venv", "build", "dist", "__pycache__", "vendor_binaries", "resources", "experiments"}

# Excluded files/directories (legacy, archives, templates, etc.)
EXCLUDED_PATHS = {
    "_archive",
    "FEATURE_FLAGS.md",  # Don't check the registry itself
    "verify_feature_flags.py",  # Don't check this script
    "templates",  # Template files may contain example flags
    "change_impact.yaml",  # Template files
    "ADRs",  # ADR files may contain example flags
}


@dataclass
class FlagMetadata:
    """Metadata for a feature flag from the registry."""
    name: str
    type: str  # feature or kill_switch
    owner: str
    default: str
    scope: str
    kill_switch: str  # "-" if none
    description: str


@dataclass
class FlagLocation:
    """Location information for a flag usage."""
    file_path: str
    line_num: int
    code_line: str
    func_or_class: Optional[str]


def load_feature_flags_registry() -> Set[str]:
    """
    Load feature flags from FEATURE_FLAGS.md.
    
    Returns:
        Set of flag names found in the registry (both env and config flags).
    """
    flags_md = ROOT / "Docs" / "FEATURE_FLAGS.md"
    if not flags_md.exists():
        print(f"{RED}ERROR: FEATURE_FLAGS.md not found at {flags_md}{RESET}", file=sys.stderr)
        return set()
    
    flags = set()
    try:
        with open(flags_md, "r", encoding="utf-8") as f:
            content = f.read()
            
            # Extract flag names from markdown table
            # Format: | `FLAG_NAME` | type | owner | ...
            pattern = r"^\| `([^`]+)` \|"
            for line in content.split("\n"):
                match = re.match(pattern, line.strip())
                if match:
                    flag_name = match.group(1)
                    flags.add(flag_name)
                    
            # Also check for flags without backticks (legacy format)
            pattern_legacy = r"^\| `?([A-Z_][A-Z0-9_]+)`? \|"
            for line in content.split("\n"):
                match = re.match(pattern_legacy, line.strip())
                if match:
                    flag_name = match.group(1)
                    # Accept both env flags (NEXY_*) and config flags (lowercase_with_underscores)
                    flags.add(flag_name)
                        
    except Exception as e:
        print(f"{YELLOW}Warning: Could not parse FEATURE_FLAGS.md: {e}{RESET}", file=sys.stderr)
    
    return flags


def load_config_flags_from_yaml() -> Set[str]:
    """
    Load all config flags from unified_config.yaml.
    
    Returns:
        Set of flag names from features.* and kill_switches.* sections.
    """
    config_path = ROOT / "config" / "unified_config.yaml"
    if not config_path.exists():
        return set()
    
    flags = set()
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
            
            # Extract features.* flags
            features = config.get("features", {})
            if isinstance(features, dict):
                for key in features.keys():
                    flags.add(key)
            
            # Extract kill_switches.* flags
            kill_switches = config.get("kill_switches", {})
            if isinstance(kill_switches, dict):
                for key in kill_switches.keys():
                    flags.add(key)
            
    except Exception as e:
        print(f"{YELLOW}Warning: Could not parse unified_config.yaml: {e}{RESET}", file=sys.stderr)
    
    return flags


def load_feature_flags_registry_with_metadata() -> Dict[str, FlagMetadata]:
    """
    Load feature flags from FEATURE_FLAGS.md with full metadata.
    
    Returns:
        Dict mapping flag name -> FlagMetadata.
    """
    flags_md = ROOT / "Docs" / "FEATURE_FLAGS.md"
    if not flags_md.exists():
        print(f"{RED}ERROR: FEATURE_FLAGS.md not found at {flags_md}{RESET}", file=sys.stderr)
        return {}
    
    flags_metadata = {}
    try:
        with open(flags_md, "r", encoding="utf-8") as f:
            content = f.read()
            
            # Parse markdown table
            # Format: | `name` | type | owner | default | scope | kill_switch | description |
            lines = content.split("\n")
            in_table = False
            
            for line in lines:
                line = line.strip()
                if line.startswith("| name |"):
                    in_table = True
                    continue
                if in_table and line.startswith("|---"):
                    continue
                if in_table and line.startswith("|"):
                    # Parse table row
                    parts = [p.strip() for p in line.split("|")[1:-1]]  # Skip first and last empty
                    if len(parts) >= 7:
                        name = parts[0].strip("`")
                        type_val = parts[1].strip()
                        owner = parts[2].strip()
                        default = parts[3].strip()
                        scope = parts[4].strip()
                        kill_switch = parts[5].strip()
                        description = parts[6].strip()
                        
                        flags_metadata[name] = FlagMetadata(
                            name=name,
                            type=type_val,
                            owner=owner,
                            default=default,
                            scope=scope,
                            kill_switch=kill_switch,
                            description=description
                        )
                elif in_table and not line.startswith("|"):
                    # End of table
                    break
                        
    except Exception as e:
        print(f"{YELLOW}Warning: Could not parse FEATURE_FLAGS.md: {e}{RESET}", file=sys.stderr)
    
    return flags_metadata


def get_code_context(file_path: Path, line_num: int, context_lines: int = 1) -> Tuple[str, Optional[str]]:
    """
    Get code context for a flag usage: function/class name and code line.
    
    Args:
        file_path: Path to the file
        line_num: Line number (1-based)
        context_lines: Number of lines around to show (default: 1)
    
    Returns:
        Tuple of (code_line, function_or_class_name)
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        if line_num < 1 or line_num > len(lines):
            return "", None
        
        # Get the actual line (0-based index)
        actual_line = lines[line_num - 1].rstrip()
        
        # Find function/class name by looking backwards
        function_or_class = None
        for i in range(line_num - 2, -1, -1):  # Start from line before, go backwards
            line = lines[i].strip()
            # Match: def function_name(...) or class ClassName(...)
            def_match = re.match(r"^def\s+([a-zA-Z_][a-zA-Z0-9_]*)", line)
            class_match = re.match(r"^class\s+([a-zA-Z_][a-zA-Z0-9_]*)", line)
            
            if def_match:
                function_or_class = f"def {def_match.group(1)}"
                break
            elif class_match:
                function_or_class = f"class {class_match.group(1)}"
                break
        
        return actual_line, function_or_class
        
    except Exception:
        return "", None


def get_yaml_path(flag_name: str) -> Optional[str]:
    """
    Get the full YAML path for a config flag.
    
    Args:
        flag_name: Flag name (e.g., "use_module_coordinator")
    
    Returns:
        Full YAML path (e.g., "features.use_module_coordinator") or None
    """
    config_path = ROOT / "config" / "unified_config.yaml"
    if not config_path.exists():
        return None
    
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
        
        features = config.get("features", {})
        kill_switches = config.get("kill_switches", {})
        
        # Check features
        if flag_name in features:
            return f"features.{flag_name}"
        
        # Check kill_switches
        if flag_name in kill_switches:
            return f"kill_switches.{flag_name}"
        
    except Exception:
        pass
    
    return None


def find_env_flags_in_code(module_path: Optional[Path] = None) -> Dict[str, List[Tuple[str, int]]]:
    """
    Find all NEXY_KS_*, NEXY_DISABLE_* flags in code.
    
    Returns:
        Dict mapping flag_name -> list of (file_path, line_number) tuples.
    """
    flags_found = {}
    
    # Pattern to match:
    # - NEXY_KS_*, NEXY_DISABLE_* (kill-switches)
    # - USE_* (env overrides for features, e.g., USE_MODULE_COORDINATOR, USE_WORKFLOW_INTEGRATIONS)
    # - FORWARD_ASSISTANT_ACTIONS (special env override)
    # Must be a complete flag name (not partial like NEXY_KS_DISABLE_)
    # Require at least one uppercase letter after the prefix, exclude trailing underscores
    # Examples: NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS (valid), USE_MODULE_COORDINATOR (valid), NEXY_KS_DISABLE_ (invalid)
    # Exclude patterns like NEXY_KS_DISABLE_<FEATURE> (template in docs)
    # Exclude non-feature-flag USE_* variables (e.g., USE_GITHUB for update scripts)
    pattern = re.compile(r"\b((?:NEXY_(?:KS_|DISABLE_)|USE_)[A-Z][A-Z0-9_]+|FORWARD_ASSISTANT_ACTIONS)\b")
    
    # Determine search scope
    if module_path:
        if module_path.is_file():
            search_paths = [module_path]
        else:
            search_paths = list(module_path.rglob("*.py")) + list(module_path.rglob("*.yaml")) + list(module_path.rglob("*.sh")) + list(module_path.rglob("*.md"))
    else:
        search_paths = list(ROOT.rglob("*.py")) + list(ROOT.rglob("*.yaml")) + list(ROOT.rglob("*.sh")) + list(ROOT.rglob("*.md"))
    
    # Search in files
    for file_path in search_paths:
        if _should_skip_file(file_path):
            continue
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line_num, line in enumerate(lines, 1):
                    for match in pattern.finditer(line):
                        flag_name = match.group(1)
                        if flag_name not in flags_found:
                            flags_found[flag_name] = []
                        rel_path = file_path.relative_to(ROOT) if file_path.is_relative_to(ROOT) else file_path
                        flags_found[flag_name].append((str(rel_path), line_num))
        except Exception:
            pass
    
    return flags_found


def find_config_flags_in_code(module_path: Optional[Path] = None) -> Dict[str, List[Tuple[str, int]]]:
    """
    Find all config flags (features.*, kill_switches.*) in code.
    
    Looks for:
    - features.<flag> in YAML files (via yaml.safe_load)
    - kill_switches.<flag> in YAML files
    - config.features.<flag> in Python
    - config.kill_switches.<flag> in Python
    
    Returns:
        Dict mapping flag_name -> list of (file_path, line_number) tuples.
    """
    flags_found = {}
    
    # First, get all config flags from unified_config.yaml
    config_flags_from_yaml = load_config_flags_from_yaml()
    
    # Also search for ANY features.*/kill_switches.* usage in code
    # Pattern: get("features", {}).get("flag_name") or config.features.flag_name
    # Note: default argument is optional and can be any value (string, dict, etc.)
    # IMPORTANT: When modifying this regex, test with: .get("features", {}).get("temp_flag", {})
    # to ensure flags with default arguments are correctly detected and their locations collected.
    pattern_features_get = re.compile(r'\.get\(["\']features["\']\s*,\s*{{}}\s*\)\s*\.\s*get\(["\']([a-z0-9_\.]+)["\'](?:\s*,\s*[^)]+)?\)')
    pattern_kill_switches_get = re.compile(r'\.get\(["\']kill_switches["\']\s*,\s*{{}}\s*\)\s*\.\s*get\(["\']([a-z0-9_\.]+)["\'](?:\s*,\s*[^)]+)?\)')
    pattern_features_dot = re.compile(r'features\.([a-z0-9_\.]+)')
    pattern_kill_switches_dot = re.compile(r'kill_switches\.([a-z0-9_\.]+)')
    pattern_features_bracket = re.compile(r'features\[["\']([a-z0-9_\.]+)["\']\]')
    pattern_kill_switches_bracket = re.compile(r'kill_switches\[["\']([a-z0-9_\.]+)["\']\]')
    
    # Collect all flags found in code
    flags_in_code = set()
    
    # Search in Python files for features.*/kill_switches.* usage
    for py_file in ROOT.rglob("*.py"):
        if _should_skip_file(py_file):
            continue
        
        try:
            with open(py_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line_num, line in enumerate(lines, 1):
                    # Find all features.* flags in code
                    for match in pattern_features_get.finditer(line):
                        flags_in_code.add(match.group(1))
                    for match in pattern_kill_switches_get.finditer(line):
                        flags_in_code.add(match.group(1))
                    for match in pattern_features_dot.finditer(line):
                        flags_in_code.add(match.group(1))
                    for match in pattern_kill_switches_dot.finditer(line):
                        flags_in_code.add(match.group(1))
                    for match in pattern_features_bracket.finditer(line):
                        flags_in_code.add(match.group(1))
                    for match in pattern_kill_switches_bracket.finditer(line):
                        flags_in_code.add(match.group(1))
        except Exception as e:
            # Silently skip files that can't be read
            pass
    
    # Combine flags from YAML and code
    all_config_flags = config_flags_from_yaml | flags_in_code
    
    if not all_config_flags:
        return flags_found
    
    # Pattern to match config flag usage in Python
    # Matches: get("features", {}).get("flag_name") or config.features.flag_name
    for flag_name in all_config_flags:
        # Escape special regex characters
        escaped_flag = re.escape(flag_name)
        
        # Pattern 1: get("features", {}).get("flag_name") or get("features", {}).get("flag_name", default)
        # Allow optional whitespace, different quote styles, and optional default argument
        # IMPORTANT: The optional default argument pattern (?:\s*,\s*[^)]+)? is critical for:
        # - Catching flags with default values: .get("flag", {})
        # - Providing accurate file/line coordinates for all flag usages
        # - Regression testing: any flag usage must show exact location
        pattern1_features = re.compile(rf'\.get\(["\']features["\']\s*,\s*{{}}\s*\)\s*\.\s*get\(["\']{escaped_flag}["\'](?:\s*,\s*[^)]+)?\)')
        pattern1_kill_switches = re.compile(rf'\.get\(["\']kill_switches["\']\s*,\s*{{}}\s*\)\s*\.\s*get\(["\']{escaped_flag}["\'](?:\s*,\s*[^)]+)?\)')
        # Pattern 2: config.features.flag_name or config["features"]["flag_name"]
        pattern2_features = re.compile(rf'(?:config|features)\.{escaped_flag}|(?:config|features)\["{escaped_flag}"\]|(?:config|features)\[\'{escaped_flag}\'\]')
        pattern2_kill_switches = re.compile(rf'(?:config|kill_switches)\.{escaped_flag}|(?:config|kill_switches)\["{escaped_flag}"\]|(?:config|kill_switches)\[\'{escaped_flag}\'\]')
        # Pattern 3: features[flag_name] or kill_switches[flag_name]
        pattern3_features = re.compile(rf'features\[["\']{escaped_flag}["\']\]')
        pattern3_kill_switches = re.compile(rf'kill_switches\[["\']{escaped_flag}["\']\]')
        # Pattern 4: Simple string match (for comments, docs, etc.)
        pattern4 = re.compile(rf'\b{escaped_flag}\b')
        
        # Search in Python files
        for py_file in ROOT.rglob("*.py"):
            if _should_skip_file(py_file):
                continue
            
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    for line_num, line in enumerate(lines, 1):
                        # Check all patterns - any match means flag is used
                        if (pattern1_features.search(line) or pattern1_kill_switches.search(line) or 
                            pattern2_features.search(line) or pattern2_kill_switches.search(line) or
                            pattern3_features.search(line) or pattern3_kill_switches.search(line)):
                            if flag_name not in flags_found:
                                flags_found[flag_name] = []
                            rel_path = py_file.relative_to(ROOT)
                            flags_found[flag_name].append((str(rel_path), line_num))
                        # Also check simple string match if in features/kill_switches context (for comments, docs, etc.)
                        elif pattern4.search(line) and ('features' in line.lower() or 'kill_switches' in line.lower() or 'config' in line.lower()):
                            if flag_name not in flags_found:
                                flags_found[flag_name] = []
                            rel_path = py_file.relative_to(ROOT)
                            flags_found[flag_name].append((str(rel_path), line_num))
            except Exception:
                pass
        
        # Search in YAML files
        for yaml_file in ROOT.rglob("*.yaml"):
            if _should_skip_file(yaml_file):
                continue
            
            try:
                with open(yaml_file, "r", encoding="utf-8") as f:
                    yaml_content = yaml.safe_load(f) or {}
                    
                    features = yaml_content.get("features", {})
                    kill_switches = yaml_content.get("kill_switches", {})
                    
                    # Check all flags from all_config_flags
                    for check_flag in all_config_flags:
                        if check_flag == flag_name:
                            if flag_name in features or flag_name in kill_switches:
                                if flag_name not in flags_found:
                                    flags_found[flag_name] = []
                                rel_path = yaml_file.relative_to(ROOT)
                                flags_found[flag_name].append((str(rel_path), 0))  # Line number not available from yaml.load
            except Exception:
                pass
    
    return flags_found


def _should_skip_file(filepath: Path) -> bool:
    """Check if file should be skipped from scanning."""
    # Skip excluded directories
    if any(excluded in str(filepath) for excluded in EXCLUDED_DIRS):
        return True
    
    # Skip excluded paths
    if any(excluded in str(filepath) for excluded in EXCLUDED_PATHS):
        return True
    
    return False


def discover_flags_in_module(module_path: Path) -> Dict[str, List[FlagLocation]]:
    """
    Discover all flags in a specific module/path.
    
    Args:
        module_path: Path to file or directory to scan
    
    Returns:
        Dict mapping flag_name -> list of FlagLocation objects
    """
    all_flags = {}
    
    # Exclude false positives
    EXCLUDED_FLAGS = {"__dict__", "__init__", "__getattr__", "__setattr__"}
    
    # Find env flags
    env_flags = find_env_flags_in_code(module_path)
    for flag_name, locations in env_flags.items():
        if flag_name in EXCLUDED_FLAGS:
            continue
        all_flags[flag_name] = []
        for file_path, line_num in locations:
            full_path = ROOT / file_path if Path(file_path).is_relative_to(ROOT) else Path(file_path)
            code_line, func_or_class = get_code_context(full_path, line_num)
            all_flags[flag_name].append(FlagLocation(
                file_path=str(file_path),
                line_num=line_num,
                code_line=code_line,
                func_or_class=func_or_class
            ))
    
    # Find config flags
    config_flags = find_config_flags_in_code(module_path)
    for flag_name, locations in config_flags.items():
        if flag_name in EXCLUDED_FLAGS:
            continue
        if flag_name not in all_flags:
            all_flags[flag_name] = []
        for file_path, line_num in locations:
            full_path = ROOT / file_path if Path(file_path).is_relative_to(ROOT) else Path(file_path)
            code_line, func_or_class = get_code_context(full_path, line_num)
            all_flags[flag_name].append(FlagLocation(
                file_path=str(file_path),
                line_num=line_num,
                code_line=code_line,
                func_or_class=func_or_class
            ))
    
    return all_flags


def generate_discovery_report(module_path: Path, flags: Dict[str, List[FlagLocation]], flags_metadata: Dict[str, FlagMetadata]) -> None:
    """
    Generate and print flags discovery report.
    
    Args:
        module_path: Path that was scanned
        flags: Dict mapping flag_name -> list of FlagLocation objects
        flags_metadata: Dict mapping flag_name -> FlagMetadata from registry
    """
    print(f"{BLUE}{'='*70}{RESET}")
    print(f"{BLUE}Flags Discovery Report{RESET}")
    print(f"{BLUE}{'='*70}{RESET}\n")
    
    print(f"{YELLOW}Module/Path:{RESET} {module_path}")
    print(f"{YELLOW}Total flags found:{RESET} {len(flags)}\n")
    
    if not flags:
        print(f"{YELLOW}No flags found in the specified path.{RESET}")
        return
    
    # Group flags by registration status
    registered = []
    unregistered = []
    
    for flag_name in sorted(flags.keys()):
        if flag_name in flags_metadata:
            registered.append((flag_name, flags[flag_name], flags_metadata[flag_name]))
        else:
            unregistered.append((flag_name, flags[flag_name]))
    
    # Print registered flags
    if registered:
        print(f"{GREEN}{'─'*70}{RESET}")
        print(f"{GREEN}✅ Registered Flags ({len(registered)}){RESET}")
        print(f"{GREEN}{'─'*70}{RESET}\n")
        
        for flag_name, locations, metadata in registered:
            print(f"{GREEN}• {flag_name}{RESET}")
            print(f"  Type: {metadata.type}")
            print(f"  Owner: {metadata.owner}")
            print(f"  Default: {metadata.default}")
            print(f"  Scope: {metadata.scope}")
            if metadata.kill_switch != "-":
                print(f"  Kill-switch: {metadata.kill_switch}")
            print(f"  Description: {metadata.description}")
            
            # YAML path for config flags
            yaml_path = get_yaml_path(flag_name)
            if yaml_path:
                print(f"  YAML path: {yaml_path}")
            
            print(f"  Locations ({len(locations)}):")
            for loc in locations[:10]:  # Show first 10 locations
                location_str = f"    {loc.file_path}:{loc.line_num}"
                if loc.func_or_class:
                    location_str += f" ({loc.func_or_class})"
                print(f"  {YELLOW}→{RESET} {location_str}")
                if loc.code_line:
                    code_preview = loc.code_line[:80] + "..." if len(loc.code_line) > 80 else loc.code_line
                    print(f"      {code_preview}")
            if len(locations) > 10:
                print(f"    ... and {len(locations) - 10} more locations")
            print()
    
    # Print unregistered flags
    if unregistered:
        print(f"{RED}{'─'*70}{RESET}")
        print(f"{RED}❌ UNREGISTERED Flags ({len(unregistered)}){RESET}")
        print(f"{RED}{'─'*70}{RESET}\n")
        
        for flag_name, locations in unregistered:
            print(f"{RED}• {flag_name} {YELLOW}[UNREGISTERED]{RESET}")
            print(f"  Locations ({len(locations)}):")
            for loc in locations[:10]:  # Show first 10 locations
                location_str = f"    {loc.file_path}:{loc.line_num}"
                if loc.func_or_class:
                    location_str += f" ({loc.func_or_class})"
                print(f"  {YELLOW}→{RESET} {location_str}")
                if loc.code_line:
                    code_preview = loc.code_line[:80] + "..." if len(loc.code_line) > 80 else loc.code_line
                    print(f"      {code_preview}")
            if len(locations) > 10:
                print(f"    ... and {len(locations) - 10} more locations")
            print()
            print(f"  {YELLOW}💡 Action required: Add to Docs/FEATURE_FLAGS.md{RESET}")
            print(f"  {YELLOW}   Format: | `{flag_name}` | type | owner | default | scope | kill_switch | description |{RESET}\n")
    
    print(f"{BLUE}{'='*70}{RESET}")


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Verify feature flags registration or discover flags in a module",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--module",
        type=str,
        help="Path to file or directory to scan (discovery mode). If not specified, runs full verification."
    )
    
    args = parser.parse_args()
    
    # Discovery mode
    if args.module:
        module_path = Path(args.module)
        if not module_path.is_absolute():
            module_path = ROOT / module_path
        
        if not module_path.exists():
            print(f"{RED}ERROR: Path not found: {module_path}{RESET}", file=sys.stderr)
            return 1
        
        # Load registry metadata
        flags_metadata = load_feature_flags_registry_with_metadata()
        
        # Discover flags
        flags = discover_flags_in_module(module_path)
        
        # Generate report
        generate_discovery_report(module_path, flags, flags_metadata)
        
        # Return 1 if there are unregistered flags
        registered_flags = set(flags_metadata.keys())
        unregistered = [f for f in flags.keys() if f not in registered_flags]
        return 1 if unregistered else 0
    
    # Verification mode (default)
    print(f"{YELLOW}🔍 Checking feature flags registration...{RESET}\n")
    
    # Load registry
    registered_flags = load_feature_flags_registry()
    if not registered_flags:
        print(f"{RED}❌ ERROR: No flags found in FEATURE_FLAGS.md{RESET}", file=sys.stderr)
        return 1
    
    print(f"{GREEN}✅ Loaded {len(registered_flags)} flags from FEATURE_FLAGS.md{RESET}")
    
    # Find env flags in code
    env_flags_in_code = find_env_flags_in_code()
    print(f"{GREEN}✅ Found {len(env_flags_in_code)} unique env flags (NEXY_*, USE_*, FORWARD_ASSISTANT_ACTIONS) in code{RESET}")
    
    # Find config flags: check all flags from unified_config.yaml (not just those used in code)
    # This ensures all config flags are registered, even if not yet used
    config_flags_from_yaml = load_config_flags_from_yaml()
    
    # Also find config flags used in code (for reporting and catching flags not in YAML)
    config_flags_in_code = find_config_flags_in_code()
    
    # Use flags from YAML as source of truth (all must be registered)
    # But also include flags found in code that might not be in YAML yet
    # This ensures flags used only in code (without YAML) are also checked
    all_config_flags = config_flags_from_yaml | set(config_flags_in_code.keys())
    
    print(f"{GREEN}✅ Found {len(config_flags_from_yaml)} config flags in unified_config.yaml{RESET}")
    if config_flags_in_code:
        print(f"{GREEN}✅ Found {len(config_flags_in_code)} config flags used in code{RESET}\n")
    else:
        print()
    
    # Convert config flags to same format as env flags for checking
    config_flags_dict = {flag: [] for flag in all_config_flags}
    # Add actual code locations if found
    for flag, locations in config_flags_in_code.items():
        config_flags_dict[flag] = locations
    
    # Merge all flags found
    all_flags_in_code = {**env_flags_in_code, **config_flags_dict}
    
    # Check for unregistered flags
    errors = []
    # Exclude false positives
    EXCLUDED_FLAGS = {"__dict__", "__init__", "__getattr__", "__setattr__"}
    # Exclude non-feature-flag USE_* variables (used in update/deployment/config scripts, not feature flags)
    EXCLUDED_USE_VARS = {
        "USE_GITHUB",  # Used in update scripts, not a feature flag override
        "USE_TLS",  # Used in gRPC config, not a feature flag override
    }
    
    for flag_name, locations in sorted(all_flags_in_code.items()):
        # Skip excluded flags (false positives)
        if flag_name in EXCLUDED_FLAGS:
            continue
        # Skip excluded USE_* variables (not feature flag overrides)
        if flag_name in EXCLUDED_USE_VARS:
            continue
        # Skip incomplete flag names (like NEXY_KS_DISABLE_ without completion)
        # These appear in documentation as examples/templates (e.g., NEXY_KS_DISABLE_<FEATURE>)
        # Valid flags must have content after the prefix (not just NEXY_KS_DISABLE_)
        # Check: if ends with underscore and has less than 4 parts (NEXY, KS/DISABLE, empty), skip
        if flag_name.endswith("_") and len([p for p in flag_name.split("_") if p]) < 4:
            continue
        if flag_name not in registered_flags:
            errors.append((flag_name, locations))
    
    # Report results
    if errors:
        print(f"{RED}{'='*60}{RESET}")
        print(f"{RED}❌ FAILED: Found {len(errors)} unregistered flags{RESET}\n")
        
        for flag_name, locations in errors:
            print(f"{RED}  • {flag_name}{RESET}")
            # Show first 5 locations
            for file_path, line_num in locations[:5]:
                if line_num > 0:
                    print(f"    {YELLOW}→ {file_path}:{line_num}{RESET}")
                else:
                    print(f"    {YELLOW}→ {file_path}{RESET}")
            if len(locations) > 5:
                print(f"    {YELLOW}  ... and {len(locations) - 5} more locations{RESET}")
            print()
        
        print(f"{RED}💡 Solution: Add these flags to Docs/FEATURE_FLAGS.md{RESET}")
        print(f"{RED}   Format: | `{errors[0][0]}` | type | owner | default | scope | kill_switch | description |{RESET}")
        return 1
    
    # All flags registered
    num_config_flags = len(all_config_flags) if 'all_config_flags' in locals() else len(config_flags_dict)
    print(f"{GREEN}{'='*60}{RESET}")
    print(f"{GREEN}✅ PASSED: All {len(all_flags_in_code)} flags are registered in FEATURE_FLAGS.md{RESET}")
    print(f"{GREEN}   ({len(env_flags_in_code)} env flags, {num_config_flags} config flags){RESET}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
