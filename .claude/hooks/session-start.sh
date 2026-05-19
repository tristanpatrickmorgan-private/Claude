#!/bin/bash
set -euo pipefail

cd "${CLAUDE_PROJECT_DIR:-.}"

python3 << 'PYEOF'
import json
import os
import re
import datetime
from pathlib import Path

repo = Path(os.environ.get("CLAUDE_PROJECT_DIR", "."))
account_uuid = os.environ.get("CLAUDE_CODE_ACCOUNT_UUID", "")

OPEN_TASK = re.compile(r'^\s*- \[ \]')
INBOX_ITEM = re.compile(r'^\s*- ')
DATE_HEADING = re.compile(r'^##\s+(\d{4}-\d{2}-\d{2})(?:\s+to\s+(\d{4}-\d{2}-\d{2}))?\b.*$')


def identify_user():
    """Match UUID against the table in root CLAUDE.md. Returns (name, folder) or (None, None)."""
    claude_md = repo / "CLAUDE.md"
    if not claude_md.exists() or not account_uuid:
        return (None, None)
    text = claude_md.read_text()
    # Look for a markdown table row: | Name | `UUID` | `Folder/` |
    pattern = re.compile(r'^\|\s*([^|]+?)\s*\|\s*`?' + re.escape(account_uuid) + r'`?\s*\|\s*`?([^|`]+?)`?\s*\|', re.M)
    m = pattern.search(text)
    if m:
        return (m.group(1).strip(), m.group(2).strip().rstrip('/'))
    return (None, None)


def open_items(rel_path):
    p = repo / rel_path
    if not p.exists():
        return []
    return [line.rstrip() for line in p.read_text().splitlines() if OPEN_TASK.match(line)]


def inbox_items(rel_path):
    """Return non-header bullet items from an inbox file."""
    p = repo / rel_path
    if not p.exists():
        return []
    items = []
    for line in p.read_text().splitlines():
        if INBOX_ITEM.match(line) and not line.strip().startswith('- >'):
            items.append(line.rstrip())
    return items


def shopping_by_section(rel_path):
    p = repo / rel_path
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


def upcoming_calendar(rel_path, days_ahead=14):
    p = repo / rel_path
    if not p.exists():
        return []
    today = datetime.date.today()
    horizon = today + datetime.timedelta(days=days_ahead)
    lines = p.read_text().splitlines()
    upcoming = []
    current_block = None
    current_date = None
    for line in lines:
        m = DATE_HEADING.match(line)
        if m:
            if current_block and current_date and today <= current_date <= horizon:
                upcoming.append((current_date, current_block))
            try:
                current_date = datetime.date.fromisoformat(m.group(1))
            except ValueError:
                current_date = None
            current_block = [line.rstrip()]
        elif line.startswith("## "):
            if current_block and current_date and today <= current_date <= horizon:
                upcoming.append((current_date, current_block))
            current_block = None
            current_date = None
        elif current_block is not None and line.strip():
            current_block.append(line.rstrip())
    if current_block and current_date and today <= current_date <= horizon:
        upcoming.append((current_date, current_block))
    return [block for _, block in sorted(upcoming)]


name, folder = identify_user()
lines = []

if name is None:
    lines.append("## ⚠️ Unknown user")
    lines.append("")
    lines.append(f"`CLAUDE_CODE_ACCOUNT_UUID` = `{account_uuid or '(not set)'}` is not registered in the root `CLAUDE.md` table.")
    lines.append("")
    lines.append("Before doing anything else: ask the user 'Are you Tristan or Marie?', then add their UUID to the table in root `CLAUDE.md` and commit. After that, the rest of this hook will start surfacing their personal inbox/todo/shopping automatically.")
    lines.append("")
else:
    # Inbox first — most time-sensitive
    inbox = inbox_items(f"{folder}/inbox.md")
    lines.append(f"## 📬 {name}'s inbox ({folder}/inbox.md)")
    lines.append("")
    if inbox:
        lines.append(f"**{len(inbox)} item(s) waiting** — read these first and either act on them, move them into the right place (todo / logs / projects), or acknowledge to the other person. Then delete the entries you've handled.")
        lines.append("")
        lines.extend(inbox)
    else:
        lines.append("(empty)")
    lines.append("")

    # Personal todos
    todos = open_items(f"{folder}/todo.md")
    lines.append(f"## Open to-dos ({folder}/todo.md)")
    lines.append("")
    lines.extend(todos if todos else ["(none)"])
    lines.append("")

    # Shopping — personal + family
    personal_shop = shopping_by_section(f"{folder}/shopping.md")
    family_shop = shopping_by_section("Family/shopping.md")
    if personal_shop or family_shop:
        lines.append("## Open shopping items")
        lines.append("")
        if personal_shop:
            lines.append(f"_From {folder}/shopping.md (personal):_")
            for sect, items in personal_shop:
                lines.append(f"**{sect}**")
                lines.extend(items)
                lines.append("")
        if family_shop:
            lines.append("_From Family/shopping.md (joint):_")
            for sect, items in family_shop:
                lines.append(f"**{sect}**")
                lines.extend(items)
                lines.append("")

    # Upcoming family calendar
    upcoming = upcoming_calendar("Family/calendar.md", days_ahead=14)
    if upcoming:
        lines.append("## 📅 Upcoming family events (next 14 days)")
        lines.append("")
        for block in upcoming:
            lines.extend(block)
            lines.append("")

context = "\n".join(lines).rstrip() + "\n"

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": context,
    }
}))
PYEOF
