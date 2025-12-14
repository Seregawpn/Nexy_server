"""
AVFoundation Audio Engine Core Module
"""

try:
    from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine
    from modules.audio_avf.core.types import AudioState, AudioFormat, AudioInputResult, AudioDeviceInfo
    __all__ = ['AVFAudioEngine', 'AudioState', 'AudioFormat', 'AudioInputResult', 'AudioDeviceInfo']
except ImportError as e:
    import logging
    logger = logging.getLogger(__name__)
    logger.error(f"❌ [AVF] Не удалось импортировать модули из core: {e}")
    AVFAudioEngine = None
    AudioState = None
    AudioFormat = None
    AudioInputResult = None
    AudioDeviceInfo = None
    __all__ = []
