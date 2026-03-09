from pathlib import Path
from types import SimpleNamespace
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from modules.update.providers.update_server_provider import UpdateServerProvider


class _ManifestProvider:
    def __init__(self) -> None:
        self.channels: list[str] = []

    def get_manifest_for_channel(self, channel: str):
        self.channels.append(channel)
        if channel == "beta":
            return {"version": "2.0.0.43", "build": "2.0.0.43"}
        return {"version": "2.0.0.31", "build": "2.0.0.31"}


class _ArtifactProvider:
    def list_artifacts(self):
        return []


@pytest.mark.asyncio
async def test_health_uses_beta_manifest_for_staging_runtime():
    manifest_provider = _ManifestProvider()
    config = SimpleNamespace(
        beta_enabled=True,
        port=8083,
        manifests_dir="/home/azureuser/voice-assistant-staging/updates/manifests",
        downloads_dir="/home/azureuser/voice-assistant-staging/updates/downloads",
        default_version="2.0.0.41",
        default_build="2.0.0.41",
    )
    provider = UpdateServerProvider(
        config=config,
        manifest_provider=manifest_provider,
        artifact_provider=_ArtifactProvider(),
        version_provider=SimpleNamespace(get_default_version=lambda: "2.0.0.41"),
    )

    response = await provider.health_handler(SimpleNamespace())

    assert manifest_provider.channels == ["beta"]
    assert response.status == 200
    assert response.text
    assert '"latest_version": "2.0.0.43"' in response.text
    assert '"latest_build": "2.0.0.43"' in response.text
