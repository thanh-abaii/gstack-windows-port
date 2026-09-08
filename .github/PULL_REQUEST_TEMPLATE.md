## What changed

<!-- One sentence per bullet. Link issues with Closes #NNN. -->

-
-

## Windows 11 checklist

- [ ] No new Bashisms (`rm -rf`, `grep`, `export`, `mkdir -p`, absolute Unix paths)
- [ ] PowerShell scripts use CRLF line endings
- [ ] No hardcoded secrets, passwords, or API keys
- [ ] `python skills/gstack-maintainer-auditor/maintainer_auditor.py --fail-on-secrets` passes
- [ ] Affected `tests/*.ps1` pass (`Get-ChildItem tests/*.ps1 | ForEach-Object { & $_.FullName }`)

## Codex review

- [ ] Requested Codex review on this PR (see `docs/codex-usage.md`)
- [ ] Addressed or triaged Codex findings into follow-up issues
