# Summary
- Dev лог найден в `~/Library/Logs/Nexy/nexy.log` (не в Application Support).
- Текущие ошибки: дубликаты инстанса, Quartz monitor broken pipe, WhatsApp node missing, welcome gRPC loop mismatch (см. фиксы).

# Key Errors (timestamps)
- 2026-02-05 10:38:05–10:38:51: duplicate_instance SAFE_EXIT (lock in `~/Library/Application Support/Nexy/nexy.lock`).
- 2026-02-05 10:38:12/10:38:24: Quartz monitor `Broken pipe` → keyboard backend none.
- 2026-02-05 11:11:05: WhatsApp service start failed: `/usr/local/bin/node` missing.
- 2026-02-05 11:11:05: welcome audio gRPC loop mismatch error.

# Locations
- ~/Library/Logs/Nexy/nexy.log
- ~/Library/Logs/Nexy/nexy.log.1 (older)

# Tests
- Not run (log analysis only).
