---
name: Add New Tool Data Schema
about: >
  Use this template to add a data schema information sheet for a tool that is
  not yet represented in this repository.
title: "Add data schema sheet: <Tool Name>"
labels: new-schema
assignees: ""
---

## Tool Information

**Tool / Schema Name:** <!-- e.g., MyTool Data Model -->
**Organization / Maintainer:** <!-- e.g., NREL, Princeton, OET -->
**Repository:** <!-- https://github.com/... -->

---

## Instructions for the Tool Owner

Please create a new YAML sheet for your tool and submit a Pull Request.  Pick
the option below that fits your access level.

### Option A — Fork & Pull Request (external contributors)

1. **Fork** this repository (click _Fork_ at the top-right of the page).
2. In your fork, copy the template to a new file in `data_schemas/`:
   ```bash
   cp template_data_schema_sheet.yaml data_schemas/<tool_name>.yaml
   ```
   Use a short, lowercase, underscore-separated filename
   (e.g., `my_tool_data_model.yaml`).
3. Open the new file and replace every `<...>` placeholder with real values.
   Use `~` (YAML null) for fields that don't apply.
4. Commit and push to your fork, then open a **Pull Request** targeting `main`.
   Title it: `Add data schema sheet: <Tool Name>`.
5. Link this issue in your PR description.

### Option B — Branch & Pull Request (contributors with write access)

1. Create a new branch from `main`:
   ```bash
   git checkout main && git pull
   git checkout -b add-schema/<tool-name>
   ```
2. Copy and fill in the template:
   ```bash
   cp template_data_schema_sheet.yaml data_schemas/<tool_name>.yaml
   # edit data_schemas/<tool_name>.yaml
   ```
3. Commit, push, and open a Pull Request targeting `main`:
   ```bash
   git add data_schemas/<tool_name>.yaml
   git commit -m "Add data schema sheet: <Tool Name>"
   git push origin add-schema/<tool-name>
   ```
4. Link this issue in your PR description.

### After Opening the PR

- A maintainer will review your sheet and may leave questions as PR comments.
- Address comments by pushing additional commits to the same branch/fork.
- Once approved the sheet is merged and this issue is closed.

### YAML Linting

CI will lint your file automatically.  To check locally before pushing:

```bash
pip install yamllint
yamllint -c .yamllint.yaml data_schemas/<tool_name>.yaml
```

---

_Questions?  Comment on this issue._

