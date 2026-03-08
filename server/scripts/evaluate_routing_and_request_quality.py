#!/usr/bin/env python3
"""Evaluate category recognition quality, request-handling quality, and processing time.

Input format:
  rn | hardware_id_hash | created_at | prompt | answer_created_at | answer
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from statistics import median
import re
import argparse


CATEGORIES = {
    "none",
    "whatsapp",
    "messages",
    "browser",
    "google_search",
    "describe",
    "system_control",
    "payment",
    "capability",
    "unknown",
}


def pct(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    s = sorted(values)
    k = (len(s) - 1) * q
    f = int(k)
    c = min(f + 1, len(s) - 1)
    if f == c:
        return s[f]
    return s[f] + (s[c] - s[f]) * (k - f)


def parse_rows(path: Path):
    rows = []
    lines = path.read_text(encoding="utf-8").splitlines()
    for line in lines[1:]:
        parts = line.split(" | ", 5)
        if len(parts) < 6:
            continue
        rn, hardware_id_hash, created_at, prompt, answer_created_at, answer = parts
        prompt = prompt.strip()
        answer = answer.strip()

        latency_ms = None
        try:
            if created_at.strip() and answer_created_at.strip():
                t0 = datetime.fromisoformat(created_at.strip())
                t1 = datetime.fromisoformat(answer_created_at.strip())
                latency_ms = (t1 - t0).total_seconds() * 1000.0
        except Exception:
            latency_ms = None

        rows.append(
            {
                "rn": int(rn.strip()) if rn.strip().isdigit() else rn.strip(),
                "prompt": prompt,
                "answer": answer,
                "latency_ms": latency_ms,
            }
        )
    return rows


def expected_category_from_prompt(prompt: str) -> str:
    p = prompt.lower().strip()

    if not p:
        return "none"

    if "whatsapp" in p:
        if any(x in p for x in ["send", "message", "read", "last messages", "check"]):
            return "whatsapp"

    if any(x in p for x in ["imessage", "messages app", "messages"]) and "whatsapp" not in p:
        if any(x in p for x in ["send", "read", "message", "last"]):
            return "messages"

    if any(x in p for x in ["what can you do", "capab", "what web browsing capab", "tell me your services"]):
        return "capability"

    if any(x in p for x in ["what is on my screen", "describe", "where am i", "video clips"]):
        return "describe"

    if any(x in p for x in ["latest news", "search", "find best", "look up", "find deal"]):
        # If clearly navigation command to site/app, prefer browser.
        if any(x in p for x in ["go to youtube", "open youtube", "go to "]):
            return "browser"
        return "google_search"

    if any(x in p for x in ["go to youtube", "open youtube", "close youtube", "go to "]):
        return "browser"

    if any(x in p for x in ["open ", "close ", "application"]) or re.search(r"\bapp\b", p):
        # keep browser for explicit youtube path
        if "youtube" in p:
            return "browser"
        return "system_control"

    if any(x in p for x in ["payment", "subscription", "billing", "plan"]):
        return "payment"

    return "none"


def actual_category_from_answer(answer: str) -> str:
    a = answer.lower().strip()
    if not a:
        return "unknown"

    if any(x in a for x in ["what can i do", "i can help you", "i can help with various tasks"]):
        return "capability"

    if "whatsapp" in a:
        return "whatsapp"

    if any(x in a for x in ["messages", "imessage"]) and "whatsapp" not in a:
        if any(x in a for x in ["send", "reading", "message"]):
            return "messages"

    if any(x in a for x in ["opening youtube", "going to youtube", "closing youtube", "open youtube"]):
        return "browser"

    if any(x in a for x in ["find news", "latest news headlines", "search for deals", "search for cabin deals"]):
        return "google_search"

    if any(x in a for x in ["open applications", "opening safari", "opening club deck", "opening "]):
        if "youtube" not in a:
            return "system_control"

    if any(x in a for x in ["you are in final cut pro", "applications window", "project timeline", "describe"]):
        return "describe"

    return "none"


def request_quality(row: dict) -> tuple[bool, str]:
    p = row["prompt"].lower()
    a = row["answer"].lower()

    if not a:
        return False, "empty_answer"

    if "provider is unavailable" in a:
        return False, "provider_unavailable"

    # WhatsApp explicit send with content should not be dropped.
    if "whatsapp" in p and any(x in p for x in ["send", "message"]):
        if any(x in p for x in ["how are", "what's up", "how are you doing"]):
            if any(x in a for x in ["what would you like to send", "what message would you like"]):
                return False, "message_content_lost"

    # Follow-up: tell me more should stay in previous intent context; description dump likely miss.
    if "tell me more" in p and any(x in a for x in ["final cut pro", "project timeline", "ramblio.app"]):
        return False, "follow_up_context_miss"

    return True, "ok"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="server/monitor_inbox/all_requests_with_answers_prod_2026-03-02.txt",
    )
    args = parser.parse_args()

    rows = parse_rows(Path(args.input))

    # Latency stats
    lat = [r["latency_ms"] for r in rows if r["latency_ms"] is not None]

    # Category quality
    eval_rows = []
    for r in rows:
        exp = expected_category_from_prompt(r["prompt"])
        act = actual_category_from_answer(r["answer"])
        eval_rows.append((r, exp, act))

    cat_scored = [(r, e, a) for (r, e, a) in eval_rows if e != "none" and a != "unknown"]
    cat_ok = [(r, e, a) for (r, e, a) in cat_scored if e == a]

    # Request quality
    rq = [request_quality(r) for r in rows]
    rq_ok = sum(1 for ok, _ in rq if ok)
    rq_fail = [(rows[i], reason) for i, (ok, reason) in enumerate(rq) if not ok]

    print(f"rows={len(rows)}")
    if lat:
        print(
            "processing_time_ms="
            f"min:{min(lat):.3f} p50:{median(lat):.3f} p95:{pct(lat,0.95):.3f} max:{max(lat):.3f}"
        )

    print(f"category_scored={len(cat_scored)}")
    cat_acc = (len(cat_ok) / len(cat_scored) * 100.0) if cat_scored else 0.0
    print(f"category_accuracy_percent={cat_acc:.2f}")

    print(f"request_quality_ok={rq_ok}")
    print(f"request_quality_fail={len(rq_fail)}")

    # Top category mismatches
    mismatches = [(r, e, a) for (r, e, a) in cat_scored if e != a]
    print(f"category_mismatches={len(mismatches)}")
    for r, e, a in mismatches[:15]:
        print(f"MISMATCH rn={r['rn']} expected={e} actual={a}")
        print(f"  prompt={r['prompt']}")
        print(f"  answer={r['answer'][:180]}")

    for r, reason in rq_fail[:15]:
        print(f"REQUEST_FAIL rn={r['rn']} reason={reason}")
        print(f"  prompt={r['prompt']}")
        print(f"  answer={r['answer'][:180]}")


if __name__ == "__main__":
    main()
