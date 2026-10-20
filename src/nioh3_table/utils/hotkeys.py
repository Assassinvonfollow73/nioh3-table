"""Hotkey parsing helpers for the overlay."""
from __future__ import annotations


def normalize(hotkey: str) -> str:
    return hotkey.strip().lower().replace(" ", "")


def is_function_key(hotkey: str) -> bool:
    hk = normalize(hotkey)
    return hk.startswith("f") and hk[1:].isdigit()