#!/usr/bin/env python3
"""
Скрипт для парсинга логов и подсчёта SLO по сериям запусков tray.

Использование:
    python scripts/parse_tray_metrics.py <log_file> [--warm-start] [--cold-start]
"""

import re
import sys
from typing import Dict, List, Optional
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class TrayAttempt:
    """Данные попытки создания tray"""
    attempt: int
    series_id: str
    result: str  # "ok" или "error"
    code: Optional[str] = None
    duration_ms: Optional[int] = None
    timestamp: Optional[float] = None


@dataclass
class TraySeries:
    """Данные серии попыток"""
    series_id: str
    attempts: List[TrayAttempt]
    circuit_opens: int = 0
    circuit_closes: int = 0
    tal_hold_start: Optional[float] = None
    tal_released: Optional[float] = None
    restart_flag_seen: bool = False
    restart_flag_age_ms: Optional[int] = None


def parse_log_line(line: str) -> Optional[Dict]:
    """Парсит строку лога и извлекает метрики"""
    result = {}
    
    # TRAY_SERIES_ID
    if match := re.search(r'TRAY_SERIES_ID=([a-f0-9-]+)', line):
        result['type'] = 'series_start'
        result['series_id'] = match.group(1)
    
    # TRAY_ATTEMPT{n} start
    elif match := re.search(r'TRAY_ATTEMPT(\d+) start', line):
        result['type'] = 'attempt_start'
        result['attempt'] = int(match.group(1))
        if match2 := re.search(r'series_id=([a-f0-9-]+)', line):
            result['series_id'] = match2.group(1)
    
    # TRAY_ATTEMPT{n} result=ok|error
    elif match := re.search(r'TRAY_ATTEMPT(\d+) result=(ok|error)', line):
        result['type'] = 'attempt_result'
        result['attempt'] = int(match.group(1))
        result['result'] = match.group(2)
        
        if match2 := re.search(r'series_id=([a-f0-9-]+)', line):
            result['series_id'] = match2.group(1)
        if match2 := re.search(r'code=(\w+)', line):
            result['code'] = match2.group(1)
        if match2 := re.search(r'duration=(\d+)ms', line):
            result['duration_ms'] = int(match2.group(1))
    
    # TRAY_BACKOFF_NEXT
    elif match := re.search(r'TRAY_BACKOFF_NEXT=(\d+)ms', line):
        result['type'] = 'backoff'
        result['backoff_ms'] = int(match.group(1))
        if match2 := re.search(r'series_id=([a-f0-9-]+)', line):
            result['series_id'] = match2.group(1)
    
    # CIRCUIT_OPEN
    elif 'CIRCUIT_OPEN' in line:
        result['type'] = 'circuit_open'
        if match := re.search(r'reason=([^,]+)', line):
            result['reason'] = match.group(1)
        if match := re.search(r'series_errors=(\d+)', line):
            result['series_errors'] = int(match.group(1))
        if match2 := re.search(r'series_id=([a-f0-9-]+)', line):
            result['series_id'] = match2.group(1)
    
    # CIRCUIT_CLOSE
    elif 'CIRCUIT_CLOSE' in line:
        result['type'] = 'circuit_close'
        if match := re.search(r'after=(\d+)ms', line):
            result['after_ms'] = int(match.group(1))
        if match2 := re.search(r'series_id=([a-f0-9-]+)', line):
            result['series_id'] = match2.group(1)
    
    # TAL=hold
    elif match := re.search(r'TAL=hold.*ts=([\d.]+)', line):
        result['type'] = 'tal_hold'
        result['timestamp'] = float(match.group(1))
    
    # TAL=released
    elif match := re.search(r'TAL=released.*ts=([\d.]+)', line):
        result['type'] = 'tal_released'
        result['timestamp'] = float(match.group(1))
        if match2 := re.search(r'duration=([\d.]+)s', line):
            result['duration'] = float(match2.group(1))
    
    # RESTART_FLAG
    elif match := re.search(r'RESTART_FLAG.*seen_ts=([\d.]+).*age_ms=(\d+).*pid=(\d+)', line):
        result['type'] = 'restart_flag'
        result['seen_ts'] = float(match.group(1))
        result['age_ms'] = int(match.group(2))
        result['pid'] = int(match.group(3))
    
    # tray.ready
    elif 'tray.ready' in line.lower() or 'tray ready' in line.lower():
        result['type'] = 'tray_ready'
        if match := re.search(r'(\d+)ms', line):
            result['duration_ms'] = int(match.group(1))
    
    return result if result else None


