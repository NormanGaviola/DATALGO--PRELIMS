"""Norman Raphael M. Gaviola

DATALOG Lab01
Feb. 26, 2020
I have neither received nor provided any help on this (lab) activity, nor have I concealed any violation of the Honor Code."""

class Airplane:
    def __init__(self):
        self.speed = 0
    def set_speed(self, speed):
        self.speed = speed
    def get_speed(self):
        return self.speed

class Jet(Airplane):
    def __init__(self):
        self.multiplier = 2
    def set_speed(self, speed):
        super().set_speed(speed * self.multiplier)
    def accelerate(self):
        super().set_speed(self.set_speed() * 2)

class Flytest():
    biplane = Airplane()
    biplane.set_speed(212)
    print(biplane.set_speed)

    boeing = Jet()
    boeing.set_speed(424)
    print(boeing.set_speed)
    x = 1
    while x == 0:
        biplane.accelerate
        print( biplane.set_speed)
        if boeing.set_speed > 5000:
            boeing.accelerate(boeing.set_speed() * 2)
        else:
            boeing.get_speed()
            x += 1
        print(boeing.get_speed())
Flytest()
