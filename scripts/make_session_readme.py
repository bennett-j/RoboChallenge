#!/usr/bin/env python3
import yaml
import os
import sys
from datetime import datetime

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 make_session_readme.py <session_name> <version>")
        sys.exit(1)
    
    session = sys.argv[1]
    version = sys.argv[2]
    session_path = f"sessions/{session}"
    
    # Read session.yaml
    with open(f"{session_path}/session.yaml") as f:
        config = yaml.safe_load(f)
    
    # Extract session information
    name = config.get("name", session)
    description = config.get("description", "")
    suitability = config.get("suitability", "")
    objectives = config.get("objectives", [])
    duration = config.get("duration", "")
    authors = config.get("authors", [])
    
    # Format datetime strings
    current_year = datetime.now().strftime('%Y')
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Format objectives list
    newline = '\n'
    objectives_list = newline.join([f'- {objective}' for objective in objectives])
    
    # Format authors
    authors_text = ', '.join(authors) + ' and RoboChallenge Contributors' if authors else 'RoboChallenge Contributors'
    
    # Create README content
    readme_content = f"""# {name} {version}

{description}

## Objectives

In this challenge you will:

{objectives_list}

## Instructions

Follow the `{session}.pdf` worksheet, using the programs in this release.

## Session Details

- **Name**: {name}
- **Version**: {version}
- **Duration**: {duration}
- **Suitable for**: {suitability}

## License
[RoboChallenge](https://github.com/bennett-j/RoboChallenge) {session} {version} © {current_year} by {authors_text} is licensed under [CC BY-SA 4.0 ](https://creativecommons.org/licenses/by/4.0/)

---
*Generated on {current_datetime}*
"""
    
    # Write README to release directory
    readme_path = "/tmp/release/README.md"
    with open(readme_path, 'w') as f:
        f.write(readme_content)
    
    print(f"✓ Created README.md for {session} {version}")

if __name__ == "__main__":
    main()
