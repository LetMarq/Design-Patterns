'''
    Composite is a structural design pattern that allows you to compose objects into tree 
    structures and then work with those structures as if they were individual objects.
'''

class Graphic:
    def draw(self):
        raise NotImplementedError("You should implement this method (Draw)!")

class Circle(Graphic):
    def draw(self):
        print("~ Drawing a circle ~")

class Square(Graphic):
    def draw(self):
        print("~ Drawing a square ~")

class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def draw(self):
        for graphic in self.graphics:
            graphic.draw()

    def add(self, graphic):
        self.graphics.append(graphic)

    def remove(self, graphic):
        self.graphics.remove(graphic)

circle = Circle()
square = Square()
composite = CompositeGraphic()
composite.add(circle)
composite.add(square)

composite.draw()
