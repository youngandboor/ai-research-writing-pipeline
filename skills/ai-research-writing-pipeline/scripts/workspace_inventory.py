#!/usr/bin/env python3
"""Generate a lightweight research-workspace inventory in Markdown."""

from __future__ import annotations

import argparse
import os
from pathlib import Path


CACHE_NAMES = {
    ".DS_Store",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".ipynb_checkpoints",
}

DEFAULT_IGNORE_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "site-packages",
    "__pycache__",
}

BUILD_SUFFIXES = {".aux", ".fls", ".fdb_latexmk", ".blg", ".synctex.gz"}
IMPORTANT_NAMES = {
    "AGENTS.md",
    "CLAUDE.md",
    "PROTOCOL.md",
    "README.md",
    "PROJECT_MAP.md",
    "workflow_state.json",
    "claim_registry.jsonl",
    "numeric_claims.jsonl",
    "validated_references.jsonl",
}


def human_size(n: int) -> str:
    units = ["B", "KB", "MB", "GB", "TB"]
    value = float(n)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.1f} {unit}" if unit != "B" else f"{int(value)} B"
        value /= 1024
    return f"{n} B"


def should_skip_dir(name: str) -> bool:
    return name in DEFAULT_IGNORE_DIRS or name.startswith(".venv")


def iter_paths(root: Path):
    for current, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not should_skip_dir(d)]
        current_path = Path(current)
        for name in dirs:
            yield current_path / name
        for name in files:
            yield current_path / name


def dir_size(path: Path) -> int:
    total = 0
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if not should_skip_dir(d)]
        for name in files:
            try:
                total += (Path(root) / name).stat().st_size
            except OSError:
                pass
    return total


def is_build_file(path: Path) -> bool:
    name = path.name
    return any(name.endswith(suffix) for suffix in BUILD_SUFFIXES)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--max-depth", type=int, default=2)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    print(f"# Workspace Inventory\n")
    print(f"- Root: `{root}`")

    top_dirs = [p for p in root.iterdir() if p.is_dir() and not should_skip_dir(p.name)]
    top_files = [p for p in root.iterdir() if p.is_file()]

    print("\n## Top-Level Directories\n")
    print("| Path | Files | Size |")
    print("|---|---:|---:|")
    for path in sorted(top_dirs):
        file_count = sum(1 for p in path.rglob("*") if p.is_file())
        print(f"| `{path.name}/` | {file_count} | {human_size(dir_size(path))} |")

    print("\n## Important Files\n")
    for path in sorted(iter_paths(root)):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        depth = len(rel.parts) - 1
        if depth <= args.max_depth and (path.name in IMPORTANT_NAMES or path.name.lower() in IMPORTANT_NAMES):
            print(f"- `{rel}`")

    print("\n## Possible Clutter\n")
    cache_count = 0
    build_count = 0
    for path in iter_paths(root):
        if path.name in CACHE_NAMES:
            cache_count += 1
        if path.is_file() and is_build_file(path):
            build_count += 1
    print(f"- Cache/build directories or files matching common names: {cache_count}")
    print(f"- LaTeX build sidecar files: {build_count}")

    print("\n## Root Files\n")
    for path in sorted(top_files):
        print(f"- `{path.name}` ({human_size(path.stat().st_size)})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
