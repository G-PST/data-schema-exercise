---
name: Fill Out Existing Tool Data Schema Sheet
about: >
  Use this template to track filling out the data schema information sheet
  for a tool that already has a placeholder YAML in this repository.
title: "Fill out data schema sheet: <Tool Name>"
labels: fill-out-schema
assignees: ""
---

## Tool

**Tool / Schema Name:** <!-- e.g., Sienna Data Model -->
**YAML file:** <!-- e.g., data_schemas/sienna_data_model.yaml — link to the file above -->
**Assigned to:** <!-- @github-handle of the person responsible -->

---

## Instructions for the Tool Owner

Your tool already has a placeholder YAML file in `data_schemas/`.  Please fill
it out and submit a Pull Request.  Pick the option below that fits your access
level.

### Option A — Fork & Pull Request (external contributors)

1. **Fork** this repository (click _Fork_ at the top-right of the page).
2. In your fork, open the file listed above (e.g.,
   `data_schemas/sienna_data_model.yaml`).
3. Replace every `<...>` placeholder with real information.
   Use `~` (YAML null) for fields that don't apply.
4. Commit your changes and push them to your fork.
5. Open a **Pull Request** from your fork back to the `main` branch of this
   repository.  Title it: `Fill out data schema sheet: <Tool Name>`.
6. Link this issue in your PR description (paste the issue URL).

### Option B — Branch & Pull Request (contributors with write access)

1. Create a new branch from `main`:
   ```bash
   git checkout main && git pull
   git checkout -b fill-schema/<tool-name>
   ```
2. Edit the placeholder file:
   ```bash
   # e.g., open data_schemas/sienna_data_model.yaml in your editor
   ```
3. Replace every `<...>` placeholder, then commit and push:
   ```bash
   git add data_schemas/<tool_name>.yaml
   git commit -m "Fill out data schema sheet: <Tool Name>"
   git push origin fill-schema/<tool-name>
   ```
4. Open a **Pull Request** on GitHub targeting `main`.
   Link this issue in your PR description.

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
