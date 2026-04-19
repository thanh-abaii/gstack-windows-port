#!/usr/bin/env python3
import sys
import os
import re

# Add current bin dir to path to import utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from gstack_utils import get_gstack_home

CONFIG_HEADER = """# gstack configuration — edit freely, changes take effect on next skill run.
# Docs: https://github.com/garrytan/gstack
# ... (rest of header truncated for brevity in this call) ...
"""

def get_config_file():
    return os.path.join(get_gstack_home(), "config.yaml")

def get_val(key):
    config_file = get_config_file()
    if not os.path.exists(config_file):
        return ""
    
    pattern = re.compile(rf"^{key}:\s*(.*)$")
    last_match = ""
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            for line in f:
                match = pattern.match(line.strip())
                if match:
                    last_match = match.group(1).strip()
    except:
        pass
    return last_match

def set_val(key, value):
    if not re.match(r"^[a-zA-Z0-9_]+$", key):
        print("Error: key must contain only alphanumeric characters and underscores", file=sys.stderr)
        sys.exit(1)
    
    config_file = get_config_file()
    os.makedirs(os.path.dirname(config_file), exist_ok=True)
    
    lines = []
    if os.path.exists(config_file):
        with open(config_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
    found = False
    new_line = f"{key}: {value}\n"
    for i, line in enumerate(lines):
        if line.startswith(f"{key}:"):
            lines[i] = new_line
            found = True
            break
    
    if not found:
        if lines and not lines[-1].endswith("\n"):
            lines[-1] += "\n"
        lines.append(new_line)
        
    with open(config_file, "w", encoding="utf-8") as f:
        f.writelines(lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "get" and len(sys.argv) >= 3:
        print(get_val(sys.argv[2]))
    elif cmd == "set" and len(sys.argv) >= 4:
        set_val(sys.argv[2], sys.argv[3])
