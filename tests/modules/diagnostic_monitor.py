#!/usr/bin/env python3
"""
Система мониторинга диагностических тестов
"""

import asyncio
import logging
import sys
import os
import time
import json
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from pathlib import Path

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

logger = logging.getLogger(__name__)

class DiagnosticMonitor:
    """Система мониторинга диагностических тестов"""
    
    def __init__(self, config_path: str = "diagnostic_monitor_config.json"):
        self.config_path = config_path
        self.config = self._load_config()
        self.monitoring_active = False
        self.last_results = {}
        self.alert_thresholds = {
            'success_rate': 80.0,  # Минимальный процент успешности
            'failed_tests': 10,    # Максимальное количество неудачных тестов
            'response_time': 300   # Максимальное время выполнения в секундах
        }
    
    def _load_config(self) -> Dict[str, Any]:
        """Загрузка конфигурации мониторинга"""
        default_config = {
            'monitoring_interval': 300,  # 5 минут
            'alert_email': None,
            'alert_webhook': None,
            'log_file': 'diagnostic_monitor.log',
            'history_file': 'diagnostic_history.json',
            'enabled_modules': [
                'audio_device_manager',
                'speech_recognizer',
                'grpc_client',
                'input_processing',
                'speech_playback',
                'permissions',
                'network_manager',
                'mode_management',
                'audio_device_integration',
                'unified_config'
            ]
        }
        
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r') as f:
                    config = json.load(f)
                # Объединяем с конфигурацией по умолчанию
                default_config.update(config)
            except Exception as e:
                logger.warning(f"Не удалось загрузить конфигурацию: {e}")
        
        return default_config
    
    async def start_monitoring(self):
        """Запуск мониторинга"""
        logger.info("🚀 Запуск мониторинга диагностических тестов...")
        self.monitoring_active = True
        
        while self.monitoring_active:
            try:
                # Запускаем диагностические тесты
                results = await self._run_diagnostics()
                
                # Анализируем результаты
                analysis = self._analyze_results(results)
                
                # Сохраняем историю
                await self._save_history(results, analysis)
                
                # Проверяем на нарушения
                violations = self._check_violations(analysis)
                
                if violations:
                    await self._send_alerts(violations, analysis)
                
                # Ждем до следующего цикла
                await asyncio.sleep(self.config['monitoring_interval'])
                
            except Exception as e:
                logger.error(f"Ошибка в цикле мониторинга: {e}")
                await asyncio.sleep(60)  # Ждем минуту при ошибке
    
    async def stop_monitoring(self):
        """Остановка мониторинга"""
        logger.info("🛑 Остановка мониторинга...")
        self.monitoring_active = False
    
    async def _run_diagnostics(self) -> Dict[str, Any]:
        """Запуск диагностических тестов"""
        logger.info("🔍 Запуск диагностических тестов...")
        
        # Импортируем и запускаем главный диагностический скрипт
        try:
            from run_diagnostics import MasterDiagnostic
            
            diagnostic = MasterDiagnostic()
            results = await diagnostic.run_all_diagnostics()
            
            return results
            
        except Exception as e:
            logger.error(f"Ошибка запуска диагностики: {e}")
            return {"error": str(e)}
    
    def _analyze_results(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Анализ результатов диагностики"""
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'total_tests': 0,
            'successful_tests': 0,
            'failed_tests': 0,
            'success_rate': 0.0,
            'execution_time': 0,
            'module_results': {},
            'critical_issues': [],
            'warnings': []
        }
        
        if 'error' in results:
            analysis['critical_issues'].append(f"Критическая ошибка: {results['error']}")
            return analysis
        
        # Анализируем результаты по категориям
        for category, category_results in results.get('categories', {}).items():
            if isinstance(category_results, dict) and 'total_tests' in category_results:
                total = category_results['total_tests']
                successful = category_results.get('successful_tests', 0)
                failed = total - successful
                success_rate = (successful / total * 100) if total > 0 else 0
                
                analysis['total_tests'] += total
                analysis['successful_tests'] += successful
                analysis['failed_tests'] += failed
                
                analysis['module_results'][category] = {
                    'total_tests': total,
                    'successful_tests': successful,
                    'failed_tests': failed,
                    'success_rate': success_rate
                }
                
                # Проверяем на критические проблемы
                if success_rate < 50:
                    analysis['critical_issues'].append(f"Критически низкая успешность {category}: {success_rate:.1f}%")
                elif success_rate < 80:
                    analysis['warnings'].append(f"Низкая успешность {category}: {success_rate:.1f}%")
        
        # Вычисляем общую успешность
        if analysis['total_tests'] > 0:
            analysis['success_rate'] = (analysis['successful_tests'] / analysis['total_tests'] * 100)
        
        return analysis
    
    def _check_violations(self, analysis: Dict[str, Any]) -> List[str]:
        """Проверка нарушений пороговых значений"""
        violations = []
        
        # Проверяем общую успешность
        if analysis['success_rate'] < self.alert_thresholds['success_rate']:
            violations.append(f"Общая успешность ниже порога: {analysis['success_rate']:.1f}% < {self.alert_thresholds['success_rate']}%")
        
        # Проверяем количество неудачных тестов
        if analysis['failed_tests'] > self.alert_thresholds['failed_tests']:
            violations.append(f"Слишком много неудачных тестов: {analysis['failed_tests']} > {self.alert_thresholds['failed_tests']}")
        
        # Проверяем время выполнения
        if analysis['execution_time'] > self.alert_thresholds['response_time']:
            violations.append(f"Время выполнения превышено: {analysis['execution_time']}s > {self.alert_thresholds['response_time']}s")
        
        return violations
    
    async def _save_history(self, results: Dict[str, Any], analysis: Dict[str, Any]):
        """Сохранение истории результатов"""
        history_file = self.config['history_file']
        
        try:
            # Загружаем существующую историю
            history = []
            if os.path.exists(history_file):
                with open(history_file, 'r') as f:
                    history = json.load(f)
            
            # Добавляем новые результаты
            history.append({
                'timestamp': analysis['timestamp'],
                'results': results,
                'analysis': analysis
            })
            
            # Ограничиваем историю последними 100 записями
            if len(history) > 100:
                history = history[-100:]
            
            # Сохраняем историю
            with open(history_file, 'w') as f:
                json.dump(history, f, indent=2)
            
            logger.info(f"📊 История сохранена: {len(history)} записей")
            
        except Exception as e:
            logger.error(f"Ошибка сохранения истории: {e}")
    
    async def _send_alerts(self, violations: List[str], analysis: Dict[str, Any]):
        """Отправка уведомлений о нарушениях"""
        logger.warning(f"🚨 Обнаружены нарушения: {len(violations)}")
        
        for violation in violations:
            logger.warning(f"   ⚠️ {violation}")
        
        # Отправляем email уведомления
        if self.config.get('alert_email'):
            await self._send_email_alert(violations, analysis)
        
        # Отправляем webhook уведомления
        if self.config.get('alert_webhook'):
            await self._send_webhook_alert(violations, analysis)
    
    async def _send_email_alert(self, violations: List[str], analysis: Dict[str, Any]):
        """Отправка email уведомления"""
        # Здесь должна быть логика отправки email
        logger.info("📧 Email уведомление отправлено")
    
    async def _send_webhook_alert(self, violations: List[str], analysis: Dict[str, Any]):
        """Отправка webhook уведомления"""
        # Здесь должна быть логика отправки webhook
        logger.info("🔗 Webhook уведомление отправлено")
    
    def get_status(self) -> Dict[str, Any]:
        """Получение статуса мониторинга"""
        return {
            'monitoring_active': self.monitoring_active,
            'last_check': self.last_results.get('timestamp'),
            'config': self.config,
            'alert_thresholds': self.alert_thresholds
        }
    
    def get_history(self, hours: int = 24) -> List[Dict[str, Any]]:
        """Получение истории за указанное количество часов"""
        history_file = self.config['history_file']
        
        if not os.path.exists(history_file):
            return []
        
        try:
            with open(history_file, 'r') as f:
                history = json.load(f)
            
            # Фильтруем по времени
            cutoff_time = datetime.now() - timedelta(hours=hours)
            filtered_history = []
            
            for entry in history:
                entry_time = datetime.fromisoformat(entry['timestamp'])
                if entry_time >= cutoff_time:
                    filtered_history.append(entry)
            
            return filtered_history
            
        except Exception as e:
            logger.error(f"Ошибка загрузки истории: {e}")
            return []

async def main():
    """Основная функция"""
    logger.info("🚀 Запуск системы мониторинга диагностических тестов...")
    
    monitor = DiagnosticMonitor()
    
    try:
        # Запускаем мониторинг
        await monitor.start_monitoring()
    except KeyboardInterrupt:
        logger.info("🛑 Получен сигнал остановки...")
        await monitor.stop_monitoring()
    except Exception as e:
        logger.error(f"❌ Критическая ошибка мониторинга: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
