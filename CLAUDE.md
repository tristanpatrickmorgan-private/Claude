# My Personal Assistant — Instructions for Claude

This repo is my personal life organiser. Keep everything simple and low-friction.

## General rules
- Push directly to main. No branches, no pull requests.
- Keep changes minimal — don't reformat unrelated content.
- Today's date is always provided in context. Use it.

## Files and where things go

| What I say | What to do |
|---|---|
| Add a to-do / task | Append to `todo.md` under the right section |
| Mark something done | Tick it off in `todo.md` and move to `## Done` with the date |
| Shopping list | Edit `shopping.md` — add items under the relevant store or `## General` |
| Gym / fitness | Append to `logs/gym.md` under a `## YYYY-MM-DD` heading |
| Log something / note something | Append to `logs/YYYY-MM.md` under a `## YYYY-MM-DD` heading |
| Holiday / trip planning | Edit `notes/holidays.md`, creating it if it doesn't exist |
| Any other list or note | Create a simple `.md` file in the right place and tell me |

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

**logs/gym.md**
```
# Gym Log

## 2026-04-27
- Squats: 3x8 @ 100kg
- Bench: 3x10 @ 70kg
```

**logs/YYYY-MM.md**
```
# April 2026

## 2026-04-27
- Discussed holiday plans with Sarah — leaning towards Portugal in September
```

## Tone
Be brief. Confirm what was saved. Don't add unsolicited advice or filler.
