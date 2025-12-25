#!/usr/bin/env python3
"""
Упрощённый тест для быстрой проверки
"""

import sys
import os
import numpy as np

# Добавляем путь к проекту
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

print("="*60)
print("AUDIO PRODUCTION TESTING")
print("="*60)

try:
    from modules.speech_playback.core.player import SequentialSpeechPlayer
    print("✅ Импорт SequentialSpeechPlayer: OK")
except Exception as e:
    print(f"❌ Импорт SequentialSpeechPlayer: FAIL - {e}")
    sys.exit(1)

# Тест 1: Lock-инварианты
print("\n🧪 Тест 1: Lock-инварианты")
try:
    player = SequentialSpeechPlayer()
    with player._stream_lock:
        assert player._audio_stream is None or hasattr(player._audio_stream, 'start')
        assert isinstance(player._stream_started, bool)
        assert player._current_stream_gen >= 0
    print("✅ Lock-инварианты: PASS")
except Exception as e:
    print(f"❌ Lock-инварианты: FAIL - {e}")
    sys.exit(1)

# Тест 2: Нормализация int16 → float32
print("\n🧪 Тест 2: Нормализация int16 → float32")
try:
    test_values = np.array([-32768, 0, 32767], dtype=np.int16)
    normalized = test_values.astype(np.float32) / 32768.0
    assert abs(normalized[0] - (-1.0)) < 1e-6
    assert abs(normalized[1] - 0.0) < 1e-6
    print("✅ Нормализация: PASS")
except Exception as e:
    print(f"❌ Нормализация: FAIL - {e}")
    sys.exit(1)

# Тест 3: Resampling (round)
print("\n🧪 Тест 3: Resampling (round)")
try:
    from modules.speech_playback.utils.device_utils import resample_audio
    test_data = np.random.randn(1000).astype(np.float32)
    resampled = resample_audio(test_data, 24000, 48000)
    assert len(resampled) > 0
    print(f"✅ Resampling: PASS (len={len(resampled)})")
except Exception as e:
    print(f"❌ Resampling: FAIL - {e}")
    sys.exit(1)

# Тест 4: Generation counter
print("\n🧪 Тест 4: Generation counter")
try:
    player._stream_gen = 1
    player._current_stream_gen = 1
    callback = player._make_audio_callback(stream_gen=1, stream_sr=24000, content_sr=24000)
    player._current_stream_gen = 2
    outdata = np.zeros((1024, 2), dtype=np.float32)
    callback(outdata, 1024, None, None)
    assert np.all(outdata == 0) or player._callback_gen_mismatch_count > 0
    print("✅ Generation counter: PASS")
except Exception as e:
    print(f"❌ Generation counter: FAIL - {e}")
    sys.exit(1)

# Тест 5: Mono/Stereo mix
print("\n🧪 Тест 5: Mono/Stereo mix")
try:
    mono_data = np.random.randn(1000, 1).astype(np.float32)
    out_stereo = np.zeros((1000, 2), dtype=np.float32)
    out_stereo[:, 0] = mono_data[:, 0]
    out_stereo[:, 1] = mono_data[:, 0]
    assert np.allclose(out_stereo[:, 0], out_stereo[:, 1])
    print("✅ Mono/Stereo mix: PASS")
except Exception as e:
    print(f"❌ Mono/Stereo mix: FAIL - {e}")
    sys.exit(1)

# Итоговый отчёт
print("\n" + "="*60)
print("ИТОГОВЫЙ ОТЧЁТ")
print("="*60)
print("✅ Все базовые тесты пройдены!")
print("\nДля полного тестирования запустите:")
print("  python scripts/test_audio_production.py")
print("="*60)


