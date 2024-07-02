'''
    The Flyweight design pattern is a structural pattern that focuses on reducing the memory usage of an application.
    It achieves this by sharing as much data as possible between similar objects; 
    that is, it tries to reuse existing objects instead of creating new ones whenever possible.
'''

class CharacterFlyweight:
    def __init__(self, health, weapon):
        self.health = health  # Shared state
        self.weapon = weapon  # Shared state

class CharacterFactory:
    _characters = {}

    def get_character(character_type):
        if character_type not in CharacterFactory._characters:
            if character_type == "Sniper":
                CharacterFactory._characters[character_type] = CharacterFlyweight(100, "Sniper Rifle")
            elif character_type == "Soldier":
                CharacterFactory._characters[character_type] = CharacterFlyweight(150, "Assault Rifle")
        return CharacterFactory._characters[character_type]

class Player:
    def __init__(self, name, character_type):
        self.name = name
        self.character = CharacterFactory.get_character(character_type)
        self.position = (0, 0)
        self.current_health = self.character.health

    def move(self, x, y):
        self.position = (x, y)

    def display(self):
        print(f"{self.name} playing as {self.character.weapon} at position {self.position}")

# Criando jogadores
player1 = Player("Alice", "Sniper")
player2 = Player("Bob", "Sniper")
player3 = Player("Charlie", "Soldier")

# Movendo jogadores
player1.move(100, 200)
player2.move(150, 225)
player3.move(200, 250)

# Mostrando jogadores
player1.display()
player2.display()
player3.display()

print(player1.character is player2.character)  # Output: True
