hourly_rate = float(input("Enter Hourly Rate : "))
hours_worked = int(input("Enter Hours Worked : "))
tax_bracket = float(input("Enter Tax Bracket (Example 0.20): "))

gross_pay = hourly_rate * hours_worked
net_pay = gross_pay - (gross_pay * tax_bracket)

print("\nProcessed Data Types")

print("hourly_rate :", type(hourly_rate))
print("hours_worked:", type(hours_worked))
print("tax_bracket :", type(tax_bracket))
print("gross_pay   :", type(gross_pay))
print("net_pay     :", type(net_pay))


print("\n")

header = f"{'OFFICIAL PAYSLIP':=^40}"
divider = "=" * 40

print(header)
print(divider)

print(f"{'Hourly Rate':<25}${hourly_rate:>13.3f}")
print(f"{'Hours Worked':<25}{hours_worked:>14}")
print(f"{'Tax Bracket':<25}{tax_bracket:>13.3f}")
print(f"{'Gross Pay':<25}${gross_pay:>13.3f}")
print(f"{'Net Pay':<25}${net_pay:>13.3f}")
print(divider)