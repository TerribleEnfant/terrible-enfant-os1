# BOTH Ventures - Company Context

## What We Are
BOTH Ventures is a venture platform designed to operate where single-logic strategies no longer suffice. We build and accelerate companies at the intersection of capital, technology, culture, and governance -- structured for complexity, not despite it.

**Core premise:** Contradiction is not a bug. Holding multiple logics simultaneously -- capital and meaning, speed and depth, structure and emergence -- produces more resilient institutions than optimizing for any single logic.

**Base:** Punta del Este, Uruguay. Operating globally.

## Team

| Name | Role | Venture Ownership | Sole Decisions |
|------|------|-------------------|----------------|
| Gaston Frydlewski | CEO / Ultimate Decision Maker | Casa Manantial, Reshore, Punta Cripto | Capital allocation, new projects, exits, corporate structure changes, investor comms |
| Rene Labarthe | Head of Strategy + Comms | LAK3, Photonic Lab | Narrative direction, positioning, content sign-off |
| Daiana Goldenberg | Operations + Finance | Casa Manantial, La Chamana | Ops priorities, finance tracking, process design |
| Andres Burecovics | Co-founder / CLO | Panambi, Quantum | Legal structuring, due diligence, compliance |
| Mariano Boris | Context Engineer / Tools Admin / Technical Lead | Context Engineering (support) | Tool configuration, documentation protocols |

**Decision authority:** Gaston alone on capital, exits, structure, LP comms. Team consensus on strategic pivots, major operational changes, new hires. Owner autonomy on day-to-day within their ventures and domains.

## Venture Portfolio

8 active ventures. Each has a primary owner who reports on status. BOTH's involvement ranges from hands-on building to observational.

**Taxonomy:** Meaning (Explore / Build / Scale) · Action (Hands-on / Supportive / Observational) · Outcome (Learning / Momentum / Value)

| Venture | Description | BOTH Role | Owner | Status |
|---------|-------------|-----------|-------|--------|
| MANANTIAL.CASA | Physical HQ + institutional base. Events, retreats, innovation. | Build + Daily | Gaston / Daiana | Build |
| RESHORE | Infrastructure for re-localizing production. Resilient supply chains. | Build + Hands On | Gaston | Build |
| LAK3 | Tokenizes water and real-world assets for liquidity + transparent ownership. | Build + Hands On | Rene | Build |
| PHOTONIC LAB | Venture-scale biotech lab. Research to impact. | Explore + Hands On | Rene | Explore |
| LA CHAMANA | Luxury private villa in Tulum. High-trust founder retreat. | Explore + Ops | Daiana | Explore |
| PANAMBI | Investment fund for mental health sciences in Latin America. | Explore + Observational | Andres | Explore |
| QUANTUM | New venture, legal structuring in progress. Business plan pending. | Explore + Hands On | Andres | Explore |
| PUNTA CRIPTO | Crypto initiative. Key income source for BOTH's financial self-sufficiency. | Build + Strategic | Gaston | Build |

## Voice + Tone
- Precise, not promotional. Structured, not inflated. Institutional, not corporate.
- Never "innovative" or "disruptive." Prefer: structural, optionality, both/and, becoming, permanent beta.
- Short declaratives. Fragments acceptable. False binaries rejected: capital vs meaning, discipline vs creativity, technology vs nature.
- Documents reference: Both_Ventures, Both_, version strings (V0.1.0), quarter codes (Q-01.26).

## Operational Stack

| Tool | Purpose | Owner |
|------|---------|-------|
| Google Drive | Source of truth for documents | All |
| WhatsApp | Internal comms (primary) | All |
| Claude (Cowork / Code) | AI agent interface | All (Boris manages) |
| Email | Investor communications only | Gaston |
| Supabase | Database (vault context, agent registry, memory) | Boris |
| n8n | Workflow automation (Tuesday Digest, Meeting Miner, WhatsApp bot) — not currently active | Boris |
| Make.com | Transcript ingestion — Fireflies → vault/transcripts/ auto-commit on every call | Boris |
| Fireflies | Call recording + transcription — webhook fires to Make on transcription complete | Boris |
| GitHub | Context sync, vault storage, version control | Boris |
| Asana | Task approval layer -- meeting action items go through Asana before agent execution | Daiana |
| WhatsApp Bot | Status pings, approval flows, task mining from group conversations | Boris |
| evolution-api | WhatsApp gateway (self-hosted on Railway, dedicated SIM) | Boris |
| Paperclip | Shared agent interface (forked, BOTH-branded, Railway) | Boris |
| Railway | Hosting for Paperclip + evolution-api | Boris |

**Not used:** Slack, Notion, Jira. Tools find us where we are -- we don't adopt tools for tools' sake.

---

## Agent Directory

13 specialized agents accessible via Claude Code / Cowork. Each agent file is a markdown prompt in `.claude/agents/`.

### How to Use an Agent
1. Open Claude Code or Cowork in this repo
2. Reference the agent: `@agents/meeting-miner.md`
3. Or paste the agent content as system context for any Claude session

### Agent Commands

