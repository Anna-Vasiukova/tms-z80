from Hometask5.Window import Window

window = Window(100, 100, 800, 600)


class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.point = (self.x, self.y)


    # def draw(self):
    #
    #
    # def top(self) -> float:
    #           # верхняя граница
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
        self.size = (2*self.radius, 2*self.radius)
        window.draw_ellipse(self.point, self.size, color='red')


class Triangle(Shape):  # равносторонний треугольник
    def __init__(self, x, y, height):
        Shape.__init__(self, x, y)
        self.height = (self.x + height, self.y + height)
        size = (*self.point, *self.height)
        window.draw_polygon(size, color='black')


while not window.closed:
    # a = Rectangle(300, 400, 200, 100)
    # b = Square(200, 500, 100)
    # c = Circle(400, 100, 100)
    d = Triangle(300, 400, 100)
    window.update()


