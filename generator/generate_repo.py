import os
from pathlib import Path
from jinja2 import Template

ROOT = Path(__file__).resolve().parents[1]

def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def main() -> None:
    # Minimal placeholder: pipeline will overwrite with full project in next commits.
    # This file exists so workflow can run even before full content is embedded.
    write("gitanalyzer-pro/.keep", "generated\n")

    # A tiny marker README for generated project root (will be replaced by full generator later)
    write("gitanalyzer-pro/README.md", "# GitAnalyzer Pro (Generated)\n")

if __name__ == "__main__":
    main()