| Command | Agent | Owner |
|---------|-------|-------|
| `/mm` | Meeting Miner | Daiana |
| `/tc` | Task Coordinator | Daiana |
| `/vt` | Venture Tracker | Daiana |
| `/vu` | Venture Update (weekly champion update) | All champions |
| `/au` | Area Update (weekly area lead update) | All area leads |
| `/wr` | Weekly Reporter (Tuesday Sync Digest) | Daiana |
| `/ir` | Investor Researcher | Gaston |
| `/nw` | Narrative Writer | Rene |
| `/cs` | Capital Strategist | Daiana |
| `/if` | Intelligence Feed | Rene |
| `/ga` | Governance Advisor | Andres |
| `/dr` | Deck Refiner | Gaston |
| `/ad` | Art Director | Rene |

### Saving Agent Outputs
After completing any substantive task (reports, analyses, content), save the output:
```bash
cat <<'EOF' | bash scripts/save-output.sh --agent {slug} --title "{title}" --type {type} --status final
{markdown output}
EOF
```

---

## Knowledge Vault

Structured organizational knowledge lives in `vault/` at the repo root. See `vault/_index.md` for full conventions.

### Directories
| Directory | Contents |
|-----------|----------|
| `decisions/` | Type-1/Type-2 decisions with rationale, assumptions |
| `strategy/` | Strategic positions, market theses, portfolio-level thinking |
| `ventures/` | Per-venture status, updates, KPIs (8 venture files) |
| `investors/` | LP and co-investor profiles, thesis alignment, comms history |
| `risks/` | Risk register (likelihood, impact, mitigation) |
| `transcripts/` | Raw meeting notes — immutable archive (input for `/mine`) |
| `pending/` | Extracted items awaiting champion approval before vault write |
| `agent_outputs/` | Saved outputs from any agent run |
| `archive/` | Retired/superseded notes |

### Key Commands
- **`/mine`** -- Extract structured knowledge from meeting notes into the vault
- **`/generate-pdf`** -- Create branded PDFs from markdown
- **`/supabase-query`** -- Query the database directly from Claude

### Vault Conventions
- YAML frontmatter required on every file (title, created, updated, status, tags, author)
- Lifecycle: draft -> active -> superseded -> archived. Never delete, always archive.
- Hooks auto-commit vault changes and validate frontmatter on every write.

---

## Weekly Operating Rhythm (Tuesday Sync)

THE most important process. The entire weekly cadence flows through this.

1. **During week:** Each person works on ventures + areas. Exploratory, not final.
2. **Monday:** Each champion runs `/vu` to update their venture(s) and `/au` to update their functional area. Updates land in the vault and auto-commit.
3. **Monday evening or Tuesday AM:** Boris generates the digest via `/wr`. Daiana validates. Digest distributed for pre-reading.
4. **Tuesday meeting (in-person):** Decisions only. Gaston chairs. Everyone arrives having read the digest. Max 60 min.
5. **Post-meeting:** Daiana captures notes (text paste or audio), runs `/mine`. Claude extracts decisions, action items, risks, and venture updates. Raw notes archived immediately. Extracted items land in `vault/pending/` for champion review.
6. **Champion review:** Each owner opens their pending file, marks `approved: true` on confirmed items, runs `/mine approve vault/pending/{file}.md`. Approved items write to vault. Auto-commit fires.
7. **Vault updated.** Context evolves. Loop closed.

**Principle:** AI generates, humans validate, vault captures. The weekly snapshot is the single source of truth.

### Meeting Miner Cycle (V1 — Claude Code native)
```
Notes or audio → /mine → raw archive → pending review → /mine approve → vault
```
- Audio files: `bash scripts/transcribe.sh {path}` converts to text first (Whisper API)
- Pending file: `vault/pending/YYYY-MM-DD-{slug}.md` — champions edit this, not Claude
- Nothing writes to the main vault without explicit champion approval
- Action items: captured in pending file, printed in approval summary (Asana routing in V2)

---

## System Architecture (Two Layers)

Both layers share the same agents, company context, knowledge vault, and Supabase database.

| Layer | Interface | Runs On | Who Uses It |
|-------|-----------|---------|-------------|
| **Local** | Claude Code / Cowork | Each person's machine | Full team -- agent prompts + vault on disk |
| **Cloud** | n8n + Supabase | n8n + Supabase (free tier) | Boris manages -- automated workflows |

### How They Connect
- **Local:** Claude reads agent `.md` files + vault from disk. Hooks auto-commit changes. Scripts sync vault -> Supabase.
- **Cloud:** n8n workflows query Supabase for vault context, generate Monday Digest, process meeting notes.
- **Sync:** GitHub repo is the bridge. Each person pulls daily. Vault changes auto-commit + push.

