from abc import ABCMeta, abstractmethod
import math


class Shape(metaclass=ABCMeta):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass


class Circle(Shape):

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r * self.r


class Rectangle(Shape):

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def perimeter(self):
        return abs(self.x2 - self.x1) * 2 + abs(self.y2 - self.y1) * 2

    def square(self):
        return abs(self.x2 - self.x1) * abs(self.y2 - self.y1)


if __name__ == '__main__':
    c = Circle(0, 0, 1)
    print(c.perimeter(), c.square())
    r = Rectangle(0, 0, 2, 3)