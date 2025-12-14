"""
SFSpeechRecognizer Module

Native macOS streaming speech recognition.
"""

from modules.speech_recognition_sf.core.sf_speech_recognizer import (
    SFSpeechRecognizerWrapper,
    RecognitionState,
    RecognitionResult,
)

__all__ = [
    "SFSpeechRecognizerWrapper",
    "RecognitionState",
    "RecognitionResult",
]



