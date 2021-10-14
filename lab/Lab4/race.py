# Two Player Racing Game
# each player rolls a 6-sided die and moves forward in a lane based on the value of the die
# in order to win the game, a player must move their game piece exactly onto the last position

# https://docs.python.org/3/library/random.html
import random


def roll_die(active_player):
    # rolling the die
    # ask for player input to roll
    # randomly chooses integer from 1 to 6 and displays roll result
    # active player is a string used to indicate which player is rolling
    # returns integer roll representing die result of the active player
    input("Player " + active_player + " press enter to roll!")
    roll = random.randint(1, 6)
    print("Player " + active_player + " rolled a " + str(roll))

    return roll


def display_state(active_player, opponent_player, player_positions):
    # changes/draws position of each player's token in race lane
    # displays lane state as a one-line text
    # active_player is a str indicating who the active player of this turn is
    # opponent_player is a str indicating who the opponent player of this turn is
    # player_positions is a list of two integers with the current player positions [x, o]
    # return NoneType

    lane = ["-"] * 8

    # determine who is the active player for indexing player position list
    if active_player == "x":
        i_active = 0
        i_opponent = 1
    else:
        i_active = 1
        i_opponent = 0

    # place token for each player
    lane[player_positions[i_active]] = active_player
    lane[player_positions[i_opponent]] = opponent_player

    # condition for start of game when both tokens at same spot on lane
    if player_positions[i_active] == player_positions[i_opponent]:
        lane[player_positions[i_active]] = "*"

    # display result
    print("update: " + " ".join(lane))


def update_position(active_player, player_positions, roll):
    # updating position of player after die has been rolled
    # active_player is a str indicating who the active player of the turn is (moving from roll)
    # opponent_player is a str indicating who the opponent player of the turn is (not moving from roll)
    # roll is an integer representing the amount of lane spaces the active player will move
    # returns list of 2 integers representing player position indexes [x, o]

    # determine who is active player for indexing player positions list
    if active_player == "x":
        i_active = 0
        i_opponent = 1
    else:
        i_active = 1
        i_opponent = 0

    # condition if player moves off of race lane
    if player_positions[i_active] + roll > 7:
        print("The roll was too high, player " +
              active_player + " stays in this position")
    # opponentwise move player position by roll value
    else:
        player_positions[i_active] += roll

    # condition after moving
    # if active player lands on opponent player, send opponent player back to start
    if player_positions[i_active] == player_positions[i_opponent]:
        player_positions[i_opponent] = 0
        print(str(active_player) + " kicked the rival!")

    return player_positions


def check_game_over(player_positions, game_over):
    # checking if player has won/ if active player has reached the last position or not
    # player_positions is a list of two integers representing the lane positions of each player [x, o]
    # game_over is a bool representing if a player has won or not
    # returns bool that represent game over state
    if player_positions[0] == 7 or player_positions[1] == 7:
        game_over = True

    return game_over


def opponent(active_player, opponent_player):
    # change turn after each move by returning the opponent of a given player
    # active_player is a str representing who the current active player is
    # opponent_player is a str representing who the current opponent player is
    # returns two strings, each representing the new active and opponent players
    newactive_player = opponent_player
    newopponent_player = active_player

    return newactive_player, newopponent_player


def main():
    # sets initial game environment and runs main game loop

    # initial game state
    game_over = False
    # visual game separator
    game_separator = ("*" * 36)

    # set initial active and opponent player
    active_player = "x"
    opponent_player = "o"
    # initial player lane spots
    x_lane_position = 0
    o_lane_position = 0
    # create player position list [x, o]
    player_positions = [x_lane_position, o_lane_position]

    # display initial instructions and state
    print("Players begin in the starting position")
    print(game_separator)
    display_state(active_player, opponent_player, player_positions)
    print(game_separator)

    # main game play loop that continue until player's token reaches end of race lane
    while not game_over:

        # roll dice for active player
        roll = roll_die(active_player)
        # update player positions on race lane
        player_positions = update_position(
            active_player, player_positions, roll)
        # dispaly game state using race lane
        print(game_separator)
        display_state(active_player, opponent_player, player_positions)
        print(game_separator)
        # change active and opponent players
        opponents = opponent(active_player, opponent_player)
        active_player = opponents[0]  # new active player
        opponent_player = opponents[1]  # new opponent player
        # check if game over/if active player reached end of lane
        game_over = check_game_over(player_positions, game_over)
    # opponent player is winner because game has changed opponents in main game loop
    print("Player " + opponent_player + " has won!")


main()