### Infrastructure
- **Supabase:** PostgreSQL + pgvector. 12 tables: user_profiles, agent_registry, vault_context, conversations, conversation_messages, agent_memory, usage_metrics, venture_snapshots, agent_outputs, task_queue, pending_actions, access_grants. RLS policies enforce access scopes.
- **n8n:** 6 workflows -- Monday Digest Generator, Meeting Miner, Action Items to Asana, Action Approval Webhook, WhatsApp Bot Core, WhatsApp Group Miner. Note: WhatsApp workflows (Phase 2) require self-hosted n8n for evolution-api community node. Phase 1 workflows work on n8n Cloud or self-hosted.
- **Railway:** Hosts Paperclip (agent interface) + evolution-api (WhatsApp gateway).
- **Anthropic API:** Claude for all agent intelligence. Per-agent model selection + company budget cap.
- **OpenAI API:** text-embedding-3-small for vector embeddings only.
- **Asana:** Task approval layer. Daiana's existing workspace. BOTH project with per-venture sections.

---

## Permissions Model

Not everyone sees everything. Access is scoped at every layer.

### Three Access Scopes

| Scope | Who | Sees |
|-------|-----|------|
| **admin** | Gaston, Daiana, Boris | Everything -- all vault files, all agents, all ventures, all outputs |
| **team** | Rene, Andres | Shared vault (no investor data), non-fundraising agents, their ventures |
| **restricted** | External collaborators (e.g., Gaston's assistant) | Only explicitly granted items via access_grants table |

### Two GitHub Repos

| Repo | Contents | Access |
|------|----------|--------|
| `both-os` | Shared agents, vault (non-confidential), schema, workflows, CLAUDE.md | All 5 team + Daniel (during engagement) |
| `both-private` | Confidential vault (investors, strategy), Family Office data, LP comms | Gaston + Daiana only |

### How It Works Per Layer

- **Claude Cowork:** Local by default. Nothing shared unless you push to vault/GitHub.
- **GitHub:** Repo-level access. `both-private` is invisible to team-scope users.
- **Supabase:** Row Level Security (RLS) filters by user's access_scope. Fundraising agents and investor data hidden from team scope. Restricted users see only explicitly granted items.
- **Paperclip:** Agents filtered by department. Team scope cannot see investor-researcher or deck-refiner.
- **Google Drive:** Existing sharing controls. Separate shared drives per scope (BOTH main, Family Office, per-venture).

### Adding External Collaborators

To give a restricted user access to specific items:
1. Add them to `user_profiles` with `access_scope = 'restricted'`
2. Insert rows into `access_grants` table specifying which vault files, ventures, agents, or outputs they can see
3. Set `expires_at` if the access is temporary

---

## Developer Setup (Claude Code)

### What You Get by Cloning This Repo
When you run `claude` inside this repo, Claude Code automatically loads this file. That gives you:
- Full company context, team, venture portfolio
- All 10 agent prompts in `.claude/agents/`
- Knowledge vault in `vault/`
- Skills: /mine, /generate-pdf, /supabase-query

**No additional setup required.** Clone, `cd` into the repo, and run `claude`.

### Hooks (configured in `.claude/settings.local.json`)
- **`session-orient.sh`** -- Shows vault state and recent changes on session start
- **`write-validate.sh`** -- Warns if vault files are missing required frontmatter
- **`auto-commit.sh`** -- Auto-stages and commits vault file changes

### Sync Scripts
- **`vault-sync.sh`** -- Push vault markdown -> Supabase vault_context table (hourly via launchd)
- **`sync-agents.sh`** -- Push agent prompts -> Supabase agent_registry (run after modifying agents)
- **`backup-supabase.sh`** -- Full database dump (daily at 3 AM, 30-day retention)
- **`scripts/transcribe.sh`** -- Convert audio to transcript via Whisper API (requires OPENAI_API_KEY)
- **`scripts/save-output.sh`** -- Save any agent output to vault/agent_outputs/ with frontmatter

---

## Active Projects

Living technical builds. Each has a dedicated folder under `projects/` with deployment context, status, and decisions. Distinct from the vault (institutional knowledge) and agents (reusable prompts).

| Project | Description | Owner | Status |
|---------|-------------|-------|--------|
| `lc-paperclip` | BOTH-branded Paperclip AI — shared agent interface, runs locally via Docker | Boris | Operational |
| `telegram-agent` | Telegram bot for team — vault search, calendar, tasks via Claude tool_use | Boris | Code complete, blocked on credentials |
| `ai-infrastructure` | Living documentation of AI stack status and evolution — snapshots, decisions | Boris | Active |

### Convention

Each project folder contains:
- `context.md` — architecture, deployment steps, config references
- `status.md` — current state, open items, decisions

Code that is actively deployed (e.g., `telegram-agent/`) stays at repo root to preserve Railway/Docker paths. `projects/{name}/context.md` acts as the pointer and documentation layer.

---

## Context Self-Audit Protocol

After completing any substantial task, check whether any reference files need updating:
1. **Did any company facts change?** -> Update this file
2. **Did I learn a better way to do something an agent does?** -> Update that agent's `.md`
3. **Did the team add/remove/change a tool?** -> Update tool tables + affected agents
4. **Did someone correct me on something?** -> Find the source of wrong info and fix it

Rules: Always propose updates explicitly. Show the diff. One source of truth. Don't bloat.
