import copy

'''
    The Prototype design pattern is another creational pattern that is used to 
    create duplicate objects while maintaining performance. This pattern is particularly useful when creating 
    an instance of a class is complex or resource-intensive, but you need many similar instances of that class.
'''

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        # Registers an object that can be cloned.
        self._objects[name] = obj

    def unregister_object(self, name):
        # Removes an object from the registry.
        del self._objects[name]

    def clone(self, name, **attrs):
        # Clones a registered object and adds/changes its attributes.
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj

class MedicalEquipment:
    def __init__(self, name, settings):
        self.name = name
        self.settings = settings

    def __str__(self):
        return f'{self.name} with settings: {self.settings}'

prototype = Prototype()
prototype.register_object('ultrasound', MedicalEquipment('Ultrasound Machine', {'mode': 'B-mode', 'frequency': '3MHz'}))

ultrasound_default = prototype.clone('ultrasound')
ultrasound_cardiac = prototype.clone('ultrasound', settings={'mode': 'Doppler', 'frequency': '5MHz'})
ultrasound_abdominal = prototype.clone('ultrasound', settings={'mode': 'B-mode', 'frequency': '3.5MHz'})

print(ultrasound_default)
print(ultrasound_cardiac)
print(ultrasound_abdominal)
