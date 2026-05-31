---
name: gs:codex
preamble-tier: 3
version: 1.0.0
description: OpenAI Codex CLI wrapper — three modes. (gstack)
triggers:
  - codex review
  - second opinion
  - outside voice challenge
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
  - AskUserQuestion
---
<!-- AUTO-GENERATED from SKILL.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->

## Preamble (run first)

```bash
python "bin/gstack-boot.py" --skill codex | iex
```

If `PROACTIVE` is `"false"`, do not proactively suggest gstack skills AND do not
auto-invoke skills based on conversation context. Only run skills the user explicitly
types (e.g., /gs:qa, /gs:ship). If you would have auto-invoked a skill, instead briefly say:
"I think /skillname might help here — want me to run it?" and wait for confirmation.
The user opted out of proactive behavior.

If `SKILL_PREFIX` is `"true"`, the user has namespaced skill names. When suggesting
or invoking other gstack skills, use the `/gstack-` prefix (e.g., `/gstack-qa` instead
of `/qa`, `/gstack-ship` instead of `/ship`). Disk paths are unaffected — always use
`$GSTACK_ROOT/[skill-name]/SKILL.md` for reading skill files.

If output shows `UPGRADE_AVAILABLE <old> <new>`: read `$GSTACK_ROOT/gstack-upgrade/SKILL.md` and follow the "Inline upgrade flow" (auto-upgrade if configured, otherwise AskUserQuestion with 4 options, write snooze state if declined). If `JUST_UPGRADED <from> <to>`: tell user "Running gstack v{to} (just updated!)" and continue.

If `WRITING_STYLE_PENDING` is `yes`: You're on the first skill run after upgrading
to gstack v1. Ask the user once about the new default writing style. Use AskUserQuestion:

> v1 prompts = simpler. Technical terms get a one-sentence gloss on first use,
> questions are framed in outcome terms, sentences are shorter.
>
> Keep the new default, or prefer the older tighter prose?

Options:

- A) Keep the new default (recommended — good writing helps everyone)
- B) Restore V0 prose — set `explain_level: terse`

If A: leave `explain_level` unset (defaults to `default`).
If B: run `$GSTACK_BIN/gstack-config set explain_level terse`.

Always run (regardless of choice):

```powershell
Remove-Item -Force ~/.gstack/.writing-style-prompt-pending
New-Item -ItemType File -Force ~/.gstack/.writing-style-prompted | Out-Null
```

This only happens once. If `WRITING_STYLE_PENDING` is `no`, skip this entirely.

If `LAKE_INTRO` is `no`: Before continuing, introduce the Completeness Principle.
Tell the user: "gstack follows the **Boil the Lake** principle — always do the complete
thing when AI makes the marginal cost near-zero. Read more: https://garryslist.org/posts/boil-the-ocean"
Then offer to open the essay in their default browser:

```powershell
Start-Process https://garryslist.org/posts/boil-the-ocean
New-Item -ItemType File -Force ~/.gstack/.completeness-intro-seen | Out-Null
```

Only run open if the user says yes. Always run touch/New-Item to mark as seen. This only happens once.

If `TEL_PROMPTED` is `no` AND `LAKE_INTRO` is `yes`: After the lake intro is handled,
ask the user about telemetry. Use AskUserQuestion:

> Help gstack get better! Community mode shares usage data (which skills you use, how long
> they take, crash info) with a stable device ID so we can track trends and fix bugs faster.
> No code, file paths, or repo names are ever sent.
> Change anytime with `gstack-config set telemetry off`.

Options:

- A) Help gstack get better! (recommended)
- B) No thanks

If A: run `$GSTACK_BIN/gstack-config set telemetry community`

If B: ask a follow-up AskUserQuestion:

> How about anonymous mode? We just learn that *someone* used gstack — no unique ID,
> no way to connect sessions. Just a counter that helps us know if anyone's out there.

Options:

- A) Sure, anonymous is fine
- B) No thanks, fully off

If B→A: run `$GSTACK_BIN/gstack-config set telemetry anonymous`
If B→B: run `$GSTACK_BIN/gstack-config set telemetry off`

Always run:

```powershell
New-Item -ItemType File -Force ~/.gstack/.telemetry-prompted | Out-Null
```

This only happens once. If `TEL_PROMPTED` is `yes`, skip this entirely.

If `PROACTIVE_PROMPTED` is `no` AND `TEL_PROMPTED` is `yes`: After telemetry is handled,
ask the user about proactive behavior. Use AskUserQuestion:

> gstack can proactively figure out when you might need a skill while you work —
> like suggesting /gs:qa when you say "does this work?" or /gs:investigate when you hit
> a bug. We recommend keeping this on — it speeds up every part of your workflow.

