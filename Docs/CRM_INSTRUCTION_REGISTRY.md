# CRM Instruction Registry

**Version:** 1.0.0
**Master Standard:** [CRM_MASTER_INSTRUCTION.md](./CRM_MASTER_INSTRUCTION.md)

This registry acts as the **Index** for all valid instructions in the project. The CRM system uses these IDs to link tasks to standard operating procedures.

## 📜 Registry Contract
The `kanban_progress_collector.py` script relies on the exact format of the table below:
1.  **Registry ID**: Must be in the first column. Supports both **Bold** (`**INS-XXX**`) and Plain (`INS-XXX`) formats.
2.  **File Path**: Must be a markdown link `[Title](./Path.md)` relative to `Docs/`.

## Core Processes

| Registry ID | Title | File Path | Description |
|:---|:---|:---|:---|
| **INS-001** | **Master Standard** | [CRM_MASTER_INSTRUCTION.md](./CRM_MASTER_INSTRUCTION.md) | Defines the structure for all other docs. |
| **INS-002** | **Packaging Guide** | [PACKAGING_FINAL_GUIDE.md](./PACKAGING_FINAL_GUIDE.md) | Standard macOS packaging (DMG/PKG) workflow. |
| **INS-003** | **Pre-Flight Check** | [PRE_PACKAGING_VERIFICATION.md](./PRE_PACKAGING_VERIFICATION.md) | Checklist before starting a build. |
| **INS-004** | **Release Testing** | [RELEASE_TESTING_GUIDE.md](./RELEASE_TESTING_GUIDE.md) | QA checklist for release candidates. |
| **INS-005** | **Architecture Overview** | [ARCHITECTURE_OVERVIEW.md](./ARCHITECTURE_OVERVIEW.md) | High-level system design key. |
| **INS-006** | **Kanban Development** | [PROJECT_KANBAN.html](./PROJECT_KANBAN.html) | The CRM/Kanban tool itself (Self-hosted). |
| **INS-007** | Deployment Checklist | [DEPLOY_CHECKLIST.md](./DEPLOY_CHECKLIST.md) | Step-by-step deployment verification (Progress Test). |
| **INS-008** | Assistant Instructions | [CRM_ASSISTANT_INSTRUCTIONS.md](./CRM_ASSISTANT_INSTRUCTIONS.md) | How AI assistants create/manage tasks |

## Task Templates
| Registry ID | Title | Template Source | Usage |
|:------------|:------|:----------------|:------|
| **TPL-BUG** | **Bug Report** | Use Master Format | For reporting defects. |
| **TPL-FEAT** | **Feature Spec** | Use Master Format | For planning new features. |

## Change Log
- **2026-01-05**: Registry initialized. Added contract definition.
