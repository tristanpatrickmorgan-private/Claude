"""Build UK + Swedish tax calculation tabs for 24-25 (filed) and 25-26 (this year)."""
import openpyxl
from openpyxl.styles import Font, PatternFill

SRC = '/root/.claude/uploads/6092ff8c-99e4-41ec-9272-1c431cac58bd/9a049394-Tax_Return.xlsx'
DST = '/home/user/Claude/projects/uk-rental/Tax_Return.xlsx'

wb = openpyxl.load_workbook(SRC)
ws_ing = wb['76A Ingelow Road']
ws_san = wb['Santander']

def read_row(ws, r):
    return [ws.cell(row=r, column=c).value for c in range(1, ws.max_column + 1)]

# Ingelow Road sheet
swed = read_row(ws_ing, 1)
uk = read_row(ws_ing, 2)
income_row = read_row(ws_ing, 6)
mgmt_row = read_row(ws_ing, 10)
letting_row = read_row(ws_ing, 11)
maint_row = read_row(ws_ing, 13)

# Santander sheet
san_uk = read_row(ws_san, 3)      # "23/24", "24/25", etc.
san_swed = read_row(ws_san, 4)    # "2023", "2024", etc.
san_int = read_row(ws_san, 6)
san_fee = read_row(ws_san, 8)

def sum_for(grouping, target, row):
    total = 0
    for i, g in enumerate(grouping):
        if g == target and isinstance(row[i], (int, float)):
            total += row[i]
    return round(total, 2)

# Convert "24.25" float -> "24/25" string
def uk_str_to_slash(uk_float):
    # 24.25 -> "24/25"
    parts = f"{uk_float:.2f}".split(".")
    return f"{parts[0]}/{parts[1]}"

def uk_aggregate(uk_float):
    return {
        "income": sum_for(uk, uk_float, income_row),
        "mgmt": sum_for(uk, uk_float, mgmt_row),
        "letting": sum_for(uk, uk_float, letting_row),
        "maint": sum_for(uk, uk_float, maint_row),
        "mortgage_int": sum_for(san_uk, uk_str_to_slash(uk_float), san_int),
        "mortgage_fee": sum_for(san_uk, uk_str_to_slash(uk_float), san_fee),
    }

def swed_aggregate(yr):
    return {
        "income": sum_for(swed, yr, income_row),
        "mgmt": sum_for(swed, yr, mgmt_row),
        "letting": sum_for(swed, yr, letting_row),
        "maint": sum_for(swed, yr, maint_row),
        "mortgage_int": sum_for(san_swed, str(yr), san_int),
        "mortgage_fee": sum_for(san_swed, str(yr), san_fee),
    }

# FX
FX_2024 = 13.50453
FX_2025 = 12.919

# UK tax bands (24/25 and 25/26 — both frozen at these values)
PA = 12570
BASIC_TOP = 50270
BASIC_RATE = 0.20
FIN_CREDIT_RATE = 0.20

# Swedish deductions
SE_STD_SEK = 40000
SE_PCT = 0.20

