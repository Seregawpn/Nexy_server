# Build Logs: Contacts Module

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-24
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
Контакты не запрашиваются из-за отсутствия модуля `Contacts` в собранном .app.

## Root Cause
Внутри `/Applications/Nexy.app` отсутствуют файлы `Contacts*`; в runtime логах есть `No module named 'Contacts'`.

## Optimal Fix
Убедиться, что `pyobjc-framework-Contacts` установлен в окружении сборки и попадает в PyInstaller bundle; пересобрать.

## Verification
Внутри .app появляется модуль `Contacts`, диалог появляется после `tccutil reset Contacts`.

## Запрос/цель
Проверка сборочных логов на проблему с Contacts.

## Контекст
- Файлы: build_logs/packaging_20260123_103005.log
- Логи: `~/Library/Logs/Nexy/nexy.log`

## Решения/выводы
- В build logs явной ошибки по Contacts нет.
- В .app модуль отсутствует, значит проблема в сборочном окружении/bundle.

## Открытые вопросы
- Отсутствует Docs/CRM_INSTRUCTION_REGISTRY.md; нужен источник INS-###.

## Следующие шаги
- Проверить окружение сборки и пересобрать.
