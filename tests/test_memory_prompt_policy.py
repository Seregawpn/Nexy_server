from pathlib import Path
import sys


project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.memory_management.config import MemoryConfig
from modules.memory_management.providers.memory_analyzer import MemoryAnalyzer


def test_memory_prompt_contains_expanded_short_and_long_term_policy():
    config = MemoryConfig()
    prompt = config.memory_analysis_prompt

    assert "EXISTING_CURRENT_GOAL: {existing_current_goal}" in prompt
    assert "GOAL_STATE:" in prompt
    assert "CURRENT GOAL (active executable user goal)" in prompt
    assert "GOAL_STATE must be exactly one of:" in prompt
    assert "set" in prompt
    assert "keep" in prompt
    assert "clear" in prompt
    assert "replace" in prompt
    assert "empty" in prompt
    assert "CURRENT_GOAL must be plain text only and must never use JSON or nested structure." in prompt
    assert "The final response MUST contain exactly these labels in this exact order:" in prompt
    assert "GOAL_STATE:" in prompt
    assert 'Do NOT output numbered headings like "0) CURRENT GOAL"' in prompt
    assert "Do NOT output unlabeled bare lines." in prompt
    assert "Canonical response example:" in prompt
    assert "GOAL_STATE: keep" in prompt
    assert "CURRENT_GOAL: User wants to send a message to Sophia. Missing detail: message text." in prompt
    assert "SHORT_TERM: [2026-03-07 00:00:00 UTC] USER: Send a message to Sophia | ASSISTANT: What message would you like to send to Sophia?" in prompt
    assert "Return exactly one plain-text line describing the current active executable goal." in prompt
    assert "If the turn is ordinary conversation, small talk, gratitude, capability/help, meta-conversation, or no executable goal exists, return EMPTY." in prompt
    assert "If the user explicitly rejects, cancels, abandons, or declines the previous task, CURRENT_GOAL must be EMPTY unless the same turn clearly starts a new executable task." in prompt
    assert "Universal task lifecycle policy:" in prompt
    assert "Decide lifecycle by task continuity and task outcome, never by isolated keywords." in prompt
    assert "Use the same decision model for all executable categories: messages, WhatsApp, browser, web search, system control, payment, and future executable categories." in prompt
    assert "Highest priority: if the task is unfinished after this turn, CURRENT_GOAL must stay semantically correct and active for the exact unfinished task." in prompt
    assert "Highest priority: if the task is already finished in this turn, no active CURRENT_GOAL should remain after the turn." in prompt
    assert "Decision framework:" in prompt
    assert "Was there an active executable task before this turn?" in prompt
    assert "Does the current user turn start a new executable task, continue the same task, cancel the old task, or replace it with a new one?" in prompt
    assert "Task identity rules:" in prompt
    assert "Missing details do not create a new task. A task with unresolved details is still the same task." in prompt
    assert 'Referential follow-up like "tell her ...", "send it", "world news", "Safari", or "sleep music instead" should usually continue the active task' in prompt
    assert "If the user abandons the old task and starts a different explicit task in the same turn, use replace only when that new task remains active after the turn." in prompt
    assert "If the user abandons the old task and the new explicit task is also fully completed in the same turn, use clear because no active executable goal remains after the turn." in prompt
    assert "Outcome rules:" in prompt
    assert "Clarification question for an unfinished task means the task remains active after the turn." in prompt
    assert "While the task remains unfinished, prefer the correct active CURRENT_GOAL over any shortcut that would drop or reset the goal too early." in prompt
    assert "Immediate execution means the task is not active after the turn unless the assistant explicitly leaves another required step unfinished." in prompt
    assert "For completed turns, the important terminal outcome is that CURRENT_GOAL is EMPTY after the turn." in prompt
    assert 'Add "Missing detail: ..." only when one required detail is truly blocking execution right now.' in prompt
    assert 'Add "Missing detail: ..." only when the assistant explicitly asks for that detail in this response.' in prompt
    assert "Keep only one most critical missing detail." in prompt
    assert "Do not keep old missing details once they are provided, no longer relevant, or the task is completed." in prompt
    assert "If the task is executable now, do not include Missing detail." in prompt
    assert "SHORT-TERM MEMORY (current operational context)" in prompt
    assert "SHORT_TERM must be exactly one line and must describe only the current turn." in prompt
    assert "REQUIRED exact shape:" in prompt
    assert "[YYYY-MM-DD HH:MM:SS UTC] USER: <plain summary> | ASSISTANT: <plain summary>" in prompt
    assert "Do NOT include labels like CURRENT, PREVIOUS, TURN, CONTEXT, CURRENT_REQUEST, PREVIOUS_REQUEST_n, DATE_UTC, TIME_UTC." in prompt
    assert "rewrite it into one short plain-language action description before storing memory" in prompt
    assert '{"command":"open_app","args":{"app_name":"Safari"}} -> opened Safari' in prompt
    assert '{"command":"browser_search","args":{"query":"weather in Toronto"}} -> started a browser search for weather in Toronto' in prompt
    assert "EXISTING_SHORT_MEMORY: {existing_short_memory}" in prompt
    assert "EXISTING_MEDIUM_MEMORY: {existing_medium_memory}" in prompt
    assert "EXISTING_LONG_MEMORY: {existing_long_memory}" in prompt
    assert "CURRENT_DATE_UTC: {current_date_utc}" in prompt
    assert "MEDIUM-TERM MEMORY (daily analytical summary)" in prompt
    assert "MEDIUM_TERM is a day-level summary built from short-term interactions." in prompt
    assert "Return EXACTLY one new MEDIUM_TERM line for the current day." in prompt
    assert "The line should briefly and logically summarize what happened during the day:" in prompt
    assert "which goals were pursued" in prompt
    assert "what kinds of tasks were performed overall" in prompt
    assert "what meaningful outcomes were achieved" in prompt
    assert "what was special/important that day" in prompt
    assert "what assistant requested/clarified from the user that day" in prompt
    assert "Do NOT copy raw dialogue and do NOT include runtime/transcript labels." in prompt
    assert "rewrite that into short plain-language descriptions of what assistant did" in prompt
    assert "REQUIRED exact shape:" in prompt
    assert "[YYYY-MM-DD] <complete daily summary sentence>" in prompt
    assert "Do NOT duplicate information inside a section." in prompt
    assert "Merge policy is mandatory: output must include valid existing entries from EXISTING_SHORT_MEMORY, EXISTING_MEDIUM_MEMORY, and EXISTING_LONG_MEMORY, plus new/updated entries from the current turn." in prompt
    assert "Do not replace the whole section with only new data if older valid data exists; keep prior valid items and append/update them in canonical format." in prompt
    assert "MEDIUM_TERM MUST be derived from current + existing SHORT_TERM context (not from raw tool payloads)." in prompt
    assert "This section is active only in the dedicated once-per-24-hours medium-rollup call controlled by runtime/orchestrator." in prompt
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
    prompt_without_current_goal = config.build_memory_analysis_prompt(include_current_goal=False)
    assert "CURRENT_GOAL update is inactive for this call." in prompt_without_current_goal
    assert "Return CURRENT_GOAL exactly as EXISTING_CURRENT_GOAL" in prompt_without_current_goal
    prompt_without_long = config.build_memory_analysis_prompt(include_long_term=False)
    assert "LONG_TERM update is inactive for this call." in prompt_without_long
    assert "Return LONG_TERM exactly as EXISTING_LONG_MEMORY" in prompt_without_long
    assert "LONG-TERM MEMORY (stable user profile, cross-session)" in prompt
    assert "Keep it concise, but preserve all necessary key points and keywords for personalization." in prompt
    assert "LONG_TERM must contain plain factual lines only." in prompt
    assert "Each line must be one complete stable fact about the user." in prompt
    assert "STRICT FACTS ONLY:" in prompt
    assert "Do NOT infer, guess, or generalize from one-time requests." in prompt
    assert 'If user says a direct fact (example: "I love sneakers"), this MAY be stored in LONG_TERM.' in prompt
    assert 'If user asks a task/request (example: "find me sneakers"), this is NOT a stable preference and MUST NOT be stored in LONG_TERM.' in prompt
    assert "first name / last name / preferred name" in prompt
    assert "work profile / recurring projects / project directories" in prompt
    assert "remove ONLY those requested facts from LONG_TERM and keep all other valid facts." in prompt
    assert "For partial forget requests, return LONG_TERM as updated fact list without deleted items" in prompt
    assert "LONG_TERM: __CLEAR_LONG_TERM__" in prompt
    assert "User has Gmail account credentials saved elsewhere." in prompt
    assert "never raw secret values" in prompt.lower()
    assert "raw JSON, command payloads, args objects, tool schemas, or runtime action metadata." in prompt