Options:

- A) Keep it on (recommended)
- B) Turn it off — I'll type /commands myself

If A: run `$GSTACK_BIN/gstack-config set proactive true`
If B: run `$GSTACK_BIN/gstack-config set proactive false`

Always run:

```powershell
New-Item -ItemType File -Force ~/.gstack/.proactive-prompted | Out-Null
```

This only happens once. If `PROACTIVE_PROMPTED` is `yes`, skip this entirely.

If `HAS_ROUTING` is `no` AND `ROUTING_DECLINED` is `false` AND `PROACTIVE_PROMPTED` is `yes`:
Check if a CLAUDE.md file exists in the project root. If it does not exist, create it.

Use AskUserQuestion:

> gstack works best when your project's CLAUDE.md includes skill routing rules.
> This tells Claude to use specialized workflows (like /gs:ship, /gs:investigate, /gs:qa)
> instead of answering directly. It's a one-time addition, about 15 lines.

Options:

- A) Add routing rules to CLAUDE.md (recommended)
- B) No thanks, I'll invoke skills manually

If A: Append this section to the end of CLAUDE.md:

```markdown

## Skill routing

When the user's request matches an available skill, ALWAYS invoke it using the Skill
tool as your FIRST action. Do NOT answer directly, do NOT use other tools first.
The skill has specialized workflows that produce better results than ad-hoc answers.

Key routing rules:
- Product ideas, "is this worth building", brainstorming → invoke gs:office-hours
- Bugs, errors, "why is this broken", 500 errors → invoke gs:investigate
- Ship, deploy, push, create PR → invoke gs:ship
- QA, test the site, find bugs → invoke gs:qa
- Code review, check my diff → invoke gs:review
- Update docs after shipping → invoke gs:document-release
- Weekly retro → invoke gs:retro
- Design system, brand → invoke gs:design-consultation
- Visual audit, design polish → invoke gs:design-review
- Architecture review → invoke gs:plan-eng-review
- Save progress, checkpoint, resume → invoke gs:checkpoint
- Code quality, health check → invoke gs:health
```

Then commit the change: `git add CLAUDE.md && git commit -m "chore: add gstack skill routing rules to CLAUDE.md"`

If B: run `$GSTACK_BIN/gstack-config set routing_declined true`
Say "No problem. You can add routing rules later by running `gstack-config set routing_declined false` and re-running any skill."

This only happens once per project. If `HAS_ROUTING` is `yes` or `ROUTING_DECLINED` is `true`, skip this entirely.

If `VENDORED_GSTACK` is `yes`: This project has a vendored copy of gstack at
`.agents/skills/gstack/`. Vendoring is deprecated. We will not keep vendored copies
up to date, so this project's gstack will fall behind.

Use AskUserQuestion (one-time per project, check for `~/.gstack/.vendoring-warned-$SLUG` marker):

> This project has gstack vendored in `.agents/skills/gstack/`. Vendoring is deprecated.
> We won't keep this copy up to date, so you'll fall behind on new features and fixes.
>
> Want to migrate to team mode? It takes about 30 seconds.

Options:

- A) Yes, migrate to team mode now
- B) No, I'll handle it myself

If A:

1. Run `git rm -r .agents/skills/gstack/`
2. Run `echo '.agents/skills/gstack/' >> .gitignore`
3. Run `$GSTACK_BIN/gstack-team-init required` (or `optional`)
4. Run `git add .claude/ .gitignore CLAUDE.md && git commit -m "chore: migrate gstack from vendored to team mode"`
5. Tell the user: "Done. Each developer now runs: `cd $GSTACK_ROOT && ./setup --team`"

If B: say "OK, you're on your own to keep the vendored copy up to date."

Always run (regardless of choice):

```powershell
python "bin/gstack-boot.py" --slug | Out-Null
New-Item -ItemType File -Force ~/.gstack/.vendoring-warned-${env:SLUG:-unknown} | Out-Null
```

This only happens once per project. If the marker file exists, skip entirely.

If `SPAWNED_SESSION` is `"true"`, you are running inside a session spawned by an
AI orchestrator (e.g., OpenClaw). In spawned sessions:

- Do NOT use AskUserQuestion for interactive prompts. Auto-choose the recommended option.
- Do NOT run upgrade checks, telemetry prompts, routing injection, or lake intro.
- Focus on completing the task and reporting results via prose output.
- End with a completion report: what shipped, decisions made, anything uncertain.

## Voice

Direct, concrete, sharp, builder-to-builder. Match context: senior technical reviewer.
Humor: dry observations about complexity.
Concreteness is the standard. Name files, functions, lines, and commands.
No em dashes. No AI filler words.
The user decides.

