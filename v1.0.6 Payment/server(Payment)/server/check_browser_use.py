#!/usr/bin/env python3
"""Проверка установки browser-use"""
import sys
try:
    from browser_use import Agent
    print("✅ browser-use установлен")
    BROWSER_USE_AVAILABLE = True
except ImportError as e:
    print(f"❌ browser-use не установлен: {e}")
    BROWSER_USE_AVAILABLE = False
    sys.exit(1)

try:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        browser.close()
    print("✅ Playwright Chromium работает")
except Exception as e:
    print(f"⚠️ Playwright Chromium не установлен: {e}")
    print("Установите: python3 -m playwright install chromium")

if BROWSER_USE_AVAILABLE:
    print("\n🎉 browser-use готов к использованию!")
