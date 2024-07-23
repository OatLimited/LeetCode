print('-'*20)
print('Income Tax calculator')
print()
taxable_income = float(input("Enter Income : "))

tax = 0

if taxable_income < 150000:
    tax = 0
elif taxable_income < 300000:
    tax = (taxable_income - 150000) * 0.05
elif taxable_income < 50000:
    tax = 7500 + (taxable_income - 300000) * 0.1
elif taxable_income < 750000:
    tax = 7500 + 20000 + (taxable_income - 500000) * 0.15
elif taxable_income < 1000000:
    tax = 7500 + 20000 + 37500 + (taxable_income - 750000) * 0.2
elif taxable_income < 2000000:
    tax = 7500 + 20000 + 37500 + 50000 + (taxable_income - 2000000) * 0.25
elif taxable_income < 2000000:
    tax = 7500 + 20000 + 37500 + 50000 + \
        250000 + (taxable_income - 2000000) * 0.3
else:
    tax = 7500 + 20000 + 37500 + 50000 + 250000 + \
        900000 + (taxable_income - 2000000) * 0.3

print(f'Your tax is {tax}')
