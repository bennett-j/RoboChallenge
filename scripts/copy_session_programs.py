#!/usr/bin/env python3
import yaml
import shutil
import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 copy_session_programs.py <session_name>")
        sys.exit(1)
    
    session = sys.argv[1]
    session_path = f"sessions/{session}"
    
    # Read session.yaml
    with open(f"{session_path}/session.yaml") as f:
        config = yaml.safe_load(f)
    
    # Copy files listed in session.yaml
    files_to_copy = config.get("files", [])
    for file in files_to_copy:
        if os.path.exists(file):
            dst = f"/tmp/release/{os.path.basename(file)}"
            shutil.copy(file, dst)
            print(f"✓ Copied {file}")
        else:
            print(f"⚠ File not found: {file}")

if __name__ == "__main__":
    main()