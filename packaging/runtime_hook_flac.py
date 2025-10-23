"""
PyInstaller runtime hook для замены устаревшего FLAC бинарника на новый ARM64
Заменяет старый Intel x86_64 flac-mac на новый ARM64 бинарник
"""

import sys
import os
import shutil

# Заменяем старый FLAC бинарник на новый ARM64
if hasattr(sys, '_MEIPASS'):
    # PyInstaller bundle mode
    speech_recog_path = os.path.join(sys._MEIPASS, 'speech_recognition')
    if os.path.exists(speech_recog_path):
        old_flac_path = os.path.join(speech_recog_path, 'flac-mac')
        new_flac_path = '/Users/sergiyzasorin/Downloads/flac-1.5.0/src/flac/flac'
        
        if os.path.exists(old_flac_path) and os.path.exists(new_flac_path):
            try:
                # Удаляем старый файл
                os.remove(old_flac_path)
                # Копируем новый ARM64 бинарник
                shutil.copy2(new_flac_path, old_flac_path)
                print(f"✅ Заменили старый FLAC на новый ARM64 бинарник")
            except Exception as e:
                print(f"⚠️ Не удалось заменить FLAC: {e}")
                # Если не удалось заменить - удаляем старый
                try:
                    os.remove(old_flac_path)
                except Exception:
                    pass
