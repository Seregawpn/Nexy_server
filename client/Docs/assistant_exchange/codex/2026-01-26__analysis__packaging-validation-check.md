# Packaging Validation Check

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-26
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
В текущих артефактах `dist/Nexy.pkg` и `dist/Nexy.dmg` подписи невалидны по локальной проверке, а `/Applications/Nexy.app` отсутствует для прямой валидации.

## Root Cause
Сборка была прервана таймаутом на этапе нотарификации, поэтому артефакты могли остаться в промежуточном/некорректном состоянии.

## Optimal Fix
Дождаться полного завершения `packaging/build_final.sh` (без таймаута) и повторить проверку подписи.

## Verification
- `pkgutil --check-signature dist/Nexy.pkg` должен быть valid
- `spctl -a -vv dist/Nexy.pkg` / `spctl -a -vv dist/Nexy.dmg` должны проходить

## Запрос/цель
Проверить корректность упаковки.

## Контекст
- Файлы: dist/Nexy.pkg, dist/Nexy.dmg, build_logs/build_20260126_110845.log

## Решения/выводы
- Локальная проверка показала `invalid signature` для pkg.
- Валидация app невозможна: `/Applications/Nexy.app` отсутствует.

## Открытые вопросы
- Нужен ли прогон сборки без нотарификации (для локального теста)?

## Следующие шаги
- Перезапустить `packaging/build_final.sh` и дождаться завершения.
- Повторить проверки spctl/pkgutil.
