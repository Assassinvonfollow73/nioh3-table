from nioh3_table.config.loader import load_config
from nioh3_table.config.schema import TrainerConfig


def test_defaults_load():
    cfg = load_config()
    assert isinstance(cfg, TrainerConfig)
    assert cfg.process_name.endswith(".exe")
    assert cfg.max_ki > 0


def test_ammo_max_positive():
    cfg = load_config()
    assert cfg.ammo_max >= 1