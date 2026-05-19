# Marie — Personal Context for Claude

Personal routing rules. Loaded alongside the root `CLAUDE.md` when the current user is Marie.

> **Note:** This is a starter file. Tell Claude what you'd like to track and Claude will add to this routing table over time.

## What I say → what to do (starter)

| What I say | What to do |
|---|---|
| Add a to-do / task | Append to `Marie/todo.md` under the right section |
| Mark something done | Tick it off in `Marie/todo.md` and move to `## Done` with the date |
| Personal shopping (just for me) | Edit `Marie/shopping.md` |
| Joint / household shopping | Edit `Family/shopping.md` |
| Log something / note something | Append to `Marie/logs/YYYY-MM.md` under a `## YYYY-MM-DD` heading |
| Holiday / trip planning | Edit `Family/projects/holidays/notes.md` (joint) |
| Archie — general / sleep | Edit `Family/projects/archie/notes.md` or `Family/projects/archie/sleep-log.md` |
| Eloise | Edit `Family/projects/eloise/notes.md` |
| Account credentials / usernames | Create `Marie/accounts.md` if needed (usernames only — never passwords or 2FA seeds) |
| Something for Tristan | Append to `Tristan/inbox.md` (and tell me you did) |
| Any other list or note | Create a simple `.md` file in the right place and tell me |

## My projects

_None yet — Claude will help you set these up as you start using new categories. Likely candidates:_

- `Marie/projects/work/` — work / career notes
- `Marie/projects/books/` — reading list, book notes
- `Marie/projects/health/` — fitness, health log

## Inbox

`Marie/inbox.md` is where Tristan can drop tasks/notes/links for me. When I open a session:
- Check inbox.md
- Triage anything actionable into my todo / logs / projects
- Once triaged, remove the entry from inbox

## File formats

**`Marie/todo.md`**
```
# To-do

- [ ] Buy milk
- [ ] Call the dentist

## Done
- [x] 2026-05-19 — Book restaurant
```

**`Marie/logs/YYYY-MM.md`**
```
# May 2026

## 2026-05-19
- Notes about the day...
```

## Tone

Be brief. Confirm what was saved. Don't add unsolicited advice or filler.
