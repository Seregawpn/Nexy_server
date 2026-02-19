# Release Versioning & Publishing Guide (Client)

**Статус:** канонический регламент для обновления версии и заливки клиента  
**Целевая версия сейчас:** `1.6.1.43`  
**Целевой GitHub-репозиторий для клиентской заливки:** `https://github.com/Seregawpn/Nexy_client_test`

---

## 1. Область действия

Этот регламент обязателен для любых задач:
- обновить версию клиента;
- собрать/подготовить релиз;
- залить изменения клиента в GitHub.

---

## 2. Source of Truth

Единый source of truth для релизной версии:
- `../VERSION` (корень workspace)

Обновление версии выполнять только owner-скриптом:
```bash
python3 ../server/scripts/update_version.py X.Y.Z.W
```

Этот скрипт обновляет `../config/unified_config.yaml` и запускает `../config/auto_sync.py`, который синхронизирует все производные client-файлы.

---

## 3. Где обязательно должна совпадать версия

### Runtime / config
- `config/unified_config.yaml`
- `client/VERSION_INFO.json`

### Packaging
- `packaging/distribution.xml`

### Bundle metadata (Info.plist)
- `modules/grpc_client/macos/info/Info.plist`
- `modules/hardware_id/macos/info/Info.plist`
- `modules/input_processing/macos/info/Info.plist`

### Python package markers
- `integration/__init__.py`
- `integration/workflows/__init__.py`
- `integration/integrations/__init__.py`
- `modules/*/__init__.py` (где есть `__version__`)

---

## 4. Обязательный процесс обновления версии

1. Выбрать новую версию (например, `1.6.1.41`).
2. Запустить owner-скрипт:
```bash
python3 ../server/scripts/update_version.py 1.6.1.41
```
3. Проверить, что синк client-файлов выполнен (`../config/auto_sync.py` запускается автоматически).
4. Проверить, что старой версии в клиенте не осталось:
```bash
rg -n "OLD_VERSION" . -S -g '!**/*.pyc' -g '!.venv/**' -g '!build_logs/**'
```
5. Проверить, что новая версия стоит в ключевых точках:
```bash
rg -n "NEW_VERSION" \
  config/unified_config.yaml \
  client/VERSION_INFO.json \
  packaging/distribution.xml \
  integration/__init__.py integration/workflows/__init__.py integration/integrations/__init__.py \
  modules/*/__init__.py modules/*/macos/info/Info.plist -S
```

---

## 5. Политика правильной заливки (Client)

Для client **code push** разрешен только один remote:
- `client_test` -> `https://github.com/Seregawpn/Nexy_client_test`

Для production **release assets** (`Nexy.dmg`, `Nexy.pkg`, `LATEST_CHANGES.md`) owner-канал:
- `Seregawpn/Nexy_production` (публикация через server publish flow).

Не смешивать code push и artifact publish.

Запрещено для клиентской заливки:
- `origin` (`Nexy`)
- любые другие remote

---

## 6. Обязательный процесс заливки клиента

1. Убедиться, что работа ведется из директории:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client`

2. Стадировать только клиентскую часть:
```bash
git add -A .
```

3. Проверить staged:
```bash
git status --short
git diff --cached --name-only
```
В staged не должно быть путей вне `client/...`.

4. Сделать commit:
```bash
git commit -m "chore: ..."
```

5. Пушить только в `client_test`:
```bash
git push client_test HEAD:refs/heads/<target-branch>
```

6. Проверить remote-ветку:
```bash
git ls-remote --heads client_test <target-branch>
```

7. После завершения релизного апдейта очистить журнал текущего цикла:
- Обновить `Docs/LATEST_CHANGES.md` до шаблона нового цикла:
  - `Статус: EMPTY`
  - `Изменения текущего цикла: - (пусто)`
- Это обязательный reset перед следующей серией изменений.

---

## 7. Обязательная синхронизация release_inbox (DMG/PKG/LATEST_CHANGES)

Перед publish на сервере артефакты и снимок журнала изменений должны быть синхронизированы в:

- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/release_inbox`

Единый owner-скрипт на клиенте:

```bash
./scripts/sync_release_inbox.sh
```

Скрипт копирует:
- `dist/Nexy.dmg`
- `dist/Nexy.pkg`
- `Docs/LATEST_CHANGES.md` -> `release_inbox/LATEST_CHANGES.md`

Автоматический путь:
- `./packaging/build_final.sh` после сборки и валидации всегда выполняет `sync_release_inbox.sh`.

---

## 8. Definition of Done

- Версия синхронизирована во всех обязательных местах из раздела 3.
- Поиск старой версии возвращает 0 совпадений (кроме архивных/исторических записей).
- Push выполнен только в `Nexy_client_test`.
- `Nexy.dmg`, `Nexy.pkg`, `LATEST_CHANGES.md` синхронизированы в `server/release_inbox`.
- Создан отчет в `Docs/assistant_exchange/codex/` с датой и перечнем измененных файлов.
- `Docs/LATEST_CHANGES.md` обновлялся в changeset и очищен после завершения апдейта.

---

## 9. Пошаговый Production Release (обязательно)

Единый запуск (рекомендуется):

```bash
cd /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27
./scripts/release_package_and_publish.sh
```

Что выполняется по шагам:

1. Packaging owner (`packaging/build_final.sh`)
- Сборка/подпись/нотаризация.
- Автосинхронизация в `server/release_inbox`:
  - `Nexy.dmg`
  - `Nexy.pkg`
  - `LATEST_CHANGES.md`

2. Publish owner (`server/server/scripts/publish_assets_and_sync.py`)
- Публикация assets в `Seregawpn/Nexy_production`.
- Единый release tag: `vX.Y.Z.W`.
- Повторный запуск для того же tag:
  - если файлы совпадают -> `already published, skip`;
  - если отличаются -> publish блокируется (без overwrite).

3. Remote metadata sync (`server/server/scripts/update_manifest_remote_locked.sh`)
- Обновляет remote `manifest.json` на VM по `url/size/sha256` из релиза.
- Server code deploy для этого шага не требуется.

4. Обязательная проверка после релиза
- Проверить release в GitHub: `Seregawpn/Nexy_production`, tag `vX.Y.Z.W`.
- Проверить update metadata (`manifest`/appcast/health).
- Проверить установку DMG на чистом Mac.

Запрещено:
- использовать альтернативные packaging entrypoints;
- вручную перезаписывать assets под тем же version tag;
- править `manifest.json` вручную.
