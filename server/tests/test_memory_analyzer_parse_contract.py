from modules.memory_management.providers.memory_analyzer import MemoryAnalyzer


def _analyzer() -> MemoryAnalyzer:
    return MemoryAnalyzer.__new__(MemoryAnalyzer)


def test_parse_three_line_contract_with_labels():
    analyzer = _analyzer()
    text = (
        "SHORT_TERM: Current task is choosing sneakers\n"
        "MEDIUM_TERM: Last week user compared white and black models\n"
        "LONG_TERM: User likes running; Preferred language is English\n"
        
    )

    short_memory, medium_memory, long_memory = analyzer._parse_analysis_response(text)

    assert "choosing sneakers" in short_memory
    assert "Last week" in medium_memory
    assert "User likes running" in long_memory


def test_parse_rejects_missing_section_label():
    analyzer = _analyzer()
    text = (
        "SHORT_TERM: Current context for this session\n"
        "LONG_TERM: User likes sports\n"
        
    )

    short_memory, medium_memory, long_memory = analyzer._parse_analysis_response(text)

    assert short_memory == ""
    assert medium_memory == ""
    assert long_memory == ""


def test_parse_repairs_wrong_label_order():
    analyzer = _analyzer()
    text = (
        "SHORT_TERM: session context\n"
        "LONG_TERM: User likes sports\n"
        "MEDIUM_TERM: previous topic\n"
        
    )

    short_memory, medium_memory, long_memory = analyzer._parse_analysis_response(text)

    assert short_memory == "session context"
    assert medium_memory == "previous topic"
    assert long_memory == "User likes sports"


def test_parse_rejects_leading_or_trailing_extra_text():
    analyzer = _analyzer()
    text = (
        "Here is memory update:\n"
        "SHORT_TERM: session context\n"
        "MEDIUM_TERM: previous topic\n"
        "LONG_TERM: user likes sports\n"
        
        "Done."
    )

    short_memory, medium_memory, long_memory = analyzer._parse_analysis_response(text)

    assert short_memory == ""
    assert medium_memory == ""
    assert long_memory == ""


def test_parse_repairs_code_fence_wrapping():
    analyzer = _analyzer()
    text = (
        "```text\n"
        "SHORT_TERM: session context\n"
        "MEDIUM_TERM: previous topic\n"
        "LONG_TERM: user likes sports\n"
        
        "```"
    )

    short_memory, medium_memory, long_memory = analyzer._parse_analysis_response(text)

    assert short_memory == "session context"
    assert medium_memory == "previous topic"
    assert long_memory == "user likes sports"


def test_parse_repairs_label_variants_and_numbering():
    analyzer = _analyzer()
    text = (
        "1) SHORT TERM: session context\n"
        "2) MEDIUM-TERM: previous topic\n"
        "3) LONG TERM: user likes sports"
    )

    short_memory, medium_memory, long_memory = analyzer._parse_analysis_response(text)

    assert short_memory == "session context"
    assert medium_memory == "previous topic"
    assert long_memory == "user likes sports"


def test_parse_repairs_fullwidth_colon_and_preamble():
    analyzer = _analyzer()
    text = (
        "Memory update below:\n"
        "SHORT_TERM：session context\n"
        "MEDIUM_TERM：previous topic\n"
        "LONG_TERM：user likes sports"
    )

    short_memory, medium_memory, long_memory = analyzer._parse_analysis_response(text)

    assert short_memory == "session context"
    assert medium_memory == "previous topic"
    assert long_memory == "user likes sports"


def test_parse_rejects_duplicate_labels():
    analyzer = _analyzer()
    text = (
        "SHORT_TERM: session context\n"
        "MEDIUM_TERM: previous topic\n"
        "LONG_TERM: user likes sports\n"
        
        "LONG_TERM: duplicate label"
    )

    short_memory, medium_memory, long_memory = analyzer._parse_analysis_response(text)

    assert short_memory == ""
    assert medium_memory == ""
    assert long_memory == ""


def test_parse_sanitizes_secret_values():
    analyzer = _analyzer()
    text = (
        "SHORT_TERM: password reset discussion\n"
        "MEDIUM_TERM: token was shared in previous message\n"
        "LONG_TERM: remember api key abc123\n"
        
    )

    short_memory, medium_memory, long_memory = analyzer._parse_analysis_response(text)

    assert "password" not in short_memory.lower()
    assert "token" not in medium_memory.lower()
    assert "api key" not in long_memory.lower()


def test_parse_deduplicates_semicolon_facts():
    analyzer = _analyzer()
    text = (
        "SHORT_TERM: discussed montreal weather; discussed montreal weather\n"
        "MEDIUM_TERM: discussed sneakers shortlist; discussed sneakers shortlist\n"
        "LONG_TERM: user likes running; user likes running\n"
        
    )

    short_memory, medium_memory, long_memory = analyzer._parse_analysis_response(text)

    assert short_memory.count("discussed montreal weather") == 1
    assert medium_memory.count("discussed sneakers shortlist") == 1
    assert long_memory.count("user likes running") == 1


