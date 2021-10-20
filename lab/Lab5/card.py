import random

# user defined classes


class Card:
    def __init__(self, rank, suit):
        # initialize a card with a given suit and rank
        # rank is an integer between 1 and 13
        # suit is a string of wither "Hearts", "Clubs", "Diamonds", or "Spades"
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        # return the rank of a card
        return self.rank

    def display(self):
        # display a card as a string with the name of the rank
        ranks = {1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
                 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"}
        print(ranks[self.rank] + " of " + self.suit)


class Deck:
    def __init__(self):
        # initialize a deck by generating one of each possible card using Card class
        # deck should contain one Card object for each of the 52 different cards
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.deck = []

        for suit in suits:
            for i in range(1, 14):
                deck_card = Card(i, suit)
                self.deck.append(deck_card)

    def shuffle(self):
        # randomly shuffle the deck of cards
        random.shuffle(self.deck)

    def deal(self):
        # return a card from the top of the deck
        # remove that card from the deck
        dealt_card = random.choice(self.deck)
        self.deck.remove(dealt_card)

        return dealt_card


class Player:
    def __init__(self):
        # initialize a player who can keep track of the cards in their hand
        # initially, the hand is empty
        self.hand = []

    def add(self, card):
        # add a card to the players hand
        # card is an instance of the Card class
        self.hand.append(card)

    def ace_cards(self):
        # returns a number of Ace cards in players hand
        number_aces = 0
        for card in self.hand:
            if card.get_rank() == 1:
                number_aces += 1
        return number_aces

    def display(self):
        # display the players hand
        # calls display() method of each card object in the players hand
        for card in self.hand:
            card.display()


def main():

    shuffle_again = True

    while shuffle_again:
        # create one deck
        deck = Deck()

        # shuffle the deck
        deck.shuffle()

        # create both players
        player_one = Player()
        player_two = Player()

        # populate the players hands with 5 cards each
        players = (player_one, player_two)
        for player in players:
            for i in range(0, 6):
                dealt_card = deck.deal()
                player.add(dealt_card)

        # display the players hands
        print("This is the hand of player 1: ")
        player_one.display()
        print()
        print("This is the hand of player 2: ")
        player_two.display()
        print()

        # display the number of ace cards in each players hand
        player_one_aces = player_one.ace_cards()
        player_two_aces = player_two.ace_cards()
        print("Number of ace cards in each player's hand: ")
        print("Player 1 has " + str(player_one_aces) + " aces")
        print("Player 2 has " + str(player_two_aces) + " aces")
        print()

        # display the winner
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

        # if tie, restart the game


main()
