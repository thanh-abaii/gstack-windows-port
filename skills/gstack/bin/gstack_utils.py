import os
import sys
import json
import time
import subprocess
from pathlib import Path

def get_gstack_home():
    """Returns the .gstack state directory path, handling overrides."""
    state_dir = os.environ.get("GSTACK_STATE_DIR")
    if not state_dir:
        state_dir = os.path.join(os.path.expanduser("~"), ".gstack")
    return os.path.abspath(state_dir)

def get_gstack_root():
    """Returns the current gstack installation root directory based on the location of this script."""
    try:
        # Since this script is in [SKILLS]/gstack/bin/gstack_utils.py
        current_script_path = os.path.realpath(__file__)
        current_bin = os.path.dirname(current_script_path)
        root = os.path.dirname(current_bin)
        return root
    except:
        pass
    
    return os.path.abspath(os.path.join(os.path.expanduser("~"), ".codex", "skills", "gstack"))

def get_slug():
    """Returns a unique slug for the current project."""
    try:
        # Try to find git root from CWD
        root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], 
                                       stderr=subprocess.DEVNULL, 
                                       shell=True).decode().strip()
        return os.path.basename(root)
    except:
        return "unknown"

def write_jsonl_safe(file_path, data, retries=5, delay=0.2):
    """Writes a line to a JSONL file with retry logic for Windows file locking."""
    line = json.dumps(data) + "\n"
    file_path = os.path.abspath(file_path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    for i in range(retries):
        try:
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(line)
            return True
        except PermissionError:
            if i < retries - 1:
                time.sleep(delay)
            else:
                print(f"Error: Could not write to {file_path} after {retries} attempts due to file lock.", file=sys.stderr)
                return False
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)
            return False

def clean_sessions(sessions_dir, max_age_minutes=120):
    """Deletes session files older than the specified age."""
    if not os.path.exists(sessions_dir):
        return
    
    now = time.time()
    for entry in os.scandir(sessions_dir):
        if entry.is_file():
            if (now - entry.stat().st_mtime) / 60 > max_age_minutes:
                try:
                    os.remove(entry.path)
                except:
                    pass

if __name__ == "__main__":
    print(f"GSTACK_HOME: {get_gstack_home()}")
    print(f"GSTACK_ROOT: {get_gstack_root()}")
    print(f"SLUG: {get_slug()}")
