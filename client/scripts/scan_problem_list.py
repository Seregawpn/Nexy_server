#!/usr/bin/env python3
"""
Project-wide problem scanner.

Runs static checks and writes a single consolidated issue list:
- Ruff (always, if available)
- basedpyright (if available)
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from typing import Any

EXCLUDED_PATH_FRAGMENTS = ("/Docs/_archive/",)


def _is_excluded_issue_file(file_path: str | None) -> bool:
    if not file_path:
        return False
    normalized = file_path.replace("\\", "/")
    return any(fragment in normalized for fragment in EXCLUDED_PATH_FRAGMENTS)


def _run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    current_pythonpath = env.get("PYTHONPATH", "")
    base_paths = [str(cwd), str(cwd.parent)]
    if current_pythonpath:
        env["PYTHONPATH"] = os.pathsep.join([*base_paths, current_pythonpath])
    else:
        env["PYTHONPATH"] = os.pathsep.join(base_paths)
    return subprocess.run(
        cmd,
        cwd=cwd,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )


def _detect_basedpyright(root: Path) -> str | None:
    from_env = os.environ.get("BASEDPYRIGHT_BIN")
    if from_env:
        env_path = Path(from_env)
        if env_path.exists() and env_path.is_file():
            return str(env_path)
    candidates = [
        root / ".venv" / "bin" / "basedpyright",
        root / ".venv_x86" / "bin" / "basedpyright",
        root.parent / "server" / ".venv" / "bin" / "basedpyright",
    ]
    for path in candidates:
        if path.exists() and path.is_file():
            return str(path)
    from_path = shutil.which("basedpyright")
    return from_path


def _detect_pytest(root: Path) -> str | None:
    pytest_bin = root / ".venv" / "bin" / "pytest"
    if pytest_bin.exists() and pytest_bin.is_file():
        return str(pytest_bin)
    return shutil.which("pytest")


def _scan_ruff(root: Path) -> dict[str, Any]:
    ruff_bin = root / ".venv" / "bin" / "ruff"
    if not ruff_bin.exists():
        ruff_path = shutil.which("ruff")
        if not ruff_path:
            return {"status": "skipped", "reason": "ruff_not_found", "issues": []}
        ruff_cmd = [ruff_path]
    else:
        ruff_cmd = [str(ruff_bin)]

    proc = _run([*ruff_cmd, "check", ".", "--output-format", "json"], root)
    issues: list[dict[str, Any]] = []
    try:
        payload = json.loads(proc.stdout or "[]")
    except json.JSONDecodeError:
        payload = []
    for item in payload:
        file_path = item.get("filename")
        if _is_excluded_issue_file(file_path):
            continue
        loc = item.get("location", {}) or {}
        issues.append(
            {
                "tool": "ruff",
                "severity": "error",
                "file": file_path,
                "line": loc.get("row"),
                "column": loc.get("column"),
                "code": item.get("code"),
                "message": item.get("message"),
            }
        )
    status = "ok" if not issues else "failed"
    return {"status": status, "issues": issues, "returncode": proc.returncode}


def _scan_basedpyright(root: Path) -> dict[str, Any]:
    bin_path = _detect_basedpyright(root)
    if not bin_path:
        return {"status": "skipped", "reason": "basedpyright_not_found", "issues": []}

    proc = _run([bin_path, "--outputjson"], root)
    issues: list[dict[str, Any]] = []
    try:
        payload = json.loads(proc.stdout or "{}")
    except json.JSONDecodeError:
        payload = {}

    for item in payload.get("generalDiagnostics", []) or []:
        file_path = item.get("file")
        if _is_excluded_issue_file(file_path):
            continue
        rng = item.get("range", {}) or {}
        start = rng.get("start", {}) or {}
        line = start.get("line")
        char = start.get("character")
        issues.append(
            {
                "tool": "basedpyright",
                "severity": item.get("severity", "error"),
                "file": file_path,
                "line": (line + 1) if isinstance(line, int) else None,
                "column": (char + 1) if isinstance(char, int) else None,
                "code": item.get("rule"),
                "message": item.get("message"),
            }
        )

    status = "ok" if not issues else "failed"
    return {"status": status, "issues": issues, "returncode": proc.returncode}


def _scan_script(root: Path, name: str, cmd: list[str]) -> dict[str, Any]:
    proc = _run(cmd, root)
    if proc.returncode == 0:
        return {"status": "ok", "issues": [], "returncode": 0}
    tail = "\n".join((proc.stdout + "\n" + proc.stderr).strip().splitlines()[-20:])
    return {
        "status": "failed",
        "returncode": proc.returncode,
        "issues": [
            {
                "tool": name,
                "severity": "error",
                "file": None,
                "line": None,
                "column": None,
                "code": f"{name}_failed",
                "message": tail if tail else f"{name} returned non-zero",
            }
        ],
    }


def _scan_pytest(root: Path) -> dict[str, Any]:
    pytest_bin = _detect_pytest(root)
    if not pytest_bin:
        return {"status": "skipped", "reason": "pytest_not_found", "issues": []}

    proc = _run(
        [
            pytest_bin,
            "-q",
            "--maxfail=100",
            "--disable-warnings",
            "--tb=short",
            "tests",
        ],
        root,
    )
    if proc.returncode == 0:
        return {"status": "ok", "issues": [], "returncode": 0}

    issues: list[dict[str, Any]] = []
    failed_pattern_with_reason = re.compile(r"^FAILED\s+([^\s:]+)(::[^\s]+)?\s+-\s+(.*)$")
    failed_pattern_plain = re.compile(r"^FAILED\s+([^\s:]+)(::[^\s]+)?$")
    for line in proc.stdout.splitlines():
        stripped = line.strip()
        match = failed_pattern_with_reason.match(stripped)
        message = "test failed"
        if not match:
            match = failed_pattern_plain.match(stripped)
            if not match:
                continue
        else:
            message = match.group(3)
        file_path = match.group(1)
        test_name = (match.group(2) or "").removeprefix("::")
        issues.append(
            {
                "tool": "pytest",
                "severity": "error",
                "file": file_path,
                "line": None,
                "column": None,
                "code": test_name or "test_failed",
                "message": message,
            }
        )

    if not issues:
        tail = "\n".join((proc.stdout + "\n" + proc.stderr).strip().splitlines()[-20:])
        issues.append(
            {
                "tool": "pytest",
                "severity": "error",
                "file": None,
                "line": None,
                "column": None,
                "code": "pytest_failed",
                "message": tail if tail else "pytest returned non-zero",
            }
        )
    return {"status": "failed", "issues": issues, "returncode": proc.returncode}


def _to_markdown(result: dict[str, Any]) -> str:
    lines = [
        "# Problem Scan Report",
        "",
        f"- total_issues: {result['summary']['total_issues']}",
        f"- blocking_issues: {result['summary']['blocking_issues']}",
        f"- ruff_status: {result['summary']['ruff_status']}",
        f"- basedpyright_status: {result['summary']['basedpyright_status']}",
        f"- verify_imports_status: {result['summary']['verify_imports_status']}",
        f"- verify_state_access_status: {result['summary']['verify_state_access_status']}",
        f"- dependency_rules_status: {result['summary']['dependency_rules_status']}",
        f"- pytest_status: {result['summary']['pytest_status']}",
        "",
        "| tool | severity | file | line | code | message |",
        "|---|---|---|---:|---|---|",
    ]
    for issue in result["issues"]:
        file_path = issue.get("file") or "-"
        line = issue.get("line") or "-"
        code = issue.get("code") or "-"
        message = (issue.get("message") or "").replace("\n", " ").strip()
        lines.append(
            f"| {issue.get('tool', '-')} | {issue.get('severity', '-')} | {file_path} | "
            f"{line} | {code} | {message} |"
        )
    if not result["issues"]:
        lines.append("| - | - | - | - | - | no issues found |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-json",
        default="build_logs/problem_scan_latest.json",
        help="Path for JSON output",
    )
    parser.add_argument(
        "--output-md",
        default="build_logs/problem_scan_latest.md",
        help="Path for Markdown output",
    )
    parser.add_argument(
        "--with-tests",
        action="store_true",
        help="Include pytest scan over tests/",
    )
    parser.add_argument(
        "--update-baseline",
        help="Save current issues to this file as a baseline",
    )
    parser.add_argument(
        "--baseline",
        help="Load baseline from this file and suppress matching issues",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    out_json = root / args.output_json
    out_md = root / args.output_md
    out_json.parent.mkdir(parents=True, exist_ok=True)

    check_baseline: set[tuple[str, str, str, str]] = set()
    if args.baseline:
        bp = root / args.baseline
        if bp.exists():
            try:
                base_data = json.loads(bp.read_text(encoding="utf-8"))
                for b_item in base_data:
                    # stored as [tool, code, file, message]
                    if len(b_item) >= 4:
                        check_baseline.add(tuple(b_item[:4]))
            except Exception as e:
                print(f"[WARN] Failed to load baseline: {e}")

    ruff = _scan_ruff(root)
    basedpyright = _scan_basedpyright(root)
    verify_imports = _scan_script(
        root,
        "verify_imports",
        [str(root / ".venv" / "bin" / "python"), "scripts/verify_imports.py"],
    )
    verify_state_access = _scan_script(
        root,
        "verify_no_direct_state_access",
        [str(root / ".venv" / "bin" / "python"), "scripts/verify_no_direct_state_access.py"],
    )
    dependency_rules = _scan_script(
        root,
        "check_dependency_violations",
        [str(root / ".venv" / "bin" / "python"), "scripts/check_dependency_violations.py"],
    )
    pytest_scan = (
        _scan_pytest(root)
        if args.with_tests
        else {
            "status": "skipped",
            "reason": "tests_not_requested",
            "issues": [],
        }
    )

    raw_issues = [
        *ruff["issues"],
        *basedpyright["issues"],
        *verify_imports["issues"],
        *verify_state_access["issues"],
        *dependency_rules["issues"],
        *pytest_scan["issues"],
    ]

    # Process issues against baseline
    final_issues = []
    baseline_issues_to_save = []

    for issue in raw_issues:
        tool = str(issue.get("tool") or "-")
        code = str(issue.get("code") or "-")
        file_path = str(issue.get("file") or "-")
        message = str(issue.get("message") or "")

        # Signature for baseline (excluding line numbers)
        sig = (tool, code, file_path, message)

        if args.update_baseline:
            baseline_issues_to_save.append(list(sig))

        if sig in check_baseline:
            # Downgrade to warning
            issue["severity"] = "warning"
            issue["baseline"] = True

        final_issues.append(issue)

    if args.update_baseline:
        bp_save = root / args.update_baseline
        bp_save.parent.mkdir(parents=True, exist_ok=True)
        # Deduplicate before saving
        unique_baseline = []
        seen = set()
        for item in baseline_issues_to_save:
            t = tuple(item)
            if t not in seen:
                seen.add(t)
                unique_baseline.append(item)
        bp_save.write_text(json.dumps(unique_baseline, indent=2), encoding="utf-8")
        print(f"[INFO] Saved {len(unique_baseline)} baseline issues to {bp_save}")

    blocking_issues = [issue for issue in final_issues if issue.get("severity") != "warning"]

    # Recompute status for each tool based on final (filtered) blocking issues
    tool_status = {}
    for tool_name in [
        "ruff",
        "basedpyright",
        "verify_imports",
        "verify_no_direct_state_access",
        "check_dependency_violations",
        "pytest",
    ]:
        tool_issues = [i for i in final_issues if i.get("tool") == tool_name]
        tool_blocking = [i for i in tool_issues if i.get("severity") != "warning"]
        # Mapping for variable names is tricky, let's just use the dicts we already have
        if tool_name == "ruff":
            source = ruff
        elif tool_name == "basedpyright":
            source = basedpyright
        elif tool_name == "verify_imports":
            source = verify_imports
        elif tool_name == "verify_no_direct_state_access":
            source = verify_state_access
        elif tool_name == "check_dependency_violations":
            source = dependency_rules
        elif tool_name == "pytest":
            source = pytest_scan
        else:
            source = {"status": "unknown"}

        if source.get("status") == "failed" and not tool_blocking:
            tool_status[tool_name] = "ok"
        else:
            tool_status[tool_name] = source.get("status", "unknown")

    result = {
        "summary": {
            "total_issues": len(final_issues),
            "blocking_issues": len(blocking_issues),
            "ruff_status": tool_status["ruff"],
            "basedpyright_status": tool_status["basedpyright"],
            "verify_imports_status": tool_status["verify_imports"],
            "verify_state_access_status": tool_status["verify_no_direct_state_access"],
            "dependency_rules_status": tool_status["check_dependency_violations"],
            "pytest_status": tool_status["pytest"],
        },
        "tools": {
            "ruff": {k: v for k, v in ruff.items() if k != "issues"},
            "basedpyright": {k: v for k, v in basedpyright.items() if k != "issues"},
            "verify_imports": {k: v for k, v in verify_imports.items() if k != "issues"},
            "verify_no_direct_state_access": {
                k: v for k, v in verify_state_access.items() if k != "issues"
            },
            "check_dependency_violations": {
                k: v for k, v in dependency_rules.items() if k != "issues"
            },
            "pytest": {k: v for k, v in pytest_scan.items() if k != "issues"},
        },
        "issues": final_issues,
    }

    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md.write_text(_to_markdown(result), encoding="utf-8")

    print(f"JSON: {out_json}")
    print(f"MD: {out_md}")
    print(f"TOTAL_ISSUES={len(final_issues)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
