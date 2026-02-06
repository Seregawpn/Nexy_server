#!/usr/bin/env python3
"""Verify feature flags registry matches env and config usage."""

from __future__ import annotations

from pathlib import Path
import re

import yaml

ROOT = Path(__file__).resolve().parents[1]

ENV_PATTERN = re.compile(r"\\bNEXY_[A-Z0-9_]+\\b")


def load_registry_flags(path: Path) -> set[str]:
    names = set()
    for line in path.read_text(errors="ignore").splitlines():
        if line.startswith("|") and "|" in line[1:]:
            parts = [p.strip() for p in line.strip().split("|")[1:-1]]
            if not parts:
                continue
            name = parts[0].strip()
            if name.startswith("`") and name.endswith("`"):
                name = name[1:-1]
            if name:
                names.add(name)
    return names


def collect_env_flags() -> set[str]:
    flags = set()
    for path in [ROOT / "integration", ROOT / "modules", ROOT / "config", ROOT / "main.py"]:
        if path.is_file():
            flags.update(ENV_PATTERN.findall(path.read_text(errors="ignore")))
        elif path.is_dir():
            for f in path.rglob("*.py"):
                flags.update(ENV_PATTERN.findall(f.read_text(errors="ignore")))
    return flags


def collect_config_flags() -> tuple[set[str], set[str]]:
    config_path = ROOT / "config" / "unified_config.yaml"
    if not config_path.exists():
        return set(), set()
    config = yaml.safe_load(config_path.read_text())
    features: set[str] = set()
    ks: set[str] = set()

    def walk(obj, path=None):
        if path is None:
            path = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                new_path = path + [str(k)]
                if len(path) >= 1 and path[0] == "features":
                    if len(new_path) >= 2:
                        features.add(".".join(new_path[:2]))
                if str(k).startswith("ks_"):
                    ks.add(str(k))
                walk(v, new_path)
        elif isinstance(obj, list):
            for item in obj:
                walk(item, path)

    walk(config)
    return features, ks


def main() -> int:
    registry_path = ROOT / "Docs" / "FEATURE_FLAGS.md"
    if not registry_path.exists():
        print("Missing Docs/FEATURE_FLAGS.md")
        return 1

    registry = load_registry_flags(registry_path)
    env_flags = collect_env_flags()
    features, ks = collect_config_flags()

    missing_env = sorted(env_flags - registry)
    missing_features = sorted(features - registry)
    missing_ks = sorted(ks - registry)

    if missing_env or missing_features or missing_ks:
        print("Feature flags registry missing entries:")
        for f in missing_env:
            print(f"- ENV: {f}")
        for f in missing_features:
            print(f"- FEATURE: {f}")
        for f in missing_ks:
            print(f"- KS: {f}")
        return 1

    print("Feature flags registry OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
