"""Helper to sanity-check the offset YAML against a running process."""
from __future__ import annotations

import sys

from nioh3_table.core.attacher import ProcessAttacher
from nioh3_table.offsets import resolver


def main() -> int:
    att = ProcessAttacher()
    if not att.attach():
        print("nioh3.exe not running", file=sys.stderr)
        return 1
    print(f"hp addr = 0x{resolver.resolve_player_hp(att):x}")
    print(f"ki addr = 0x{resolver.resolve_ki_pool(att):x}")
    return 0


if __name__ == "__main__":
    sys.exit(main())