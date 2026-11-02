"""Report relative Markdown links and <img> sources in Armotheca_docs whose target file is missing."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote

SKIP_DIRS = {".git", ".obsidian", ".idea", ".claude", ".trash"}
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
IMG = re.compile(r"<img\s[^>]*src=\"([^\"]+)\"")


def iter_docs(root):
    for path in root.rglob("*.md"):
        if not SKIP_DIRS.intersection(path.relative_to(root).parts):
            yield path


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    broken = []
    for doc in iter_docs(root):
        in_code = False
        for number, line in enumerate(doc.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_code = not in_code
            if in_code:
                continue
            for target in LINK.findall(line) + IMG.findall(line):
                if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                    continue
                file_part = unquote(target.split("#", 1)[0])
                if not (doc.parent / file_part).exists():
                    broken.append(f"{doc.relative_to(root)}:{number}: {target}")
    for entry in broken:
        print(entry)
    print(f"{len(broken)} broken link(s)")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
