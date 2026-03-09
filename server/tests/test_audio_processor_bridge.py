from types import SimpleNamespace

from modules.audio_generation.core.audio_processor_bridge import (
    apply_voice_settings_to_config,
    apply_voice_settings_to_provider,
    build_audio_info_from_config,
    build_not_ready_reason,
    build_processor_summary,
    build_provider_name,
    is_processor_ready,
)


def test_is_processor_ready_and_reason() -> None:
    assert not is_processor_ready(False, None)
    assert build_not_ready_reason(False, None) == "AudioProcessor not initialized"
    assert build_not_ready_reason(True, None) == "AudioProcessor provider not initialized"


def test_build_audio_info_from_config_uses_edge_voice_fields() -> None:
    config = SimpleNamespace(
        audio_format="pcm",
        sample_rate=48000,
        channels=1,
        bits_per_sample=16,
        edge_tts_voice_name="en-US-AriaNeural",
        edge_tts_rate="+0%",
        edge_tts_pitch="+0Hz",
        edge_tts_volume="+0%",
    )

    assert build_audio_info_from_config(config) == {
        "format": "pcm",
        "sample_rate": 48000,
        "channels": 1,
        "bits_per_sample": 16,
        "voice_name": "en-US-AriaNeural",
        "rate": "+0%",
        "pitch": "+0Hz",
        "volume": "+0%",
    }


def test_apply_voice_settings_to_config_and_provider() -> None:
    config = SimpleNamespace(
        edge_tts_voice_name="a",
        edge_tts_rate="+0%",
        edge_tts_pitch="+0Hz",
        edge_tts_volume="+0%",
    )
    provider = SimpleNamespace(
        voice_name="a",
        rate="+0%",
        pitch="+0Hz",
        volume="+0%",
    )

    apply_voice_settings_to_config(
        config,
        {"voice_name": "b", "rate": "+20%", "pitch": "+10Hz"},
    )
    apply_voice_settings_to_provider(provider, config)

    assert config.edge_tts_voice_name == "b"
    assert config.edge_tts_rate == "+20%"
    assert config.edge_tts_pitch == "+10Hz"
    assert provider.voice_name == "b"
    assert provider.rate == "+20%"
    assert provider.pitch == "+10Hz"
    assert provider.volume == "+0%"


def test_build_processor_summary_uses_provider_name_and_availability() -> None:
    provider = SimpleNamespace(name="edge_tts", is_available=True)

    summary = build_processor_summary(
        is_initialized=True,
        provider=provider,
        config_valid=True,
        audio_info={"format": "pcm"},
    )

    assert summary["provider_name"] == "edge_tts"
    assert summary["provider_available"] is True
    assert build_provider_name(None) == "none"
