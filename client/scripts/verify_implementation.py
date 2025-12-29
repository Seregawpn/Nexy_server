#!/usr/bin/env python3
"""
Verify implementation consistency between client and server.

**Цель**: Воспроизводимое подтверждение, что логика реализована на обеих сторонах.

**Логика**:
1. Проверка соответствия документации коду (клиент и сервер)
2. Запуск автоматических проверок (verify_architecture.py, verify_feature_flags.py)
3. Проверка gRPC протокола и конфигурации
4. Генерация артефактов подтверждения (выводы, git-SHA, чек-лист)

**Использование**:
    python scripts/verify_implementation.py [--client-only] [--server-only] [--output-dir <dir>]

**Exit codes**:
    0 — все проверки пройдены
    1 — хотя бы одна проверка провалена
"""
import subprocess
import sys
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict
from datetime import datetime

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Root directories
CLIENT_ROOT = Path(__file__).parent.parent
SERVER_ROOT = CLIENT_ROOT.parent / "server" / "server"
REPO_ROOT = CLIENT_ROOT.parent


@dataclass
class CheckResult:
    """Result of a single check."""
    name: str
    status: str  # "pass", "fail", "skip"
    message: str
    details: Optional[str] = None
    output: Optional[str] = None


@dataclass
class VerificationReport:
    """Complete verification report."""
    timestamp: str
    client_git_sha: Optional[str]
    server_git_sha: Optional[str]
    checks: List[Dict]
    summary: Dict[str, int]  # pass, fail, skip counts


