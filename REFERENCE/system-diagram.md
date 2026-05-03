# Terrible Enfant OS1 — System Diagrams

Four diagrams. Read in order: layers → weekly cycle → data flow → folder structure.

---

## 1. System Layers Overview

```mermaid
graph LR
    subgraph PEOPLE["👥 People Layer"]
        P1["Hache\nCEO"]
        P2["Comando\nDir. Creativo"]
        P3["Fanny\nPM Transversal"]
        P4["Nacho / Jorge\nLegales / Logística"]
        P5["Freequency\nBrasil"]
    end

    subgraph FILES["📁 File Layer (GitHub)"]
        F1["12 × STATUS.md\n(ARG + BRA, 6 áreas cada uno)"]
        F2["12 × kpis.md\n(mensuales)"]
        F3["W[XX] Report\nWEEKLY/2026/"]
        F4["Decisions Log\n_GLOBAL/weekly-decisions-log.md"]
        F5["Brand & Strategy docs\nCORE / STRATEGY"]
    end

    subgraph AUTO["⚙️ Automation Layer (Boris + Claude Code)"]
        A1["compile-weekly-status.md\n→ Compila 12 STATUS en reporte"]
        A2["draft-meeting-agenda.md\n→ Genera agenda del martes"]
        A3["generate-decision-log.md\n→ Formatea notas en decisiones"]
    end

    subgraph OUTPUT["📤 Outputs"]
        O1["Reporte semanal\n(Hache lo lee antes del martes)"]
        O2["Agenda WhatsApp\n(antes de las 10:00 del martes)"]
        O3["Decisions log\n(append-only, permanente)"]
        O4["Asana tasks\n(solo Fanny crea)"]
        O5["KPI narrative\n(para Jorge, mensual)"]
    end

    P1 & P2 & P3 & P4 & P5 -->|"escribe STATUS.md\ncada lunes"| F1
    P1 & P2 -->|"actualiza docs\nde marca"| F5
    P4 -->|"KPIs mensuales"| F2

    F1 -->|"INPUT"| A1
    A1 -->|"produce"| F3
    F3 -->|"INPUT"| A2
    F3 -->|"INPUT"| O1

    A2 -->|"produce"| O2
    A3 -->|"produce"| F4

    F4 -->|"lee"| P3
    P3 -->|"crea tareas"| O4

    F2 -->|"INPUT mensual"| O5
```

---

## 2. Weekly Operational Cycle

```mermaid
graph TD
    START(["🔁 Ciclo semanal"])

    START --> MON1

    subgraph LUNES["LUNES"]
        MON1["Cada líder de área\nactualiza su STATUS.md\n📝 ×12 archivos"]
        MON2{"¿Todos\nentregados?"}
        MON3["Fanny hace seguimiento\na quien falta"]
        MON4["Boris abre repo en VS Code\nClaude Code lee 12 STATUS.md"]
        MON5["Claude compila reporte\nusando _template-weekly-report.md"]
        MON6["Reporte guardado\nWEEKLY/2026/W[XX]-[fecha].md\n+ git commit + push"]
    end

    subgraph MARTES["MARTES"]
        TUE1["Boris genera agenda\ncon draft-meeting-agenda.md"]
        TUE2["Agenda enviada\nvía WhatsApp/email\n⏰ antes de 10:00"]
        TUE3["📅 Reunión 10:00–10:45\nHache + Comando + Fanny\n+ líderes relevantes"]
        TUE4["Solo decisiones\n(los updates ya fueron leídos)"]
        TUE5["Boris/Fanny capturan\nnotas crudas"]
        TUE6["Claude formatea decisiones\ncon generate-decision-log.md"]
        TUE7["Decisions log actualizado\n(append-only)\n+ git commit"]
        TUE8["Fanny crea tareas\nen Asana\n(solo ella puede hacerlo)"]
    end

    subgraph SEMANA["MIÉRCOLES–VIERNES"]
        WF1["Ejecución\nCada responsable ejecuta sus tareas"]
        WF2["Updates de estado\nen Asana (no en STATUS.md)"]
        WF3["No hay commits al repo\ndurante la semana"]
    end

    MON1 --> MON2
    MON2 -->|"Sí — antes de 18:00"| MON4
    MON2 -->|"No"| MON3
    MON3 --> MON4
    MON4 --> MON5
    MON5 --> MON6

    MON6 --> TUE1
    TUE1 --> TUE2
    TUE2 --> TUE3
    TUE3 --> TUE4
    TUE4 --> TUE5
    TUE5 --> TUE6
    TUE6 --> TUE7
    TUE7 --> TUE8

    TUE8 --> WF1
    WF1 --> WF2
    WF2 --> WF3
    WF3 --> START
```

---

## 3. Data Flow — Quién escribe, quién lee

