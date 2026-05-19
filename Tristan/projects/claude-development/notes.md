# Claude Development

Ideas for making this setup more powerful — automations, integrations, improvements.

## Ideas to explore

### Daily digest / notifications
Send a daily summary (to-do list, Archie sleep log, reminders) via email or messaging app.

**Options:**
- **GitHub Actions (scheduled)** — runs on a cron schedule, reads files from the repo, sends an email. Free, no extra infrastructure needed. Most realistic starting point.
- **Email** — easiest delivery method. GitHub Actions can send via Gmail (app password) or a service like SendGrid/Resend.
- **WhatsApp** — possible via Twilio API or WhatsApp Business API but requires paid account and more setup.
- **Telegram** — easier than WhatsApp from an API perspective, free bot API, could be a good middle ground.
- **iOS Shortcut + webhook** — could trigger a summary on demand from your phone.

**What could be in a daily digest:**
- Open to-dos
- Archie sleep summary (last 7 days)
- Any upcoming reminders (e.g. doctor follow-ups)
- Holiday / trip reminders

### Other automation ideas
- Reminder when a to-do has been open for X days
- Weekly sleep summary for Archie auto-generated
- Prompt to log gym session if no entry in X days

## Status
- Daily email digest — **built** (GitHub Action + `scripts/daily_email.py`)
- SessionStart hook surfacing open todos + shopping — **built** (`.claude/hooks/session-start.sh`)
- Everything else below — brainstorming

---

## Research: how others use Claude as a personal assistant

Researched 2026-05-15. Sources at end.

### Setups people have built
- **davidhariri/life-system** — Plain-text "life OS" inspired by Carmack's `.plan` files. Layout: `journal/2026/`, `people/`, `reference/`, `decisions/`, `templates/`, `skills/morning/`, plus root `plan.md` (10-year vision), `inbox.md`, `CLAUDE.md`. Uses `[[wiki-links]]`. A `jrn` script creates today's journal, backfills missing days, carries forward uncompleted todos, pulls calendar events. https://github.com/davidhariri/life-system
- **ballred/obsidian-claude-pkm** — Obsidian vault + Claude Code starter kit. Folders for `Goals/` (3-year / yearly / monthly), `Daily Notes/`, `Projects/`. Ships slash commands `/daily`, `/weekly`, `/push`. Agents for note organisation, weekly review, goal alignment, inbox processing. Auto-commit hook on file change. https://github.com/ballred/obsidian-claude-pkm
- **c0dezli/claude-code-personal-assistant** — Template with Notion MCP + Google Workspace MCP + Python "task analyzers" that bulk-fetch tasks to save context. https://github.com/c0dezli/claude-code-personal-assistant
- **Obie Fernandez — "Personal CTO OS"** — User as CEO, Claude as Chief of Staff; structured files for OKRs, decisions, meetings. https://obie.medium.com/building-a-personal-cto-operating-system-with-claude-code-b3fb9c4933c7
- **Karpathy's LLM Wiki pattern** — Dump raw info, give Claude a schema, let it maintain a structured markdown wiki. Widely copied. https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code

### Common patterns
- **Morning / evening routines as skills** — `/morning` reviews yesterday and sets today's priorities tied to annual goals; `/evening` for reflection.
- **Daily-note auto-generation with carry-forward** — Today's note is generated from a template, unfinished todos roll over, calendar embedded.
- **Weekly review skill** — Reads the week's daily notes, scores goal progress, drafts next week.
- **Auto-logging** — Mentioned tasks appended to the right file; done items moved to `## Done` with date (matches this setup).
- **Auto-commit + push hook** — File-change hook syncs vault to GitHub for cross-device access.
- **Per-domain split files** — `work.md`, `personal.md`, `home.md`, plus a `log.md` for session activity.
- **Daily/weekly digest emails** — Scheduled GitHub Action runs Claude Code in headless mode and emails the output. https://github.com/ROCm/repo-digest

