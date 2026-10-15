<!-- Added by Judge FR/UE for BASE-008, 2026-10-15. -->

# Fork community lifecycle — 0.1.0

This contract takes precedence over generic directory-copy instructions in
the inherited hub workflows. Keep all existing allowlist, raw-source,
read-only scan, QA, role-routing, freshness and human-approval gates.
`--apply` requests review; it never authorizes unattended changes.

Only install standalone community skills. Given upstream slug `example`, the
directory and frontmatter `name` become `judge-fr-eu-example`, under
`~/.claude/skills/`. Show this exact identity and all rewritten content during
review. Review all candidate file-write targets: reject instructions targeting
another distribution. Do not install into any internal plugin. Internal
manifest identifiers and their directory keys are both off-limits, including
the original distribution's twelve domain names. The set in the helper is
canonical and must match the packaged template's built-in list.

The filesystem stage is `${CLAUDE_PLUGIN_ROOT}/scripts/community_store.py`.
Use an argument array, after approval. The helper never fetches or executes
candidate content. Stage any validated freshness preamble in the reviewed
candidate before invoking it; keep the original name in candidate frontmatter.
The helper renames that identity on copying. Re-run the reviewed transformation
for every new version. Do not reuse an original distribution's journal,
consent, profile or allowlist.

```text
python "${CLAUDE_PLUGIN_ROOT}/scripts/community_store.py" install example --source <reviewed-candidate> --sha <exact-commit> --metadata <reviewed-json> --approved
python "${CLAUDE_PLUGIN_ROOT}/scripts/community_store.py" update example --source <reviewed-candidate> --sha <new-exact-commit> --metadata <reviewed-json> --approved
python "${CLAUDE_PLUGIN_ROOT}/scripts/community_store.py" rollback example --sha <saved-exact-commit> --approved
python "${CLAUDE_PLUGIN_ROOT}/scripts/community_store.py" disable example --approved
python "${CLAUDE_PLUGIN_ROOT}/scripts/community_store.py" enable example --approved
python "${CLAUDE_PLUGIN_ROOT}/scripts/community_store.py" uninstall example --approved
```

`--approved` records that the calling workflow completed its gates; it does
not replace them. Include the source registry, publisher, license and license
source, deployment context, review verdict, validated freshness tokens/URLs
and quoted rejected raw tokens in the reviewed metadata JSON. Metadata is
stored as data under `metadata` and cannot override identity or paths.

The authoritative `install-log.yaml` is schema-1 JSON (valid YAML), with
`namespace: judge-fr-eu` and append-only `events`. The helper owns this file;
do not append ad hoc YAML or edit old events. Freshness decisions are structured
metadata on the next approved operation; if only recording a reminder, use
the separate `freshness-review.yaml` under this hub's config root, through
the storage helper. The profile's starter-pack table is a display projection,
updated after the helper succeeds; it never authorizes lifecycle operations.

Every event includes upstream slug, installed identity, canonical lexical
path with all links refused, exact SHA, state, contents digest and timestamp.
The latest state may be enabled or disabled for removal; updates and rollback
require enabled state. Unknown, foreign, malformed or stale journals refuse
operations. Missing or locally edited files require preservation and comparison
before any new action. Do not use an original journal to reconstruct authority.

Backups live under this hub's fork config root at
`backups/judge-fr-eu-<skill>/<sha>/`. Each backup's path, contents digest,
metadata and SHA are recorded in the fork journal. Refuse occupied backup
paths. Rollback accepts only a recorded backup with matching contents and
identity, and preserves the replaced version as another backup. Disable and
enable rename SKILL.md, hooks and agent entry points with collision checks;
uninstall removes only the logged fork directory and keeps user configuration
and backups. Every candidate tree, installation, backup, root and ancestor is
checked for traversal, links, hard links and junctions before mutation.

This helper deliberately refuses legacy journal shapes. Judge FR/UE 0.1.0
starts a new journal; assisted import and format migration need a separate
story. A failed or interrupted operation requires reviewing the lock, staging
and current files. Never overwrite a destination to repair a partial operation.
