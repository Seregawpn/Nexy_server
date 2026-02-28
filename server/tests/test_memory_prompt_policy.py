from pathlib import Path
import sys


project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.memory_management.config import MemoryConfig


def test_memory_prompt_contains_expanded_short_and_long_term_policy():
    prompt = MemoryConfig().memory_analysis_prompt

    assert "SHORT-TERM MEMORY (current operational context)" in prompt
    assert "EXISTING_SHORT_MEMORY: {existing_short_memory}" in prompt
    assert "EXISTING_MEDIUM_MEMORY: {existing_medium_memory}" in prompt
    assert "EXISTING_LONG_MEMORY: {existing_long_memory}" in prompt
    assert "CURRENT_DATE_UTC: {current_date_utc}" in prompt
    assert "Record information in brief form, but include all necessary key points and keywords." in prompt
    assert "Use compact clauses separated by \"; \"" in prompt
    assert "MEDIUM-TERM MEMORY (cross-session digest)" in prompt
    assert "Every medium-term fact MUST start with date in format [YYYY-MM-DD]." in prompt
    assert "Use ONLY CURRENT_DATE_UTC as the reference date for aging" in prompt
    assert "CURRENT_DATE_UTC is always provided in input" in prompt
    assert "Daily accumulation policy (MEDIUM_TERM only):" in prompt
    assert "Keep existing medium-term records from previous dates." in prompt
    assert "When CURRENT_DATE_UTC is a new date not present in MEDIUM_TERM, create a new dated record" in prompt
    assert "When CURRENT_DATE_UTC date already exists in MEDIUM_TERM, update/append that same date record" in prompt
    assert "Keep one consolidated record per date" in prompt
    assert "Never delete previous-date records just because a new day started." in prompt
    assert "Step 1: Parse entry date from [YYYY-MM-DD]" in prompt
    assert "Step 2: Compute age_days = (CURRENT_DATE_UTC - entry_date)" in prompt
    assert "Step 3: If age_days > 30, remove this medium-term fact." in prompt
    assert "Step 4: If age_days <= 30, keep this medium-term fact." in prompt
    assert "Step 5: If a medium-term fact has no valid [YYYY-MM-DD], remove it" in prompt
    assert "Do NOT duplicate information inside a section." in prompt
    assert "Each fact must appear only once per section." in prompt
    assert "you MUST remove that information from all relevant memory sections (SHORT_TERM, MEDIUM_TERM, LONG_TERM)" in prompt
    assert "Forget requests are mandatory" in prompt
    assert "If age_days > 30, remove this medium-term fact." in prompt
    assert "This 30-day removal rule applies ONLY to MEDIUM_TERM." in prompt
    assert "Do NOT remove LONG_TERM facts because of age." in prompt
    assert "LONG-TERM MEMORY (stable user profile, cross-session)" in prompt
    assert "Keep it concise, but preserve all necessary key points and keywords for personalization." in prompt
    assert "STRICT FACTS ONLY:" in prompt
    assert "Do NOT infer, guess, or generalize from one-time requests." in prompt
    assert 'If user says a direct fact (example: "I love sneakers"), this MAY be stored in LONG_TERM.' in prompt
    assert 'If user asks a task/request (example: "find me sneakers"), this is NOT a stable preference and MUST NOT be stored in LONG_TERM.' in prompt
    assert "date of birth, marital status, family status" in prompt
    assert "important file names, folder paths, project directories" in prompt
    assert "important emails/usernames/contact identifiers" in prompt
    assert "favorite music, artists, movies, series, books, sports" in prompt
    assert "favorite websites/services/apps used repeatedly" in prompt
    assert "projects, roles, recurring work context, long-term goals" in prompt
    assert "remove ONLY those requested facts from LONG_TERM and keep all other valid facts." in prompt
    assert "For partial forget requests, return LONG_TERM as updated fact list without deleted items" in prompt
    assert "LONG_TERM: __CLEAR_LONG_TERM__" in prompt
    assert "safe reference" in prompt
    assert "never raw secret values" in prompt.lower()


def test_memory_analyzer_has_no_default_prompt_fallback():
    analyzer_source = (project_root / "modules/memory_management/providers/memory_analyzer.py").read_text()

    assert "DEFAULT_ANALYSIS_PROMPT_TEMPLATE" not in analyzer_source
    assert "analysis_prompt_template is required and must come from MemoryConfig" in analyzer_source
