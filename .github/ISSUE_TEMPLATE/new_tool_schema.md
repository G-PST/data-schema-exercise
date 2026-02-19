---
name: Add New Tool Data Schema
about: Request to add a new power systems planning tool data schema information sheet
title: "Add data schema sheet: <Tool Name>"
labels: new-schema
assignees: ""
---

## Tool Information

**Tool / Schema Name:** <!-- e.g., MyTool Data Model -->
**Organization / Maintainer:** <!-- e.g., NREL, Princeton, OET -->
**Repository:** <!-- https://github.com/... -->

## Instructions for the Tool Owner

Thank you for contributing to the G-PST Power System Planning Interoperability
Data Schema Workshop!  Please follow the steps below to fill out and submit
your data schema information sheet.

### Option A — Fork & Pull Request (recommended for external contributors)

1. **Fork** this repository using the _Fork_ button at the top right of the
   GitHub page.
2. In your fork, copy the template file to a new file in `data_schemas/`:
   ```
   cp template_data_schema_sheet.yaml data_schemas/<tool_name>.yaml
   ```
   Use a short, lowercase, underscore-separated name (e.g.,
   `my_tool_data_model.yaml`).
3. Open `data_schemas/<tool_name>.yaml` in your editor and fill in every
   field.  Replace all angle-bracket placeholders `<...>` with real values.
   Use `~` (YAML null) for fields that don't apply.
4. Commit your changes and push them to your fork.
5. Open a **Pull Request** from your fork back to the `main` branch of this
   repository.  Use the PR title `Add data schema sheet: <Tool Name>`.

### Option B — Branch & Pull Request (for contributors with write access)

1. Create a new branch from `main`:
   ```
   git checkout main
   git pull
   git checkout -b add-schema/<tool-name>
   ```
2. Copy the template:
   ```
   cp template_data_schema_sheet.yaml data_schemas/<tool_name>.yaml
   ```
3. Fill in your YAML file, commit, and push the branch:
   ```
   git add data_schemas/<tool_name>.yaml
   git commit -m "Add data schema sheet: <Tool Name>"
   git push origin add-schema/<tool-name>
   ```
4. Open a **Pull Request** on GitHub targeting the `main` branch.

### After Opening the PR

- A maintainer will review your sheet and may leave comments or questions
  directly on the PR.
- Address any comments by pushing additional commits to the same branch/fork.
- Once approved, your sheet will be merged into `main` and stored in the
  `data_schemas/` folder.

### YAML Linting

A CI check will automatically lint your YAML file when you open the PR.
You can run it locally before pushing:

```bash
pip install yamllint
yamllint -c .yamllint.yaml data_schemas/<tool_name>.yaml
```

---

_If you have any questions, feel free to comment on this issue._
