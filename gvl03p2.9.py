"""Norman Raphael M. Gaviola
   DATALOG Lab02
   Feb.9,2020 """
class Vector:


    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            try:  # testing if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')

    def __len__(self):

        return len(self._coords)

    def __getitem__(self, j):

        return self._coords[j]

    def __setitem__(self, j, val):

        self._coords[j] = val

    def __add__(self, other):

        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    

    def __str__(self):

        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation

if __name__ == '__main__':

    v = Vector(5)
    v[1] = 13
    v[-1] = 50
    print(v[4])
    u = v + v
    print(u)
    w = v - u
    print(w)
    total = 0
    for entry in v:
        total += entry