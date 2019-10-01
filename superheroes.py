import random

class Ability():
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)

class Weapon(Ability):
    def attack(self):
        return random.randint(1/2, self.max_damage)

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
        self.kills = []
        self.deaths = []

    def add_kills(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total = 0
        for force in self.abilities:
            total += int(force.max_damage)
        return total

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt=0):
        sum = 0
        for armor in self.armors:
            num = armor.defend() 
            sum += num
        return sum + damage_amt

    def take_damage(self, damage):
        call_defend = self.defend(damage)
        self.current_health = self.current_health - call_defend
        
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
                self.add_deaths(1)

            else:
                print(self.name + " defeated " + opponent.name)
                self.add_kills(1)
                break

            if opponent.is_alive():
                damage = opponent.attack()
                self.take_damage(damage)
                print(self.name + " attacked " + opponent.name)
                opponent.add_deaths(1)
            else:
                print(opponent.name + " defeated " + self.name)
                opponent.add_kills(1)
                break

    def add_weapon(self, weapon):
        self.add_ability(weapon)

class Team(object):
    def __init__(self, name, health = 100):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        for hero in self.heroes:
            self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            hero.calculate_hero_stats()

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            self.current_health = 100
        return hero

    def is_all_dead(self):
        all_heroes_dead = False

        for hero in self.heroes:
            if hero.is_alive():
                all_heroes_dead = True
                
            return all_heroes_dead

    def get_random_hero(self):
        return self.heroes[random.randint(0, len(self.heroes)- 1)]

    def attack(self, other_team):
        while self.is_all_dead() and other_team.is_all_dead():
            random_hero = self.get_random_hero()
            teams_hero = other_team.get_random_hero()
            if random_hero.is_alive() or teams_hero.is_alive():
                random_hero.fight(teams_hero)
            else:
                random_hero = self.get_random_hero()
                teams_hero = other_team.get_random_hero()

class Arena:
    def __init__(self):
        self.team_one = Team('Team one')
        self.team_two = Team('Team two')

    def create_ability(self):
        ability_name = input("Ability name: ")
        ability_damage = int(input("Ability damage: "))
        return Ability(ability_name, ability_damage)
    
    def create_weapon(self):
        weapon_name = input("Weapon name: ")
        weapon_damage = int(input("Weapon damage: "))
        return Weapon(weapon_name, weapon_damage)

    def create_armor(self):
        armor_name = input("Armor name: ")
        armor_num = int(input("Armor Amount: "))
        return Armor(armor_name, armor_num)

    def create_hero(self):
        hero_name = input("Hero name: ")
        hero_health = int(input("Hero starting health: "))
        new_hero = Hero(hero_name, hero_health)
        num_abilities = int(input("Number of desired abilities to add:"))
        for i in range(0, num_abilities):
            new_hero.add_ability(self.create_ability())
        num_weapons = int(input("Number of desired weapons to add:"))
        for i in range(0, num_weapons):
            new_hero.add_weapon(self.create_weapon())
        num_armor = int(input("Number of desired armors to add:"))
        for i in range(0, num_armor):
            new_hero.add_armor(self.create_armor())
            print(i)
        return new_hero

    def build_team_one(self):
        team_name = input("Enter a team name:")
        num_heroes = int(input("Enter number of heroes:"))
        self.team_one = Team(team_name)

        for i in range (0, num_heroes):
            self.team_one.heroes.append(self.create_hero())
        return i

    def build_team_two(self):
        team_name = input("Enter another team name: ")
        num_heroes = int(input("Enter number of heroes: "))
        self.team_two = Team(team_name)

        for i in range (0, num_heroes):
            self.team_two.heroes.append(self.create_hero())
        return i

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print(self.team_battle())

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()