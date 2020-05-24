from collections import deque
from time import time

values = deque()
while True:
    n = int(input())
    t = int(1000 * time())
    values.append((n, t))
    while len(values):
        value = values[0]
        if t - value[1] < 5000:
            break
        values.popleft()
    for value in values:
        print(f'{value[0]} ', end='')
    print()
