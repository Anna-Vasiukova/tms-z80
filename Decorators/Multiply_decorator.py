from functools import reduce


def multiply(f):
    def wrapper(*args):
        result = f(reduce(lambda x, y: x * y, args))
        return result
    return wrapper


@multiply
def func(x):
    print(x)


numbers = map(int, input().split())
func(*numbers)

# in  > 1 2 3
# out > 6
