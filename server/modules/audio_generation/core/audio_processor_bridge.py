"""Helper-only policy/shaping for AudioProcessor."""

from typing import Any, Dict, Optional


def is_processor_ready(is_initialized: bool, provider: Optional[Any]) -> bool:
    return bool(is_initialized and provider is not None)


def build_not_ready_reason(is_initialized: bool, provider: Optional[Any]) -> str:
    if not is_initialized:
        return "AudioProcessor not initialized"
    if provider is None:
        return "AudioProcessor provider not initialized"
    return ""


def build_provider_name(provider: Optional[Any]) -> str:
    if provider is None:
        return "none"
    return getattr(provider, "name", "edge_tts")


def build_audio_info_from_config(config: Any) -> Dict[str, Any]:
    return {
        "format": config.audio_format,
        "sample_rate": config.sample_rate,
        "channels": config.channels,
        "bits_per_sample": config.bits_per_sample,
        "voice_name": config.edge_tts_voice_name,
        "rate": config.edge_tts_rate,
        "pitch": config.edge_tts_pitch,
        "volume": config.edge_tts_volume,
    }


def build_processor_status(
    *,
    is_initialized: bool,
    config_status: Dict[str, Any],
    provider: Optional[Any],
) -> Dict[str, Any]:
    return {
        "is_initialized": is_initialized,
        "config_status": config_status,
        "provider": provider.get_status() if provider else None,
    }


def build_processor_metrics(
    *,
    is_initialized: bool,
    provider: Optional[Any],
) -> Dict[str, Any]:
    return {
        "is_initialized": is_initialized,
        "provider": provider.get_metrics() if provider else None,
    }


def build_processor_summary(
    *,
    is_initialized: bool,
    provider: Optional[Any],
    config_valid: bool,
    audio_info: Dict[str, Any],
) -> Dict[str, Any]:
    return {
        "is_initialized": is_initialized,
        "provider_name": build_provider_name(provider),
        "provider_available": bool(getattr(provider, "is_available", False)) if provider else False,
        "config_valid": config_valid,
        "audio_info": audio_info,
    }


def apply_voice_settings_to_config(config: Any, voice_settings: Dict[str, Any]) -> None:
    field_map = {
        "voice_name": "edge_tts_voice_name",
        "rate": "edge_tts_rate",
        "pitch": "edge_tts_pitch",
        "volume": "edge_tts_volume",
    }
    for input_key, config_attr in field_map.items():
        if input_key in voice_settings:
            setattr(config, config_attr, voice_settings[input_key])


def apply_voice_settings_to_provider(provider: Optional[Any], config: Any) -> None:
    if provider is None:
        return

    provider_map = {
        "voice_name": config.edge_tts_voice_name,
        "rate": config.edge_tts_rate,
        "pitch": config.edge_tts_pitch,
        "volume": config.edge_tts_volume,
    }
    for provider_attr, value in provider_map.items():
        if hasattr(provider, provider_attr):
            setattr(provider, provider_attr, value)

