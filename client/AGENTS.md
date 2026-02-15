# PROJECT ASSISTANT RULES — CLIENT

Этот файл дополняет корневой `AGENTS.md` и применяется только для клиентской части.

## Контекст клиента
- Базовые правила проекта: `AGENTS.md` (в корне).
- Архитектура и текущие принципы: `Docs/ARCHITECTURE_OVERVIEW.md`.
- Требования: `Docs/PROJECT_REQUIREMENTS.md`.
- Клиентские правила и упаковка: см. `.cursorrules` (раздел 1.0.1).
- Регламент версии и заливки: `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`.
- Документация: см. `Docs/README.md` для актуального индекса документов.

## Отчетность ассистента (обязательно)
- После каждого выполненного задания создать отчетный документ.
- Путь: `Docs/assistant_exchange/<assistant>/`.
- Формат имени: `YYYY-MM-DD__type__short-title.md`.
- Типы: `task-brief`, `analysis`, `review`, `handoff`.
- Перезапись запрещена: только новый файл.

## Фокус клиента
- Работай внутри текущих модулей и интеграций клиента.
- Не нарушай существующие границы модулей.

## Политика заливки в GitHub (обязательно)
- Если запрос касается заливки/публикации/push клиентской части, использовать только репозиторий: `https://github.com/Seregawpn/Nexy_client_test`.
- Не выполнять push в `Nexy`, `origin` или любые другие remote для клиентской заливки.

## Architecture Gates (обязательно, client-only)
- Правило: **One event, one owner** для критичных событий.
- Для mode-цепочки единственный owner переходов: `ModeManagementIntegration -> ModeController -> ApplicationStateManager`.
- Запрещено добавлять второй путь принятия решений (локальный workaround) вместо расширения owner-слоя.
- Любой runtime legacy/fallback путь обязан иметь `LEGACY_EXPIRY:` (версия/дата удаления).
- Новые `sys.path.insert(...)` вне `main.py` запрещены.
- Любой новый feature flag должен иметь runtime-использование и запись в `Docs/FEATURE_FLAGS.md`.

## PR Gate Policy (обязательно)
- PR должен содержать `Single Owner Check`:
- owner оси/события;
- source of truth;
- что удалено/слито как дубликат;
- доказательство, что второй путь не добавлен;
- expiry для legacy/fallback (если есть).
- PR без заполненного блока считается архитектурно неполным.

## CI/Local Enforcement
- CI: `.github/workflows/ci.yml` запускает `python scripts/verify_architecture_guards.py`.
- Local gate: `scripts/pre_build_gate.sh` также запускает `scripts/verify_architecture_guards.py`.
- Политика baseline: блокируются новые нарушения относительно `scripts/architecture_guard_baseline.json`.
