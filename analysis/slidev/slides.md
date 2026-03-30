---
theme: default
title: G-PST Data Schema Comparative Analysis
info: |
  A comparison of six power system data schemas submitted to the G-PST data-schema-exercise repository for the Workshop on Data Schema Approaches for Grid Planning Model Interoperability.
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Comparing Data Schema Across Common Grid Planning Models

A comparison comparison of six power system data schemas

<div class="abs-b mb-8 text-sm opacity-60">
Based on schema submissions to the G-PST data-schema-exercise repository for the Workshop on Data Schema Approaches for Grid Planning Model Interoperability.
</div>

---
layout: two-cols
layoutClass: gap-4
---

# Schemas Compared

Six organizations submitted filled schema cards describing their data models for power system modeling.


- **CIM** — ENTSO-E
- **CESM** — G-PST
- **GenX** — Princeton / MIT
- **GDM** — NREL
- **PyPSA** — TU Berlin
- **SAInt** — encoord


::right::

<div class="mt-12">

| Schema | Maturity | License |
|--------|----------|---------|
| CIM | Production | Apache-2.0 |
| CESM | v0.1.0 | TBD |
| GenX | Production | GPL-2.0 |
| GDM | Active dev | BSD-3 |
| PyPSA | Production | MIT |
| SAInt | Production | Proprietary |

</div>

---

# What Each Schema Is

<div class="grid grid-cols-2 gap-3 text-xs">

<div class="border rounded-lg p-3 bg-blue-50">
<h4 class="text-blue-800 font-bold mb-1">CIM (ENTSO-E)</h4>
An international standard (IEC 61970/61968) profiled by ENTSO-E for cross-organization exchange of transmission grid models. Not a tool — a semantic contract enabling dozens of vendors and 40+ TSOs to share network data through CGMES profiles published as RDFS vocabularies with SHACL validation.
</div>

<div class="border rounded-lg p-3 bg-green-50">
<h4 class="text-green-800 font-bold mb-1">CESM (G-PST)</h4>
A tool-neutral data standard with a hub-and-spoke architecture. Defines energy system concepts (nodes, units, links, storage) in LinkML and provides bidirectional transformers to/from specific tools. Designed to eliminate point-to-point converters between modeling tools.
</div>

<div class="border rounded-lg p-3 bg-purple-50">
<h4 class="text-purple-800 font-bold mb-1">GenX (Princeton/MIT)</h4>
A capacity expansion planning tool where the data model is inseparable from the solver. Resources are Julia structs wrapping dictionaries, with CSV inputs and YAML settings. The schema exists to serve GenX's optimization, not as a standalone exchange format.
</div>

<div class="border rounded-lg p-3 bg-orange-50">
<h4 class="text-orange-800 font-bold mb-1">GDM (NREL)</h4>
A Python package providing Pydantic-validated data models specifically for distribution systems. Acts as the single source of truth for the NREL Distribution Suite — solving code duplication, unit confusion, and the lack of cross-object validation in CIM at the distribution level.
</div>

<div class="border rounded-lg p-3 bg-red-50">
<h4 class="text-red-800 font-bold mb-1">PyPSA (TU Berlin)</h4>
A Python energy system modeling framework where the data model is the tool's internal representation. Components live in Pandas DataFrames (static attributes) and dicts-of-DataFrames (time series). Currently migrating to Pydantic/Pandera for stricter validation.
</div>

<div class="border rounded-lg p-3 bg-teal-50">
<h4 class="text-teal-800 font-bold mb-1">SAInt (encoord)</h4>
A commercial integrated planning platform where networks are directed graphs of typed objects. Uniquely separates the physical 'what' (network structure) from the mathematical 'how' (scenarios, solutions), enabling the same grid to be analyzed across capacity expansion, production cost, and AC power flow.
</div>

</div>

---

# Domain Coverage Compared

<div class="grid grid-cols-2 gap-3 text-xs">

<div class="border-l-4 border-blue-500 pl-3 mb-2">
<strong>CIM:</strong> Transmission grid modeling and exchange. Covers equipment, topology, steady-state, dynamics, diagrams. Does NOT cover market optimization, simulation internals, or distribution detail.
</div>

<div class="border-l-4 border-green-500 pl-3 mb-2">
<strong>CESM:</strong> Multi-energy capacity expansion and production cost. Covers electricity, gas, heat, hydrogen, storage, investment. Does NOT cover AC/DC power flow, dynamics, or distribution.
</div>

<div class="border-l-4 border-purple-500 pl-3 mb-2">
<strong>GenX:</strong> Electricity capacity expansion with unit commitment. Covers zonal/DC-OPF networks, renewables, storage, H₂, CCS, policy constraints. Does NOT cover AC power flow, gas/heat, or distribution.
</div>

<div class="border-l-4 border-orange-500 pl-3 mb-2">
<strong>GDM:</strong> Distribution systems only. Covers bus-branch topology, transformers, DERs, battery storage, load profiles, equipment catalogs. Does NOT cover transmission, dynamics, or capacity expansion.
</div>

<div class="border-l-4 border-red-500 pl-3 mb-2">
<strong>PyPSA:</strong> Broadest domain coverage. Capacity expansion, LOPF, AC/DC power flow, sector coupling, storage, UC. Does NOT cover distribution detail, imperfect competition, or endogenous learning.
</div>

