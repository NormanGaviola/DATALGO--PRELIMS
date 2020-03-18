"""Norman Raphael M. Gaviola

DATALOG Lab01
Feb. 12, 2020
I have neither received nor provided any help on this (lab) activity, nor have I concealed any violation of the Honor Code."""

from abc import ABC, abstractmethod
class Polygon(ABC):

    def __init__(self,LS):
        self.NS = len(LS)
        self.LS = [0] * self.NS
        self.assign_values_to_sides(LS)

    def print_num_sides(self):

        print('There are ' + str(self.NS) + 'sides.')

    def assign_values_to_sides(self, LS):
        index = 0
        while index < len(LS):
            self.LS[index] = LS[index]
            index += 1

    @abstractmethod
    def area(self):         #Return the area of the polygon

        return

    @abstractmethod
    def perimeter(self):            #Return the perimeter of the polygon

        return


class Triangle(Polygon):

    def __init__(self, LS):
        super().__init__(LS)
        Polygon.__init__(self, 3, LS)

    def area(self):         #return the area of the triangle using the semi-perimeter method

        a, b, c = self.LS
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def perimeter(self):            #Return the perimeter of the polygon

        # calculate the perimeter
        s = (self.LS[0] + self.LS[1] + self.LS[2])
        return s


class IsoscelesTriangle(Triangle):

    def __init__(self, side, base):  # [side, base]
        super().__init__([side, side, base])


class EquilateralTriangle(Triangle):

    def __init__(self, side):  # side
        super().__init__([side, side, side])


class Pentagon(Polygon):

    def __init__(self, LS):
        super().__init__(LS)
        assert 5, self.NS

    def area(self):
        x, y = self.LS[0], self.LS[1]
        return x * y

    def perimeter(self):            #Return the perimeter of the polygon

        # calculate the perimeter
        x, y = self.LS
        return (x + y) * 2


class Hexagon(Polygon):

    def __init__(self, LS):
        super().__init__(LS)
        assert 6, self.NS

    def area(self):
        x, y = self.LS[0], self.LS[1]
        return x * y

    def perimeter(self):            #Return the perimeter of the polygon

        # calculate the perimeter
        x, y = self.LS
        return (x + y) * 2


class Octagon(Polygon):

    def __init__(self, LS):
        super().__init__(LS)
        assert 8, self.NS

    def area(self):
        x, y = self.LS[0], self.LS[1]
        return x * y

    def perimeter(self):            #Return the perimeter of the polygon

        # calculate the perimeter
        x, y = self.LS
        return (x + y) * 2


class Quadrilateral(Polygon):

    def __init__(self, LS):  # [side1, side2]
        super().__init__([LS[0], LS[1], LS[0], LS[1]])
        assert 4, self.NS

    def area(self):
        x, y = self.LS[0], self.LS[1]
        return x * y

    def perimeter(self):        #Return the perimeter of the polygon

        # calculate the perimeter
        x, y = self.LS
        return (x + y) * 2


class Rectangle(Quadrilateral):

    def __init__(self, LS):  # [side1, side2]
        super().__init__(LS)

    def area(self):
        x, y = self.LS[0], self.LS[1]
        return x * y

    def perimeter(self):            #Return the perimeter of the polygon

        # calculate the perimeter
        x, y = self.LS
        return (x + y) * 2


class Square(Rectangle):

    def __init__(self, side):
        super().__init__([side, side])

    def area(self):
        x = self.LS[0]
        return x * x

    def perimeter(self):            #Return the perimeter of the polygon

        # calculate the perimeter
        x = self.LS [0]
        return x * 4

if __name__ == '__main__':
    a = Triangle(3)