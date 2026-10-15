---
name: disable
description: >
  Disable a community skill installed through the hub without removing its
  files. Use when the user wants to temporarily quiet a community skill
  ("disable [skill]"), stop its hooks from firing while keeping its config,
  or re-enable a previously disabled skill.
argument-hint: "[skill name]"
---

For every community lifecycle operation, first load `${CLAUDE_PLUGIN_ROOT}/references/community-lifecycle.md`. Its helper owns installation, updates, backups, rollback, disabling, enabling, uninstall and the fork journal.

<!-- Modified by Judge FR/UE for BASE-008 (2026-10-15): technical identity and storage isolation; legal adaptation pending. -->

Before accessing profiles, matters, registers or outputs, read `${CLAUDE_PLUGIN_ROOT}/references/isolation.md` and follow its storage boundary.

# /disable

Run the `disable` workflow from the skill-manager reference skill against the
named skill.

What disable does:

- Renames the skill's `SKILL.md` to `SKILL.md.disabled` so Claude no longer
  discovers it as an active skill. Files, references, templates, and config
  stay in place.
- If the skill ships hooks in `hooks/hooks.json`, also rename that file to
  `hooks.json.disabled` so no automatic triggers fire while the skill is
  disabled.
- Logs the action to
  `~/.claude/plugins/config/judge-fr-eu/legal-builder-hub/install-log.yaml`.

Safety rules:

1. **Only disable community skills installed through this hub.** Same check
   as uninstall — consult the install log and CLAUDE.md installed table.
2. **Never disable a first-party plugin's skill.** Off-limits.
3. **Confirm before renaming.** Show the paths, get explicit `yes`.

Re-enable by running the command again with the same skill name — the
skill-manager workflow recognizes a disabled skill and flips the rename back.

> Detailed uninstall, disable, and re-enable workflows live in the
> `skill-manager` reference skill — load it before doing substantive work.
