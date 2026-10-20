"""Godmode — keeps player HP pinned at max each tick."""
from __future__ import annotations

import threading
import time

from nioh3_table.core.feature import Feature
from nioh3_table.core.attacher import ProcessAttacher
from nioh3_table.config.schema import TrainerConfig
from nioh3_table.offsets.resolver import resolve_player_hp


class GodmodeFeature(Feature):
    name = "godmode"
    hotkey = "f1"

    def __init__(self, attacher: ProcessAttacher, cfg: TrainerConfig) -> None:
        super().__init__(attacher)
        self._cfg = cfg
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None

    def enable(self) -> None:
        self._stop.clear()
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def disable(self) -> None:
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=1.0)

    def _loop(self) -> None:
        hp_addr = resolve_player_hp(self._attacher)
        while not self._stop.is_set():
            try:
                self._attacher.write_float(hp_addr, 9999.0)
            except Exception:
                return
            time.sleep(0.05)