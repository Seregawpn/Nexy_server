from pathlib import Path

import yaml

from config.unified_config_loader import UnifiedConfigLoader


def _write_config(path: Path, audio_system: dict) -> None:
    payload = {"audio_system": audio_system}
    path.write_text(yaml.safe_dump(payload), encoding="utf-8")


def test_avfoundation_flags_from_config(tmp_path: Path):
    config_path = tmp_path / "unified_config.yaml"
    _write_config(
        config_path,
        {
            "avfoundation_enabled": True,
            "avfoundation_input_monitor_enabled": True,
            "avfoundation_output_enabled": False,
            "avfoundation_route_manager_enabled": True,
            "ks_avfoundation_input_monitor": False,
            "ks_avfoundation_output": False,
            "ks_avfoundation_route_manager": False,
        },
    )

    UnifiedConfigLoader.reset_instance()
    loader = UnifiedConfigLoader(config_path)
    flags = loader.get_avfoundation_flags()

    assert flags["effective"]["master"] is True
    assert flags["effective"]["input_monitor"] is True
    assert flags["effective"]["output"] is False
    assert flags["effective"]["route_manager"] is True
    assert flags["source"]["feature_master"] == "config"


def test_avfoundation_env_overrides_config(tmp_path: Path, monkeypatch):
    config_path = tmp_path / "unified_config.yaml"
    _write_config(
        config_path,
        {
            "avfoundation_enabled": False,
            "avfoundation_input_monitor_enabled": False,
            "avfoundation_output_enabled": False,
            "avfoundation_route_manager_enabled": False,
            "ks_avfoundation_input_monitor": False,
            "ks_avfoundation_output": False,
            "ks_avfoundation_route_manager": False,
        },
    )

    monkeypatch.setenv("NEXY_FEATURE_AVFOUNDATION_AUDIO_V2", "1")
    monkeypatch.setenv("NEXY_FEATURE_AVFOUNDATION_INPUT_MONITOR_V2", "true")
    monkeypatch.setenv("NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2", "1")
    monkeypatch.setenv("NEXY_KS_AVFOUNDATION_OUTPUT_V2", "1")

    UnifiedConfigLoader.reset_instance()
    loader = UnifiedConfigLoader(config_path)
    flags = loader.get_avfoundation_flags()

    assert flags["features"]["master"] is True
    assert flags["features"]["input_monitor"] is True
    assert flags["features"]["output"] is True
    assert flags["kill_switches"]["output"] is True
    assert flags["effective"]["master"] is True
    assert flags["effective"]["input_monitor"] is True
    assert flags["effective"]["output"] is False
    assert flags["source"]["feature_output"] == "env"
    assert flags["source"]["ks_output"] == "env"


def test_avfoundation_master_kill_switch_disables_all(tmp_path: Path, monkeypatch):
    config_path = tmp_path / "unified_config.yaml"
    _write_config(
        config_path,
        {
            "avfoundation_enabled": True,
            "avfoundation_input_monitor_enabled": True,
            "avfoundation_output_enabled": True,
            "avfoundation_route_manager_enabled": True,
            "ks_avfoundation_input_monitor": False,
            "ks_avfoundation_output": False,
            "ks_avfoundation_route_manager": False,
        },
    )

    monkeypatch.setenv("NEXY_KS_AVFOUNDATION_AUDIO_V2", "true")

    UnifiedConfigLoader.reset_instance()
    loader = UnifiedConfigLoader(config_path)
    flags = loader.get_avfoundation_flags()

    assert flags["kill_switches"]["master"] is True
    assert flags["effective"]["master"] is False
    assert flags["effective"]["input_monitor"] is False
    assert flags["effective"]["output"] is False
    assert flags["effective"]["route_manager"] is False
