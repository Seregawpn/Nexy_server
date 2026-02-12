"""
Permission System V2 - Microphone Prober

Probes Microphone permission by attempting to open an audio stream.
"""

from __future__ import annotations

import logging
from typing import Literal

from ..error_matrix import apply_normalization_to_evidence
from ..types import PermissionId, ProbeEvidence, ProbeResult, StepConfig
from .base import BaseProber

logger = logging.getLogger(__name__)


class MicrophoneProber(BaseProber):
    """Prober for Microphone permission."""

    def __init__(self, config: StepConfig):
        super().__init__(config)
        self.permission = PermissionId.MICROPHONE
        self._last_result: bool | None = None

    async def trigger(self) -> None:
        """
        Trigger microphone permission by attempting to open a stream.
        This causes macOS TCC to show the permission dialog.
        """
        try:
            import sounddevice as sd

            # Very short recording attempt to trigger TCC
            logger.debug("[MIC_PROBER] Triggering mic permission via sounddevice")
            sd.rec(frames=1, samplerate=16000, channels=1, blocking=False)
            sd.stop()
        except Exception as e:
            logger.warning("[MIC_PROBER] Trigger failed: %s", e)

    async def probe(self, probe_kind: Literal["light", "heavy"]) -> ProbeResult:
        """Probe microphone capability."""
        ts = self._now()

        # Light probe: use cached
        if probe_kind == "light" and self._last_result is not None:
            ok = self._last_result
            domain, code, msg = None, None, None
        else:
            ok, domain, code, msg = await self._capability_mic_frames(probe_kind)
            self._last_result = ok

        ev = ProbeEvidence(
            frames_received=ok,
            error_domain=domain,
            error_code=code,
            error_message=msg,
        )
        ev = apply_normalization_to_evidence(self.permission, ev)

        return ProbeResult(
            permission=self.permission, timestamp=ts, probe_kind=probe_kind, evidence=ev
        )

    async def _capability_mic_frames(
        self, probe_kind: str
    ) -> tuple[bool | None, str | None, str | None, str | None]:
        """
        Test microphone capability by recording a few frames.
        Returns (frames_received, domain, code, message).
        """
        try:
            import numpy as np
            import sounddevice as sd

            # Quick recording test
            duration = 0.1 if probe_kind == "heavy" else 0.02
            samplerate = 16000

            try:
                recording = sd.rec(
                    int(duration * samplerate),
                    samplerate=samplerate,
                    channels=1,
                    dtype=np.float32,
                    blocking=True,
                )

                if recording is not None and len(recording) > 0:
                    logger.debug("[MIC_PROBER] Got %d frames", len(recording))
                    return True, None, None, None
                else:
                    return False, "sounddevice", None, "no frames received"

            except sd.PortAudioError as e:
                error_msg = str(e).lower()
                if "not authorized" in error_msg or "permission" in error_msg:
                    return False, "PortAudio", "AUTH", str(e)
                return None, "PortAudio", None, str(e)

        except ImportError as e:
            logger.warning("[MIC_PROBER] sounddevice not available: %s", e)
            return None, "import", None, str(e)
        except Exception as e:
            logger.error("[MIC_PROBER] Mic test failed: %s", e)
            return None, "mic", type(e).__name__, str(e)

    def supports_light_probe(self) -> bool:
        return True
