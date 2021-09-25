# Word Puzzle Game
# player randomly guesses letter of a mystery word chosen randomly from a list
# player co tinues to guess letters until they guess the word or run out of remaining guesses
# game ends after one round

# https://docs.python.org/3/library/random.html
import random


def display_instructions():
    # reads and displays instructions
    # returns None
    filename = "wp_instructions.txt"
    filemode = "r"
    file = open(filename, filemode)
    instructions = file.read()
    file.close()
    print(instructions)


def update_puzzle_state(letter_guess, answer, puzzle_state):
    # updates puzzle state based on letters guessed correctly
    # letter_guess is a string representing a letter that was inputted by the player
    # answer is a string representing a word that was randomly chosen from a list
    # puzzle_state is a list of strings representing the game state based on letters of the answer guessed correctly
    # returns list
    for i in range(len(answer)):
        if answer[i] == letter_guess:
            puzzle_state[i] = letter_guess
    return puzzle_state


def update_guesses_remaining(letter_guess, answer, puzzle_state, guesses_remaining):
    # updates the number of guesses that the player has left
    # letter_guess is a string representing a letter that was inputted by the player
    # answer is a string representing a word that was randomly chosen from a list
    # puzzle_state is a list of strings representing the game state based on letters of the answer guessed correctly
    # guesses_remaining is an int representing the total number of guesses the player has left
    # returns int
    if letter_guess not in answer or letter_guess in puzzle_state:
        guesses_remaining -= 1
    return guesses_remaining


def display_game_results(answer, puzzle_state, guesses_remaining):
    # displays game results after player has either correctly guessed the answer or run out of remaining guesses
    # answer is a string representing a word that was randomly chosen from a list
    # puzzle_state is a list of strings representing the game state based on letters of the answer guessed correctly
    # guesses_remaining is an int representing the total number of guesses the player has left
    # returns None
    print("The answer so far is " + " ".join(puzzle_state))
    if guesses_remaining == 0:
        print("Not quite, the correct word was " +
              answer + ". Better luck next time ")
    else:
        print("Good job! You found the word " + answer + "!")


def main():
    # choose answer randomly from a list of words
    word_list = ["apple", "banana", "watermelon", "kiwi", "pineapple", "mango"]
    answer = random.choice(word_list)
    # initial game state and guesses remaining for the player
    puzzle_state = ["_"] * len(answer)
    guesses_remaining = 4
    # display instructions
    display_instructions()
    # displays game state, prompts letter guess, and updates guesses remaining and game state until game ends
    while guesses_remaining > 0 and "_" in puzzle_state:
        # display current game state
        print("The answer so far is " + " ".join(puzzle_state))
        # prompt player to guess a letter and display how many guesses left
        letter_guess = input(
            "Guess a letter (" + str(guesses_remaining) + " guesses remaining): ")
        # update guesses remaining
        guesses_remaining = update_guesses_remaining(
            letter_guess, answer, puzzle_state, guesses_remaining)
        # update game state
        puzzle_state = update_puzzle_state(letter_guess, answer, puzzle_state)
    # display end of game results
    display_game_results(answer, puzzle_state, guesses_remaining)
    # prompt player to end game
    input("Press enter to end the game. ")


main()
