from modules.audio_generation.providers.edge_tts_provider_bridge import (
    build_conversion_mode_log_message,
    build_edge_audio_info,
    get_retry_delay_sec,
    iter_chunk_bytes,
    resolve_conversion_mode,
    should_retry_process_attempt,
)


class _Provider:
    voice_name = "en-US-AriaNeural"
    rate = "+0%"
    volume = "+0%"
    pitch = "+0Hz"
    audio_format = "pcm"
    sample_rate = 48000
    channels = 1
    bits_per_sample = 16
    is_available = True
    convert_to_pcm = True


def test_resolve_conversion_mode_variants() -> None:
    assert resolve_conversion_mode(convert_to_pcm=False, ffmpeg_available=True, pydub_available=True) == "mp3_passthrough"
    assert resolve_conversion_mode(convert_to_pcm=True, ffmpeg_available=True, pydub_available=True) == "ffmpeg_streaming_pcm"
    assert resolve_conversion_mode(convert_to_pcm=True, ffmpeg_available=False, pydub_available=True) == "pydub_buffered_pcm"
    assert resolve_conversion_mode(convert_to_pcm=True, ffmpeg_available=False, pydub_available=False) == "degraded_mp3_passthrough"


def test_iter_chunk_bytes_splits_data() -> None:
    chunks = list(iter_chunk_bytes(b"abcdef", 2))
    assert chunks == [b"ab", b"cd", b"ef"]


def test_should_retry_process_attempt_obeys_has_yielded_and_attempt() -> None:
    assert should_retry_process_attempt(has_yielded=False, attempt=0, max_retries=3) is True
    assert should_retry_process_attempt(has_yielded=True, attempt=0, max_retries=3) is False
    assert should_retry_process_attempt(has_yielded=False, attempt=2, max_retries=3) is False
    assert get_retry_delay_sec(2) == 2.0


def test_build_edge_audio_info_includes_conversion_mode() -> None:
    info = build_edge_audio_info(_Provider(), conversion_mode="ffmpeg_streaming_pcm")
    assert info["conversion_mode"] == "ffmpeg_streaming_pcm"
    assert info["voice_name"] == "en-US-AriaNeural"


def test_build_conversion_mode_log_message_returns_level_and_message() -> None:
    level, message = build_conversion_mode_log_message("ffmpeg_streaming_pcm")
    assert level == "info"
    assert "ffmpeg streaming MP3->PCM" in message
