"""Weekly review email — past 7 days ending today.

Reads gym log, Archie sleep log, and todo.md. Prints a summary to stdout.
"""

import re
from datetime import datetime, timezone, timedelta, date

# Swedish time
tz = timezone(timedelta(hours=2))  # CEST (summer); change to +1 in winter
today = datetime.now(tz).date()
week_end = today
week_start = today - timedelta(days=6)
date_range = f"{week_start.strftime('%a %d %b')} – {week_end.strftime('%a %d %b %Y')}"


def in_week(d_str):
    try:
        d = date.fromisoformat(d_str)
        return week_start <= d <= week_end
    except (ValueError, TypeError):
        return False


def parse_time(t):
    """Parse '5:30am' or '7:00pm' -> minutes since midnight, or None."""
    if not t:
        return None
    t = t.strip().lower().replace(' ', '')
    m = re.match(r'(\d{1,2}):(\d{2})(am|pm)', t)
    if not m:
        return None
    h, mn, ampm = int(m.group(1)), int(m.group(2)), m.group(3)
    if ampm == 'pm' and h != 12:
        h += 12
    if ampm == 'am' and h == 12:
        h = 0
    return h * 60 + mn


def fmt_time(mins):
    h, m = divmod(mins, 60)
    ampm = 'am' if h < 12 else 'pm'
    h12 = h % 12 or 12
    return f"{h12}:{m:02d}{ampm}"


lines = []
lines.append(f"Weekly review — {date_range}")
lines.append("")

# ── ARCHIE SLEEP ─────────────────────────────
# Columns: Date | Bedtime (prev. night) | Wake time | Resettled? | Back to sleep until | Nap | Notes
try:
    with open('projects/archie/sleep-log.md') as f:
        content = f.read()
    rows = [
        l for l in content.split('\n')
        if l.startswith('|')
        and not l.startswith('| Date')
        and not l.startswith('|---')
    ]
    week_rows = []
    for r in rows:
        cells = [c.strip() for c in r.split('|')[1:-1]]
        if len(cells) >= 7 and in_week(cells[0]):
            week_rows.append(cells)

    lines.append(f"ARCHIE SLEEP ({len(week_rows)} entries)")
    lines.append("-" * 30)
    if week_rows:
        wake_mins = [m for m in (parse_time(c[2]) for c in week_rows) if m is not None]
        if wake_mins:
            avg = sum(wake_mins) // len(wake_mins)
            lines.append(f"  Avg wake:  {fmt_time(avg)}")
            lines.append(f"  Earliest:  {fmt_time(min(wake_mins))}")
            lines.append(f"  Latest:    {fmt_time(max(wake_mins))}")
        resettled = sum(1 for c in week_rows if c[3].lower().startswith('y'))
        lines.append(f"  Resettled successfully: {resettled}/{len(week_rows)} nights")
        lines.append("")
        for c in week_rows:
            lines.append(f"  {c[0]}: bedtime {c[1]}, wake {c[2]}")
    else:
        lines.append("  No entries this week")
except Exception as e:
    lines.append(f"Could not read sleep log: {e}")

lines.append("")

# ── GYM ──────────────────────────────────────
try:
    with open('logs/gym.md') as f:
        content = f.read()
    headers = re.findall(r'^## (\d{4}-\d{2}-\d{2}) — (.+)$', content, re.MULTILINE)
    week_sessions = [(d, t) for d, t in headers if in_week(d)]

    lines.append(f"GYM ({len(week_sessions)} sessions)")
    lines.append("-" * 30)
    if week_sessions:
        for d, t in week_sessions:
            lines.append(f"  • {d} — {t}")
    else:
        lines.append("  No sessions this week")
except Exception as e:
    lines.append(f"Could not read gym log: {e}")

lines.append("")

# ── TODOS ────────────────────────────────────
try:
    with open('todo.md') as f:
        content = f.read()
    open_count = sum(1 for l in content.split('\n') if l.strip().startswith('- [ ]'))
    closed = []
    for l in content.split('\n'):
        m = re.match(r'^- \[x\] (\d{4}-\d{2}-\d{2}) — (.+)$', l.strip())
        if m and in_week(m.group(1)):
            closed.append((m.group(1), m.group(2)))

    lines.append(f"TODOS CLOSED THIS WEEK ({len(closed)})")
    lines.append("-" * 30)
    if closed:
        for d, t in closed:
            lines.append(f"  • {d} — {t}")
    else:
        lines.append("  None closed this week")
    lines.append("")
    lines.append(f"OPEN TODOS: {open_count}")
except Exception as e:
    lines.append(f"Could not read todo.md: {e}")

lines.append("")
lines.append("-" * 30)
lines.append("Your personal assistant · github.com/tristanpatrickmorgan-private/claude")

print('\n'.join(lines))
