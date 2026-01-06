# Post-Signing Hash Guard

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-03

## Запрос/цель
Добавить проверку целостности .app после подписи и копирования в dist/.

## Контекст
- Файлы: packaging/build_final.sh, Docs/PACKAGING_FINAL_GUIDE.md
- Документы: Docs/PACKAGING_FINAL_GUIDE.md

## Решения/выводы
- Добавлена функция hash_app_bundle и сравнение хэша CLEAN_APP с dist/Nexy.app.
- Документация дополнена упоминанием защиты от post-signing изменений.

## Открытые вопросы
- Нет.

## Следующие шаги
- Запустить build_final.sh и убедиться, что hash guard не срабатывает.
