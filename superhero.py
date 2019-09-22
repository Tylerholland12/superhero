import random

class Ability():
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    def attack(self):
        return random.randint(0, self.max_damage)
    
ability = Ability("Debugging Ability", 35)
print(ability.name)
print(ability.attack())

class Armor():
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def defend(self):
        return random.randint(0, self.max_block)

defense_ability = Armor("Shield", 34)
print(defense_ability.name)
print(defense_ability.defend())
        
    
class Hero():
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.abilities = []
        self.armors = []
        self.current_health = starting_health
    def add_ability(self, ability):
        self.abilities.append("joust")
        

my_hero = Hero("Interdimensionoid", 200)
print(my_hero.name)
print(my_hero.current_health)
ability = Ability("Great Debugging", 50)
hero = Hero("Grace Hopper", 200)
hero.add_ability(ability)
print(hero.abilities)