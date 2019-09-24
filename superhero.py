import random

class Ability():
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    def attack(self):
        return random.randint(0, self.max_damage)
    
ability = Ability("Debugging Ability", 35)
# print(ability.name)
# print(ability.attack())
another_ability = Ability("Smarty Pants", 50)
# print(another_ability.name)
# print(another_ability.attack)

class Armor():
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def defend(self):
        return random.randint(0, self.max_block)

defense_ability = Armor("Shield", 34)
# print(defense_ability.name)
# print(defense_ability.defend())

class Hero():
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.abilities = []
        self.armors = []
        self.current_health = starting_health

    def add_ability(self, ability):
        # self.add_ability = []
        self.abilities.append("decode")
        self.abilities.append("code faster")

    def attack(self):
        total_damage = self.starting_health - ability.attack() + defense_ability.defend()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt):
        sum = 0
        for armor in self.armors:
            num = armor.defend() 
            sum = num + sum
        return sum

    def take_damage(self, damage):
        self.current_health = damage - defense_ability

my_hero = Hero("Interdimensionoid", 200)
my_hero.add_ability(ability)

# print(my_hero.name)
# print(my_hero.current_health)

my_hero.add_ability(another_ability)
print(my_hero.attack())
