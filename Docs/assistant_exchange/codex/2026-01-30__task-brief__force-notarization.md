# Force Notarization Always

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-30
- ID (INS-###): INS-005

## Diagnosis
Нотаризация пропускалась через флаги skip, что недопустимо.

## Root Cause
В build_final.sh были условия SKIP_NOTARIZATION и офлайн-guard, позволяющие пропустить notarization и stapler validate.

## Optimal Fix
Убрать все ветки skip и всегда выполнять notarytool submit + stapler validate; при TIMESTAMP_MODE=none — остановка сборки.

## Verification
Сборка падает при отсутствии сети (ожидаемо), но notarization всегда выполняется при наличии сети.

## Запрос/цель
Сделать нотарификацию обязательной без опций пропуска.

## Контекст
- Файлы: client/packaging/build_final.sh
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без изменения логики подписи вне notarization

## Решения/выводы
- Удалены все условия SKIP_NOTARIZATION для app/DMG/PKG и validate.
- Добавлена ошибка при TIMESTAMP_MODE=none.

## Открытые вопросы
- Нужен ли отдельный режим для офлайн-сборок (не предусмотрен после изменения).

## Следующие шаги
- Запустить build_final.sh с рабочей сетью и проверить notarytool/stapler.
