# Household Assistant

A simple shared life organiser powered by Claude + GitHub, used by **Tristan** and **Marie**.

Each of us chats with Claude from our own device. Claude figures out which of us is speaking (from the account UUID), reads our personal context, and edits the right files. Both of us can read everything; each of us only edits our own folder, plus the `Family/` folder for joint things.

## Layout

```
README.md          — this file
CLAUDE.md          — Claude's instructions (universal rules + user detection)

Tristan/           — Tristan's stuff (only he edits, both read)
  CLAUDE.md          — Tristan's personal routing rules
  inbox.md           — Marie can drop tasks/notes here for Tristan
  todo.md, accounts.md, logs/, notes/, projects/, scripts/

Marie/             — Marie's stuff (only she edits, both read)
  CLAUDE.md          — Marie's personal routing rules
  README.md          — Marie's onboarding doc
  inbox.md           — Tristan can drop tasks/notes here for Marie
  todo.md, shopping.md, logs/, notes/, projects/

Family/            — joint, both edit
  shopping.md        — joint shopping
  projects/
    archie/          — Archie (kids)
    eloise/          — Eloise (kids)
    holidays/        — trip & holiday planning
    home/            — household
    date-night/      — joint plans
```

## How we use it

Just talk to Claude naturally:

- "Add milk to the shopping list" → `Family/shopping.md` (joint) or your personal `shopping.md`
- "Log gym: 3x10 bench at 70kg" → `Tristan/logs/gym.md` if Tristan; `Marie/logs/gym.md` if Marie
- "Remind Marie to book the dentist" → appended to `Marie/inbox.md`
- "What's on my to-do list?" → reads `Tristan/todo.md` (or Marie's)
- "How are Archie's naps going?" → reads `Family/projects/archie/sleep-log.md`

Claude handles file routing, commits, and pushes automatically. The key rule: **each person only edits their own folder, except for the other person's `inbox.md`**.

## Inboxes

`Tristan/inbox.md` and `Marie/inbox.md` are the bridge. If Tristan tells Claude "remind Marie to grab cherries on the way home", Claude appends to `Marie/inbox.md`. Marie sees it next session and decides whether to triage it into her todo, log it, or just acknowledge.

Don't delete things you didn't add to someone else's inbox — that's the owner's job.

## Setup for new device

1. Log in to Claude on the device with your own account (Tristan: `tristan@trine.com`; Marie: her Gmail).
2. Open this repo in Claude Code / mobile app.
3. First time, Claude will detect an unknown UUID and ask "Are you Tristan or Marie?" — answer once, it'll be remembered.
4. Talk to Claude normally — everything's automated from there.
