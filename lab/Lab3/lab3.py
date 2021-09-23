# Coin Toss Game

# https://docs.python.org/3/library/random.html
import random
# https://docs.python.org/3/library/statistics.html
import statistics


def instructions():
    # reads instruction file and print instructions
    # returns None
    # read instruction file
    filename = "instructions.txt"
    filemode = "r"
    file = open(filename, filemode)
    instructions = file.read()
    file.close()
    # print instructions
    print(instructions)


def toss_coins():
    # randomly tosses two coins
    # returns list
    tosses = []
    coin_sides = ["H", "T"]
    number_players = 2
    # toss coins
    for i in range(number_players):
        side = random.choice(coin_sides)
        tosses.append(side)
    return tosses


def toss_results(tosses):
    # prints coin toss results
    # returns None
    print("Player 1 has tossed " + tosses[0])
    print("Player 2 has tossed " + tosses[1])


def toss_winner(tosses, answer):
    # evaluates winner
    # returns string
    winner = ""
    if tosses[0] == answer:
        winner = "1"
    if tosses[1] == answer:
        winner = "2"
    return winner


def main():
    # print instructions
    instructions()

    # prompt for coin side answer

    # toss coins for each player, display results, display winner
    number_rounds = 4
    toss_winners = []
    for i in range(number_rounds):
        # prompt coin side input for answer
        answer = input("Heads or Tails ? Type H or T >").upper()
        # randomly toss coins for each player
        tosses = toss_coins()
        # print toss results
        toss_results(tosses)
        # evaluate winner of toss and ass to list of winners
        coin_winner = toss_winner(tosses, answer)
        toss_winners.append(coin_winner)
        # display winner or end of round stats message
        if i in range(number_rounds-1):
            print("Player " + coin_winner + " wins")
        else:
            print("ROUND STATS")
    round_winner = statistics.multimode(toss_winners)

    if len(round_winner) > 1:
        print("Players tied this round")
    else:
        print("Player " + round_winner[0] + " won this round")


main()