<div class="border-l-4 border-teal-500 pl-3 mb-2">
<strong>SAInt:</strong> Multi-energy integrated planning. Covers capacity expansion, production cost, AC power flow, gas hydraulics. Does NOT cover electromagnetic transients (phasor/EMT).
</div>

</div>

---

# Domain Coverage Matrix

<div class="overflow-x-auto">

| Domain | CIM | CESM | GenX | GDM | PyPSA | SAInt |
|--------|:---:|:----:|:----:|:---:|:-----:|:-----:|
| Capacity Expansion | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ |
| Production Cost / UC | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ |
| AC Power Flow | 🟡 | ❌ | ❌ | 🟡 | ✅ | ✅ |
| DC-OPF / LOPF | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ |
| Dynamic / Transient | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Distribution | 🟡 | ❌ | ❌ | ✅ | ❌ | ❌ |
| Multi-Sector Coupling | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ |
| Storage | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Transmission / Network | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gas / Hydraulic | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ |

</div>

<div class="mt-4 text-xs text-gray-500">
✅ Supported &nbsp;&nbsp; 🟡 Partial &nbsp;&nbsp; ❌ Not covered &nbsp;&nbsp; (AI-assessed from submissions)
</div>

---

# Conceptual Structure

<div class="grid grid-cols-2 gap-4 text-xs">

<div>

### CIM
**Profile-based semantic graph.** Objects are RDF resources linked by typed relationships. Data partitioned into profiles (EQ, TP, SSH, SV, DY) connected through persistent mRID identifiers. Fundamentally a graph, not tables.

### CESM
**Entity-relationship with graph-like topology.** Nodes (Balance, Storage, Commodity) connected via Links and Units through typed Ports. Uses LinkML mixins (HasFlow, HasInvestments) for shared behaviors.

### GenX
**Component-based type hierarchy.** All resources subtype AbstractResource (Thermal, Vre, Hydro, Storage, etc.). Julia's multiple dispatch selects constraint logic per type. Internally dictionary-backed for flexibility.

</div>

<div>

### GDM
**Three-layer hybrid:** Pydantic-validated components → bus-based topology → NetworkX graph for analysis. Explicit phase modeling (A, B, C, N, S1, S2). Container hierarchy: DistributionSystem → Substation → Feeder.

### PyPSA
**Bus-centric component model in tabular form.** Static attributes in one DataFrame per component type, time-varying in snapshot-indexed DataFrames. Buses are nodes, branches are edges.

### SAInt
**Directed graph of typed elementary objects** (nodes, branches, externals) with inheritance. Clear separation: network holds physical structure, scenarios hold simulation parameters, solutions hold results.

</div>

</div>

---

# Structural Patterns

<div class="overflow-x-auto text-sm">

| Pattern | CIM | CESM | GenX | GDM | PyPSA | SAInt |
|---------|:---:|:----:|:----:|:---:|:-----:|:-----:|
| Component-based | | ✅ | ✅ | ✅ | ✅ | |
| Bus-based | | | | ✅ | ✅ | |
| Graph / Network | ✅ | ✅ | | ✅ | | ✅ |
| Tabular | | | ✅ | | ✅ | |
| Object-oriented | ✅ | | ✅ | ✅ | | ✅ |
| Entity-Relationship | | ✅ | | | | |
| Profile-based | ✅ | | | | | |
| Hierarchical | | | | ✅ | | |

</div>

<div class="mt-4 text-xs text-gray-500">
Each schema combines multiple patterns. CIM is unique in its profile-based partitioning; GDM is unique in its hierarchical container model.
</div>

---

# Design Philosophy

<div class="grid grid-cols-3 gap-3 text-xs">

<div class="border rounded p-3">
<h4 class="font-bold text-blue-700 mb-2">CIM</h4>

- Build on IEC international standard — reuse, not reinvent
- Modular profiles for different exchange contracts
- Machine-readable semantics (RDFS) + validation (SHACL)
- Persistent identity (mRID) for merging, versioning, continuity
- Tool-neutral — no vendor lock-in
</div>

<div class="border rounded p-3">
<h4 class="font-bold text-green-700 mb-2">CESM</h4>

- Specification separate from implementation
- Domain-agnostic — units convert energy/matter generically
- Methods make modeling choices explicit
- Single definition per concept (efficiency OR heat rate, not both)
- Hub-and-spoke: one interchange format, many tool translators
</div>

<div class="border rounded p-3">
<h4 class="font-bold text-purple-700 mb-2">GenX</h4>

- Dictionary-backed resource structs for maximum flexibility
- Multiple dispatch on resource types
- CSV input + YAML settings — accessible to non-programmers
- Optional features gated by settings flags
- Backward compatibility across versions
</div>

<div class="border rounded p-3">
<h4 class="font-bold text-orange-700 mb-2">GDM</h4>

- Pydantic V2 as schema foundation — types enforced at creation
- Equipment models separated from component models
- Explicit phase enums (not assumed balanced)
- Pint-based unit system — enforced dimensionality
- Cross-object validation catches errors data models can't
</div>

