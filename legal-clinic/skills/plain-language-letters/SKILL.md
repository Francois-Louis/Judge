---
name: plain-language-letters
description: >
  Reference: DEPRECATED — use `/client-letter` for routine correspondence or
  `/status client` for substantive updates. Split into two more focused skills
  during the v2 rebuild. Kept as a redirect for migration.
user-invocable: false
---

<!-- Modified by Judge FR/UE for BASE-008 (2026-10-15): technical identity and storage isolation; legal adaptation pending. -->

Before accessing profiles, matters, registers or outputs, read `${CLAUDE_PLUGIN_ROOT}/references/isolation.md` and follow its storage boundary.

# [DEPRECATED] Plain-Language Letters → see `/client-letter` and `/status client`

This skill was split during the v2 rebuild:

- **Routine correspondence** (appointment confirms, document requests, brief
  "we filed it" updates) → `${CLAUDE_PLUGIN_ROOT}/skills/client-letter/` — use `/client-letter [type]`

- **Substantive client status updates** → `${CLAUDE_PLUGIN_ROOT}/skills/status/` in client-facing
  mode — use `/status client`

Both apply the plain-language standards (reading level, no jargon) from CLAUDE.md.

See the respective SKILL.md files for full workflows.