```mermaid
graph LR
    subgraph WRITERS["✍️ Escritores"]
        W_HACHE["Hache"]
        W_NACHO["Nacho"]
        W_COMANDO["Comando"]
        W_FANNY["Fanny"]
        W_JORGE["Jorge"]
        W_FREQ["Freequency"]
    end

    subgraph REPO["📂 Repo (GitHub)"]
        S_FA_ARG["STATUS.md\nFinance-Admin ARG"]
        S_LC_ARG["STATUS.md\nLegal ARG"]
        S_PR_ARG["STATUS.md\nProducto ARG"]
        S_OP_ARG["STATUS.md\nOperations ARG"]
        S_LG_ARG["STATUS.md\nLogistics ARG"]
        S_MC_ARG["STATUS.md\nMktg-Comms ARG"]
        S_BRA["STATUS.md ×6\nBRA mirror"]
        REPORT["W[XX] Report\nWEEKLY/2026/"]
        DLOG["Decisions Log\n_GLOBAL/"]
        AGENDA["Agenda\n(texto, no archivo)"]
    end

    subgraph BORIS["⚙️ Boris + Claude Code"]
        B1["Lee 12 STATUS.md"]
        B2["Compila reporte W[XX]"]
        B3["Genera agenda"]
        B4["Formatea decisiones"]
    end

    subgraph READERS["👁 Lectores / Consumidores"]
        R_HACHE["Hache\n(exec summary)"]
        R_FANNY_READ["Fanny\n(decisions log)"]
        R_ASANA["Asana\n(tareas)"]
        R_JORGE["Jorge\n(KPI narrative)"]
        R_MEETING["Equipo\n(agenda martes)"]
    end

    W_HACHE -->|"Finance, Producto ARG"| S_FA_ARG & S_PR_ARG
    W_NACHO -->|"Legal ARG"| S_LC_ARG
    W_COMANDO -->|"Producto, Mktg ARG"| S_PR_ARG & S_MC_ARG
    W_FANNY -->|"Operations ARG+BRA"| S_OP_ARG & S_BRA
    W_JORGE -->|"Logistics ARG"| S_LG_ARG
    W_FREQ -->|"BRA Mktg + Ops"| S_BRA

    S_FA_ARG & S_LC_ARG & S_PR_ARG & S_OP_ARG & S_LG_ARG & S_MC_ARG & S_BRA --> B1
    B1 --> B2 --> REPORT
    REPORT --> B3 --> AGENDA
    REPORT --> R_HACHE

    B4 --> DLOG
    DLOG --> R_FANNY_READ --> R_ASANA
    AGENDA --> R_MEETING
```

---

## 4. Folder Structure

```mermaid
graph TD
    ROOT["📦 TERRIBLE ENFANT · OS1\nRaíz del repo"]

    ROOT --> CORE["CORE/\n🔒 ADN de marca\nNo modificar sin Hache o Comando"]
    ROOT --> STRAT["STRATEGY/\nDocumentos estratégicos globales\nExpansión BRA, campaña activa"]
    ROOT --> OPS["OPERATIONS/\n❤️ Corazón operacional"]
    ROOT --> WEEKLY["WEEKLY/\nReportes semanales compilados"]
    ROOT --> AUTO["AUTOMATION/\n⚙️ Dominio de Boris"]
    ROOT --> ARCH["ARCHIVE/\nCampañas cerradas, ciclos completados"]
    ROOT --> REF["REFERENCE/\nDocs originales, Notion, legacy"]
    ROOT --> CLAUDE["CLAUDE.md\n📖 Leer PRIMERO — instrucciones para Claude"]

    OPS --> GLOBAL["_GLOBAL/\nCoordinación transversal (Fanny)\nDecisions log · Asana guidelines"]
    OPS --> ARG["ARG/\n🇦🇷 6 áreas operacionales"]
    OPS --> BRA["BRA/\n🇧🇷 Espejo de las 6 áreas ARG"]

    ARG --> ARG1["finance-admin/\nSTATUS.md + kpis.md\n→ Hache"]
    ARG --> ARG2["legal-contable/\nSTATUS.md + kpis.md\n→ Nacho"]
    ARG --> ARG3["producto/\nSTATUS.md + kpis.md\n→ Hache + Comando"]
    ARG --> ARG4["operations/\nSTATUS.md + kpis.md\n→ Fanny"]
    ARG --> ARG5["logistics/\nSTATUS.md + kpis.md\n→ Jorge"]
    ARG --> ARG6["marketing-comms/\nSTATUS.md + kpis.md\n→ Comando"]

    BRA --> BRA_NOTE["Misma estructura × 6\n⚠️ legal-contable SIN asignar — urgente"]

    WEEKLY --> WT["_template-weekly-report.md\nPlantilla de compilación"]
    WEEKLY --> WY["2026/\nW[01]–W[52] archivos"]

    AUTO --> AP["prompts/\ncompile-weekly-status.md\ndraft-meeting-agenda.md\ngenerate-decision-log.md"]
    AUTO --> AL["logs/\nautomation-log.md"]
    AUTO --> AB["boris-playbook.md\nInstrucciones completas"]
```

---

*Generado automáticamente con Claude Code — actualizar si cambia la estructura del repo.*
