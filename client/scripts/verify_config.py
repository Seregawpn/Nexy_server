#!/usr/bin/env python3
"""
verify_config.py — Preflight проверки конфигурации

Проверяет:
1. Синтаксис YAML
2. Наличие обязательных секций и полей
3. Корректность типов значений
4. Валидность настроек серверов (local/production)
"""

import os
import sys
from typing import Any

# Цвета для вывода
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
NC = "\033[0m"


class TestResult:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.warnings = 0
        self.errors = []

    def ok(self, name: str):
        self.passed += 1
        print(f"  {GREEN}✓{NC} {name}")

    def warn(self, name: str, reason: str):
        self.warnings += 1
        print(f"  {YELLOW}⚠{NC} {name}: {reason}")

    def fail(self, name: str, reason: str):
        self.failed += 1
        self.errors.append(f"{name}: {reason}")
        print(f"  {RED}✗{NC} {name}: {reason}")

    def summary(self) -> bool:
        total = self.passed + self.failed
        if self.failed == 0:
            msg = f"Все {total} проверок пройдены"
            if self.warnings > 0:
                msg += f" ({self.warnings} предупреждений)"
            print(f"\n{GREEN}✅ {msg}{NC}")
            return True
        else:
            print(f"\n{RED}❌ Провалено {self.failed} из {total} проверок{NC}")
            for err in self.errors:
                print(f"   • {err}")
            return False


