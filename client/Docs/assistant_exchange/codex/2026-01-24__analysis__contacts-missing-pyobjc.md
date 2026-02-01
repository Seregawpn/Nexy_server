# Contacts Prompt Missing

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-24
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
Contacts разрешение не запрашивается, потому что модуль Contacts не импортируется в рантайме.

## Root Cause
В логах `~/Library/Logs/Nexy/nexy.log` есть предупреждение: `Contacts framework not available: No module named 'Contacts'` → отсутствует pyobjc-framework-Contacts в сборке/окружении.

## Optimal Fix
Убедиться, что `pyobjc-framework-Contacts` установлен в окружении сборки и включен в bundle (hiddenimports), затем пересобрать приложение.

## Verification
Импорт `Contacts` должен проходить, а диалог Contacts появляться при `tccutil reset Contacts`.

## Запрос/цель
Определить причину отсутствия запроса Contacts и путь устранения.

## Контекст
- Файлы: packaging/Nexy.spec, requirements.txt
- Логи: `~/Library/Logs/Nexy/nexy.log`

## Решения/выводы
- Причина — отсутствует модуль `Contacts` в рантайме, а не ошибка логики запроса.

## Открытые вопросы
- Отсутствует Docs/CRM_INSTRUCTION_REGISTRY.md; нужен источник INS-###.

## Следующие шаги
- Проверить окружение сборки, пересобрать `.app`.
