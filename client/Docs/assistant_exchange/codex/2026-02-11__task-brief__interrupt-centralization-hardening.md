# Interrupt Centralization Hardening

Дата: 2026-02-11

## Что сделано
- Убран дублирующий путь `mode.request(SLEEPING)` из `ListeningWorkflow` при `interrupt.request`.
- В `InterruptCoordinator` добавлен lock-safe `cancel_all_interrupts()` и защита от гонки при финализации уже отменённого interrupt.
- В `InterruptManagementIntegration`:
  - ужесточён контракт чтения `interrupt.request` только из `event.data`;
  - удалены неиспользуемые side-channel события `speech.stop_requested`, `recording.stop_requested`, `session.clear_requested`;
  - удалён ручной `active_interrupts.clear()` путь, используется только coordinator API.

## Проверка
- `PYTHONPATH=. pytest -q tests/test_interrupt_management_contract.py tests/test_interrupt_playback.py`
  - результат: `22 passed`
- `python3 scripts/verify_cancel_centralization.py`
  - результат: `OK: cancel centralization verified`

## Эффект
- Один owner-path для interrupt → mode transition.
- Снижен риск race condition на `active_interrupts`.
- Меньше дублирующих/мертвых interrupt-событий.
