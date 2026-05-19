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
| **23/24** | **2,952.23** | 0 | **2,952.23** | **Full year ✓** |
| **24/25** | **3,576.30** | **1,749.00** | **5,325.30** | **Full year ✓** |
| **25/26** | **7,829.88** | 0 | **7,829.88** | **Full year ✓** |
| 26/27 | 652.49 | 0 | 652.49 | Partial (May 2026 only so far) |

### Swedish tax years (calendar year)

| Year | Interest (£) | Fees (£) | Total (£) | Coverage |
|---|---|---|---|---|
| **2023** | **3,013.06** | 0 | **3,013.06** | **Full year ✓ (statement)** |
| **2024** | **2,803.66** | 0 | **2,803.66** | **Full year ✓ (derived)** |
| **2025** | **6,955.02** | **1,749.00** | **8,704.02** | **Full year ✓ (statement)** |
| 2026 | 3,262.45 | 0 | 3,262.45 | Partial (Jan-May 2026 only) |

## How 2024 was derived

2024 wasn't in the provided PDFs, but everything we need is known:
- Opening balance: **£195,880.10** (31 Dec 2023 close per 2023 statement)
- Rate: **1.49% fixed** (unchanged throughout 2024 — product ran until 02 Feb 2025)
- Standard monthly DD: **£940.33**
- Assumed monthly overpayment: **£700** (matches the late-2023 statement pattern)

Computed month-by-month at 1.49%/12 on the running balance:

| Month | Opening | Interest | Cap from DD | Overpay | Closing |
|---|---:|---:|---:|---:|---:|
| Jan 2024 | 195,880.10 | 243.22 | 697.11 | 700.00 | 194,482.99 |
| Feb 2024 | 194,482.99 | 241.48 | 698.85 | 700.00 | 193,084.14 |
| Mar 2024 | 193,084.14 | 239.75 | 700.58 | 700.00 | 191,683.56 |
| Apr 2024 | 191,683.56 | 238.01 | 702.32 | 700.00 | 190,281.23 |
| May 2024 | 190,281.23 | 236.27 | 704.06 | 700.00 | 188,877.17 |
| Jun 2024 | 188,877.17 | 234.52 | 705.81 | 700.00 | 187,471.36 |
| Jul 2024 | 187,471.36 | 232.78 | 707.55 | 700.00 | 186,063.81 |
| Aug 2024 | 186,063.81 | 231.03 | 709.30 | 700.00 | 184,654.51 |
| Sep 2024 | 184,654.51 | 229.28 | 711.05 | 700.00 | 183,243.46 |
| Oct 2024 | 183,243.46 | 227.53 | 712.80 | 700.00 | 181,830.66 |
| Nov 2024 | 181,830.66 | 225.77 | 714.56 | 700.00 | 180,416.10 |
| Dec 2024 | 180,416.10 | 224.02 | 716.31 | 700.00 | 178,999.78 |

**Dec 2024 close: £178,999.78** — reconciles to the Jan 2025 statement opening of **£178,999.86** within **£0.08**. So the model is essentially exact.

## £234.92 puzzle — resolved

The previous gap between the Cashflows spreadsheet's "Aug 2024 actual close" (£178,764.94) and the Jan 2025 statement opening (£178,999.86) **wasn't a real Santander event** — it was an error in the spreadsheet's tracking.

The correct Aug 2024 close (per the derived model above) is **£184,654.51**, not £178,764.94. The mortgage behaved consistently throughout 2024 with no missed payments, fees, or rate changes. The numeric coincidence between Aug→Jan 2024-25 (+£234.92) and 2025's net reduction (−£234.92) was just an artefact of the spreadsheet running a flawed model that happened to come out exact in 2025 only because the new interest-only deal hit different inputs.

## Data sources

| Period | Source | Status |
|---|---|---|
| Jan-Dec 2023 | 2023 annual statement PDF | Authoritative ✓ |
| Jan-Dec 2024 | **Derived** from rate × balance, reconciled to Jan 2025 PDF | Reliable ✓ |
| Jan-Dec 2025 | 2025 annual statement PDF | Authoritative ✓ |
| Jan-May 2026 | Online banking PDF | Authoritative ✓ |

