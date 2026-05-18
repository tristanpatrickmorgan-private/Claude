# UK & Swedish Tax Returns 2025 — Guide & Working

**Property:** 76a Ingelow Road, London SW8 3PF
**Filer:** Tristan Morgan, Swedish tax resident since 25 November 2021
**Tax year covered:** UK 2025/26 (6 Apr 2025 – 5 Apr 2026) and Swedish 2025 (calendar year)

---

## Critical findings from research before you file

Three items need a decision or verification **before** filing the Swedish return tomorrow.

### 1. Schablonavdrag base — gross rent vs. net-of-commission

Per Skatteverket's rättslig vägledning (Inkomstskattelagen 42 kap. 30–31 §§) and SKV 398 "Hur man deklarerar sin bostad i utlandet", a privately owned dwelling let out — even abroad — is a **privatbostad**. Allowed deductions:

- SEK 40,000 schablonavdrag per dwelling, per year
- **PLUS 20% of the rent** (because the UK flat is freehold-equivalent, i.e. privatbostadsfastighet)

The 20% is applied to **gross rent**, not rent net of agent commission. **Actual costs (agent commission, maintenance, insurance) are not separately deductible** under schablonavdrag.

**Implication for you**

Your 2024 filed return used £24,571 (rent net of Knight Frank commission) as the base for the 20% deduction, giving Box 7.3 = SEK 225,457.

The strict reading would use the gross rent (£29,406 in 2024) as the base, which would give a higher Box 7.3 (~SEK 277,000).

**Action**: confirm with your accountant which interpretation they used. Some practitioners treat agent-retained commission as "not received" by the landlord (so the base is the net the landlord actually got). The strict Inkomstskattelagen reading is gross.

If the strict reading applies, your filed 2024 return understated income by ~£4,000 of base → ~£235 of additional Swedish tax. The same issue would apply for 2025.

### 2. Vanguard ISA — Genomsnittsmetoden (no rebasing on Swedish move)

Skatteverket does **not** rebase your cost basis when you become Swedish-resident. The cost basis for shares/funds acquired before moving is **the original acquisition cost in SEK at the original acquisition-date FX rate** — even if that's pre-2021.

**Implication for you**

My current calc uses the 25 Nov 2021 value (£23,031.31) as cost basis, which is **wrong per strict Swedish law**. You need the genomsnittsmetoden (weighted-average) cost basis across all your actual Vanguard contributions, each converted at its acquisition-date FX rate.

The Vanguard statement shows you started in Sept 2020 and contributed ~£19,500 over time. If most was before Nov 2021 at GBP/SEK rates around 11.50–12.00, the SEK cost basis would be lower than my Nov 2021 figure → the gain would be **higher** → more Swedish tax.

**Action**: pull the Vanguard transaction history (date + GBP amount for each contribution). I can then build a proper genomsnittsmetoden calc. Without it, my CGT figure is a rough approximation — for filing tomorrow, mark it as provisional and amend later if needed.

### 3. Mortgage product fee deductibility (£1,749 Feb 2025)

Skatteverket has no published guidance specifically on UK mortgage arrangement fees:
- If treated as compensation for credit (interest-equivalent) → deductible in Box 8.1
- If treated as pure administrative fee → not deductible

**Conservative position**: exclude (deduct only £6,955 mortgage interest in Box 8.1)
**Aggressive position**: include with a note in Övriga upplysningar explaining you treat the fee as economically equivalent to interest

Differential: 30% × £1,749 = ~£525 of Swedish tax. Worth a brief call to your accountant.

### 4. Foreign tax credit timing (avräkning utländsk skatt)

Skatteverket only credits **finalised** UK tax, not provisional. UK 25/26 SA must be filed and assessed before you can claim it as a credit against Swedish 2025 tax.

**Implication for you**

If you file the Swedish 2025 return **before** the UK 25/26 SA is finalised, you can only claim FTC for the 3/12 portion of finalised UK 24/25 (filed) + any other already-finalised UK tax. The 9/12 portion of UK 25/26 has to wait.

Options:
- File Sweden first, claim partial FTC, then file omprövning (amended return) once UK 25/26 is finalised to claim the rest
- File UK 25/26 first, then Sweden with full FTC

Your apportionment method (3/12 prior + 9/12 current) is defensible — Skatteverket doesn't publish a fixed formula but accepts "reasonable and consistent" allocation. Document the working in Övriga upplysningar.

