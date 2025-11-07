#!/usr/bin/env python3
"""Validate Cache-Control headers in the bundled Nginx config.

The fail-fast CI pipeline uses this script to ensure that every public
endpoint exposed through the reference ingress configuration keeps the
cache directives mandated by the server principles. The script reads the
`server/nginx/grpc-passthrough.conf` file and asserts that each location
block has the expected TTL value.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict

EXPECTED_CACHE_HEADERS: Dict[str, str] = {
    "/health": "public, max-age=30",
    "/status": "public, max-age=30",
    "/updates/": "public, max-age=300",
    "/updates/appcast.xml": "public, max-age=60",
    "/updates/health": "public, max-age=30",
}

LOCATION_PATTERN = re.compile(r"^location\s+(?P<path>[^\s]+)")
HEADER_PATTERN = re.compile(r'add_header\s+Cache-Control\s+"(?P<value>[^"]+)"')


def _parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Cache-Control headers in the Nginx config")
    parser.add_argument(
        "config_path",
        nargs="?",
        default=Path("server/nginx/grpc-passthrough.conf"),
        type=Path,
        help="Path to the Nginx configuration file",
    )
    return parser.parse_args()


def _normalize_path(path_token: str) -> str:
    """Return the canonical location key used in EXPECTED_CACHE_HEADERS."""

    cleaned = path_token.rstrip("{").strip()
    return cleaned


def validate_cache_headers(config_path: Path) -> int:
    """Validate cache headers inside the provided Nginx configuration."""

    if not config_path.exists():
        print(f"❌ Config file not found: {config_path}")
        return 1

    contents = config_path.read_text(encoding="utf-8")
    current_location: str | None = None
    discovered_headers: Dict[str, str] = {}

    for raw_line in contents.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        location_match = LOCATION_PATTERN.match(line)
        if location_match:
            current_location = _normalize_path(location_match.group("path"))
            continue

        if current_location is None:
            continue

        header_match = HEADER_PATTERN.search(line)
        if header_match:
            discovered_headers[current_location] = header_match.group("value")
            continue

        if line == "}":
            current_location = None

    missing_locations = sorted(set(EXPECTED_CACHE_HEADERS.keys()) - set(discovered_headers.keys()))
    mismatched_locations = [
        (location, discovered_headers.get(location, ""), EXPECTED_CACHE_HEADERS[location])
        for location in EXPECTED_CACHE_HEADERS
        if discovered_headers.get(location) != EXPECTED_CACHE_HEADERS[location]
    ]

    exit_code = 0

    if missing_locations:
        exit_code = 1
        print("❌ Missing Cache-Control directives for the following locations:")
        for location in missing_locations:
            print(f"  - {location}")

    if mismatched_locations:
        exit_code = 1
        print("❌ Unexpected Cache-Control values detected:")
        for location, actual, expected in mismatched_locations:
            display_actual = actual or "∅"
            print(f"  - {location}: expected '{expected}', found '{display_actual}'")

    if exit_code == 0:
        print("✅ All Cache-Control headers match the canonical configuration")

    return exit_code


def main() -> None:
    args = _parse_arguments()
    exit_code = validate_cache_headers(args.config_path)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
