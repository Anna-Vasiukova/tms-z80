from itertools import chain


def log(func):
    def wrapper(*args, **kwargs):
        print(func.__name__, end='')
        arg_str = ', '.join(chain(map(str, args), map(lambda x: f'{x[0]}={x[1]}', kwargs.items())))
        print(f'({arg_str})', end='')
        result = func(*args, **kwargs)
        print(f' -> {result}')
        return result
    return wrapper


@log
def a(x):
    return -x


@log
def b(x, y):
    return x * y


@log
def c(x, y, *args):
    result = x + y
    for arg in args:
        result += arg
    return result


a(1)        # out > a(1) -> -1
b(2, y=3)   # out > b(2, y=3) -> 6
c(1, 2, 3)  # out > c(1, 2, 3) -> 6
