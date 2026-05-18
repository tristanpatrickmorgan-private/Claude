"""Replace Capital Gains 2025 tab with proper genomsnittsmetoden using actual contribution history."""
import openpyxl
from openpyxl.styles import Font, PatternFill

PATH = '/home/user/Claude/projects/uk-rental/Tax_Return.xlsx'
wb = openpyxl.load_workbook(PATH)

name = "Capital Gains 2025"
if name in wb.sheetnames:
    del wb[name]
ws = wb.create_sheet(name)

H = Font(bold=True, size=14, color="FFFFFF")
HF = PatternFill("solid", fgColor="4472C4")
S = Font(bold=True, size=11)
SF = PatternFill("solid", fgColor="D9E1F2")
R = PatternFill("solid", fgColor="FFE699")
G = PatternFill("solid", fgColor="C6EFCE")
Y = PatternFill("solid", fgColor="FFFFCC")  # editable FX cells
Bld = Font(bold=True)
It = Font(italic=True)

ws.cell(row=1, column=1, value="Vanguard ISA — Capital Gains 2025 (genomsnittsmetoden)").font = H
ws.cell(row=1, column=1).fill = HF
ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=6)

ws.cell(row=3, column=1, value="Per Swedish tax law: cost basis = original acquisition cost in SEK at original-date FX rate.").font = It
ws.cell(row=4, column=1, value="No rebasing on Swedish residency move. All contributions were Sep 2020 to Oct 2021 (no contributions after Nov 2021 move).").font = It
ws.cell(row=5, column=1, value="FX rates in yellow cells — approximate; verify against Riksbanken monthly averages and overwrite.").font = It

# Header row
r = 7
hdrs = ["Month", "Contribution (£)", "Monthly avg FX (SEK/GBP)", "Source", "SEK cost basis", ""]
for i, h in enumerate(hdrs, 1):
    ws.cell(row=r, column=i, value=h).font = Bld
    ws.cell(row=r, column=i).fill = SF

# Contributions from Vanguard PDF (the "Purchases & Withdrawals" column)
# FX estimates from general knowledge — user to verify against Riksbank
contributions = [
    ("Sep 2020", 200.00,    11.34, "Riksbanken monthly avg (estimate, verify)"),
    ("Oct 2020", 2508.82,   11.27, "Riksbanken monthly avg (estimate, verify)"),
    ("Nov 2020", 200.00,    11.34, "Riksbanken monthly avg (estimate, verify)"),
    ("Dec 2020", 200.00,    11.21, "Riksbanken monthly avg (estimate, verify)"),
    ("Jan 2021", 200.00,    11.34, "Riksbanken monthly avg (estimate, verify)"),
    ("Feb 2021", 9800.00,   11.78, "Riksbanken monthly avg (estimate, verify)"),
    ("Mar 2021", 800.00,    11.78, "Riksbanken monthly avg (estimate, verify)"),
    ("Apr 2021", 800.00,    11.74, "Riksbanken monthly avg (estimate, verify)"),
    ("May 2021", 800.00,    11.78, "Riksbanken monthly avg (estimate, verify)"),
    ("Jun 2021", 800.00,    11.80, "Riksbanken monthly avg (estimate, verify)"),
    ("Jul 2021", 800.00,    11.80, "Riksbanken monthly avg (estimate, verify)"),
    ("Aug 2021", 800.00,    11.95, "Riksbanken monthly avg (estimate, verify)"),
    ("Sep 2021", 800.00,    11.92, "Riksbanken monthly avg (estimate, verify)"),
    ("Oct 2021", 800.00,    11.89, "Riksbanken monthly avg (estimate, verify)"),
]

first_contrib_row = r + 1
for month, gbp, fx, src in contributions:
    r += 1
    ws.cell(row=r, column=1, value=month)
    ws.cell(row=r, column=2, value=gbp)
    ws.cell(row=r, column=3, value=fx)
    ws.cell(row=r, column=3).fill = Y  # mark editable
    ws.cell(row=r, column=4, value=src)
    ws.cell(row=r, column=5, value=f"=B{r}*C{r}")
last_contrib_row = r

r += 1
ws.cell(row=r, column=1, value="Total contributions").font = Bld
ws.cell(row=r, column=2, value=f"=SUM(B{first_contrib_row}:B{last_contrib_row})").font = Bld
ws.cell(row=r, column=5, value=f"=SUM(E{first_contrib_row}:E{last_contrib_row})").font = Bld
ws.cell(row=r, column=2).fill = R
ws.cell(row=r, column=5).fill = R
total_gbp_ref = f"$B${r}"
total_sek_basis_ref = f"$E${r}"
r += 2

# Sale
ws.cell(row=r, column=1, value="Sale 5 June 2025").font = S
for c in range(1, 7): ws.cell(row=r, column=c).fill = SF
r += 1
ws.cell(row=r, column=1, value="Sale proceeds (£)")
ws.cell(row=r, column=2, value=29862.97)
sale_gbp_ref = f"$B${r}"
r += 1
ws.cell(row=r, column=1, value="June 2025 monthly avg FX (SEK/GBP)")
ws.cell(row=r, column=2, value=12.9485)
ws.cell(row=r, column=2).fill = Y
ws.cell(row=r, column=4, value="Riksbanken Jun 2025 monthly avg")
sale_fx_ref = f"$B${r}"
r += 1
ws.cell(row=r, column=1, value="Sale proceeds (SEK)").font = Bld
ws.cell(row=r, column=2, value=f"={sale_gbp_ref}*{sale_fx_ref}").font = Bld
ws.cell(row=r, column=2).fill = R
sale_sek_ref = f"$B${r}"
r += 2

