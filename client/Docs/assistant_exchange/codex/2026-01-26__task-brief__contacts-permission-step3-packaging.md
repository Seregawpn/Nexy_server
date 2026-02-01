# Contacts Permission Step 3 — Packaging/Deps Check

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-26
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
Контакты требуют наличия pyobjc Contacts framework в рантайме и включения в сборку PyInstaller.

## Root Cause
Без `pyobjc-framework-Contacts` или `Contacts` в hiddenimports диалог не появится.

## Optimal Fix
Подтвердить:
- `requirements.txt` содержит `pyobjc-framework-Contacts`.
- `packaging/Nexy.spec` включает `Contacts` в `hiddenimports`.
- `packaging/build_final.sh` проверяет `import Contacts`.

## Verification
- Все три пункта присутствуют в коде/скриптах.

## Запрос/цель
Выполнить третий этап — проверка зависимостей и упаковки.

## Контекст
- Файлы: requirements.txt, packaging/Nexy.spec, packaging/build_final.sh

## Решения/выводы
- `requirements.txt` содержит `pyobjc-framework-Contacts==12.1`.
- `packaging/Nexy.spec` включает `Contacts` в hiddenimports.
- `packaging/build_final.sh` проверяет `import Contacts` (arm64/x86_64).

## Открытые вопросы
- Нет.

## Следующие шаги
- Переход к runtime‑проверке (logs/ledger/trigger).
