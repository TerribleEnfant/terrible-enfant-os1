> **External reference — not a TE document.** Imported into the TE OS1 repo as context for the
> BRA e-commerce build (Nuvemshop). Source: the **La Chamana OS / `lc-chaman`** project — a faithful
> "as-built" record of how that Shopify + marketing/analytics stack was assembled. The platform there
> is Shopify (TE BRA uses Nuvemshop), so treat the platform-specific steps as analogues, not literal
> instructions. Public IDs quoted below belong to La Chamana, not Terrible Enfant.
> Imported 2026-06-04 by Boris.

---

# Handoff to an Imaginary Project

> A faithful "as-built" record of how the **La Chamana OS / El Chaman** workspace was assembled —
> written so a brand-new project (the *imaginary* one reading this) can stand up something similar.
>
> **Version:** 1.0 · **Snapshot date:** 2026-06-04 · **Source repo:** `lc-chaman`

---

## 0 · What this is and how to read it

This document captures two bodies of work:

- **Part A — The OS environment.** The Claude Code workspace itself: config, MCP servers, hooks,
  subagents, skills, memory, ops-state tracking, repo layout, automation architecture. *Build this
  first* — the marketing work was driven from inside it.
- **Part B — The Alter Blue Shopify / marketing stack.** The analytics + ad-platform + email +
  landing-page + server-side tracking system, rolled out in phases. *This is the emphasized part.*

**Reading convention.** Each section in Part B is split into:

- **What we did** — the literal, as-built record, including real IDs. Container IDs, measurement IDs,
  and pixel IDs are *public* (they ship in your page source), so they are quoted verbatim as
  concrete reference.
- **For your project** — the generalized instruction, with placeholders like `G-XXXXXXXXXX`.

**Secrets are deliberately excluded.** No API keys, tokens, passwords, or session cookies appear
here. Those live only in the gitignored `.claude/settings.local.json`. Where a secret is required,
this doc names the *setting* (e.g. `KLAVIYO_API_KEY`) — never its value.

---

# Part A — The OS environment

A single-operator "operating system" runs in Claude Code (VS Code extension). One human (the
principal) drives high-leverage sessions; the workspace gives the model durable context, guardrails,
specialized skills, and memory so each session resumes where the last left off.

## A.1 · Claude Code configuration

### `CLAUDE.md` — the single source of truth

The project root holds one `CLAUDE.md` that every session loads automatically. It encodes the things
that must never drift:

- **North Star** — the one metric everything ranks against (here: 9 bookings, $4,500/night, 3-night
  minimum, fixed window). Every section ties back to it.
- **What the product is** + **team & decision-routing table** (who signs off on what).
- **Active channels in priority order.**
- **Voice / tone** — preferred words, banned words, format rules, a "read it aloud" voice test.
- **Hard rules** — explicit Never / Always lists.
- **Routing logic** — a trigger → skill table (e.g. "incoming inquiry → `/lead`").
- **Reference-file index** — pointers to the deeper context docs.

> **For your project:** put one `CLAUDE.md` at the repo root. Treat it as law, not notes. Keep it
> under ~250 lines; push detail into linked reference files. Re-audit it at the end of any session
> that changed strategy, channel status, or rules.

### `.mcp.json` — MCP servers

Three MCP servers are wired in the **project** `.mcp.json`:

- `notion-source` and `notion-target` — Notion API servers (Bearer auth) for two separate Notion
  workspaces (read-from / write-to).
- `playwright` — Playwright MCP driving a real Chrome with a **persistent** profile at
  `~/.cache/playwright-mcp-lc/`, vision + PDF capabilities enabled.

> **Gotcha that cost ~3 restarts:** an `mcpServers` block in `~/.claude/settings.json` is **silently
> ignored** by Claude Code. MCP servers must live in the project `.mcp.json` (or be added via
> `claude mcp add`). Browser-control via Playwright MCP turned out to be the *workhorse* for
> GTM / GA4 / Shopify admin work when API tokens were friction-heavy — it replaced an abandoned
> Shopify Admin API-token route.

