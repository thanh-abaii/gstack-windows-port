# Codex for OSS application kit

Form: https://openai.com/form/codex-for-oss/
Role: primary maintainer. Tick both: Codex Security, API credits.

## Field 1: why does this repository qualify? (max 500 chars)

> gstack-windows-port is a MIT Windows 11-native port of garrytan/gstack (49 skills). Most agents emit Unix shell that breaks on PowerShell. We ship Python/PowerShell bootloader, CI gates, PowerShell tests, public auditor reports (503 tracked items, 0 secrets). Actively released, used as hands-on reference by Binh Dan Hoc AI community in Vietnam for Windows-native agent workflows.

## Field 2: how will you use API credits? (max 500 chars)

> For Codex maintainer automation: (1) PR review bot for Bashisms, CRLF, paths, secrets; (2) auto-triage Windows parser failures to fix suggestions; (3) release workflow for changelogs/checklists; (4) harden skill bodies, expand tests from 11 to 49 skills. All runs logged in CI/reports for transparent maintenance.

## Field 3: anything else? (max 500 chars)

> Upstream-credited fork, Windows-only differentiation. Roadmap Q4 2026: Codex-assisted release pipeline + local token-spend telemetry to cut API waste. Education-focused, grant funds public maintenance only.

## Pre-submit checklist

- [ ] `CHANGELOG.md` exists and release v1.2.1 is published
- [ ] 5 triage issues open with `good first issue` / `help wanted` labels
- [ ] `docs/codex-usage.md` + `codex-review.yml` baseline visible on main
- [ ] New files committed and pushed (see pending files below)
- [ ] OpenAI organization ID ready from platform.openai.com/settings/organization/general
- [ ] ChatGPT account email matches the form email

Pending local files to commit: `CHANGELOG.md`,
`.github/PULL_REQUEST_TEMPLATE.md`, `.github/workflows/codex-review.yml`,
`docs/codex-usage.md`, this file, `README.md` touch-up.

## Community post draft (Binh Dan Hoc AI, Vietnamese)

> Xin sao cho repo Windows-native: em vừa mở 5 issues `good first issue`
> dọn Bashisms cho 49 skills gstack chạy trên PowerShell, có CI + release
> v1.2.1. Ai dùng Windows + AI agent thì vào star, review hoặc nhận 1 issue
> giúp em để đủ tín hiệu nộp Codex for OSS: [link repo]

## Upstream note draft (garrytan/gstack issue or discussion)

> Hi, I maintain a Windows 11-native port of this skill ecosystem
> (Python/PowerShell bridge, no WSL/Docker, MIT, upstream-credited):
> [link]. Applying to Codex for OSS to fund PR review and release
> automation. Happy to upstream any PowerShell-safe patterns you find
> useful, and to link back as a community Windows port if welcome.
