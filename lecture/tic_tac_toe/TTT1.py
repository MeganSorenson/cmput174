# TTT Version 1

import pygame


# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption('Tic Tac Toe')
    # get the display surface
    w_surface = pygame.display.get_surface()
    # create a game object
    game = Game(w_surface)
    # start the main game loop by calling the play method on the game object
    game.play()
    # quit pygame and clean up the pygame window
    pygame.quit()


# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object

        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color('black')

        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

        # === game specific objects
        self.board_size = 3  # can store as one number because row and col numbers are the same
        self.board = []  # will be represented by a list of lists
        self.create_board()

    def create_board(self):
        width = self.surface.get_width() // self.board_size
        height = self.surface.get_height() // self.board_size, self.surface
        for row_index in range(0, self.board_size):
            row = []
            for col_index in range(0, self.board_size):
                x = col_index * width
                y = row_index * height
                tile = Tile(x, y, width, height, self.surface)
                row.append(tile)
            self.board.append(row)

    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.

        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()
            if self.continue_game:
                self.update()
                self.decide_continue()
            # run at most with FPS Frames Per Second
            self.game_Clock.tick(self.FPS)

    def handle_events(self):
        # Handle each user event by changing the game state appropriately.
        # - self is the Game whose events will be handled

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color)  # clear the display surface first
        # draw the board
        for row in self.board:
            for tile in row:
                tile.draw
        pygame.display.update()  # make the updated surface appear on the display

    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update

        pass

    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check

        pass


class Tile:
    def __init__(self, x, y, width, height, surface):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color("white")
        self.border_width = 3
        self.surface = surface

    def draw(self):
        pygame.draw.rect(self.surface, self.color,
                         self.rect, self.border_width)


main()
