year = float(input('input year : '))
if year % 4 == 0 and year % 400 != 0:
    print('This is leap year')
else:
    print('This is year')
