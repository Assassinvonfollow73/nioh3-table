"""Entry point — attach to nioh3.exe and launch the overlay."""
from __future__ import annotations

import sys

from nioh3_table.core.attacher import ProcessAttacher
from nioh3_table.core.overlay import TrainerOverlay
from nioh3_table.config.loader import load_config
from nioh3_table.utils.logger import get_logger

log = get_logger("bootstrap")


def main() -> int:
    cfg = load_config()
    attacher = ProcessAttacher(target=cfg.process_name)
    if not attacher.attach():
        log.error("could not attach to %s", cfg.process_name)
        return 1

    log.info("attached pid=%s base=0x%x", attacher.pid, attacher.base_address)
    overlay = TrainerOverlay(attacher=attacher, config=cfg)
    overlay.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())