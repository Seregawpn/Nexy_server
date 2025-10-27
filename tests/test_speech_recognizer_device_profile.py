import asyncio
from unittest.mock import MagicMock, AsyncMock, patch

import numpy as np
import pytest

from modules.voice_recognition.core.types import RecognitionConfig, RecognitionState
from modules.voice_recognition.core.speech_recognizer import SpeechRecognizer


class DummyMicrophone:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


def build_speech_recognizer(mock_sd, mock_sr, default_device=(3, 5)):
    mock_recognizer = MagicMock()
    mock_sr.Recognizer.return_value = mock_recognizer
    mock_sr.Microphone.return_value = DummyMicrophone()
    mock_recognizer.adjust_for_ambient_noise.return_value = None

    mock_sd.default.device = default_device
    mock_sd.query_hostapis.return_value = [{"name": "CoreAudio", "type": "coreaudio"}]

    config = RecognitionConfig()
    return SpeechRecognizer(config)


@patch("modules.voice_recognition.core.speech_recognizer.sd")
@patch("modules.voice_recognition.core.speech_recognizer.sr")
def test_prepare_input_device_primary(mock_sr, mock_sd):
    input_info = {
        "name": "Test Mic",
        "index": 3,
        "default_samplerate": 44100,
        "max_input_channels": 2,
        "default_low_input_latency": 0.01,
        "default_high_input_latency": 0.02,
        "max_output_channels": 0,
        "hostapi": 0,
    }
    output_info = {
        "name": "Test Speakers",
        "index": 5,
        "default_samplerate": 48000,
        "max_output_channels": 2,
        "default_low_output_latency": 0.02,
        "default_high_output_latency": 0.04,
        "max_input_channels": 0,
        "hostapi": 0,
    }
    device_list = [input_info, output_info]

    def fake_query_devices(device=None, kind=None):
        if kind == "input":
            if device == 3:
                return dict(input_info)
            raise Exception("Input device not available")
        if kind == "output":
            if device == 5:
                return dict(output_info)
            raise Exception("Output device not available")
        return list(device_list)

    mock_sd.query_devices.side_effect = fake_query_devices

    recognizer = build_speech_recognizer(mock_sd, mock_sr, default_device=(3, 5))
    device_id = recognizer._prepare_input_device()

    assert device_id == 3
    assert recognizer.actual_input_rate == 44100
    assert recognizer.actual_input_channels == 2
    assert recognizer.input_device_info["name"] == "Test Mic"
    assert recognizer.output_device_info["name"] == "Test Speakers"
    assert recognizer.host_apis == [{"name": "CoreAudio", "type": "coreaudio"}]

    status = recognizer.get_status()
    assert status["actual_device"]["name"] == "Test Mic"
    assert status["actual_device"]["effective_rate"] == 44100
    assert status["actual_device"]["effective_channels"] == 2
    assert status["output_device"]["name"] == "Test Speakers"


@patch("modules.voice_recognition.core.speech_recognizer.sd")
@patch("modules.voice_recognition.core.speech_recognizer.sr")
def test_prepare_input_device_fallback(mock_sr, mock_sd):
    input_info = {
        "name": "Fallback Mic",
        "index": 0,  # fallback берет первый доступный из списка (индекс 0)
        "default_samplerate": 16000,
        "max_input_channels": 1,
        "default_low_input_latency": 0.03,
        "default_high_input_latency": 0.05,
        "max_output_channels": 0,
        "hostapi": 1,
    }
    output_info = {
        "name": "Fallback Speakers",
        "index": 1,  # fallback берет первый доступный из списка (индекс 1)
        "default_samplerate": 44100,
        "max_output_channels": 2,
        "default_low_output_latency": 0.02,
        "default_high_output_latency": 0.04,
        "max_input_channels": 0,
        "hostapi": 1,
    }
    device_list = [input_info, output_info]

    def fake_query_devices(device=None, kind=None):
        if kind == "input":
            if device in (None, -1):
                raise Exception("Primary input missing")
            if device == 0:
                return dict(input_info)
            raise Exception("Unknown input device")
        if kind == "output":
            if device in (None, -1):
                raise Exception("Primary output missing")
            if device == 1:
                return dict(output_info)
            raise Exception("Unknown output device")
        return list(device_list)

    mock_sd.query_devices.side_effect = fake_query_devices

    recognizer = build_speech_recognizer(mock_sd, mock_sr, default_device=(-1, -1))
    device_id = recognizer._prepare_input_device()

    assert device_id == 0  # fallback возвращает индекс первого доступного устройства
    assert recognizer.actual_input_rate == 16000
    assert recognizer.actual_input_channels == 1
    assert recognizer.input_device_info["name"] == "Fallback Mic"
    assert recognizer.output_device_info["name"] == "Fallback Speakers"


@patch("modules.voice_recognition.core.speech_recognizer.sd")
@patch("modules.voice_recognition.core.speech_recognizer.sr")
def test_signal_stats_updated(mock_sr, mock_sd):
    input_info = {
        "name": "Stat Mic",
        "index": 2,
        "default_samplerate": 32000,
        "max_input_channels": 2,
        "default_low_input_latency": 0.01,
        "default_high_input_latency": 0.02,
        "max_output_channels": 0,
        "hostapi": 0,
    }
    output_info = {
        "name": "Stat Speakers",
        "index": 4,
        "default_samplerate": 48000,
        "max_output_channels": 2,
        "default_low_output_latency": 0.02,
        "default_high_output_latency": 0.04,
        "max_input_channels": 0,
        "hostapi": 0,
    }
    device_list = [input_info, output_info]

    def fake_query_devices(device=None, kind=None):
        if kind == "input":
            if device == 2:
                return dict(input_info)
            raise Exception("Input not present")
        if kind == "output":
            if device == 4:
                return dict(output_info)
            raise Exception("Output not present")
        return list(device_list)

    mock_sd.query_devices.side_effect = fake_query_devices

    recognizer = build_speech_recognizer(mock_sd, mock_sr, default_device=(2, 4))
    recognizer._prepare_input_device()

    # имитируем запись двух каналов по 500 сэмплов
    recognizer.audio_data = [
        np.ones((500, recognizer.actual_input_channels), dtype=np.float32) * 0.25
    ]
    recognizer._notify_event = AsyncMock(return_value=None)
    recognizer._recognize_with_engine = AsyncMock(return_value="test")

    result = asyncio.run(recognizer._recognize_audio())

    assert result.text == "test"
    stats = recognizer.last_audio_stats
    assert stats["samples"] > 0
    assert stats["rms"] > 0
    assert stats["rms_db"] > float("-inf")
    assert stats["raw_rate"] == recognizer.actual_input_rate
    assert stats["raw_channels"] == recognizer.actual_input_channels


@pytest.mark.asyncio
@patch("modules.voice_recognition.core.speech_recognizer.sd")
@patch("modules.voice_recognition.core.speech_recognizer.sr")
async def test_start_listening_fails_when_device_unavailable(mock_sr, mock_sd):
    mock_sr.Recognizer.return_value = MagicMock()
    mock_sr.Microphone.return_value = DummyMicrophone()
    mock_sd.default.device = (-1, -1)
    mock_sd.query_hostapis.return_value = []

    def no_device(*args, **kwargs):
        raise Exception("no device")

    mock_sd.query_devices.side_effect = no_device

    recognizer = SpeechRecognizer(RecognitionConfig())

    result = await recognizer.start_listening()

    assert result is False
    assert recognizer.state == RecognitionState.IDLE
    assert recognizer.prepared_device_id is None
