# Analysis — Accessibility Prompt Blocked

Дата: 2026-01-14  
Контекст: в `log.md` отсутствует диалог Accessibility при first-run.

## Наблюдения

- В системном логе зафиксированы вызовы `TCCAccessRequest` для Accessibility от `com.nexy.assistant` без приватного entitlement.
- macOS Sequoia блокирует prompt без `com.apple.private.tcc.manager.check-by-audit-token`.

## Вывод

Диалог Accessibility не появляется, потому что macOS блокирует `AXIsProcessTrustedWithOptions(prompt=True)` без приватного entitlement. Это поведение ОС, не баг в текущем вызове.

## Рекомендация

Для Accessibility нужен fallback через System Settings (in‑app alert → open Settings). Без энтайтлмента прямой prompt не гарантирован и часто блокируется.
