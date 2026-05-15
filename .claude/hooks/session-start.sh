#!/bin/bash
set -euo pipefail

cd "${CLAUDE_PROJECT_DIR:-.}"

python3 << 'PYEOF'
import json
import os
import re
from pathlib import Path

repo = Path(os.environ.get("CLAUDE_PROJECT_DIR", "."))

OPEN_TASK = re.compile(r'^\s*- \[ \]')

def open_items(rel_path):
    p = repo / rel_path
    if not p.exists():
        return []
    return [line.rstrip() for line in p.read_text().splitlines() if OPEN_TASK.match(line)]

def shopping_by_section():
    p = repo / "shopping.md"
    if not p.exists():
        return []
    sections = []
    current = None
    for line in p.read_text().splitlines():
        if line.startswith("## "):
            current = (line[3:].strip(), [])
            sections.append(current)
        elif current is not None and OPEN_TASK.match(line):
            current[1].append(line.rstrip())
    return [(name, items) for name, items in sections if items]

lines = []

todos = open_items("todo.md")
lines.append("## Open to-dos (todo.md)")
lines.append("")
lines.extend(todos if todos else ["(none)"])
lines.append("")

shopping = shopping_by_section()
lines.append("## Open shopping items (shopping.md)")
lines.append("")
if shopping:
    for name, items in shopping:
        lines.append(f"**{name}**")
        lines.extend(items)
        lines.append("")
else:
    lines.append("(none)")
    lines.append("")

context = "\n".join(lines).rstrip() + "\n"

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": context,
    }
}))
PYEOF
