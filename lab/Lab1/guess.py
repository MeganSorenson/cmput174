# Guess the Number
# randomly chooses a number between one and ten
# asks player to guess the number and states answer
# https://docs.python.org/3/library/random.html
import random

# display initial statement
print("I am thinking of a number between 1 and 10.")

# prompt player to guess a number
guess = input("What is the number?")

# randomly pick number between 1 and 10
answer = random.randint(1, 10)

# display the answer
print("The number was " + str(answer) + ".")

# display the player's guess
print("You guessed " + guess + ".")
