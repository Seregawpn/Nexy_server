"""
Audio gateways for microphone activation decisions.
"""
from __future__ import annotations

import logging
from integration.core.selectors import Snapshot
from integration.core.gateways.types import Decision
from integration.core.state_manager import AppMode

logger = logging.getLogger(__name__)


def decide_allow_shortcut_during_processing(snapshot: Snapshot, source: str) -> Decision:
    """
    Решает, разрешена ли активация через Shortcut во время PROCESSING.
    
    Правило:
    - Разрешаем активацию через Shortcut ВСЕГДА (для прерывания воспроизведения)
    - Блокируем только автоматическую активацию (когда source != "keyboard")
    
    Args:
        snapshot: Снимок состояния системы
        source: Источник активации ("keyboard" для Shortcut, другие для автоматической)
    
    Returns:
        Decision.START - разрешить активацию
        Decision.ABORT - заблокировать активацию
    """
    if snapshot.app_mode == AppMode.PROCESSING:
        if source == "keyboard":
            # ✅ Разрешаем активацию через Shortcut для прерывания воспроизведения
            logger.info("✅ [AUDIO_GATEWAY] Разрешаем активацию через Shortcut во время PROCESSING (прерывание воспроизведения)")
            return Decision.START
        else:
            # ❌ Блокируем автоматическую активацию во время PROCESSING
            logger.warning("🔒 [AUDIO_GATEWAY] Блокируем автоматическую активацию во время PROCESSING")
            return Decision.ABORT
    
    # В других режимах разрешаем активацию
    return Decision.START

