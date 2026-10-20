"""Infinite Ki — clamps the ki pool to its maximum every tick."""
from __future__ import annotations

from nioh3_table.core.feature import Feature
from nioh3_table.core.attacher import ProcessAttacher
from nioh3_table.config.schema import TrainerConfig
from nioh3_table.offsets.resolver import resolve_ki_pool


class InfiniteKiFeature(Feature):
    name = "infinite_ki"
    hotkey = "f2"

    def __init__(self, attacher: ProcessAttacher, cfg: TrainerConfig) -> None:
        super().__init__(attacher)
        self._cfg = cfg

    def enable(self) -> None:
        addr = resolve_ki_pool(self._attacher)
        self._attacher.write_float(addr, self._cfg.max_ki)

    def disable(self) -> None:
        pass