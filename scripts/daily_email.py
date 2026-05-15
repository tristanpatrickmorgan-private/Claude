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

# ── PROJECTS ────────────────────────────────
try:
    projects = sorted(
        name for name in os.listdir('projects')
        if os.path.isdir(os.path.join('projects', name))
    )
    lines.append(f"PROJECTS ({len(projects)})")
    lines.append("-" * 30)
    for name in projects:
        lines.append(f"  • {name}")
except Exception as e:
    lines.append(f"Could not list projects: {e}")

lines.append("")

# ── ARCHIE — LAST SLEEP ─────────────────────────
# Sleep-log columns: Date | Bedtime (prev. night) | Wake time | Resettled? | Back to sleep until | Nap | Notes
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
        if len(cells) >= 7:
            date, bedtime, wake, resettled, back_to_sleep, nap, notes = cells[:7]
            lines.append(f"ARCHIE — last sleep ({date})")
            lines.append("-" * 30)
            lines.append(f"  Bedtime (prev. night): {bedtime}")
            lines.append(f"  Wake:                  {wake}")
            if resettled and resettled != '-':
                lines.append(f"  Resettled:             {resettled}")
            if back_to_sleep and back_to_sleep != '-':
                lines.append(f"  Back to sleep until:   {back_to_sleep}")
            if nap and nap != '-':
                lines.append(f"  Nap:                   {nap}")
            if notes:
                lines.append(f"  Notes:                 {notes}")
except Exception as e:
    lines.append(f"Could not read sleep log: {e}")

lines.append("")
lines.append("-" * 30)
lines.append("Your personal assistant · github.com/tristanpatrickmorgan-private/claude")

print('\n'.join(lines))
