from random import randint
from functools import reduce

n = int(input())
array = [randint(1, 9) for i in range(n)]
print(array)


amount = (lambda a1, b1: a1+b1, lambda: 0)
# print(amount)


multiply_all = reduce(lambda a1, b1: a1*b1, array)
print(multiply_all)


joins = reduce(lambda a1,b1: a1*10+b1, array)
print(joins)


def unique(lst):
    y = set(lst)
    return y


print(unique(array))


def revers(lst):
    return list(reversed(lst))


print(revers(array))


def negate(lst):
    return -lst


# negated = list(map(negate, array))
# print(negated)

inv = list(map(lambda a1: 1 / a1, array))
print(inv)

sq = list(map(lambda a1: a1**2, array))
print(sq)


def odds(lst):
    return lst % 2


def evens(lst):
    return (lst+1) % 2


def primes(lst):
    for i in (2, 3, 5, 7):
        return lst
print(primes(array))


Od = list(filter(odds, array))
print(Od)

Ev = list(filter(evens, array))
print(Ev)

reducers = {'sum': amount,
            'multiply': multiply_all,
            'join': joins,
            'unite': unique(array),
            'reverse': revers(array)}
mappers = {
    'negated': negate,
    'inverted': inv,
    'squared': sq}
generators = {'evens': Ev,
              'odds': Od }

reducers_name, mappers_name, generators_name = input().split()
reducer = reducers[reducers_name]
mapper = mappers[mappers_name]
generator = generators[generators_name]

# result = reduce(reduce, map(mapper, generator))

# print(result)

# print(reducer)
# # print(mapper(array))
# print(generator)
# d = list(map(mapper, generator))
# print(f'D: {d}')
# c = (unique, d)
# print(c)