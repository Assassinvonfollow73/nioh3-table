from nioh3_table.core.attacher import ProcessAttacher
from nioh3_table.config.schema import TrainerConfig
from nioh3_table.features.godmode import GodmodeFeature
from nioh3_table.features.infinite_ki import InfiniteKiFeature
from nioh3_table.features.ammo_refill import AmmoRefillFeature
from nioh3_table.features.amrita_multiplier import AmritaMultiplierFeature


def build_features(attacher: ProcessAttacher, cfg: TrainerConfig):
    return [
        GodmodeFeature(attacher, cfg),
        InfiniteKiFeature(attacher, cfg),
        AmmoRefillFeature(attacher, cfg),
        AmritaMultiplierFeature(attacher, cfg),
    ]