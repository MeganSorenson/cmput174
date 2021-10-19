# user defined classes
class Card:
    def __init__(self, rank, suit):
        # initialize a card with a given suit and rank
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        # return the rank of a card
        pass

    def display(self):
        # display a card as a string with the name of the rank
        pass


class Deck:
    def __init__(self):
        # initialize a deck by generating one of eahc possible card using Card class
        # deck should contain one Card object for each of the 52 different cards
        pass

    def shuffle(self):
        # randomly shuffle the deck of cards
        pass

    def deal(self):
        # return a card from the top of the deck
        # remove that card from the deck
        pass


class Player:
    def __init__(self):
        # initialize a player whho can keep track of the cards in their hand
        # initially, the hadn is empty
        pass

    def add(self, card):
        # add a card to the players hand
        # card is an instance of the Card class
        pass

    def ace_cards(self):
        # returns a number of Ace cards in players hand
        pass

    def display(self):
        # display the players hand
        # calls display() mehthod of each card object in the players hand
        pass


def main():
    pass
    # create one deck
    # shuffle the deck
    # create both players
    # populate the players hands with 5 cards each
    # display thhe players hands
    # display the number of ace cards in each players hand
    # display the winner
    # if tie, restart the game


main()
