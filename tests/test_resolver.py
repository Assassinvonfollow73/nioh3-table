from unittest.mock import MagicMock

from nioh3_table.offsets import resolver


def _fake_attacher():
    att = MagicMock()
    att.base_address = 0x1000
    att.resolve.return_value = 0xDEAD
    return att


def test_resolve_player_hp_returns_int():
    att = _fake_attacher()
    addr = resolver.resolve_player_hp(att)
    assert isinstance(addr, int)
    assert addr == 0xDEAD


def test_resolve_ammo_slots_count():
    att = _fake_attacher()
    slots = resolver.resolve_ammo_slots(att)
    assert len(slots) == 6
    assert slots[1] - slots[0] == 0x8