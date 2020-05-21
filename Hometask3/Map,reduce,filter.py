from random import randint
from functools import reduce

n = int(input())
array = [randint(1, 9) for i in range(n)]
print(array)


#  REDUCER


def amount(a1, b1):
    return a1 + b1


def multiply(a1, b1):
    return a1 * b1


def joins(a1, b1):
    return str(a1) + str(b1)


def unique(f: set, y):
    f.add(y)
    return f


def revers(seq: list, y):
    seq.insert(0, y)
    return seq


# MAPPER


def negate(lst):
    return -lst


def invert(lst):
    return 1 / lst


def squared(lst):
    return lst ** 2


# FILTER


def odds(lst):
    return lst % 2


def evens(lst):
    return (lst + 1) % 2


def primes(lst):
    simple = [2, 3, 5, 7]
    if lst in simple:
        return lst


reducers = {'sum': (amount, 0),
            'multiply': (multiply, 1),
            'join': (joins, 0),
            'unite': (unique, set),
            'reverse': (revers, list)
            }
mappers = {
    'negated': negate,
    'inverted': invert,
    'squared': squared
        }
generators = {'evens': evens,
              'odds': odds,
              'primes': primes
              }

reducers_request, mappers_request, generators_request = input().split()
reducer, initial = reducers[reducers_request]
mapper = mappers[mappers_request]
generator = generators[generators_request]

c = reduce(reducer, array, initial())
d = list(map(mapper, array))
z = list(filter(generator, array))
print(c)
print(d)
print(z)

q = list(map(mapper, list(filter(generator, array))))
w = reduce(reducer, list(map(mapper, list(filter(generator, array)))), initial())
print(q)
print(w)
