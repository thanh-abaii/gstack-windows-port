# Codex maintainer automation plan

This document describes how this repository uses (and plans to use, with
Codex for Open Source credits) Codex in everyday maintainer workflows:
pull request review, issue triage, and releases.

## Current baseline (no API credits needed)

Every push and PR already runs deterministic gates in `.github/workflows/ci.yml`:

- bootloader contract for `bin/gstack-boot.py` (known skill emits PowerShell,
  unknown skill exits 2, `python | iex` end-to-end check)
- all PowerShell integration tests in `tests/*.ps1`
- maintainer audit with `--fail-on-secrets` (baseline: 0 hardcoded secrets)

`.github/workflows/codex-review.yml` publishes the audit report as a PR
comment so reviewers see the Windows-compatibility delta without extra tooling.

## Planned Codex usage (with API credits)

1. **PR review bot.** On each PR, Codex reviews the diff for Bashisms
   (`rm -rf`, `grep`, `export`, absolute Unix paths), CRLF violations,
   unsafe `iex` usage, and secret leaks. Findings post as review comments;
   unresolved high-severity items block merge via the PR template checklist.
2. **Issue triage.** Nightly Codex run groups new `reports/maintainer_audit_report.md`
   findings into the tracked triage issues (see open `good first issue` items),
   suggests PowerShell-native replacements, and drafts fix patches for maintainer approval.
3. **Release workflow.** Codex drafts `CHANGELOG.md` entries and release checklists
   from merged PRs, so each tag ships with an accurate, reviewer-approved changelog.
4. **Security deep scans.** The `python | iex` bootloader pattern is a high-risk
   surface by design. Conditional Codex Security access would cover quarterly deep
   scans of `bin/`, `setup.ps1`, and skill preambles, beyond the regex auditor.

## Cost control

- Codex runs only on PR events and a nightly schedule, scoped to changed files first.
- Deterministic CI gates stay the merge blocker; Codex is advisory until its
  precision is measured over 30 PRs.
- Token spend is tracked per workflow run and summarized in release notes,
  feeding the Q4 2026 local telemetry dashboard on the roadmap.
