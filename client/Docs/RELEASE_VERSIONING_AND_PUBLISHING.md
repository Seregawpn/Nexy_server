# Release Versioning & Publishing Guide (Client)

**Статус:** канонический регламент для обновления версии и заливки клиента  
**Целевая версия сейчас:** `1.6.1.40`  
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

1. Выбрать новую версию (например, `1.6.1.40`).
2. Запустить owner-скрипт:
```bash
python3 ../server/scripts/update_version.py 1.6.1.40
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

Для задач заливки клиента разрешен только один remote:
- `client_test` -> `https://github.com/Seregawpn/Nexy_client_test`

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

---

## 7. Definition of Done

- Версия синхронизирована во всех обязательных местах из раздела 3.
- Поиск старой версии возвращает 0 совпадений (кроме архивных/исторических записей).
- Push выполнен только в `Nexy_client_test`.
- Создан отчет в `Docs/assistant_exchange/codex/` с датой и перечнем измененных файлов.
