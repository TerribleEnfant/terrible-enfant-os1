# Herramienta: Email transaccional (Resend)

**Owner:** Boris
**Propósito:** envío programático de emails desde automatizaciones (V1: recaps de reuniones del auto-miner).
**Status:** activo (V1, acotado al recap interno) · pendiente confirmar dominio sender + DKIM

---

## Para qué se usa

- **Recap de reuniones** (`WF_OPS_MINE`) → a participantes **internos** de la llamada.

## Qué NO se usa (todavía)

- Comunicaciones externas (clientes, prensa, partners) → siguen gated por **Comando**, manual.
- Email marketing / newsletter / transaccional de e-commerce → otro stack (Klaviyo/SendGrid, BRA).

## Regla de destinatarios (recap)

Destinatarios = **participantes de la llamada (de Read AI) ∩ allowlist interna** (dominio interno
o email explícito en `config/te-mining.json` → `email`). Invitados externos se descartan. Si no
queda ningún interno, no se manda (no es error). Ver `scripts/send_recap.py`.

## Gobierno

El auto-send está autorizado **solo** para el recap interno (amendment M2, ver `TE-OS_M1.md §11`).
Cualquier otro envío programático a externos requiere aprobación de **Comando**.

---

## Auth (1Password)

> Convención del Canon: los secretos nunca van al repo. 1Password es el vault de record;
> se inyectan en runtime vía `op`. Documentar acá solo el **nombre del item**, nunca el valor.

- **`TE_RESEND_API_KEY`** — vault item: `TODO: vault ref`. En GitHub Actions va como secret del repo.
- **Dominio sender + DKIM:** `TODO` — configurar en Resend y completar `email.from` en `config/te-mining.json`.