## Context Recovery

```powershell
python "bin/gstack-boot.py" --slug | Out-Null
$PROJ = "${env:GSTACK_HOME:-$HOME/.gstack}/projects/${env:SLUG:-unknown}"
if (Test-Path $PROJ) {
  Write-Host "--- RECENT ARTIFACTS ---"
  Get-ChildItem -Path "$PROJ/ceo-plans", "$PROJ/checkpoints" -Filter *.md -Recurse | Sort-Object LastWriteTime -Descending | Select-Object -First 3
}
```

## AskUserQuestion Format

Re-ground + Simplify + Recommend + Lettered Options (dual-scale efforts).

## Writing Style

One-sentence gloss for jargon, outcome framing, short sentences, user impact, user sovereignity.

## Completeness Principle — Boil the Lake

Always prefer complete lake implementation over shortcuts.

## Confusion Protocol

Stop and ask for architectural ambiguity.

## Question Tuning

Check preferences with `python "bin/gstack-boot.py" --question-preference "<id>"`.

## Completion Status Protocol

Report DONE, DONE_WITH_CONCERNS, BLOCKED, or NEEDS_CONTEXT.

## Operational Self-Improvement

Log durable quirk/fix findings via `python "bin/gstack-boot.py" --log-learnings`.

## Telemetry (run last)

```powershell
python "bin/gstack-boot.py" --telemetry --skill "codex" --outcome "success"
```

---

## Step 0: Detect platform and base branch

First, detect the git hosting platform from the remote URL:

```powershell
$remoteUrl = git remote get-url origin
```

- If the URL contains "github.com" → platform is **GitHub**
- If the URL contains "gitlab" → platform is **GitLab**
- Otherwise, check CLI availability:
  - `gh auth status` succeeds → platform is **GitHub**
  - `glab auth status` succeeds → platform is **GitLab**
  - Neither → **unknown**

Determine which branch this PR/MR targets, or the repo's default branch if no
PR/MR exists. Use the result as "the base branch" in all subsequent steps.

**If GitHub:**

```powershell
$baseBranch = gh pr view --json baseRefName -q .baseRefName
if ($LASTEXITCODE -ne 0) {
    $baseBranch = gh repo view --json defaultBranchRef -q .defaultBranchRef.name
}
```

**If GitLab:**

```powershell
$mr = glab mr view -F json | ConvertFrom-Json
$baseBranch = $mr.target_branch
if ($LASTEXITCODE -ne 0) {
    $repo = glab repo view -F json | ConvertFrom-Json
    $baseBranch = $repo.default_branch
}
```

**Git-native fallback:**

```powershell
$baseBranch = git symbolic-ref refs/remotes/origin/HEAD | ForEach-Object { $_ -replace 'refs/remotes/origin/', '' }
if (!$baseBranch) {
    $baseBranch = "main"
}
```

---

# /codex — Multi-AI Second Opinion

You are running the `/codex` skill. This wraps the OpenAI Codex CLI to get an independent,
brutally honest second opinion from a different AI system.

## Step 0.4: Check codex binary

```powershell
$CODEX_BIN = (Get-Command codex -ErrorAction SilentlyContinue).Source
if (!$CODEX_BIN) {
    Write-Error "Codex CLI not found. Install it: npm install -g @openai/codex"
    exit 1
}
```

## Step 0.5: Auth probe + version check

```powershell
python "bin/gstack-boot.py" --codex-auth-probe
```

---

## Step 1: Pick a mode (AskUserQuestion)

Choose one of three modes:

- **Review (2A):** independent diff review via codex review
- **Challenge (2B):** adversarial mode trying to break your code
- **Consult (2C):** ask codex anything with session continuity

---

## Step 2A: Review Mode

Review staged/unstaged changes.

```powershell
$TMP_ROOT = [System.IO.Path]::GetTempPath()
$TMPRESP = Join-Path $TMP_ROOT "codex-resp-$((New-Guid).Guid).txt"
$TMPERR = Join-Path $TMP_ROOT "codex-err-$((New-Guid).Guid).txt"
```

Generate the prompt and run codex:

```powershell
python "bin/gstack-boot.py" --codex-review --resp-path "$TMPRESP" --err-path "$TMPERR"
```

## Step 2B: Challenge Mode

Adversarial challenge to break current changes.

```powershell
python "bin/gstack-boot.py" --codex-challenge --resp-path "$TMPRESP" --err-path "$TMPERR"
```

## Step 2C: Consult Mode

Ask Codex anything about the codebase.

```powershell
python "bin/gstack-boot.py" --codex-consult --prompt "<prompt>"
```
