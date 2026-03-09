from typing import Any, Dict, Iterable


def resolve_conversion_mode(*, convert_to_pcm: bool, ffmpeg_available: bool, pydub_available: bool) -> str:
    if not convert_to_pcm:
        return "mp3_passthrough"
    if ffmpeg_available:
        return "ffmpeg_streaming_pcm"
    if pydub_available:
        return "pydub_buffered_pcm"
    return "degraded_mp3_passthrough"


def build_conversion_mode_log_message(mode: str) -> tuple[str, str]:
    if mode == "mp3_passthrough":
        return "info", "EdgeTTS conversion mode: convert_to_pcm=false (streaming MP3 passthrough)"
    if mode == "ffmpeg_streaming_pcm":
        return "info", "EdgeTTS conversion mode: ffmpeg streaming MP3->PCM"
    if mode == "pydub_buffered_pcm":
        return "info", "EdgeTTS conversion mode: pydub MP3->PCM (non-streaming fallback)"
    return "warning", "⚠️ EdgeTTS conversion degraded: no ffmpeg/pydub; streaming MP3 passthrough enabled"


def iter_chunk_bytes(data: bytes, chunk_size: int) -> Iterable[bytes]:
    offset = 0
    while offset < len(data):
        chunk_end = min(offset + chunk_size, len(data))
        yield data[offset:chunk_end]
        offset = chunk_end


def should_retry_process_attempt(*, has_yielded: bool, attempt: int, max_retries: int) -> bool:
    return (not has_yielded) and (attempt < max_retries - 1)


def get_retry_delay_sec(attempt: int) -> float:
    return 0.5 * (2 ** attempt)


def build_edge_status_payload(provider: Any, *, pydub_available: bool, edge_tts_available: bool, conversion_mode: str) -> Dict[str, Any]:
    return {
        "provider_type": "edge_tts",
        "voice_name": provider.voice_name,
        "rate": provider.rate,
        "volume": provider.volume,
        "pitch": provider.pitch,
        "audio_format": provider.audio_format,
        "sample_rate": provider.sample_rate,
        "channels": provider.channels,
        "bits_per_sample": provider.bits_per_sample,
        "is_available": provider.is_available,
        "convert_to_pcm": provider.convert_to_pcm,
        "conversion_mode": conversion_mode,
        "pydub_available": pydub_available,
        "edge_tts_available": edge_tts_available,
    }


def build_edge_metrics_payload(provider: Any) -> Dict[str, Any]:
    return {
        "provider_type": "edge_tts",
        "voice_name": provider.voice_name,
        "audio_format": provider.audio_format,
        "is_available": provider.is_available,
    }


def build_edge_audio_info(provider: Any, *, conversion_mode: str) -> Dict[str, Any]:
    return {
        "format": provider.audio_format,
        "sample_rate": provider.sample_rate,
        "channels": provider.channels,
        "bits_per_sample": provider.bits_per_sample,
        "voice_name": provider.voice_name,
        "rate": provider.rate,
        "volume": provider.volume,
        "pitch": provider.pitch,
        "convert_to_pcm": provider.convert_to_pcm,
        "conversion_mode": conversion_mode,
    }
