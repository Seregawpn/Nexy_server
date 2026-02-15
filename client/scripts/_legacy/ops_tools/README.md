# Ops Tools (Legacy)

Операционные утилиты, не входящие в CI/preflight/release pipeline.

Текущий состав:
- `clean.sh` — полный локальный cleanup следов Nexy на macOS.

Правило:
- запуск только вручную;
- любые изменения в этих инструментах не должны влиять на production pipeline без явного подключения в CI/docs.
