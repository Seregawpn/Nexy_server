# WhatsApp QR Not Displaying

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-05
- ID (INS-###): N/A

## Diagnosis
QR не отображается при запросе WhatsApp; вероятно, QR-событие не достигает QRViewer из-за несовпадения канала логов Node-сервиса и обработки в клиенте.

## Root Cause
Логи/QR из Node-WhatsApp MCP идут в stdout, а QR-парсер слушает только stderr → QR callback не вызывается → whatsapp.status остаётся connecting/disconnected → пользователь слышит только TTS без QR.

## Optimal Fix
Перенести/дублировать QR-детекцию в поток stdout внутри WhatsappMCPClient (единственный читатель stdout), вызывая service_manager.qr_callback при обнаружении qrCodeData/quickchart URL; оставить stderr-мониторинг как fallback.

## Verification
Запуск `client/scripts/force_login_whatsapp.py` показывает QR URL и открывает его в браузере; в логах появляется переход `whatsapp.status -> qr_required`, затем `connected` после сканирования.

## Запрос/цель
Разобрать, почему QR не показывается и дать архитектурно корректный план фикса.

## Контекст
- Файлы: `client/integration/integrations/whatsapp_integration.py`, `client/modules/whatsapp/service_manager.py`, `client/modules/whatsapp/mcp_client.py`, `client/modules/whatsapp/qr_viewer.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`
- Ограничения: без новых источников истины, через EventBus/StateManager

## Решения/выводы
- QR не должен обрабатываться вторым читателем stdout.
- Центр обработки QR должен быть там, где читается stdout (WhatsappMCPClient).

## Открытые вопросы
- Пишет ли whatsapp-mcp логи/qr в stdout или stderr в текущей сборке?
- Корректен ли `node_path` и существует ли `Whatsapp/whatsapp-mcp-ready/.../index.js`?

## Следующие шаги
- Добавить QR-детекцию в `WhatsappMCPClient._listen_loop` и `_handle_message`.
- Проверить верификацией через `force_login_whatsapp.py`.