def build_sheet(wb, name, uk_float, swed_yr, fx, fx_label,
                uk_prior_str, uk_prior_tax_gbp):
    if name in wb.sheetnames:
        del wb[name]
    ws = wb.create_sheet(name)

    uk_d = uk_aggregate(uk_float)
    sw_d = swed_aggregate(swed_yr)

    H = Font(bold=True, size=14, color="FFFFFF")
    HF = PatternFill("solid", fgColor="4472C4")
    S = Font(bold=True, size=11)
    SF = PatternFill("solid", fgColor="D9E1F2")
    R = PatternFill("solid", fgColor="FFE699")
    G = PatternFill("solid", fgColor="C6EFCE")
    B = Font(bold=True)

    r = 1
    ws.cell(row=r, column=1, value=f"Tax calculation — UK {uk_str_to_slash(uk_float)} + Swedish {swed_yr}").font = H
    ws.cell(row=r, column=1).fill = HF
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=5)
    r += 2

    ws.cell(row=r, column=1, value="FX rate (SEK per GBP)").font = B
    ws.cell(row=r, column=2, value=fx)
    ws.cell(row=r, column=3, value=fx_label)
    r += 2

    # === UK section ===
    ws.cell(row=r, column=1, value=f"UK tax year {uk_str_to_slash(uk_float)} (6 April to 5 April)").font = S
    for c in range(1, 6): ws.cell(row=r, column=c).fill = SF
    r += 1
    ws.cell(row=r, column=2, value="GBP").font = B
    r += 1

    ws.cell(row=r, column=1, value="Rental Income")
    ws.cell(row=r, column=2, value=uk_d["income"])
    r += 1

    uk_comm = round(uk_d["mgmt"] + uk_d["letting"], 2)
    ws.cell(row=r, column=1, value="Knight Frank Commission (mgmt + letting)")
    ws.cell(row=r, column=2, value=uk_comm)
    r += 1

    uk_net_pre = round(uk_d["income"] + uk_comm, 2)
    ws.cell(row=r, column=1, value="Net Income before Expenses").font = B
    ws.cell(row=r, column=2, value=uk_net_pre).font = B
    r += 1

    ws.cell(row=r, column=1, value="Repair and Maintenance Expenses")
    ws.cell(row=r, column=2, value=uk_d["maint"])
    r += 1

    uk_profit = round(uk_net_pre + uk_d["maint"], 2)
    ws.cell(row=r, column=1, value="Taxable Property Profit (SA105 box 38/40)").font = B
    ws.cell(row=r, column=2, value=uk_profit).font = B
    ws.cell(row=r, column=2).fill = R
    r += 2

    ws.cell(row=r, column=1, value="Memo — residential property finance costs (SA105 box 44):").font = Font(italic=True)
    r += 1
    ws.cell(row=r, column=1, value="  Mortgage interest")
    ws.cell(row=r, column=2, value=uk_d["mortgage_int"])
    r += 1
    ws.cell(row=r, column=1, value="  Mortgage product fees")
    ws.cell(row=r, column=2, value=uk_d["mortgage_fee"])
    r += 1
    uk_fin = round(uk_d["mortgage_int"] + uk_d["mortgage_fee"], 2)
    ws.cell(row=r, column=1, value="  Total residential finance costs").font = B
    ws.cell(row=r, column=2, value=uk_fin).font = B
    r += 2

    ws.cell(row=r, column=1, value="UK tax calculation").font = S
    for c in range(1, 6): ws.cell(row=r, column=c).fill = SF
    r += 1
    ws.cell(row=r, column=1, value=f"Personal Allowance (0%)")
    ws.cell(row=r, column=2, value=PA)
    r += 1
    ws.cell(row=r, column=1, value=f"Basic rate band cap (20% to £{BASIC_TOP:,})")
    ws.cell(row=r, column=2, value=BASIC_TOP)
    r += 2

    ws.cell(row=r, column=1, value="Total taxable income (property profit)")
    ws.cell(row=r, column=2, value=uk_profit)
    r += 1
    above_pa = max(0, uk_profit - PA)
    ws.cell(row=r, column=1, value="Above personal allowance")
    ws.cell(row=r, column=2, value=round(above_pa, 2))
    r += 1
    basic_tax = round(above_pa * BASIC_RATE, 2)
    ws.cell(row=r, column=1, value="Basic rate tax (20%)")
    ws.cell(row=r, column=2, value=basic_tax)
    r += 1
    fin_credit = round(uk_fin * FIN_CREDIT_RATE, 2)
    ws.cell(row=r, column=1, value=f"Less: financing cost credit (20% × £{uk_fin:,.2f})")
    ws.cell(row=r, column=2, value=-fin_credit)
    r += 1
    net_uk_tax = round(basic_tax - fin_credit, 2)
    ws.cell(row=r, column=1, value="Net UK Tax").font = B
    ws.cell(row=r, column=2, value=net_uk_tax).font = B
    ws.cell(row=r, column=2).fill = G
    r += 3

    # === Swedish section ===
    ws.cell(row=r, column=1, value=f"Swedish tax year {swed_yr} (1 January to 31 December)").font = S
    for c in range(1, 6): ws.cell(row=r, column=c).fill = SF
    r += 1
    ws.cell(row=r, column=2, value="GBP").font = B
    ws.cell(row=r, column=3, value="SEK").font = B
    r += 1

    ws.cell(row=r, column=1, value="Rental Income")
    ws.cell(row=r, column=2, value=sw_d["income"])
    ws.cell(row=r, column=3, value=round(sw_d["income"] * fx, 2))
    r += 1

    sw_comm = round(sw_d["mgmt"] + sw_d["letting"], 2)
    ws.cell(row=r, column=1, value="Knight Frank Commission")
    ws.cell(row=r, column=2, value=sw_comm)
    ws.cell(row=r, column=3, value=round(sw_comm * fx, 2))
    r += 1

    sw_base = round(sw_d["income"] + sw_comm, 2)
    ws.cell(row=r, column=1, value="Rental income net of commission (basis for schablonavdrag)").font = B
    ws.cell(row=r, column=2, value=sw_base).font = B
    ws.cell(row=r, column=3, value=round(sw_base * fx, 2)).font = B
    ws.cell(row=r, column=2).fill = R
    ws.cell(row=r, column=3).fill = R
    r += 2

    # Schablonavdrag — replaces actual expense deduction in Sweden
    ws.cell(row=r, column=1, value="Schablonavdrag (replaces actual expense deduction):").font = Font(italic=True)
    r += 1
    std_gbp = round(SE_STD_SEK / fx, 2)
    ws.cell(row=r, column=1, value="  Standard SEK 40,000 deduction")
    ws.cell(row=r, column=2, value=-std_gbp)
    ws.cell(row=r, column=3, value=-SE_STD_SEK)
    r += 1
    pct_gbp = round(sw_base * SE_PCT, 2)
    ws.cell(row=r, column=1, value="  20% of rental income (net of commission) deduction")
    ws.cell(row=r, column=2, value=-pct_gbp)
    ws.cell(row=r, column=3, value=round(-pct_gbp * fx, 2))
    r += 1

    sw_box73 = round(sw_base - std_gbp - pct_gbp, 2)
    ws.cell(row=r, column=1, value="Box 7.3 — Överskott vid uthyrning av privatbostad").font = B
    ws.cell(row=r, column=2, value=sw_box73).font = B
    ws.cell(row=r, column=3, value=round(sw_box73 * fx, 2)).font = B
    ws.cell(row=r, column=2).fill = G
    ws.cell(row=r, column=3).fill = G
    r += 2

    # Memo for repairs (not deductible under schablonavdrag)
    ws.cell(row=r, column=1, value=f"Memo — repairs not deductible under schablonavdrag: £{sw_d['maint']:,.2f}").font = Font(italic=True)
    r += 2

    # Box 8.1 — mortgage interest (separately deducted, treated as private interest)
    ws.cell(row=r, column=1, value="Box 8.1 — Ränteutgifter (mortgage interest)").font = S
    for c in range(1, 6): ws.cell(row=r, column=c).fill = SF
    r += 1
    ws.cell(row=r, column=1, value="Mortgage interest (calendar year)")
    ws.cell(row=r, column=2, value=sw_d["mortgage_int"])
    ws.cell(row=r, column=3, value=round(sw_d["mortgage_int"] * fx, 2))
    r += 1
    if sw_d["mortgage_fee"] > 0:
        ws.cell(row=r, column=1, value="Mortgage product fees (also deductible)")
        ws.cell(row=r, column=2, value=sw_d["mortgage_fee"])
        ws.cell(row=r, column=3, value=round(sw_d["mortgage_fee"] * fx, 2))
        r += 1
    sw_box81 = round(sw_d["mortgage_int"] + sw_d["mortgage_fee"], 2)
    ws.cell(row=r, column=1, value="Box 8.1 total").font = B
    ws.cell(row=r, column=2, value=sw_box81).font = B
    ws.cell(row=r, column=3, value=round(sw_box81 * fx, 2)).font = B
    ws.cell(row=r, column=2).fill = G
    ws.cell(row=r, column=3).fill = G
    r += 2

    # Foreign tax credit
    ws.cell(row=r, column=1, value="Foreign tax credit (Avräkning utländsk skatt)").font = S
    for c in range(1, 6): ws.cell(row=r, column=c).fill = SF
    r += 1
    ws.cell(row=r, column=1, value=f"UK {uk_prior_str} tax × 3/12 (Jan-Mar fell in old UK year)")
    ws.cell(row=r, column=2, value=round(uk_prior_tax_gbp * 3/12, 2))
    ws.cell(row=r, column=3, value=round(uk_prior_tax_gbp * 3/12 * fx, 2))
    r += 1
    ws.cell(row=r, column=1, value=f"UK {uk_str_to_slash(uk_float)} tax × 9/12 (Apr-Dec fell in new UK year)")
    ws.cell(row=r, column=2, value=round(net_uk_tax * 9/12, 2))
    ws.cell(row=r, column=3, value=round(net_uk_tax * 9/12 * fx, 2))
    r += 1
    ftc_gbp = round(uk_prior_tax_gbp * 3/12 + net_uk_tax * 9/12, 2)
    ws.cell(row=r, column=1, value="Apportioned FTC for this Swedish year").font = B
    ws.cell(row=r, column=2, value=ftc_gbp).font = B
    ws.cell(row=r, column=3, value=round(ftc_gbp * fx, 2)).font = B
    ws.cell(row=r, column=2).fill = G
    ws.cell(row=r, column=3).fill = G
    r += 2

    # Column widths
    ws.column_dimensions['A'].width = 60
    ws.column_dimensions['B'].width = 13
    ws.column_dimensions['C'].width = 14

    return {
        "uk_profit": uk_profit, "uk_tax": net_uk_tax,
        "sw_box73": sw_box73, "sw_box81": sw_box81, "ftc": ftc_gbp,
    }

