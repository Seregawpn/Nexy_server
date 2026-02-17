# Task Brief: Ctrl+N деградация при потере фокуса/VoiceOver

## Context
Пользователь сообщил: через некоторое время приложение теряет фокус, и при зажатии shortcut (`Ctrl+N`) активация не происходит, слышны только системные клики.

## Diagnosis
В owner-слое hotkey (`quartz_monitor`) фильтр комбинации был слишком строгим: для `Ctrl+N` запрещался любой `Shift`. В сценариях VoiceOver/frontmost transitions это приводило к ложному `non_target_combo` и пропуску события в систему.

## Implemented Fix
- Ослаблен предикат combo для `ctrl_n`:
  - обязательный `Control` оставлен;
  - запрещены только `Command/Alt`;
  - `Shift` допускается как transient noise.
- Согласовано поведение `combo_blocked_by_modifiers`:
  - блокирующими считаются только `Command/Alt` (без `Shift`).
- Обновлены комментарии под новое каноническое правило.

## Verification
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py` — passed.

## Информация об изменениях
- Что изменено:
  - Смягчена фильтрация модификаторов для `Ctrl+N`, чтобы исключить ложные блокировки при focus/VoiceOver шуме по `Shift`.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/input_processing/keyboard/mac/quartz_monitor.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-16__task-brief__ctrl-n-focus-voiceover-shift-tolerance-fix.md`
- Причина/цель изменений:
  - Устранить ситуацию, когда `Ctrl+N` перестаёт активироваться и даёт только системные клики при нестабильных модификаторах в macOS/VoiceOver контексте.
- Проверка (что выполнено для валидации):
  - Локальная компиляция изменённого модуля; анализ предоставленных `log.md` и `voiceover.md`.
