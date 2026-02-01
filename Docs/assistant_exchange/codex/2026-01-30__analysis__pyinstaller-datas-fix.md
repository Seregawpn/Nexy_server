# PyInstaller datas tuple fix

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-30
- ID (INS-###): INS-005

## Diagnosis
PyInstaller падает при разборе datas из Nexy.spec из-за элемента списка, который не является tuple.

## Root Cause
В datas добавлен динамический блок, который возвращает [] вместо (src, dest), что ломает format_binaries_and_datas.

## Optimal Fix
Вынести сбор Playwright driver в отдельный список extra_datas и добавлять его только если путь существует.

## Verification
Сборка PyInstaller проходит этап анализа без ValueError; driver подхватывается, если доступен.

## Запрос/цель
Устранить ValueError в Nexy.spec при добавлении Playwright driver.

## Контекст
- Файлы: client/packaging/Nexy.spec
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без изменения архитектуры

## Решения/выводы
- Убрана вставка [] в datas.
- Путь к driver вычисляется через import playwright.

## Открытые вопросы
- Должны ли мы также бандлить playwright/.local-browsers (не рекомендуется без явной просьбы).

## Следующие шаги
- Запустить сборку и подтвердить, что ValueError исчез.
