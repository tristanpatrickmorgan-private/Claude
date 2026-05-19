# Next Year — Tax Returns 2026 Checklist

What needs to happen for the **UK 2026/27** and **Swedish 2026** returns (filing in 2027). Pre-populated with everything known today (19 May 2026).

## Background — what carries forward

- **Swedish tax resident** since 25 Nov 2021 (unchanged).
- **UK rental property** at 76a Ingelow Road, London SW8 3PF — continues as before (assume still let unless told otherwise).
- **Vanguard ISA** — empty as of 19 Jun 2025 (all 4 funds sold). **No K4 needed in 2026.**
- **Mortgage** (Santander 0915/862/044470945) — interest-only until 02 May 2027 at 4.38%. Box 8.1 will be ~£7,830 for full UK 25/26, then drops to whatever the new product gives from May 2027.

## Critical new items for 2026 return

### 1. Swedish property sale (2026 disposal)

Tristan owned a Swedish property (taxeringsvärde SEK 671,600) on 1 Jan 2025 and sold it during 2026.

**To gather before filing 2026 return:**
- [ ] Sale contract date and price (SEK)
- [ ] Purchase price (omkostnadsbelopp) — original GBP/SEK cost when bought
- [ ] All förbättringsutgifter (improvements) with dated receipts — capital improvements only, repairs not deductible
- [ ] Legal/agent fees on sale (deductible from sale proceeds)
- [ ] Was it a privatbostadsfastighet (small house / ägarlägenhet) or bostadsrätt? Determines which form:
  - **K5** if privatbostadsfastighet (small house / ägarlägenhet)
  - **K6** if bostadsrätt (apartment in housing co-op)
- [ ] Confirm if owned on 1 Jan 2026 → **second year of fastighetsavgift** on 2026 return (~SEK 5,037 again unless taxeringsvärde changed)

**Swedish CGT rate on private home sale:** 22% (i.e. 22/30 of the gain taxed at 30% = effective 22%). Possible uppskov if reinvested in replacement home (but only within EES, not UK).

### 2. UK tax year alignment

- UK 25/26 finalised 2026-05-19 → 3/12 of it apportions into Swedish 2026 calc as FTC (SEK ~£54 × 12.92 ≈ SEK 700).
- UK 26/27 closes 5 Apr 2027 — will likely NOT be filed by Swedish deadline (2 May 2027). Either:
  - File UK 26/27 SA early (April 2027) to enable full FTC, OR
  - Claim 3/12 of UK 25/26 only + omprövning later for 9/12 of UK 26/27 once finalised.

## Recurring items (carried over from 2025 method)

| Item | 2025 method (confirmed working) | 2026 action |
|---|---|---|
| Rental Box 7.3 | Schablonavdrag on GROSS rent (40,000 + 20%) | Same method, refresh GBP figures |
| Box 8.1 | UK mortgage interest only (no product fee) | Same; pull 2026 Santander statement |
| HSBC interest Box 7.2 | Calendar-year total | Pull 12-month statement Jan–Dec 2026 |
| Schablonintäkter Box 7.1 | Förtryckt from ISK | Verify förtryckt amount |
| Övriga upplysningar | Three-block disclosure (utländsk inkomst rows + avräkning + öppen redovisning text) | Reuse template from `Ovriga_upplysningar_2025.md`; update numbers |

## Pre-filing checklist (use Mar–Apr 2027)

### UK side first
1. [ ] Get Knight Frank annual statement for UK 26/27
2. [ ] Get Santander annual mortgage interest statement for UK 26/27
3. [ ] Pull HSBC interest for UK 26/27
4. [ ] Update `Tax_Return.xlsx` → "Tax 26-27" tab (clone "Tax 25-26" structure)
5. [ ] File UK SA100 + SA105 for 26/27 early to enable Swedish FTC

### Swedish side
6. [ ] Knight Frank calendar-2026 rental total → Box 7.3 (gross × FX)
7. [ ] Santander calendar-2026 mortgage interest → Box 8.1
8. [ ] HSBC calendar-2026 interest → Box 7.2
9. [ ] Swedish property sale → K5/K6 (TBD which)
10. [ ] FTC apportionment (SKV 2703 / e-tjänst Avräkning utländsk skatt) — 9/12 UK 26/27 + 3/12 UK 25/26
11. [ ] Öppen redovisning text in Övrigt (adapt 2025 template; mention 2026 sale)

## Files to prepare (parallel to 2025 set)

| 2025 file | 2026 equivalent |
|---|---|
| `Tax_Filing_Guide_2025.md` | `Tax_Filing_Guide_2026.md` (clone, update) |
| `K4-vanguard-working-2025.md` | N/A — ISA empty |
| `Ovriga_upplysningar_2025.md` | `Ovriga_upplysningar_2026.md` |
| `Swedish_Tax_Return_2025_filed.md` | `Swedish_Tax_Return_2026_filed.md` (after submission) |
| (none) | `K5_or_K6_Swedish_property_sale_2026.md` (new — sale calc) |

## Deadlines

- **UK SA 26/27:** online filing 31 Jan 2028 (paper 31 Oct 2027). Earlier filing recommended to enable Swedish FTC.
- **Swedish INK1 2026:** 2 May 2027 (digital deadline). Paper deadline late May.
- **Swedish skatt to pay:** 12 Nov 2027 (assessment usually mid-2027; pay before interest accrues from 1 May 2027 if amount >SEK 30,000).

## Quick numbers to expect (back-of-envelope)

Assuming everything stable except removal of Vanguard CGT and addition of Swedish property sale:

- Box 7.3 rental: similar to 2025, ~SEK 310k
- Box 7.4: 0 (no securities sales expected)
- K5/K6 gain: TBD — depends on sale price vs cost basis × 22/30 (effective 22%)
- Box 8.1: ~SEK 89k (£6,955-ish at 13ish FX)
- Box 5.1 fastighetsavgift: SEK 5,037 if still owned 1 Jan 2026 (one final year)

## Investigation defence (if Skatteverket queries the 2025 return)

If Skatteverket challenges any 2025 position post-filing, the öppen redovisning paragraph in Övriga upplysningar protects against skattetillägg. They can only re-assess as rättsfråga → back tax + interest only, no 40% penalty.

Files to point to in any query:
- `Tax_Filing_Guide_2025.md` — positions and statutory anchors
- `K4-vanguard-working-2025.md` — transaction-level Vanguard detail
- `Tax_Return.xlsx` "Capital Gains 2025" tab — formula-driven calc
- `Swedish_Tax_Return_2025_kvittens.pdf` — proof of timely submission with full disclosure
- `UK_Tax_Return_2025-26_filed.pdf` — proof of finalised UK tax for FTC
- Vanguard transaction PDFs (3 files — should be archived from this session)
