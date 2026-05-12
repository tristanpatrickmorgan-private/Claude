from datetime import datetime, timezone, timedelta
import os

# Swedish time
tz = timezone(timedelta(hours=2))  # CEST (summer); change to +1 in winter
today = datetime.now(tz)
date_str = today.strftime('%A %d %B %Y')

lines = []
lines.append(f"Good morning — {date_str}")
lines.append("")

# ── TO-DO LIST ──────────────────────────────
try:
    with open('todo.md', 'r') as f:
        content = f.read()

    open_tasks = [
        line.strip()[6:]
        for line in content.split('\n')
        if line.strip().startswith('- [ ]')
    ]

    lines.append(f"OPEN TASKS ({len(open_tasks)})")
    lines.append("-" * 30)
    if open_tasks:
        for task in open_tasks:
            lines.append(f"  • {task}")
    else:
        lines.append("  All clear!")
except Exception as e:
    lines.append(f"Could not read todo.md: {e}")

lines.append("")

# ── ARCHIE — LAST SLEEP ─────────────────────────
try:
    with open('projects/archie/sleep-log.md', 'r') as f:
        content = f.read()

    rows = [
        line for line in content.split('\n')
        if line.startswith('|')
        and not line.startswith('| Date')
        and not line.startswith('|---')
        and '|' in line[1:]
    ]

    if rows:
        cells = [c.strip() for c in rows[-1].split('|')[1:-1]]
        if len(cells) >= 6:
            date, wake, nap, nap_dur, bedtime, notes = cells[:6]
            lines.append(f"ARCHIE — last sleep ({date})")
            lines.append("-" * 30)
            lines.append(f"  Wake:    {wake}")
            lines.append(f"  Bedtime: {bedtime}")
            if nap and nap != '-':
                lines.append(f"  Nap:     {nap} ({nap_dur})")
            if notes:
                lines.append(f"  Notes:   {notes}")
except Exception as e:
    lines.append(f"Could not read sleep log: {e}")

lines.append("")
lines.append("-" * 30)
lines.append("Your personal assistant · github.com/tristanpatrickmorgan-private/claude")

print('\n'.join(lines))
