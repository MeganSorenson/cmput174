# Rock Paper Scissors Lizard Spock
# a naive implementation using dictionaries
# scissors wins against paper and lizard
# paper wins against rock and spock
# rock wins against lizard and scissors
# lizard wins against spock and paper
# spock wins against scissors and rock

import random


def main():
    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'
    lizard = 'lizard'
    spock = 'spock'
    choices = [rock, paper, scissors, lizard, spock]

    computer_wins_message = 'I win!'
    player_wins_message = 'You win!'
    tie_message = "Tie!"

    computer_choice = random.choice(choices)
    print(computer_choice)
    player_choice = ''
    while player_choice not in choices:
        player_choice = input('What do you choose: ' +
                              ', '.join(choices) + '? > ')

    rules = {scissors: [paper, lizard],
             paper: [rock, spock],
             rock: [lizard, scissors],
             lizard: [spock, paper],
             spock: [scissors, rock]}

    if computer_choice in rules[player_choice]:
        print(player_wins_message)
    elif player_choice in rules[computer_choice]:
        print(computer_wins_message)
    else:
        print(tie_message)


main()
