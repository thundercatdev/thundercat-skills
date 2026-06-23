#!/usr/bin/env python3
"""Validate manifest lock and published skill packages.

Usage (from repo root or apps/engram-skills):
  python apps/engram-skills/scripts/validate.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_FRONTMATTER_RE = re.compile(r'^---\r?\n(.*?)\r?\n---\r?\n?(.*)\Z', re.DOTALL)


def _parse_skill_id(skill_md: Path) -> str:
    """Return skill id from SKILL.md frontmatter."""
    import yaml

    content = skill_md.read_text(encoding='utf-8')
    match = _FRONTMATTER_RE.match(content.strip())
    if not match:
        raise ValueError(f'{skill_md}: missing YAML frontmatter')
    frontmatter = yaml.safe_load(match.group(1)) or {}
    if not isinstance(frontmatter, dict):
        raise ValueError(f'{skill_md}: frontmatter must be a mapping')
    metadata = frontmatter.get('metadata') if isinstance(frontmatter.get('metadata'), dict) else {}
    engram = metadata.get('engram') if isinstance(metadata.get('engram'), dict) else {}
    skill_id = str(engram.get('id') or frontmatter.get('name') or '').strip()
    if not skill_id:
        raise ValueError(f'{skill_md}: requires name or metadata.engram.id')
    return skill_id


def main() -> int:
    manifest_path = _ROOT / 'manifest.json'
    if not manifest_path.is_file():
        print(f'manifest missing: {manifest_path}', file=sys.stderr)
        return 1

    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    published = manifest.get('published')
    if not isinstance(published, list) or not published:
        print('manifest.published must be a non-empty list', file=sys.stderr)
        return 1

    errors: list[str] = []
    seen: set[str] = set()
    for entry in published:
        if not isinstance(entry, dict):
            errors.append('manifest entry must be an object')
            continue
        skill_id = str(entry.get('id') or '').strip()
        if not skill_id:
            errors.append('manifest entry missing id')
            continue
        if skill_id in seen:
            errors.append(f'duplicate manifest id: {skill_id}')
        seen.add(skill_id)

        skill_dir = _ROOT / skill_id
        skill_md = skill_dir / 'SKILL.md'
        if not skill_md.is_file():
            errors.append(f'missing package: {skill_id}/SKILL.md')
            continue
        try:
            parsed_id = _parse_skill_id(skill_md)
            if parsed_id != skill_id:
                errors.append(f'{skill_id}: SKILL.md id mismatch ({parsed_id})')
        except Exception as exc:
            errors.append(f'{skill_id}: {exc}')

    backlog_ref = str(manifest.get('backlog_ref') or '').strip()
    if backlog_ref and not (_ROOT / backlog_ref).is_file():
        errors.append(f'backlog_ref missing: {backlog_ref}')

    # Warn on unpublished skill dirs (not a failure — drafts are allowed locally).
    for child in sorted(_ROOT.iterdir()):
        if not child.is_dir() or child.name.startswith('.') or child.name in {'scripts', 'references'}:
            continue
        if not (child / 'SKILL.md').is_file():
            continue
        if child.name not in seen:
            print(f'note: unpublished draft package {child.name}')

    if errors:
        for err in errors:
            print(f'error: {err}', file=sys.stderr)
        return 1

    print(f'ok: {len(seen)} published skill(s) validated')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
