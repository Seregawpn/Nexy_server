#!/usr/bin/env python3
"""Client-only architecture guard checks with debt baseline support.

Checks:
- sys.path.insert outside entrypoint (main.py)
- critical event publisher ownership
- runtime legacy-path markers without LEGACY_EXPIRY note
- config feature flags without runtime usage (dead flags)

The script compares findings against scripts/architecture_guard_baseline.json and
fails only on *new* findings, allowing gradual debt reduction.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re
from typing import Iterable

import yaml

ROOT = Path(__file__).resolve().parents[1]
BASELINE_PATH = ROOT / "scripts" / "architecture_guard_baseline.json"

CRITICAL_EVENT_OWNERS: dict[str, set[str]] = {
    "app.mode_changed": {"integration/core/state_manager.py"},
    "processing.terminal": {"integration/workflows/processing_workflow.py"},
}

LEGACY_MARKERS = (
    "fallback_to=legacy",
    "text_chunk_legacy",
)
LEGACY_EXPIRY_TOKEN = "LEGACY_EXPIRY:"

SYS_PATH_INSERT_RE = re.compile(r"\bsys\.path\.insert\s*\(")
PUBLISH_RE_TMPL = r"\bpublish\s*\(\s*[\"\']{event}[\"\']"
IS_FEATURE_ENABLED_RE = re.compile(r"\bis_feature_enabled\(\s*[\"\']([a-zA-Z0-9_]+)[\"\']")
GET_FEATURE_CONFIG_RE = re.compile(r"\bget_feature_config\(\s*[\"\']([a-zA-Z0-9_]+)[\"\']")
FEATURES_GET_RE = re.compile(
    r"\bfeatures\s*\.\s*get\(\s*[\"\']([a-zA-Z0-9_]+)[\"\']"
)


@dataclass(frozen=True)
class Finding:
    category: str
    key: str


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def iter_py_files(paths: Iterable[Path]) -> Iterable[Path]:
    for p in paths:
        if p.is_file() and p.suffix == ".py":
            yield p
        elif p.is_dir():
            yield from p.rglob("*.py")


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def check_sys_path_insert() -> list[Finding]:
    findings: list[Finding] = []
    for f in iter_py_files([ROOT / "integration", ROOT / "modules", ROOT / "config", ROOT / "scripts", ROOT / "main.py"]):
        rf = rel(f)
        if rf == "main.py":
            continue
        for idx, line in enumerate(load_text(f).splitlines(), start=1):
            if SYS_PATH_INSERT_RE.search(line):
                findings.append(Finding("sys_path_insert_outside_entrypoint", f"{rf}:{idx}"))
    return findings


def check_event_owner() -> list[Finding]:
    findings: list[Finding] = []
    files = list(iter_py_files([ROOT / "integration", ROOT / "modules", ROOT / "config", ROOT / "main.py"]))
    for event, owners in CRITICAL_EVENT_OWNERS.items():
        pat = re.compile(PUBLISH_RE_TMPL.format(event=re.escape(event)))
        for f in files:
            rf = rel(f)
            txt = load_text(f)
            if not pat.search(txt):
                continue
            if rf not in owners:
                findings.append(Finding("critical_event_owner_violation", f"{event}|{rf}"))
    return findings


def check_legacy_expiry() -> list[Finding]:
    findings: list[Finding] = []
    for f in iter_py_files([ROOT / "integration"]):
        rf = rel(f)
        txt = load_text(f)
        if not any(marker in txt for marker in LEGACY_MARKERS):
            continue
        if LEGACY_EXPIRY_TOKEN in txt:
            continue
        for idx, line in enumerate(txt.splitlines(), start=1):
            if any(marker in line for marker in LEGACY_MARKERS):
                findings.append(Finding("legacy_runtime_without_expiry", f"{rf}:{idx}"))
    return findings


def collect_runtime_feature_usage() -> set[str]:
    used: set[str] = set()
    for f in iter_py_files([ROOT / "integration", ROOT / "modules", ROOT / "config", ROOT / "main.py"]):
        txt = load_text(f)
        used.update(IS_FEATURE_ENABLED_RE.findall(txt))
        used.update(GET_FEATURE_CONFIG_RE.findall(txt))
        used.update(FEATURES_GET_RE.findall(txt))
    return used


def load_config_features() -> set[str]:
    cfg_path = ROOT / "config" / "unified_config.yaml"
    if not cfg_path.exists():
        return set()
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
    features = cfg.get("features", {})
    if not isinstance(features, dict):
        return set()
    return {str(k) for k in features.keys()}


def check_dead_flags() -> list[Finding]:
    configured = load_config_features()
    used = collect_runtime_feature_usage()
    unused = sorted(configured - used)
    return [Finding("dead_feature_flag", name) for name in unused]


def build_findings() -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    all_findings: list[Finding] = []
    all_findings.extend(check_sys_path_insert())
    all_findings.extend(check_event_owner())
    all_findings.extend(check_legacy_expiry())
    all_findings.extend(check_dead_flags())

    for f in all_findings:
        out.setdefault(f.category, []).append(f.key)
    for k in list(out.keys()):
        out[k] = sorted(set(out[k]))
    return dict(sorted(out.items()))


def load_baseline() -> dict[str, list[str]]:
    if not BASELINE_PATH.exists():
        return {}
    raw = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    result: dict[str, list[str]] = {}
    if isinstance(raw, dict):
        for k, v in raw.items():
            if isinstance(v, list):
                result[str(k)] = sorted({str(x) for x in v})
    return result


def diff_new(findings: dict[str, list[str]], baseline: dict[str, list[str]]) -> dict[str, list[str]]:
    new: dict[str, list[str]] = {}
    for cat, items in findings.items():
        base_items = set(baseline.get(cat, []))
        add = sorted([x for x in items if x not in base_items])
        if add:
            new[cat] = add
    return new


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--update-baseline", action="store_true")
    args = parser.parse_args()

    findings = build_findings()
    if args.update_baseline:
        BASELINE_PATH.write_text(json.dumps(findings, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
        print(f"Updated baseline: {rel(BASELINE_PATH)}")
        return 0

    baseline = load_baseline()
    if not baseline:
        print("ERROR: baseline not found. Run with --update-baseline first.")
        return 1

    new = diff_new(findings, baseline)
    if new:
        print("Architecture guard failed: new violations detected")
        for cat, items in sorted(new.items()):
            print(f"- {cat}:")
            for item in items:
                print(f"  - {item}")
        return 1

    print("Architecture guards OK (no new violations beyond baseline).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
