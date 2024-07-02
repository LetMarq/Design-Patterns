'''
    The Adapter design pattern is a structural pattern that allows interaction between incompatible interfaces. 
    This pattern is often used to make existing systems work together without changing their source code. 
    The Adapter works as an intermediary that translates calls between two systems with different interfaces.
'''

class Car:
    def accelerate(self):
        print("Car accelerating")

class Bicycle:
    def pedal(self):
        print("Bicycle pedaling")

class BicycleAdapter:
    def __init__(self, bicycle):
        self.bicycle = bicycle

    def accelerate(self): # -> Doesnt need to be the same as Car.accelerate
        self.bicycle.pedal()

# Client waiting for an object with accelerate method
def client_code(vehicle):
    vehicle.accelerate()

car = Car()
client_code(car)

# Adapting Bicycle to be used as a Car
bicycle = Bicycle()
bicycle_adapter = BicycleAdapter(bicycle)
client_code(bicycle_adapter)
