"""Process attach + pointer resolution helpers."""
from __future__ import annotations

from dataclasses import dataclass

import pymem
import pymem.process


@dataclass
class ProcessAttacher:
    target: str = "nioh3.exe"
    pid: int = 0
    base_address: int = 0
    _pm: pymem.Pymem | None = None

    def attach(self) -> bool:
        try:
            self._pm = pymem.Pymem(self.target)
            module = pymem.process.module_from_name(
                self._pm.process_handle, self.target
            )
            self.pid = self._pm.process_id
            self.base_address = module.lpBaseOfDll
            return True
        except pymem.exception.ProcessNotFound:
            return False

    def read_ptr(self, address: int) -> int:
        if self._pm is None:
            raise RuntimeError("not attached")
        return self._pm.read_longlong(address)

    def write_float(self, address: int, value: float) -> None:
        if self._pm is None:
            raise RuntimeError("not attached")
        self._pm.write_float(address, value)

    def resolve(self, base_offset: int, chain: list[int]) -> int:
        addr = self.base_address + base_offset
        for offset in chain[:-1]:
            addr = self.read_ptr(addr) + offset
        return addr + chain[-1]