def test_parse_filters_inferred_and_one_off_from_long_term():
    analyzer = _analyzer()
    text = (
        "SHORT_TERM: user asked for sneakers\n"
        "MEDIUM_TERM: discussed sneakers request\n"
        "LONG_TERM: Implied interest in sneakers; user asked me to find sneakers; Name is Sergiy\n"
        
    )

    short_memory, medium_memory, long_memory = analyzer._parse_analysis_response(text)

    assert "asked for sneakers" in short_memory
    assert "discussed sneakers request" in medium_memory
    assert "Implied interest in sneakers" not in long_memory
    assert "asked me to find sneakers" not in long_memory
    assert "Name is Sergiy" in long_memory


def test_parse_keeps_identity_fact_even_with_request_wording():
    analyzer = _analyzer()
    text = (
        "SHORT_TERM: user asked to remember name\n"
        "MEDIUM_TERM: discussed memory\n"
        "LONG_TERM: User asked me to remember that my name is Sergiy\n"
        
    )

    _, _, long_memory = analyzer._parse_analysis_response(text)

    assert "sergiy" in long_memory.lower()


def test_parse_contract_stability_10_runs():
    analyzer = _analyzer()
    inputs = [
        (
            "SHORT_TERM: Current communication: Name provided\n"
            "MEDIUM_TERM: [2026-02-28] Discussed profile; captured identity.\n"
            "LONG_TERM: User name: Sergey"
        ),
        (
            "SHORT_TERM: Current communication: User asked recall\n"
            "MEDIUM_TERM: [2026-02-28] Discussed memory recall; pending verification.\n"
            "LONG_TERM: Preferred language: Russian"
        ),
        (
            "SHORT_TERM: Current communication: Asked to forget nickname\n"
            "MEDIUM_TERM: [2026-02-28] Discussed forget request; update required.\n"
            "LONG_TERM: __CLEAR_LONG_TERM__"
        ),
        (
            "SHORT_TERM: Current communication: Planning tasks\n"
            "MEDIUM_TERM: [2026-02-28] Discussed weekly planning; agreed workflow.\n"
            "LONG_TERM: Work profile: Product manager"
        ),
        (
            "SHORT_TERM: Current communication: Updated pronunciation\n"
            "MEDIUM_TERM: [2026-02-28] Discussed pronunciation preferences; accepted.\n"
            "LONG_TERM: Name pronunciation: Ser-gay"
        ),
        (
            "SHORT_TERM: Current communication: Review preferences\n"
            "MEDIUM_TERM: [2026-02-28] Discussed answer style; concise requested.\n"
            "LONG_TERM: Communication preference: concise"
        ),
        (
            "SHORT_TERM: Current communication: Project context updated\n"
            "MEDIUM_TERM: [2026-02-28] Discussed project directory; confirmed.\n"
            "LONG_TERM: Project directory: /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27"
        ),
        (
            "SHORT_TERM: Current communication: Running diagnostics\n"
            "MEDIUM_TERM: [2026-02-28] Discussed diagnostics flow; validated.\n"
            "LONG_TERM: Recurring routine: run memory diagnostics before release"
        ),
        (
            "SHORT_TERM: Current communication: Cross-session recall check\n"
            "MEDIUM_TERM: [2026-02-28] Discussed recall reliability; improving parser.\n"
            "LONG_TERM: Stable interest: system reliability"
        ),
        (
            "SHORT_TERM: Current communication: Parser contract finalized\n"
            "MEDIUM_TERM: [2026-02-28] Discussed strict format; adopted.\n"
            "LONG_TERM: Memory contract: strict_three_sections"
        ),
        (
            "SHORT_TERM: Current communication: User shared timezone\n"
            "MEDIUM_TERM: [2026-02-28] Discussed scheduling; timezone clarified.\n"
            "LONG_TERM: Timezone: America/Toronto"
        ),
        (
            "SHORT_TERM: Current communication: User shared preferred nickname\n"
            "MEDIUM_TERM: [2026-02-28] Discussed addressing style; nickname accepted.\n"
            "LONG_TERM: Preferred nickname: Serge"
        ),
        (
            "SHORT_TERM: Current communication: User clarified communication language\n"
            "MEDIUM_TERM: [2026-02-28] Discussed bilingual flow; selected language.\n"
            "LONG_TERM: Preferred language: Russian"
        ),
        (
            "SHORT_TERM: Current communication: User shared recurring project name\n"
            "MEDIUM_TERM: [2026-02-28] Discussed current project; repository confirmed.\n"
            "LONG_TERM: Recurring project: Nexy"
        ),
        (
            "SHORT_TERM: Current communication: User requested concise diagnostics\n"
            "MEDIUM_TERM: [2026-02-28] Discussed debug reports; concise format chosen.\n"
            "LONG_TERM: Report preference: concise technical format"
        ),
    ]

    assert len(inputs) == 15

    for payload in inputs:
        short_memory, medium_memory, long_memory = analyzer._parse_analysis_response(payload)
        assert short_memory != ""
        assert medium_memory != ""
        assert long_memory != ""
