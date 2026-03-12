#!/bin/bash
set -euo pipefail

az vm run-command invoke \
  --resource-group NexyNewRG \
  --name NexyNew \
  --command-id RunShellScript \
  --scripts '
set -e
export HOME=/home/azureuser

git config --global --add safe.directory /home/azureuser/voice-assistant
cp /home/azureuser/voice-assistant-staging/config.env /tmp/nexy_staging_config.env

cd /home/azureuser/voice-assistant
git checkout -f 34eef453fa5e1db3b11cffe252035c150a513636

rm -rf /home/azureuser/voice-assistant-staging
mkdir -p /home/azureuser/voice-assistant-staging
rsync -a --delete /home/azureuser/voice-assistant/ /home/azureuser/voice-assistant-staging/
cp /tmp/nexy_staging_config.env /home/azureuser/voice-assistant-staging/config.env

python3 - <<'"'"'PYEOF'"'"'
from pathlib import Path

p = Path("/home/azureuser/voice-assistant-staging/modules/update/providers/update_server_provider.py")
text = p.read_text()
needle = """    def _resolve_appcast_channel(self, path: str) -> str:
        if path.endswith("/appcast-beta.xml"):
            return "beta"
        return "stable"
"""
if "_resolve_runtime_channel" not in text:
    insert = needle + """
    def _resolve_runtime_channel(self) -> str:
        \"\"\"Resolve the manifest channel for runtime-owned endpoints such as /health.\"\"\"
        manifests_dir = str(getattr(self.config, "manifests_dir", "") or "")
        downloads_dir = str(getattr(self.config, "downloads_dir", "") or "")
        if "voice-assistant-staging" in manifests_dir or "voice-assistant-staging" in downloads_dir:
            return "beta"
        if int(getattr(self.config, "port", 0) or 0) == 8083:
            return "beta"
        return "stable"
"""
    text = text.replace(needle, insert)

text = text.replace(
    "            # Runtime source of truth: primary manifest.json.\\n            latest_manifest = self.manifest_provider.get_latest_manifest()\\n",
    "            channel = self._resolve_runtime_channel()\\n            latest_manifest = self.manifest_provider.get_manifest_for_channel(channel)\\n",
)
p.write_text(text)
PYEOF

ln -sfn /home/azureuser/voice-assistant-staging/config.env /home/azureuser/config.env
chown -R azureuser:azureuser /home/azureuser/voice-assistant-staging
chown root:azureuser /home/azureuser/voice-assistant-staging/config.env
chmod 640 /home/azureuser/voice-assistant-staging/config.env

python3 - <<'"'"'PYEOF'"'"'
from pathlib import Path

p = Path("/etc/systemd/system/voice-assistant-staging.service")
text = p.read_text()
text = text.replace(
    "ExecStart=/home/azureuser/voice-assistant-staging/venv/bin/python3 server/main.py",
    "ExecStart=/home/azureuser/voice-assistant-staging/venv/bin/python3 main.py",
)
p.write_text(text)
PYEOF

systemctl daemon-reload
systemctl restart voice-assistant-staging
sleep 15
echo "[service]"
systemctl is-active voice-assistant-staging || true
echo "[health]"
curl -fsS http://127.0.0.1:8083/health || true
echo
echo "[updates-health]"
curl -fsS http://127.0.0.1:8083/updates/health || true
'
