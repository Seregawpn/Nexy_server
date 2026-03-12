from types import SimpleNamespace
from unittest.mock import patch

import pytest

from modules.memory_management.config import MemoryConfig
from modules.memory_management.core.memory_manager import MemoryManager


def test_memory_config_uses_vertex_api_key_from_text_processing_owner() -> None:
    unified = SimpleNamespace(
        memory=SimpleNamespace(
            gemini_api_key="legacy-gemini-key",
            max_short_term_memory_size=10240,
            max_long_term_memory_size=10240,
            memory_timeout=2.0,
            analysis_timeout=5.0,
            memory_analysis_model="gemini-2.5-flash-lite",
            memory_analysis_temperature=0.3,
        ),
        text_processing=SimpleNamespace(
            use_vertex_ai=True,
            vertex_project="vertex-project",
            vertex_location="global",
            vertex_api_key="vertex-owner-key",
            gemini_api_key="legacy-gemini-key",
        ),
    )

    with patch("modules.memory_management.config.get_config", return_value=unified):
        config = MemoryConfig()

    assert config.vertex_api_key == "vertex-owner-key"


@pytest.mark.asyncio
async def test_memory_manager_initializes_analyzer_in_vertex_mode_without_gemini_key() -> None:
    manager = MemoryManager(db_manager=None)
    manager.config = SimpleNamespace(
        gemini_api_key="",
        memory_analysis_model="gemini-2.5-flash-lite",
        memory_analysis_temperature=0.3,
        memory_analysis_prompt="prompt",
        use_vertex_ai=True,
        vertex_project="vertex-project",
        vertex_location="global",
        vertex_api_key="vertex-owner-key",
        validate_config=lambda: True,
    )

    captured = {}

    class _FakeAnalyzer:
        def __init__(self, gemini_api_key, **kwargs):
            captured["gemini_api_key"] = gemini_api_key
            captured.update(kwargs)

    with patch("modules.memory_management.core.memory_manager.MemoryAnalyzer", _FakeAnalyzer):
        result = await manager.initialize()

    assert result is True
    assert manager.memory_analyzer is not None
    assert captured["gemini_api_key"] == ""
    assert captured["use_vertex_ai"] is True
    assert captured["vertex_api_key"] == "vertex-owner-key"