### `.claude/settings.json` — permissions + hooks

- **Allowlist** — `WebFetch` domains the work actually touches (Shopify, Google Tag Manager,
  Google Analytics, Facebook, Klaviyo, TikTok, CloudBeds, Stape, n8n, Google Drive/Docs/Sheets,
  GitHub) and `Bash` verbs (git, grep/find, npm, python, Shopify CLI, file ops, `scripts/`).
- **Deny list** — destructive ops are hard-denied: `rm -rf`, `git push --force`,
  `git reset --hard`, `git clean -f`, `git branch -D`.
- **Hooks** — `SessionStart` and `PostToolUse` (Write/Edit) wired to the scripts below.

### `.claude/settings.local.json` — secrets (gitignored, names only)

The local file holds, **by setting name**: Slack webhooks (`SLACK_WEBHOOK_*`), Airtable token +
base ID, Gmail app password (testing inbox), the production send-inbox app password, CloudBeds
client credentials + API key + property ID, Shopify Admin API token + store handle + API version,
and `KLAVIYO_API_KEY` + Klaviyo company ID.

> **For your project:** commit `.claude/settings.json` (shareable rules), gitignore
> `.claude/settings.local.json` (secrets). Mirror the deny-list — a broad allowlist is only safe
> next to a firm deny-list.

## A.2 · Hooks (`.claude/hooks/`)

| Hook | Fires on | Does |
|------|----------|------|
| `session-orient.sh` | `SessionStart` | Prints the orientation banner: target delta, memory index, last 3 evolution-log entries, agents, skills, recent commits, "read these next" pointer. |
| `write-validate.sh` | `PostToolUse` (Write/Edit) | Lightweight QA on written files. |
| `auto-commit.sh` | `PostToolUse` (Write/Edit) | Auto-commits changes so work is never lost between sessions. |

## A.3 · Subagents (`.claude/agents/`) — read-only auditors

Three purpose-built, **read-only** subagents (Sonnet) that emit structured reports and never mutate
state. Built for the Alter Blue sprint and reusable:

| Subagent | Role | Fires during |
|----------|------|--------------|
| `copy-reviewer` | Validates draft copy against the `CLAUDE.md` hard rules (banned words, voice test). Returns PASS / REVIEW / REJECT with line-level violations. | Before any external-facing copy ships; pre-check ahead of human brand sign-off. |
| `tracking-verifier` | Curls a URL and detects which tags fire (GTM, GA4, Meta/TikTok pixels, Klaviyo, UTM passthrough). Returns found-vs-expected table. | Runbook steps 2, 8, 13, 24 (baseline, cross-platform verify, double-fire check, E2E smoke). |
| `klaviyo-auditor` | Walks Klaviyo integration depth, sync coverage, UTM config, flow inventory, segmentation. Read-only. | Runbook steps 14, 18. |

## A.4 · Skills (`.claude/skills/`)

Twenty custom skills, each a `SKILL.md` (frontmatter + body), invoked as `/name`:

| Skill | Purpose |
|-------|---------|
| `/lead` | Qualify a booking inquiry, draft concierge first response (no premature pricing). |
| `/pitch` | Agency / operator narrative pitch; philosophy before product, price last. |
| `/dm` | Curatorial IG outreach DM (≤3 sentences, Tier A/B/C, human approval gate). |
| `/caption` | IG caption (1–3 options), brand voice, no hashtags on hero posts. |
| `/brief` | Influencer residency creative brief. |
| `/event` | Event proposal (wedding / offsite) — experience frame, journey, pricing guidance. |
| `/content-plan` | 2-week day-by-day IG content calendar. |
| `/status` | Pipeline vs. target, pace analysis, next action; updates `ops/pulse.md`. |
| `/mine` | Extract decisions + actions from meeting notes → review → task system. |
| `/doc` | Narrative-first, versioned document (fact sheet, dossier, press kit). |
| `/match` | Score any tool on an 8-dimension fit/synergy scorecard. |
| `/research-digest` | Daily AI-tool digest from GitHub/Reddit/HN/PH → Slack. |
| `/r2bv` | Tech-stack status report to the parent org via Slack. |
| `/startup` | Session init: read state, compute pace, surface last work, flag stale blockers. |
| `/upc` | Update-Push-Commit: validate index sync, compose semantic commit, push. |
| `/wat-compose` | Scaffold a new Workflow / Agent / Tool entry with correct frontmatter. |
| `/brand-theme` | List / inspect / apply / validate UI themes on HTML. |
| `/import-contacts` | Load a contact database into the CRM. |
| `/bv-snapshot` | Daily commercial snapshot → Slack + archive. |

> **For your project:** a skill is the right home for any workflow you run more than twice. Keep each
> one narrow, give it a routing trigger in `CLAUDE.md`, and let it read/write the ops-state files.

## A.5 · Memory system

- One **fact per file** in `memory/`, with frontmatter (`name`, `description`, `metadata.type` of
  `user | feedback | project | reference`). Body links related memories with `[[name]]`.
- `memory/MEMORY.md` is the **index** — one line per memory, loaded into context each session.
- Lifecycle: check for an existing file before creating a duplicate; update wrong memories; never
  store what the repo/git already records.

> **For your project:** modular files beat one giant memory blob — they're individually editable,
> linkable, and cheap to recall. The index line is what the model actually scans at startup.

## A.6 · Ops-state tracking (`ops/`)

| File | Role |
|------|------|
| `ops/pulse.md` | **Live target delta** — confirmed vs. goal, days elapsed/remaining, current pace vs. needed pace, pipeline counts, channel-activation table, active blockers, highest-leverage next actions. Updated at session start and after `/status`. |
| `ops/evolution_log.md` | **Dated capability log** — append-only `\| date \| type \| entry \| rationale \|` rows (`capability` / `campaign` / `workflow` / `strategic`). Last 3 surfaced at startup. |
| `ops/routines.md` | **Scheduled autonomy** — registered recurring routines (R-001…), e.g. daily digest, Monday pulse, Friday outreach report. |
| `ops/tracking/` | Live audit snapshots, e.g. `v1.2-phase1-status.md`. |

## A.7 · Repo information architecture

```
lc-chaman/
├── CLAUDE.md                 Master context (law: brand, team, rules, routing)
├── README.md                 Quick reference
├── .mcp.json                 MCP servers (notion-source/target, playwright)
├── .claude/
│   ├── settings.json         Permissions + hooks (committed)
│   ├── settings.local.json   Secrets (gitignored)
│   ├── agents/               Read-only auditor subagents
│   ├── skills/               20 custom skills
│   └── hooks/                session-orient / write-validate / auto-commit
├── context/                  Founding docs + brand system (manifesto, voice, funnel, GTM flow)
├── vault/                    Strategic artifact archive
│   ├── strategy/             Architecture + decision docs
│   ├── plans/                Project runbooks + artifacts  ← alter-blue lives here
│   ├── campaigns/ pipeline/ reports/ sent/ decisions/ risks/ pending/ transcripts/
├── ops/                      Live state (pulse, evolution_log, routines, tracking/)
├── memory/                   Session-continuity facts + MEMORY.md index
├── scripts/                  Outreach, data-integration, sync scripts
├── docs/                     Shareable HTML/MD deliverables  ← this file
├── research/ tools/ backlog/ Tool evals, tool inventory, speculative features
```

## A.8 · Automation architecture (forward-looking)

A **3-layer** stack (`vault/strategy/automation-architecture-v1.0.md`):

