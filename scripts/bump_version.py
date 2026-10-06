#!/usr/bin/env python3
"""Set one release version in every manifest that carries it.

Usage: python3 scripts/bump_version.py 1.4.0
Then add the CHANGELOG entry and run `bash validate-skills.sh`, which fails if any
manifest still has a different version.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_repo import BUNDLE, ROOT, VERSIONED_MANIFESTS  # noqa: E402


def write(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def main() -> int:
    if len(sys.argv) != 2 or not re.fullmatch(r"\d+\.\d+\.\d+", sys.argv[1]):
        print(__doc__)
        return 2
    version = sys.argv[1]

    for rel in VERSIONED_MANIFESTS:
        path = ROOT / rel
        data = json.loads(path.read_text())
        data["version"] = version
        write(path, data)
        print(f"{rel}: {version}")

    rel = ".claude-plugin/marketplace.json"
    path = ROOT / rel
    market = json.loads(path.read_text())
    market["metadata"]["version"] = version
    for plugin in market["plugins"]:
        if plugin["name"] == BUNDLE:
            plugin["version"] = version
    write(path, market)
    print(f"{rel}: {version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
