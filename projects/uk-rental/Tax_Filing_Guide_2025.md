# UK & Swedish Tax Returns 2025 — Guide & Working

**Property:** 76a Ingelow Road, London SW8 3PF (UK leasehold flat with share of freehold)
**Filer:** Tristan Morgan, Swedish tax resident since 25 November 2021
**Tax year covered:** UK 2025/26 (6 Apr 2025 – 5 Apr 2026) and Swedish 2025 (calendar year)

**Positions taken on the Swedish return (decided 19 May 2026):**
- **Schablonavdrag base: GROSS rent** (strict reading per Skatteverket — 20% applies to gross, agent commission absorbed into schablonavdrag)
- **Product fee NOT in Box 8.1** (RÅ 1997 ref. 63 — arrangement fees are not interest)
- **Vanguard cost basis: genomsnittsmetoden** with original-date FX (no rebasing at residency move)

---

## Position #1 — Schablonavdrag on GROSS rent

Skatteverket explicitly: *"Om ett förmedlingsföretag endast förmedlar uthyrningen och tar ut en avgift räknas du som hyresvärd och ska redovisa hela den avtalade hyran som intäkt inklusive avgiften som du betalar till förmedlingsföretaget."* You can't deduct the agent commission on top of the schablonavdrag — it's absorbed into it.

The "agency rents in its own name" exception (which would allow net-of-commission) requires the agency to be the lessor on the tenancy. With Knight Frank as a mediating agent collecting commission from your gross rent, you're the lessor — so gross applies.

