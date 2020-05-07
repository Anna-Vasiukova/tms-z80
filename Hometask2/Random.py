from random import randint

while True:
    s = int(input('Отгадай число:'))
    a = randint(0, 11)
    if s>10:
        print ('Я загадываю числа от 1 до 10')
    elif s == a:
        print ('Победил')
        break
    elif s != a:
        print('Проиграл')
        continue

