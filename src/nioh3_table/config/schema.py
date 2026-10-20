"""Typed config schema for the trainer."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TrainerConfig:
    process_name: str = "nioh3.exe"
    max_ki: float = 100.0
    ammo_max: int = 99
    amrita_multiplier: float = 5.0
    hotkeys: dict[str, str] = field(default_factory=dict)
    log_level: str = "INFO"