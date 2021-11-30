# Rock Paper Scissors
# a naive implementation
# rock smashes scissors, paper covers rock, scissors cut paper

import random


def main():
    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'
    choices = [rock, paper, scissors]

    computer_wins_message = 'I win!'
    player_wins_message = 'You win!'
    tie_message = "Tie!"

    computer_choice = random.choice(choices)
    print(computer_choice)
    player_choice = ''
    while player_choice not in choices:
        player_choice = input('What do you choose: ' +
                              ', '.join(choices) + '? > ')
    if player_choice == rock:
        if computer_choice == paper:
            print(computer_wins_message)
        elif computer_choice == scissors:
            print(player_wins_message)
        else:
            print(tie_message)

    if player_choice == scissors:
        if computer_choice == rock:
            print(computer_wins_message)
        elif computer_choice == paper:
            print(player_wins_message)
        else:
            print(tie_message)

    if player_choice == paper:
        if computer_choice == scissors:
            print(computer_wins_message)
        elif computer_choice == rock:
            print(player_wins_message)
        else:
            print(tie_message)


main()
