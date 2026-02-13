# Task
Убрать избыточный warning-шум в runtime-логах без изменения бизнес-поведения.

# Applied Changes
1. `integration/integrations/permission_restart_integration.py`
- `V2 enabled: legacy permission restart paths are frozen...` переведен из `WARNING` в `INFO`.

2. `modules/tray_controller/macos/menu_handler.py`
- `NSApplication activation policy не установлен, устанавливаем...` переведен из `WARNING` в `INFO`.

3. `modules/grpc_client/core/connection_manager.py`
- `SSL verification disabled for ...` переведен из `WARNING` в `INFO` (dev/self-signed сценарий).

4. `modules/updater/net.py`
- `SSL verification disabled ...` переведен в `INFO`.
- Исправлен параметр `cert_reqs`: теперь `ssl.CERT_NONE` вместо строки `"CERT_NONE"` (убирает ложный warning про `str` -> `integer`).

5. `modules/voice_recognition/core/google_sr_controller.py`
- `Google could not understand audio` переведен из `WARNING` в `INFO`.

6. `integration/integrations/voice_recognition_integration.py`
- `[AUDIO_V2] Recognition failed: ...` переведен из `WARNING` в `INFO`.

# Validation
- Выполнен `py_compile` для измененных файлов — ошибок нет.

# Expected Impact
- Существенно меньше `WARNING` в `nexy-dev.log`.
- В `WARNING` остаются более значимые события (например, real workflow failures), а ожидаемые transient/dev-path события становятся `INFO`.
