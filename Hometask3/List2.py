x = input('Введите список чисел: ')
a = x.split(' ')
print(a)
b = set(a)
c = 0
m = 1

for i in b:
    d = a.count(i)
    if d > m:
        m = d
        c = i

print(f'{c} повторяется {m} раз')