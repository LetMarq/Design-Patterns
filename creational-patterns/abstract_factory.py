from abc import ABC, abstractmethod

'''
    The Abstract Factory design pattern is a creation pattern that allows you to create families of related objects 
    without specifying their concrete classes. This pattern is particularly useful for systems that need to be independent 
    of how their products are created, composed, and represented. It promotes consistency between products 
    and is often used when there are several possible variations of a product or when these products must be used together.
'''

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Concrete Products
class WinButton:
    def paint(self):
        print("Render a button in a Windows style")

class WinCheckbox:
    def paint(self):
        print("Render a checkbox in a Windows style")

class MacButton:
    def paint(self):
        print("Render a button in a macOS style")

class MacCheckbox:
    def paint(self):
        print("Render a checkbox in a macOS style")

class LinuxButton:
    def paint(self):
        print("Render a button in a macOS style")

class LinuxCheckbox:
    def paint(self):
        print("Render a checkbox in a macOS style")

# Concrete Factories
class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()

    def create_checkbox(self):
        return LinuxCheckbox()


# Client code
def application(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.paint()
    checkbox.paint()

# Usage
current_os = "Windows"
if current_os == "Windows":
    factory = WinFactory()
elif current_os == "Mac":
    factory = MacFactory()
else:
    factory = LinuxFactory()


application(factory)