def test_memory_analyzer_has_no_default_prompt_fallback():
    analyzer_source = (project_root / "modules/memory_management/providers/memory_analyzer.py").read_text()

    assert "DEFAULT_ANALYSIS_PROMPT_TEMPLATE" not in analyzer_source
    assert "analysis_prompt_template is required and must come from MemoryConfig" in analyzer_source


def test_memory_analyzer_safe_prompt_format_preserves_json_examples():
    template = (
        'USER INPUT: {prompt}\\n'
        'EXAMPLE: {"command":"open_app","args":{"app_name":"Safari"}}\\n'
        'EXISTING_CURRENT_GOAL: {existing_current_goal}'
    )

    rendered = MemoryAnalyzer._safe_format_analysis_prompt(
        template,
        prompt="Open Safari",
        existing_current_goal="EMPTY",
    )

    assert 'USER INPUT: Open Safari' in rendered
    assert 'EXISTING_CURRENT_GOAL: EMPTY' in rendered
    assert '{"command":"open_app","args":{"app_name":"Safari"}}' in rendered


def test_current_goal_prompt_is_separable_and_reusable():
    config = MemoryConfig()

    active_goal_prompt = config.build_current_goal_prompt(active=True)
    inactive_goal_prompt = config.build_current_goal_prompt(active=False)

    assert "0) CURRENT GOAL (active executable user goal):" in active_goal_prompt
    assert "First output GOAL_STATE on its own single line." in active_goal_prompt
    assert "Activation rules:" in active_goal_prompt
    assert "Lifecycle rules:" in active_goal_prompt
    assert "For product correctness, goal continuity while the task is unfinished is more important than the exact terminal label after the task is already finished." in active_goal_prompt
    assert "If the user continues an active browser task with a short or noisy follow-up and the assistant immediately performs that browser action in the same turn, use clear and return CURRENT_GOAL as EMPTY." in active_goal_prompt
    assert "If the user provides a short topical follow-up that fills the active search task's missing topic and the assistant returns the factual search answer in the same turn, use clear and return CURRENT_GOAL as EMPTY." in active_goal_prompt
    assert "If an active messaging or WhatsApp goal already knows the recipient and a short or noisy follow-up provides the message body, then sending that message in the same turn is clear and CURRENT_GOAL must be EMPTY." in active_goal_prompt
    assert "If the same turn abandons the old goal and immediately returns the final factual answer for a new search task, use clear and return CURRENT_GOAL as EMPTY because no executable goal remains active after the turn." in active_goal_prompt
    assert "Universal task lifecycle policy:" in active_goal_prompt
    assert "Decision framework:" in active_goal_prompt
    assert "Task identity rules:" in active_goal_prompt
    assert "Outcome rules:" in active_goal_prompt
    assert "If the user explicitly rejects, cancels, abandons, or declines the previous task" in active_goal_prompt
    assert "CURRENT_GOAL being EMPTY is mandatory even if clear vs empty is later interpreted differently by downstream product checks." in active_goal_prompt
    assert "Missing detail rules:" in active_goal_prompt
    assert "Good examples:" in active_goal_prompt
    assert "GOAL_STATE: empty" in active_goal_prompt
    assert "USER: Open Safari / ASSISTANT: Opening Safari. -> GOAL_STATE: empty" in active_goal_prompt
    assert "USER: Message Mom on WhatsApp / ASSISTANT: What message do you want to send to Mom? -> GOAL_STATE: set / CURRENT_GOAL: User wants to send a WhatsApp message to Mom. Missing detail: message text." in active_goal_prompt
    assert "EXISTING_CURRENT_GOAL: EMPTY / USER: world news / ASSISTANT: Here are the latest world news headlines. -> GOAL_STATE: empty / CURRENT_GOAL: EMPTY" in active_goal_prompt
    assert "EXISTING_CURRENT_GOAL: EMPTY / USER: Find latest world news / ASSISTANT: The latest world news includes ongoing tensions in the Middle East ... -> GOAL_STATE: empty / CURRENT_GOAL: EMPTY" in active_goal_prompt
    assert "EXISTING_CURRENT_GOAL: User wants latest news. Missing detail: topic. / USER: world headlines / ASSISTANT: Here are the latest world headlines. -> GOAL_STATE: clear / CURRENT_GOAL: EMPTY" in active_goal_prompt
    assert "EXISTING_CURRENT_GOAL: User wants to send a message to Sophia. Missing detail: message text. / USER: snd her ill b outside in 2 / ASSISTANT: Sending message to Sophia. -> GOAL_STATE: clear / CURRENT_GOAL: EMPTY" in active_goal_prompt
    assert "EXISTING_CURRENT_GOAL: EMPTY / USER: world news / ASSISTANT: Here are the latest world news headlines. -> GOAL_STATE: clear / CURRENT_GOAL: EMPTY" not in active_goal_prompt
    assert "prefer replace over clear even if the assistant immediately starts executing the new task" not in active_goal_prompt
    assert "CURRENT_GOAL update is inactive for this call." in inactive_goal_prompt
    assert "GOAL_STATE: empty" in inactive_goal_prompt
