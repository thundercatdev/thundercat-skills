#!/usr/bin/env python3
"""Rank raw competitor signals by priority tier (P1 > P2 > P3).

Optional helper for the competitive-intel-content-brief skill.
Usage: python prioritize_signals.py '[{"signal":"...","priority":"P2"}, ...]'
"""

from __future__ import annotations

import json
import sys

_ORDER = {'P1': 0, 'P2': 1, 'P3': 2}


def prioritize(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    """Sort signal rows by priority then signal text."""
    return sorted(
        rows,
        key=lambda row: (_ORDER.get(str(row.get('priority') or 'P3').upper(), 9), str(row.get('signal') or '')),
    )


def main() -> int:
    raw = sys.argv[1] if len(sys.argv) > 1 else '[]'
    rows = json.loads(raw)
    if not isinstance(rows, list):
        raise SystemExit('Expected JSON array of signal objects')
    print(json.dumps(prioritize(rows), indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