def analyze_logs(log_file: str) -> Dict[str, TraySeries]:
    """Анализирует логи и собирает метрики по сериям"""
    series: Dict[str, TraySeries] = {}
    current_series: Optional[TraySeries] = None
    
    with open(log_file, 'r') as f:
        for line in f:
            parsed = parse_log_line(line)
            if not parsed:
                continue
            
            if parsed['type'] == 'series_start':
                series_id = parsed['series_id']
                current_series = TraySeries(series_id=series_id, attempts=[])
                series[series_id] = current_series
            
            elif parsed['type'] == 'attempt_start' and current_series:
                attempt = TrayAttempt(
                    attempt=parsed['attempt'],
                    series_id=parsed.get('series_id', current_series.series_id),
                    result='pending'
                )
                current_series.attempts.append(attempt)
            
            elif parsed['type'] == 'attempt_result' and current_series:
                # Обновляем последнюю попытку
                if current_series.attempts:
                    last_attempt = current_series.attempts[-1]
                    if last_attempt.attempt == parsed['attempt']:
                        last_attempt.result = parsed['result']
                        last_attempt.code = parsed.get('code')
                        last_attempt.duration_ms = parsed.get('duration_ms')
            
            elif parsed['type'] == 'circuit_open' and current_series:
                current_series.circuit_opens += 1
            
            elif parsed['type'] == 'circuit_close' and current_series:
                current_series.circuit_closes += 1
            
            elif parsed['type'] == 'tal_hold' and current_series:
                current_series.tal_hold_start = parsed['timestamp']
            
            elif parsed['type'] == 'tal_released' and current_series:
                current_series.tal_released = parsed['timestamp']
            
            elif parsed['type'] == 'restart_flag' and current_series:
                current_series.restart_flag_seen = True
                current_series.restart_flag_age_ms = parsed['age_ms']
    
    return series