<div class="border rounded p-3">
<h4 class="font-bold text-red-700 mb-2">PyPSA</h4>

- Tabular format — easiest for users to work with
- Static/dynamic attribute split mirrors modeling needs
- Full backward compatibility maintained since v1.0
- Components organized per type, not per entity
- Bus-based topology with abstract composable components
</div>

<div class="border rounded p-3">
<h4 class="font-bold text-teal-700 mb-2">SAInt</h4>

- Separate 'what' (network) from 'how' (scenarios)
- Separate base results from derived results (lazy evaluation)
- Single network representation shared across all analysis types
- Vendor-controlled evolution — users extend via API, not schema
</div>

</div>

---

# Format, Units & Validation

<div class="text-xs">

| Schema | Schema Format | Units Approach | Validation |
|--------|--------------|----------------|------------|
| **CIM** | CIM/RDF/RDFS + SHACL | CIM semantic types | Declarative SHACL constraints — profile conformance, cardinality, associations, cross-profile consistency |
| **CESM** | LinkML → Pydantic | QUDT annotations per field | LinkML type checking + enum constraints + regex patterns; referential integrity left to runtime |
| **GenX** | Julia structs + CSV/YAML | Implicit in field names | File existence checks, column name validation, time series alignment, settings-dependent requirements |
| **GDM** | Pydantic V2 + JSON | Pint (enforced at runtime) | Multi-layer: Pydantic types → cross-object validators → system-level diagnostics → graph cycle detection |
| **PyPSA** | CSV/Pandas (→ Pydantic) | Documented, not enforced | Being overhauled: migrating to Pydantic + Pandera for schema structure, types, ranges, cross-field checks |
| **SAInt** | Proprietary | Built-in units library | Real-time blocking: invalid entries rejected as user edits; cross-field rules + graph consistency enforced continuously |

</div>

---

# Schema–Tool Coupling Spectrum

<div class="mt-12 relative h-48">
  <div class="absolute inset-x-0 top-16 h-3 bg-gradient-to-r from-blue-200 via-yellow-200 to-red-200 rounded-full"></div>
  <div class="absolute left-0 top-24 text-xs italic text-gray-500">← Exchange-oriented</div>
  <div class="absolute right-0 top-24 text-xs italic text-gray-500">Tool-coupled →</div>
  <div class="absolute left-[5%] top-6 text-center">
    <div class="w-12 h-12 rounded-full bg-blue-500 text-white flex items-center justify-center text-xs font-bold mx-auto">CIM</div>
    <div class="text-xs mt-1">Pure exchange</div>
  </div>
  <div class="absolute left-[22%] top-6 text-center">
    <div class="w-12 h-12 rounded-full bg-green-500 text-white flex items-center justify-center text-xs font-bold mx-auto">CESM</div>
    <div class="text-xs mt-1">Interchange hub</div>
  </div>
  <div class="absolute left-[42%] top-6 text-center">
    <div class="w-12 h-12 rounded-full bg-orange-500 text-white flex items-center justify-center text-xs font-bold mx-auto">GDM</div>
    <div class="text-xs mt-1">Data + validation</div>
  </div>
  <div class="absolute left-[55%] top-6 text-center">
    <div class="w-12 h-12 rounded-full bg-teal-500 text-white flex items-center justify-center text-xs font-bold mx-auto">SAInt</div>
    <div class="text-xs mt-1">Data + tool logic</div>
  </div>
  <div class="absolute left-[78%] top-6 text-center">
    <div class="w-12 h-12 rounded-full bg-purple-500 text-white flex items-center justify-center text-xs font-bold mx-auto">GenX</div>
    <div class="text-xs mt-1">Tool IS schema</div>
  </div>
  <div class="absolute left-[90%] top-6 text-center">
    <div class="w-12 h-12 rounded-full bg-red-500 text-white flex items-center justify-center text-xs font-bold mx-auto">PyPSA</div>
    <div class="text-xs mt-1">Tool IS schema</div>
  </div>
</div>

---

# What Tool Coupling Means in Practice

<div class="text-sm">

| Schema | Coupling Level | What this means |
|--------|---------------|-----------------|
| **CIM** | Exchange-only | Defines how organizations share data, not how tools work internally. Pure semantic contract. |
| **CESM** | Interchange hub | Tool-neutral specification with bidirectional translators to specific tools. Schema and tools evolve independently. |
| **GDM** | Data-first, opinionated | Pydantic models with built-in validation logic and unit enforcement. Data package with "smart" behavior. |
| **SAInt** | Data with tool conventions | Vendor-controlled schema with some built-in analysis logic. Users extend via API, not schema modification. |
| **GenX** | Tool IS the schema | Julia structs serve the optimizer; data model can't be meaningfully separated from the solver logic. |
| **PyPSA** | Tool IS the schema | Pandas DataFrames are both the data model and the runtime representation. Inseparable from the framework. |

</div>

---

# Hardest Problems Encountered

<div class="grid grid-cols-2 gap-3 text-xs">

<div class="border-l-4 border-blue-500 pl-3 mb-3">
<strong class="text-blue-700">CIM:</strong> Not defining classes, but achieving stable interoperability across 40+ organizations and dozens of software products. Semantic web standards (RDF, SHACL, SPARQL) created a learning barrier, but the payoff in machine-checkable validation proved worth it.
</div>

