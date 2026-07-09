import math

class Point:
    # __init__ to konstruktor
    def __init__(self, x:int | float, y: int | float):
        self.x = x
        self.y = y
    

    # za pomocą @property i metody setter mogę wykonać walidacje wejścia

    @property # (getter) pobieramy dane
    def x(self): # x przekierowujemy do _x, od teraz x i _x są ze sobą połączone, _x 
        return self._x # _x to pusta przestrzeń, do której zostanie przypisana wartość, jeśli setter ją sprawdzi i wszystko będzie ok
    # (setter) modifikujemy / filtrujemy dane
    @x.setter # wywołuje metodę setter, czyli "bramkarza" który sprawdza x z property, jeśli spełnia wymagania to przypisuje wartość do _x, jeśli nie to podnosi błąd.
    def x(self, value):
        if not isinstance(value, (int,float)): # sprawdzamy value X
            raise TypeError("Współrzędna x musi być typu int lub float!")
        self._x = value # jeśli wszystko jest ok, to do _x zostaje przypisana wartość wejścia usera
         
    @property
    def y(self):
        return self._y 

    @y.setter
    def y(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError("Współrzędna y musi być typu int lub float!")
        self._y = value

    def __repr__(self):
        # _x i x są połączone, ale wedle zasad, nie wywołujemy rzeczy z podkreślikiem
        return f'POINT ({self.x}, {self.y})'

    def distance(self, pt):
            return float(math.dist((self.x, self.y), (pt.x, pt.y)))

    @classmethod
    def from_iterable(cls, iterable):
        coordinates = list(iterable)
        pass
    

p1 = Point(1, 2)
p2 = Point(2, "zeszyt")
print(p1.distance(p2))
print(p2)

#do aktualnej implementacji klasy point dopisz niezbedne walidacje wejścia
#napisz metodę klasy from_iterable - ktora utworzy instacnje klasy Point z obiektu iterowalnego 1D