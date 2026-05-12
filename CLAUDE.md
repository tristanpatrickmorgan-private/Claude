# My Personal Assistant — Instructions for Claude

This repo is my personal life organiser. Keep everything simple and low-friction.

## General rules
- Push directly to main. No branches, no pull requests.
- Keep changes minimal — don't reformat unrelated content.
- Today's date is always provided in context. Use it.
- **After every file change: commit with a clear message, then push.** Every interaction that modifies a file must result in a git commit and a push to remote. This is non-negotiable — do not skip the push.

## Files and where things go

| What I say | What to do |
|---|---|
| Add a to-do / task | Append to `todo.md` under the right section |
| Mark something done | Tick it off in `todo.md` and move to `## Done` with the date |
| Shopping list | Edit `shopping.md` — add items under the relevant store or `## General` |
| Gym / fitness / health | Append gym logs to `logs/gym.md`; edit plan at `projects/health-fitness/training-plan.md` |
| Log something / note something | Append to `logs/YYYY-MM.md` under a `## YYYY-MM-DD` heading |
| Holiday / trip planning | Edit `notes/holidays.md` |
| Meal ideas | Edit `notes/meals.md` |
| Swedish learning | Edit `projects/swedish/notes.md` |
| Archie — general | Edit `projects/archie/notes.md` |
| Archie — sleep | Append a row to `projects/archie/sleep-log.md` |
| Eloise | Edit `projects/eloise/notes.md` |
| Books / reading / habits | Edit `projects/habits/notes.md` |
| Notes on a specific book | Create or edit `projects/habits/<book-slug>-notes.md` |
| Jeep / Land Rover build | Edit `projects/jeep-build/notes.md` |
| Any other list or note | Create a simple `.md` file in the right place and tell me |

## Projects

| Folder | What it's for |
|---|---|
| `projects/health-fitness/` | Training plan, gym context |
| `projects/swedish/` | Swedish learning notes, vocabulary, progress |
| `projects/archie/` | Archie (born 12 Mar 2024) — milestones, health, memories, sleep tracking |
| `projects/eloise/` | Eloise (born 3 Nov 2025) — milestones, health, memories |
| `projects/habits/` | Reading log, intentions, habit tracking, per-book notes |
| `projects/jeep-build/` | Half-scale Willy's Jeep or Land Rover build project |

## Full file structure (as it exists)

```
todo.md                               tasks and to-dos
shopping.md                           shopping lists
logs/
  gym.md                              gym sessions (newest first)
  YYYY-MM.md                          general daily notes
notes/
  holidays.md                         trip and holiday planning
  meals.md                            meal ideas by category
projects/
  health-fitness/
    training-plan.md                  current training plan with exercise guide
  archie/
    notes.md                          sleep context/routine, milestones, health, memories
    sleep-log.md                      ongoing early-waking tracker (table, append new rows)
  eloise/
    notes.md                          milestones, health, memories
  habits/
    notes.md                          reading list, intentions, books read/in progress
    the-trusted-advisor-notes.md      example of a per-book notes file
  swedish/
    notes.md                          vocabulary, grammar notes, books, progress
  jeep-build/
    notes.md                          research, plans, build log
```

## File formats

**todo.md**
```
# To-do

- [ ] Buy milk
- [ ] Call the dentist

## Done
- [x] 2026-04-27 — Book restaurant
```

**shopping.md**
```
# Shopping

## General
- [ ] Milk
- [ ] Bread
```

**logs/gym.md** — newest session at the top
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

**logs/YYYY-MM.md**
```
# April 2026

## 2026-04-27
- Discussed holiday plans with Sarah — leaning towards Portugal in September
```

**projects/archie/sleep-log.md** — append a new row to the existing table
```
| Date | Wake time | Nap | Nap duration | Bedtime | Notes |
|---|---|---|---|---|---|
| 2026-05-06 | 4:50am | - | - | 7pm | Resettled when told to lie down. Woke 5:58 — brought to bed at 6am. |
```

## Tone
Be brief. Confirm what was saved. Don't add unsolicited advice or filler.
