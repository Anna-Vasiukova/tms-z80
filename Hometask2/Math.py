print("Введите длины сторон треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

from math import cos, pi, acos

if a + b > c and a + c > b and b + c > a:
    #  лучше было сделать функцию:
    #  def angle(a, b, c): ...
    #  вместо того, чтобы три раза дублировать вычисление acos
    print("Треугольник существует")
    alfa = acos((b**2+c**2-a**2)/(2*b*c))
    print((alfa)*180//pi)
    betta = acos((a**2+c**2-b**2)/(2*a*c))
    print((betta)*180//pi)
    gamma = acos((a**2+c**2-b**2)/(2*a*c))
    print((gamma)*180//pi)
else:
    print("Треугольник не существует")
