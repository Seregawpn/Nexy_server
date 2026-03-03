#!/usr/bin/env python3
import asyncio
import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from modules.text_processing.core.text_processor import TextProcessor
from config.unified_config import get_config

QUERY = os.getenv("QUERY", "latest news about SpaceX")
TIMEOUT = float(os.getenv("TIMEOUT", "12"))


async def main() -> None:
    cfg = get_config().get_module_config("text_processing")
    processor = TextProcessor(cfg)
    ok = await processor.initialize()
    print(f"initialized: {ok}")
    if not ok:
        return

    print(f"query: {QUERY}")

    async def collect_first_chunk():
        async for chunk in processor.process_text_streaming(
            QUERY,
            session_id="smoke-websearch",
            use_search=True,
        ):
            return chunk
        return None

    try:
        chunk = await asyncio.wait_for(collect_first_chunk(), timeout=TIMEOUT)
        if chunk is None:
            print("result: no chunks")
            return
        print(f"first_chunk_len: {len(chunk)}")
        print("first_chunk_preview:")
        print(chunk[:1000])
    except asyncio.TimeoutError:
        print(f"result: TIMEOUT after {TIMEOUT}s")
    except Exception as exc:
        print(f"result: ERROR {type(exc).__name__}: {exc}")


if __name__ == "__main__":
    asyncio.run(main())
