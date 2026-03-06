#!/usr/bin/env python3
"""
Lightweight benchmark: request -> first audio chunk / end_message.
Runs workflow with mocked text module and real AudioProcessor.
"""

import asyncio
import time
from dataclasses import dataclass
from pathlib import Path
import sys
from statistics import median
from typing import AsyncIterator, Dict, List

sys.path.insert(0, str(Path(__file__).parent.parent))

from modules.audio_generation.core.audio_processor import AudioProcessor
from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration


@dataclass
class Scenario:
    prompt: str
    llm_delay_ms: int
    llm_text: str


class MockTextModule:
    def __init__(self, llm_delay_ms: int, llm_text: str):
        self.is_initialized = True
        self.name = "text_processing"
        self._llm_delay_ms = llm_delay_ms
        self._llm_text = llm_text

    async def process(self, payload: Dict) -> AsyncIterator[Dict]:
        await asyncio.sleep(self._llm_delay_ms / 1000.0)
        yield {"text_response": self._llm_text}


def pct(values: List[float], q: float) -> float:
    if not values:
        return 0.0
    s = sorted(values)
    k = (len(s) - 1) * q
    f = int(k)
    c = min(f + 1, len(s) - 1)
    if f == c:
        return s[f]
    return s[f] + (s[c] - s[f]) * (k - f)


async def run_once(s: Scenario) -> Dict[str, float]:
    text_module = MockTextModule(llm_delay_ms=s.llm_delay_ms, llm_text=s.llm_text)
    audio_module = AudioProcessor()
    await audio_module.initialize()

    workflow = StreamingWorkflowIntegration(
        text_processor=text_module,
        audio_processor=audio_module,
        memory_workflow=None,
        text_filter_manager=None,
    )
    await workflow.initialize()

    request_data = {
        "text": s.prompt,
        "session_id": f"bench-{int(time.time() * 1000)}",
        "hardware_id": "bench-hw",
    }

    t0 = time.perf_counter()
    t_first_audio = None
    t_end = None

    async for item in workflow.process_request_streaming(request_data):
        if t_first_audio is None and item.get("audio_chunk"):
            t_first_audio = (time.perf_counter() - t0) * 1000.0
        if item.get("is_final"):
            t_end = (time.perf_counter() - t0) * 1000.0

    return {
        "first_audio_ms": t_first_audio or 0.0,
        "end_to_end_ms": t_end or 0.0,
    }


async def main() -> None:
    scenarios = [
        Scenario(
            prompt="send to Sophia in WhatsApp how are you doing",
            llm_delay_ms=120,
            llm_text="Sending a WhatsApp message to Sophia.",
        ),
        Scenario(
            prompt="open YouTube",
            llm_delay_ms=90,
            llm_text="Opening YouTube for you.",
        ),
        Scenario(
            prompt="what can you do for me",
            llm_delay_ms=150,
            llm_text="I can help with apps, messages, WhatsApp, browser, search and screen description.",
        ),
    ]

    runs = []
    for _ in range(2):
        for s in scenarios:
            metrics = await run_once(s)
            runs.append((s.prompt, metrics))
            print(
                f"prompt={s.prompt!r} first_audio_ms={metrics['first_audio_ms']:.1f} "
                f"end_to_end_ms={metrics['end_to_end_ms']:.1f}"
            )

    first_audio = [m["first_audio_ms"] for _, m in runs]
    e2e = [m["end_to_end_ms"] for _, m in runs]

    print("\nSummary")
    print(
        "first_audio_ms: "
        f"min={min(first_audio):.1f} p50={median(first_audio):.1f} "
        f"p95={pct(first_audio, 0.95):.1f} max={max(first_audio):.1f}"
    )
    print(
        "end_to_end_ms: "
        f"min={min(e2e):.1f} p50={median(e2e):.1f} "
        f"p95={pct(e2e, 0.95):.1f} max={max(e2e):.1f}"
    )


if __name__ == "__main__":
    asyncio.run(main())
