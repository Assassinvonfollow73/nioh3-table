"""Amrita gain multiplier — scales the amrita drop value on kill."""
from __future__ import annotations

from nioh3_table.core.feature import Feature
from nioh3_table.core.attacher import ProcessAttacher
from nioh3_table.config.schema import TrainerConfig
from nioh3_table.offsets.resolver import resolve_amrita_gain


class AmritaMultiplierFeature(Feature):
    name = "amrita_multiplier"
    hotkey = "f4"

    def __init__(self, attacher: ProcessAttacher, cfg: TrainerConfig) -> None:
        super().__init__(attacher)
        self._cfg = cfg

    def enable(self) -> None:
        addr = resolve_amrita_gain(self._attacher)
        self._attacher.write_float(addr, self._cfg.amrita_multiplier)

    def disable(self) -> None:
        addr = resolve_amrita_gain(self._attacher)
        self._attacher.write_float(addr, 1.0)