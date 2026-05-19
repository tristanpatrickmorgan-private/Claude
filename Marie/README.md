# Welcome, Marie 👋

This is your personal area in our shared household assistant repo. You and Tristan each have your own folder; both can read everything but each only edits their own.

## How to get started

1. **Open Claude on your phone (the free app) or web** — log in with your account.
2. **Open this repo** — it'll be linked to you as a GitHub collaborator.
3. The very first time you chat with Claude here, it'll detect your account is new and ask "Are you Marie?" — say yes, and your account UUID gets recorded in the root `CLAUDE.md`. From then on Claude knows it's you automatically.
4. Just talk to Claude naturally — ask it to log something, add a to-do, take a note. It'll figure out where to save things and commit/push for you.

## Try these to start

- "What's in my inbox?" → Claude reads `Marie/inbox.md`
- "Add to my to-do: book the dentist" → goes to `Marie/todo.md`
- "Log: had coffee with Anna today, she's planning a baby" → appends to `Marie/logs/2026-05.md`
- "What's on the joint shopping list?" → reads `Family/shopping.md`
- "Add Greek yoghurt to the joint shopping" → adds to `Family/shopping.md`
- "Remind Tristan to call the plumber" → appends to `Tristan/inbox.md`
- "What's Archie's bedtime been recently?" → reads `Family/projects/archie/sleep-log.md`

## What's in your folder

| File / Folder | What it's for |
|---|---|
| `CLAUDE.md` | Your personal routing rules (what you say → which file Claude edits). Grows over time. |
| `README.md` | This file. |
| `inbox.md` | Tristan can drop tasks/notes for you here. Only file in your folder that he can edit. |
| `todo.md` | Your to-do list. |
| `shopping.md` | Your personal shopping list (joint shopping is in `Family/shopping.md`). |
| `logs/` | Daily notes (one file per month, e.g. `2026-05.md`), plus any logs you want to keep. |
| `notes/` | Free-form notes. |
| `projects/` | Anything bigger than a note — e.g. work, books, hobbies. Empty for now; Claude will help you set these up as you go. |

## What's shared (`Family/`)

Both of you edit these freely:

- `Family/shopping.md` — joint shopping list
- `Family/projects/archie/` — Archie (notes, sleep log, milestones)
- `Family/projects/eloise/` — Eloise
- `Family/projects/holidays/` — trip planning
- `Family/projects/home/` — household
- `Family/projects/date-night/` — joint plans

## What's Tristan's (`Tristan/`)

Read freely, but **don't edit** anything except `Tristan/inbox.md`. If you want to ask him to do something or share a thought, that's what his inbox is for.

## A few tips

- **Just be conversational.** No need to remember file paths — Claude figures it out from what you ask.
- **If unsure where something belongs, say so.** Claude will suggest and confirm before writing.
- **Anything sensitive (passwords, 2FA codes) — don't store here.** Usernames are OK in `accounts.md` if you create one, but passwords belong in a password manager.
- **Claude commits and pushes automatically.** Everything you do is saved and visible to both of you immediately.

Welcome aboard. ❤️
