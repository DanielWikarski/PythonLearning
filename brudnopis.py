import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'POINT ({self.x}, {self.y})'

    def distance(self, pt) -> float:
        return math.dist((self.x, self.y), (pt.x, pt.y))


p1 = Point(1, 2)
p2 = Point(3, 'zeszyt')
print(p1.distance(p2))

#do aktualnej implementacji klasy point dopisz niezbedne walidacje wejścia
#napisz metodę klasy from_iterable - ktora utworzy instacnje klasy Point z obiektu iterowalnego 1D