from modules.speech_playback.core import avf_player as avf


class _FakeSession:
    def __init__(self, *, category: str = "ambient", mode: str = "default"):
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
    monkeypatch.setattr(avf, "AVAudioSessionCategoryAmbient", "ambient")
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
    player._last_audio_session_signature = ("ambient", "default", 3, "route-a")

    player._deactivate_audio_session(reason="unit")

    assert fake_session.set_active_false_calls == 1
    assert player._session_active is False
    assert player._last_audio_session_signature is None


def test_shutdown_deactivates_immediately(monkeypatch):
    """shutdown() must deactivate audio session immediately (not deferred)."""
    player = avf.AVFoundationPlayer()
    calls = []

    def _fake_deactivate(*, reason: str):
        calls.append(reason)

    monkeypatch.setattr(player, "_deactivate_audio_session", _fake_deactivate)

    player.shutdown()

    assert "shutdown" in calls


def test_stop_playback_schedules_deferred_deactivation(monkeypatch):
    """stop_playback() schedules deferred deactivation (not immediate)."""
    player = avf.AVFoundationPlayer()
    deactivate_calls = []
    schedule_calls = []

    def _fake_deactivate(*, reason: str):
        deactivate_calls.append(reason)

    def _fake_schedule(*, reason: str, delay: float = 1.5):
        schedule_calls.append(reason)

    monkeypatch.setattr(player, "_deactivate_audio_session", _fake_deactivate)
    monkeypatch.setattr(player, "_schedule_deferred_deactivation", _fake_schedule)

    player.stop_playback()

    # Immediate deactivation must NOT fire
    assert "stop_playback" not in deactivate_calls
    # Deferred schedule MUST fire
    assert "stop_playback" in schedule_calls


def test_deferred_deactivation_fires_when_idle(monkeypatch):
    """Deferred timer fires deactivation if player stays idle."""
    import time

    fake_session = _configure_fake_session(monkeypatch)
    player = avf.AVFoundationPlayer()
    player._session_active = True
    player._playing = False  # idle

    player._schedule_deferred_deactivation(reason="test_idle", delay=0.1)
    time.sleep(0.3)  # wait for timer to fire

    assert fake_session.set_active_false_calls >= 1
    assert player._session_active is False


def test_deferred_deactivation_cancelled_by_start(monkeypatch):
    """start_playback() cancels pending deferred deactivation."""
    import time

    fake_session = _configure_fake_session(monkeypatch)
    player = avf.AVFoundationPlayer()
    player._session_active = True
    player._playing = False

    player._schedule_deferred_deactivation(reason="test_cancel", delay=0.5)
    # Simulate new playback starting before timer fires
    player._cancel_deferred_deactivation()
    time.sleep(0.7)

    # Deactivation must NOT have fired
    assert fake_session.set_active_false_calls == 0
    assert player._session_active is True


def test_playback_loop_exit_schedules_deferred(monkeypatch):
    """When _playback_loop exits, deferred deactivation is scheduled (not immediate)."""
    player = avf.AVFoundationPlayer()
    schedule_calls = []

    def _fake_schedule(*, reason: str, delay: float = 1.5):
        schedule_calls.append(reason)

    monkeypatch.setattr(player, "_schedule_deferred_deactivation", _fake_schedule)
    monkeypatch.setattr(avf, "AVAudioFormat", None)
    monkeypatch.setattr(avf, "AVAudioPCMBuffer", None)
    player._playing = True
    player._playback_loop()

    assert "playback_loop_exit" in schedule_calls
