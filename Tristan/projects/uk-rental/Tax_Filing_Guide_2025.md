# UK & Swedish Tax Returns 2025 — Filed Record & Position Guide

> **Status:** ✅ Both returns submitted 19 May 2026. This document is the canonical post-filing record and the reference for any future investigation or omprövning.

**Property:** 76a Ingelow Road, London SW8 3PF (UK leasehold flat with share of freehold)
**Filer:** Tristan Patrick Morgan (Swedish PIN 199209225011)
**Swedish tax resident since:** 25 November 2021
**Tax year covered:** UK 2025/26 (6 Apr 2025 – 5 Apr 2026) and Swedish 2025 (calendar year)

---

## Submission references

| Jurisdiction | Form | Date / time | Reference | Receipt PDF |
|---|---|---|---|---|
| **HMRC (UK)** | SA100 + SA105 2025/26 | 2026-05-19 07:38 GMT | **2605755020** (submission ref `TJCNMDAJSEYYVY2C25QSPA5A4RJGUXN4`) | `UK_Tax_Return_2025-26_filed.pdf`, `UK_Tax_Return_2025-26_submission_receipt.pdf` |
| **Skatteverket (Sweden)** | INK1 + K4 avsnitt A 2025 | 2026-05-19 10:14 CEST | Kvittens **20260519101426199209225011262906** | `Swedish_Tax_Return_2025_kvittens.pdf` |

UK 25/26 finalised first → enabled full FTC claim on the Swedish return same day.

---

## Positions taken (with statutory anchors)

### Position #1 — Schablonavdrag on GROSS rent

Skatteverket explicitly: *"Om ett förmedlingsföretag endast förmedlar uthyrningen och tar ut en avgift räknas du som hyresvärd och ska redovisa hela den avtalade hyran som intäkt inklusive avgiften som du betalar till förmedlingsföretaget."* Agent commission absorbed into schablonavdrag, not separately deductible.

The "agency rents in its own name" exception (which would allow net-of-commission) requires the agency to be the lessor on the tenancy. Knight Frank acts as a mediating agent collecting commission from gross rent — Tristan is the lessor → gross applies.

