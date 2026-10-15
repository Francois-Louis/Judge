#!/usr/bin/env bash
# Copyright 2026 Anthropic PBC
# SPDX-License-Identifier: Apache-2.0
# Modified by Judge FR/UE for BASE-008, 2026-10-15; BASE-009 interpreter portability.
# Dry-run every managed-agent cookbook and assert the resolved POST /v1/agents
# bodies are well-formed: valid JSON, depth-1, non-empty system prompts, no
# output_schema. Exits non-zero if any cookbook fails.
set -euo pipefail
export PYTHONUTF8=1
# Windows ships a Store stub named python3; use the first interpreter that runs.
if [[ -z "${PYTHON:-}" ]]; then
  for c in python3 python; do "$c" -c '' 2>/dev/null && { PYTHON=$c; break; }; done
fi
[[ -n "${PYTHON:-}" ]] || { echo "requires python 3" >&2; exit 1; }
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail=0

# Tool-scope lint: assert orchestrators do not carry MCP toolsets, Write, or
# Slack tools. Orchestrators emit handoff_request instead of calling these directly.
if ! "$PYTHON" "$ROOT/scripts/lint-tool-scope.py"; then
  echo "  ✗ tool-scope lint" >&2
  fail=1
fi

for d in "$ROOT"/managed-agent-cookbooks/*/; do
  slug=$(basename "$d")
  if ! JUDGE_DEPLOYMENT_ID="offline-$slug" bash "$ROOT/scripts/deploy-managed-agent.sh" "$slug" --dry-run | tail -n +2 | "$PYTHON" -c "
import json,sys
b=json.load(sys.stdin)
errs=[]
for i,x in enumerate(b):
    if not x.get('system'): errs.append(f'{x.get(\"name\")}: empty system')
    if not x.get('name', '').startswith('judge-fr-eu-'): errs.append('missing fork agent identity')
    expected='./judge-fr-eu-runs/offline-'+sys.argv[1]+'/'+sys.argv[1]+'/out/'
    if expected not in x.get('system', ''): errs.append('missing isolated output path')
    if './out/' in x.get('system', ''): errs.append('unbound original output path')
    if x.get('metadata', {}).get('judge_fr_eu_cookbook') != 'judge-fr-eu/'+sys.argv[1]: errs.append('wrong fork tag')
    if i<len(b)-1 and x.get('callable_agents'): errs.append(f'{x.get(\"name\")}: depth>1 (subagent has callable_agents)')
if 'output_schema' in json.dumps(b): errs.append('output_schema leaked into a body')
if errs:
    for e in errs: print(f'      {e}', file=sys.stderr)
    sys.exit(1)
print(f'  ✓ {sys.argv[1]:24s} {len(b)} bodies')
" "$slug"; then
    echo "  ✗ $slug" >&2
    fail=1
  fi
done
exit $fail
