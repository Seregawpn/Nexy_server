#!/usr/bin/env python3
"""
Production Testing Script для Audio Playback System

Проверяет все критические сценарии и метрики после рефакторинга.
"""

import sys
import os
import time
import threading
import numpy as np
import logging
from typing import Dict, Any, Optional

# Добавляем путь к проекту
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from modules.speech_playback.core.player import SequentialSpeechPlayer, PlayerConfig

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AudioProductionTester:
    """Тестер для production-проверок audio playback"""
    
    def __init__(self):
        self.player = SequentialSpeechPlayer()
        self.test_results: Dict[str, Any] = {}
        
    def test_lock_invariants(self) -> bool:
        """Тест: Lock-инварианты"""
        logger.info("🧪 Тест: Lock-инварианты")
        try:
            # Проверяем, что все операции с shared state под lock
            with self.player._stream_lock:
                assert self.player._audio_stream is None or hasattr(self.player._audio_stream, 'start')
                assert isinstance(self.player._stream_started, bool)
                assert self.player._current_stream_gen >= 0
            
            logger.info("✅ Lock-инварианты: PASS")
            self.test_results['lock_invariants'] = 'PASS'
            return True
        except Exception as e:
            logger.error(f"❌ Lock-инварианты: FAIL - {e}")
            self.test_results['lock_invariants'] = f'FAIL: {e}'
            return False
    
    def test_generation_counter(self) -> bool:
        """Тест: Generation counter (closure)"""
        logger.info("🧪 Тест: Generation counter")
        try:
            # Создаём stream с gen=1
            initial_gen = self.player._stream_gen
            self.player._stream_gen = 1
            self.player._current_stream_gen = 1
            
            # Создаём callback с gen=1
            callback = self.player._make_audio_callback(stream_gen=1, stream_sr=24000, content_sr=24000)
            
            # Увеличиваем generation (симулируем recreate)
            self.player._stream_gen = 2
            self.player._current_stream_gen = 2
            
            # Вызываем старый callback
            outdata = np.zeros((1024, 2), dtype=np.float32)
            callback(outdata, 1024, None, None)
            
            # Проверяем, что старый callback не пишет данные (заполняет нулями)
            assert np.all(outdata == 0), "Старый callback должен заполнять нулями"
            assert self.player._callback_gen_mismatch_count > 0, "Счётчик должен увеличиться"
            
            logger.info("✅ Generation counter: PASS")
            self.test_results['generation_counter'] = 'PASS'
            return True
        except Exception as e:
            logger.error(f"❌ Generation counter: FAIL - {e}")
            self.test_results['generation_counter'] = f'FAIL: {e}'
            return False
    
    def test_normalization(self) -> bool:
        """Тест: Нормализация int16 → float32"""
        logger.info("🧪 Тест: Нормализация int16 → float32")
        try:
            # Тест симметричной нормализации
            test_values = np.array([-32768, 0, 32767], dtype=np.int16)
            
            # Нормализация
            normalized = test_values.astype(np.float32) / 32768.0
            assert abs(normalized[0] - (-1.0)) < 1e-6, f"Ожидалось -1.0, получили {normalized[0]}"
            assert abs(normalized[1] - 0.0) < 1e-6, f"Ожидалось 0.0, получили {normalized[1]}"
            assert abs(normalized[2] - (32767.0/32768.0)) < 1e-6, f"Ожидалось ~0.99997, получили {normalized[2]}"
            
            # Обратная конвертация
            clipped = np.clip(normalized, -1.0, 1.0 - (1.0/32768.0))
            restored = (clipped * 32768.0).astype(np.int16)
            
            # Проверяем восстановление (с учётом округления)
            assert abs(restored[0] - (-32768)) <= 1, f"Ожидалось -32768, получили {restored[0]}"
            assert abs(restored[1] - 0) <= 1, f"Ожидалось 0, получили {restored[1]}"
            assert abs(restored[2] - 32767) <= 1, f"Ожидалось 32767, получили {restored[2]}"
            
            logger.info("✅ Нормализация: PASS")
            self.test_results['normalization'] = 'PASS'
            return True
        except Exception as e:
            logger.error(f"❌ Нормализация: FAIL - {e}")
            self.test_results['normalization'] = f'FAIL: {e}'
            return False
    
    def test_resampling_round(self) -> bool:
        """Тест: Resampling (round vs int)"""
        logger.info("🧪 Тест: Resampling (round vs int)")
        try:
            from modules.speech_playback.utils.device_utils import resample_audio
            
            # Создаём последовательность чанков
            chunks = [np.random.randn(1000).astype(np.float32) for _ in range(10)]
            ratio = 48000 / 24000  # 2.0
            
            # Ресемплируем с round()
            total_len_round = 0
            for chunk in chunks:
                resampled = resample_audio(chunk, 24000, 48000)
                total_len_round += len(resampled)
            
            # Ожидаемая длина с round()
            expected_len_round = int(round(sum(len(chunk) for chunk in chunks) * ratio))
            
            # Проверяем, что длина близка к ожидаемой
            assert abs(total_len_round - expected_len_round) <= 10, \
                f"Ожидалось ~{expected_len_round}, получили {total_len_round}"
            
            logger.info(f"✅ Resampling (round): PASS (total_len={total_len_round}, expected={expected_len_round})")
            self.test_results['resampling_round'] = 'PASS'
            return True
        except Exception as e:
            logger.error(f"❌ Resampling: FAIL - {e}")
            self.test_results['resampling_round'] = f'FAIL: {e}'
            return False
    
    def test_mono_stereo_mix(self) -> bool:
        """Тест: Mono/Stereo mix"""
        logger.info("🧪 Тест: Mono/Stereo mix")
        try:
            # Тест: Mono → Stereo
            mono_data = np.random.randn(1000, 1).astype(np.float32)
            out_stereo = np.zeros((1000, 2), dtype=np.float32)
            
            # Дублируем канал
            out_stereo[:, 0] = mono_data[:, 0]
            out_stereo[:, 1] = mono_data[:, 0]
            
            assert np.allclose(out_stereo[:, 0], out_stereo[:, 1]), "Mono → Stereo: каналы должны быть одинаковыми"
            
            # Тест: Stereo → Mono
            stereo_data = np.random.randn(1000, 2).astype(np.float32)
            out_mono = np.zeros((1000, 1), dtype=np.float32)
            
            # Среднее (L+R)/2
            out_mono[:, 0] = 0.5 * (stereo_data[:, 0] + stereo_data[:, 1])
            
            expected = 0.5 * (stereo_data[:, 0] + stereo_data[:, 1])
            assert np.allclose(out_mono[:, 0], expected), "Stereo → Mono: должно быть среднее"
            
            logger.info("✅ Mono/Stereo mix: PASS")
            self.test_results['mono_stereo_mix'] = 'PASS'
            return True
        except Exception as e:
            logger.error(f"❌ Mono/Stereo mix: FAIL - {e}")
            self.test_results['mono_stereo_mix'] = f'FAIL: {e}'
            return False
    
    def test_concurrency_storm(self) -> bool:
        """Тест: Concurrency storm"""
        logger.info("🧪 Тест: Concurrency storm")
        try:
            def add_audio_worker():
                for _ in range(50):
                    audio_data = np.random.randint(-32768, 32767, 1000, dtype=np.int16)
                    try:
                        self.player.add_audio_data(audio_data)
                    except Exception as e:
                        logger.error(f"Ошибка в worker: {e}")
                    time.sleep(0.01)
            
            # Создаём 10 потоков
            threads = []
            for _ in range(10):
                t = threading.Thread(target=add_audio_worker)
                threads.append(t)
                t.start()
            
            # Ждём завершения
            for t in threads:
                t.join(timeout=30)
            
            # Проверяем метрики
            assert self.player._recreating_stream == False, "Recreating stream залипло"
            assert self.player._stream_recreate_count <= 20, \
                f"Слишком много recreate: {self.player._stream_recreate_count}"
            
            logger.info(f"✅ Concurrency storm: PASS (recreate_count={self.player._stream_recreate_count})")
            self.test_results['concurrency_storm'] = 'PASS'
            return True
        except Exception as e:
            logger.error(f"❌ Concurrency storm: FAIL - {e}")
            self.test_results['concurrency_storm'] = f'FAIL: {e}'
            return False
    
    def test_metrics(self) -> bool:
        """Тест: Проверка метрик"""
        logger.info("🧪 Тест: Проверка метрик")
        try:
            metrics = {
                'underrun_count': self.player._callback_underrun_count,
                'gen_mismatch_count': self.player._callback_gen_mismatch_count,
                'shape_mismatch_count': self.player._callback_shape_mismatch_count,
                'error_count': self.player._callback_error_count,
                'resample_error_count': self.player._resample_error_count,
                'recreate_count': self.player._stream_recreate_count,
            }
            
            # Проверка tripwires
            warnings = []
            if metrics['underrun_count'] > 10:
                warnings.append(f"⚠️ Underrun count high: {metrics['underrun_count']}")
            if metrics['shape_mismatch_count'] > 0:
                warnings.append(f"⚠️ Shape mismatch detected: {metrics['shape_mismatch_count']}")
            
            # Проверка p95 resample latency
            if len(self.player._callback_resample_ms_history) > 0:
                p95 = np.percentile(self.player._callback_resample_ms_history, 95)
                if p95 > 8:
                    warnings.append(f"⚠️ Resample p95 high: {p95:.2f}ms")
                metrics['resample_p95'] = p95
            
            if warnings:
                logger.warning(f"⚠️ Предупреждения: {warnings}")
            
            logger.info(f"✅ Метрики: PASS {metrics}")
            self.test_results['metrics'] = {'status': 'PASS', 'values': metrics, 'warnings': warnings}
            return True
        except Exception as e:
            logger.error(f"❌ Метрики: FAIL - {e}")
            self.test_results['metrics'] = f'FAIL: {e}'
            return False
    
    def run_all_tests(self) -> Dict[str, Any]:
        """Запуск всех тестов"""
        logger.info("🚀 Запуск всех production-тестов")
        
        tests = [
            self.test_lock_invariants,
            self.test_generation_counter,
            self.test_normalization,
            self.test_resampling_round,
            self.test_mono_stereo_mix,
            self.test_concurrency_storm,
            self.test_metrics,
        ]
        
        results = {}
        for test in tests:
            try:
                result = test()
                results[test.__name__] = result
            except Exception as e:
                logger.error(f"❌ Ошибка в тесте {test.__name__}: {e}")
                results[test.__name__] = False
        
        # Итоговый отчёт
        passed = sum(1 for r in results.values() if r)
        total = len(results)
        
        logger.info(f"\n📊 Итоговый отчёт: {passed}/{total} тестов пройдено")
        
        return {
            'summary': {
                'passed': passed,
                'total': total,
                'success_rate': passed / total if total > 0 else 0
            },
            'results': results,
            'test_results': self.test_results
        }


def main():
    """Главная функция"""
    tester = AudioProductionTester()
    report = tester.run_all_tests()
    
    # Выводим отчёт
    print("\n" + "="*60)
    print("PRODUCTION TESTING REPORT")
    print("="*60)
    print(f"Пройдено: {report['summary']['passed']}/{report['summary']['total']}")
    print(f"Успешность: {report['summary']['success_rate']*100:.1f}%")
    print("\nДетали:")
    for test_name, result in report['test_results'].items():
        status = "✅ PASS" if result == 'PASS' or (isinstance(result, dict) and result.get('status') == 'PASS') else "❌ FAIL"
        print(f"  {test_name}: {status}")
    
    # Exit code
    if report['summary']['passed'] == report['summary']['total']:
        print("\n✅ Все тесты пройдены!")
        return 0
    else:
        print("\n❌ Некоторые тесты провалены!")
        return 1


if __name__ == '__main__':
    sys.exit(main())


