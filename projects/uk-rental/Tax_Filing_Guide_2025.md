# UK & Swedish Tax Returns 2025 — Guide & Working

**Property:** 76a Ingelow Road, London SW8 3PF (UK leasehold flat with share of freehold)
**Filer:** Tristan Morgan, Swedish tax resident since 25 November 2021
**Tax year covered:** UK 2025/26 (6 Apr 2025 – 5 Apr 2026) and Swedish 2025 (calendar year)

---

## Critical findings — what's confirmed and what's ambiguous

### 1. Property classification (Swedish tax) — privatbostadsfastighet

UK leasehold flat with share of freehold is classified as **privatbostadsfastighet** for Swedish tax purposes, not privatbostadsrätt.

**Why**: privatbostadsrätt requires membership in a *privatbostadsföretag* (Swedish ekonomisk förening / AB providing housing to members, or foreign equivalent). A UK freehold management company holding the freehold for *leaseholders* doesn't qualify — leaseholders own a property interest (a long lease), not a membership share whose primary purpose is housing the holders. Skatteverket treats it like an ägarlägenhet equivalent.

**Implication**: schablonavdrag formula = **40,000 SEK + 20% of rental income** (not "40k + actual avgift" which would apply to bostadsrätt). Service charges to the freehold management company are NOT separately deductible.

