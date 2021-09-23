# Coin Toss Game

# https://docs.python.org/3/library/random.html
import random


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
    playerone_wins = 0
    playertwo_wins = 0
    playerone_tosses = []
    playertwo_tosses = []
    for i in range(number_rounds):
        # prompt coin side input for answer
        answer = input("Heads or Tails ? Type H or T >").upper()
        # randomly toss coins for each player
        tosses = toss_coins()
        # print toss results and add results to player list
        toss_results(tosses)
        playerone_tosses.append(tosses[0])
        playertwo_tosses.append(tosses[1])
        # evaluate winner of toss and add to respective player win list
        coin_winner = toss_winner(tosses, answer)
        if coin_winner == "1":
            playerone_wins = playerone_wins + 1
        if coin_winner == "2":
            playertwo_wins = playertwo_wins + 1
        # display winner or end of round stats message
        if coin_winner != "":
            if i in range(number_rounds-1):
                print("Player " + coin_winner + " wins")
            else:
                print("ROUND STATS")

    # evaluate and display round winner
    if playerone_wins > playertwo_wins:
        print("Player 1 wins this round")
    elif playertwo_wins > playerone_wins:
        print("Player 2 wins this round")
    # display player points
    print("Player 1 points " + str(playerone_wins))
    print("Player 2 points " + str(playertwo_wins))
    # display player toss sequences
    print("Player 1 tossed ", playerone_tosses)
    print("Player 2 tossed ", playertwo_tosses)
    # determine and display HH occurence in player toss sequence
    playerone_hh = 0
    playertwo_hh = 0
    for i in range(len(playerone_tosses)):
        if playerone_tosses[i] == "H" and playerone_tosses[i + 1] == "H":
            playerone_hh = playerone_hh + 1
    for i in range(len(playerone_tosses)):
        if playertwo_tosses[i] == "H" and playertwo_tosses[i + 1] == "H":
            playertwo_hh = playertwo_hh + 1
    print("H H found in the player 1 sequence " + str(playerone_hh) + " times")
    print("H H found in the player 2 sequence " + str(playertwo_hh) + " times")


main()
