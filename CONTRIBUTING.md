# Contributing to nioh3-table

Thanks for wanting to help improve the Nioh 3 Trainer table. This is a community
project — contributions of new offsets, feature modules, and bug reports are welcome.

## Ground rules

- Keep feature modules self-contained under `src/nioh3_table/features/`.
- Never hardcode a raw address. All pointers go through `src/nioh3_table/offsets/`.
- Every new feature must ship with a stub test in `tests/`.
- Use `pymem` for memory access — do not add a second memory library.
- Follow the existing `Feature` interface (`src/nioh3_table/core/feature.py`).

## Workflow

1. Fork the repo and create a branch: `feat/<feature-name>`.
2. Update `offsets/nioh3_offsets.yaml` if the game patch shifted values.
3. Run `pytest -q` before opening a PR.
4. Describe the game version you tested against in the PR body.

## Style

- Python 3.11+, `ruff` formatting, type hints on public functions.
- Log through `src/nioh3_table/utils/logger.py`, not `print`.
- No telemetry, no network calls except the update checker.

## Legal / disclaimer

This trainer is provided for educational and single-player modding purposes only.
Do not use it in any online or multiplayer context. Use at your own risk.