<div class="border-l-4 border-green-500 pl-3 mb-3">
<strong class="text-green-700">CESM:</strong> Designing a schema generic enough for multiple energy carriers and tools without losing semantic precision. The breakthrough was 'explicit methods' — enumerations that make modeling choices visible rather than burying them in implicit tool behavior.
</div>

<div class="border-l-4 border-purple-500 pl-3 mb-3">
<strong class="text-purple-700">GenX:</strong> Balancing dictionary-backed flexibility against type safety and validation. Maintaining backward compatibility as new resource types (H₂, CCS, VRE-storage) and policy modules are added.
</div>

<div class="border-l-4 border-orange-500 pl-3 mb-3">
<strong class="text-orange-700">GDM:</strong> Cross-object validation that CIM cannot enforce — like ensuring three-phase loads only connect to three-phase buses. Matrix impedance representation with careful unit conversion and numerical stability.
</div>

<div class="border-l-4 border-red-500 pl-3 mb-3">
<strong class="text-red-700">PyPSA:</strong> Supporting many different use cases with a single data model while maintaining strict backward compatibility since v1.0. The tabular format sometimes fights against naturally graph-structured network data.
</div>

<div class="border-l-4 border-teal-500 pl-3 mb-3">
<strong class="text-teal-700">SAInt:</strong> Bringing together data from different tools into one coherent dataset for integrated planning. The biggest challenge is surprisingly mundane: naming conventions and data availability, even within the same organization.
</div>

</div>

---

# Where Schemas Overlap & Differ

<div class="text-xs">

| Pair | Relationship |
|------|-------------|
| **CIM ↔ CESM** | Complementary: CIM provides semantic vocabulary, CESM provides tool interchange. CESM cites CIM as complementary rather than competing. |
| **CIM ↔ GDM** | GDM was inspired by CIM but found CIM's distribution coverage insufficient for cross-object validation (e.g., phase consistency). |
| **CIM ↔ SAInt** | Both model transmission networks, but CIM is exchange-only while SAInt is an integrated analysis platform with its own network representation. |
| **CESM ↔ GenX** | CESM includes a GenX transformer. Overlap in resource components and capacity expansion concepts, but GenX is solver-specific. |
| **CESM ↔ PyPSA** | CESM includes a PyPSA transformer. Both cover capacity expansion and sector coupling, but PyPSA's model is tool-internal. |
| **GenX ↔ PyPSA** | Similar component-based resource abstractions for capacity expansion. Both tightly coupled to their solvers. Both say convergence requires translators. |
| **GDM ↔ others** | Minimal direct overlap — GDM is distribution-focused while others target transmission/planning. Potential bridge between transmission schemas and distribution tools. |
| **SAInt ↔ others** | SAInt's integrated model (one network, multiple analysis types) represents what convergence might look like. Closest to CESM's vision but vendor-controlled. |

</div>

---

# What Would Convergence Require?

<div class="grid grid-cols-2 gap-3 text-xs">

<div class="border rounded p-3 bg-blue-50">
<h4 class="text-blue-800 font-bold mb-1">CIM</h4>
Agreement on canonical identity management, topology semantics, equipment parameters, and profile boundaries. Any common layer must preserve stable identifiers, profile modularity, explicit semantics, and machine-checkable validation.
</div>

<div class="border rounded p-3 bg-green-50">
<h4 class="text-green-800 font-bold mb-1">CESM</h4>
CESM's hub-and-spoke is designed for this — convergence mainly requires agreeing on common entity naming/taxonomy and ensuring core concepts map cleanly. Explicit methods and single-definition-per-concept principles should be considered.
</div>

<div class="border rounded p-3 bg-purple-50">
<h4 class="text-purple-800 font-bold mb-1">GenX</h4>
A common resource type taxonomy and attribute naming convention. Standardized time series formats. Agreement on unit conventions. GenX's flexible dictionary model could adapt via translation wrappers.
</div>

<div class="border rounded p-3 bg-orange-50">
<h4 class="text-orange-800 font-bold mb-1">GDM</h4>
Mapping GDM's distribution hierarchy to a broader schema without losing cross-object validation depth. Pint-based units and Pydantic type safety should be preserved in any common layer.
</div>

<div class="border rounded p-3 bg-red-50">
<h4 class="text-red-800 font-bold mb-1">PyPSA</h4>
Full backward compatibility must be maintained for existing users. Interoperability can most likely only be incorporated via translators — the data model is too integrated with the tool to change fundamentally.
</div>

<div class="border rounded p-3 bg-teal-50">
<h4 class="text-teal-800 font-bold mb-1">SAInt</h4>
A software-agnostic schema representing time-series scenario analysis across capacity expansion, production cost, AC power flow, and dynamic domains. Explicit translation contracts between a common layer and each tool.
</div>

</div>

---

# The One Thing Others Should Know

<div class="space-y-4 text-sm mt-4">

<div class="flex items-start gap-3">
<span class="text-2xl">🔵</span>
<div><strong>CIM:</strong> CIM/ENTSO-E is much more than a file format. Its value is shared semantics, profile contracts, persistent identity, and conformity governance that make cross-vendor interoperability work at continental scale.</div>
</div>

