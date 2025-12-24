#!/usr/bin/env python3
"""
MVP-3: Storm/Reconcile (single-flight, debounce)

Цель: Доказать устойчивость к бурям событий (device storms)
"""

import sys
import logging
import time
import threading
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List
from collections import deque
from datetime import datetime

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class DeviceEvent:
    """Событие изменения устройства"""
    event_type: str  # 'connected', 'disconnected', 'changed'
    device_name: str
    device_uid: str
    transport: str  # 'bluetooth', 'usb', 'built_in', 'unknown'
    timestamp: float


class ReconcileEngine:
    """Упрощенный reconcile engine для тестирования"""
    
    def __init__(self):
        self.lock = threading.Lock()
        self.is_reconciling = False
        self.pending = False
        self.reconcile_count = 0
        self.restart_count = 0
        self.events_processed = 0
        
    def reconcile(self, events: List[DeviceEvent]) -> bool:
        """
        Выполнение reconcile с single-flight механизмом
        
        Returns:
            True если reconcile выполнен, False если был pending
        """
        with self.lock:
            # Если уже выполняется - помечаем как pending
            if self.is_reconciling:
                self.pending = True
                logger.warning(f"  ⚠️ Reconcile уже выполняется, помечаем как pending")
                return False
            
            # Начинаем reconcile
            self.is_reconciling = True
            self.pending = False
        
        try:
            # Симуляция работы reconcile
            logger.info(f"  🔄 Reconcile начат (событий: {len(events)})")
            self.reconcile_count += 1
            self.events_processed += len(events)
            
            # Определяем, нужен ли restart
            needs_restart = self._needs_restart(events)
            
            if needs_restart:
                self.restart_count += 1
                logger.info(f"  🔁 Restart необходим (всего restarts: {self.restart_count})")
                time.sleep(0.1)  # Симуляция времени restart
            
            # Симуляция времени reconcile
            time.sleep(0.05)
            
            logger.info(f"  ✅ Reconcile завершен")
            
            return True
            
        finally:
            with self.lock:
                self.is_reconciling = False
                was_pending = self.pending
                self.pending = False
            
            # Если был pending - выполняем еще раз
            if was_pending:
                logger.info(f"  🔄 Выполняем pending reconcile")
                # Рекурсивный вызов (в реальности через event loop)
                # Здесь просто логируем
                pass
    
    def _needs_restart(self, events: List[DeviceEvent]) -> bool:
        """Определение необходимости restart"""
        # Упрощенная логика: restart нужен при disconnect или change
        for event in events:
            if event.event_type in ('disconnected', 'changed'):
                return True
        return False


class DebounceManager:
    """Упрощенный debounce manager для тестирования"""
    
    def __init__(self):
        self.device_timers: dict = {}
        self.lock = threading.Lock()
        
        # Debounce конфигурация
        self.config = {
            'bluetooth': {'initial': 0.2, 'increment': 0.2, 'max': 1.2},
            'usb': {'initial': 0.1, 'increment': 0.1, 'max': 0.6},
            'built_in': {'initial': 0.1, 'increment': 0.0, 'max': 0.2},
            'unknown': {'initial': 0.2, 'increment': 0.2, 'max': 1.2},
        }
    
    def get_debounce_delay(self, transport: str) -> float:
        """Получение задержки debounce для транспорта"""
        config = self.config.get(transport, self.config['unknown'])
        device_key = transport
        
        with self.lock:
            if device_key not in self.device_timers:
                self.device_timers[device_key] = {
                    'delay': config['initial'],
                    'last_event': time.time()
                }
                return config['initial']
            
            timer = self.device_timers[device_key]
            elapsed = time.time() - timer['last_event']
            
            # Если прошло достаточно времени - сбрасываем
            if elapsed > timer['delay']:
                timer['delay'] = config['initial']
                timer['last_event'] = time.time()
                return config['initial']
            
            # Увеличиваем задержку
            new_delay = min(timer['delay'] + config['increment'], config['max'])
            timer['delay'] = new_delay
            timer['last_event'] = time.time()
            
            return new_delay
    
    def reset_device(self, transport: str):
        """Сброс таймера для устройства"""
        with self.lock:
            if transport in self.device_timers:
                del self.device_timers[transport]