def find_config_file() -> str:
    """Найти unified_config.yaml."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    client_dir = os.path.dirname(script_dir)
    config_path = os.path.join(client_dir, "config", "unified_config.yaml")
    return config_path


def test_yaml_syntax(result: TestResult, config_path: str) -> dict[str, Any] | None:
    """Проверка синтаксиса YAML."""
    try:
        import yaml

        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        if config is None:
            result.fail("YAML синтаксис", "Файл пустой или невалидный")
            return None

        result.ok(f"YAML синтаксис валиден ({len(config)} секций)")
        return config

    except yaml.YAMLError as e:
        result.fail("YAML синтаксис", str(e))
        return None
    except FileNotFoundError:
        result.fail("YAML файл", f"Не найден: {config_path}")
        return None
    except Exception as e:
        result.fail("YAML загрузка", str(e))
        return None


def test_required_sections(result: TestResult, config: dict[str, Any]):
    """Проверка обязательных секций."""
    required = ["app", "integrations", "grpc"]

    for section in required:
        if section in config:
            result.ok(f"Секция '{section}' присутствует")
        else:
            result.fail(f"Секция '{section}'", "Отсутствует")


def test_integrations(result: TestResult, config: dict[str, Any]):
    """Проверка конфигурации интеграций."""
    integrations = config.get("integrations", {})
    if not integrations:
        result.fail("integrations", "Секция пустая")
        return

    # Критичные интеграции (актуальный канон)
    critical = ["grpc_client", "permissions_v2", "voice_recognition"]
    for name in critical:
        if name in integrations:
            int_cfg = integrations[name]
            enabled = int_cfg.get("enabled", True)
            status = "включена" if enabled else "отключена"
            if enabled:
                result.ok(f"Интеграция '{name}' {status}")
            else:
                result.warn(f"Интеграция '{name}'", f"{status}")
        else:
            result.warn(f"Интеграция '{name}'", "Не найдена в конфиге")


def test_grpc_servers(result: TestResult, config: dict[str, Any]):
    """Проверка конфигурации gRPC серверов."""
    grpc = config.get("grpc", {})
    servers = grpc.get("servers", {})

    if not servers:
        result.fail("gRPC серверы", "Секция 'grpc.servers' пустая")
        return

    # Проверяем обязательные серверы
    for server_name in ["local", "production"]:
        if server_name not in servers:
            result.fail(f"gRPC сервер '{server_name}'", "Не определён")
            continue

        server = servers[server_name]
        host = server.get("host", "")
        port = server.get("port", 0)

        if not host:
            result.fail(f"gRPC '{server_name}'", "host не указан")
        elif not port:
            result.fail(f"gRPC '{server_name}'", "port не указан")
        else:
            result.ok(f"gRPC '{server_name}' = {host}:{port}")


def test_grpc_client_config(result: TestResult, config: dict[str, Any]):
    """Проверка конфигурации gRPC клиента."""
    integrations = config.get("integrations", {})
    grpc_client = integrations.get("grpc_client", {})

    if not grpc_client:
        result.warn("grpc_client", "Конфигурация не найдена")
        return

    server = grpc_client.get("server", "production")

    if server == "local":
        result.ok(f"grpc_client.server = '{server}' (разработка)")
    elif server == "production":
        result.warn("grpc_client.server", f"'{server}' (для продакшена)")
    else:
        result.warn("grpc_client.server", f"Неизвестное значение: '{server}'")

    # Проверяем таймауты
    timeout = grpc_client.get("request_timeout_sec", 30)
    if timeout > 60:
        result.warn("grpc_client.request_timeout_sec", f"{timeout}s слишком большой")
    else:
        result.ok(f"grpc_client.request_timeout_sec = {timeout}s")


def test_updater_config(result: TestResult, config: dict[str, Any]):
    """Проверка конфигурации Sparkle/Updater."""
    updater = config.get("updater", {})
    default = updater.get("default", {})

    if not default:
        result.warn("updater", "Конфигурация не найдена")
        return

    enabled = default.get("enabled", True)
    check_on_startup = default.get("check_on_startup", True)

    if enabled and check_on_startup:
        result.warn("updater", "Включён и проверяет при запуске (может вызвать задержки)")
    elif not enabled:
        result.ok("updater.enabled = false (отключён)")
    else:
        result.ok(f"updater: enabled={enabled}, check_on_startup={check_on_startup}")


def test_permissions_config(result: TestResult, config: dict[str, Any]):
    """Проверка конфигурации разрешений."""
    integrations = config.get("integrations", {})
    perms_v2 = integrations.get("permissions_v2", {})

    if not perms_v2:
        result.warn("permissions_v2", "Конфигурация не найдена")
        return

    if perms_v2.get("enabled", False):
        result.ok("permissions_v2.enabled = true")
    else:
        result.warn("permissions_v2.enabled", "false (flow разрешений отключен)")

    order = perms_v2.get("order", [])
    if not isinstance(order, list) or not order:
        result.warn("permissions_v2.order", "Список пуст")
    else:
        result.ok(f"permissions_v2.order: {order}")

    perm_restart = integrations.get("permission_restart", {})
    critical_permissions = perm_restart.get("critical_permissions", [])
    if not isinstance(critical_permissions, list) or not critical_permissions:
        result.warn("permission_restart.critical_permissions", "Список пуст")
    else:
        result.ok(f"permission_restart.critical_permissions: {critical_permissions}")


def main():
    print(f"\n{YELLOW}📋 КОНФИГУРАЦИЯ PREFLIGHT ПРОВЕРКИ{NC}")
    print("=" * 50)

    result = TestResult()
    config_path = find_config_file()

    print(f"\n{YELLOW}1. YAML синтаксис{NC}")
    config = test_yaml_syntax(result, config_path)

    if config is None:
        print("=" * 50)
        result.summary()
        sys.exit(1)

    print(f"\n{YELLOW}2. Обязательные секции{NC}")
    test_required_sections(result, config)

    print(f"\n{YELLOW}3. Интеграции{NC}")
    test_integrations(result, config)

    print(f"\n{YELLOW}4. gRPC серверы{NC}")
    test_grpc_servers(result, config)

    print(f"\n{YELLOW}5. gRPC клиент{NC}")
    test_grpc_client_config(result, config)

    print(f"\n{YELLOW}6. Updater (Sparkle){NC}")
    test_updater_config(result, config)

    print(f"\n{YELLOW}7. Разрешения{NC}")
    test_permissions_config(result, config)

    print("=" * 50)
    success = result.summary()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
