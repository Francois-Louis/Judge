#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Added by Judge FR/UE for BASE-008, 2026-10-15.
"""Per-deployment local workspace contract, also rendered into remote prompts."""

import argparse
import json
from pathlib import Path
import re

from judge_store import Store


ROLES = {"reg-monitor", "renewal-watcher", "docket-watcher", "diligence-grid", "launch-radar"}
RUN_ROOT = "judge-fr-eu-runs"


def output_prefix(deployment, role):
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,50}", deployment or "") or role not in ROLES:
        raise ValueError("explicit deployment slug and known cookbook role required")
    return f"./{RUN_ROOT}/{deployment}/{role}/out/"


def output_store(base, deployment, role):
    prefix = output_prefix(deployment, role)
    return Store(Path(base).absolute() / prefix.removeprefix("./"))


def prepare(base, deployment, role):
    store = output_store(base, deployment, role)
    run = store.root.parent
    # Refuse an existing workspace, including an empty directory.
    run.parent.mkdir(parents=True, exist_ok=True)
    run.mkdir()
    store.create("workspace.json", json.dumps({"namespace": "judge-fr-eu", "deployment": deployment, "role": role}))
    return store


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("role", choices=sorted(ROLES))
    parser.add_argument("--deployment", required=True)
    parser.add_argument("--prepare", action="store_true")
    args = parser.parse_args()
    prefix = output_prefix(args.deployment, args.role)
    if args.prepare:
        prepare(Path.cwd(), args.deployment, args.role)
    print(prefix)


if __name__ == "__main__":
    main()