*Sources*: [Skatteverket — Bostad utomlands](https://www.skatteverket.se/privat/fastigheterochbostad/bostadutomlands.4.233f91f71260075abe8800033670.html), [SKV 398](https://skatteverket.se/download/18.6e8a1495181dad54084157/1708609332774/Deklarera%20bostad%20i%20utlandet.pdf), 2 kap. 2 § and 17 § IL.

### 2. Schablonavdrag base — gross or net of commission?

Skatteverket distinguishes between two arrangements:

> **"When the agency is considered a landlord"** — the agency rents out the home in their own name and handles advertising, agreements, cleaning and tenant access. In this case, you only report what you receive net of the agency's fee.

> **"When the agency only mediates"** — you report the gross rent (including the agency's commission) and cannot deduct the commission separately.

**The legal test** is whether the agency rents *in their own name* — i.e., whose name is on the tenancy agreement with the tenant.

- **Standard UK lettings agency model** (most common): the tenancy is between the owner (you) and the tenant. The agency is named as agent for the landlord, collects rent on the landlord's behalf, deducts commission, pays the net. → strict reading is gross.
- **Sublet / guaranteed-rent model**: the agency leases from the owner, then sublets in own name. → net of commission.

**Indicator** in your data: Knight Frank charges you a separate **Letting Commission** (~£3,145 in 2023, ~£3,430 in 2024) when a new tenancy is signed. That's classic agent behaviour — they wouldn't bill the landlord a letting fee if they were the sublessor.

**Decision for you tomorrow**: confirm whether the tenancy agreement is signed *between you and the tenant* (agent model → gross applies strictly) or *between Knight Frank and the tenant* (sublet → net is correct).

You can defensibly file either way given the operational complexity, but if your tenancy names you as landlord, the strict reading is gross.

**Your 2024 filed return used net-of-commission.** The spreadsheet keeps that as the primary calc (consistent with prior year). A "strict gross" memo block at the bottom shows the differential (~£1,215 more Swedish tax for 2025 if you switch to gross).

*Sources*: [Skatteverket — Hyresinkomster och annan avkastning](https://www4.skatteverket.se/rattsligvagledning/edition/2025.2/326151.html), [Rättslig vägledning förmedling](https://www4.skatteverket.se/rattsligvagledning/edition/2023.14/348280.html).

### 3. Vanguard ISA cost basis — genomsnittsmetoden (resolved)

No rebasing on becoming Swedish-resident. The cost basis = original GBP cost × FX rate at original acquisition date. Since all your contributions were Sept 2020 – Oct 2021 (before your move), I've built the calc using monthly FX estimates.

**New Vanguard CGT figures (using estimated FX rates)**:
- Sum of 14 contributions: £19,508.82
- Cost basis: ~SEK 228,492 (estimate — verify the FX rates in the spreadsheet against Riksbanken's monthly averages)
- Sale proceeds: SEK 386,681
- Gain: ~SEK 158,188
- Swedish tax @ 30%: ~SEK 47,456

This is **SEK 13,310 more tax** (~£1,030) than the Nov 2021 value approach.

**Action**: open the `Capital Gains 2025` tab. Yellow cells (column C) are my estimated monthly FX rates. Pull the actual Riksbanken monthly averages from [riksbank.se → search exchange rates](https://www.riksbank.se/en-gb/statistics/interest-rates-and-exchange-rates/search-annual-and-monthly-average-exchange-rates/) and paste over my estimates. Everything else recalculates.

*Sources*: 44 kap. 14 § IL; [Skatteverket — Utländsk valuta](https://www4.skatteverket.se/rattsligvagledning/edition/2025.1/2818.html).

### 4. Mortgage product fee (£1,749 Feb 2025) — not deductible

HFD case law (**RÅ 1997 ref. 63** in particular) explicitly rejects uppläggningsavgifter (arrangement / product fees) as ränteutgift. Interest is defined in **RÅ 1987 ref. 78** as "förutsebar ersättning för kredit beräknad utifrån kreditbelopp och kredittid" — a fixed up-front fee unrelated to amount × time fails the definition.

**Implication**: do **not** include the £1,749 in Box 8.1. Box 8.1 = mortgage interest only (£6,955 for calendar 2025).

*Sources*: [Skatteverket — Avdrag för ränteutgifter](https://www.skatteverket.se/privat/deklaration/avdragforprivatpersoner/avdragforranteutgifter.106.1b39a64a1919eabb488b87.html), [Rättslig vägledning §2836](https://www4.skatteverket.se/rattsligvagledning/edition/2025.2/2836.html).

### 5. Foreign tax credit timing

Only **finalised** UK tax counts. If UK 25/26 SA hasn't been filed/assessed before the Swedish 2025 return, you can claim:
- Full 3/12 of finalised UK 24/25
- Partial of UK 25/26 only if finalised

Otherwise: file Sweden with partial credit, then file omprövning once UK 25/26 is finalised to claim the rest.

Your apportionment method (3/12 prior + 9/12 current) is defensible. Document it in Övriga upplysningar.

---

## Where everything goes on the Swedish return (INK1)

### Inkomster — Tjänst (Box 1)
- Box 1.1: Salary (~SEK 800,000) — förtryckt

### Inkomster — Kapital (Box 7)

| Box | Item | Source / value |
|---|---|---|
| 7.1 | Schablonintäkter (Swedish ISK / fund deemed income) | Förtryckt — verify |
| **7.2** | **Ränteinkomster — HSBC interest (full year 2025)** | **£211.26 → SEK 2,730** (from `HSBC Interest` tab) |
| **7.3** | **Överskott vid uthyrning av privatbostad** | **From `Tax 25-26` rental calc — see issue #2 above** |
| **7.4** | **Kapitalvinst — Vanguard ISA sale** | **From `Capital Gains 2025` tab (verify FX)** |

### Avdrag — Kapital (Box 8)

| Box | Item | Value |
|---|---|---|
| **8.1** | **Ränteutgifter — UK mortgage interest only** | **£6,955 → ~SEK 89,876** (excl. product fee) |

### Bilagor
- **K4 avsnitt A** — Vanguard ISA sale: list units, försäljningspris (SEK), omkostnadsbelopp (SEK), vinst
- **SKV 2703** — Avräkning utländsk skatt claim

### Övriga upplysningar
- Rental income source, UK tax paid, apportionment method
- FX rates used and source (Riksbanken)
- Note 1.49 % rate ran to 02/03/2025, then 4.38 % fixed to 02/05/2027

---

## Where everything goes on the UK return (SA100 / SA105)

### SA100 (main)
| Box | Item | Value |
|---|---|---|
| TR3 box 2 | Untaxed UK interest (HSBC) | ~£242 |

### SA105 (UK property)
| Box | Item | Value |
|---|---|---|
| 20 | Total rents received (gross) | ~£32,271 |
| 20.2 | Traditional accounting basis | X |
| 25 | Property repairs and maintenance | ~£7,943 |
| 27 | Legal, management and other professional fees | ~£2,859 (Knight Frank) |
| 38 | Adjusted profit for the year | ~£21,469 |
| 40 | Taxable profit for the year | ~£21,469 |
| 44 | Residential property finance costs | ~£7,830 (mortgage interest) |

**UK 25/26 net tax**: ~£214 (after 20% financing-cost credit)

HSBC interest sits under the £1,000 PSA → no additional UK tax. Still report.

---

## FX rates

| Period | Rate | Source |
|---|---|---|
| Riksbanken 2024 annual avg | 13.50453 | 2024 return |
| **Riksbanken 2025 annual avg** | **12.92163** | **For 2025 return — most line items** |
| Riksbanken Sep 2020 – Oct 2021 (monthly) | various (~11.21 – 11.95) | Vanguard cost basis — **estimates in spreadsheet, verify** |
| Riksbanken Jun 2025 monthly | 12.9485 | Vanguard sale |

---

## Tax payable (headline)

### Swedish 2025 (using net-of-commission base for rental, gross genomsnittsmetoden for Vanguard)

| Item | SEK |
|---:|---:|
| Box 7.2 — HSBC interest | 2,730 |
| Box 7.3 — Rental net (schablonavdrag applied) | ~258,094 |
| Box 7.4 — Vanguard CGT (estimated FX) | ~158,188 |
| Subtotal capital income | ~418,952 |
| Less Box 8.1 — Mortgage interest | (89,876) |
| Net capital base | ~329,076 |
| Swedish tax @ 30% | ~98,723 |
| Less UK FTC | (~5,600) |
| **Swedish tax payable 2025** | **~SEK 93,123 (~£7,210)** |

### Differential if switching to gross-rent base for schablonavdrag
- +£4,049 to Box 7.3 → +~£1,215 Swedish tax (~SEK 15,700 more)

### UK 25/26
- Net UK tax: ~£214

---

## Things to confirm before filing tomorrow

1. **Tenancy agreement** — your name or Knight Frank's? Determines whether net-of-commission position is defensible.
2. **Vanguard FX rates** — pull from Riksbanken; paste into yellow cells.
3. **UK 25/26 SA** — filed yet? Affects FTC strategy.
4. **Schablonintäkter 2025** — does förtryckt show this?
5. **Capital losses** — any realised in 2025 to offset the Vanguard gain?

## What we agreed is NOT available

- ROT/RUT (UK property — not in EES)
- Travel to UK to manage property (covered by schablonavdrag)
- Maintenance / repairs as separate deduction (covered by schablonavdrag)
- Service charges to freehold management co (covered by schablonavdrag)
- Mortgage product fee as ränteutgift (case law confirms — not deductible)
- Rebasing Vanguard cost basis to Nov 2021 (no such Swedish provision)

---

## Source citations

- [Skatteverket — Bostad utomlands](https://www.skatteverket.se/privat/fastigheterochbostad/bostadutomlands.4.233f91f71260075abe8800033670.html)
- [SKV 398 — Deklarera bostad i utlandet](https://skatteverket.se/download/18.6e8a1495181dad54084157/1708609332774/Deklarera%20bostad%20i%20utlandet.pdf)
- [Skatteverket — Hyresinkomster och annan avkastning](https://www4.skatteverket.se/rattsligvagledning/edition/2025.2/326151.html)
- [Rättslig vägledning — Förmedlingsföretag](https://www4.skatteverket.se/rattsligvagledning/edition/2023.14/348280.html)
- [Skatteverket — Utländsk valuta](https://www4.skatteverket.se/rattsligvagledning/edition/2025.1/2818.html)
- [Skatteverket — Avdrag för ränteutgifter](https://www.skatteverket.se/privat/deklaration/avdragforprivatpersoner/avdragforranteutgifter.106.1b39a64a1919eabb488b87.html)
- [Rättslig vägledning §2836 — Ränteutgifter](https://www4.skatteverket.se/rattsligvagledning/edition/2025.2/2836.html)
- 2 kap. 2 § och 17 § IL (privatbostadsföretag)
- 44 kap. 14 § IL (omkostnadsbelopp)
- RÅ 1987 ref. 78; RÅ 1997 ref. 44, 63; RÅ 2001 ref. 21 I (definition of interest)
- [2015 UK-Sweden Double Taxation Convention](https://www.gov.uk/government/publications/sweden-tax-treaties/2015-uk-sweden-double-taxation-convention-as-amended-in-2021-in-force)
- [Riksbanken — Search annual and monthly average exchange rates](https://www.riksbank.se/en-gb/statistics/interest-rates-and-exchange-rates/search-annual-and-monthly-average-exchange-rates/)