<div class="flex items-start gap-3">
<span class="text-2xl">🟢</span>
<div><strong>CESM:</strong> CESM is not a tool — it's a data standard with transformers. Its value is the interchange layer that lets different tools share datasets without custom point-to-point converters.</div>
</div>

<div class="flex items-start gap-3">
<span class="text-2xl">🟣</span>
<div><strong>GenX:</strong> GenX's data model is tightly coupled to its optimization engine. The schema is intentionally flexible (dictionary-backed) but validation is convention-based rather than enforced by a formal schema definition language.</div>
</div>

<div class="flex items-start gap-3">
<span class="text-2xl">🟠</span>
<div><strong>GDM:</strong> GDM's primary strength is built-in cross-object validation — "a three-phase load can only connect to a three-phase bus" is enforced at data creation time, not discovered at simulation time.</div>
</div>

<div class="flex items-start gap-3">
<span class="text-2xl">🔴</span>
<div><strong>PyPSA:</strong> <em>(Not provided in submission)</em></div>
</div>

<div class="flex items-start gap-3">
<span class="text-2xl">🔷</span>
<div><strong>SAInt:</strong> SAInt already implements what convergence would need at the data layer: a single network with a time-series scenario layer so capacity expansion, production cost, and AC power flow share one underlying model.</div>
</div>

</div>

---

# Five Themes for Convergence

<v-clicks>

### 1. Nobody wants one schema to rule them all
Every submission assumes translators/converters rather than replacement. The question is whether to converge on a hub (CESM's approach), a vocabulary (CIM's approach), or just mapping contracts.

### 2. Identity and naming are the hardest prerequisites
CIM's persistent mRID, CESM's explicit typing, SAInt's naming challenges — everyone agrees that agreeing on what things are called and how they're identified is the unglamorous prerequisite everything else depends on.

### 3. Validation approaches vary wildly — but all want more
From SHACL (CIM) to Pydantic (GDM) to "being overhauled" (PyPSA) — every team is investing in stricter validation. A shared validation layer could be common ground.

### 4. The tool-coupled schemas face the hardest convergence path
GenX and PyPSA are deeply integrated with their solvers. Both say convergence must come through translators, not schema changes. The tool-neutral schemas (CIM, CESM) have more flexibility to adapt.

### 5. Multi-energy is the emerging frontier
CESM, SAInt, and PyPSA already handle multiple energy carriers. CIM is transmission-focused, GDM is distribution-only, GenX is electricity-only. Sector coupling may drive convergence.

</v-clicks>

---

# Possible Convergence Pathways

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="border-2 border-blue-300 rounded-xl p-4">
<h3 class="text-blue-700 font-bold mb-2">1. Hub-and-spoke interchange</h3>
<p class="text-sm">CESM's approach: define a common interchange schema + bidirectional translators for each tool. Avoids N² point-to-point converters.</p>
</div>

<div class="border-2 border-green-300 rounded-xl p-4">
<h3 class="text-green-700 font-bold mb-2">2. Common vocabulary / taxonomy</h3>
<p class="text-sm">CIM's approach: agree on what things are called and what they mean, with machine-readable semantics. Tools keep internal models but speak a shared language.</p>
</div>

<div class="border-2 border-purple-300 rounded-xl p-4">
<h3 class="text-purple-700 font-bold mb-2">3. Layered convergence</h3>
<p class="text-sm">Start with the domains where schemas already overlap (transmission topology, generator parameters, time series). Expand outward to contested territory (distribution, multi-energy, dynamics).</p>
</div>

<div class="border-2 border-orange-300 rounded-xl p-4">
<h3 class="text-orange-700 font-bold mb-2">4. Shared validation service</h3>
<p class="text-sm">Build a common validation layer that any schema can use — independent of format. If everyone is investing in stricter validation anyway, pool the effort.</p>
</div>

</div>

---
layout: section
---

# Use Case Comparison
## The Same Grid, Six Ways

A simple 2-bus test system with a generator, transformer, and line — represented in each schema's native format

---

# The Test System

<div class="mt-4">

```
  ┌─────────────┐         ┌─────────────┐
  │   Bus 1      │── Line ──│   Bus 2      │
  │  (HV 230kV)  │         │  (LV 13.8kV) │
  └──────┬───────┘         └──────┬───────┘
         │                        │
    Generator               Transformer
   (100 MW Gas)            (230/13.8 kV)
```

</div>

<div class="grid grid-cols-3 gap-4 mt-6 text-sm">
<div class="border rounded p-3 bg-blue-50">

**Bus 1 (HV)**
- 230 kV nominal
- Generator connected
</div>
<div class="border rounded p-3 bg-green-50">

**Bus 2 (LV)**
- 13.8 kV nominal
- Transformer secondary
</div>
<div class="border rounded p-3 bg-purple-50">

**Links**
- 100 MW gas generator
- 50 km transmission line
- 230/13.8 kV transformer
</div>
</div>

---

# Bus Representation: CIM vs PyPSA

<div class="grid grid-cols-2 gap-4 text-xs">

