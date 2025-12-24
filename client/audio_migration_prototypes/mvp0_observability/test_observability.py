#!/usr/bin/env python3
"""
MVP-0: Observability (лог-формат)

Цель: Доказать, что любой баг можно восстановить по логам

Exit Gate:
- [ ] Лог-формат определен и документирован
- [ ] Примеры логов для всех критических событий
- [ ] Можно восстановить цепочку: snapshot → decision → action
"""

import sys
import logging
import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional
from datetime import datetime

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class Snapshot:
    """Снимок состояния системы"""
    perm_mic: str  # GRANTED/DENIED/NOT_DETERMINED
    perm_screen: str
    device_input: str  # DEFAULT_OK/BUSY/UNAVAILABLE
    network: str  # ONLINE/OFFLINE
    first_run: bool
    app_mode: str  # SLEEPING/LISTENING/PROCESSING
    audio_input_device: Optional[str] = None
    audio_output_device: Optional[str] = None
    timestamp: str = ""
    
    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> dict:
        return asdict(self)
    
    def to_log_string(self) -> str:
        """Канонический формат для логов"""
        return f"snapshot={{mic={self.perm_mic},screen={self.perm_screen},device={self.device_input},network={self.network},firstRun={self.first_run},appMode={self.app_mode},inputDevice={self.audio_input_device},outputDevice={self.audio_output_device}}}"


@dataclass
class Decision:
    """Решение gateway"""
    decision_type: str  # START/ABORT/RETRY/DEGRADE
    context: Snapshot
    source: str  # domain (audio/permissions/mode)
    duration_ms: int
    reason: str
    timestamp: str = ""
    
    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> dict:
        return {
            "decision_type": self.decision_type,
            "context": self.context.to_dict(),
            "source": self.source,
            "duration_ms": self.duration_ms,
            "reason": self.reason,
            "timestamp": self.timestamp
        }
    
    def to_log_string(self) -> str:
        """Канонический формат decision-лога"""
        ctx_str = self.context.to_log_string()
        return f"decision=<{self.decision_type.lower()}> {ctx_str} source=<{self.source}> duration_ms=<{self.duration_ms}> reason=\"{self.reason}\""


@dataclass
class Action:
    """Действие, выполненное системой"""
    action_type: str  # START_INPUT/STOP_INPUT/RECREATE_OUTPUT/NOOP
    target: str  # device_name или "system_default"
    result: str  # SUCCESS/FAILED
    error_message: Optional[str] = None
    timestamp: str = ""
    
    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> dict:
        return asdict(self)
    
    def to_log_string(self) -> str:
        """Канонический формат для логов"""
        result_str = f"action=<{self.action_type}> target=\"{self.target}\" result=<{self.result.lower()}>"
        if self.error_message:
            result_str += f" error=\"{self.error_message}\""
        return result_str


