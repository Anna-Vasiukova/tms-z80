from Hometask5.Window import Window
from random import randint

window = Window(0, 0, 500, 500)


class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.point = (self.x, self.y)

    # def draw(self):
    # def top(self) -> float:
    # def bottom(self) -> float: ...  # нижняя граница
    # def left(self) -> float: ...  # левая граница
    # def right(self) -> float: ...  # правая граница


class Rectangle(Shape):  # прямоугольник
    def __init__(self, x, y, width, height):
        Shape.__init__(self, x, y)
        self.width = width
        self.height = height
        self.size = (self.width, self.height)
        window.draw_rectangle(self.point, self.size, color='green')


class Square(Rectangle):  # квадрат
    def __init__(self, x, y, size):
        Rectangle.__init__(self, x, y, size, size)
        window.draw_rectangle(self.point, self.size, color='black')


class Circle(Shape):  # круг
    def __init__(self, x, y, radius):
        Shape.__init__(self, x, y)
        self.radius = radius
        self.size = (2 * self.radius, 2 * self.radius)
        window.draw_ellipse(self.point, self.size, color='red')


class Triangle(Shape):  # равносторонний треугольник
    def __init__(self, x, y, height):
        Shape.__init__(self, x, y)
        self.point2 = (self.x + height, self.y)
        self.point3 = (self.x + height / 2, self.y + height / 2)
        self.points = (self.point, self.point2, self.point3)
        window.draw_polygon(*self.points, color='yellow')


# N = int(input())
# for i in range(N):
#     size = list(map(int, input('Введите размер фигуры: ').split(',')))
#     print(size)

# center = (0, 0)
#
# while not window.closed:
#     start = time()
#     window.clear()
#     point1 = (center[0] + randint(50, 450), center[1] + randint(50, 450))
#     a = Rectangle(*point1, 80, 50)
#     point2 = (center[0] + randint(50, 450), center[1] + randint(50, 450))
#     b = Square(*point2, 50)
#     point3 = (center[0] + randint(50, 450), center[1] + randint(50, 450))
#     c = Circle(*point3, 40)
#     point4 = (center[0] + randint(50, 450), center[1] + randint(50, 450))
#     d = Triangle(*point4, 70)
#     window.update()
#     sleep(0.7)

a = Rectangle(randint(50, 450), randint(50, 450), 80, 50)
dx = 3
dy = 2

while not window.closed:
    window.clear()
    x, y = a.point
    if x+dx >= 420 or x+dx <= 0:
        dx = -dx
    if y+dy >= 450 or y+dy <= 0:
        dy = -dy
    a = Rectangle(x+dx, y+dy, 80, 50)

    window.update()