<div>

### CIM (ENTSO-E)
```xml
<!-- RDF resource with persistent mRID -->
<cim:ConnectivityNode rdf:ID="_bus1">
  <cim:IdentifiedObject.mRID>
    550e8400-e29b-41d4-a716-446655440000
  </cim:IdentifiedObject.mRID>
  <cim:IdentifiedObject.name>Bus 1</...>
  <cim:ConnectivityNode.ConnectivityNodeContainer
    rdf:resource="#_substation1"/>
</cim:ConnectivityNode>

<cim:TopologicalNode rdf:ID="_tn1">
  <cim:TopologicalNode.BaseVoltage
    rdf:resource="#_bv230"/>
</cim:TopologicalNode>

<!-- Voltage defined in separate BaseVoltage -->
<cim:BaseVoltage rdf:ID="_bv230">
  <cim:BaseVoltage.nominalVoltage>
    230
  </cim:BaseVoltage.nominalVoltage>
</cim:BaseVoltage>
```

**Note:** Bus is split across profiles — `ConnectivityNode` (EQ), `TopologicalNode` (TP), `SvVoltage` (SV). Linked by persistent mRIDs.

</div>

<div>

### PyPSA
```python
# Single row in a Pandas DataFrame
network.add("Bus", "Bus 1",
    v_nom=230,      # kV (implicit)
    carrier="AC",
    x=0.0, y=0.0,   # coordinates
)

network.add("Bus", "Bus 2",
    v_nom=13.8,
    carrier="AC",
    x=50.0, y=0.0,
)
```

```
# Or equivalently as CSV:
# buses.csv
name,   v_nom, carrier, x,   y
Bus 1,  230,   AC,      0.0, 0.0
Bus 2,  13.8,  AC,      50,  0.0
```

**Note:** Buses are rows in a DataFrame. `v_nom` is nominal voltage — units implicit (always kV). No persistent identity beyond the string name.

</div>
</div>

---

# Bus Representation: GDM vs SAInt

<div class="grid grid-cols-2 gap-4 text-xs">

<div>

### GDM (NREL) — Pydantic
```python
from gdm import DistributionBus
from gdm.quantities import Voltage
from gdm.distribution.enums import (
    Phase, VoltageTypes
)

bus1 = DistributionBus(
    name="Bus1",
    voltage_type=VoltageTypes.LINE_TO_LINE,
    phases=[Phase.A, Phase.B, Phase.C],
    rated_voltage=Voltage(230, "kilovolt"),
    voltagelimits=[
        VoltageLimitSet(
            limit_type=LimitType.MIN,
            value=Voltage(230*0.9, "kilovolt")
        ),
        VoltageLimitSet(
            limit_type=LimitType.MAX,
            value=Voltage(230*1.1, "kilovolt")
        ),
    ],
    substation=substation,
    feeder=feeder,
    coordinate=Location(x=0.0, y=0.0),
)
```

