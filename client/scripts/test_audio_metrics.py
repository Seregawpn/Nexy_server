#!/usr/bin/env python3
"""
Скрипт для проверки метрик audio playback после длительного тестирования
"""

import sys
import os
import json
import numpy as np
import logging
from typing import Dict, Any

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from modules.speech_playback.core.player import SequentialSpeechPlayer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def check_audio_metrics(player: SequentialSpeechPlayer) -> Dict[str, Any]:
    """Проверка метрик audio playback"""
    metrics = {
        'underrun_count': player._callback_underrun_count,
        'gen_mismatch_count': player._callback_gen_mismatch_count,
        'shape_mismatch_count': player._callback_shape_mismatch_count,
        'error_count': player._callback_error_count,
        'resample_error_count': player._resample_error_count,
        'recreate_count': player._stream_recreate_count,
        'device_query_failure_count': player._device_query_failure_count,
        'stream_open_fail_count': player._stream_open_fail_count,
    }
    
    # Проверка tripwires
    warnings = []
    errors = []
    
    if metrics['underrun_count'] > 10:
        warnings.append(f"⚠️ Underrun count high: {metrics['underrun_count']}")
    if metrics['underrun_count'] > 50:
        errors.append(f"❌ Underrun count critical: {metrics['underrun_count']}")
    
    if metrics['shape_mismatch_count'] > 0:
        warnings.append(f"⚠️ Shape mismatch detected: {metrics['shape_mismatch_count']}")
    if metrics['shape_mismatch_count'] > 10:
        errors.append(f"❌ Shape mismatch critical: {metrics['shape_mismatch_count']}")
    
    # Проверка p95 resample latency
    if len(player._callback_resample_ms_history) > 0:
        p95 = np.percentile(player._callback_resample_ms_history, 95)
        p50 = np.percentile(player._callback_resample_ms_history, 50)
        p99 = np.percentile(player._callback_resample_ms_history, 99)
        metrics['resample_p50'] = p50
        metrics['resample_p95'] = p95
        metrics['resample_p99'] = p99
        
        if p95 > 8:
            warnings.append(f"⚠️ Resample p95 high: {p95:.2f}ms")
        if p95 > 15:
            errors.append(f"❌ Resample p95 critical: {p95:.2f}ms")
    else:
        metrics['resample_p50'] = None
        metrics['resample_p95'] = None
        metrics['resample_p99'] = None
    
    # Проверка recreate latency
    if len(player._recreate_total_ms_history) > 0:
        p95 = np.percentile(player._recreate_total_ms_history, 95)
        metrics['recreate_p95'] = p95
        
        if p95 > 5000:
            warnings.append(f"⚠️ Recreate p95 high: {p95:.1f}ms")
        if p95 > 10000:
            errors.append(f"❌ Recreate p95 critical: {p95:.1f}ms")
    else:
        metrics['recreate_p95'] = None
    
    return {
        'metrics': metrics,
        'warnings': warnings,
        'errors': errors,
        'all_clear': len(errors) == 0
    }


def main():
    """Главная функция"""
    player = SequentialSpeechPlayer()
    
    # Здесь можно добавить логику для получения player из работающего приложения
    # или создать тестовый player
    
    report = check_audio_metrics(player)
    
    print(json.dumps(report, indent=2, default=str))
    
    if not report['all_clear']:
        print("\n❌ Обнаружены критические ошибки!")
        return 1
    elif report['warnings']:
        print("\n⚠️ Обнаружены предупреждения")
        return 0
    else:
        print("\n✅ Все метрики в норме!")
        return 0


if __name__ == '__main__':
    sys.exit(main())


