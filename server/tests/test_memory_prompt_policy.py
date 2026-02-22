from pathlib import Path
import sys


project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.memory_management.config import MemoryConfig


def test_memory_prompt_contains_expanded_short_and_long_term_policy():
    prompt = MemoryConfig().memory_analysis_prompt

    assert "SHORT-TERM MEMORY (session context, quickly expiring, operational)" in prompt
    assert "LONG-TERM MEMORY (stable user profile, cross-session)" in prompt
    assert "favorite music, artists, movies, series, books, sports" in prompt
    assert "favorite websites/services/apps used repeatedly" in prompt
    assert "projects, roles, recurring work context, long-term goals" in prompt
    assert "safe reference" in prompt
    assert "NEVER store raw secret values" in prompt


def test_memory_analyzer_has_no_default_prompt_fallback():
    analyzer_source = (project_root / "modules/memory_management/providers/memory_analyzer.py").read_text()

    assert "DEFAULT_ANALYSIS_PROMPT_TEMPLATE" not in analyzer_source
    assert "analysis_prompt_template is required and must come from MemoryConfig" in analyzer_source
