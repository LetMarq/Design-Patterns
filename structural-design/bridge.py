'''
    O padrão de projeto Bridge é um padrão estrutural que visa separar uma abstração de sua implementação, 
    permitindo que ambos variem independentemente. Esse padrão é especialmente útil quando você 
    deseja desacoplar uma interface de sua implementação para que eles possam ser desenvolvidos, 
    estendidos e operados separadamente.
'''

# Implement
class Device:
    def is_enabled(self): pass
    def enable(self): pass
    def disable(self): pass
    def get_volume(self): pass
    def set_volume(self, percent): pass

# Concrete implement
class Tv(Device):
    def __init__(self):
        self.on = False
        self.volume = 10

    def is_enabled(self):
        return self.on

    def enable(self):
        self.on = True

    def disable(self):
        self.on = False

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        self.volume = percent

# Implementador Concreto para Rádio
class Radio(Device):
    def __init__(self):
        self.on = False
        self.volume = 20

    def is_enabled(self):
        return self.on

    def enable(self):
        self.on = True

    def disable(self):
        self.on = False

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        self.volume = percent

# Abstraction
class RemoteControl:
    def __init__(self, device):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 10)

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 10)

tv = Tv()
remote = RemoteControl(tv)
remote.toggle_power()  # Turn Tv on
remote.volume_up()  # Turn Tv volume
