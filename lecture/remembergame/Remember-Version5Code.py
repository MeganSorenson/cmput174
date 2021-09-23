# Remember the Word Design

# Version 1 Code - display, prompt, pause, restart
# Version 2 Code - clear, conditional feedback, identify and replace adjacent duplicate line grups with a for statement
# Version 3 Code - software quality requirement; identify any literals that occur more than once and bind to an identifer and replace literal with identifier, random selection of 4 words, randome selection of answer
# Version 4 Code - player can play the game multiple times
# Version 5 Code - identify non-adjacent duplicate line groups, define a function, place the linw group in the body of the function, replace all other occurences of line group with user defined function

# https://docs.python.org/3/library/time.htmlhttps://docs.python.org/3/library/time.html
# https://docs.python.org/3/library/os.html
# https://docs.python.org/3/library/random.html
import time
import os
import random


def display_header():
    # clears screen and displays header
    # returns None
    # clear screen
    clear_command = "clear"  # clear command for mac
    if os.name == 'nt':
        clear_command = 'cls'  # clear command for windows
    os.system(clear_command)
    # print header
    header_border = "-" * 80
    header_content = "Remember The Word"
    print(header_border)
    print(header_content)
    print(header_border)


def display_instructions():
    # displays instructions
    # returns None
    filename = "instructions.txt"
    filemode = "r"
    file = open(filename, filemode)
    instructions = file.read()
    file.close()
    print(instructions)


def choose_words():
    # samples 4 words randomly from a file
    # returns list
    filename = "words.txt"
    filemode = "r"
    file = open(filename, filemode)
    all_words = file.read()
    file.close()
    words = all_words.splitlines()
    four_words = random.sample(words, 4)
    return four_words


def display_words(four_words):
    # displays the four words
    # four_words is parameter type list
    # returns None
    pause_time = 1
    for word in four_words:
        print(word)
        time.sleep(pause_time)
        display_header()


def prompt_guess(first_letter):
    # prompt player to enter word thats starts with letter
    # returns string
    guess = input("What word starts with the letter " + first_letter + "?")
    return guess


def display_result(guess, answer):
    # evaluates result and displays the result
    # returns None
    if guess.lower() == answer.lower():
        # congratulations if correct
        print("Congratulations, you are correct.")
    else:
        # condolence if wrong
        print("Sorry you entered " + guess + ".")
    print("The answer was " + answer + ".")


def prompt_continue():
    # prompts the player to continue or not
    # returns bool
    reply = input("Play again? y/N").lower()
    continue_game = reply == "y"
    return continue_game


def main():
    continue_game = True
    while continue_game:
        display_header()
        display_instructions()

        # prompt player to press enter
        input("Press enter key to display the words.")
        display_header()

        # display 4 words
        #   displayed one at a time
        #   there is a 1 second pause before word disapears and next word appears
        #   words are different each time game is played
        #   words are chosen randomly from a list
        four_words = choose_words()
        answer = random.choice(four_words)
        first_letter = answer[0]
        display_words(four_words)

        # prompt player to enter word thats starts with letter
        #   answer is chosen randomly from 4 displayed words
        #   prompt is formulated using the first letter of the answer
        guess = prompt_guess(first_letter)

        # evaluate the answer and display feedback
        display_result(guess, answer)

        # prompt player to play again
        #   restarts if player chooses so
        #   or program terminates
        continue_game = prompt_continue()


main()
