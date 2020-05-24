from math import pi, acos

print("Введите длины сторон треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))


def angle(a1, b1, c1):
    angles = acos((b1**2+c1**2-a1**2)/(2*b1*c1))
    return angles*180//pi


if a + b > c and a + c > b and b + c > a:
    #  лучше было сделать функцию:
    #  def angle(a, b, c): ...
    #  вместо того, чтобы три раза дублировать вычисление acos
    print("Треугольник существует")
    al = angle(a, b, c)
    bt = angle(b, a, c)
    gm = angle(c, a, b)
    print(f'Улглы треугольника составляют:\n{al}, {bt}, {gm} градусов')

else:
    print("Треугольник не существует")