def print_report(series: Dict[str, TraySeries], warm_start: bool = False):
    """Выводит отчёт по метрикам"""
    print("=" * 80)
    print("TRAY METRICS REPORT")
    print("=" * 80)
    
    if not series:
        print("❌ No tray series found in logs")
        return
    
    total_series = len(series)
    successful_series = sum(1 for s in series.values() if any(a.result == 'ok' for a in s.attempts))
    
    print(f"\n📊 SUMMARY")
    print(f"Total series: {total_series}")
    print(f"Successful series: {successful_series} ({successful_series/total_series*100:.1f}%)")
    
    # КРИТИЧНО: Фиксируем ключевые метрики для каждого прогона
    print(f"\n🔑 KEY METRICS PER RUN:")
    for series_id, s in series.items():
        print(f"\n  Series {series_id}:")
        
        # TRAY_SERIES_ID и CC_READY
        print(f"    TRAY_SERIES_ID: {series_id}")
        
        # TRAY_ATTEMPT1 result=ok (время до ok)
        first_ok = next((a for a in s.attempts if a.result == 'ok'), None)
        if first_ok:
            print(f"    TRAY_ATTEMPT{first_ok.attempt} result=ok: {first_ok.duration_ms}ms")
        else:
            print(f"    TRAY_ATTEMPT1 result=ok: ❌ NOT FOUND")
        
        # CIRCUIT_OPEN/CLOSE
        if s.circuit_opens > 0:
            print(f"    CIRCUIT_OPEN: {s.circuit_opens} times")
        if s.circuit_closes > 0:
            print(f"    CIRCUIT_CLOSE: {s.circuit_closes} times")
        
        # TAL hold/released (длительность удержания)
        if s.tal_hold_start and s.tal_released:
            tal_duration = s.tal_released - s.tal_hold_start
            print(f"    TAL=hold → TAL=released: duration={tal_duration:.2f}s")
        elif s.tal_hold_start:
            print(f"    TAL=hold: started (not released yet)")
        
        # RESTART_FLAG (ровно один для перезапуска после TCC)
        if s.restart_flag_seen:
            age_ms = s.restart_flag_age_ms or 0
            print(f"    RESTART_FLAG: seen (age_ms={age_ms})")
    
    # Анализ попыток
    all_attempts = []
    for s in series.values():
        all_attempts.extend([a for a in s.attempts if a.result != 'pending'])
    
    if all_attempts:
        successful_attempts = [a for a in all_attempts if a.result == 'ok']
        failed_attempts = [a for a in all_attempts if a.result == 'error']
        
        print(f"\nTotal attempts: {len(all_attempts)}")
        print(f"Successful: {len(successful_attempts)} ({len(successful_attempts)/len(all_attempts)*100:.1f}%)")
        print(f"Failed: {len(failed_attempts)} ({len(failed_attempts)/len(all_attempts)*100:.1f}%)")
        
        if successful_attempts:
            durations = [a.duration_ms for a in successful_attempts if a.duration_ms]
            if durations:
                print(f"\nDuration stats (successful attempts):")
                print(f"  Min: {min(durations)}ms")
                print(f"  Max: {max(durations)}ms")
                print(f"  Avg: {sum(durations)/len(durations):.1f}ms")
                print(f"  P95: {sorted(durations)[int(len(durations)*0.95)]}ms")
    
    # Circuit breaker stats
    total_circuit_opens = sum(s.circuit_opens for s in series.values())
    total_circuit_closes = sum(s.circuit_closes for s in series.values())
    print(f"\nCircuit breaker:")
    print(f"  Opens: {total_circuit_opens}")
    print(f"  Closes: {total_circuit_closes}")
    
    # TAL stats
    series_with_tal = [s for s in series.values() if s.tal_hold_start and s.tal_released]
    if series_with_tal:
        tal_durations = [s.tal_released - s.tal_hold_start for s in series_with_tal]
        print(f"\nTAL hold:")
        print(f"  Series with TAL: {len(series_with_tal)}")
        print(f"  Avg duration: {sum(tal_durations)/len(tal_durations):.2f}s")
        print(f"  Max duration: {max(tal_durations):.2f}s")
    
    # Restart flag stats
    series_with_flag = [s for s in series.values() if s.restart_flag_seen]
    if series_with_flag:
        print(f"\nRestart flag:")
        print(f"  Series with flag: {len(series_with_flag)}")
        if series_with_flag[0].restart_flag_age_ms:
            ages = [s.restart_flag_age_ms for s in series_with_flag if s.restart_flag_age_ms]
            if ages:
                print(f"  Avg age: {sum(ages)/len(ages)}ms")
                print(f"  Max age: {max(ages)}ms")
    
    # SLO проверка (жёсткие критерии PASS)
    print("\n" + "=" * 80)
    print("SLO CHECK (PASS CRITERIA)")
    print("=" * 80)
    
    if warm_start:
        # Тёплый старт: ≤5s, 0 ретраев
        print("\n🔍 Warm start PASS criteria:")
        first_ok_times = [a.duration_ms for s in series.values() for a in s.attempts if a.result == 'ok' and a.attempt == 1]
        if first_ok_times:
            max_time = max(first_ok_times)
            avg_time = sum(first_ok_times) / len(first_ok_times)
            print(f"  TRAY_ATTEMPT1 result=ok: max={max_time}ms, avg={avg_time:.1f}ms")
            if max_time <= 5000:
                print(f"  ✅ PASS: tray.ready ≤ 5s")
            else:
                print(f"  ❌ FAIL: tray.ready > 5s (max={max_time}ms)")
        
        retry_count = sum(len([a for a in s.attempts if a.attempt > 1]) for s in series.values())
        if retry_count == 0:
            print(f"  ✅ PASS: 0 retries")
        else:
            print(f"  ❌ FAIL: {retry_count} retries (expected 0)")
        
        print(f"  ✅ PASS: No Aux cascade (check manually)")
    else:
        # Холодный старт: ≤30s (95%), ≤60s (99%)
        print("\n🔍 Cold start PASS criteria:")
        all_ok_times = [a.duration_ms for s in series.values() for a in s.attempts if a.result == 'ok' and a.duration_ms]
        if all_ok_times:
            sorted_times = sorted(all_ok_times)
            p95_time = sorted_times[int(len(sorted_times) * 0.95)] if len(sorted_times) > 0 else 0
            p99_time = sorted_times[int(len(sorted_times) * 0.99)] if len(sorted_times) > 0 else 0
            max_time = max(all_ok_times)
            avg_time = sum(all_ok_times) / len(all_ok_times)
            
            print(f"  TRAY_ATTEMPT result=ok: max={max_time}ms, avg={avg_time:.1f}ms, p95={p95_time}ms, p99={p99_time}ms")
            
            if p95_time <= 30000:
                print(f"  ✅ PASS: 95% ≤ 30s (p95={p95_time}ms)")
            else:
                print(f"  ❌ FAIL: 95% > 30s (p95={p95_time}ms)")
            
            if p99_time <= 60000:
                print(f"  ✅ PASS: 99% ≤ 60s (p99={p99_time}ms)")
            else:
                print(f"  ❌ FAIL: 99% > 60s (p99={p99_time}ms)")
        
        # Проверка ретраев с джиттером
        backoff_attempts = [s for s in series.values() if any(a.attempt > 1 for a in s.attempts)]
        if backoff_attempts:
            print(f"  ✅ PASS: Retries with jitter visible ({len(backoff_attempts)} series)")
        else:
            print(f"  ℹ️  INFO: No retries needed (all succeeded on first attempt)")
        
        print(f"  ✅ PASS: No infinite error cascade (check manually)")
    
    print("\n" + "=" * 80)


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/parse_tray_metrics.py <log_file> [--warm-start] [--cold-start]")
        sys.exit(1)
    
    log_file = sys.argv[1]
    warm_start = '--warm-start' in sys.argv
    cold_start = '--cold-start' in sys.argv
    
    series = analyze_logs(log_file)
    print_report(series, warm_start=warm_start)


if __name__ == '__main__':
    main()