Property is **privatbostadsfastighet** for Swedish purposes (leasehold + share of freehold ≠ Swedish bostadsrätt because the UK freehold management company doesn't meet the privatbostadsföretag membership test). Schablonavdrag formula = **40,000 SEK + 20% of gross rent**.

*Cost vs net-of-commission position: ~£1,215 more Swedish tax for 2025.*

*Sources*: [Hyra ut privatbostad](https://skatteverket.se/privat/fastigheterochbostad/inkomsterfranbostad/hyrautprivatbostadbostadsrattsmahusberattsmahusochhyresratt.4.233f91f71260075abe8800033479.html), [Rättslig vägledning förmedling](https://www4.skatteverket.se/rattsligvagledning/edition/2023.14/348280.html).

## Position #2 — Vanguard ISA: genomsnittsmetoden

No rebasing on Swedish residency move. Cost basis = original GBP cost × FX rate at original acquisition date.

**Reality (per K4 working, 19 May 2026):** 46 buy transactions across 4 funds (FTSE 100 UT Acc, VUSA, VMID, VERX) — Sep 2020 to 1 Nov 2021, gross £20,282.34. One pre-residency partial sale (15 Nov 2021 FTSE 100, 5.0134 units) — not on Swedish return; reduces pool only. Each buy converted at Riksbanken monthly Medel GBP/SEK.

**Headline (verified FX):**
- Cost basis (2025 Swedish-relevant): SEK 230,052
- Sale proceeds (Jun 2025, FX 12.9485): SEK 380,193
- **Gain: SEK 150,142**
- Swedish tax @ 30%: **~SEK 45,043**

See `K4-vanguard-working-2025.md` for full per-fund working and the 4 K4 avsnitt A rows.

*Difference vs Nov 2021-value approach: SEK 13,310 more tax (~£1,030). The Nov 2021-value approach is not supported by Swedish law.*

*Sources*: 44 kap. 14 § IL; [Skatteverket — Utländsk valuta](https://www4.skatteverket.se/rattsligvagledning/edition/2025.1/2818.html).

## Position #3 — Mortgage product fee NOT deductible

**RÅ 1997 ref. 63** explicitly rejects uppläggningsavgift as interest. RÅ 1987 ref. 78 defines interest as "förutsebar ersättning för kredit beräknad utifrån kreditbelopp och kredittid" — a fixed up-front fee fails this test.

Box 8.1 = **mortgage interest only** (£6,955 for calendar 2025). The £1,749 product fee is excluded.

*Cost vs claiming the fee: ~£525 more Swedish tax for 2025.*

*Sources*: [Avdrag för ränteutgifter](https://www.skatteverket.se/privat/deklaration/avdragforprivatpersoner/avdragforranteutgifter.106.1b39a64a1919eabb488b87.html), [Rättslig vägledning §2836](https://www4.skatteverket.se/rattsligvagledning/edition/2025.2/2836.html).

## Position #4 — Foreign tax credit timing

Only **finalised** UK tax counts. Apportionment 3/12 prior + 9/12 current — defensible practitioner method, document in Övriga upplysningar.

If UK 25/26 SA isn't filed/assessed yet, you can only claim finalised portion now; balance via omprövning later.

---

## Where everything goes on the Swedish return (INK1)

### Inkomster — Tjänst (Box 1)
- Box 1.1: Salary (~SEK 800,000) — förtryckt

### Inkomster — Kapital (Box 7)

| Box | Item | Source / value |
|---|---|---|
| 7.1 | Schablonintäkter (Swedish ISK / fund deemed income) | Förtryckt — verify |
| **7.2** | **Ränteinkomster — HSBC interest (full year 2025)** | **£211.26 → SEK 2,730** |
| **7.3** | **Överskott vid uthyrning av privatbostad (GROSS base)** | **~£24,024 → ~SEK 310,394** |
| **7.4** | **Kapitalvinst — Vanguard ISA sale (genomsnittsmetoden, 4 funds)** | **SEK 150,142** (per K4 working) |

### Avdrag — Kapital (Box 8)

| Box | Item | Value |
|---|---|---|
| **8.1** | **Ränteutgifter — UK mortgage interest only** | **£6,955 → ~SEK 89,876** (product fee excluded) |

### Bilagor
- **K4 avsnitt A** — Vanguard sale, list units / försäljningspris / omkostnadsbelopp / vinst
- **SKV 2703** — Avräkning utländsk skatt claim

### Övriga upplysningar (free text)
Recommended text (Swedish):

> *"Hyresinkomst avser uthyrning av lägenhet i London (76a Ingelow Road, SW8 3PF) via förmedlingsföretag (Knight Frank). Schablonavdrag har applicerats på bruttohyran om GBP 33,900 (SEK [omräknat]). Förmedlingsavgift om GBP 5,062 har inte särskilt dragits av eftersom den ingår i schablonavdraget.*
>
> *Mortgage interest avser ränta på lån hos Santander UK till finansiering av uthyrningsfastigheten. GBP 6,955 omräknat till SEK [belopp]. Produktavgift om GBP 1,749 har inte dragits av i ruta 8.1.*
>
> *Kapitalvinst avser försäljning av Vanguard ISA-konto den 5 juni 2025. Omkostnadsbelopp beräknat enligt genomsnittsmetoden för 14 månadsvisa inbetalningar september 2020 till oktober 2021, omräknat till SEK med Riksbankens månadsgenomsnitt för respektive månad. Vinst redovisad i K4 avsnitt A.*
>
> *Avräkning av utländsk skatt om SEK [belopp] enligt SKV 2703. UK-skatteår löper 6 april till 5 april. Apportion: 3/12 av UK 24/25 (final, GBP 1,092) och 9/12 av UK 25/26 (GBP [214 eller om finalised]). FX-kurser: Riksbankens årsgenomsnitt 2025 = 12.92163 SEK/GBP."*

This open-disclosure paragraph protects against skattetillägg (40% penalty) on any position later challenged — Skatteverket would only re-assess on a rättsfråga basis, with back tax + interest only.

---

## Where everything goes on the UK return (SA100 / SA105)

### SA100 (main return)
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

HSBC interest sits under £1,000 PSA → no additional UK tax. Still report.

---

## FX rates

| Period | Rate | Source |
|---|---|---|
| Riksbanken 2024 annual avg | 13.50453 | 2024 return |
| **Riksbanken 2025 annual avg** | **12.92163** | **2025 return — recurring items** |
| Riksbanken Sep 2020 – Oct 2021 (monthly) | ~11.21 – 11.95 | Vanguard cost basis — estimates in spreadsheet, **verify against Riksbank** |
| Riksbanken Jun 2025 monthly | 12.9485 | Vanguard sale |

---

## Headline tax payable

### Swedish 2025 (using all conservative positions)

| Item | SEK |
|---:|---:|
| Box 7.1 — Schablonintäkter (förtryckt) | 18,360 |
| Box 7.2 — HSBC interest (322 förtryckt + 2,730 HSBC) | 3,052 |
| Box 7.3 — Rental (gross base, schablonavdrag) | 310,434 |
| Box 7.4 — Vanguard CGT (genomsnittsmetoden, 4 funds) | 150,142 |
| Subtotal capital income | 481,988 |
| Less Box 8.1 — Mortgage interest only | (89,876) |
| Net capital base | 392,112 |
| Swedish tax @ 30% | 117,634 |
| Less UK FTC (full UK 25/26 now finalised + 3/12 UK 24/25 apportion) | (~5,600) |
| **Swedish tax payable 2025** | **~SEK 112,034 (~£8,670)** |

### Differential vs less conservative positions
- Net-of-commission base: −~£1,215 of tax
- Product fee in Box 8.1: −~£525 of tax
- Nov 2021 Vanguard value: −~£1,030 of tax

### UK 25/26
- Net UK tax: ~£214

---

## Pre-filing checklist

1. ✅ Schablonavdrag — using GROSS rent (no commission deduction)
2. ✅ Box 8.1 — interest only (no product fee)
3. ✅ Vanguard — genomsnittsmetoden
4. ⚠️ Vanguard FX rates — verify against Riksbanken monthly averages and paste in
5. ⚠️ UK 25/26 SA — file UK first to enable full FTC, or accept partial credit now + omprövning later
6. ⚠️ Schablonintäkter 2025 — check förtryckt return for any
7. ⚠️ Capital losses 2025 — any realised that could offset the Vanguard gain?
8. ⚠️ Add open-disclosure paragraph in Övriga upplysningar (template above)

## What we agreed is NOT available

- ROT/RUT (UK property — not in EES)
- Travel to UK to manage property (covered by schablonavdrag)
- Maintenance / repairs as separate deduction (covered by schablonavdrag)
- Agent commission as separate deduction (covered by schablonavdrag)
- Service charges to freehold management co (covered by schablonavdrag)
- Mortgage product fee as ränteutgift (case law confirms)
- Rebasing Vanguard cost basis to Nov 2021 (no Swedish provision for this)

---

## Source citations

- [Skatteverket — Bostad utomlands](https://www.skatteverket.se/privat/fastigheterochbostad/bostadutomlands.4.233f91f71260075abe8800033670.html)
- [Skatteverket — Hyra ut privatbostad](https://skatteverket.se/privat/fastigheterochbostad/inkomsterfranbostad/hyrautprivatbostadbostadsrattsmahusberattsmahusochhyresratt.4.233f91f71260075abe8800033479.html)
- [SKV 398 — Deklarera bostad i utlandet](https://skatteverket.se/download/18.6e8a1495181dad54084157/1708609332774/Deklarera%20bostad%20i%20utlandet.pdf)
- [Rättslig vägledning — Hyresinkomster och annan avkastning](https://www4.skatteverket.se/rattsligvagledning/edition/2025.2/326151.html)
- [Rättslig vägledning — Förmedlingsföretag](https://www4.skatteverket.se/rattsligvagledning/edition/2023.14/348280.html)
- [Skatteverket — Utländsk valuta](https://www4.skatteverket.se/rattsligvagledning/edition/2025.1/2818.html)
- [Skatteverket — Avdrag för ränteutgifter](https://www.skatteverket.se/privat/deklaration/avdragforprivatpersoner/avdragforranteutgifter.106.1b39a64a1919eabb488b87.html)
- [Rättslig vägledning §2836 — Ränteutgifter](https://www4.skatteverket.se/rattsligvagledning/edition/2025.2/2836.html)
- 2 kap. 2 § och 17 § IL (privatbostadsföretag); 44 kap. 14 § IL (omkostnadsbelopp)
- RÅ 1987 ref. 78; RÅ 1997 ref. 44, 63; RÅ 2001 ref. 21 I (definition of interest)
- [2015 UK-Sweden Double Taxation Convention](https://www.gov.uk/government/publications/sweden-tax-treaties/2015-uk-sweden-double-taxation-convention-as-amended-in-2021-in-force)
- [Riksbanken — Search annual and monthly average exchange rates](https://www.riksbank.se/en-gb/statistics/interest-rates-and-exchange-rates/search-annual-and-monthly-average-exchange-rates/)
