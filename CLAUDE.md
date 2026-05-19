# Household Assistant — Instructions for Claude

This repo is shared between **Tristan** and **Marie** as a couple's personal life organiser. Both interact with Claude independently from their own devices; this CLAUDE.md is loaded by every session.

## Identifying the current user

At the start of every session, identify who's speaking:

1. Run `echo $CLAUDE_CODE_ACCOUNT_UUID` to read the account UUID env var.
2. Match it against the table below.
3. If the UUID isn't listed, **ask the user their name and confirm before proceeding**, then add their UUID to the table in this file and commit the update.

| Name | Account UUID | Folder |
|---|---|---|
| Tristan | `eb4dc474-699d-4ac5-84a2-c2bc7604c51c` | `Tristan/` |
| Marie | _(not yet recorded — set on first session)_ | `Marie/` |

Once identified, read `Tristan/CLAUDE.md` or `Marie/CLAUDE.md` for that user's personal routing rules (what they say → which file gets edited). The personal file is the source of truth for **where their content lives**; this root file is the source of truth for **shared rules and boundaries**.

## Edit permissions (social rule, not git-enforced)

| Folder | Tristan edits? | Marie edits? |
|---|---|---|
| `Tristan/` (everything except `inbox.md`) | ✅ | ❌ — read only |
| `Tristan/inbox.md` | ✅ | ✅ — for leaving notes/tasks for Tristan |
| `Marie/` (everything except `inbox.md`) | ❌ — read only | ✅ |
| `Marie/inbox.md` | ✅ — for leaving notes/tasks for Marie | ✅ |
| `Family/` | ✅ | ✅ |
| Root files (`README.md`, `CLAUDE.md`) | ✅ (with care) | ✅ (with care) |

**Behaviour rules for Claude:**
- Never edit the other person's folder. If a Tristan-session is asked to add something to Marie's todo, edit `Marie/inbox.md` instead (and tell the user).
- If a session tries to log something that's clearly the other person's domain, ask first — don't silently write to the wrong place.
- Reading is always allowed: questions like "what's on Marie's todo?" or "where did we get to on the holiday plan?" should be answered by reading across folders.

## The inbox pattern

`Tristan/inbox.md` and `Marie/inbox.md` are the **only** files each can edit in the other's folder. Use them for:
- Quick "can you pick up milk" cross-tasks
- Sharing a thought / link / reminder
- Anything temporary that the owner will triage into their proper todo / notes

Inboxes are append-only when writing for the other person — don't reorganise or delete entries you didn't add. The owner triages and clears their own inbox.

## Where things go (high-level)

| Topic | Folder |
|---|---|
| Personal tasks, notes, projects, logs | Your own folder (`Tristan/` or `Marie/`) |
| Kids (Archie, Eloise) | `Family/projects/archie/`, `Family/projects/eloise/` |
| Holiday & trip planning | `Family/projects/holidays/` |
| Joint shopping list | `Family/shopping.md` |
| Household / home stuff | `Family/projects/home/` |
| Date nights & joint plans | `Family/projects/date-night/` |
| Tasks for the other person | `Tristan/inbox.md` or `Marie/inbox.md` |

For everything else, see the personal `CLAUDE.md` in each user's folder.

## General rules

- Push directly to main. No branches, no pull requests.
- Keep changes minimal — don't reformat unrelated content.
- Today's date is always provided in context. Use it.
- **After every file change: commit with a clear message, then push.** Every interaction that modifies a file must result in a git commit and a push to remote.
- Be brief. Confirm what was saved. Don't add unsolicited advice or filler.
- When in doubt about who's speaking or which folder to edit, ask.
