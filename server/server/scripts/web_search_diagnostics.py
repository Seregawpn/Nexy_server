#!/usr/bin/env python3
import os
import socket
import sys
import ssl
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from config.unified_config import get_config

TIMEOUT = float(os.getenv("DIAG_TIMEOUT", "5"))


def check_dns(host: str) -> str:
    try:
        socket.gethostbyname(host)
        return "ok"
    except Exception as exc:
        return f"error: {type(exc).__name__}: {exc}"


def check_https(url: str) -> str:
    try:
        req = Request(url, headers={"User-Agent": "nexy-websearch-diag"})
        with urlopen(req, timeout=TIMEOUT, context=ssl.create_default_context()) as resp:
            return f"ok: {resp.status}"
    except HTTPError as exc:
        return f"http_error: {exc.code}"
    except URLError as exc:
        return f"url_error: {exc}"
    except Exception as exc:
        return f"error: {type(exc).__name__}: {exc}"


def main() -> None:
    cfg = get_config()

    print("== Web Search Diagnostics ==")
    print("WEB_SEARCH_ENABLED:", cfg.features.web_search_enabled)
    print("TEXT_PROCESSING_TOOLS:", cfg.text_processing.tools)
    print("LANGCHAIN_MODEL:", cfg.text_processing.langchain_model)
    print("LANGCHAIN_API_KEY_SET:", bool(cfg.text_processing.gemini_api_key))

    print("\n== DNS ==")
    for host in ["googleapis.com", "generativelanguage.googleapis.com", "www.google.com"]:
        print(host, "->", check_dns(host))

    print("\n== HTTPS ==")
    for url in [
        "https://www.google.com",
        "https://generativelanguage.googleapis.com",
    ]:
        print(url, "->", check_https(url))

    print("\nIf HTTPS fails, Web Search will not work in this environment.")


if __name__ == "__main__":
    main()
