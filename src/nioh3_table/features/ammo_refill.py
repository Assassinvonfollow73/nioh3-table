"""Ammo refill — tops up ranged weapon ammo counts."""
from __future__ import annotations

from nioh3_table.core.feature import Feature
from nioh3_table.core.attacher import ProcessAttacher
from nioh3_table.config.schema import TrainerConfig
from nioh3_table.offsets.resolver import resolve_ammo_slots


class AmmoRefillFeature(Feature):
    name = "ammo_refill"
    hotkey = "f3"

    def __init__(self, attacher: ProcessAttacher, cfg: TrainerConfig) -> None:
        super().__init__(attacher)
        self._cfg = cfg

    def enable(self) -> None:
        for addr in resolve_ammo_slots(self._attacher):
            self._attacher.write_float(addr, float(self._cfg.ammo_max))

    def disable(self) -> None:
        pass