import random

class Ability():
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    def attack(self):
        return random.randint(0, self.max_damage)

class Armor():
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def defend(self):
        return random.randint(0, self.max_block)

class Hero():
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.abilities = []
        self.armors = []
        self.current_health = self.starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total = 0
        for force in self.abilities:
            total += int(force.max_damage)
        return total

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt):
        sum = 0
        for armor in self.armors:
            num = armor.defend() 
            sum = num + sum
        return sum

    def take_damage(self, damage):
        call_defend = self.defend(damage)
        self.current_health - call_defend
        
    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):

        while True:
        
            if self.is_alive():
                damage = self.attack()
                opponent.take_damage(damage)
                print(opponent.name + " attacked " + self.name)
            else:
                print(self.name + " defeated " + opponent.name)
                break
            
            if opponent.is_alive():
                damage = opponent.attack()
                self.take_damage(damage)
                print(self.name + " attacked " + opponent.name)
            else:
                print(opponent.name + " defeated " + self.name)
                
        else:
            return False

       
hero1 = Hero("Interdimensionoid")
hero2 = Hero("Surfire")
ability1 = Ability("Teleporting Kick", 300)
ability2 = Ability("Interdimensional Sweep", 130)
ability3 = Ability("Fire Wind", 80)
ability4 = Ability("Wizard Beard", 20)
hero1.add_ability(ability1)
hero1.add_ability(ability2)
hero2.add_ability(ability3)
hero2.add_ability(ability4)
hero1.fight(hero2)


# my_hero = Hero("Interdimensionoid", 200)
# my_hero.add_ability(ability)

# # print(my_hero.name)
# print(my_hero.current_health)

# my_hero.add_ability(another_ability)
# # print(my_hero.attack())

# print(my_hero.is_alive)