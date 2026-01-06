# Skip Build Flag

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-02

## Запрос/цель
Добавить флаг --skip-build в packaging/build_final.sh для переиспользования существующего dist/Nexy.app.

## Контекст
- Файлы: packaging/build_final.sh, Docs/PACKAGING_FINAL_GUIDE.md
- Документы: Docs/PACKAGING_FINAL_GUIDE.md
- Ограничения: единый источник истины, без дублирования пайплайна

## Решения/выводы
- Добавлен парсинг флага --skip-build и проверка Universal 2.
- Документация обновлена с примером использования.

## Открытые вопросы
- Нет.

## Следующие шаги
- Прогнать ./packaging/build_final.sh --skip-build и проверить dist/packaging_verification.log.
