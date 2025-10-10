"""
PyInstaller runtime hook для удаления устаревшего FLAC бинарника
Устанавливает приоритет ffmpeg для speech_recognition
"""

import sys
import os

# Если speech_recognition попытается использовать FLAC - перенаправим на ffmpeg
if hasattr(sys, '_MEIPASS'):
    # PyInstaller bundle mode
    # Удаляем пути к FLAC из поиска
    speech_recog_path = os.path.join(sys._MEIPASS, 'speech_recognition')
    if os.path.exists(speech_recog_path):
        flac_path = os.path.join(speech_recog_path, 'flac-mac')
        if os.path.exists(flac_path):
            try:
                os.remove(flac_path)
            except Exception:
                pass  # Если не удалось удалить - не критично
