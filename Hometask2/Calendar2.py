from datetime import datetime
from calendar import weekday, day_name, month_name

day = input('Enter day of the week: ')
a = list(day_name)
b = a.index(day)
s = datetime.today()
year = s.year
month = s.month

while True:
    if weekday(year, month, 1) == b:
        print(year, month_name[month])
        break

    month -= 1
    if month == 0:
        year -= 1
        month = 12




