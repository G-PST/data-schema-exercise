# G-PST Data Schema Information Sheets

This repository collects **data schema information sheets** for power systems
planning tools.  Sheets are filled-out YAML files that describe each tool's
data model, design decisions, real-world usage, and interoperability posture.
They will be used for cross-project comparison at the
**G-PST Power System Planning Interoperability Data Schema Workshop**.

---

## Repository Layout

```
template_data_schema_sheet.yaml   ← master template (do not edit)
data_schemas/                     ← one YAML per tool (filled-out sheets)
  sienna_data_model.yaml
  genx_data_model.yaml
  grid_data_model.yaml
  common_energy_system_model.yaml
  pypsa_data_model.yaml
  encoord_data_model.yaml
  cim_entso_e.yaml
.github/
  workflows/lint.yml              ← CI: yamllint on every PR
  ISSUE_TEMPLATE/new_tool_schema.md
```

---

## How to Fill Out Your Sheet

You will need a GitHub account.  Choose the option that fits your access level.

### Option A — Fork & Pull Request (external contributors)

1. **Fork** this repository (click _Fork_ at the top-right of the GitHub page).
2. In your fork, copy the template to a new file inside `data_schemas/`:

   ```bash
   cp template_data_schema_sheet.yaml data_schemas/<tool_name>.yaml
   ```

   Use a short, lowercase, underscore-separated filename
   (e.g., `my_tool_data_model.yaml`).

3. Open the new file and replace every `<...>` placeholder with real
   information.  Use `~` (YAML null) for fields that don't apply.

4. Commit and push to your fork, then open a **Pull Request** targeting the
   `main` branch of this repository.  Title it:
   `Add data schema sheet: <Tool Name>`.

### Option B — Branch & Pull Request (contributors with write access)

1. Create a new branch from `main`:

   ```bash
   git checkout main && git pull
   git checkout -b add-schema/<tool-name>
   ```

2. Copy and edit the template:

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

### What Happens Next

* A maintainer will review your sheet and may ask questions via PR comments.
* Address comments by pushing additional commits to the same branch/fork.
* Once approved, the sheet is merged into `main`.

> **Note:** Direct pushes to `main` are not permitted.
> All changes must go through a Pull Request.

---

## YAML Linting

Every pull request is automatically checked with
[yamllint](https://yamllint.readthedocs.io/).  To run the lint check locally
before pushing:

```bash
pip install yamllint
yamllint -c .yamllint.yaml data_schemas/<tool_name>.yaml
```

---

## Adding a New Tool

If you want to add a tool that isn't already listed, open a new issue using
the **Add New Tool Data Schema** template and follow the instructions there.

---

## Current Schemas

| File | Tool |
|------|------|
| `data_schemas/sienna_data_model.yaml` | Sienna Data Model |
| `data_schemas/genx_data_model.yaml` | GenX Data Model |
| `data_schemas/grid_data_model.yaml` | Grid Data Model |
| `data_schemas/common_energy_system_model.yaml` | CommonEnergySystemModel |
| `data_schemas/pypsa_data_model.yaml` | PyPSA Data Model |
| `data_schemas/encoord_data_model.yaml` | Encoord Data Model |
| `data_schemas/cim_entso_e.yaml` | CIM/ENTSO-E |