1. **Layer 1 — Brain (local, principal only):** VS Code + Claude Code. Primary orchestration,
   complex reasoning, memory, vault. *Active.*
2. **Layer 2 — Team interface (VPS):** always-on agents, dashboards, approval gates, scheduled
   routines. *Phase 0 pending.*
3. **Layer 3 — Messaging gateway (deferred):** WhatsApp/Slack/Telegram front door.

**Autonomy tiers:** A = draft-only (all sends need approval) → B = auto-send low-risk, approve
high-risk → C = auto-send approved sequences with a hard daily budget cap. The pre-activation
checklist lives in `vault/strategy/phase-0-prep.md`.

---

# Part B — The Alter Blue Shopify / marketing stack

The website is a Shopify storefront (`lachamana.com`). "Alter Blue" is the codename for the project
that instrumented it for campaigns and paid media. It rolled out in phases so that each gate
(analytics → ad platforms → SEO/i18n → server-side) could ship and be verified independently.

**Canonical references in-repo:**
- Master plan: `vault/plans/alter-blue/00-overview.md`
- 27-step runbook: `vault/plans/alter-blue/v1.2-sprint-runbook.md`
- Live status log: `ops/tracking/v1.2-phase1-status.md`
- Paste-ready artifacts: `vault/plans/alter-blue/artifacts/`

## B.1 · The phased model

| Phase | Scope | State |
|-------|-------|-------|
| **Phase 1** | GA4 + GTM Web container + Klaviyo audit/wiring + a proof-of-concept landing page | ✅ Sealed |
| **Phase 1.5** | Native ad-platform connectors + OAuths (Meta, Google Ads, TikTok) | ✅ Meta + Google live; TikTok parked |
| **Phase 2** | SEO base + locale/markets fix (UY→MX) + Klaviyo flows | Specs ready, execution pending |
| **Phase 3** | Server-side spine (Stape sGTM + Cloudflare Workers + offline conversions) | Architecture locked, awaiting budget sign-off |

> **Why phase it:** each phase only needs the credentials it needs. Phase 1 ran entirely on one
> already-authenticated admin login; ad-platform OAuths (which were blocked on a personal-account /
> billing / shop-country gate) were forward-loaded out of the critical path into Phase 1.5.

## B.2 · Phase 1 — analytics foundation (as-built)

**What we did.** Installed an independent analytics + tag-management layer:

| System | Real ID | Installed where | Status |
|--------|---------|-----------------|--------|
| GA4 | Measurement ID `G-8QZY4X9R5R` (property `539286638`, account `396057879`, stream `14958405117`; tz Mexico City; currency USD) | Tag fires via GTM | ✅ Live |
| GTM Web container | `GTM-598X2STS` (account `6357740694`, workspace Default) | `layout/theme.liquid` lines **4–10** (head snippet) + **33–36** (after-`<body>` snippet) | ✅ Live, Version 3 published |
| Google Ads | Customer ID `821-425-8609`, conversion ID `18193810694` | Shopify Google & YouTube connector | ✅ Live (no campaign published) |
| Meta Pixel | `744944938681825` (Business Manager "La Chamana") | Shopify Facebook & Instagram connector | ✅ Live |
| TikTok Pixel | — | Shopify TikTok app | 🟡 Parked (shop country UY blocks install) |
| Klaviyo | Company ID `VY9Q2w` (orphan `RZEtpF` deprecated) | Shopify connector | ✅ Live |
| Shopify store | `q1xbgj-t8.myshopify.com` / alias `la-chamana-8065` | — | ✅ Live |

**The no-pixels-in-GTM lock.** Native Shopify connectors own the Meta / Google / TikTok pixels.
Adding those same pixels as GTM tags would **double-fire**. GTM is reserved for GA4 + custom events
only. This rule is written into the GTM container notes and the GA4 Config tag description.

> **For your project:** decide *one* owner per pixel — Shopify native connector **or** GTM, never
> both. Native connectors are the lower-friction default.

