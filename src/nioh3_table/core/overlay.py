"""Console overlay that binds hotkeys to feature toggles."""
from __future__ import annotations

import keyboard
from rich.console import Console

from nioh3_table.core.attacher import ProcessAttacher
from nioh3_table.config.schema import TrainerConfig
from nioh3_table.features import build_features
from nioh3_table.utils.logger import get_logger

log = get_logger("overlay")


class TrainerOverlay:
    def __init__(self, attacher: ProcessAttacher, config: TrainerConfig) -> None:
        self._attacher = attacher
        self._config = config
        self._console = Console()
        self._features = build_features(attacher, config)

    def run(self) -> None:
        self._console.print("[bold green]Nioh 3 Trainer[/] — loaded")
        for feat in self._features:
            if feat.hotkey:
                keyboard.add_hotkey(feat.hotkey, feat.toggle)
                self._console.print(f"  {feat.hotkey:<12} -> {feat.name}")
        self._console.print("press ctrl+c to exit")
        try:
            keyboard.wait("ctrl+c")
        except KeyboardInterrupt:
            log.info("shutting down")