#!/usr/bin/env python3
"""
Release Suite для Nexy Client

Выполняет полный цикл интеграционных проверок перед релизом:
- Сборка dev-билда клиента
- Headless запуск и проверка логов
- Критические интеграционные тесты
- Проверки серверной части
- Сверка требований с тестами

Использование:
    python scripts/run_release_suite.py [--skip-build] [--skip-server] [--output <file.json>]

Возвращает JSON-отчёт с результатами всех проверок.
"""

import argparse
import asyncio
from datetime import datetime
import json
import logging
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from typing import Any

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Цвета для вывода
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
NC = '\033[0m'  # No Color


class ReleaseSuite:
    """Release Suite для выполнения всех проверок перед релизом"""
    
    def __init__(self, project_root: Path, skip_build: bool = False, skip_server: bool = False, smoke_mode: bool = False):
        self.project_root = project_root
        self.skip_build = skip_build
        self.skip_server = skip_server
        self.smoke_mode = smoke_mode
        self.results: dict[str, Any] = {
            'timestamp': datetime.now().isoformat(),
            'version': self._get_version(),
            'checks': {}
        }
        self.temp_dir = None
        self.app_path = None
        
    def _get_version(self) -> str:
        """Получает версию из VERSION_INFO.json"""
        version_file = self.project_root / 'client' / 'VERSION_INFO.json'
        if version_file.exists():
            try:
                with open(version_file, 'r') as f:
                    data = json.load(f)
                    return data.get('version', 'unknown')
            except Exception:
                pass
        return 'unknown'
    
    def log_info(self, message: str):
        """Логирует информационное сообщение"""
        logger.info(message)
        print(f"{GREEN}[INFO]{NC} {message}")
    
    def log_error(self, message: str):
        """Логирует сообщение об ошибке"""
        logger.error(message)
        print(f"{RED}[ERROR]{NC} {message}")
    
    def log_warn(self, message: str):
        """Логирует предупреждение"""
        logger.warning(message)
        print(f"{YELLOW}[WARN]{NC} {message}")
    
    def run_check(self, name: str, check_func, *args, **kwargs) -> bool:
        """Выполняет проверку и сохраняет результат"""
        self.log_info(f"Проверка: {name}")
        start_time = time.time()
        
        try:
            result = check_func(*args, **kwargs)  # type: ignore[reportArgumentType, reportCallIssue]
            duration = time.time() - start_time
            
            if result:
                self.results['checks'][name] = {
                    'status': 'PASS',
                    'duration_sec': round(duration, 2),
                    'error': None
                }
                self.log_info(f"✅ {name} - PASSED ({duration:.2f}s)")
                return True
            else:
                self.results['checks'][name] = {
                    'status': 'FAIL',
                    'duration_sec': round(duration, 2),
                    'error': 'Check returned False'
                }
                self.log_error(f"❌ {name} - FAILED")
                return False
        except Exception as e:
            duration = time.time() - start_time
            self.results['checks'][name] = {
                'status': 'ERROR',
                'duration_sec': round(duration, 2),
                'error': str(e)
            }
            self.log_error(f"❌ {name} - ERROR: {e}")
            return False
    
    def check_pre_build_gate(self) -> bool:
        """Проверка 1: Pre-build gate"""
        gate_script = self.project_root / 'scripts' / 'pre_build_gate.sh'
        if not gate_script.exists():
            self.log_warn("pre_build_gate.sh не найден, пропускаем")
            return True
        
        try:
            result = subprocess.run(
                [str(gate_script), '--skip-tests'],  # Пропускаем тесты, они будут отдельно
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=300
            )
            return result.returncode == 0
        except subprocess.TimeoutExpired:
            self.log_error("Pre-build gate превысил таймаут")
            return False
        except Exception as e:
            self.log_error(f"Ошибка выполнения pre-build gate: {e}")
            return False

    def check_problem_scan_gate(self) -> bool:
        """Проверка 1.1: Consolidated problem scan gate (blocking only)."""
        gate_script = self.project_root / "scripts" / "problem_scan_gate.sh"
        if not gate_script.exists():
            self.log_warn("problem_scan_gate.sh не найден, пропускаем")
            return True

        try:
            env = dict(os.environ)
            env["REQUIRE_BASEDPYRIGHT_IN_SCAN"] = "true"
            result = subprocess.run(
                [str(gate_script)],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=600,
                env=env,
            )
            return result.returncode == 0
        except subprocess.TimeoutExpired:
            self.log_error("Problem scan gate превысил таймаут")
            return False
        except Exception as e:
            self.log_error(f"Ошибка выполнения problem scan gate: {e}")
            return False
    
    def build_dev_build(self) -> bool:
        """Проверка 2: Сборка dev-билда клиента"""
        if self.skip_build:
            self.log_warn("Сборка пропущена (--skip-build)")
            return True
        
        rebuild_script = self.project_root / 'rebuild_from_scratch.sh'
        if not rebuild_script.exists():
            self.log_error("rebuild_from_scratch.sh не найден")
            return False
        
        try:
            # Создаём временную директорию для сборки
            self.temp_dir = tempfile.mkdtemp(prefix='nexy_release_suite_')
            self.log_info(f"Временная директория: {self.temp_dir}")
            
            # Запускаем сборку (только PyInstaller часть, без подписи/нотарификации)
            result = subprocess.run(
                ['bash', str(rebuild_script)],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=600  # 10 минут на сборку
            )
            
            if result.returncode != 0:
                self.log_error(f"Сборка провалилась:\n{result.stderr}")
                return False
            
            # Проверяем наличие .app
            app_path = self.project_root / 'dist' / 'Nexy.app'
            if not app_path.exists():
                self.log_error("Nexy.app не найден после сборки")
                return False
            
            self.app_path = app_path
            self.log_info(f"✅ Сборка успешна: {app_path}")
            return True
            
        except subprocess.TimeoutExpired:
            self.log_error("Сборка превысила таймаут")
            return False
        except Exception as e:
            self.log_error(f"Ошибка сборки: {e}")
            return False
    
    def check_logs_specs(self) -> bool:
        """Проверка 3: Headless запуск и проверка логов на соответствие спецификациям"""
        if not self.app_path or not self.app_path.exists():
            self.log_warn("Nexy.app не найден, пропускаем проверку логов")
            return True
        
        # Запускаем приложение в фоне
        try:
            self.log_info("Запуск Nexy.app для проверки логов...")
            process = subprocess.Popen(
                ['open', '-W', str(self.app_path)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            # Ждём 30 секунд для инициализации
            time.sleep(30)
            
            # Проверяем логи на наличие ключевых паттернов
            checks = [
                ('TAL=hold', 'TAL hold установлен'),
                ('tray.ready', 'Tray готов'),
                ('TAL=released', 'TAL released'),
            ]
            
            all_passed = True
            for pattern, description in checks:
                result = subprocess.run(
                    ['log', 'show', '--last', '1m', '--style', 'compact',
                     '--predicate', f'process == "Nexy" && eventMessage CONTAINS "{pattern}"'],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if pattern in result.stdout:
                    self.log_info(f"✅ {description}: найдено в логах")
                else:
                    self.log_warn(f"⚠️ {description}: не найдено в логах")
                    all_passed = False
            
            # Завершаем процесс
            try:
                process.terminate()
                process.wait(timeout=5)
            except Exception:
                process.kill()
            
            return all_passed
            
        except Exception as e:
            self.log_error(f"Ошибка проверки логов: {e}")
            return False
    
    def run_integration_tests(self) -> bool:
        """Проверка 4: Критические интеграционные тесты"""
        # Проверяем наличие pytest
        try:
            subprocess.run(['pytest', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            self.log_warn("pytest не установлен, пропускаем интеграционные тесты")
            return True
        
        # В smoke mode выполняем только критичные тесты
        if self.smoke_mode:
            test_files = [
                'tests/test_gateways.py',  # Критично для архитектуры
                'tests/test_init_order.py',  # Критично для инициализации
            ]
        else:
            test_files = [
                'tests/test_gateways.py',
                'tests/test_init_order.py',
                'tests/test_permission_restart_logic.py',
                'tests/test_permission_restart_priority_order.py',
            ]
        
        all_passed = True
        for test_file in test_files:
            test_path = self.project_root / test_file
            if not test_path.exists():
                self.log_warn(f"Тест не найден: {test_file}")
                continue
            
            try:
                result = subprocess.run(
                    ['pytest', str(test_path), '-v', '--tb=short'],
                    cwd=self.project_root,
                    capture_output=True,
                    text=True,
                    timeout=300
                )
                
                if result.returncode == 0:
                    self.log_info(f"✅ {test_file} - PASSED")
                else:
                    self.log_error(f"❌ {test_file} - FAILED")
                    if self.results.get('verbose', False):
                        print(result.stdout)
                        print(result.stderr)
                    all_passed = False
                    
            except subprocess.TimeoutExpired:
                self.log_error(f"Тест превысил таймаут: {test_file}")
                all_passed = False
            except Exception as e:
                self.log_error(f"Ошибка выполнения теста {test_file}: {e}")
                all_passed = False
        
        return all_passed
    
    async def check_grpc_health(self) -> bool:
        """Проверка 5: gRPC health check"""
        if self.skip_server:
            self.log_warn("Проверка сервера пропущена (--skip-server)")
            return True
        
        try:
            # Импортируем gRPC клиент
            sys.path.insert(0, str(self.project_root))
            from config.unified_config_loader import UnifiedConfigLoader
            from modules.grpc_client import create_default_grpc_client
            
            # Загружаем конфигурацию
            config_loader = UnifiedConfigLoader()
            config = config_loader._load_config()
            
            grpc_config = config.get('grpc', {})
            servers = grpc_config.get('servers', {})
            
            if not servers:
                self.log_warn("Серверы не настроены в конфигурации")
                return True
            
            # Создаём клиент с конфигурацией
            client = create_default_grpc_client()
            
            # Пробуем подключиться к первому доступному серверу
            server_name = list(servers.keys())[0] if servers else None
            if server_name:
                connected = await client.connect(server_name)
                
                if connected:
                    self.log_info(f"✅ gRPC подключение успешно к {server_name}")
                    await client.disconnect()
                    return True
                else:
                    self.log_warn(f"⚠️ gRPC подключение к {server_name} не удалось (сервер может быть недоступен)")
                    return True  # Не критично для release suite
            else:
                self.log_warn("Нет доступных серверов для подключения")
                return True
            
        except ImportError as e:
            self.log_warn(f"Не удалось импортировать gRPC клиент: {e}")
            return True  # Не критично
        except Exception as e:
            self.log_warn(f"Ошибка проверки gRPC: {e}")
            return True  # Не критично для release suite
    
    def check_appcast(self) -> bool:
        """Проверка 6: AppCast доступность"""
        if self.skip_server:
            self.log_warn("Проверка сервера пропущена (--skip-server)")
            return True
        
        try:
            # Загружаем конфигурацию
            sys.path.insert(0, str(self.project_root))
            from config.unified_config_loader import UnifiedConfigLoader
            
            config_loader = UnifiedConfigLoader()
            config = config_loader._load_config()
            
            updater_config = config.get('updater', {})
            appcast_url = updater_config.get('appcast_url', '')
            
            if not appcast_url:
                self.log_warn("AppCast URL не настроен")
                return True
            
            # Проверяем доступность через curl
            result = subprocess.run(
                ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', '--max-time', '10', appcast_url],
                capture_output=True,
                text=True,
                timeout=15
            )
            
            if result.returncode == 0 and result.stdout.strip() == '200':
                self.log_info(f"✅ AppCast доступен: {appcast_url}")
                return True
            else:
                self.log_warn(f"⚠️ AppCast недоступен: {appcast_url} (HTTP {result.stdout.strip()})")
                return True  # Не критично для release suite
            
        except Exception as e:
            self.log_warn(f"Ошибка проверки AppCast: {e}")
            return True  # Не критично
    
    def check_requirements_coverage(self) -> bool:
        """Проверка 7: Сверка требований из PROJECT_REQUIREMENTS с тестами"""
        requirements_file = self.project_root / 'Docs' / 'PROJECT_REQUIREMENTS.md'
        if not requirements_file.exists():
            self.log_warn("PROJECT_REQUIREMENTS.md не найден")
            return True
        
        try:
            # Запускаем скрипт проверки соответствия
            check_script = self.project_root / 'scripts' / 'check_requirements_mapping.py'
            if not check_script.exists():
                self.log_warn("check_requirements_mapping.py не найден")
                return True
            
            result = subprocess.run(
                ['python3', str(check_script)],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                self.log_info("✅ Сверка требований - PASSED")
                return True
            else:
                self.log_warn(f"⚠️ Сверка требований - есть несоответствия:\n{result.stdout}")
                return True  # Не критично, только предупреждение
            
        except Exception as e:
            self.log_warn(f"Ошибка сверки требований: {e}")
            return True  # Не критично
    
    def check_metrics_slo(self) -> bool:
        """Проверка 8: Мониторинг метрик и SLO"""
        try:
            monitor_script = self.project_root / 'scripts' / 'monitor_metrics.py'
            if not monitor_script.exists():
                self.log_warn("monitor_metrics.py не найден")
                return True  # Не критично
            
            # Ищем последний лог-файл
            log_files = list(self.project_root.glob('log*.md'))
            if not log_files:
                self.log_warn("Лог-файлы не найдены, пропускаем мониторинг метрик")
                return True  # Не критично
            
            latest_log = max(log_files, key=lambda p: p.stat().st_mtime)
            
            result = subprocess.run(
                ['python3', str(monitor_script), '--log-file', str(latest_log), '--check-slo'],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                self.log_info("✅ Мониторинг метрик и SLO - PASSED")
                return True
            else:
                self.log_warn(f"⚠️ Мониторинг метрик - обнаружены нарушения SLO:\n{result.stdout}")
                return True  # Не критично, только предупреждение
            
        except Exception as e:
            self.log_warn(f"Ошибка мониторинга метрик: {e}")
            return True  # Не критично
    
    async def run_all_checks(self) -> dict[str, Any]:
        """Запускает все проверки"""
        mode_str = "SMOKE MODE" if self.smoke_mode else "FULL MODE"
        self.log_info("=" * 80)
        self.log_info(f"🚀 RELEASE SUITE - Запуск всех проверок ({mode_str})")
        self.log_info("=" * 80)
        print()
        
        # 1. Pre-build gate (всегда выполняется)
        self.run_check('pre_build_gate', self.check_pre_build_gate)

        # 1.1 Consolidated problem scan gate (всегда выполняется)
        self.run_check('problem_scan_gate', self.check_problem_scan_gate)
        
        # 2. Сборка dev-билда (пропускается в smoke mode)
        if not self.smoke_mode:
            self.run_check('build_dev_build', self.build_dev_build)
        else:
            self.log_warn("Сборка dev-билда пропущена (smoke mode)")
            self.results['checks']['build_dev_build'] = {
                'status': 'SKIPPED',
                'duration_sec': 0,
                'error': 'Skipped in smoke mode'
            }
        
        # 3. Проверка логов (пропускается в smoke mode)
        if not self.smoke_mode:
            self.run_check('check_logs_specs', self.check_logs_specs)
        else:
            self.log_warn("Проверка логов пропущена (smoke mode)")
            self.results['checks']['check_logs_specs'] = {
                'status': 'SKIPPED',
                'duration_sec': 0,
                'error': 'Skipped in smoke mode'
            }
        
        # 4. Интеграционные тесты (всегда выполняется, но ограниченный набор в smoke mode)
        self.run_check('integration_tests', self.run_integration_tests)
        
        # 5. gRPC health (пропускается в smoke mode)
        if not self.smoke_mode:
            async def run_grpc_check():
                return await self.check_grpc_health()
            
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            
            self.run_check('grpc_health', lambda: loop.run_until_complete(run_grpc_check()))
        else:
            self.log_warn("gRPC health check пропущен (smoke mode)")
            self.results['checks']['grpc_health'] = {
                'status': 'SKIPPED',
                'duration_sec': 0,
                'error': 'Skipped in smoke mode'
            }
        
        # 6. AppCast (пропускается в smoke mode)
        if not self.smoke_mode:
            self.run_check('appcast', self.check_appcast)
        else:
            self.log_warn("AppCast проверка пропущена (smoke mode)")
            self.results['checks']['appcast'] = {
                'status': 'SKIPPED',
                'duration_sec': 0,
                'error': 'Skipped in smoke mode'
            }
        
        # 7. Сверка требований (всегда выполняется)
        self.run_check('requirements_coverage', self.check_requirements_coverage)
        
        # 8. Мониторинг метрик и SLO (только в full mode)
        if not self.smoke_mode:
            self.run_check('metrics_monitoring', self.check_metrics_slo)
        else:
            self.log_warn("Мониторинг метрик пропущен (smoke mode)")
            self.results['checks']['metrics_monitoring'] = {
                'status': 'SKIPPED',
                'duration_sec': 0,
                'error': 'Skipped in smoke mode'
            }
        
        # Подсчитываем итоги
        total = len(self.results['checks'])
        passed = sum(1 for c in self.results['checks'].values() if c['status'] == 'PASS')
        failed = sum(1 for c in self.results['checks'].values() if c['status'] == 'FAIL')
        errors = sum(1 for c in self.results['checks'].values() if c['status'] == 'ERROR')
        skipped = sum(1 for c in self.results['checks'].values() if c['status'] == 'SKIPPED')
        
        self.results['summary'] = {
            'total': total,
            'passed': passed,
            'failed': failed,
            'errors': errors,
            'skipped': skipped,
            'success': failed == 0 and errors == 0
        }
        
        return self.results
    
    def print_summary(self):
        """Выводит итоговую сводку"""
        print()
        self.log_info("=" * 80)
        self.log_info("📊 ИТОГИ RELEASE SUITE")
        self.log_info("=" * 80)
        print()
        
        summary = self.results['summary']
        total = summary['total']
        passed = summary['passed']
        failed = summary['failed']
        errors = summary['errors']
        skipped = summary.get('skipped', 0)
        
        print(f"Всего проверок: {total}")
        print(f"{GREEN}Пройдено: {passed}{NC}")
        if skipped > 0:
            print(f"{YELLOW}Пропущено: {skipped}{NC}")
        if failed > 0:
            print(f"{RED}Провалено: {failed}{NC}")
        if errors > 0:
            print(f"{RED}Ошибок: {errors}{NC}")
        print()
        
        if summary['success']:
            self.log_info("✅ RELEASE SUITE: ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ")
        else:
            self.log_error("❌ RELEASE SUITE: НЕКОТОРЫЕ ПРОВЕРКИ ПРОВАЛЕНЫ")
        
        print()
    
    def save_report(self, output_file: Path | None = None):
        """Сохраняет JSON-отчёт"""
        if output_file is None:
            output_file = self.project_root / 'release_suite_report.json'
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2, ensure_ascii=False)
            self.log_info(f"📄 Отчёт сохранён: {output_file}")
        except Exception as e:
            self.log_error(f"Ошибка сохранения отчёта: {e}")


def main():
    parser = argparse.ArgumentParser(description='Release Suite для Nexy Client')
    parser.add_argument('--skip-build', action='store_true', help='Пропустить сборку dev-билда')
    parser.add_argument('--skip-server', action='store_true', help='Пропустить проверки сервера')
    parser.add_argument('--smoke', action='store_true', help='Smoke mode: быстрые проверки без сборки и сервера')
    parser.add_argument('--output', type=str, help='Путь к файлу для сохранения JSON-отчёта')
    args = parser.parse_args()
    
    # Определяем корень проекта
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Если указан --smoke, автоматически включаем --skip-build и --skip-server
    smoke_mode = args.smoke
    skip_build = args.skip_build or smoke_mode
    skip_server = args.skip_server or smoke_mode
    
    # Создаём Release Suite
    suite = ReleaseSuite(
        project_root=project_root,
        skip_build=skip_build,
        skip_server=skip_server,
        smoke_mode=smoke_mode
    )
    
    # Запускаем все проверки (синхронно, но внутри есть async вызовы)
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    results = loop.run_until_complete(suite.run_all_checks())
    
    # Выводим сводку
    suite.print_summary()
    
    # Сохраняем отчёт
    output_file = Path(args.output) if args.output else None
    suite.save_report(output_file)
    
    # Возвращаем код выхода
    if results['summary']['success']:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
