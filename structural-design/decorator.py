'''
    The Decorator design pattern is a structural pattern that allows you to add behaviors to individual objects, 
    extending their functionality without modifying the original class. This pattern is very useful for 
    dynamically and flexibly adding functionality to objects in systems where extending functionality through 
    inheritance would be impractical or would cause a very complex and burdensome class design.
'''


class Coffee:
    def cost(self):
        return 5
    def ingredients(self):
        return "Coffee"

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

    def ingredients(self):
        return self._coffee.ingredients() + ", Milk"

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

    def ingredients(self):
        return self._coffee.ingredients() + ", Sugar"


simple_coffee = Coffee()
print(f"Cost: {simple_coffee.cost()} - Ingredients: {simple_coffee.ingredients()}")

milk_coffee = MilkDecorator(simple_coffee)
print(f"Cost: {milk_coffee.cost()} - Ingredients: {milk_coffee.ingredients()}")

sugar_milk_coffee = SugarDecorator(milk_coffee)
print(f"Cost: {sugar_milk_coffee.cost()} - Ingredients: {sugar_milk_coffee.ingredients()}")

#           Output:
# Cost: 5 - Ingredients: Coffee
# Cost: 7 - Ingredients: Coffee, Milk
# Cost: 8 - Ingredients: Coffee, Milk, Sugar

