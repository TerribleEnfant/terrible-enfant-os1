# Canon Migration Brief — rework TE-OS into a 4C harness

> **What this is.** The kickoff brief for migrating this repository to the COMANDO Canon
> (the 4C model). Open a fresh Claude Code session **in this repo** and paste the prompt
> below to begin. It drives a Diagnose → Design → Deploy refactor that preserves content
> and git history. The canon itself lives in the sibling repo `COMANDO-AI/C-OS`.

---

## MISSION — Rework TE-OS into a canonical 4C harness (COMANDO Canon)

You are **Comander**, operating inside the **Terrible Enfant OS (TE-OS)** repository
(`TerribleEnfant/terrible-enfant-os1`). Refactor this repo so its structure conforms to the
**COMANDO Canon — the 4C model**, without losing content and while preserving git history.

This is an **in-place refactor of a live OS** (active projects: brazil-launch, gtm-sao-paulo,
collabs), not a greenfield build. **Propose before you move anything.**

### 0 · Frame — what you are actually building

TE-OS is not "a docs folder." It is a **natural-language, file-backed harness (NLAH)**: an
orchestration layer, externalized as `.md` artifacts, that governs how an agent stores,
retrieves, and acts on TE's information. The **COMANDO Canon is the meta-harness** stamping
this one.

**The full foundation is `canon/spec/harness-theory.md` (read it first — see §1).** Two
principles from it are **binding constraints on this refactor**:
- **Additive over architectural rewrite** → migrate by relocation (`git mv`), not
  delete-and-recreate. Preserve history; smallest structural change that achieves conformance.
- **Keep raw history raw** → Cadence logs (pulse, decision_log, automation-log) are the
  harness's filesystem-exposed history. Relocate them intact; do not summarize or prune.

The **Charter / OS-layer split** is the theory's runtime-charter vs harness-logic (IHR)
distinction; the **WAT artifacts** are NLAHs (agents = Roles, workflows = Stage structure +
Contracts, Cadence = State, escalation = failure taxonomy).

### 1 · Read the canon (source of truth)

The Canon lives in the sibling repo **COMANDO-AI/C-OS**, on this machine at:
`/Users/boris/Documents/COMANDO/!_C-OS_M1/`

Read, in order:
1. `canon/spec/harness-theory.md` — the harness / meta-harness foundation and the principles
   that bind how we build.
2. `canon/spec/4C.md` — the 4C model, WAT-inside-4C, Charter/OS-layer split, fused lexicon.
3. `canon/README.md`, `canon/skeleton/README.md`, `canon/skeleton/CLAUDE_TEMPLATE.md`.
4. `canon/method/WF_CANON_DEPLOY.md` + the three worksheets under
   `canon/method/{1_diagnose,2_design,3_deploy}/`.
5. `C-OS_M3.md` (root) — the reference **boot spec** (OS-layer file). TE-OS needs its own.
6. Skim COMANDO's filled instance (`capabilities/`, `cadence/`, `CLAUDE.md`) as a worked example.

### 2 · The target model — 4C, with its harness-theory role

| Layer | Holds | Harness-theory role |
|---|---|---|
| **`context/`** | identity, strategy, distilled knowledge (static/slow) | persisted knowledge state |
| **`connections/`** | live data & integrations as `TL_*` (auth via 1Password) | runtime retrieval / intake |
| **`capabilities/`** | `AG_*` agents, `WF_*` workflows, skills registry | **Roles** + **Stage structure** |
| **`cadence/`** | routines, pulse, decision_log, logs, dashboards | file-backed durable **State** + self-trigger loop |

**Data flow:** `Connections (live intake) → Capability (distillation) → Context (durable
residue)`. Raw intake stages in `vault/` (never committed); distilled residue lands in
`context/knowledge/`.

**Charter vs OS-layer split (= IHR runtime-charter vs harness-logic):**
- **Charter** (pinned runtime): `CLAUDE.md` pointer (from `CLAUDE_TEMPLATE.md`; keep TE's
  principal and Spanish working language) + `.claude/` (skills, settings).
- **OS layer** (harness logic): the 4C content + a TE-OS **boot spec** at root (analogous to
  `C-OS_M3.md`), versioned by Mark.

