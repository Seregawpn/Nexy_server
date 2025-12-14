"""
AVFoundation Audio Engine Module

Модуль для работы с аудио через AVFoundation на macOS.
"""

try:
    from modules.audio_avf.core import AVFAudioEngine
    __all__ = ['AVFAudioEngine']
except ImportError as e:
    import logging
    logger = logging.getLogger(__name__)
    logger.error(f"❌ [AVF] Не удалось импортировать AVFAudioEngine: {e}")
    logger.exception("❌ [AVF] Детали ImportError при импорте AVFAudioEngine")
    AVFAudioEngine = None
    __all__ = []