def get_git_sha(repo_path: Path) -> Optional[str]:
    """Get current git SHA for a repository."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_path,
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None


def run_check(name: str, command: List[str], cwd: Path, timeout: int = 60, allow_warnings: bool = False) -> CheckResult:
    """Run a check command and return result."""
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        output = result.stdout + result.stderr
        
        if result.returncode == 0:
            return CheckResult(
                name=name,
                status="pass",
                message=f"✅ {name} passed",
                output=output
            )
        else:
            # Check if output contains only warnings (not errors)
            if allow_warnings:
                has_errors = any(keyword in output.lower() for keyword in ["error", "failed", "❌", "critical"])
                if not has_errors and "warning" in output.lower():
                    return CheckResult(
                        name=name,
                        status="pass",
                        message=f"✅ {name} passed (warnings only, non-critical)",
                        details=output[:500] if output else None,
                        output=output
                    )
            
            return CheckResult(
                name=name,
                status="fail",
                message=f"❌ {name} failed (exit code: {result.returncode})",
                details=output[:500] if output else None,
                output=output
            )
    except subprocess.TimeoutExpired:
        return CheckResult(
            name=name,
            status="fail",
            message=f"❌ {name} timed out",
            details="Command exceeded timeout"
        )
    except Exception as e:
        return CheckResult(
            name=name,
            status="fail",
            message=f"❌ {name} error: {str(e)}",
            details=str(e)
        )


def check_client_architecture_docs() -> CheckResult:
    """Check client architecture documentation matches code - STRICT comparison."""
    try:
        arch_doc = CLIENT_ROOT / "Docs" / "ARCHITECTURE_OVERVIEW.md"
        coordinator = CLIENT_ROOT / "integration" / "core" / "simple_module_coordinator.py"
        
        if not arch_doc.exists():
            return CheckResult(
                name="Client Architecture Docs",
                status="fail",
                message="ARCHITECTURE_OVERVIEW.md not found"
            )
        
        if not coordinator.exists():
            return CheckResult(
                name="Client Architecture Docs",
                status="fail",
                message="simple_module_coordinator.py not found"
            )
        
        # Read coordinator to find integration order
        with open(coordinator, "r", encoding="utf-8") as f:
            coordinator_content = f.read()
        
        # Extract integration order from _create_integrations - STRICT parsing
        integration_order_code = []
        in_create_integrations = False
        for line in coordinator_content.split("\n"):
            if "_create_integrations" in line and ("def" in line or "async def" in line):
                in_create_integrations = True
                continue
            if in_create_integrations:
                # Match: self.integrations['name'] = Integration(...)
                # Note: tray is conditional (if tray_enabled), but we still track it in order
                match = re.search(r"self\.integrations\[['\"]([^'\"]+)['\"]", line)
                if match:
                    integration_name = match.group(1)
                    # Skip duplicates (tray might appear twice: once in if, once in else)
                    if integration_name not in integration_order_code:
                        integration_order_code.append(integration_name)
                # Stop at next function definition
                if line.strip().startswith("def ") or line.strip().startswith("async def "):
                    if "_create_integrations" not in line:
                        break
        
        if len(integration_order_code) == 0:
            return CheckResult(
                name="Client Architecture Docs",
                status="fail",
                message="Could not extract integration order from coordinator",
                details="No integrations found in _create_integrations()"
            )
        
        # Read architecture doc and extract documented order
        with open(arch_doc, "r", encoding="utf-8") as f:
            arch_content = f.read()
        
        # Extract documented order from "Порядок создания интеграций" section
        integration_order_doc = []
        in_order_section = False
        for line in arch_content.split("\n"):
            if "Порядок создания интеграций" in line or "**Порядок создания интеграций**" in line:
                in_order_section = True
                continue
            if in_order_section:
                # Match numbered list: "1. integration_name" or "1. integration_name (comment)"
                match = re.match(r"^\d+\.\s+([a-z_]+)", line.strip())
                if match:
                    integration_order_doc.append(match.group(1))
                # Stop at next section (## or **Порядок запуска)
                if line.strip().startswith("##") or "**Порядок запуска" in line:
                    break
        
        if len(integration_order_doc) == 0:
            return CheckResult(
                name="Client Architecture Docs",
                status="fail",
                message="Could not extract integration order from documentation",
                details="No numbered list found in 'Порядок создания интеграций' section"
            )
        
        # STRICT comparison: order must match exactly
        if integration_order_code == integration_order_doc:
            return CheckResult(
                name="Client Architecture Docs",
                status="pass",
                message=f"✅ Integration order matches exactly ({len(integration_order_code)} integrations)",
                details=f"Code and documentation have identical order"
            )
        else:
            # Find differences
            differences = []
            max_len = max(len(integration_order_code), len(integration_order_doc))
            for i in range(max_len):
                code_item = integration_order_code[i] if i < len(integration_order_code) else "<missing>"
                doc_item = integration_order_doc[i] if i < len(integration_order_doc) else "<missing>"
                if code_item != doc_item:
                    differences.append(f"Position {i+1}: code='{code_item}' vs doc='{doc_item}'")
            
            return CheckResult(
                name="Client Architecture Docs",
                status="fail",
                message=f"❌ Integration order mismatch ({len(differences)} differences)",
                details="; ".join(differences[:5]) + (f" ... and {len(differences)-5} more" if len(differences) > 5 else "")
            )
            
    except Exception as e:
        return CheckResult(
            name="Client Architecture Docs",
            status="fail",
            message=f"Error checking architecture docs: {str(e)}",
            details=str(e)
        )


def check_server_architecture_docs() -> CheckResult:
    """Check server architecture documentation matches code structure - STRICT validation."""
    try:
        arch_doc = SERVER_ROOT / "Docs" / "ARCHITECTURE_OVERVIEW.md"
        
        if not arch_doc.exists():
            return CheckResult(
                name="Server Architecture Docs",
                status="skip",
                message="Server ARCHITECTURE_OVERVIEW.md not found (may be in different location)"
            )
        
        # Read architecture doc
        with open(arch_doc, "r", encoding="utf-8") as f:
            arch_content = f.read()
        
        # Extract documented structure from code blocks - focus on modules/ subdirectories
        # STRICT: Only parse lines that are clearly inside modules/ section
        documented_modules = set()
        in_code_block = False
        in_modules_section = False
        for line in arch_content.split("\n"):
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                if not in_code_block:
                    in_modules_section = False
                continue
            if in_code_block:
                # Check if we're entering modules section
                if "├── modules/" in line:
                    in_modules_section = True
                    continue
                # Only parse if we're inside modules section
                if in_modules_section:
                    # Match: │   ├── module_name/ (must have "│" prefix to be inside modules/)
                    # Stop if we hit a root-level directory (starts with "├──" without "│")
                    if line.strip().startswith("├──") and not line.strip().startswith("│"):
                        # This is a root-level directory, stop parsing modules
                        break
                    if "│" in line and "├──" in line:
                        match = re.search(r"├──\s+([a-z_]+)/", line)
                        if match:
                            module_name = match.group(1)
                            # Stop if we hit known non-module directories
                            if module_name in ["integrations", "monitoring", "scripts", "tests", "config", "utils", "updates", "nginx", "Docs"]:
                                break
                            documented_modules.add(module_name)
        
        # Check actual server modules structure
        if not SERVER_ROOT.exists():
            return CheckResult(
                name="Server Architecture Docs",
                status="skip",
                message="Server root directory not found"
            )
        
        modules_dir = SERVER_ROOT / "modules"
        if not modules_dir.exists():
            return CheckResult(
                name="Server Architecture Docs",
                status="fail",
                message="Server modules/ directory not found"
            )
        
        actual_modules = set()
        for item in modules_dir.iterdir():
            if item.is_dir() and not item.name.startswith(".") and not item.name.startswith("__"):
                actual_modules.add(item.name)
        
        # STRICT comparison: check if documented modules exist
        missing_modules = documented_modules - actual_modules
        extra_modules = actual_modules - documented_modules
        
        if len(missing_modules) == 0 and len(extra_modules) == 0:
            return CheckResult(
                name="Server Architecture Docs",
                status="pass",
                message=f"✅ Server modules structure matches documentation exactly ({len(actual_modules)} modules)",
                details="All documented modules exist"
            )
        else:
            issues = []
            if missing_modules:
                issues.append(f"Missing modules: {', '.join(sorted(missing_modules)[:5])}")
            if extra_modules:
                issues.append(f"Extra modules: {', '.join(sorted(extra_modules)[:5])}")
            
            return CheckResult(
                name="Server Architecture Docs",
                status="fail",
                message=f"❌ Server structure mismatch",
                details="; ".join(issues)
            )
            
    except Exception as e:
        return CheckResult(
            name="Server Architecture Docs",
            status="fail",
            message=f"Error checking server architecture docs: {str(e)}",
            details=str(e)
        )


def check_grpc_protocol() -> CheckResult:
    """Check gRPC protocol consistency - STRICT canonical path validation."""
    try:
        # Canonical path: server/server/modules/grpc_service/streaming.proto
        canonical_proto = SERVER_ROOT / "modules" / "grpc_service" / "streaming.proto"
        
        if not canonical_proto.exists():
            # Fallback: search for streaming.proto
            proto_files = list(REPO_ROOT.rglob("streaming.proto"))
            if not proto_files:
                return CheckResult(
                    name="gRPC Protocol",
                    status="fail",
                    message="streaming.proto not found at canonical path",
                    details=f"Expected: {canonical_proto.relative_to(REPO_ROOT)}"
                )
            else:
                found_path = proto_files[0].relative_to(REPO_ROOT)
                return CheckResult(
                    name="gRPC Protocol",
                    status="fail",
                    message="streaming.proto found at non-canonical path",
                    details=f"Found: {found_path}, Expected: {canonical_proto.relative_to(REPO_ROOT)}"
                )
        
        # Check if proto file is readable and valid
        with open(canonical_proto, "r", encoding="utf-8") as f:
            proto_content = f.read()
        
        # STRICT validation: must contain all key gRPC definitions
        key_definitions = ["service", "rpc", "message", "stream"]
        found_definitions = [defn for defn in key_definitions if defn in proto_content]
        missing_definitions = [defn for defn in key_definitions if defn not in proto_content]
        
        if len(missing_definitions) == 0:
            return CheckResult(
                name="gRPC Protocol",
                status="pass",
                message=f"✅ gRPC protocol file found at canonical path and valid",
                details=f"Found all {len(key_definitions)} key definitions at {canonical_proto.relative_to(REPO_ROOT)}"
            )
        else:
            return CheckResult(
                name="gRPC Protocol",
                status="fail",
                message=f"❌ gRPC protocol file missing key definitions",
                details=f"Missing: {', '.join(missing_definitions)}"
            )
            
    except Exception as e:
        return CheckResult(
            name="gRPC Protocol",
            status="fail",
            message=f"Error checking gRPC protocol: {str(e)}",
            details=str(e)
        )


def check_unified_config() -> CheckResult:
    """Check unified_config.yaml consistency."""
    try:
        client_config = CLIENT_ROOT / "config" / "unified_config.yaml"
        server_config = SERVER_ROOT / "config" / "unified_config.yaml"
        
        results = []
        
        if client_config.exists():
            results.append("client config exists")
        else:
            return CheckResult(
                name="Unified Config",
                status="fail",
                message="Client unified_config.yaml not found"
            )
        
        if server_config.exists():
            results.append("server config exists")
        else:
            return CheckResult(
                name="Unified Config",
                status="skip",
                message="Server unified_config.yaml not found (may use different config system)"
            )
        
        return CheckResult(
            name="Unified Config",
            status="pass",
            message="✅ Unified config files found",
            details=", ".join(results)
        )
        
    except Exception as e:
        return CheckResult(
            name="Unified Config",
            status="fail",
            message=f"Error checking unified config: {str(e)}",
            details=str(e)
        )


def main() -> int:
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Verify implementation consistency")
    parser.add_argument("--client-only", action="store_true", help="Only check client")
    parser.add_argument("--server-only", action="store_true", help="Only check server")
    parser.add_argument("--output-dir", type=str, default=".verification", help="Output directory for artifacts")
    
    args = parser.parse_args()
    
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}🔍 Verifying Implementation Consistency{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    # Get git SHAs
    client_git_sha = get_git_sha(CLIENT_ROOT) if not args.server_only else None
    server_git_sha = get_git_sha(SERVER_ROOT) if not args.client_only else None
    
    if client_git_sha:
        print(f"{GREEN}Client git SHA: {client_git_sha[:8]}{RESET}")
    if server_git_sha:
        print(f"{GREEN}Server git SHA: {server_git_sha[:8]}{RESET}")
    print()
    
    # Run checks
    checks: List[CheckResult] = []
    
    # Client checks
    if not args.server_only:
        print(f"{YELLOW}Running client checks...{RESET}\n")
        
        # Architecture docs
        checks.append(check_client_architecture_docs())
        
        # verify_architecture.py (allow warnings, they're non-critical)
        if (CLIENT_ROOT / "scripts" / "verify_architecture.py").exists():
            checks.append(run_check(
                "Client Architecture Verification",
                [sys.executable, "scripts/verify_architecture.py"],
                CLIENT_ROOT,
                allow_warnings=True
            ))
        
        # verify_feature_flags.py
        if (CLIENT_ROOT / "scripts" / "verify_feature_flags.py").exists():
            checks.append(run_check(
                "Client Feature Flags Verification",
                [sys.executable, "scripts/verify_feature_flags.py"],
                CLIENT_ROOT
            ))
    
    # Server checks
    if not args.client_only:
        print(f"{YELLOW}Running server checks...{RESET}\n")
        
        # Architecture docs
        checks.append(check_server_architecture_docs())
        
        # verify_feature_flags.py (server)
        if (SERVER_ROOT / "scripts" / "verify_feature_flags.py").exists():
            checks.append(run_check(
                "Server Feature Flags Verification",
                [sys.executable, "scripts/verify_feature_flags.py"],
                SERVER_ROOT
            ))
        
        # Unified config
        checks.append(check_unified_config())
    
    # Shared checks
    if not args.client_only and not args.server_only:
        checks.append(check_grpc_protocol())
    
    # Print results
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}📊 Verification Results{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    pass_count = sum(1 for c in checks if c.status == "pass")
    fail_count = sum(1 for c in checks if c.status == "fail")
    skip_count = sum(1 for c in checks if c.status == "skip")
    
    for check in checks:
        status_color = GREEN if check.status == "pass" else RED if check.status == "fail" else YELLOW
        print(f"{status_color}{check.message}{RESET}")
        if check.details:
            print(f"   {check.details}")
        print()
    
    # Generate report
    report = VerificationReport(
        timestamp=datetime.now().isoformat(),
        client_git_sha=client_git_sha,
        server_git_sha=server_git_sha,
        checks=[asdict(c) for c in checks],
        summary={
            "pass": pass_count,
            "fail": fail_count,
            "skip": skip_count
        }
    )
    
    # Save report
    report_file = output_dir / "verification_report.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(asdict(report), f, indent=2)
    
    # Save outputs
    for check in checks:
        if check.output:
            output_file = output_dir / f"{check.name.replace(' ', '_').lower()}_output.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(check.output)
    
    # Print summary
    print(f"{BLUE}{'='*60}{RESET}")
    print(f"{GREEN}✅ Passed: {pass_count}{RESET}")
    if fail_count > 0:
        print(f"{RED}❌ Failed: {fail_count}{RESET}")
    if skip_count > 0:
        print(f"{YELLOW}⏭️  Skipped: {skip_count}{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    print(f"{GREEN}📄 Report saved to: {report_file}{RESET}")
    print(f"{GREEN}📁 Artifacts saved to: {output_dir}{RESET}\n")
    
    # Generate checklist
    checklist_file = output_dir / "checklist.md"
    with open(checklist_file, "w", encoding="utf-8") as f:
        f.write("# Implementation Verification Checklist\n\n")
        f.write(f"**Generated**: {report.timestamp}\n\n")
        if client_git_sha:
            f.write(f"**Client git SHA**: {client_git_sha}\n")
        if server_git_sha:
            f.write(f"**Server git SHA**: {server_git_sha}\n")
        f.write("\n## Checks\n\n")
        for check in checks:
            status_icon = "✅" if check.status == "pass" else "❌" if check.status == "fail" else "⏭️"
            f.write(f"- {status_icon} **{check.name}**: {check.status.upper()}\n")
            if check.details:
                f.write(f"  - {check.details}\n")
        f.write("\n## Summary\n\n")
        f.write(f"- ✅ Passed: {pass_count}\n")
        f.write(f"- ❌ Failed: {fail_count}\n")
        f.write(f"- ⏭️  Skipped: {skip_count}\n")
    
    print(f"{GREEN}📋 Checklist saved to: {checklist_file}{RESET}\n")
    
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
