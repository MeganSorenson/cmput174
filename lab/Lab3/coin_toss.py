# Coin Toss Game
# randomly tosses a coin for two computer players
# players win by their coin landing on a user pre-decided coin face
# after 4 tosses a round winner is decided and the game can be replayed

# https://docs.python.org/3/library/random.html
import random


def instructions():
    # reads and displays instructions
    # returns None
    # read instruction file
    filename = "instructions.txt"
    filemode = "r"
    file = open(filename, filemode)
    instructions = file.read()
    file.close()
    # display instructions
    print(instructions)


def toss_coins():
    # randomly tosses two coins
    # returns list of toss results (H/T)
    tosses = []
    coin_sides = ["H", "T"]
    number_players = 2
    # toss 2 coins randomly
    for i in range(number_players):
        side = random.choice(coin_sides)
        tosses.append(side)
    return tosses


def toss_results(tosses):
    # displays coin toss results
    # tosses is a list of 2 str items with the H/T toss results
    # returns None
    print("Player 1 has tossed " + tosses[0])
    print("Player 2 has tossed " + tosses[1])


def toss_winner(tosses, answer):
    # evaluates winner(s)
    # tosses is a list of 2 str items with the H/T toss results
    # answer is  a str (H/T) determined by user input that the tosses will be compared to
    # returns list of winners
    winner = []
    if tosses[0] == answer:
        winner.append("1")
    if tosses[1] == answer:
        winner.append("2")
    return winner


def hh_occurence(player_tosses, player_number):
    # determine and display H H occurence in player toss sequences
    # player_tosses is an list of length 4 with H/T sequences from 4 random coin flips for a player
    # player_number is an integer explaining which player the toss list is provided for
    # returns None
    player_hh = 0
    # determine H H occurence
    i = 0
    while i < len(player_tosses) - 1:
        if player_tosses[i] == "H" and player_tosses[i + 1] == "H":
            player_hh += 1
        i = i + 1
    # displays results
    print("H H found in the player " + str(player_number) +
          " sequence " + str(player_hh) + " times")


def main():
    # main game flow of coin toss game
    # initial game stats records
    play = True
    total_playeronewins = 0
    total_playertwowins = 0
    total_playerties = 0

    # display instructions
    instructions()

    while play:
        # initial round stats records
        number_rounds = 4
        playerone_wins = 0
        playertwo_wins = 0
        playerone_tosses = []
        playertwo_tosses = []
        # toss coins for each player, display results, display winner
        for i in range(number_rounds):
            # prompt coin side input for answer
            answer = input("Heads or Tails ? Type H or T >").upper()
            # randomly toss coins for each player
            tosses = toss_coins()
            # display toss results
            toss_results(tosses)
            # add results to player round records
            playerone_tosses.append(tosses[0])
            playertwo_tosses.append(tosses[1])

            # evaluate winner(s)
            coin_winner = toss_winner(tosses, answer)
            # add to appropriate player round records and display winner(s)
            i = 0
            while i < len(coin_winner):
                if coin_winner[i] == "1":
                    playerone_wins += 1
                    print("Player 1 wins")
                elif coin_winner[i] == "2":
                    playertwo_wins += 1
                    print("Player 2 wins")
                i = i + 1

        # round stats after 4 tosses
        print("ROUND STATS")
        # evaluate and display round winnerand add result to game records
        if playerone_wins > playertwo_wins:
            print("Player 1 wins this round")
            total_playeronewins += 1
        elif playertwo_wins > playerone_wins:
            print("Player 2 wins this round")
            total_playertwowins += 1
        else:
            total_playerties += 1
        # display player points for round
        print("Player 1 points " + str(playerone_wins))
        print("Player 2 points " + str(playertwo_wins))
        # display player toss sequences for round
        print("Player 1 tossed ", playerone_tosses)
        print("Player 2 tossed ", playertwo_tosses)
        # determine and display H H occurence in player toss sequences
        hh_occurence(playerone_tosses, 1)
        hh_occurence(playertwo_tosses, 2)

        # ask to replay
        replay = input("Do you want to play another round? y/n >").lower()
        play = replay == "y"

    # display overall round summary stats after player quits game
    print("SUMMARY STATS")
    print("numer of ties " + str(total_playerties))
    print("number of player 1 wins " + str(total_playeronewins))
    print("number of player 2 wins " + str(total_playertwowins))


main()
