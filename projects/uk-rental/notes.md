# 76a Ingelow Road — UK rental property

Mortgage and tax notes for the rental property at 76a Ingelow Road, London SW8 3PF.

## Property
- Address: **76a Ingelow Road, London SW8 3PF**
- Mortgage account: **Santander 0915/862/044470945/MOR**
- Mortgage started: **21 January 2020**
- Managed by: Knight Frank

## Mortgage product timeline

| From | To | Type | Rate | Monthly | Term |
|---|---|---|---|---|---|
| 21 Jan 2020 | 02 Feb 2025 | Repayment | 1.49% fixed | £940.33 | (original) |
| 03 Feb 2025 | 02 May 2027 | **Interest only** | 4.38% fixed | £652.49 | 17 yrs 2 mo remaining |

- Product fee on switch: **£1,749.00** (charged 03 Feb 2025, added to balance)
- ERC if paid off before 02/05/2027: **£3,575.30**

## Tax-year totals (mortgage interest + fees)

### UK tax years (6 April – 5 April)

| Year | Interest (£) | Fees (£) | Total (£) | Coverage |
|---|---|---|---|---|
| 22/23 | 1,023.29 | 0 | 1,023.29 | Partial (Jan-Mar 2023 only) |
| 23/24 | 3,147.55 | 0 | 3,147.55 | Apr-Dec 2023 (PDF) + Jan-Mar 2024 (spreadsheet) |
| 24/25 | 5,680.73 | 1,749.00 | 7,429.73 | Apr-Dec 2024 (spreadsheet, partial Sep-Dec gap) + Jan-Mar 2025 (PDF) |
| **25/26** | **7,829.88** | **0** | **7,829.88** | **Full year ✓ (statement)** |
| 26/27 | 652.49 | 0 | 652.49 | Partial (May 2026 only so far) |

### Swedish tax years (calendar year)

| Year | Interest (£) | Fees (£) | Total (£) | Coverage |
|---|---|---|---|---|
| **2023** | **3,013.06** | **0** | **3,013.06** | **Full year ✓ (statement)** |
| 2024 | 5,103.41 | 0 | 5,103.41 | **Partial — Jan-Aug only, Sep-Dec MISSING** |
| **2025** | **6,955.02** | **1,749.00** | **8,704.02** | **Full year ✓ (statement)** |
| 2026 | 3,262.45 | 0 | 3,262.45 | Partial (Jan-May 2026 only) |

### Caveats on 2024 figures
- 2024 data is from your Cashflows spreadsheet, NOT a Santander 2024 statement.
- **Jul 2024 interest = £2,397.11** in the spreadsheet — this is anomalous (~11× a normal month). Likely a one-time correction/fee mislabeled as interest. Real interest at 1.49% on ~£177k would be ~£220.
- **Aug 2024 interest = £652.49** matches the post-Feb-2025 rate (4.38%) rather than the 1.49% deal that should have been active. Looks like a projection rather than actual statement data.
- **Sep-Dec 2024**: no data — would need 2024 annual statement.
- The opening balance in Jan 2024 from the spreadsheet is £189,805.22 vs the actual Dec 2023 PDF close of £195,880.10 (~£6k below). The whole 2024 chain inherits this drift.

If you want defensible figures for the Swedish 2024 return, **request the 2024 annual statement** — it's the only way to get accurate Jan-Dec 2024 interest.

## Data sources

| Period | Source | Status |
|---|---|---|
| Jan-Dec 2023 | 2023 annual statement PDF | Authoritative ✓ |
| Jan-Aug 2024 | User's spreadsheet | Best available, has model drift |
| Sep-Dec 2024 | — | **Missing** |
| Jan-Dec 2025 | 2025 annual statement PDF | Authoritative ✓ |
| Jan-May 2026 | Online banking PDF | Authoritative ✓ |

## The £234.92 puzzle

Two suspiciously matching figures:

1. **Aug 2024 spreadsheet close → Jan 2025 statement open: balance UP £234.92**
   - Aug 2024 spreadsheet actual close: £178,764.94
   - 1 Jan 2025 statement open: £178,999.86

2. **Jan 2025 → Dec 2025: balance DOWN £234.92**
   - 2025 capital paid £1,983.92, product fee added £1,749.00 → net −£234.92
   - Closed back at £178,764.94

**Most likely explanation**: somewhere in Sep-Dec 2024, interest of about £234 was charged but not covered by a direct debit — probably a single month's missed/skipped payment that simply added to the balance. At 1.49% on £178,764.94 the monthly interest is **£221.93** — close enough to £234.92 that one month with a slight rate or fee adjustment fits exactly. The 2024 annual statement would confirm this.

## Files in this folder

| File | What it is |
|---|---|
| `notes.md` | This file — overview and tax-year totals |
| `mortgage-monthly.xlsx` | Monthly mortgage table + tax summary sheet |
| `mortgage-monthly.csv` | Same data as CSV for easy pasting |

## Open actions

- [ ] **Request 2024 annual Santander statement** to fill the Sep-Dec 2024 gap and confirm the £234.92 hypothesis
- [ ] UK 2025/26 tax return — mortgage interest **£7,829.88** (full year ✓)
- [ ] Swedish 2025 tax return — mortgage interest **£6,955.02** + fee **£1,749.00** = **£8,704.02** total deductible
- [ ] Swedish 2024 tax return — provisional **£5,103.41** but should be refined once 2024 statement obtained (Jul 2024 figure looks like a misclassified fee)
