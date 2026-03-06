from pathlib import Path
import sys


project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.memory_management.config import MemoryConfig


def test_memory_prompt_contains_expanded_short_and_long_term_policy():
    config = MemoryConfig()
    prompt = config.memory_analysis_prompt

    assert "SHORT-TERM MEMORY (current operational context)" in prompt
    assert "SHORT_TERM must be exactly one line and must describe only the current turn." in prompt
    assert "Do NOT include labels like CURRENT, PREVIOUS, TURN, TIME_UTC, CURRENT_REQUEST, PREVIOUS_REQUEST_n." in prompt
    assert "Recommended shape:" in prompt
    assert "user_request=<plain summary>; assistant_reply=<plain summary>; outcome=<plain summary>" in prompt
    assert "EXISTING_SHORT_MEMORY: {existing_short_memory}" in prompt
    assert "EXISTING_MEDIUM_MEMORY: {existing_medium_memory}" in prompt
    assert "EXISTING_LONG_MEMORY: {existing_long_memory}" in prompt
    assert "CURRENT_DATE_UTC: {current_date_utc}" in prompt
    assert "Use compact clauses separated by \"; \"" in prompt
    assert "MEDIUM-TERM MEMORY (daily analytical summary)" in prompt
    assert "MEDIUM_TERM is a day-level summary built from short-term interactions." in prompt
    assert "Every entry MUST start with [YYYY-MM-DD]." in prompt
    assert "Return EXACTLY one MEDIUM_TERM line (single-line output, no extra lines)." in prompt
    assert "Parser expects one line only: do not output multi-line bullets/tables/numbered blocks." in prompt
    assert "which goals were pursued" in prompt
    assert "what kinds of tasks were performed overall" in prompt
    assert "what meaningful outcomes were achieved" in prompt
    assert "what was special/important that day" in prompt
    assert "Do NOT copy raw dialogue and do NOT include runtime/transcript labels." in prompt
    assert "MEDIUM_TERM must be returned as a single output line." in prompt
    assert 'If there are multiple daily records, keep them in that same line separated by " || ".' in prompt
    assert "Ordering rule: newest record first, oldest record last." in prompt
    assert "One record = one day summary (do NOT create separate records for each individual task)." in prompt
    assert "Within each day record, aggregate repeated requests into one consolidated summary." in prompt
    assert "Do not duplicate topic/action/outcome values inside the same day record." in prompt
    assert "Each day record must be a complete, logically finished text." in prompt
    assert "Preferred record shape:" in prompt
    assert "daily_summary=<complete sentence>" in prompt
    assert "key_actions=<category1|category2>" in prompt
    assert "outcomes=<result1|result2>" in prompt
    assert "repeat_signals=<signal1 xN|signal2 xM>" in prompt
    assert "status=<done|in_progress|mixed>" in prompt
    assert "Do NOT duplicate information inside a section." in prompt
    assert "Merge policy is mandatory: output must include valid existing entries from EXISTING_SHORT_MEMORY, EXISTING_MEDIUM_MEMORY, and EXISTING_LONG_MEMORY, plus new/updated entries from the current turn." in prompt
    assert "Do not replace the whole section with only new data if older valid data exists; keep prior valid items and append/update them in canonical format." in prompt
    assert "Processing order is mandatory: first analyze/update SHORT_TERM, then derive/update MEDIUM_TERM from SHORT_TERM, and only after that SHORT_TERM may be reduced/cleaned by runtime policies." in prompt
    assert "Never lose day context: if SHORT_TERM contains useful daily activity, reflect it in MEDIUM_TERM before any short-term cleanup." in prompt
    assert "MEDIUM_TERM activation is trigger-based. Use activation phrase exactly: MEDIUM_TERM_ROLLUP_24H=ON." in prompt
    assert "If activation phrase is missing, keep MEDIUM_TERM unchanged from EXISTING_MEDIUM_MEMORY (or EMPTY if no existing value)." in prompt
    assert "24h cadence owner is runtime/orchestrator: trigger phrase should be injected no more than once per 24 hours." in prompt
    assert "MEDIUM_TERM MUST be derived from current + existing SHORT_TERM context (not from raw tool payloads)." in prompt
    assert "MEDIUM_TERM must be recalculated/updated only when activation phrase MEDIUM_TERM_ROLLUP_24H=ON is present." in prompt
    assert config.memory_analysis_short_term_prompt_active.strip() in prompt
    assert config.memory_analysis_medium_term_prompt_active.strip() in prompt
    assert config.memory_analysis_long_term_prompt_active.strip() in prompt
    prompt_without_medium_rollup = config.build_memory_analysis_prompt(include_medium_rollup=False)
    assert "MEDIUM_TERM rollup is inactive for this call." in prompt_without_medium_rollup
    assert "Return MEDIUM_TERM exactly as EXISTING_MEDIUM_MEMORY" in prompt_without_medium_rollup
    assert "Do NOT derive new medium-term summaries in this call." in prompt_without_medium_rollup
    prompt_without_short = config.build_memory_analysis_prompt(include_short_term=False)
    assert "SHORT_TERM update is inactive for this call." in prompt_without_short
    assert "Return SHORT_TERM exactly as EXISTING_SHORT_MEMORY" in prompt_without_short
    prompt_without_long = config.build_memory_analysis_prompt(include_long_term=False)
    assert "LONG_TERM update is inactive for this call." in prompt_without_long
    assert "Return LONG_TERM exactly as EXISTING_LONG_MEMORY" in prompt_without_long
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
