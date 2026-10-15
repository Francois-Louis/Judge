<!-- Added by Judge FR/UE for BASE-008, 2026-10-15. -->

# Judge FR/UE storage boundary — 0.1.0

This file is packaged with every internal plugin. Load it before any durable
data access, including implicit skill triggers and scheduled agents. This
technical migration does not adapt the inherited legal tasks to France/EU.

The only durable root is `~/.claude/plugins/config/judge-fr-eu/`.
Each plugin uses its existing domain directory under that root; its manifest
identifier adds `judge-fr-eu-` but its data directory does not. The only shared
file is `company-profile.md`, shared among this fork's plugins only.
Never search another distribution or a cache for profiles or missing data.
A missing practice profile requires a fresh interview, including when called
with `--check-integrations`. Preserve an existing profile and paused answers.
Use the packaged `CLAUDE.md` only as a scaffold; do not treat its legal examples
or defaults as confirmed France/EU rules. Never write durable data in a package.

For every access to a profile, company profile, matter, archive, register,
policy, proposal, verification log or output, use the packaged Python helper
at `${CLAUDE_PLUGIN_ROOT}/scripts/judge_store.py` (Python 3.12 or later).
If it cannot run, stop before data access and report that limitation.
Do not bypass it with Read/Write, shell redirection or a fallback path.
User-provided source documents and connectors remain explicit inputs; they
are not implicitly imported configurations.

Invoke the helper with an argument array; never interpolate user slugs or
contents into a shell command. All data paths are relative to this plugin's
domain root. Forward slashes separate components. The helper refuses absolute
paths, `..`, empty components, Windows drive/UNC/alternate-stream paths,
symlinks, junctions, reparse points and hard links, including in ancestors.
Stop on refusal. Do not normalize a rejected slug and retry silently.

Examples (replace the plugin root with its actual installed path):

```text
python "${CLAUDE_PLUGIN_ROOT}/scripts/judge_store.py" read CLAUDE.md
python "${CLAUDE_PLUGIN_ROOT}/scripts/judge_store.py" read company-profile.md --shared
python "${CLAUDE_PLUGIN_ROOT}/scripts/judge_store.py" list matters
python "${CLAUDE_PLUGIN_ROOT}/scripts/judge_store.py" create CLAUDE.md
python "${CLAUDE_PLUGIN_ROOT}/scripts/judge_store.py" create matters/demo/matter.md
python "${CLAUDE_PLUGIN_ROOT}/scripts/judge_store.py" append matters/demo/history.md
python "${CLAUDE_PLUGIN_ROOT}/scripts/judge_store.py" replace CLAUDE.md --expected-sha256 <reviewed-digest>
python "${CLAUDE_PLUGIN_ROOT}/scripts/judge_store.py" move matters/demo --destination matters/_archived/demo
```

`create`, `replace` and `append` take UTF-8 text on stdin, passed as data by
the calling tool. `read` returns JSON with content, SHA-256, status and the
access trace. `list` checks each child before descending and returns relative
paths; never enumerate durable trees with an unguarded recursive Glob.
`path` validates a relative destination. `create` refuses an existing file,
including an empty file. `move` refuses an existing destination and checks
descendants before moving a directory. A read missing profile returns
`interview-required`; no fallback is attempted. `replace` requires the digest
from the reviewed read; stop and compare if the file changed. Preserve answers
outside an explicitly agreed section edit. `--shared` permits only the company
profile. `--home` is for disposable offline fixtures, never a user-supplied
way to switch an installed session to another distribution's home.

The helpers are local guards, not an operating-system sandbox. Do not run
concurrent operations or allow another process to mutate their trees during
an operation. Hub operations take a lock; an abandoned lock requires review
of the journal and staging before recovery. No silent recovery or overwrite.

Updates and rollback replace the package only. Configurations and matters
stay outside its cache and keep their current format. Durable customization
belongs in the profile, or in a reviewed private package/branch with its own
identifier; direct edits inside an installed cache are replaceable.

The hub has an additional packaged community-lifecycle.md reference in its
references directory. Community operations must use its
helper after the existing trust review and explicit approval gates.
Other plugins do not load that hub-only reference.