# Gain
ws.cell(row=r, column=1, value="Calculation").font = S
for c in range(1, 7): ws.cell(row=r, column=c).fill = SF
r += 1
ws.cell(row=r, column=2, value="GBP").font = Bld
ws.cell(row=r, column=3, value="SEK").font = Bld
r += 1
ws.cell(row=r, column=1, value="Sale proceeds")
ws.cell(row=r, column=2, value=f"={sale_gbp_ref}")
ws.cell(row=r, column=3, value=f"={sale_sek_ref}")
r += 1
ws.cell(row=r, column=1, value="Less: Omkostnadsbelopp (sum of contributions in SEK)")
ws.cell(row=r, column=2, value=f"=-{total_gbp_ref}")
ws.cell(row=r, column=3, value=f"=-{total_sek_basis_ref}")
r += 1
ws.cell(row=r, column=1, value="Capital gain").font = Bld
ws.cell(row=r, column=2, value=f"={sale_gbp_ref}-{total_gbp_ref}").font = Bld
ws.cell(row=r, column=3, value=f"={sale_sek_ref}-{total_sek_basis_ref}").font = Bld
ws.cell(row=r, column=2).fill = R
ws.cell(row=r, column=3).fill = R
gain_gbp_ref = f"$B${r}"
gain_sek_ref = f"$C${r}"
r += 2

ws.cell(row=r, column=1, value="Swedish capital tax (30%)").font = Bld
ws.cell(row=r, column=2, value=f"={gain_sek_ref}*0.30/{sale_fx_ref}").font = Bld
ws.cell(row=r, column=3, value=f"={gain_sek_ref}*0.30").font = Bld
ws.cell(row=r, column=2).fill = G
ws.cell(row=r, column=3).fill = G
r += 3

# Footer notes
ws.cell(row=r, column=1, value="Genomsnittsmetoden (weighted-average) cost basis").font = S
for c in range(1, 7): ws.cell(row=r, column=c).fill = SF
r += 1
ws.cell(row=r, column=1, value="• Sweden uses genomsnittsmetoden: each contribution's cost basis is the GBP × FX at acquisition date.").font = It
r += 1
ws.cell(row=r, column=1, value="• Since the user sold ALL units in June 2025, the cost basis is simply the SEK sum of all contributions.").font = It
r += 1
ws.cell(row=r, column=1, value="• No rebasing on becoming Swedish resident (Nov 2021).").font = It
r += 1
ws.cell(row=r, column=1, value="• Reference: 44 kap. 14 § Inkomstskattelagen; Skatteverket 'Utländsk valuta' guidance.").font = It
r += 1
ws.cell(row=r, column=1, value="• Yellow FX cells are estimates — verify against riksbank.se/sv/statistik/rantor-och-valutakurser/sok-rantor-och-valutakurser/").font = It

# Reporting in INK1
r += 2
ws.cell(row=r, column=1, value="Reporting on Swedish tax return (INK1)").font = S
for c in range(1, 7): ws.cell(row=r, column=c).fill = SF
r += 1
for note in [
    "• File K4 avsnitt A — list units sold, försäljningspris (sale SEK), omkostnadsbelopp (cost SEK), vinst",
    "• Net gain rolls into Box 7.4 (kapitalvinst marknadsnoterade aktier/fonder)",
    "• ISA wrapper is irrelevant for Swedish tax — full gain taxable",
    "• Capital losses elsewhere in 2025 can offset (100% against listed shares, 70% against other capital)",
]:
    ws.cell(row=r, column=1, value=note).font = It
    r += 1

# Column widths
ws.column_dimensions['A'].width = 50
ws.column_dimensions['B'].width = 18
ws.column_dimensions['C'].width = 20
ws.column_dimensions['D'].width = 38
ws.column_dimensions['E'].width = 18

# Now I need to update the Tax 25-26 sheet — Box 7.4 references this sheet's gain cells
# The new gain GBP is at gain_gbp_ref, SEK at gain_sek_ref
# Update Tax 25-26 row 66 to point to these new cells

# First find the row & column for those cells:
# gain row is row r-... let me track better. Capture the row numbers.

# Re-find by reloading
wb.save(PATH)
wb2 = openpyxl.load_workbook(PATH)
ws2 = wb2['Capital Gains 2025']
for rr in range(1, ws2.max_row + 1):
    a = ws2.cell(row=rr, column=1).value
    if a and str(a) == "Capital gain":
        gain_row = rr
        break

print(f"Gain row found at {gain_row}")

# Update Tax 25-26 row 66 to reference the new gain cells
ws_tax = wb2['Tax 25-26']
ws_tax.cell(row=66, column=2, value=f"='Capital Gains 2025'!$B${gain_row}")
ws_tax.cell(row=66, column=3, value=f"='Capital Gains 2025'!$C${gain_row}")

wb2.save(PATH)

# Print result preview
total_gbp = sum(c[1] for c in contributions)
total_sek_basis = sum(c[1] * c[2] for c in contributions)
sale_sek = 29862.97 * 12.9485
gain_sek = sale_sek - total_sek_basis
print(f"\nTotal contributions GBP: £{total_gbp:,.2f}")
print(f"Total cost basis SEK (using estimates): SEK {total_sek_basis:,.2f}")
print(f"Sale proceeds SEK: SEK {sale_sek:,.2f}")
print(f"Gain SEK: SEK {gain_sek:,.2f}")
print(f"Tax at 30%: SEK {gain_sek * 0.30:,.2f}")
print(f"vs previous calc using Nov 2021 value:")
print(f"  Previous gain SEK: SEK 113,822")
print(f"  Previous tax: SEK 34,147")
print(f"  Increase: SEK {gain_sek * 0.30 - 34147:,.2f}")
