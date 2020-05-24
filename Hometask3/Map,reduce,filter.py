from random import randint
from functools import reduce
from math import log10

n = int(input())
array = [randint(1, 9) for i in range(n)]
print(array)


#  REDUCER


def amount(a1, b1):
    return a1 + b1


def multiply(a1, b1):
    return a1 * b1


def joins(a1, b1):
    digits = int(log10(abs(b1))+1)
    return a1*10**digits+b1


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
    return lst in {1, 2, 3, 5, 7}


reducers = {'sum': (amount, lambda: 0),
            'multiply': (multiply, lambda: 1),
            'join': (joins, lambda: 0),
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


sp1 = list(map(mapper, filter(generator, array)))
result = reduce(reducer, list(map(mapper, filter(generator, array))), initial())
print(sp1)
print(result)
