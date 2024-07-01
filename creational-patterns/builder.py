'''
    The Builder design pattern is a creational pattern that allows you to build complex objects step by step. 
    It is used when the construction of an object involves more than simply initializing fields,
    especially when many steps are involved in creating an object. One of the main advantages of the Builder 
    pattern is that it allows the internal construction processes of an object to vary between different representations.
'''

class Car:
    def __init__(self):
        self.color = None
        self.wheels = 0
        self.engine = None

    def __str__(self):
        return f'Car with {self.color} color, {self.wheels} wheels, and {self.engine} engine.'

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_color(self, color):
        self.car.color = color
        return self

    def set_wheels(self, wheels):
        self.car.wheels = wheels
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def build(self):
        return self.car

class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct_sports_car(self):
        self._builder.set_color('Red').set_wheels(4).set_engine('V8')
        return self._builder.build()

    def construct_family_car(self):
        self._builder.set_color('Blue').set_wheels(4).set_engine('V6')
        return self._builder.build()

builder = CarBuilder()
director = Director(builder)

sports_car = director.construct_sports_car()
family_car = director.construct_family_car()

print(sports_car)
print(family_car)
