import calendar
s = input()
x = s.split('.')
a = calendar.weekday(int(x[-1]), int(x[-2]), int(x[-3]))
if a == 0:
    print('Monday')
elif a == 1:
    print('Tuesday')
elif a == 2:
    print('Wednesday')
elif a == 3:
    print('Thursday')
elif a == 4:
    print('Friday')
elif a == 5:
    print('Saturday')
elif a == 6:
    print('Sunday')
else:
    print('Error')
