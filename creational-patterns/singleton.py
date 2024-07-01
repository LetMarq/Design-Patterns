'''
    The Singleton design pattern is a creational pattern that ensures that a class has only one instance, 
    while providing a global access point to that instance. It is commonly used in situations where 
    centralized control of resources or information is required, such as in system configurations, 
    database connections, or log file management.
'''

class AppConfig:
    _instance = None  # Private attribute to store the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppConfig, cls).__new__(cls)
            # Initialize any attribute of your instance here
            cls._instance.configuration = {}
        return cls._instance # If alreayd has an instance -> just return the old one

    def set_config(self, key, value):
        self.configuration[key] = value

    def get_config(self, key):
        return self.configuration.get(key)

# Using the Singleton pattern
config1 = AppConfig()
config2 = AppConfig()

config1.set_config('theme', 'Dark Mode')
config1.set_config('language', 'English')

print(config2.get_config('theme'))  # Output: Dark Mode
print(config2.get_config('language'))  # Output: English

# Checking if both instances are the same
print(config1 is config2)  # Output: True
