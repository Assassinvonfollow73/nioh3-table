"""Merge default.yaml with an optional local override."""
from __future__ import annotations

from pathlib import Path
import yaml

from nioh3_table.config.schema import TrainerConfig

_CFG_DIR = Path(__file__).parent
_DEFAULT = _CFG_DIR / "default.yaml"
_LOCAL = _CFG_DIR / "local.yaml"


def _read(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def load_config() -> TrainerConfig:
    data = {**_read(_DEFAULT), **_read(_LOCAL)}
    return TrainerConfig(**{k: v for k, v in data.items()
                            if k in TrainerConfig.__dataclass_fields__})