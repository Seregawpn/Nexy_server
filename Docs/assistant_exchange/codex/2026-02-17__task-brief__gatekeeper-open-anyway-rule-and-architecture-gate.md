# Gatekeeper Open Anyway Rule And Architecture Gate

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-17
- ID (INS-###): N/A

## Diagnosis
Требовалось формально закрепить в правилах и архитектурном документе запрет на release с риском "Open Anyway".

## Root Cause
Anti-Gatekeeper требования были обсуждены операционно, но не были явно зафиксированы как обязательный rule/gate в root-каноне.

## Optimal Fix
1. В `AGENTS.md` добавлен обязательный раздел:
   - `11) Gatekeeper / Notarization Gate (обязательно)`
   - включает обязательные проверки:
     - `codesign --verify --deep --strict dist/Nexy.app`
     - `xcrun stapler validate dist/Nexy.app`
     - `xcrun stapler validate dist/Nexy.dmg`
   - фиксирует запреты (post-signature mutation, overwrite same tag, обход runbook).

2. В `Docs/ARCHITECTURE_OVERVIEW.md` добавлено root-level правило:
   - `Release integrity gate` с ссылками на канонические документы release-потока.

## Verification
- Проверка наличия новых маркеров через `rg`.

## Информация об изменениях
- Что изменено:
  - Добавлен обязательный Gatekeeper/Notarization rule в root rules.
  - Добавлен архитектурный integrity gate для release.
- Файлы:
  - `AGENTS.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
- Причина/цель:
  - Исключить повторные релизы с риском "Open Anyway" на уровне обязательных правил.
- Проверка:
  - grep-проверка новых секций и ключевых формулировок.

## Запрос/цель
Записать anti-"Open Anyway" требования в rules и architecture document.

## Контекст
- Production release owner-flow уже централизован.

## Решения/выводы
- Требование теперь зафиксировано в корневых правилах и архитектурном индексе.

## Открытые вопросы
- Нет.

## Следующие шаги
- Следовать release runbook и Gatekeeper/Notarization gate без обходов.