## B.3 · The GTM + GA4 install pattern

**What we did.**

1. Created the GA4 property (got Measurement ID `G-8QZY4X9R5R`).
2. Created the GTM Web container (`GTM-598X2STS`) and pasted **both** install snippets into
   `layout/theme.liquid` — the `<head>` snippet high in `<head>`, the `<noscript>` snippet
   immediately after `<body>`. The verbatim snippets are archived in
   `vault/plans/alter-blue/artifacts/gtm-install-snippets.md`.
3. Configured **Tag A — GA4 Configuration**: type *Google tag*, ID `G-8QZY4X9R5R`, trigger
   *Initialization – All Pages*. Set **`send_page_view = false`** to suppress a config-layer
   duplicate `page_view` (the v1.1 fix), published as Version 3.
4. Verified `window.dataLayer` and `google_tag_manager` are live, and that `/g/collect?en=page_view`
   fires. (A residual gtag-library double `page_view` is deduped by GA4 server-side via the `_p`
   hash — acceptable for Phase 1; full fix tracked for a later window.)

> **For your project:** GA4 property → GTM container → both snippets in your theme's main layout →
> one GA4 Config tag on Initialization-All-Pages → publish → verify the `/g/collect` hit. Keep
> `send_page_view=false` if anything else already emits `page_view`.

## B.4 · Klaviyo wiring

**What we did.**

- Installed the Shopify ↔ Klaviyo connector on the canonical account `VY9Q2w`. (A prior orphan
  account `RZEtpF` had been leaking subscribers; all storefront references were repointed.)
- Connector syncs **6 metrics**: Placed Order, Checkout Started, Cancelled Order, Fulfilled Order,
  Ordered Product, Refunded Order. Catalog = 0 items (expected — no product catalog).
- **UTM model:** Klaviyo deprecated account-wide UTM defaults; UTMs are now set **per campaign** at
  send time. Phase-1 action accordingly closed.
- Connected Klaviyo → GA4 so `email_open` / `email_click` flow into GA4.
- Flow inventory: 0 flows at Phase 1. Phase 2 candidates (Welcome ES/EN, Post-stay, Abandoned
  checkout) are specced in `phase2-klaviyo-flows.md`.

## B.5 · The landing-page POC pattern

**What we did** (a single vertical, "Corporate Offsites," as the proof):

- **5-block section spec** (`landing-vertical-section-spec.md`): Hero · repeating 3-pillar ·
  repeating 4-spaces · Logistics · Reserve. All blocks brand-rule compliant.
- **Copy** drafted via the `/event` skill (`landing-corporate-offsites-copy.md`, v1.0), EN + ES.
- **Delivery fallback:** Shopify's Pages HTML sanitizer + Monaco editor fought a custom Liquid
  section, so the POC shipped as **inline HTML** in the page body
  (`landing-corporate-offsites-published-body.html`). A proper `sections/landing-vertical.liquid`
  is deferred to Phase 2.
- **UTM capture:** a JS snippet in `theme.liquid` (just above `</body>`) reads URL params and writes
  hidden form fields — `utm_source/medium/campaign/content/term`, `gclid`, `fbclid`. The script is
  archived at `vault/plans/alter-blue/artifacts/utm-passthrough.js`.
- **Form target:** the inquiry form POSTs directly to the **Klaviyo Client Profiles API**
  (`company_id=VY9Q2w`), creating a profile stamped with every UTM + custom property.

## B.6 · Verification approach

**What we did.** Used the `tracking-verifier` subagent and a smoke-test URL carrying UTMs, e.g.
`lachamana.com/pages/<vertical>?utm_source=verify&utm_medium=manual&utm_campaign=phase1-smoke`.
Confirmed: GA4 `page_view` (204 + `_ga` cookies), Meta Pixel `register` 200 + `fbp` cookie,
Google Ads conversion endpoint 200, and a Klaviyo profile created with all UTM fields populated.

