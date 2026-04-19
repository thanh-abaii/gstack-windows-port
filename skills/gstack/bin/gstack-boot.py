#!/usr/bin/env python3
import sys
import os
import time
import subprocess
import argparse

# Add current bin dir to path to import utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from gstack_utils import get_gstack_home, get_gstack_root, get_slug, clean_sessions

def generate_powershell(skill_name):
    """Generates PowerShell commands to set up the environment."""
    gstack_home = get_gstack_home()
    gstack_root = get_gstack_root()
    gstack_bin = os.path.join(gstack_root, "bin")
    gstack_browse = os.path.join(gstack_root, "browse", "dist")
    gstack_design = os.path.join(gstack_root, "design", "dist")
    
    sessions_dir = os.path.join(gstack_home, "sessions")
    os.makedirs(sessions_dir, exist_ok=True)
    
    try:
        branch = subprocess.check_output(["git", "branch", "--show-current"], 
                                        stderr=subprocess.DEVNULL, 
                                        shell=True).decode().strip()
    except:
        branch = "unknown"
        
    from gstack_config import get_val
    proactive = get_val("proactive") or "true"
    telemetry = get_val("telemetry") or "off"
    skill_prefix = get_val("skill_prefix") or "false"
    explain_level = get_val("explain_level") or "default"
    
    tel_start = int(time.time())
    session_id = f"{os.getpid()}-{tel_start}"
    slug = get_slug()
    
    clean_sessions(sessions_dir)
    
    # Mark session file
    try:
        session_file = os.path.join(sessions_dir, str(os.getppid()))
        with open(session_file, "a"):
            os.utime(session_file, None)
    except:
        pass

    def escape_ps(val):
        """Escapes values for PowerShell single-quoted strings."""
        if val is None: return ""
        return str(val).replace("'", "''")

    # Build PowerShell commands
    bridge_path = os.path.join(gstack_bin, "browse_bridge.py")
    commands = [
        f'$env:GSTACK_ROOT = "{gstack_root}"',
        f'$env:GSTACK_BIN = "{gstack_bin}"',
        f'$env:GSTACK_BROWSE = "{gstack_browse}"',
        f'$env:GSTACK_DESIGN = "{gstack_design}"',
        f'$env:BROWSE_SERVER_SCRIPT = "{os.path.join(gstack_browse, "server-node.mjs")}"',
        f'function B {{ python "{bridge_path}" @args }}',
        f"$env:_BRANCH = '{escape_ps(branch)}'",
        f"$env:_PROACTIVE = '{escape_ps(proactive)}'",
        f"$env:_TEL = '{escape_ps(telemetry)}'",
        f"$env:_TEL_START = '{tel_start}'",
        f"$env:_SESSION_ID = '{escape_ps(session_id)}'",
        f"$env:SLUG = '{escape_ps(slug)}'",
        f"$env:_EXPLAIN_LEVEL = '{escape_ps(explain_level)}'",
        f"$env:_SKILL_PREFIX = '{escape_ps(skill_prefix)}'"
    ]
    
    print("; ".join(commands))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="gstack bootstrapper for Windows")
    parser.add_argument("--skill", required=True, help="Name of the skill")
    args = parser.parse_args()
    generate_powershell(args.skill)