**WAT inside 4C** (not top-level): `AG_*`/`WF_*` → Capabilities; `TL_*` → Connections;
self-triggering workflows + state → Cadence. **Two orthogonal spines:** 4C = *where a file
lives*; AREA token = *what function it serves* (decide TE's tokens in Design — candidates:
`BRAND`, `OPS`, `PROJ`/`GTM`, `AUTO`, or geographic `ARG`/`BRA`; justify the choice).

**Author every WAT artifact as an NLAH:** an agent card makes its **Role** explicit; a
workflow makes its **Stage structure** (plan → execute → verify → repair), **Contracts**
(required outputs, validation gates, stopping conditions), and **failure taxonomy** explicit.

**Language rule:** structural tokens and filenames in **English** (canonical 4C/WAT vocab);
TE content stays in its existing **Spanish**.

### 3 · Method — WF_CANON_DEPLOY, adapted for in-place refactor

**Stage 0 — Safety.** Branch (`canon-4c-migration`); confirm tree committed + pushed first.

**Stage 1 — Diagnose.** Fill `DIAGNOSE_WORKSHEET.md` against current TE-OS. Produce a **gap
map** (Context exists? Connections live? Capabilities/Cadence present or missing?). Archive
the filled worksheet to `context/knowledge/`.

**Stage 2 — Design ← SIGN-OFF GATE.** Map current → 4C. Produce: target tree; **move-map**
(every file → its 4C destination via `git mv`); proposed AREA tokens and renamed WAT
(`AG_*`/`WF_*`/`TL_*`) with their NLAH Roles/Stages; anything with no clean 4C home (flag,
don't improvise — "unmapped capability" is a named failure mode). **Stop for Boris's sign-off
on the move-map before touching files.**

**Stage 3 — Deploy.** Execute the approved move-map with `git mv` (additive, history-
preserving). Small logical commits. Create `CLAUDE.md` Charter + boot spec. Wire Connections
references (1Password + `op`; never secrets on disk). Run canon-lint. Open a PR.

### 4 · Starting-hypothesis mapping (refine in Design — NOT final)

- `CORE/` (brand-bible, brand-narrative, org/team-structure, product-catalog) →
  **`context/identity/`** + **`context/strategy/`**
- `REFERENCE/` (legacy-context, notion-*) → **`context/knowledge/`**
- `AUTOMATION/tools/*` (asana, github, google-drive, meta-ads, n8n, nuvemshop, whatsapp) →
  **`connections/`** as `TL_*`
- `AUTOMATION/agents/*` → **`capabilities/agents/`** as `AG_*` (each = a Role)
- `AUTOMATION/workflows/*` + `AUTOMATION/prompts/*` → **`capabilities/workflows/`** as `WF_*`
  (each = a Stage structure + Contracts)
- `.claude/commands/upc.md` → skills registry in **`capabilities/skills/`** (file stays in `.claude/`)
- `OPERATIONS/_GLOBAL/pulse.md` → **`cadence/pulse.md`**; `weekly-decisions-log.md` →
  **`cadence/decision_log.md`**; `AUTOMATION/logs/` → **`cadence/`** (keep raw); `WEEKLY/` → **`cadence/`**
- **Open design questions (decide with rationale):** `OPERATIONS/ARG|BRA/` per-area STATUS+kpis
  (live State → Cadence, or Context?); `PROJECTS/{active,pipeline,completed}` (live work →
  Cadence?); `ARCHIVE/` (retain as-is, or fold into `context/knowledge/`?).

### 5 · Guardrails (hard rules)

- **Propose before scaffolding.** One stage at a time; check in.
- **Additive over rewrite; preserve history** — `git mv`, never delete-and-recreate.
- **Keep raw history raw** — relocate logs intact; do not summarize or prune.
- **Sign-off gate** at end of Design before any file moves.
- **Secrets** — 1Password is the vault of record; inject via `op`, never commit to disk.
- No external comms / commercial commitments without approval. Work on a branch; deliver via PR.

### 6 · Definition of done

- TE-OS boots: `CLAUDE.md → boot spec → context/identity → cadence/pulse` resolves cleanly.
- All content relocated into 4C with history preserved; nothing orphaned; logs intact and raw.
- WAT renamed and internally consistent as NLAH artifacts (Roles/Stages/Contracts explicit).
- Gap map + design doc archived in `context/knowledge/`.
- Canon-lint clean; PR opened for Boris's review.

Begin with Stage 0 and Stage 1 (Diagnose). Report the gap map and proposed move-map, then
stop for sign-off before moving files.

---

*Built on the COMANDO Canon · `COMANDO-AI/C-OS`*
