from random import randint

while True:
    s = int(input('Отгадай число:'))
    a = randint(0, 11)
    # обращай внимание на предупреждения PEP8
    # между значениями и операторами должен быть пробел
    # между именем функции и оператором вызова пробела нет
    if s > 10:
        print('Я загадываю числа от 1 до 10')
    elif s == a:
        print('Победил')
        break
    # elif - лишний, потому что условие проверять необязательно
    # если s == a не выполнился, то s != a и так всегда будет верно
    # поэтому логичнее использовать просто else
    else:
        print('Проиграл')
        # continue здесь лишний, потому что это и так последняя инструкция в блоке
        # хотя для читаемости оставить можно, но тогда непонятно, почему в блоке if s > 10 его нет :)
