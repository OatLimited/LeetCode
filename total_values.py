line = input('Enter expenses : ')
expenses = line.split()
print(expenses)
total_expensesd = 0
for expense in expenses:
    total_expensesd += float(expense)
print('Total expenses is ', total_expensesd)