---

## Where everything goes on the Swedish return (INK1)

### Inkomster — Tjänst (Box 1)
- Box 1.1: Salary (~SEK 800,000) — already on the förtryckt return

### Inkomster — Kapital (Box 7)
| Box | Item | Source |
|---|---|---|
| 7.1 | Schablonintäkter (deemed income from Swedish funds/ISK) | Förtryckt — verify |
| **7.2** | **Ränteinkomster — HSBC interest** | **£211.26 → ~SEK 2,730** (from `HSBC Interest` tab) |
| **7.3** | **Överskott vid uthyrning av privatbostad** | **From `Tax 25-26` rental calc — see critical issue #1** |
| **7.4** | **Kapitalvinst — Vanguard ISA sale** | **From `Capital Gains 2025` tab — see critical issue #2** |

### Avdrag — Kapital (Box 8)
| Box | Item | Source |
|---|---|---|
| **8.1** | **Ränteutgifter — UK mortgage interest** | **£6,955 → ~SEK 89,876** (see critical issue #3 re: fees) |

### Bilagor (attachments)
- **K4 avsnitt A** — required for the Vanguard ISA sale. List: antal/units, försäljningspris, omkostnadsbelopp, vinst
- **SKV 2703** — claim form for foreign tax credit (avräkning utländsk skatt)

### Övriga upplysningar (free text)
- State: "Avräkning utländsk skatt", with calculation of apportioned UK tax
- Note treatment of any uncertain items (e.g. product fee in Box 8.1 if claiming)
- State FX rates used and source (Riksbanken annual averages)
- Note rental income source and that UK tax is paid on it (DTA Art. 6 / Art. 24)

---

## Where everything goes on the UK return (SA100 / SA105)

### SA100 (main return)
| Box | Item | Value |
|---|---|---|
| TR3 box 2 | Untaxed UK interest (HSBC) | ~£242 (calendar 25-26 UK tax year credits) |

### SA105 (UK property)
| Box | Item | Value |
|---|---|---|
| 20 | Total rents received | ~£32,271 (gross, UK 25/26) |
| 20.2 | Traditional accounting basis | X |
| 25 | Property repairs and maintenance | ~£7,943 |
| 27 | Legal, management and other professional fees | ~£2,859 (Knight Frank) |
| 38 | Adjusted profit for the year | (auto: 20 − 25 − 27) ~£21,469 |
| 40 | Taxable profit for the year | ~£21,469 |
| 44 | Residential property finance costs | ~£7,830 (mortgage interest) |

UK tax outcome: rental profit £21,469 − Personal Allowance £12,570 = £8,899 × 20% = £1,780 basic rate tax. Less 20% × £7,830 financing credit = £1,566. **Net UK tax = ~£214.**

HSBC interest (~£242) is below the £1,000 Personal Savings Allowance, so no additional UK tax. Still report it.

---

## FX rates used

| Period | Rate (SEK per GBP) | Source |
|---|---|---|
| Riksbanken 2024 annual avg | 13.50453 | Used for Swedish 2024 return |
| **Riksbanken 2025 annual avg** | **12.92163** | **For Swedish 2025 return (most items)** |
| Riksbanken Nov 2021 monthly avg | 11.84728 | Vanguard cost basis (approximate — see issue #2) |
| Riksbanken Jun 2025 monthly avg | 12.9485 | Vanguard sale price |

Per Skatteverket guidance, the annual average is accepted for recurring income (rent, interest). Specific transactions (CGT cost/proceeds) use date-of-transaction or monthly-average rates.

---

## Tax payable (estimated)

### Headline numbers for Swedish 2025

Using net-of-commission base (per your filed 2024 method):

| Item | GBP | SEK |
|---|---:|---:|
| Box 7.2 — HSBC interest | 211 | 2,730 |
| Box 7.3 — Rental (after schablonavdrag) | 19,975 | 258,094 |
| Box 7.4 — Vanguard CGT | 6,832 (approx) | ~113,822 (approx) |
| Total capital income | | ~374,646 |
| Box 8.1 — Mortgage interest (excl. product fee) | (6,955) | (89,876) |
| **Net capital base** | | **~284,770** |
| Swedish tax @ 30% | | ~85,431 |
| Less: UK FTC (apportioned) | | ~5,600 |
| **Swedish tax payable 2025** | **~£6,180** | **~SEK 79,831** |

Using gross-rent base (strict reading):

Add ~SEK 27,580 to Box 7.3, → +30% × SEK 27,580 = ~SEK 8,274 more Swedish tax = **~SEK 88,105 total**.

### UK 25/26

| Item | GBP |
|---|---:|
| Property profit | 21,469 |
| Tax before credit | 1,780 |
| Less financing credit | (1,566) |
| **Net UK tax** | **~£214** |

---

## Things to confirm with your accountant or research further

1. **Schablonavdrag base** — gross rent or net of commission?
2. **Vanguard cost basis** — pull contribution history for genomsnittsmetoden
3. **Mortgage product fee £1,749** — Box 8.1 or not?
4. **UK 25/26 SA timing** — file UK first to enable full Swedish FTC?
5. **Schablonintäkter** for 2025 — does förtryckt return show this for your Swedish funds/ISK accounts?
6. **Tjänstepension** — do you have an occupational pension at work? If NOT, private pension contributions up to 35% salary deductible.
7. **Capital losses elsewhere** — any underwater holdings to realise in 2025 to offset gains?

---

## Things that are confirmed NOT available (so don't waste time on)

- ROT/RUT for UK property — not in EES, not eligible
- Travel to UK for property management — swallowed by schablonavdrag, not separately deductible
- Maintenance/repairs as separate deduction — covered by schablonavdrag
- Agent commission as separate deduction — covered by schablonavdrag
- "Rebasing" Vanguard cost basis to Nov 2021 — not a Swedish tax concept

---

## File structure for future years

In this repo: `projects/uk-rental/`

| File | What it does |
|---|---|
| `notes.md` | This file's compact version — overview + tax-year totals |
| `Tax_Return.xlsx` | Live spreadsheet: 76A Ingelow Road, Santander, Tax 24-25, Tax 25-26, Capital Gains 2025, HSBC Interest |
| `mortgage-monthly.xlsx` | Mortgage transactions month-by-month |
| `Tax_Filing_Guide_2025.docx` | This guide |
| `build_*.py` | Scripts that build the tabs from raw data — re-run them next year with new data |

For 2026 (filing in 2027):
1. Update `76A Ingelow Road` sheet with each Knight Frank statement
2. Update `Santander` sheet with each month's interest (or use the Online Banking PDFs)
3. Update `HSBC Interest` sheet with each month's interest credit
4. Replicate `Tax 25-26` as `Tax 26-27` — change the parameters at top, formulas auto-update
5. Update FX rates to 2026 Riksbanken averages

---

## Sources

- [Skatteverket — Bostad utomlands](https://www.skatteverket.se/privat/fastigheterochbostad/bostadutomlands.4.233f91f71260075abe8800033670.html)
- [SKV 398 — Hur man deklarerar sin bostad i utlandet](https://skatteverket.se/download/18.6e8a1495181dad54084157/1708609332774/Deklarera%20bostad%20i%20utlandet.pdf)
- [Rättslig vägledning 2025.2 — Privatbostadsfastighet](https://www4.skatteverket.se/rattsligvagledning/edition/2025.2/1944.html)
- [Skatteverket — Deklarera inkomster från utlandet](https://skatteverket.se/privat/deklaration/deklarerainkomsterfranutlandet.4.71004e4c133e23bf6db8000109217.html)
- [Skatteverket — Valutakurser till deklarationen (Riksbanken)](https://www.riksbank.se/sv/statistik/rantor-och-valutakurser/valutakurser-till-deklarationen/)
- [Avdragslexikon — Utländsk bostad](https://www.skatteverket.se/privat/skatter/arbeteochinkomst/avdragforprivatpersoner/u.4.5fc8c94513259a4ba1d800042761.html)
- [2015 UK-Sweden Double Taxation Convention (as amended 2021)](https://www.gov.uk/government/publications/sweden-tax-treaties/2015-uk-sweden-double-taxation-convention-as-amended-in-2021-in-force)
- [Rättslig vägledning §2818 — Beskattning av tillgång i utländsk valuta](https://www4.skatteverket.se/rattsligvagledning/edition/2023.15/2818.html)
- [K4 hjälptext](https://www8.skatteverket.se/hjalptexter/EfInk1k4_aktie.html)
