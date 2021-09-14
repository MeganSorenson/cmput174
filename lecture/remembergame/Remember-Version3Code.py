# Remember the Word Design

# Version 1 Code - display, prompt, pause, restart
# Version 2 Code - clear, conditional feedback, identify and replace adjacent duplicate line grups with a for statement
# Version 3 Code - software quality requirement; identify any literals that occur more than once and bind to an identifer and replace literal with identifier

# https://docs.python.org/3/library/time.htmlhttps://docs.python.org/3/library/time.html
# https://docs.python.org/3/library/os.html
# https://docs.python.org/3/library/random.html
import time
import os
import random

# clear screen
clear_command = "clear"  # clear command for mac
if os.name == 'nt':
    clear_command = 'cls'  # clear command for windows
os.system(clear_command)

# display header
header_border = "-" * 80
header_content = "Remember The Word"
print(header_border)
print(header_content)
print(header_border)

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
print(header_border)
print(header_content)
print(header_border)

# display 4 words
#   displayed one at a time
#   there is a 1 second pause before word disapears and next word appears
#   words are differetn each time game is played
#   words are chosen randomly from a list
filename = "words.txt"
filemode = "r"
file = open(filename, filemode)
all_words = file.read()
file.close()
words = all_words.splitlines()
four_words = random.sample(words, 4)

pause_time = 1

answer = random.choice(four_words)
first_letter = answer[0]

for word in four_words:
    print(word)
    time.sleep(pause_time)
    os.system(clear_command)
    # display header
    print(header_border)
    print(header_content)
    print(header_border)

# prompt player to enter word thats starts with letter
#   answer is chosenn randomly from 4 displayed words
#   prompt is formulated using the first letter of the answer
guess = input("What word starts with the letter " + first_letter + "?")

# evaluate the answer and display feedback
if guess.lower() == answer.lower():
    # congratulations if correct
    print("Congratulations, you are correct.")
else:
    # condolence if wrong
    print("Sorry you entered " + guess + ".")

print("The answer was " + answer + ".")

# prompt player to play again
#   restarts if player chooses so
#   or program terminates
reply = input("Play again? y/N")