Property is **privatbostadsfastighet** for Swedish purposes (UK leasehold + share of freehold ≠ Swedish bostadsrätt because the UK freehold management company doesn't meet the privatbostadsföretag membership test, 2 kap. 17 § IL). Schablonavdrag formula: **SEK 40,000 + 20% × gross rent**.

- Cost vs net-of-commission position: ~£1,215 more Swedish tax for 2025.
- Sources: [Hyra ut privatbostad](https://skatteverket.se/privat/fastigheterochbostad/inkomsterfranbostad/hyrautprivatbostadbostadsrattsmahusberattsmahusoch-hyresratt.4.233f91f71260075abe8800033479.html), [Rättslig vägledning — förmedling](https://www4.skatteverket.se/rattsligvagledning/edition/2023.14/348280.html), 42 kap. 30 § IL.

### Position #2 — Vanguard ISA: genomsnittsmetoden per security

No rebasing on Swedish residency move. Cost basis = original GBP cost × Riksbanken monthly Medel GBP/SEK at acquisition month. Genomsnittsmetoden applied **per security** (per ISIN), not per account.

**Reality (per K4 working):** 46 buy transactions across **4 funds** (FTSE 100 UT Acc, VUSA, VMID, VERX) — Sep 2020 to 1 Nov 2021, gross £20,282.34. One pre-residency partial sale (15 Nov 2021 FTSE 100, 5.0134 units) — not on Swedish return; reduces pool only. One pre-residency buy+sell pair (FTSE Dev Europe ex-U.K. Acc, Mar 2021) — excluded entirely.

**Submitted (verified FX, finalised 19 May 2026):**

| Beteckning | Antal | Försäljningspris (SEK) | Omkostnadsbelopp (SEK) | Vinst (SEK) |
|---|---:|---:|---:|---:|
| FTSE 100 Index Unit Trust Accumulation | 74 | 173,014 | 99,683 | 73,331 |
| S&P 500 UCITS ETF (VUSA) | 155 | 168,353 | 98,869 | 69,484 |
| FTSE 250 UCITS ETF (VMID) | 45 | 18,869 | 17,495 | 1,374 |
| FTSE Developed Europe ex UK (VERX) | 42 | 19,957 | 14,005 | 5,952 |
| **Summa (K4 → Box 7.4)** | | **380,193** | **230,052** | **150,141** |

Swedish tax @ 30%: **SEK 45,042** on this gain.

- Difference vs Nov 2021-value approach: SEK ~13,310 more tax (~£1,030). The Nov 2021-value approach is not supported by Swedish law.
- Detail: see `K4-vanguard-working-2025.md` and `Tax_Return.xlsx` "Capital Gains 2025" tab.
- Sources: 44 kap. 14 § IL; [Skatteverket — Utländsk valuta](https://www4.skatteverket.se/rattsligvagledning/edition/2025.1/2818.html).

### Position #3 — Mortgage product fee NOT in Box 8.1

**RÅ 1997 ref. 63** explicitly rejects uppläggningsavgift as interest. RÅ 1987 ref. 78 defines interest as *"förutsebar ersättning för kredit beräknad utifrån kreditbelopp och kredittid"* — a fixed up-front fee fails this test.

Box 8.1 = mortgage interest only (**£6,955 → SEK 89,876** for calendar 2025). The **£1,749 product fee** is excluded.

- Cost vs claiming the fee: ~£525 more Swedish tax for 2025.
- Sources: [Avdrag för ränteutgifter](https://www.skatteverket.se/privat/deklaration/avdragforprivatpersoner/avdragforranteutgifter.106.1b39a64a1919eabb488b87.html), [Rättslig vägledning §2836](https://www4.skatteverket.se/rattsligvagledning/edition/2025.2/2836.html).

### Position #4 — Foreign tax credit apportionment

UK tax year runs 6 Apr – 5 Apr. Swedish tax year is calendar year. FTC claims only **finalised** UK tax. Apportionment: **9/12 of UK 25/26 + 3/12 of UK 24/25** for calendar 2025.

- UK 25/26 finalised 2026-05-19 07:38 (HMRC 2605755020): net tax £214 → 9/12 × £214 = £161
- UK 24/25 finalised previously: net tax £1,092 → 3/12 × £1,092 = £273
- Total apportioned UK tax: £434 × Riksbanken 2025 årsmedel **12.92163** = **SEK 5,608**

---

## What was submitted

### Swedish INK1 — Inkomstdeklaration 1

| Box | Description | SEK |
|---|---|---:|
| 1.1 | Lön, förmåner (förtryckt) | 705,810 |
| 5.1 | Småhus/ägarlägenhet 0,75 % (Swedish property — owned 1 Jan 2025; sold 2026) | 671,600 |
| 7.1 | Schablonintäkter (förtryckt) | 18,360 |
| 7.2 | Ränteinkomster (322 förtryckt + 2,730 HSBC UK) | 3,052 |
| 7.3 | Överskott vid uthyrning av privatbostad (76a Ingelow) | 310,434 |
| 7.4 | Vinst fondandelar (Vanguard ISA, K4) | 150,141 |
| 8.1 | Ränteutgifter (Santander UK mortgage interest only) | 89,876 |

**Bilagor:** K4 avsnitt A (4 rows — see Position #2 above).

**Övriga upplysningar — utländsk inkomst (structured table):**

| Typ | Land | SEK |
|---|---|---:|
| Kapital | Storbritannien | 310,434 |
| Kapital | Storbritannien | 2,730 |
| Kapital | Storbritannien | 150,141 |

**Avräkning utländsk skatt:** SEK 5,608

**Övrigt (free-text, 839 chars — full öppen redovisning):**

> Hyresinkomst 76a Ingelow Road, London (privatbostadsfastighet; leasehold + share of freehold, ej privatbostadsföretag enl. 2 kap. 17 § IL) via förmedlare Knight Frank: schablonavdrag 40 000 + 20% × bruttohyra GBP 32 271 enligt strikt tolkning. Förmedlingsavgift GBP 2 859 ej särskilt avdrag (ingår i schablonavdraget). Box 8.1 endast räntor Santander UK GBP 6 955; uppläggningsavgift GBP 1 749 ej avdragen (RÅ 1997 ref. 63). Box 7.4 Vanguard ISA (ISA utan svensk skattefördel): 4 fonder (FTSE100 UT, VUSA, VMID, VERX) på K4 avsnitt A; genomsnittsmetoden per värdepapper (44 kap. 14 § IL); förvärv 2020–2021 omräknade med Riksbankens månadsmedel; försäljning juni 2025 vid 12,9485. Ingen omvärdering vid inflyttning 25 nov 2021. Avräkning SEK 5 608: 9/12 UK 25/26 (GBP 214) + 3/12 UK 24/25 (GBP 1 092); FX Riksbanken årsmedel 2025 12,92163.

This open-disclosure paragraph triggers **öppen redovisning** protection — Skatteverket can reassess on a rättsfråga basis (back tax + interest) but cannot apply skattetillägg (40% penalty).

### UK SA100 + SA105

| Box | Item | Value |
|---|---|---:|
| SA100 TR3 box 2 | Untaxed UK interest (HSBC) | £242 |
| SA105 box 20 | Total rents received (gross) | £32,271 |
| SA105 box 20.2 | Traditional accounting basis | ✓ |
| SA105 box 25 | Property repairs and maintenance | £7,943 |
| SA105 box 27 | Legal, management and other professional fees | £2,859 (Knight Frank) |
| SA105 box 38 | Adjusted profit for the year | £21,469 |
| SA105 box 40 | Taxable profit for the year | £21,469 |
| SA105 box 44 | Residential property finance costs | £7,830 (mortgage interest) |
| SA110 box 1 | **Total tax due** | **£213.80** |

HSBC interest sits under £1,000 PSA → no additional UK tax. Still reported.

---

## FX rates used (all Riksbanken)

| Period | Rate (SEK/GBP) | Use | Verified |
|---|---:|---|---|
| Sep 2020 | 11.45956 | Vanguard buys (Sep 2020) | ✓ |
| Oct 2020 | 11.47127 | (none) | ✓ |
| Nov 2020 | 11.41785 | Vanguard buys (Nov 2020) | ✓ |
| Dec 2020 | 11.23895 | Vanguard buys (Dec 2020) | ✓ |
| Jan 2021 | 11.31239 | Vanguard buys (Jan 2021) | ✓ |
| Feb 2021 | 11.55250 | Vanguard buys (Feb 2021) | ✓ |
| Mar 2021 | 11.83967 | Vanguard buys (Mar 2021) | ✓ |
| Apr 2021 | 11.74595 | Vanguard buys (Apr 2021) | ✓ |
| May 2021 | 11.75710 | Vanguard buys (May 2021) | ✓ |
| Jun 2021 | 11.77512 | Vanguard buys (Jun 2021) | ✓ |
| Jul 2021 | 11.90743 | Vanguard buys (Jul 2021) | ✓ |
| Aug 2021 | 11.97744 | Vanguard buys (Aug 2021) | ✓ |
| Sep 2021 | 11.87028 | Vanguard buys (Sep 2021) | ✓ |
| Oct 2021 | 11.86876 | Vanguard buys (Oct 2021) | ✓ |
| Nov 2021 | 11.84728 | Vanguard buy (1 Nov 2021) | ✓ |
| **Jun 2025** | **12.94850** | **Vanguard sale (all 4 funds, Jun 2025)** | ✓ |
| **2025 annual avg** | **12.92163** | **Recurring items (rental, interest, FTC)** | ✓ |
| 2024 annual avg | 13.50453 | (2024 return — context) | ✓ |

Source: [Riksbanken — Search annual and monthly average exchange rates](https://www.riksbank.se/en-gb/statistics/interest-rates-and-exchange-rates/search-annual-and-monthly-average-exchange-rates/).

---

## Skatteuträkning (preliminär, pre-FTC)

From Skatteverket's preview at submission:

| Item | SEK |
|---|---:|
| Fastställd förvärvsinkomst | 705,800 |
| Less grundavdrag | -17,300 |
| Beskattningsbar förvärvsinkomst | 688,500 |
| Ränteinkomster m.m. (7.1+7.2+7.3) | 331,846 |
| Less ränteutgifter (8.1) | -89,876 |
| Less avdrag för skattefritt sparande (ISK) | -4,440 |
| Kapitalvinst (7.4) | 150,141 |
| **Överskott av kapital** | **387,671** |
| Kommunal inkomstskatt @ 31.99% | 220,251 |
| Statlig skatt förvärvsinkomst @ 20% over skiktgräns 625,800 | 12,540 |
| Statlig skatt kapital @ 30% | 116,301 |
| Fastighetsavgift (Swedish property 671,600 × 0.75%) | 5,037 |
| Begravningsavgift @ 0.293% | 2,017 |
| Public service-avgift | 1,249 |
| Jobbskatteavdrag | -46,682 |
| Skattereduktion förvärvsinkomst | -1,500 |
| Skattereduktion a-kassa @ 25% | -470 |
| **Summa skatt** | **308,743** |
| Less preliminärskatt (avdragen) | -233,025 |
| **Belopp att betala (preliminär, exkl FTC)** | **75,718** |
| Less FTC (applied after submission) | -5,608 |
| **Expected actual kvarskatt** | **~70,110** |

Inbetalning till **Skatteverket bg 5050-1055**, OCR **1992092250114**.

---

## Differential vs less conservative positions

If different positions had been taken, Swedish tax would have been lower:

| Position | Conservative (used) | Less conservative | Tax saved |
|---|---|---|---:|
| Schablonavdrag base | Gross rent | Net-of-commission | ~£1,215 |
| Vanguard cost basis | Original-date FX | Nov 2021 market value | ~£1,030 |
| Box 8.1 product fee | Excluded | Included as interest | ~£525 |
| **Total potential saving** | | | **~£2,770** |

These positions were taken with statutory anchors and disclosed in Övriga upplysningar — protected from skattetillägg.

---

## What is NOT available (confirmed, do not retry next year)

- ROT/RUT (UK property — not in EES)
- Travel to UK to manage property (covered by schablonavdrag)
- Maintenance / repairs as separate deduction (covered by schablonavdrag)
- Agent commission as separate deduction (covered by schablonavdrag)
- Service charges to UK freehold management co (covered by schablonavdrag)
- Mortgage product/arrangement fees as ränteutgift (RÅ 1997 ref. 63)
- Rebasing cost basis on becoming Swedish resident (no Swedish provision)

---

## Companion files (this folder)

| File | Purpose |
|---|---|
| `Tax_Filing_Guide_2025.md` | This file — canonical post-filing reference |
| `Tax_Filing_Guide_2025.docx` | Word version (regenerated from .md) |
| `Tax_Return.xlsx` | Working spreadsheet (all calc tabs) |
| `K4-vanguard-working-2025.md` | Per-fund Vanguard genomsnittsmetoden detail |
| `Ovriga_upplysningar_2025.md` | Three blocks for Skatteverket free-text page |
| `Swedish_Tax_Return_2025_filed.md` | Submission record (kvittens + values) |
| `Swedish_Tax_Return_2025_kvittens.pdf` | Skatteverket receipt |
| `UK_Tax_Return_2025-26_filed.pdf` | HMRC submission |
| `UK_Tax_Return_2025-26_submission_receipt.pdf` | HMRC receipt |
| `Next_Year_Checklist.md` | What to do for the 2026 returns |
| `notes.md` | Mortgage history + tax-year totals (rental property) |

---

## Source citations (statutory + Skatteverket)

- 2 kap. 2 § och 17 § IL (privatbostadsföretag definition)
- 42 kap. 30 § IL (schablonavdrag privatbostad)
- 44 kap. 14 § IL (omkostnadsbelopp, genomsnittsmetoden)
- RÅ 1987 ref. 78; RÅ 1997 ref. 44, 63; RÅ 2001 ref. 21 I (definition of interest)
- [2015 UK-Sweden Double Taxation Convention](https://www.gov.uk/government/publications/sweden-tax-treaties/2015-uk-sweden-double-taxation-convention-as-amended-in-2021-in-force) (Art. 6 immovable property; Art. 13 capital gains; Art. 22 elimination of double taxation)
- [Skatteverket — Bostad utomlands](https://www.skatteverket.se/privat/fastigheterochbostad/bostadutomlands.4.233f91f71260075abe8800033670.html)
- [SKV 398 — Deklarera bostad i utlandet](https://skatteverket.se/download/18.6e8a1495181dad54084157/1708609332774/Deklarera%20bostad%20i%20utlandet.pdf)
- [Rättslig vägledning — Hyresinkomster och annan avkastning](https://www4.skatteverket.se/rattsligvagledning/edition/2025.2/326151.html)
- [Rättslig vägledning — Förmedlingsföretag](https://www4.skatteverket.se/rattsligvagledning/edition/2023.14/348280.html)
- [Skatteverket — Utländsk valuta](https://www4.skatteverket.se/rattsligvagledning/edition/2025.1/2818.html)
- [Skatteverket — Avdrag för ränteutgifter](https://www.skatteverket.se/privat/deklaration/avdragforprivatpersoner/avdragforranteutgifter.106.1b39a64a1919eabb488b87.html)
- [Rättslig vägledning §2836 — Ränteutgifter](https://www4.skatteverket.se/rattsligvagledning/edition/2025.2/2836.html)
- [Riksbanken — Search annual and monthly average exchange rates](https://www.riksbank.se/en-gb/statistics/interest-rates-and-exchange-rates/search-annual-and-monthly-average-exchange-rates/)
