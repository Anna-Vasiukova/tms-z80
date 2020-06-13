from random import randint
from Hometask5.Window import Window
from abc import abstractmethod
from time import *

window = Window(0, 0, 500, 500)
fps = 120


class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def top(self) -> float:
        pass

    @abstractmethod
    def bottom(self) -> float:
        pass

    @abstractmethod
    def left(self) -> float:
        pass

    @abstractmethod
    def right(self):
        pass


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        Shape.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dx = 2
        self.dy = 1

    def draw(self):
        window.draw_rectangle((self.x - 0.5 * self.width, self.y - 0.5 * self.height), (self.width, self.height),
                              color='green')

    def top(self):
        return self.y - 0.5 * self.height

    def bottom(self):
        return self.top() + self.height

    def left(self):
        return self.x - 0.5 * self.width

    def right(self):
        return self.left() + self.width

    @classmethod
    def input(cls):
        w = int(input('Введите ширину пямоугольника: '))
        h = int(input('Введите высоту пямоугольника: '))
        x = randint(0+w/2, window.width-w/2)
        y = randint(0+h/2, window.height-h/2)
        return Rectangle(x, y, w, h)


class Square(Rectangle):  # квадрат
    def __init__(self, x, y, size):
        Rectangle.__init__(self, x, y, size, size)
        self.dx = 3
        self.dy = 2

    def draw(self):
        window.draw_rectangle((self.x - 0.5 * self.width, self.y - 0.5 * self.width), (self.width, self.width),
                              color='black')

    def top(self):
        return self.y - 0.5 * self.width

    def bottom(self):
        return self.top() + self.width

    def left(self):
        return self.x - 0.5 * self.width

    def right(self):
        return self.left() + self.width

    @classmethod
    def input(cls):
        w = int(input('Введите сторну квадрата: '))
        x = randint(0+w/2, window.width-w/2)
        y = randint(0+w/2, window.height-w/2)
        return Square(x, y, w)


class Circle(Shape):  # круг
    def __init__(self, x, y, radius):
        Shape.__init__(self, x, y)
        self.radius = radius
        self.size = (2 * self.radius, 2 * self.radius)
        self.dx = 1
        self.dy = 3

    def draw(self):
        window.draw_ellipse((self.x - self.radius, self.y - self.radius), self.size, color='red')

    def top(self):
        return self.y - self.radius

    def bottom(self):
        return self.y + self.radius

    def left(self):
        return self.x - self.radius

    def right(self):
        return self.x + self.radius

    @classmethod
    def input(cls):
        r = int(input('Введите радиус круга: '))
        x = randint(0+2*r, window.width-2*r)
        y = randint(0+2*r, window.height-2*r)
        return Circle(x, y, r)


class Triangle(Shape):  # равносторонний треугольник
    def __init__(self, x, y, height):
        Shape.__init__(self, x, y)
        self.height = height
        self.dx = 3
        self.dy = 1

    def draw(self):
        point1 = (self.x, self.y)
        point2 = (self.x - self.height / 2, self.y - self.height)
        point3 = (self.x + self.height / 2, self.y - self.height)
        window.draw_polygon(point1, point2, point3, color='yellow')

    def top(self):
        return self.y - self.height

    def bottom(self):
        return self.y

    def left(self):
        return self.x - self.height / 2

    def right(self):
        return self.x + self.height / 2

    @classmethod
    def input(cls):
        h = int(input('Введите сторону треугольника: '))
        x = randint(0+h, window.width-h)
        y = randint(0+h, window.height-h)
        return Triangle(x, y, h)


N = int(input('Введите количество фигур: '))
Shapes = [input(f'Введите название фигуры {i+1}: ') for i in range(N)]
Examples = []
for shape in Shapes:
    if shape == 'Прямоугольник':
        rect = Rectangle.input()
        Examples.append(rect)
    elif shape == "Квадрат":
        sq = Square.input()
        Examples.append(sq)
    elif shape == "Круг":
        cir = Circle.input()
        Examples.append(cir)
    elif shape == 'Треугольник':
        tr = Triangle.input()
        Examples.append(tr)

while not window.closed:
    start = time()
    window.clear()

    for example in Examples:
        example.x += example.dx
        example.y -= example.dy

        if example.right() > window.width:
            example.dx = -example.dx
        elif example.left() < 0:
            example.dx = -example.dx

        if example.top() < 0:
            example.dy = -example.dy
        elif example.bottom() > window.height:
            example.dy = -example.dy

        example.draw()

    window.update()

    pause = 1 / fps - (time() - start)
    if pause > 0:
        sleep(pause)
