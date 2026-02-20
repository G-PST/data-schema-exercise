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
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = "G-PST/data-schema-excercise"
BASE_URL = "https://github.com/G-PST/data-schema-excercise"

# Resolve the template path relative to this script's location.
_SCRIPT_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = _SCRIPT_DIR.parent / "ISSUE_TEMPLATE" / "fill_out_schema.md"

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


def _read_template():
    """Read the fill_out_schema.md template, stripping YAML front-matter."""
    text = TEMPLATE_PATH.read_text()
    # Remove YAML front-matter (everything between the opening and closing ---)
    text = re.sub(r"^---\n.*?\n---\n*", "", text, count=1, flags=re.DOTALL)
    return text


def build_body(tool_name, yaml_file):
    """Return the Markdown body for the issue.

    Reads the fill_out_schema.md template and fills in tool-specific values
    so that every issue contains the canonical instructions.
    """
    yaml_url = f"{BASE_URL}/blob/main/data_schemas/{yaml_file}"
    branch_name = yaml_file.replace(".yaml", "")
    # e.g. "sienna-data-model" for branch slug
    tool_slug = branch_name.replace("_", "-")

    body = _read_template()

    # Fill in the tool-specific header fields (replace HTML comment placeholders)
    body = body.replace(
        "<!-- e.g., Sienna Data Model -->",
        tool_name,
    )
    body = body.replace(
        "<!-- e.g., data_schemas/sienna_data_model.yaml — link to the file above -->",
        f"[`data_schemas/{yaml_file}`]({yaml_url})",
    )
    body = body.replace(
        "<!-- @github-handle of the person responsible -->",
        "",
    )

    # Replace generic <...> placeholder tokens with real values
    body = body.replace("<Tool Name>", tool_name)
    body = body.replace("<tool-name>", tool_slug)
    body = body.replace("<tool_name>", branch_name)

    return body


def create_issue(tool_name, yaml_file):
    title = f"{tool_name} - fill out data schema sheet"

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
