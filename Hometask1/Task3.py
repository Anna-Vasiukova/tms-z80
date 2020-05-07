n = int(input())
a = [int(input()) for i in range(n)]
y = a.count(0)
x = 0
while x in a:
    x = 0
    a.remove(x)
b = [0]*y
c = b+a
print(c)
