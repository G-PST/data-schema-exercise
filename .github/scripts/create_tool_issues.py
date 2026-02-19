#!/usr/bin/env python3
"""Create one GitHub issue per tool in the data-schema-excercise repository.

This script is idempotent: it checks whether an open issue with the expected
title already exists before creating a new one.  Run it via the companion
GitHub Actions workflow, or locally (requires the ``gh`` CLI and a token
with ``issues: write`` permission):

    python3 .github/scripts/create_tool_issues.py
"""

import json
import os
import subprocess
import sys
import tempfile

REPO = "G-PST/data-schema-excercise"
BASE_URL = "https://github.com/G-PST/data-schema-excercise"
INSTRUCTIONS_URL = (
    f"{BASE_URL}/blob/main/.github/ISSUE_TEMPLATE/fill_out_schema.md"
)

# (Display name, YAML filename) for every tool in data_schemas/
TOOLS = [
    ("Sienna Data Model",        "sienna_data_model.yaml"),
    ("GenX Data Model",          "genx_data_model.yaml"),
    ("Grid Data Model",          "grid_data_model.yaml"),
    ("CommonEnergySystemModel",  "common_energy_system_model.yaml"),
    ("PyPSA Data Model",         "pypsa_data_model.yaml"),
    ("Encoord Data Model",       "encoord_data_model.yaml"),
    ("CIM/ENTSO-E",              "cim_entso_e.yaml"),
]


def gh(*args):
    """Run a ``gh`` CLI command and return the CompletedProcess."""
    return subprocess.run(["gh"] + list(args), capture_output=True, text=True)


def ensure_label():
    """Create the ``fill-out-schema`` label if it does not already exist."""
    r = gh(
        "label", "create", "fill-out-schema",
        "--repo", REPO,
        "--color", "0075ca",
        "--description", "Fill out existing tool data schema sheet",
        "--force",
    )
    if r.returncode != 0:
        print(f"Warning: could not create label: {r.stderr}", file=sys.stderr)


def issue_exists(title):
    """Return True if an open issue with this title already exists."""
    r = gh(
        "issue", "list",
        "--repo", REPO,
        "--state", "open",
        "--json", "title",
        "--limit", "100",
    )
    if r.returncode != 0:
        return False
    issues = json.loads(r.stdout or "[]")
    return any(i["title"] == title for i in issues)


def build_body(tool_name, yaml_file):
    """Return the Markdown body for the issue."""
    yaml_url = f"{BASE_URL}/blob/main/data_schemas/{yaml_file}"
    branch_name = yaml_file.replace(".yaml", "")

    return f"""\
## Tool

**Tool / Schema Name:** {tool_name}
**YAML file:** [`data_schemas/{yaml_file}`]({yaml_url})

---

## Background

This repository collects **data schema information sheets** for power systems
planning tools used for cross-project comparison at the
**G-PST Power System Planning Interoperability Data Schema Workshop**.

A placeholder YAML file for **{tool_name}** already exists at
`data_schemas/{yaml_file}`. Please fill it out and open a Pull Request.

---

## Instructions

Full step-by-step instructions are in
[`fill_out_schema.md`]({INSTRUCTIONS_URL}).

### Quick Summary

1. Open [`data_schemas/{yaml_file}`]({yaml_url}).
2. Replace every `<...>` placeholder with real information.
3. Use `~` (YAML null) for any fields that do not apply.
4. Validate locally (see **Validation** below).
5. Open a Pull Request targeting `main` and link this issue in the description.

### File Location and Naming Convention

- **File to edit:** `data_schemas/{yaml_file}`
- Keep the existing filename — do not rename it.
- The file lives in the `data_schemas/` directory at the repository root.

### Required Sections

All sections in the YAML must be addressed:

| Section | Key Fields |
|---------|------------|
| `identity` | schema_name, organization, maintainers, repository, documentation, license, version, maturity |
| `summary` | description, modeling_domains_supported, what_does_it_NOT_cover, data_captured, conceptual_structure |
| `design` | key_decisions, schema_format, implementation_languages, interoperability, units_handling, validation_approach, governance |
| `usage` | tools_built_on_schema, largest_real_world_dataset, who_is_using_it, data_available |
| `challenges` | known_limitations, hardest_problems_encountered |
| `interoperability` | areas_of_overlap_with_other_schemas, what_would_convergence_require, biggest_thing_others_should_know |
| `card_metadata` | prepared_by, date |

### Validation

Run `yamllint` locally before pushing:

```bash
pip install yamllint
yamllint -c .yamllint.yaml data_schemas/{yaml_file}
```

CI will also lint your file automatically when you open a PR.

### Opening a Pull Request

**External contributors (Fork & PR):**
1. Fork this repository.
2. Edit `data_schemas/{yaml_file}` in your fork.
3. Open a PR to `main` titled: `Fill out data schema sheet: {tool_name}`.
4. Paste this issue's URL in the PR description.

**Contributors with write access (Branch & PR):**

```bash
git checkout main && git pull
git checkout -b fill-schema/{branch_name}
# Edit data_schemas/{yaml_file}
git add data_schemas/{yaml_file}
git commit -m "Fill out data schema sheet: {tool_name}"
git push origin fill-schema/{branch_name}
```

Then open a PR on GitHub targeting `main` and link this issue.

---

## Acceptance Criteria

- [ ] All `<...>` placeholders in `data_schemas/{yaml_file}` replaced with real content (or `~` where not applicable)
- [ ] `identity` section complete: schema_name, organization, maintainers, repository, license, version, maturity
- [ ] `summary` section describes what the schema covers **and** what it does NOT cover
- [ ] `design` section covers key decisions, schema format, and implementation languages
- [ ] `usage` section includes real-world datasets and known users
- [ ] `challenges` section lists known limitations
- [ ] `interoperability` section addresses overlap with other schemas in this comparison
- [ ] `card_metadata` filled in (prepared_by, date)
- [ ] `yamllint` passes locally with no errors
- [ ] Pull Request opened targeting `main` with this issue linked in the PR description
- [ ] PR reviewed and merged by a maintainer

---

_Questions? Comment on this issue._
"""


def create_issue(tool_name, yaml_file):
    title = f"Fill out data schema sheet: {tool_name}"

    if issue_exists(title):
        print(f"Issue already exists for '{tool_name}', skipping.")
        return

    body = build_body(tool_name, yaml_file)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False
    ) as tmp:
        tmp.write(body)
        tmp_path = tmp.name

    try:
        r = gh(
            "issue", "create",
            "--repo", REPO,
            "--title", title,
            "--body-file", tmp_path,
            "--label", "fill-out-schema",
        )
        if r.returncode == 0:
            print(f"Created issue for '{tool_name}': {r.stdout.strip()}")
        else:
            print(
                f"ERROR creating issue for '{tool_name}': {r.stderr}",
                file=sys.stderr,
            )
            sys.exit(1)
    finally:
        os.unlink(tmp_path)


def main():
    ensure_label()
    for tool_name, yaml_file in TOOLS:
        create_issue(tool_name, yaml_file)


if __name__ == "__main__":
    main()
