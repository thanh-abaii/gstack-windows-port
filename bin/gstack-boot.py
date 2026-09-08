# -*- coding: utf-8 -*-
"""
gstack Windows Native Bootloader.

Generates PowerShell-native environment setup for a gstack skill so agent
workflows can bootstrap on Windows 11 without WSL or Docker.

Usage (the IEX pattern used in every SKILL.md preamble):

    python "bin/gstack-boot.py" --skill health | iex

The script prints PowerShell assignment statements to stdout, which the
caller pipes into `iex` (Invoke-Expression). It has no side effects:
no files are written, no network calls are made (stdlib only, Python 3.8+).

Exit codes:
    0 - success, PowerShell bootstrap printed to stdout.
    1 - unexpected runtime error.
    2 - usage error or unknown skill (a `throw` statement is still printed
        to stdout so `| iex` fails loudly instead of silently continuing).
"""

import argparse
import os
import re
import sys
import time
import uuid

# Skills live in <repo>/skills/gstack-<name>/SKILL.md (with a few legacy
# exceptions stored directly as skills/<name>/, plus the root 'gstack' skill).
def skill_dir_candidates(name):
    cands = ["gstack-{name}".format(name=name), "{name}".format(name=name)]
    if name == "gstack":
        cands.append("gstack")
    return cands


def repo_root():
    """Resolve the repository root from this script's location.

    Using the script path (not cwd) so the preamble works regardless of
    the PowerShell session's current directory.
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def normalize_skill_name(raw):
    """Accept 'gs:health', 'gstack-health' or 'health' -> 'health'."""
    name = (raw or "").strip()
    if name.lower().startswith("gs:"):
        name = name[3:]
    if name.lower().startswith("gstack-"):
        name = name[len("gstack-"):]
    return name.strip().lower()


def find_skill_dir(root, name):
    """Return the skill directory for a normalized skill name, or None."""
    skills_root = os.path.join(root, "skills")
    if not os.path.isdir(skills_root):
        return None
    for pattern in skill_dir_candidates(name):
        candidate = os.path.join(skills_root, pattern)
        if os.path.isfile(os.path.join(candidate, "SKILL.md")):
            return candidate
    return None


def list_skills(root):
    """Return sorted normalized skill names found under skills/."""
    skills_root = os.path.join(root, "skills")
    names = []
    if not os.path.isdir(skills_root):
        return names
    for entry in sorted(os.listdir(skills_root)):
        full = os.path.join(skills_root, entry)
        if os.path.isdir(full) and os.path.isfile(os.path.join(full, "SKILL.md")):
            if entry.lower().startswith("gstack-") and len(entry) > len("gstack-"):
                names.append(entry[len("gstack-"):].lower())
            else:
                names.append(entry.lower())
    return names


def ps_quote(value):
    """Quote a string as a PowerShell single-quoted literal."""
    return "'" + str(value).replace("'", "''") + "'"


def is_safe_token(value):
    """Allow only conservative skill tokens in generated code."""
    return re.fullmatch(r"[a-z0-9][a-z0-9\-]*", value or "") is not None


def emit_bootstrap(skill_dir, root, normalized, out):
    """Print the PowerShell bootstrap block to the given stream."""
    bin_dir = os.path.join(root, "bin")
    session_id = uuid.uuid4().hex[:12]
    start_epoch = int(time.time())
    out.write("# gstack Windows Native bootstrap for skill '{s}'\n".format(s=normalized))
    out.write("$GSTACK_ROOT={r}\n".format(r=ps_quote(root)))
    out.write("$GSTACK_BIN={b}\n".format(b=ps_quote(bin_dir)))
    out.write("$GSTACK_SKILL={s}\n".format(s=ps_quote(normalized)))
    out.write("$GSTACK_SKILL_DIR={d}\n".format(d=ps_quote(skill_dir)))
    out.write("$env:GSTACK_ROOT=$GSTACK_ROOT\n")
    out.write("$env:GSTACK_BIN=$GSTACK_BIN\n")
    out.write("$env:GSTACK_SKILL=$GSTACK_SKILL\n")
    out.write("$env:GSTACK_SKILL_DIR=$GSTACK_SKILL_DIR\n")
    out.write("$_SESSION_ID={sid}\n".format(sid=ps_quote(session_id)))
    out.write("$env:GSTACK_SESSION_ID=$_SESSION_ID\n")
    out.write("$_TEL_START={t}\n".format(t=ps_quote(str(start_epoch))))
    out.write('if (-not (Test-Path variable:global:_TEL)) { $_TEL="off" }\n')
    out.write('if (-not (Test-Path variable:global:_TEL_START)) { $_TEL_START="0" }\n')
    out.write("$env:GSTACK_SKILL_STATUS={ok}\n".format(ok=ps_quote("ready")))
    out.write(
        "Write-Host {msg} -ForegroundColor Green\n".format(
            msg=ps_quote("[gstack] skill '{s}' ready (Windows native).".format(s=normalized))
        )
    )


def emit_failure(message, out):
    """Print a loud PowerShell failure so `| iex` never continues silently."""
    out.write("Write-Error {m}\n".format(m=ps_quote(message)))
    out.write("throw {m}\n".format(m=ps_quote(message)))


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Print PowerShell bootstrap for a gstack skill (pipe to iex)."
    )
    parser.add_argument("--skill", default="", help="Skill name (health, gs:health, gstack-health).")
    parser.add_argument("--list", action="store_true", help="List available skill names and exit.")
    parser.add_argument("--root", default="", help="Override repository root (default: auto-detect).")
    args = parser.parse_args(argv)

    root = os.path.abspath(args.root) if args.root else repo_root()

    if args.list:
        for name in list_skills(root):
            print(name)
        return 0

    normalized = normalize_skill_name(args.skill)
    if not normalized or not is_safe_token(normalized):
        emit_failure(
            "[gstack] missing or invalid --skill. Example: python \"bin/gstack-boot.py\" --skill health | iex",
            sys.stdout,
        )
        print("error: missing or invalid --skill", file=sys.stderr)
        return 2

    skill_dir = find_skill_dir(root, normalized)
    if skill_dir is None:
        emit_failure(
            "[gstack] unknown skill '{n}'. Run: python \"bin/gstack-boot.py\" --list".format(n=normalized),
            sys.stdout,
        )
        print("error: unknown skill '{n}'".format(n=normalized), file=sys.stderr)
        return 2

    emit_bootstrap(skill_dir, root, normalized, sys.stdout)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:  # last-resort guard: never let | iex continue silently
        try:
            emit_failure("[gstack] bootloader failed: {e}".format(e=exc), sys.stdout)
        except Exception:
            pass
        print("error: {e}".format(e=exc), file=sys.stderr)
        sys.exit(1)
