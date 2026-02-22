# Task Brief: Full Disk Access visibility in first-run

## Summary
Исправлена причина, из-за которой `Nexy` мог не отображаться в списке Full Disk Access в момент открытия страницы Privacy.

## What changed
1. В `PermissionOrchestrator` убрано условие, блокировавшее FDA pre-probe при `advance_on_timeout=true`.
2. В `permissions_v2.order` шаг `full_disk_access` перенесён выше (сразу после `screen_capture`).

## Why
- Ранее FDA pre-probe мог не запускаться в одном из рабочих режимов orchestrator.
- FDA шаг шёл слишком поздно, после длинной цепочки запросов, что создавало UX-эффект «в списке нет Nexy».

## Verification
- Проверен diff и наличие новой позиции шага в `unified_config.yaml`.
- Проверено, что pre-probe FDA больше не зависит от `advance_on_timeout`.

## Информация об изменениях
- Что изменено:
  - Исправлено условие FDA pre-probe в orchestrator.
  - Изменён порядок шага Full Disk Access в first-run.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/permissions/v2/orchestrator.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/config/unified_config.yaml`
- Причина/цель изменений:
  - Обеспечить предсказуемое появление `Nexy` в Full Disk Access и сократить путаницу во время first-run.
- Проверка:
  - Выполнена статическая проверка изменённых участков и конфигурации порядка шагов.
