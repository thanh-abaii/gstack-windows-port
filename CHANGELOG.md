# Changelog

All notable changes to `gstack-windows-port` are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [v1.2.1] - 2026-09-08

### Added

- `bin/gstack-boot.py` bootloader referenced by all 50 skill preambles.
  Validates skill names against `skills/`, emits PowerShell bootstrap
  (`$GSTACK_ROOT`, `$GSTACK_BIN`, `$GSTACK_SKILL_DIR`), exits 2 on unknown
  skills so a broken preamble never continues silently.
- `--fail-on-secrets` flag for `skills/gstack-maintainer-auditor/maintainer_auditor.py`.
- CI gates: bootloader contract, all `tests/*.ps1`, secret scan on every push/PR.

### Fixed

- Auditor baseline corrected from 3207 noisy hits to 503 tracked findings
  by excluding its own `reports/` output and git-ignored trees.
- README EN/VI updated to v1.2.1.

### Security

- Secret scan baseline: 0 hardcoded secrets.

## [v1.2.0] - 2026-04-19

- 49 adapted skills with visual architecture diagrams.
- Automated Windows compatibility and secrets audit (`reports/maintainer_audit_report_v1.2.0.md`).
- `gstack-maintainer-auditor` skill instruction core.

## [v1.0.0] - 2026-04-19

- Official stable release, end of phase 4 of UD-Re-Suite.

## [v0.9.x] - 2026-04-14

- Initial compliance audit and Bash-to-Python bridge prototyping.

[v1.2.1]: https://github.com/thanh-abaii/gstack-windows-port/releases/tag/v1.2.1
[v1.2.0]: https://github.com/thanh-abaii/gstack-windows-port/releases/tag/v1.2.0
[v1.0.0]: https://github.com/thanh-abaii/gstack-windows-port/releases/tag/v1.0.0
