# Autostart Duplication Conflict Race Review

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-02-11

## Findings
1. Документационный конфликт: `autostart_manager_integration.py` содержит тезис "PKG управляет автозапуском", но `packaging/pkg_scripts/postinstall` больше не создает LaunchAgent.
2. Потенциальный второй путь: в модуле есть альтернативный `login_item` метод, но он не используется в интеграции.
3. Потенциальная гонка (latent): `_check_autostart_status()` может вызываться параллельно из startup/event/monitor; при `auto_repair=true` возможны параллельные попытки `enable_autostart()`.

## Risk
- Runtime сейчас низкий (из-за `auto_repair=false`), но структурный риск средний.

## Recommended minimal fix
- Обновить комментарии/документацию в интеграции под текущую политику packaging.
- Явно зафиксировать `launch_agent` как единственный поддерживаемый runtime-метод (или удалить неиспользуемый `login_item` путь).
- Добавить single-flight guard (`asyncio.Lock`) вокруг repair-path в `AutostartManagerIntegration`.
