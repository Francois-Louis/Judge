# Added by Judge FR/UE for LIV-001, 2026-10-16.
"""Build a bounded Judge FR/UE lot: selected plugins and a one-lot marketplace.

python scripts/build-lot.py --lot judge-fr-eu-lot-001 --plugin employment-legal \
    --notes backlog/04-livraison/liv-001-annexes/liv-001-notes-version.md --out <dir-outside-checkout>

The lot copies only git-tracked files of each selected plugin, from the working
tree (default) or from --rev. It refuses an output inside the checkout or an
existing output, untracked files in a selected plugin, links, and a marketplace
entry whose name/description/author differ from the plugin manifest. It writes
lot-inventory.json (SHA-256 of every file) and a reproducible ZIP next to the
lot directory. Nothing is installed, published or pushed.
"""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def git(*args, binary=False):
    out = subprocess.run(['git', *args], cwd=ROOT, check=True, capture_output=True).stdout
    return out if binary else out.decode('utf-8')


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--lot', required=True, help='Lot directory name, e.g. judge-fr-eu-lot-001.')
    parser.add_argument('--plugin', action='append', required=True,
                        help='Plugin directory at the repository root; repeat for several.')
    parser.add_argument('--notes', type=Path, required=True,
                        help='Markdown release notes copied as the lot README.md.')
    parser.add_argument('--out', type=Path, required=True, help='Parent directory outside the checkout.')
    parser.add_argument('--rev', help='Build from this git revision instead of the working tree.')
    args = parser.parse_args()

    out_parent = args.out.resolve()
    if out_parent == ROOT or ROOT in out_parent.parents:
        sys.exit('refused: output must be outside the checkout')
    lot_dir = out_parent / args.lot
    zip_path = out_parent / (args.lot + '.zip')
    if lot_dir.exists() or zip_path.exists():
        sys.exit(f'refused: {lot_dir} or {zip_path} already exists')

    head = git('rev-parse', 'HEAD').strip()
    rev = git('rev-parse', args.rev).strip() if args.rev else None

    def read(path):
        if rev:
            return git('show', f'{rev}:{path}', binary=True)
        file = ROOT / path
        if file.is_symlink():
            sys.exit(f'refused: link {path}')
        return file.read_bytes()

    market = json.loads(read('.claude-plugin/marketplace.json'))
    files, modified, plugins = {}, [], []
    for name in args.plugin:
        if PurePosixPath(name).name != name or name.startswith('.'):
            sys.exit(f'refused: plugin must be a top-level directory name: {name}')
        entry = next((p for p in market['plugins'] if p['source'] == './' + name), None)
        if entry is None:
            sys.exit(f'refused: {name} is not in the marketplace')
        manifest = json.loads(read(f'{name}/.claude-plugin/plugin.json'))
        for field in ('name', 'description', 'author'):
            if entry.get(field) != manifest.get(field):
                sys.exit(f'refused: marketplace {field} differs from {name}/.claude-plugin/plugin.json')
        if rev:
            tracked = git('ls-tree', '-r', '--name-only', '-z', rev, '--', name).split('\0')
        else:
            tracked = git('ls-files', '-z', '--', name).split('\0')
            untracked = git('ls-files', '--others', '--exclude-standard', '-z', '--', name).split('\0')
            if any(untracked):
                sys.exit(f'refused: untracked files in {name}: {[u for u in untracked if u]}')
            modified += [m for m in git('diff', '--name-only', '-z', 'HEAD', '--', name).split('\0') if m]
        for path in filter(None, tracked):
            files[path] = read(path)
        plugins.append({**entry, 'version': manifest['version']})

    files['LICENSE'] = read('LICENSE')
    files['NOTICE'] = read('NOTICE')
    if not rev:
        modified += [m for m in git('diff', '--name-only', '-z', 'HEAD', '--',
                                    'LICENSE', 'NOTICE', '.claude-plugin/marketplace.json').split('\0') if m]
    files['README.md'] = args.notes.read_bytes()
    lot_market = {
        '$schema': market.get('$schema'),
        'name': market['name'],
        'description': (f'Judge FR/UE bounded lot {args.lot}: '
                        + ', '.join(f"{p['name']} {p['version']}" for p in plugins)
                        + '. Only the plugins listed here are delivered; see README.md for adapted scope and limits.'),
        'owner': market['owner'],
        'plugins': [{k: v for k, v in p.items() if k != 'version'} for p in plugins],
    }
    files['.claude-plugin/marketplace.json'] = (
        json.dumps(lot_market, ensure_ascii=False, indent=2) + '\n').encode('utf-8')

    inventory = {
        'lot': args.lot,
        'source': {'mode': 'git-revision' if rev else 'working-tree', 'revision': rev or head,
                   'head': head, 'modified_vs_head': sorted(modified)},
        'plugins': [{'name': p['name'], 'source': p['source'], 'version': p['version']} for p in plugins],
        'files': {path: sha256(data) for path, data in sorted(files.items())},
    }
    files['lot-inventory.json'] = (json.dumps(inventory, ensure_ascii=False, indent=2) + '\n').encode('utf-8')

    for path, data in files.items():
        target = lot_dir / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(files):
            info = zipfile.ZipInfo(f'{args.lot}/{path}', date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, files[path])
    print(json.dumps({'lot_dir': str(lot_dir), 'zip': str(zip_path),
                      'zip_sha256': sha256(zip_path.read_bytes()), 'files': len(files),
                      'source': inventory['source'], 'plugins': inventory['plugins']},
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
