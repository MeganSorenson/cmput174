# a class definition characterizes thhe properties and the behaviour of a group of objects that are of a certain kind
import random


class Die:
    def __init__(self, sides, colour):
        # initializes the instance attributes (properties) of the object
        self.sides = sides
        self.colour = colour

    def roll(self):
        print(self.colour)
        return random.randint(1, self.sides)


def main():
    d6 = Die(6, "red")  # object is created, init method is called
    print(d6.roll())
    d8 = Die(8, "green")
    print(d8.roll())
    d12 = Die(12, "purple")
    print(d12.roll())


main()