## Files in this folder

| File | What it is |
|---|---|
| `notes.md` | This file — overview and tax-year totals |
| `mortgage-monthly.xlsx` | Monthly mortgage table + tax summary sheet |
| `mortgage-monthly.csv` | Same data as CSV for easy pasting |

## Filing status

| Year | UK return | Swedish return |
|---|---|---|
| 2023 | Filed (prior years) | Filed (prior years) |
| 2024 | Filed | Filed (used net-of-commission position for schablonavdrag — different from 2025) |
| **2025** | **✅ Filed 2026-05-19 07:38 GMT** (HMRC ref 2605755020) | **✅ Filed 2026-05-19 10:14 CEST** (Kvittens 20260519101426199209225011262906) |
| 2026 | Open — file by Jan 2028 (recommend early Apr 2027 for Swedish FTC) | Open — file by 2 May 2027. See `Next_Year_Checklist.md`. |

## 2025 filing — final positions taken

See `Tax_Filing_Guide_2025.md` for the full post-filing reference. Headlines:

1. **Schablonavdrag base — GROSS rent** (strict reading per Skatteverket; cost +£1,215 vs net-of-commission). Note: 2024 return used net-of-commission — different method, but 2024 not being re-opened.
2. **Vanguard CGT — genomsnittsmetoden per security, original-date FX** — 46 buys across 4 funds, total Box 7.4 = SEK 150,141. Full detail in `K4-vanguard-working-2025.md`.
3. **Mortgage product fee £1,749 — EXCLUDED from Box 8.1** (RÅ 1997 ref. 63). Box 8.1 = SEK 89,876 (interest only).
4. **FTC apportionment** — 9/12 UK 25/26 (finalised same day) + 3/12 UK 24/25 = SEK 5,608.

All four positions disclosed in Övriga upplysningar → skattetillägg shield via öppen redovisning.

## Spreadsheet tabs (`Tax_Return.xlsx`)

| Tab | What it is | Status |
|---|---|---|
| `76A Ingelow Road` | Monthly rental income/expenses (Knight Frank statements) | Authoritative |
| `Santander` | Monthly mortgage table (interest + fees, by UK + Swedish year) | Authoritative |
| `Tax 24-25` | UK 24/25 + Swedish 2024 tax calc | Historical (filed) |
| `Tax 25-26` | UK 25/26 + Swedish 2025 tax calc | **Filed 2026-05-19** |
| `Capital Gains 2025` | Vanguard ISA sale CGT — 4-fund genomsnittsmetoden (rebuilt 19 May 2026) | **Filed 2026-05-19; total SEK 150,141** |
| `HSBC Interest` | Monthly UK savings interest, by tax year | Authoritative |
| `Yield Analysis` | 76a Ingelow yield calc | Reference |
| `Submissions` | Submission refs + key figures cross-reference | **New 19 May 2026** |

All formulas; edit parameters at top of each tax sheet and totals recompute.

## Companion files (this folder)

| File | Purpose |
|---|---|
| `Tax_Filing_Guide_2025.md` | Canonical post-filing reference for both UK & Swedish 2025 returns |
| `Tax_Filing_Guide_2025.docx` | Word version regenerated from .md |
| `Tax_Return.xlsx` | Working spreadsheet (all calc tabs) |
| `K4-vanguard-working-2025.md` | Per-fund Vanguard genomsnittsmetoden detail (46 buys → 4 K4 rows) |
| `Ovriga_upplysningar_2025.md` | Three blocks of Övriga upplysningar (utländska inkomster table + avräkning + öppen redovisning text) |
| `Swedish_Tax_Return_2025_filed.md` | Submission record (kvittens + values) |
| `Swedish_Tax_Return_2025_kvittens.pdf` | Skatteverket receipt |
| `UK_Tax_Return_2025-26_filed.pdf` | HMRC submission |
| `UK_Tax_Return_2025-26_submission_receipt.pdf` | HMRC receipt |
| `Next_Year_Checklist.md` | What to do for the 2026 returns (next year) |
| `vanguard-transactions/` | Vanguard ISA transaction PDFs (3 pages, archived 19 May 2026) |
| `notes.md` | This file — mortgage history + tax-year totals |
