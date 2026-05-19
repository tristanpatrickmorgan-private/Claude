# Tristan — Personal Context for Claude

Personal routing rules. Loaded alongside the root `CLAUDE.md` when the current user is Tristan.

## What I say → what to do

| What I say | What to do |
|---|---|
| Add a to-do / task | Append to `Tristan/todo.md` under the right section |
| Mark something done | Tick it off in `Tristan/todo.md` and move to `## Done` with the date |
| Personal shopping (just for me) | Edit `Tristan/shopping.md` (create if needed) |
| Joint / household shopping | Edit `Family/shopping.md` |
| Gym / fitness / health | Append gym logs to `Tristan/logs/gym.md`; edit plan at `Tristan/projects/health-fitness/training-plan.md` |
| Log something / note something | Append to `Tristan/logs/YYYY-MM.md` under a `## YYYY-MM-DD` heading |
| Holiday / trip planning | Edit `Family/projects/holidays/notes.md` (joint) |
| Meal ideas | Edit `Tristan/notes/meals.md` |
| Swedish learning | Edit `Tristan/projects/swedish/notes.md` |
| Archie — general / sleep | Edit `Family/projects/archie/notes.md` or append to `Family/projects/archie/sleep-log.md` |
| Eloise | Edit `Family/projects/eloise/notes.md` |
| Books / reading / habits | Edit `Tristan/projects/habits/notes.md` |
| Notes on a specific book | Create or edit `Tristan/projects/habits/<book-slug>-notes.md` |
| Jeep / Land Rover build | Edit `Tristan/projects/jeep-build/notes.md` |
| UK rental / tax (76a Ingelow) | `Tristan/projects/uk-rental/` |
| Account credentials / usernames | Append to `Tristan/accounts.md` (usernames only — never passwords or 2FA seeds) |
| Something for Marie | Append to `Marie/inbox.md` (and tell me you did) |
| Any other list or note | Create a simple `.md` file in the right place and tell me |

## My projects

| Folder | What it's for |
|---|---|
| `Tristan/projects/claude-development/` | Claude/AI tooling experiments |
| `Tristan/projects/health-fitness/` | Training plan, gym context |
| `Tristan/projects/swedish/` | Swedish learning notes, vocabulary, progress |
| `Tristan/projects/habits/` | Reading log, intentions, habit tracking, per-book notes |
| `Tristan/projects/jeep-build/` | Half-scale Willys Jeep or Land Rover build project |
| `Tristan/projects/uk-rental/` | 76a Ingelow Road — mortgage, tax filings, working spreadsheets |

## Inbox

`Tristan/inbox.md` is where Marie can drop tasks/notes/links for me. When I open a session, check it and:
- Triage anything actionable into my todo / logs / projects
- Once triaged, delete the entry from inbox (only entries Marie left for me)

## File formats

**`Tristan/todo.md`**
```
# To-do

- [ ] Buy milk
- [ ] Call the dentist

## Done
- [x] 2026-04-27 — Book restaurant
```

**`Tristan/logs/gym.md`** — newest session at the top
```
# Gym Log

## 2026-05-05 — Session A (Push + Cardio)

**Strength — 3 rounds:**

| Exercise | Round 1 | Round 2 | Round 3 |
|---|---|---|---|
| Barbell floor press | 20 reps @ 16kg | 20 reps @ 16kg | 20 reps @ 16kg |

**Cardio:** 20 min @ 10km/h (~3.3km).

**Notes:** Brief observation.
```

**`Tristan/logs/YYYY-MM.md`**
```
# April 2026

## 2026-04-27
- Discussed holiday plans with Sarah — leaning towards Portugal in September
```

**`Family/projects/archie/sleep-log.md`** — append a new row to the existing table
```
| Date | Wake time | Nap | Nap duration | Bedtime | Notes |
|---|---|---|---|---|---|
| 2026-05-06 | 4:50am | - | - | 7pm | Resettled when told to lie down. Woke 5:58 — brought to bed at 6am. |
```

## Tone

Be brief. Confirm what was saved. Don't add unsolicited advice or filler.