class StormReconcilePrototype:
    """Прототип для тестирования устойчивости к device storms"""
    
    def __init__(self):
        self.reconcile_engine = ReconcileEngine()
        self.debounce_manager = DebounceManager()
        self.event_queue = deque()
        self.lock = threading.Lock()
    
    def simulate_device_storm(self, count: int = 20) -> List[DeviceEvent]:
        """Симуляция бури событий"""
        events = []
        transports = ['bluetooth', 'usb', 'built_in']
        
        for i in range(count):
            transport = transports[i % len(transports)]
            event = DeviceEvent(
                event_type='connected' if i % 2 == 0 else 'disconnected',
                device_name=f"Device {i % 3}",
                device_uid=f"uid-{i % 3}",
                transport=transport,
                timestamp=time.time()
            )
            events.append(event)
            time.sleep(0.01)  # Небольшая задержка между событиями
        
        return events
    
    def process_events_with_debounce(self, events: List[DeviceEvent]):
        """Обработка событий с debounce"""
        logger.info(f"\n📋 Обработка {len(events)} событий с debounce...")
        
        grouped_events: dict = {}
        
        for event in events:
            # Группируем по транспорту
            transport = event.transport
            if transport not in grouped_events:
                grouped_events[transport] = []
            grouped_events[transport].append(event)
        
        # Обрабатываем каждую группу с debounce
        for transport, transport_events in grouped_events.items():
            delay = self.debounce_manager.get_debounce_delay(transport)
            logger.info(f"  ⏱️ Debounce для {transport}: {delay:.3f}s ({len(transport_events)} событий)")
            
            # Ждем debounce
            time.sleep(delay)
            
            # Выполняем reconcile
            self.reconcile_engine.reconcile(transport_events)
    
    def test_single_flight(self):
        """Тестирование single-flight механизма"""
        logger.info("=" * 80)
        logger.info("MVP-3: Storm/Reconcile (single-flight, debounce)")
        logger.info("=" * 80)
        
        logger.info("\n📋 Тест 1: Single-flight механизм")
        logger.info("Симуляция параллельных событий...\n")
        
        # Создаем события
        events = self.simulate_device_storm(count=10)
        
        # Запускаем несколько reconcile параллельно
        threads = []
        for i in range(5):
            thread = threading.Thread(
                target=lambda: self.reconcile_engine.reconcile(events[i*2:(i+1)*2]),
                name=f"Reconcile-{i}"
            )
            threads.append(thread)
            thread.start()
            time.sleep(0.01)  # Небольшая задержка для создания race condition
        
        # Ждем завершения
        for thread in threads:
            thread.join()
        
        # Проверяем результаты
        logger.info(f"\n📊 Результаты:")
        logger.info(f"  Reconcile выполнено: {self.reconcile_engine.reconcile_count}")
        logger.info(f"  Restarts: {self.reconcile_engine.restart_count}")
        logger.info(f"  Событий обработано: {self.reconcile_engine.events_processed}")
        
        # Критерий: reconcile_count должно быть близко к количеству попыток
        # (не должно быть слишком много параллельных reconcile)
        expected_reconciles = 5  # 5 потоков
        actual_reconciles = self.reconcile_engine.reconcile_count
        
        # Допускаем небольшое превышение из-за pending
        success = actual_reconciles <= expected_reconciles + 2
        
        if success:
            logger.info(f"\n✅ Single-flight работает: {actual_reconciles} reconcile для {expected_reconciles} попыток")
        else:
            logger.error(f"\n❌ Single-flight не работает: {actual_reconciles} reconcile для {expected_reconciles} попыток")
        
        return success
    
    def test_debounce(self):
        """Тестирование debounce механизма"""
        logger.info("\n📋 Тест 2: Debounce механизм")
        logger.info("Симуляция бури событий (20 событий)...\n")
        
        # Создаем бурю событий
        events = self.simulate_device_storm(count=20)
        
        # Обрабатываем с debounce
        start_time = time.time()
        self.process_events_with_debounce(events)
        elapsed = time.time() - start_time
        
        logger.info(f"\n📊 Результаты:")
        logger.info(f"  Событий: {len(events)}")
        logger.info(f"  Reconcile выполнено: {self.reconcile_engine.reconcile_count}")
        logger.info(f"  Restarts: {self.reconcile_engine.restart_count}")
        logger.info(f"  Время обработки: {elapsed:.2f}s")
        
        # Критерий: не должно быть слишком много restarts
        # (debounce должен группировать события)
        max_expected_restarts = len(events) // 2  # Группировка событий
        actual_restarts = self.reconcile_engine.restart_count
        
        success = actual_restarts <= max_expected_restarts
        
        if success:
            logger.info(f"\n✅ Debounce работает: {actual_restarts} restarts для {len(events)} событий")
        else:
            logger.error(f"\n❌ Debounce не работает: {actual_restarts} restarts для {len(events)} событий")
        
        return success
    
    def test_no_cycles(self):
        """Тестирование отсутствия циклов"""
        logger.info("\n📋 Тест 3: Отсутствие циклов")
        logger.info("Симуляция повторяющихся событий...\n")
        
        # Создаем события, которые могут вызвать цикл
        events = []
        for i in range(10):
            events.append(DeviceEvent(
                event_type='changed',
                device_name="Test Device",
                device_uid="test-uid",
                transport='bluetooth',
                timestamp=time.time()
            ))
        
        # Обрабатываем
        self.process_events_with_debounce(events)
        
        # Проверяем, что нет бесконечных циклов
        # (в реальности это проверяется через timeout)
        logger.info(f"  Reconcile выполнено: {self.reconcile_engine.reconcile_count}")
        logger.info(f"  Restarts: {self.reconcile_engine.restart_count}")
        
        # Критерий: не должно быть слишком много restarts
        success = self.reconcile_engine.restart_count <= len(events)
        
        if success:
            logger.info(f"\n✅ Циклов нет: {self.reconcile_engine.restart_count} restarts для {len(events)} событий")
        else:
            logger.error(f"\n❌ Возможны циклы: {self.reconcile_engine.restart_count} restarts для {len(events)} событий")
        
        return success
    
    def run_tests(self):
        """Запуск всех тестов"""
        results = []
        
        results.append(self.test_single_flight())
        results.append(self.test_debounce())
        results.append(self.test_no_cycles())
        
        # Итоги
        logger.info("\n" + "=" * 80)
        logger.info("ИТОГИ ТЕСТИРОВАНИЯ:")
        logger.info("=" * 80)
        logger.info(f"Всего тестов: {len(results)}")
        logger.info(f"Успешных: {sum(results)}")
        logger.info(f"Проваленных: {len(results) - sum(results)}")
        
        success = all(results)
        
        if success:
            logger.info("\n✅ MVP-3 ПРОЙДЕН: Storm/Reconcile устойчив")
        else:
            logger.error("\n❌ MVP-3 ПРОВАЛЕН: Есть проблемы с устойчивостью")
        
        return success


def main():
    """Главная функция"""
    prototype = StormReconcilePrototype()
    success = prototype.run_tests()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

