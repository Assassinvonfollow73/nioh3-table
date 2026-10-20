# Security Policy

## Supported versions

Only the latest tagged release of `nioh3-table` receives fixes.

## Reporting a vulnerability

Please do **not** open a public issue for security problems. Email the maintainers
listed in `AUTHORS` or open a private security advisory on GitHub.

We care about:

- Arbitrary code execution through the config loader.
- Memory corruption / out-of-bounds reads in the pointer resolver.
- Privilege escalation via the injector bootstrap.
- Supply-chain issues in `requirements.txt`.

## Scope note

`nioh3-table` is an offline, single-player trainer. It attaches to the local
`nioh3.exe` process only and never touches network traffic. Reports about
anti-cheat detection in multiplayer are **out of scope** — the tool is not
intended for that environment.