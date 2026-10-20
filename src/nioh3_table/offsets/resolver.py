"""Load the YAML offset table and resolve live addresses."""
from __future__ import annotations

from pathlib import Path
import yaml

from nioh3_table.core.attacher import ProcessAttacher

_TABLE_PATH = Path(__file__).with_name("nioh3_offsets.yaml")
_TABLE: dict | None = None


def _table() -> dict:
    global _TABLE
    if _TABLE is None:
        with _TABLE_PATH.open("r", encoding="utf-8") as fh:
            _TABLE = yaml.safe_load(fh)
    return _TABLE


def _resolve(attacher: ProcessAttacher, entry: dict) -> int:
    return attacher.resolve(entry["base"], entry["chain"])


def resolve_player_hp(attacher: ProcessAttacher) -> int:
    return _resolve(attacher, _table()["player"]["hp"])


def resolve_ki_pool(attacher: ProcessAttacher) -> int:
    return _resolve(attacher, _table()["player"]["ki"])


def resolve_amrita_gain(attacher: ProcessAttacher) -> int:
    return _resolve(attacher, _table()["player"]["amrita_gain"])


def resolve_ammo_slots(attacher: ProcessAttacher) -> list[int]:
    entry = _table()["ammo"]["slots"]
    base = _resolve(attacher, entry)
    return [base + i * entry["stride"] for i in range(entry["count"])]