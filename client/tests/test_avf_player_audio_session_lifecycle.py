from modules.speech_playback.core import avf_player as avf


class _FakeSession:
    def __init__(self, *, category: str = "playback", mode: str = "default"):
        self._category = category
        self._mode = mode
        self.set_active_true_calls = 0
        self.set_active_false_calls = 0

    def category(self):
        return self._category

    def mode(self):
        return self._mode

    def setCategory_mode_options_error_(self, category, mode, _options, _error):
        self._category = str(category)
        self._mode = str(mode)

    def setActive_error_(self, active, _error):
        if active:
            self.set_active_true_calls += 1
        else:
            self.set_active_false_calls += 1
        return True, None


class _FakeAVAudioSession:
    _session = _FakeSession()

    @classmethod
    def sharedInstance(cls):
        return cls._session


def _configure_fake_session(monkeypatch):
    fake_session = _FakeSession()
    _FakeAVAudioSession._session = fake_session
    monkeypatch.setattr(avf, "AVAudioSession", _FakeAVAudioSession)
    monkeypatch.setattr(avf, "AVAudioSessionCategoryPlayback", "playback")
    monkeypatch.setattr(avf, "AVAudioSessionModeDefault", "default")
    monkeypatch.setattr(avf, "AVAudioSessionCategoryOptionAllowBluetoothA2DP", 1)
    monkeypatch.setattr(avf, "AVAudioSessionCategoryOptionMixWithOthers", 2)
    monkeypatch.setattr(avf, "AVAudioSessionCategoryOptionDuckOthers", 4)
    return fake_session


def test_ensure_session_skips_redundant_activation_when_already_active(monkeypatch):
    fake_session = _configure_fake_session(monkeypatch)
    player = avf.AVFoundationPlayer()
    player._session_active = True
    player._last_audio_session_signature = None
    monkeypatch.setattr(player, "_current_route_signature", lambda _session: "route-a")
    monkeypatch.setattr(player, "_capture_audio_session_runtime", lambda _session: {})

    player._ensure_playback_audio_session(reason="unit")

    assert fake_session.set_active_true_calls == 0
    assert player._session_active is True


def test_ensure_session_activates_when_not_active(monkeypatch):
    fake_session = _configure_fake_session(monkeypatch)
    player = avf.AVFoundationPlayer()
    player._session_active = False
    monkeypatch.setattr(player, "_current_route_signature", lambda _session: "route-a")
    monkeypatch.setattr(player, "_capture_audio_session_runtime", lambda _session: {})

    player._ensure_playback_audio_session(reason="unit")

    assert fake_session.set_active_true_calls == 1
    assert player._session_active is True


def test_deactivate_audio_session_resets_state(monkeypatch):
    fake_session = _configure_fake_session(monkeypatch)
    player = avf.AVFoundationPlayer()
    player._session_active = True
    player._last_audio_session_signature = ("playback", "default", 7, "route-a")

    player._deactivate_audio_session(reason="unit")

    assert fake_session.set_active_false_calls == 1
    assert player._session_active is False
    assert player._last_audio_session_signature is None


def test_stop_and_shutdown_trigger_deactivate(monkeypatch):
    player = avf.AVFoundationPlayer()
    calls = []

    def _fake_deactivate(*, reason: str):
        calls.append(reason)

    monkeypatch.setattr(player, "_deactivate_audio_session", _fake_deactivate)

    player.stop_playback()
    player.shutdown()

    assert "stop_playback" in calls
    assert "shutdown" in calls
