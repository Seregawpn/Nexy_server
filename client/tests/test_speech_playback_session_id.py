import os
import sys
import uuid

sys.path.insert(0, os.getcwd())

from integration.integrations.speech_playback_integration import SpeechPlaybackIntegration


def test_ensure_raw_session_id_generates_uuid_for_missing() -> None:
    sid, raw = SpeechPlaybackIntegration._ensure_raw_session_id(None)
    assert raw is True
    assert str(uuid.UUID(sid, version=4)) == sid


def test_ensure_raw_session_id_keeps_valid_uuid() -> None:
    source = str(uuid.uuid4())
    sid, raw = SpeechPlaybackIntegration._ensure_raw_session_id(source)
    assert sid == source
    assert raw is False


def test_ensure_raw_session_id_replaces_legacy_non_uuid() -> None:
    sid, raw = SpeechPlaybackIntegration._ensure_raw_session_id("raw:welcome_message:1770741786257")
    assert raw is True
    assert str(uuid.UUID(sid, version=4)) == sid
