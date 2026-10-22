"""Build and verify a private, local handoff packet from selected project files."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def contained_file(project, name):
    candidate = project / name
    if candidate.is_symlink() or not candidate.is_file():
        raise ValueError('Missing or symbolic-link source: ' + name)
    resolved = candidate.resolve()
    if not resolved.is_relative_to(project.resolve()):
        raise ValueError('Source outside project: ' + name)
    if candidate.stat().st_size > 10_000_000:
        raise ValueError('Source exceeds 10 MB: ' + name)
    return candidate


def create(project, destination, record, sources):
    project = project.resolve()
    if destination.parent.is_symlink():
        raise ValueError('Packet directory must not be a symbolic link')
    if shutil.which('git'):
        tracked = subprocess.run(['git', '-C', str(project), 'ls-files', '--', '.agent-handoff'],
                                 capture_output=True, text=True)
        if tracked.returncode == 0 and tracked.stdout.strip():
            raise ValueError('The packet area already contains tracked Git files')
    if destination.exists() or destination.is_symlink():
        raise ValueError('Destination exists: ' + str(destination))
    if not destination.parent.resolve().is_relative_to(project):
        raise ValueError('Destination must be within project')
    chosen = [('analysis.md', contained_file(project, record))]
    for index, name in enumerate(sources, 1):
        chosen.append((f'evidence/{index:02d}-{Path(name).name}', contained_file(project, name)))
    ignore = destination.parent / '.gitignore'
    if (destination.parent / 'INDEX.md').is_symlink():
        raise ValueError('Index must not be a symbolic link')
    if ignore.exists():
        if ignore.is_symlink():
            raise ValueError('Ignore file must not be a symbolic link')
        if ignore.read_text() != '*\n':
            raise ValueError('Expected a private .agent-handoff/.gitignore')
    destination.mkdir(parents=True)
    if not ignore.exists():
        ignore.write_text('*\n')
    entries = []
    for relative, source in chosen:
        output = destination / relative
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, output)
        if digest(source) != digest(output):
            raise ValueError('Copy verification failed: ' + str(output))
        entries.append({'file': relative, 'source': source.relative_to(project).as_posix(),
                        'sha256': digest(output), 'bytes': output.stat().st_size})
    (destination / 'manifest.json').write_text(json.dumps({'schema': 1, 'files': entries}, indent=2) + '\n')
    update_index(destination)
    return verify(destination)


def update_index(destination):
    index = destination.parent / 'INDEX.md'
    if index.is_symlink():
        raise ValueError('Index must not be a symbolic link')
    heading = '# Investigation records\n\n| Topic | Record | Evidence |\n| --- | --- | --- |\n'
    title = (destination / 'analysis.md').read_text().splitlines()[0].lstrip('# ').strip().replace('|', '/')
    line = f'| {title} | [{destination.name}]({destination.name}/analysis.md) | [manifest]({destination.name}/manifest.json) |\n'
    current = index.read_text() if index.exists() else heading
    if line not in current:
        index.write_text(current + line)


def verify(destination):
    if destination.is_symlink() or destination.parent.is_symlink():
        raise ValueError('Packet directory must not be a symbolic link')
    if (destination / 'manifest.json').is_symlink():
        raise ValueError('Manifest must not be a symbolic link')
    manifest = json.loads((destination / 'manifest.json').read_text())
    if manifest['schema'] != 1 or not manifest['files']:
        raise ValueError('Invalid manifest')
    seen = set()
    for item in manifest['files']:
        relative = item['file']
        if relative in seen:
            raise ValueError('Duplicate path')
        seen.add(relative)
        candidate = destination / relative
        if candidate.is_symlink() or not candidate.is_file() or not candidate.resolve().is_relative_to(destination.resolve()):
            raise ValueError('Missing or unsafe packet file: ' + relative)
        if digest(candidate) != item['sha256'] or candidate.stat().st_size != item['bytes']:
            raise ValueError('Packet mismatch: ' + relative)
    return {'status': 'passed', 'files': len(seen), 'destination': str(destination)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, required=True)
    parser.add_argument('--id', required=True, help='lowercase name for this handoff')
    parser.add_argument('--record', help='project-relative Markdown record for creation')
    parser.add_argument('--source', action='append', default=[])
    parser.add_argument('--verify', action='store_true', help='check an existing packet')
    args = parser.parse_args()
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,63}', args.id):
        parser.error('--id must be lowercase letters, digits and hyphens (up to 64 characters)')
    project = args.project.resolve()
    destination = project / '.agent-handoff' / args.id
    if not args.verify and not args.record:
        parser.error('--record is required when creating a packet')
    print(json.dumps(verify(destination) if args.verify else create(project, destination, args.record, args.source)))


if __name__ == '__main__':
    main()
