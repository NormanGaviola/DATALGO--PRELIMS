"""Norman Raphael M. Gaviola

DATALOG Lab01
Feb. 19, 2020
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

if __name__ == '__main__':
    LS = int(input("Length of sides :"))
    NS = int(input("Number of sides :"))


