# Golden Artifacts Verification

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-01-02

## Запрос/цель
Проверить подпись/нотарификацию и отсутствие AppleDouble в артефактах dist/Nexy.app и dist/Nexy.pkg.

## Контекст
- Файлы: dist/Nexy.app, dist/Nexy.pkg, /tmp/Nexy.app
- Документы: Docs/PACKAGING_FINAL_GUIDE.md
- Ограничения: проверка без sudo/installer

## Решения/выводы
Статус: НЕ СООТВЕТСТВУЕТ

## Найденные проблемы (если review)
- codesign verify провалился: dist/Nexy.app имеет "nested code is modified or invalid" и множественные "file modified" для Frameworks.
- pkgutil --check-signature показывает "Status: invalid signature" для dist/Nexy.pkg.
- xcrun stapler validate не смог открыть dist/Nexy.app и dist/Nexy.pkg (kLSDataUnavailableErr).
- /tmp/Nexy.app также имеет invalid signature (arm64).

## Открытые вопросы
- Какие конкретные шаги выполнялись после подписи/стаплинга, могли ли артефакты быть модифицированы?

## Следующие шаги
- Пересобрать артефакты и немедленно зафиксировать логи: codesign --verify, pkgutil --check-signature, xcrun stapler validate.
- Убедиться, что после подписи/стаплинга не выполняются операции, изменяющие Contents (включая xattr чистки и замену файлов).
