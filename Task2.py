n = int(input())
a = [int(input()) for i in range(n)]
s = sorted(a)
print(s[-1], s[-2])