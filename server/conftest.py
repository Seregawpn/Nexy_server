"""Pytest fixtures and options shared across the Nexy server test suite."""

from __future__ import annotations

import asyncio
import inspect
import os
from typing import Optional

import pytest


def _resolve_option(
    pytestconfig: pytest.Config,
    option_name: str,
    env_var: str,
) -> Optional[str]:
    """Return the CLI option or environment variable value if it is configured."""

    option_value = pytestconfig.getoption(option_name)
    if option_value:
        return option_value
    env_value = os.getenv(env_var)
    return env_value


def pytest_addoption(parser: pytest.Parser) -> None:
    """Register CLI flags for optional integration tests."""

    group = parser.getgroup("nexy")
    group.addoption(
        "--grpc-host",
        action="store",
        default=None,
        help="Target host for live gRPC smoke checks",
    )
    group.addoption(
        "--grpc-port",
        action="store",
        default=None,
        type=int,
        help="Target port for live gRPC smoke checks",
    )
    group.addoption(
        "--http-port",
        action="store",
        default=None,
        type=int,
        help="Target HTTP port for live health checks",
    )
    group.addoption(
        "--updates-port",
        action="store",
        default=None,
        type=int,
        help="Target port for the update service health endpoint",
    )


@pytest.fixture(name="host")
def grpc_host(pytestconfig: pytest.Config) -> str:
    """Return the integration test host or skip when it is not configured."""

    value = _resolve_option(pytestconfig, "--grpc-host", "NEXY_TEST_GRPC_HOST")
    if not value:
        pytest.skip(
            "gRPC integration host is not configured. "
            "Provide --grpc-host or set NEXY_TEST_GRPC_HOST to enable live checks."
        )
    return value


@pytest.fixture(name="port")
def grpc_port(pytestconfig: pytest.Config) -> int:
    """Return the integration test gRPC port or skip when it is not configured."""

    value = _resolve_option(pytestconfig, "--grpc-port", "NEXY_TEST_GRPC_PORT")
    if value is None:
        pytest.skip(
            "gRPC integration port is not configured. "
            "Provide --grpc-port or set NEXY_TEST_GRPC_PORT to enable live checks."
        )
    try:
        return int(value)
    except (TypeError, ValueError) as exc:  # pragma: no cover - defensive guard
        raise pytest.UsageError("gRPC port must be an integer") from exc


@pytest.fixture(name="http_port")
def http_port(pytestconfig: pytest.Config) -> int:
    """Return the HTTP port used for health checks or skip when missing."""

    value = _resolve_option(pytestconfig, "--http-port", "NEXY_TEST_HTTP_PORT")
    if value is None:
        pytest.skip(
            "HTTP health-check port is not configured. "
            "Provide --http-port or set NEXY_TEST_HTTP_PORT to enable live checks."
        )
    return int(value)


@pytest.fixture(name="updates_port")
def updates_port(pytestconfig: pytest.Config) -> int:
    """Return the update service port or skip when it is not configured."""

    value = _resolve_option(pytestconfig, "--updates-port", "NEXY_TEST_UPDATES_PORT")
    if value is None:
        pytest.skip(
            "Update service port is not configured. "
            "Provide --updates-port or set NEXY_TEST_UPDATES_PORT to enable live checks."
        )
    return int(value)


@pytest.fixture(name="max_streams")
def max_streams_fixture() -> int:
    """Default maximum stream count for backpressure smoke checks."""

    env_value = os.getenv("NEXY_TEST_MAX_STREAMS")
    if env_value is not None:
        try:
            return int(env_value)
        except ValueError:  # pragma: no cover - defensive guard
            pass
    return 50


@pytest.hookimpl(tryfirst=True)
def pytest_pyfunc_call(pyfuncitem: pytest.Function) -> Optional[bool]:
    """Run coroutine tests inside an event loop without requiring pytest-asyncio."""

    test_func = pyfuncitem.obj
    if not inspect.iscoroutinefunction(test_func):
        return None

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        signature = inspect.signature(test_func)
        accepted_kwargs = {
            name: pyfuncitem.funcargs[name]
            for name in signature.parameters.keys()
            if name in pyfuncitem.funcargs
        }
        loop.run_until_complete(test_func(**accepted_kwargs))
    finally:
        try:
            loop.run_until_complete(loop.shutdown_asyncgens())
        finally:
            loop.close()
            asyncio.set_event_loop(None)
    return True
