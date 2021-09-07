# Remember the Word Design

# Version 1 Code - display, prompt, pause, restart

import time

# clear screen
# display header
print(80 * "-")
print("Remember The Word")
print(80 * "-")

# display instructions
filename = "instructions.txt"
filemode = "r"
file = open(filename, filemode)
instructions = file.read()
file.close()

print(instructions)

# prompt player to press enter
input("Press enter key to display the words.")

# clear screen
# display 4 words
#   displayed one at a time
#   there is a 1 second pause before word disapears and next word appears
#   words are differetn each time game is played
#   words are chosen randomly from a list
print("orange")
time.sleep(1)
print("chair")
time.sleep(1)
print("sandwich")
time.sleep(1)
print("chair")
time.sleep(1)

# prompt player to enter word thats starts with letter
#   answer is chosenn randomly from 4 displayed words
#   prompt is formulated using the first letter of the answer
guess = input("What word starts with the letter c?")

# evaluate the answer
# display feedback
#   congratulations if correct
#   condolence if wrong
print("Congratulations, you are correct.")
print("The answer was chair.")

print("Sorry you entered " + guess + ".")
print("The answer was chair.")

# prompt player to play again
#   restarts if player chooses so
#   or program terminates
reply = input("Play again? y/N")
