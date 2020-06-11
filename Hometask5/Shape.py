from Hometask5.Window import Window
from abc import abstractmethod
from time import *

window = Window(0, 0, 500, 500)


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
        return self.y

    def bottom(self):
        return self.y - self.height

    def left(self):
        return self.x - self.height / 2

    def right(self):
        return self.x + self.height / 2


rect = Rectangle(300, 400, 80, 50)
sq = Square(300, 400, 50)
cir = Circle(300, 400, 50)
tr = Triangle(300, 400, 100)

while not window.closed:
    start = time()
    window.clear()
    rect.x += rect.dx
    rect.y -= rect.dy
    sq.x += sq.dx
    sq.y -= sq.dy
    cir.x += cir.dx
    cir.y -= cir.dy
    tr.x += tr.dx
    tr.y -= tr.dy

    if rect.right() > window.width:
        rect.dx = -rect.dx
    elif rect.left() < 0:
        rect.dx = -rect.dx

    if rect.top() < 0:
        rect.dy = -rect.dy
    elif rect.bottom() > window.height:
        rect.dy = -rect.dy

    if sq.right() > window.width:
        sq.dx = -sq.dx
    elif sq.left() < 0:
        sq.dx = -sq.dx

    if sq.top() < 0:
        sq.dy = -sq.dy
    elif sq.bottom() > window.height:
        sq.dy = -sq.dy

    if cir.right() > window.width:
        cir.dx = -cir.dx
    elif cir.left() < 0:
        cir.dx = -cir.dx

    if cir.top() < 0:
        cir.dy = -cir.dy
    elif cir.bottom() > window.height:
        cir.dy = -cir.dy

    if tr.right() > window.width:
        tr.dx = -tr.dx
    elif tr.left() < 0:
        tr.dx = - tr.dx

    if tr.top() > window.height:
        tr.dy = -tr.dy
    elif tr.bottom() < 0:
        tr.dy = -tr.dy

    rect.draw()
    sq.draw()
    cir.draw()
    tr.draw()

    window.update()
