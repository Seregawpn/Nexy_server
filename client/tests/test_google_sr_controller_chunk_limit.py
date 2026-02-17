from types import SimpleNamespace

from modules.voice_recognition.core.google_sr_controller import GoogleSRController


class _DummyMicrophone:
    def __init__(self, device_index=None):
        self.device_index = device_index

    def __enter__(self):
        return object()

    def __exit__(self, exc_type, exc, tb):
        return False


class _DummyRecognizer:
    def __init__(self, controller: GoogleSRController):
        self._controller = controller
        self.listen_calls: list[tuple[float | None, float | None]] = []

    def adjust_for_ambient_noise(self, source, duration=0.3):
        return None

    def listen(self, source, timeout=None, phrase_time_limit=None):
        self.listen_calls.append((timeout, phrase_time_limit))
        # End loop right after the first captured chunk.
        self._controller._stop.set()
        return SimpleNamespace(frame_data=b"\x00\x01")


def test_continuous_mode_uses_bounded_chunk_limit(monkeypatch):
    monkeypatch.setattr(
        "modules.voice_recognition.core.google_sr_controller.sr.Microphone",
        _DummyMicrophone,
    )

    controller = GoogleSRController(phrase_time_limit=None)
    dummy_recognizer = _DummyRecognizer(controller)
    controller._recognizer = dummy_recognizer
    controller._start_recognition_thread = lambda *args, **kwargs: None
    controller._listening.set()
    controller._active_listen_session_id = "11111111-1111-4111-8111-111111111111"

    controller._capture_and_recognize()

    assert dummy_recognizer.listen_calls
    timeout, phrase_limit = dummy_recognizer.listen_calls[0]
    assert timeout == 0.3
    assert phrase_limit == controller._continuous_chunk_limit_sec


def test_explicit_phrase_time_limit_is_preserved(monkeypatch):
    monkeypatch.setattr(
        "modules.voice_recognition.core.google_sr_controller.sr.Microphone",
        _DummyMicrophone,
    )

    controller = GoogleSRController(phrase_time_limit=2.5)
    dummy_recognizer = _DummyRecognizer(controller)
    controller._recognizer = dummy_recognizer
    controller._start_recognition_thread = lambda *args, **kwargs: None
    controller._listening.set()
    controller._active_listen_session_id = "22222222-2222-4222-8222-222222222222"

    controller._capture_and_recognize()

    assert dummy_recognizer.listen_calls
    _, phrase_limit = dummy_recognizer.listen_calls[0]
    assert phrase_limit == 2.5
