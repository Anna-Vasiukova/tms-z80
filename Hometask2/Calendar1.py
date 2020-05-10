from calendar import weekday, day_name
s = input()
x = s.split('.')
a = weekday(int(x[-1]), int(x[-2]), int(x[-3]))
print(day_name[a])
