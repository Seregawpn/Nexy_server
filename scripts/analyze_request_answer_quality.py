#!/usr/bin/env python3
"""Analyze request/answer export and print quality + text-latency metrics."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from statistics import median
import argparse


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
    lines = path.read_text(encoding="utf-8").splitlines()
    rows = []
    for line in lines[1:]:
        parts = line.split(" | ", 5)
        if len(parts) < 6:
            continue
        rn, hardware_id_hash, created_at, prompt, answer_created_at, answer = parts
        prompt = prompt.strip()
        answer = answer.strip()
        created_at = created_at.strip()
        answer_created_at = answer_created_at.strip()

        text_latency_ms = None
        if created_at and answer_created_at:
            try:
                start = datetime.fromisoformat(created_at)
                end = datetime.fromisoformat(answer_created_at)
                text_latency_ms = (end - start).total_seconds() * 1000.0
            except Exception:
                text_latency_ms = None

        rows.append(
            {
                "rn": int(rn.strip()) if rn.strip().isdigit() else rn.strip(),
                "hardware_id_hash": hardware_id_hash.strip(),
                "prompt": prompt,
                "answer": answer,
                "text_latency_ms": text_latency_ms,
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="server/monitor_inbox/all_requests_with_answers_prod_2026-03-02.txt",
        help="Path to requests+answers export",
    )
    args = parser.parse_args()

    path = Path(args.input)
    rows = parse_rows(path)
    latencies = [r["text_latency_ms"] for r in rows if r["text_latency_ms"] is not None]

    empty_answers = [r for r in rows if not r["answer"]]
    provider_unavailable = [
        r
        for r in rows
        if "provider is unavailable" in r["answer"].lower()
    ]
    whatsapp_prompts = [r for r in rows if "whatsapp" in r["prompt"].lower()]
    whatsapp_empty = [r for r in whatsapp_prompts if not r["answer"]]

    quality_flags = []
    for r in rows:
        prompt = r["prompt"].lower()
        answer = r["answer"].lower()

        if "tell me more" in prompt and any(
            token in answer
            for token in ["final cut pro", "project timeline", "ramblio.app"]
        ):
            quality_flags.append((r["rn"], "follow_up_memory_miss", r["prompt"], r["answer"]))

        if "latest news" in prompt and "here are the latest news headlines" in answer:
            quality_flags.append((r["rn"], "generic_unverified_news", r["prompt"], r["answer"]))

        if "whatsapp" in prompt and not r["answer"]:
            quality_flags.append((r["rn"], "empty_whatsapp_answer", r["prompt"], r["answer"]))

    print(f"input={path}")
    print(f"rows={len(rows)}")
    if latencies:
        print(
            "text_latency_ms="
            f"min:{min(latencies):.3f} p50:{median(latencies):.3f} "
            f"p95:{pct(latencies,0.95):.3f} max:{max(latencies):.3f}"
        )

    print(f"empty_answers={len(empty_answers)}")
    print(f"provider_unavailable={len(provider_unavailable)}")
    print(f"whatsapp_prompts={len(whatsapp_prompts)}")
    print(f"whatsapp_empty_answers={len(whatsapp_empty)}")
    print(f"quality_flags={len(quality_flags)}")

    for rn, flag, prompt, answer in quality_flags[:20]:
        print(f"FLAG rn={rn} type={flag}")
        print(f"  prompt={prompt}")
        print(f"  answer={answer[:180]}")


if __name__ == "__main__":
    main()
