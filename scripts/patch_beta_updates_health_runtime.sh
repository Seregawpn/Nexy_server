#!/bin/bash
set -euo pipefail

az vm run-command invoke \
  --resource-group NexyNewRG \
  --name NexyNew \
  --command-id RunShellScript \
  --scripts '
python3 - <<'"'"'PYEOF'"'"'
from pathlib import Path

p = Path("/home/azureuser/voice-assistant-staging/modules/update/providers/update_server_provider.py")
text = p.read_text()
old = """    async def health_handler(self, request: web_request.Request) -> web_response.Response:
        \"\"\"Проверка здоровья сервера\"\"\"
        try:
            artifacts = self.artifact_provider.list_artifacts()
            
            # Runtime source of truth: primary manifest.json.
            latest_manifest = self.manifest_provider.get_latest_manifest()
            if latest_manifest and latest_manifest.get(\"version\"):
                latest_version = str(latest_manifest.get(\"version\", \"\"))
                latest_build = str(latest_manifest.get(\"build\", latest_version))
            else:
                latest_version = str(self.config.default_version)
                latest_build = str(self.config.default_build)
                logger.warning(\"⚠️ Манифесты не найдены, версия берется из конфига (fallback)\")
"""
new = """    async def health_handler(self, request: web_request.Request) -> web_response.Response:
        \"\"\"Проверка здоровья сервера\"\"\"
        try:
            artifacts = self.artifact_provider.list_artifacts()

            channel = self._resolve_runtime_channel()
            latest_manifest = self.manifest_provider.get_manifest_for_channel(channel)
            if latest_manifest and latest_manifest.get(\"version\"):
                latest_version = str(latest_manifest.get(\"version\", \"\"))
                latest_build = str(latest_manifest.get(\"build\", latest_version))
            else:
                latest_version = str(self.config.default_version)
                latest_build = str(self.config.default_build)
                logger.warning(
                    \"Manifest for channel %s is missing, using config fallback\",
                    channel,
                )
"""
if old not in text:
    raise SystemExit("TARGET_BLOCK_NOT_FOUND")
text = text.replace(old, new, 1)
p.write_text(text)
print("PATCHED")
PYEOF

systemctl restart voice-assistant-staging
sleep 12
echo "[service]"
systemctl is-active voice-assistant-staging || true
echo "[local-update-health]"
curl -fsS http://127.0.0.1:8083/health || true
'
