# G-PST Data Schema Information Sheets

This repository will be used to collect **data schema information sheets** for power systems
planning tools. These sheets are YAML (to be filled out by tool owners) that describe each tool's
data model, design decisions, real-world usage, and interoperability posture.
Once collected, these sheets will be used for cross-tool comparison at the upcoming
**G-PST Power System Planning Interoperability Data Schema Workshop**.

---

## Current Schemas

| Tool | YAML Sheet |
|------|-----------|
| Sienna Data Model | [`data_schemas/sienna_data_model.yaml`](data_schemas/sienna_data_model.yaml) |
| GenX Data Model | [`data_schemas/genx_data_model.yaml`](data_schemas/genx_data_model.yaml) |
| Grid Data Model | [`data_schemas/grid_data_model.yaml`](data_schemas/grid_data_model.yaml) |
| CommonEnergySystemModel | [`data_schemas/common_energy_system_model.yaml`](data_schemas/common_energy_system_model.yaml) |
| PyPSA Data Model | [`data_schemas/pypsa_data_model.yaml`](data_schemas/pypsa_data_model.yaml) |
| Encoord Data Model | [`data_schemas/encoord_data_model.yaml`](data_schemas/encoord_data_model.yaml) |
| CIM/ENTSO-E | [`data_schemas/cim_entso_e.yaml`](data_schemas/cim_entso_e.yaml) |

---

## How to Contribute

**If your tool is listed above:** find the GitHub issue for your tool in the
[Issues tab](https://github.com/G-PST/data-schema-excercise/issues), open the
linked YAML file, fill it out, and submit a Pull Request — the issue has
step-by-step instructions.

**If your tool is not listed:** open a new issue using the
[Add New Tool Data Schema](https://github.com/G-PST/data-schema-excercise/issues/new?template=new_tool_schema.md)
template and follow the instructions there.

All changes to `main` go through a Pull Request.  A CI check will
automatically lint your YAML when you open one.
