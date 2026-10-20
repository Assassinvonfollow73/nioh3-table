"""Shared logger factory."""
from __future__ import annotations

import logging
import os


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(f"nioh3.{name}")
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("[%(asctime)s] %(name)s %(levelname)s: %(message)s")
        )
        logger.addHandler(handler)
        logger.setLevel(os.getenv("NIOH3_LOG_LEVEL", "INFO"))
    return logger