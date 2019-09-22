class Dog(object):
    def __init__(self, name, breed, greeting):
        self.name = name
        self.breed = breed
        self.greeting = greeting

    def bark(self):
        print("Barker, {}!".format(self.name))
        print("This is my dog Sitter, she loves to sit and she is a {}".format(self.breed) )
        print("This is my dog Roller and he always says {}".format(self.greeting))

import dog
from dog import dog

my_dog = Dog("Bark", "labradoodle", "woah!")
my_dog.bark()