r2425 = build_sheet(wb, "Tax 24-25", 24.25, 2024, FX_2024,
                    "Riksbanken 2024 annual avg",
                    "23/24", 1128)
r2526 = build_sheet(wb, "Tax 25-26", 25.26, 2025, FX_2025,
                    "Approx 2025 avg (verify vs Riksbanken)",
                    "24/25", r2425["uk_tax"])
wb.save(DST)

print("\n=== Tax 24-25 (verification) ===")
print(f"  UK 24/25 taxable profit:   £{r2425['uk_profit']:,.2f}  (filed: ~£22,941)")
print(f"  UK 24/25 net tax:          £{r2425['uk_tax']:,.2f}  (filed: ~£1,193)")
print(f"  Sweden 2024 Box 7.3:       £{r2425['sw_box73']:,.2f}  (filed: £16,695)")
print(f"  Sweden 2024 Box 8.1:       £{r2425['sw_box81']:,.2f}  (filed: £3,354)")
print(f"  Sweden 2024 FTC:           £{r2425['ftc']:,.2f}  (filed: £1,176)")
print("\n=== Tax 25-26 (this year) ===")
print(f"  UK 25/26 taxable profit:   £{r2526['uk_profit']:,.2f}")
print(f"  UK 25/26 net tax:          £{r2526['uk_tax']:,.2f}")
print(f"  Sweden 2025 Box 7.3:       £{r2526['sw_box73']:,.2f}")
print(f"  Sweden 2025 Box 8.1:       £{r2526['sw_box81']:,.2f}")
print(f"  Sweden 2025 FTC:           £{r2526['ftc']:,.2f}")
