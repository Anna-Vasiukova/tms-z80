from math import cos
k=8
print(cos(k))

x = int(input())
n = int(input())

def fact(y):
    z = 1
    for i in range(2, y + 1):
        z *= i
    return z


b = 0

for p in range(1, n+1):
    b += (-1)**p*x**(p*2)/fact(2*p)
d = 1+b
print(d)