> **For your project:** never trust "installed" — curl the live URL and confirm each tag actually
> *fires*. Automate it (a verifier subagent) so you can re-run after every change.

## B.7 · Phase 2 — forward pointers (specs ready)

| Artifact | What it does | Est. |
|----------|--------------|------|
| `phase2-locale-fix.md` | Shopify Markets change UY/UYU/en-UY → MX/USD/en+es. Unblocks TikTok pixel. Prereq: entity-US decision. | 45–60 min |
| `phase2-seo-base-paste-ready.md` | Paste-ready Liquid for title/meta/OG/Twitter/JSON-LD `LodgingBusiness` + hreflang (commented until locale fix). | 15–20 min |
| `phase2-klaviyo-flows-iru-walkthrough.md` | Click-by-click to stamp 14 flow templates (Welcome ES/EN, Post-stay ES/EN, Abandoned checkout) with country→language conditional split. | 1.5–2 h |
| `landing-corporate-offsites-published-body.html` | The Phase-1 body, ready to lift into a reusable custom Liquid section. | — |

## B.8 · Phase 3 — server-side spine (architecture locked)

Full spec in `vault/plans/alter-blue/artifacts/phase3-server-side-scaffold.md`:

- **Stape sGTM** (~$90/mo) at `sgtm.lachamana.com` — server-side GTM container forwarding GA4,
  Google Ads, Meta CAPI, TikTok Events API, and a GA4 `inquiry_qualified` event.
- **Cloudflare Worker `lc-tracking`** — `/ingest/booking` receives the CloudBeds webhook, normalizes
  it, forwards `booking_confirmed` to sGTM, mirrors to Klaviyo.
- **Cloudflare Worker `lc-customer-match`** — daily cron: read Closed-Won → SHA-256-hash emails →
  sync to Google Ads Customer Match + Meta Custom Audience.
- **Offline conversions** — nightly bookings → Google Ads Offline Conversions API + Meta Offline
  Events API.
- **Mid-funnel signal** — when a contact is marked Warm in the CRM, an automation hits
  `/ingest/inquiry-qualified` → sGTM routes to GA4 + Meta CAPI + Google Ads (Enhanced Conversions).

**Blocker:** recurring $90/mo Stape sign-off from finance owner.

## B.9 · Content Factory integration (v0.1)

`docs/content-factory-integration-plan.md` documents wiring an external Next.js copy-generation
console (Sonnet draft → sanitizer → Opus reviewer) into this OS. Three **unresolved collisions** to
settle before integrating:

1. **Name collision** — the console's writer persona vs. the outreach send-identity. (Rename writer.)
2. **"Luxury" keyword conflict** — the console's SEO clusters target a word the brand bans as an
   adjective. (Allow as keyword target; ban from body copy.)
3. **Source-of-truth drift** — two parallel voice definitions. (Auto-generate the console's JSON from
   the brand manifest.)

Integration is gated through the `copy-reviewer` subagent so nothing ships off-voice.

## B.10 · Decision gates / carried blockers

- **Entity-US decision** (finance owner) — prerequisite for the locale fix.
- **Stape $90/mo sign-off** (finance owner) — prerequisite for Phase 3.
- **Brand-voice sign-off** (brand owner) — soft flags on landing copy await async review.
- **Locale fix (UY→MX)** — prerequisite to unblock the TikTok pixel.

---

# Replication checklist

**Environment first**
- [ ] Root `CLAUDE.md` (North Star, team, rules, routing).
- [ ] `.claude/settings.json` (allowlist + deny-list + hooks); `.claude/settings.local.json` secrets, gitignored.
- [ ] `.mcp.json` with your MCP servers — **Playwright MCP must live here, not in `~/.claude/settings.json`**.
- [ ] `.claude/hooks/` session-orient + write-validate + auto-commit.
- [ ] `.claude/agents/` read-only auditors (copy-reviewer, tracking-verifier, klaviyo-auditor).
- [ ] `.claude/skills/` for any repeated workflow; register triggers in `CLAUDE.md`.
- [ ] `memory/` one-fact files + `MEMORY.md` index.
- [ ] `ops/pulse.md` + `ops/evolution_log.md` + `ops/routines.md`.
- [ ] Run `/startup` → confirm the orientation banner renders.

