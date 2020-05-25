from functools import reduce


def multiply(f):
    def wrapper(*args):
        b = reduce(lambda x, y: x * y, *args)
        print(b)
        result = f(*args)
        return result
    return wrapper


@multiply
def func(x):
    print(x)


numbers = list(map(int, input().split()))
func(numbers)

# in  > 1 2 3
# out > 6
