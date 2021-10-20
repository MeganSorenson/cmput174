# Ace Card Game
# two-player card game where each player gets 5 cards from a typical shuffled deck
# the player with the most Aces in their hand wins
# if there is a tie, the deck is shuffled again and players get 5 new cards each

# https://docs.python.org/3/library/random.html
import random


class Card:
    # creates a single card with it's own rank and suit
    # able to get its rank as an integer fron 1-13 and display its rank and suit as a string
    def __init__(self, rank, suit):
        # initialize a card with a given suit and rank
        # rank is an integer between 1 and 13
        # suit is a string of wither "Hearts", "Clubs", "Diamonds", or "Spades"
        # returns NoneType
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        # returns and integer representing the rank of a card
        return self.rank

    def display(self):
        # displays a card as a string with the name of the rank and its suit
        # returns NoneType
        ranks = {1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
                 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"}
        print(ranks[self.rank] + " of " + self.suit)


class Deck:
    # creates a deck of cards (type Card)
    # total of 52 cards in a deck using combinations of 13 ranks and 4 suits
    # decks be shuffled, and can have it's top card deealt and removed from the deck
    def __init__(self):
        # initialize a deck by generating one of each possible card using Card class
        # deck should contain one Card object for each of the 52 different cards
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.deck = []
        # add Cards to deck, for a total of 52 cards
        for suit in suits:
            for i in range(1, 14):
                deck_card = Card(i, suit)
                self.deck.append(deck_card)

    def shuffle(self):
        # randomly shuffle the deck of cards
        # returns NoneType
        random.shuffle(self.deck)

    def deal(self):
        # returns a card from the top of the deck (top assumed to be last element of list)
        # removes that card from the deck (done automatically in .pop() when chooding card at top of deck)
        # returns an object of type Card
        dealt_card = self.deck.pop()

        return dealt_card


class Player:
    # creates a player that can play the card game by keeping track of its hand of cards (type Card)
    # can add cards to it's hand, count the number of aces in its hand, and display its hand
    def __init__(self):
        # initialize a player who can keep track of the cards in their hand
        # initially, the hand is empty
        self.hand = []

    def add(self, card):
        # add a card to the players hand
        # card is an instance of the Card class
        # returns a NoneType
        self.hand.append(card)

    def ace_cards(self):
        # counts number of aces in hand
        # returns an integer representing the number of Ace cards in hand
        number_aces = 0
        # if ace, add to number of aces in hand
        for card in self.hand:
            if card.get_rank() == 1:
                number_aces += 1
        return number_aces

    def display(self):
        # display the players hand
        # calls display() method of each Card object in the players hand
        # returns NoneType
        for card in self.hand:
            card.display()


def main():
    # initially, shuffle again is True so that main game loop runs
    shuffle_again = True

    # main game loop, if tie keep making new decks
    while shuffle_again:
        # create a deck from the Deck Class
        deck = Deck()

        # shuffle the deck
        # using the shuffle method of the Deck class
        deck.shuffle()

        # create both players using the Player class
        player_one = Player()
        player_two = Player()

        # tuple of the players used for populating players hands in a for loop
        players = (player_one, player_two)

        # populate the players hands with 5 cards each
        # deal top card from deck, remove from deck, and add to player's hand
        for player in players:
            for i in range(0, 6):
                dealt_card = deck.deal()
                player.add(dealt_card)

        # display the players hands
        # put spaces between each 'section' using and empty print()
        print("This is the hand of player 1: ")
        player_one.display()
        print()
        print("This is the hand of player 2: ")
        player_two.display()
        print()

        # count and display the number of ace cards in each players hand
        # put space after 'section' using an empty print()
        player_one_aces = player_one.ace_cards()
        player_two_aces = player_two.ace_cards()
        print("Number of ace cards in each player's hand: ")
        print("Player 1 has " + str(player_one_aces) + " aces")
        print("Player 2 has " + str(player_two_aces) + " aces")
        print()

        # display the winner by chekcing who has the most aces
        print("Result: ")
        if player_one_aces == player_two_aces:
            print("No winner, shuffle again")
            print()
        elif player_one_aces > player_two_aces:
            print("Player 1 is the winner")
            shuffle_again = False
        else:
            print("Player 2 is the winner")
            shuffle_again = False


main()
