# Task Brief: Integration Dependency Management

## Scope
Formalize integration dependencies via `provides/requires`, runtime validation, and linting for direct client usage.

## Changes
- `integration/core/base_integration.py`: added `provides`/`requires` default sets.
- `integration/integrations/grpc_client_integration.py`: `provides={"grpc_client"}` + getters.
- `integration/integrations/welcome_message_integration.py`: `requires={"grpc_client"}`, defer WelcomePlayer creation to `initialize()`.
- `integration/core/simple_module_coordinator.py`: runtime dependency warnings + tracking of provided capabilities (both startup paths).
- `modules/welcome_message/core/audio_generator.py`: removed direct gRPC client creation; now requires injection.
- `scripts/check_dependency_violations.py`: AST lint for direct client instantiation.

## Verification
- `python3 scripts/check_dependency_violations.py` -> OK.
- `scripts/verify_feature_flags.py` отсутствует (не удалось выполнить required discovery).

## Notes
Dependency warnings are WARN-only (no enforcement).
