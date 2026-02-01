# CRM Master Instruction Standard

**Version:** 1.0.0
**Status:** Active
**Enforcement:** Mandatory
**Source of Truth:** [CRM_INSTRUCTION_REGISTRY.md](./CRM_INSTRUCTION_REGISTRY.md)

---

## 1. Purpose
This document defines the **single standard** for creating, updating, and executing instructions within the project. All technical tasks, bug fixes, and feature implementations must follow this structure to ensure compatibility with the CRM system.

## 2. Standard Document Structure
Every instructional document (Task Brief, Bug Report, Feature Spec) must contain the following sections:

### 2.1 Header
```markdown
# [Short Descriptive Title]
**Type:** [Task | Bug | Feature | Maintenance]
**Status:** [Draft | Active | Deprecated]
**Registry ID:** [ID from Registry, e.g., INS-001]
```

### 2.2 Diagnosis (The "Why")
Concise explanation of the current state or problem.
- **Observation:** What is happening?
- **Impact:** Why does it matter?

### 2.3 Root Cause
Technical explanation of why the issue exists or why the feature is needed.
- **Analysis:** Code-level or process-level reason.

### 2.4 Optimal Fix (The "What")
The primary solution strategy.
- **Goal:** What will be achieved.
- **Architecture Fit:** Does it follow MVC? Where does it belong?
- **Implementation Plan:** Step-by-step checklist.
- **Code Touchpoints:** List of files to change.

### 2.5 Verification (The "How")
How to prove the work is done (Definition of Done).
- **Steps:** Manual or automated tests.
- **Expected Result:** What success looks like.

---

## 3. Workflow Rules

1.  **Registry First:** Before creating a document, check [CRM_INSTRUCTION_REGISTRY.md](./CRM_INSTRUCTION_REGISTRY.md). If it doesn't exist, register it.
2.  **No Freestyle:** Do not create ad-hoc text files. Use this template.
3.  **CRM Link:** The `Registry ID` maps to the CRM Task ID or Tag.

## 4. Templating
Copy the source of this section to start a new document:

```markdown
# [Title]
**Type:** Task
**Registry ID:** [ID]

## Diagnosis
...

## Root Cause
...

## Optimal Fix
### Goal
...
### Plan
1. [ ] Step 1
2. [ ] Step 2

### Code Touchpoints
- path/to/file

## Verification
- [ ] Verify X
```
