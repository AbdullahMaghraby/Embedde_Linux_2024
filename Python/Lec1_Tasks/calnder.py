#Print the calendar of a given month and year

import calendar

# Input month and year
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

print(calendar.month(year, month))
