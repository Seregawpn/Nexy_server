# Analysis: Manual Diagnostics Cleanup Pass 3

## Scope
Client workspace: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client`

## Goal
Найти и очистить файлы, которые не участвуют в реальном runtime/CI/preflight/release контуре.

## Method
1. Проверка ссылок на файлы в `.github/workflows/ci.yml`, `scripts/pre_build_gate.sh`, `scripts/run_release_suite.py`, `scripts/problem_scan_gate.sh`, `packaging/build_final.sh`, ключевых docs.
2. Поиск упоминаний кандидатов через `rg` по всему клиентскому workspace.
3. Только безопасный cleanup: перенос в legacy вместо удаления.

## Applied changes (safe)
Перенесены из `scripts/` в `scripts/_legacy/manual_diagnostics/`:
- `debug_contact_resolution.py`
- `debug_whatsapp_session.py`
- `diagnose_whatsapp.py`
- `generate_qr.py`
- `manual_open_portal.py`
- `manual_verify_whatsapp.py`
- `test_avf_audio.py`
- `test_whatsapp_send.py`
- `v2_verify_whatsapp_gateway.py`
- `verify_browser_client.py`
- `verify_whatsapp.py`

Добавлен:
- `scripts/_legacy/manual_diagnostics/README.md`

## Why safe
- Нет подключений в CI/preflight/release scripts.
- Нет references из production runtime path.
- Файлы сохранены для истории и ручной отладки (без удаления).

## Remaining candidates (need decision)
1. `clean.sh`
- Не используется в CI/релизе.
- Но это мощный локальный очиститель macOS (может быть полезен операционно).
- Рекомендация: оставить, но переместить в `scripts/_legacy/ops_tools/` только если команда согласна.

2. `components.plist`
- Не используется текущим `packaging/build_final.sh`.
- Вероятно legacy от старого pkgbuild процесса.
- Рекомендация: перенести в `_Docs_ARCHIVED/legacy_artifacts/` или удалить после подтверждения.

3. `scripts/check_permissions_snapshot.py`
- Не в CI, но полезен для ручной диагностики permissions.
- Рекомендация: оставить в активном `scripts/` как support-tool.

4. `scripts/update_server_certificate.sh`
- Не в CI, но операционный инструмент ротации server cert.
- Рекомендация: оставить в активном `scripts/`.

5. `scripts/generate_hiddenimports.py`
- Не в CI, но полезен для ручной поддержки `Nexy.spec`.
- Рекомендация: оставить в активном `scripts/`.

## Risks
- Runtime/CI risk: low (перенос только ручных диагностических скриптов).
- Duplication risk: reduced (убран шум в активном `scripts/`).
- Race risk: none.
