number_of_hours = float(input('enter hour (hrs) : '))
hourly_rate = float(input('enter rate (thb):'))
if number_of_hours > 40:
    wages = (40 * hourly_rate) + ((number_of_hours-40) * hourly_rate * 1.5)
else:
    wages = number_of_hours * hourly_rate
print(f'This is you wages = {wages}')
