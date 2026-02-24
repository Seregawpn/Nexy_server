#!/bin/bash
# Функция для автоматической активации venv при входе в директорию
# Добавьте в ~/.zshrc:
# source /Users/sergiyzasorin/Fix_new/server/.auto_activate_venv.sh

_auto_activate_venv() {
    if [[ -n "$VIRTUAL_ENV" ]]; then
        # Если venv уже активирован, проверяем, что мы все еще в правильной директории
        local venv_dir=$(dirname "$VIRTUAL_ENV")
        local project_dir="/Users/sergiyzasorin/Fix_new/server"
        
        if [[ "$PWD" != "$project_dir"* ]]; then
            # Выходим из venv, если покинули проект
            deactivate 2>/dev/null
        fi
    fi
    
    # Активируем venv, если находимся в директории проекта
    if [[ "$PWD" == "/Users/sergiyzasorin/Fix_new/server"* ]] && [[ -z "$VIRTUAL_ENV" ]]; then
        local venv_path="/Users/sergiyzasorin/Fix_new/server/.venv"
        if [[ -d "$venv_path" ]]; then
            source "$venv_path/bin/activate"
        fi
    fi
}

# Добавляем функцию в precmd hook zsh
autoload -Uz add-zsh-hook
add-zsh-hook chpwd _auto_activate_venv

# Вызываем при запуске
_auto_activate_venv
