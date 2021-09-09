# Remember the Word Design

# Version 1 Code - display, prompt, pause, restart
# Version 2 Code - clear, conditional feedback, identify and replace adjacent duplicate line grups with a for statement

# https://docs.python.org/3/library/time.htmlhttps://docs.python.org/3/library/time.html
# https://docs.python.org/3/library/os.html
import time
import os

# clear screen
clear_command = "clear"  # clear command for mac
if os.name == 'nt':
    clear_command = 'cls'  # clear command for windows
os.system(clear_command)

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

# clear screens
os.system(clear_command)
print(80 * "-")
print("Remember The Word")
print(80 * "-")

# display 4 words
#   displayed one at a time
#   there is a 1 second pause before word disapears and next word appears
#   words are differetn each time game is played
#   words are chosen randomly from a list
words = ["orange", "chair", "sandwich", "mouse"]

for word in words:
    print(word)
    time.sleep(1)
    os.system(clear_command)
    # display header
    print(80 * "-")
    print("Remember The Word")
    print(80 * "-")

# prompt player to enter word thats starts with letter
#   answer is chosenn randomly from 4 displayed words
#   prompt is formulated using the first letter of the answer
guess = input("What word starts with the letter c?")

# evaluate the answer and display feedback
if guess == "chair" or guess == "CHAIR":
    # congratulations if correct
    print("Congratulations, you are correct.")
elif guess == "chairs" or guess == "CHAIRS":
    print("Almost correct.")
else:
    # condolence if wrong
    print("Sorry you entered " + guess + ".")
    if len(guess) > len("chair"):
        print("Too many characters.")
    else:
        print("Not enough characters.")

print("The answer was chair.")

# prompt player to play again
#   restarts if player chooses so
#   or program terminates
reply = input("Play again? y/N")
