#!/usr/bin/env python3
"""Validate agent template files in .github/agents/.

Each agent file must have YAML frontmatter with at least:
  - name
  - description

Exits with code 1 if any file fails validation.
"""

import sys
import os
import glob

AGENTS_DIR = os.path.join(
    os.path.dirname(__file__), '..', '..', '.github', 'agents'
)
REQUIRED_FIELDS = ('name', 'description')


def parse_frontmatter(text: str) -> dict | None:
    """Return parsed frontmatter dict, or None if missing/malformed."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        return None
    end = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == '---':
            end = i
            break
    if end is None:
        return None
    fm: dict = {}
    for line in lines[1:end]:
        if ':' in line:
            key, _, value = line.partition(':')
            fm[key.strip()] = value.strip()
    return fm


def validate_agent(path: str) -> list[str]:
    """Return list of error messages for the given agent file."""
    errors: list[str] = []
    with open(path, encoding='utf-8') as fh:
        content = fh.read()

    fm = parse_frontmatter(content)
    if fm is None:
        errors.append(f'{path}: missing or malformed YAML frontmatter')
        return errors

    for field in REQUIRED_FIELDS:
        if not fm.get(field):
            errors.append(f'{path}: missing required frontmatter field "{field}"')

    return errors


def main() -> int:
    pattern = os.path.join(AGENTS_DIR, '*.agent.md')
    agent_files = sorted(glob.glob(pattern))

    if not agent_files:
        print(f'WARNING: no agent files found in {AGENTS_DIR}', file=sys.stderr)
        return 0

    all_errors: list[str] = []
    for path in agent_files:
        errors = validate_agent(path)
        if errors:
            all_errors.extend(errors)
        else:
            print(f'✓ {os.path.basename(path)}')

    if all_errors:
        print('\nValidation failed:', file=sys.stderr)
        for err in all_errors:
            print(f'  ✗ {err}', file=sys.stderr)
        return 1

    print(f'\nAll {len(agent_files)} agent template(s) passed validation.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
