"""Base class for every trainer feature module."""
from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum

from nioh3_table.core.attacher import ProcessAttacher


class FeatureState(Enum):
    IDLE = "idle"
    ACTIVE = "active"
    ERROR = "error"


class Feature(ABC):
    """A toggleable trainer feature (godmode, infinite ki, etc.)."""

    name: str = "unnamed"
    hotkey: str = ""

    def __init__(self, attacher: ProcessAttacher) -> None:
        self._attacher = attacher
        self.state = FeatureState.IDLE

    @abstractmethod
    def enable(self) -> None: ...

    @abstractmethod
    def disable(self) -> None: ...

    def toggle(self) -> None:
        if self.state is FeatureState.ACTIVE:
            self.disable()
            self.state = FeatureState.IDLE
        else:
            self.enable()
            self.state = FeatureState.ACTIVE