### Integrations and hooks
- **Anthropic Routines** — official cloud-scheduled Claude Code runs; replaces self-hosted cron. https://code.claude.com/docs/en/scheduled-tasks
- **MCP servers commonly used personally**: Google Workspace (Gmail/Calendar/Drive), Notion, Slack, WhatsApp, Linear, Todoist. Harper Reed's email-triage write-up is canonical. https://harper.blog/2025/12/03/claude-code-email-productivity-mcp-agents/
- **Phone access via Telegram bot**: `linuz90/claude-telegram-bot` (voice, photos, docs) or `seedprod/claude-code-telegram`. `OpenClaw` adds iMessage and WhatsApp. https://github.com/linuz90/claude-telegram-bot · https://openclaw.ai
- **SessionStart hooks** currently only run shell commands, can't auto-execute a prompt. Open feature request: https://github.com/anthropics/claude-code/issues/37122

### Where Claude beats alternatives
- **vs Obsidian + plugins** — Obsidian plugins are rule-based; Claude understands intent and can refactor across 400 files at once. Most people run Claude *inside* the vault. https://www.eleanorkonik.com/p/claude-obsidian-got-a-level-up
- **vs Notion AI / Reflect** — Plain markdown on disk + git, fully portable, no vendor lock-in.
- **vs ChatGPT** — No native local-file loop in ChatGPT; Claude Code reads, edits, commits without copy-paste.
- **vs consumer Claude.ai** — Claude.ai has no persistent file system or cross-session memory of your structure.

### Pitfalls reported
- **Context window decay** — Files grow forever; rule of thumb is `CLAUDE.md` under ~200 lines. https://claudecodeai.blog/claude-code-context-window-size-limits-tips/
- **Auto-compaction quality drop** — Around turn 50–80, summarisation loses nuance.
- **SessionStart hooks can't run prompts** — many users want an auto "morning briefing" but must type a slash command.
- **Git noise** — Auto-commit on every change produces thousands of micro-commits; better to batch with `/push` end-of-day.

### Ideas worth stealing
- **`/morning` and `/evening` slash commands** — generate today's `logs/YYYY-MM.md` heading, carry forward yesterday's open todos, summarise yesterday's gym/Archie entries.
- **`/weekly` review** — every Sunday, read the week's logs + sleep-log + gym + todo Done section, produce a one-page review under `reviews/`.
- **Carry-forward script** — top of each day auto-pulls uncompleted `- [ ]` items from yesterday into today.
- **`inbox.md`** — single fast-capture file (e.g. via Telegram bot from phone), processed weekly into the right home.
- **Per-person memory files** — `people/sarah.md`, `people/mum.md` with prefs, birthdays, last conversations.
- **Decisions log** — `decisions/YYYY-MM-DD-<slug>.md` with context/options/choice.
- **Calendar + email MCP** — pull today's events into the daily log; let Claude draft inbox replies each morning.
- **Telegram bot pointed at this repo** — capture todos, gym logs, Archie wake times from phone without a terminal.
- **Weekly auto-digest** — extend the daily-email Action with a Sunday "week in review" mode.
- **`STATUS.md` glance file** — auto-maintained dashboard: open todos count, last gym, Archie's last wake.
- **Wiki-link book notes** — link each book in `projects/habits/notes.md` back to `[[<book-slug>-notes]]`.

### Sources
- https://github.com/davidhariri/life-system
- https://github.com/ballred/obsidian-claude-pkm
- https://github.com/c0dezli/claude-code-personal-assistant
- https://obie.medium.com/building-a-personal-cto-operating-system-with-claude-code-b3fb9c4933c7
- https://jngiam.bearblog.dev/the-instruction-that-turns-claude-into-a-self-improving-system/
- https://hannahstulberg.substack.com/p/claude-code-for-everything-the-best-personal-assistant-remembers-everything-about-you
- https://harper.blog/2025/12/03/claude-code-email-productivity-mcp-agents/
- https://code.claude.com/docs/en/scheduled-tasks
- https://code.claude.com/docs/en/mcp
- https://github.com/anthropics/claude-code/issues/37122
- https://github.com/linuz90/claude-telegram-bot
- https://github.com/seedprod/claude-code-telegram
- https://openclaw.ai/
- https://www.eleanorkonik.com/p/claude-obsidian-got-a-level-up
- https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code
- https://github.com/ROCm/repo-digest
- https://claudecodeai.blog/claude-code-context-window-size-limits-tips/
- https://www.anthropic.com/research/claude-personal-guidance