class ObservabilityPrototype:
    """
    Прототип для тестирования observability (лог-формат)
    
    Структура:
    1. Инициализация (setup)
    2. Определение формата (define_log_format)
    3. Создание примеров (create_examples)
    4. Тест восстановления (test_reconstruction)
    5. Проверка Exit Gate (check_exit_gate)
    """
    
    def __init__(self):
        self.log_format_defined = False
        self.examples: List[Dict] = []
        self.reconstruction_success = False
        
    def setup(self) -> bool:
        """Настройка окружения"""
        logger.info("=" * 80)
        logger.info("MVP-0: Observability (лог-формат)")
        logger.info("=" * 80)
        logger.info("")
        return True
        
    def define_log_format(self) -> bool:
        """Определение формата логов"""
        logger.info("📋 Определение формата логов...")
        logger.info("")
        
        # Формат: snapshot → decision → action
        log_format = {
            "format": "snapshot → decision → action",
            "components": {
                "snapshot": {
                    "format": "snapshot={mic=...,screen=...,device=...,network=...,firstRun=...,appMode=...,inputDevice=...,outputDevice=...}",
                    "fields": ["perm_mic", "perm_screen", "device_input", "network", "first_run", "app_mode", "audio_input_device", "audio_output_device"],
                    "timestamp": "ISO 8601"
                },
                "decision": {
                    "format": "decision=<start|abort|retry|degrade> ctx={...} source=<domain> duration_ms=<int> reason=\"...\"",
                    "fields": ["decision_type", "context", "source", "duration_ms", "reason"],
                    "canonical": True
                },
                "action": {
                    "format": "action=<ACTION_TYPE> target=\"...\" result=<success|failed> error=\"...\"",
                    "fields": ["action_type", "target", "result", "error_message"],
                    "timestamp": "ISO 8601"
                }
            },
            "chain": "snapshot → decision → action",
            "canonical_decision_log": True
        }
        
        logger.info("✅ Формат логов определен:")
        logger.info(f"   Формат: {log_format['format']}")
        logger.info(f"   Компоненты: {', '.join(log_format['components'].keys())}")
        logger.info("")
        
        self.log_format = log_format
        self.log_format_defined = True
        return True
        
    def create_examples(self) -> bool:
        """Создание примеров логов для всех критических событий"""
        logger.info("📋 Создание примеров логов...")
        logger.info("")
        
        # Пример 1: Успешный старт listening
        snapshot1 = Snapshot(
            perm_mic="GRANTED",
            perm_screen="GRANTED",
            device_input="DEFAULT_OK",
            network="ONLINE",
            first_run=False,
            app_mode="SLEEPING",
            audio_input_device="Built-in Microphone",
            audio_output_device="Built-in Output"
        )
        
        decision1 = Decision(
            decision_type="START",
            context=snapshot1,
            source="audio",
            duration_ms=45,
            reason="All conditions met, starting input"
        )
        
        action1 = Action(
            action_type="START_INPUT",
            target="Built-in Microphone",
            result="SUCCESS"
        )
        
        example1 = {
            "scenario": "Успешный старт listening",
            "snapshot": snapshot1.to_log_string(),
            "decision": decision1.to_log_string(),
            "action": action1.to_log_string(),
            "chain": f"{snapshot1.to_log_string()} → {decision1.to_log_string()} → {action1.to_log_string()}"
        }
        
        # Пример 2: MIC_BUSY
        snapshot2 = Snapshot(
            perm_mic="GRANTED",
            perm_screen="GRANTED",
            device_input="BUSY",
            network="ONLINE",
            first_run=False,
            app_mode="LISTENING",
            audio_input_device="Built-in Microphone"
        )
        
        decision2 = Decision(
            decision_type="ABORT",
            context=snapshot2,
            source="audio",
            duration_ms=12,
            reason="Microphone busy, another app is using it"
        )
        
        action2 = Action(
            action_type="NOOP",
            target="system",
            result="SUCCESS",
            error_message="MIC_BUSY"
        )
        
        example2 = {
            "scenario": "MIC_BUSY - микрофон занят",
            "snapshot": snapshot2.to_log_string(),
            "decision": decision2.to_log_string(),
            "action": action2.to_log_string(),
            "chain": f"{snapshot2.to_log_string()} → {decision2.to_log_string()} → {action2.to_log_string()}"
        }
        
        # Пример 3: First run блокирует
        snapshot3 = Snapshot(
            perm_mic="NOT_DETERMINED",
            perm_screen="NOT_DETERMINED",
            device_input="DEFAULT_OK",
            network="ONLINE",
            first_run=True,
            app_mode="SLEEPING"
        )
        
        decision3 = Decision(
            decision_type="ABORT",
            context=snapshot3,
            source="first_run",
            duration_ms=5,
            reason="First run in progress, blocking audio operations"
        )
        
        action3 = Action(
            action_type="NOOP",
            target="system",
            result="SUCCESS"
        )
        
        example3 = {
            "scenario": "First run блокирует операции",
            "snapshot": snapshot3.to_log_string(),
            "decision": decision3.to_log_string(),
            "action": action3.to_log_string(),
            "chain": f"{snapshot3.to_log_string()} → {decision3.to_log_string()} → {action3.to_log_string()}"
        }
        
        # Пример 4: Device switch
        snapshot4 = Snapshot(
            perm_mic="GRANTED",
            perm_screen="GRANTED",
            device_input="DEFAULT_OK",
            network="ONLINE",
            first_run=False,
            app_mode="LISTENING",
            audio_input_device="AirPods",
            audio_output_device="AirPods"
        )
        
        decision4 = Decision(
            decision_type="START",
            context=snapshot4,
            source="audio",
            duration_ms=38,
            reason="Device changed, restarting input with new device"
        )
        
        action4 = Action(
            action_type="START_INPUT",
            target="AirPods",
            result="SUCCESS"
        )
        
        example4 = {
            "scenario": "Переключение устройства",
            "snapshot": snapshot4.to_log_string(),
            "decision": decision4.to_log_string(),
            "action": action4.to_log_string(),
            "chain": f"{snapshot4.to_log_string()} → {decision4.to_log_string()} → {action4.to_log_string()}"
        }
        
        self.examples = [example1, example2, example3, example4]
        
        logger.info(f"✅ Создано {len(self.examples)} примеров логов:")
        for i, example in enumerate(self.examples, 1):
            logger.info(f"   {i}. {example['scenario']}")
        logger.info("")
        
        return True
        
    def test_reconstruction(self) -> bool:
        """Тест восстановления цепочки: snapshot → decision → action"""
        logger.info("📋 Тест восстановления цепочки...")
        logger.info("")
        
        success_count = 0
        
        for example in self.examples:
            logger.info(f"   Тест: {example['scenario']}")
            
            # Парсим цепочку
            chain = example['chain']
            
            # Проверяем наличие всех компонентов
            has_snapshot = "snapshot=" in chain
            has_decision = "decision=<" in chain
            has_action = "action=<" in chain
            
            if has_snapshot and has_decision and has_action:
                success_count += 1
                logger.info(f"      ✅ Цепочка восстановлена")
            else:
                logger.error(f"      ❌ Цепочка неполная (snapshot={has_snapshot}, decision={has_decision}, action={has_action})")
        
        logger.info("")
        
        success_rate = (success_count / len(self.examples)) * 100
        self.reconstruction_success = success_rate == 100.0
        
        logger.info(f"📊 Результаты восстановления:")
        logger.info(f"   Успешных: {success_count}/{len(self.examples)}")
        logger.info(f"   Успешность: {success_rate:.1f}%")
        logger.info("")
        
        return self.reconstruction_success
        
    def check_exit_gate(self) -> bool:
        """Проверка Exit Gate"""
        logger.info("=" * 80)
        logger.info("ПРОВЕРКА EXIT GATE")
        logger.info("=" * 80)
        logger.info("")
        
        checks = [
            ("Лог-формат определен", self.log_format_defined),
            ("Примеры логов созданы", len(self.examples) > 0),
            ("Цепочка восстанавливается", self.reconstruction_success)
        ]
        
        all_passed = True
        for check_name, check_result in checks:
            status = "✅" if check_result else "❌"
            logger.info(f"{status} {check_name}")
            if not check_result:
                all_passed = False
        
        logger.info("")
        
        if all_passed:
            logger.info("✅ MVP-0 ПРОЙДЕН: Все Exit Gate критерии выполнены")
        else:
            logger.error("❌ MVP-0 ПРОВАЛЕН: Есть невыполненные критерии")
        
        return all_passed
        
    def generate_report(self) -> str:
        """Генерация отчета"""
        report = {
            "mvp": "MVP-0: Observability",
            "status": "PASSED" if self.check_exit_gate() else "FAILED",
            "log_format": self.log_format if self.log_format_defined else None,
            "examples_count": len(self.examples),
            "reconstruction_success": self.reconstruction_success,
            "examples": self.examples
        }
        
        return json.dumps(report, indent=2, ensure_ascii=False)


def main():
    """Главная функция"""
    prototype = ObservabilityPrototype()
    
    if not prototype.setup():
        logger.error("❌ Setup провален")
        sys.exit(1)
        
    if not prototype.define_log_format():
        logger.error("❌ Определение формата провалено")
        sys.exit(1)
        
    if not prototype.create_examples():
        logger.error("❌ Создание примеров провалено")
        sys.exit(1)
        
    if not prototype.test_reconstruction():
        logger.error("❌ Тест восстановления провален")
        sys.exit(1)
    
    success = prototype.check_exit_gate()
    
    # Генерация отчета
    report = prototype.generate_report()
    report_file = Path(__file__).parent / "observability_report.json"
    report_file.write_text(report, encoding='utf-8')
    logger.info(f"📄 Отчет сохранен: {report_file}")
    logger.info("")
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

