# public => memberName
# protected => _memberName
# private => __memberName

class Car:
    numberOfWheels = 4
    _color = "black"
    __year = 2018 #_Car__year

class Bmw(Car):
    def __init__(self):
        print("protected attribute color: ", self._color)

car = Car()
print("public attribute: ", car.numberOfWheels)
bmw = Bmw()
print("private attribute: year", car._Car__year)