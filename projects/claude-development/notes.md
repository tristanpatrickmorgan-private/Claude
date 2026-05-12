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
Brainstorming — nothing built yet.