**Services**
- [ ] Shopify admin access + writable theme.
- [ ] CRM base (e.g. Airtable) + connector.
- [ ] Email send identity (app password) + transactional ESP (Klaviyo).
- [ ] Slack webhooks for reports/digests.

**Marketing rollout (phased)**
- [ ] **Phase 1 (~1 day):** GA4 property → GTM container → both snippets in theme layout → GA4
      Config tag (`send_page_view=false`) → publish → verify `/g/collect`. Install native Shopify
      connectors for each ad platform you can. Install Klaviyo connector. Ship one POC landing page
      with UTM-capture JS + form → Klaviyo API. Smoke-test with a UTM-tagged URL.
- [ ] **Phase 2 (~1–2 wk):** locale/markets fix, SEO Liquid patch + hreflang, Klaviyo flow templates,
      clone the landing template across verticals.
- [ ] **Phase 3 (~3–4 wk, budget-gated):** Stape sGTM, Cloudflare Workers (webhook bridge + Customer
      Match cron), offline conversions, the mid-funnel `inquiry_qualified` signal.

---

# Appendix — ID & file-path quick reference

### Public IDs (reference examples — not secrets)

| System | ID |
|--------|-----|
| GA4 Measurement ID | `G-8QZY4X9R5R` (property `539286638` · account `396057879` · stream `14958405117`) |
| GTM Web container | `GTM-598X2STS` (account `6357740694`) — `layout/theme.liquid` lines 4–10 + 33–36 |
| Google Ads | Customer ID `821-425-8609` · conversion ID `18193810694` |
| Meta Pixel | `744944938681825` (BM "La Chamana") |
| TikTok Pixel | parked (shop country UY) |
| Klaviyo company ID | `VY9Q2w` (orphan `RZEtpF` deprecated) |
| Shopify store | `q1xbgj-t8.myshopify.com` / `la-chamana-8065` |

### Canonical artifact paths (copy these as starting templates)

| Path | Contents |
|------|----------|
| `vault/plans/alter-blue/00-overview.md` | Master plan, locked decisions, phases, costs |
| `vault/plans/alter-blue/v1.2-sprint-runbook.md` | 27-step Phase-1 runbook |
| `vault/plans/alter-blue/artifacts/gtm-install-snippets.md` | Verbatim GTM head + body snippets |
| `vault/plans/alter-blue/artifacts/utm-passthrough.js` | UTM → hidden-field capture script |
| `vault/plans/alter-blue/artifacts/landing-vertical-section-spec.md` | 5-block landing spec |
| `vault/plans/alter-blue/artifacts/landing-corporate-offsites-published-body.html` | POC landing body |
| `vault/plans/alter-blue/artifacts/phase2-seo-base-paste-ready.md` | SEO meta + JSON-LD + hreflang Liquid |
| `vault/plans/alter-blue/artifacts/phase2-locale-fix.md` | UY→MX Markets migration |
| `vault/plans/alter-blue/artifacts/phase2-klaviyo-flows-iru-walkthrough.md` | 14 flow templates walkthrough |
| `vault/plans/alter-blue/artifacts/phase3-server-side-scaffold.md` | Stape sGTM + 2 Cloudflare Workers |
| `ops/tracking/v1.2-phase1-status.md` | Live as-built status log |
| `docs/content-factory-integration-plan.md` | External copy-console integration plan |

---

*End of handoff. Build Part A first; then Part B, phase by phase, verifying each gate before opening
the next.*
