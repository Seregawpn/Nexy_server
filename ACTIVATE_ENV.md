# Автоматическая активация виртуального окружения

## Проблема
Виртуальное окружение не активируется автоматически при открытии терминала.

## Решения

### Вариант 1: В терминале Cursor/VS Code (рекомендуется)
Настройки уже включены в `.vscode/settings.json`:
- `python.terminal.activateEnvironment: true` - автоматическая активация
- `python.terminal.activateEnvInCurrentTerminal: true` - активация в текущем терминале

**Действия:**
1. Перезагрузите окно Cursor: `Cmd+Shift+P` → "Developer: Reload Window"
2. Откройте новый терминал в Cursor - окружение должно активироваться автоматически

### Вариант 2: Ручная активация через скрипт
```bash
cd /Users/sergiyzasorin/Fix_new/server
source activate.sh
```

### Вариант 3: Автоматическая активация через direnv
1. Установите direnv:
   ```bash
   brew install direnv
   ```

2. Добавьте в `~/.zshrc`:
   ```bash
   eval "$(direnv hook zsh)"
   ```

3. Перезагрузите shell:
   ```bash
   source ~/.zshrc
   ```

4. Файл `.envrc` уже создан - direnv автоматически активирует окружение при входе в директорию

### Вариант 4: Автоматическая активация через zsh hook
1. Добавьте в `~/.zshrc`:
   ```bash
   source /Users/sergiyzasorin/Fix_new/server/.auto_activate_venv.sh
   ```

2. Перезагрузите shell:
   ```bash
   source ~/.zshrc
   ```

Теперь окружение будет активироваться автоматически при входе в директорию проекта.

## Проверка активации
```bash
which python  # Должен показать: /Users/sergiyzasorin/Fix_new/server/.venv/bin/python
echo $VIRTUAL_ENV  # Должен показать путь к .venv
```

## Текущее состояние
- ✅ Виртуальное окружение: `/Users/sergiyzasorin/Fix_new/server/.venv`
- ✅ Python версия: 3.13.7
- ✅ Настройки Cursor: включены
- ⚠️ Требуется перезагрузка окна Cursor для применения настроек
