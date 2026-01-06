# TCC Reset + Build Attempt

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-01-04

## Запрос/цель
- Прогнать шаги верификации фикса TCC (reset + build + запуск).

## Контекст
- Файлы: packaging/build_final.sh
- Ограничения: требуется Developer ID Application сертификат для сборки

## Решения/выводы
- `tccutil reset Accessibility/ListenEvent` выполнен успешно.
- `NEXY_SKIP_NOTARIZATION=1 ./packaging/build_final.sh` завершился ошибкой: Developer ID Application сертификат не найден в keychain.
- Сборка и запуск приложения не выполнены из-за отсутствия сертификата.

## Открытые вопросы
- Есть ли доступный Developer ID Application сертификат/ключ в текущем keychain?

## Следующие шаги
- Установить/разблокировать сертификат Developer ID Application.
- Повторить сборку и запуск для проверки TCC логов.
