import random


class Ability():
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    def attack(self):
        return random.randint(1, 60)
    
ability = Ability("Debugging Ability", 20)
print(ability.name)
print(ability.attack())
        

# class Armor():
#     def __init__(self, name, max_block):
#         self.name = name
#         self.max_block = max_block
#         pass
    
# class Hero():
#     def __init__(self, name, starting_health):
#         self.name = name
#         self.starting_health = starting_health
#         pass
