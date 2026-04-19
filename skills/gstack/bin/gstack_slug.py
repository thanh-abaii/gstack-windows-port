#!/usr/bin/env python3
import sys
import os

# Add current bin dir to path to import utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from gstack_utils import get_slug

if __name__ == "__main__":
    print(f"SLUG={get_slug()}")