**Note:** Explicit phases (A,B,C), enforced Pint units (`Voltage(230, "kilovolt")` — can't accidentally pass "ohms"), voltage limits built in. Bus must belong to a substation and feeder.

</div>

<div>

### SAInt (encoord)
```
# Electric Node (ENO) object
ENO.Bus1.Name = "Bus 1"
ENO.Bus1.VNOMDEF = 230  # kV
ENO.Bus1.Zone = "EZN1"
ENO.Bus1.Sub = "ESUB1"
ENO.Bus1.Lat = 0.0
ENO.Bus1.Lon = 0.0
# Voltage results are computed:
# ENO.Bus1.VM   (magnitude, pu)
# ENO.Bus1.VA   (angle, degrees)
```

**Note:** Node is a location in a directed graph. Properties split into `net-input` (static, set by user) and `derived-result` (computed by solver). Grouped via Zones (node-oriented) and Subs (branch-oriented).

</div>
</div>

---

# Bus Representation: GenX vs CESM

<div class="grid grid-cols-2 gap-4 text-xs">

<div>

### GenX (Princeton/MIT)
```julia
# GenX uses Zones, not individual buses
# Network.csv:
# Network_zones, ..., Hurdle_Rate
# z1,            ..., 0.0
# z2,            ..., 0.0

# Resources are assigned to zones:
resource = Thermal(Dict(
    :resource => "Gas_CC",
    :zone => 1,           # zone ID
    :existing_cap_mw => 100.0,
    # ... no bus-level detail
))
```

**Note:** GenX does NOT model individual buses. The network is zonal — generators and demands are assigned to zones. Transmission is modeled as inter-zonal transfer limits. This is a deliberate abstraction for capacity expansion planning where bus-level detail is unnecessary.

</div>

<div>

### CESM (G-PST)
```yaml
# LinkML Node definition
# (abstract - specialized by type)
BalanceNode:
  name: Bus1
  commodity: electricity
  # No voltage — CESM is energy-flow,
  # not power-flow

# Nodes connected via Links:
Link:
  name: Line1
  node_from: Bus1
  node_to: Bus2
  capacity: 200  # MW
  # No impedance — capacity-constrained
```

**Note:** CESM deliberately does NOT model voltage, impedance, or power flow. Nodes carry commodities (electricity, gas, heat). Network transfer is capacity-constrained linear flow. This is by design — CESM targets capacity expansion, not circuit analysis.

</div>
</div>

---

# Generator: Six Representations

<div class="text-xs overflow-y-auto" style="max-height: 420px;">

| Aspect | CIM | CESM | GenX | GDM | PyPSA | SAInt |
|--------|-----|------|------|-----|-------|-------|
| **Concept** | `GeneratingUnit` + `SynchronousMachine` | `Unit` with `ConversionMethod` | `Thermal` struct (dict-backed) | Not modeled (distribution focus) | `Generator` component | `FGEN` (Fuel Generator) |
| **Capacity** | `GeneratingUnit.maxOperatingP` (MW) | `capacity` field | `existing_cap_mw` key | N/A | `p_nom` (MW) | `PMAXDEF` (MW) |
| **Min power** | `GeneratingUnit.minOperatingP` | Not explicit | `min_power` fraction | N/A | `p_min_pu` (per-unit) | `PMINDEF` (MW) |
| **Fuel** | Separate `FuelType` entity | `commodity` input port | `fuel` key + `heat_rate_mmbtu_per_mwh` | N/A | `carrier` + `efficiency` | `FUEL` object (linked) |
| **Costs** | Not in CIM (market systems) | `marginal_cost` | `var_om_cost_per_mwh`, `inv_cost_per_mwyr` | N/A | `marginal_cost` (€/MWh) | `VOMPrice` ($/MWh) |
| **Ramp rates** | `GeneratingUnit.normalPF` | Not explicit | `ramp_up_percentage`, `ramp_dn_percentage` | N/A | `ramp_limit_up/down` | `RampUp/RampDown` (MW/min) |
| **Startup** | Not in CIM | `StartupMethod` enum | `start_cost_per_mw`, `up_time`, `down_time` | N/A | `start_up_cost` | `StartUpCost`, `MinUpTime` |
| **Location** | Via `Terminal` → `ConnectivityNode` | Via `Port` → `Node` | Via `zone` integer | Via bus reference | Via `bus` name | Via `Node` reference |
| **Units** | CIM semantic types | QUDT annotations | Implicit in field names | Pint enforced | Documented convention | Built-in units library |

</div>

<div class="mt-2 text-xs text-gray-500">
GDM focuses on distribution-level DERs (solar, battery), not bulk generation. CIM captures physical parameters, not costs.
</div>

---

# Transformer: Three That Model It

<div class="grid grid-cols-3 gap-3 text-xs">

<div class="border rounded p-3">

### CIM
```xml
<cim:PowerTransformer rdf:ID="_xfmr1">
  <cim:IdentifiedObject.name>
    Xfmr1
  </cim:IdentifiedObject.name>
</cim:PowerTransformer>

<!-- Separate winding objects -->
<cim:PowerTransformerEnd rdf:ID="_w1">
  <cim:TransformerEnd.Terminal
    rdf:resource="#_t_bus1"/>
  <cim:PowerTransformerEnd
    .ratedU>230</...>
  <cim:PowerTransformerEnd
    .ratedS>100</...>
  <cim:TransformerEnd.r>0.5</...>
  <cim:TransformerEnd.x>12.0</...>
</cim:PowerTransformerEnd>
```
Multiple objects: `PowerTransformer` + N `PowerTransformerEnd` + `TapChanger`

</div>

<div class="border rounded p-3">

### GDM
```python
DistributionTransformer(
  name="Xfmr1",
  buses=[bus_hv, bus_lv],
  winding_phases=[
    [Phase.A, Phase.B, Phase.C],
    [Phase.A, Phase.B, Phase.C],
  ],
  equipment=
    DistributionTransformerEquipment(
      name="xfmr_equip1",
      windings=[
        WindingEquipment(
          rated_voltage=Voltage(
            230, "kilovolt"),
          ...
        ),
      ]
    ),
)
```
Separates equipment (reusable specs) from component (instance in grid)

</div>

<div class="border rounded p-3">

### SAInt
```
TRF.Xfmr1.FromNode = "Bus1"
TRF.Xfmr1.ToNode   = "Bus2"
TRF.Xfmr1.VNOMHV   = 230   # kV
TRF.Xfmr1.VNOMLV   = 13.8  # kV
TRF.Xfmr1.SRATEDDEF = 100  # MVA
TRF.Xfmr1.RR = 0.005       # pu
TRF.Xfmr1.XX = 0.12        # pu
TRF.Xfmr1.TAPDEF = 1.0     # pu
TRF.Xfmr1.TAPMAXDEF = 1.1
TRF.Xfmr1.TAPMINDEF = 0.9
```
`FromNode` = HV side, `ToNode` = LV side (convention). Tap changer built into branch properties.

</div>

</div>

<div class="mt-4 text-xs">

**Not modeled:** CESM (no impedance), GenX (zonal abstraction), PyPSA — *wait, PyPSA does model transformers:*
```python
network.add("Transformer", "Xfmr1", bus0="Bus 1", bus1="Bus 2",
            type="230 MVA 230/13.8 kV", s_nom=100, tap_ratio=1.0)
```

</div>

---

# Transmission Line: Four Approaches

<div class="grid grid-cols-2 gap-4 text-xs">

<div class="border rounded p-3">

### CIM
```xml
<cim:ACLineSegment rdf:ID="_line1">
  <cim:Conductor.length>50</...>
  <cim:ACLineSegment.r>0.01</...>
  <cim:ACLineSegment.x>0.1</...>
  <cim:ACLineSegment.bch>0.02</...>
  <!-- Connected via Terminals -->
</cim:ACLineSegment>
```
Full pi-model parameters (R, X, B). Length in km. Connected via `Terminal` objects to `ConnectivityNode`s.

</div>

<div class="border rounded p-3">

### PyPSA
```python
network.add("Line", "Line1",
    bus0="Bus 1", bus1="Bus 2",
    s_nom=200,     # MVA
    length=50,     # km
    type="243-AL1/39-ST1A 220.0",
    # or specify directly:
    r=0.01, x=0.1, b=0.02,
)
```
Standard type library auto-fills R, X, B from line type. Units implicit (per-unit or Ω/km).

</div>

<div class="border rounded p-3">

### SAInt
```
LI.Line1.FromNode = "Bus1"
LI.Line1.ToNode   = "Bus2"
LI.Line1.LNDEF    = 50     # km
LI.Line1.RRDEF    = 0.01   # pu
LI.Line1.XXDEF    = 0.10   # pu
LI.Line1.BBDEF    = 0.02   # pu
LI.Line1.SRATEDDEF = 200   # MVA
```
Same directed-graph convention as transformers: `FromNode` → `ToNode`. Properties split into defaults and event-overridable.

</div>

<div class="border rounded p-3">

### GenX
```
# Network.csv (inter-zonal)
Network_Lines, z1, z2, Line_Max_Flow_MW,
  Line_Loss_Percentage, ...
1,             1,  2,  200,
  0.01,             ...
```
No R/X/B — just transfer limits (MW) and loss percentage between zones. Optionally DC-OPF with PTDF matrix.

</div>

</div>

<div class="mt-2 text-xs text-gray-500">
CESM: Uses abstract "Links" with capacity (MW) but no impedance. GDM: Models branches with full matrix or sequence impedance including phase coupling.
</div>

---

# Key Nuances Revealed by the Use Case

<div class="grid grid-cols-2 gap-4 text-sm mt-2">

<div class="border-l-4 border-blue-500 pl-3 mb-3">

### Identity
- **CIM:** UUID-based mRIDs that persist across versions and organizations
- **PyPSA:** String names (user-chosen, no standard)
- **SAInt:** `ObjectType.Name` convention (e.g., `ENO.Bus1`)
- **GenX:** Integer zone IDs + resource names from CSV headers

</div>

<div class="border-l-4 border-green-500 pl-3 mb-3">

### Abstraction Level
- **CIM, GDM, SAInt:** Model physical devices with full electrical parameters
- **PyPSA:** Physical parameters but simplified (optional standard types)
- **GenX:** Zonal abstraction — no individual buses or branches
- **CESM:** Energy-flow abstraction — no impedance or voltage

</div>

<div class="border-l-4 border-purple-500 pl-3 mb-3">

### Units
- **GDM:** `Voltage(230, "kilovolt")` — enforced by Pint (can't mix units)
- **CIM:** Semantic types in RDF (machine-readable, formally defined)
- **SAInt:** Built-in units library
- **PyPSA/GenX:** Convention only — kV, MW, per-unit (documentation, not code)

</div>

<div class="border-l-4 border-orange-500 pl-3 mb-3">

### What Gets Validated
- **GDM:** Phase consistency (3φ load ↔ 3φ bus), voltage agreement, graph cycles
- **CIM:** SHACL profile conformance, cardinality, cross-profile consistency
- **SAInt:** Real-time rejection of invalid entries during editing
- **GenX:** File existence, column names, time series alignment
- **PyPSA:** Migrating to Pydantic/Pandera (currently minimal)

</div>

</div>

---

# What This Use Case Teaches Us

<v-clicks>

### The schemas aren't competing — they serve different problems
The same 2-bus system needs *different* representations depending on what you're solving. Capacity expansion (GenX, CESM) doesn't need impedance. Exchange (CIM) doesn't need costs. Distribution (GDM) needs phase detail no one else models.

### Translation is lossy in both directions
Converting CIM → GenX loses all electrical parameters. Converting GenX → CIM loses all cost data. A common schema would need to be a *superset*, not an *intersection*.

### The real convergence challenge: semantics, not syntax
All six can represent "a thing connected to a bus." The hard part is agreeing what the thing *means* — is SAInt's `FGEN` the same as GenX's `Thermal`? Is CIM's `ConnectivityNode` the same as PyPSA's `Bus`? The answer is "sort of, but the edge cases matter enormously."

### Validation depth reflects domain maturity
GDM's cross-object validation ("3φ load on 3φ bus") and CIM's SHACL conformance testing reflect decades of experience with real-world data quality problems. Newer schemas will likely evolve toward similar strictness.

</v-clicks>

---
layout: center
class: text-center
---

# Thank You

<div class="text-lg mt-4 opacity-70">

Analysis by Claude AI

Source data: G-PST/data-schema-exercise

</div>
