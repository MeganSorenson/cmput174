# TTT Version 1

import pygame
import random


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
        self.board_size = 4
        self.image_list = []
        self.load_images()
        self.board = []  # will be represented by a list of lists
        self.create_board()

    def load_images(self):
        # load the images from the files into the image list
        # you hvae to load 7 more for the memory game
        image = pygame.image.load('image1.bmp')
        self.image_list.append(image)
        # make it so that there are pairs of the images
        self.image_list += self.image_list
        random.shuffle(self.image_list)  # shuffle the images

    def create_board(self):
        # width = self.surface.get_width()//self.board_size
        # height = self.surface.get_height()//self.board_size
        for row_index in range(0, self.board_size):
            row = []
            for col_index in range(0, self.board_size):
                image = self.image_list[0]  # we will have more than one image
                width = image.get_width()  # image is a pygame.Surface object
                height = image.get_height()
                x = col_index * width
                y = row_index * height
                tile = Tile(x, y, width, height, image, self.surface)
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
                tile.draw()
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
    # defines properties and behaviour
    def __init__(self, x, y, width, height, image, surface):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('white')
        self.border_width = 3
        self.surface = surface
        self.content = image  # the image is the fill of the tile
        self.hidden_image = pygame.image.load('image0.bmp')
        self.hidden = True

    def draw(self):
        location = (self.rect.x, self.rect.y)
        if self.hidden:
            self.surface.blit(self.hidden_image, location)
        else:
            self.surface.blit(self.content, location)
        pygame.draw.rect(self.surface, self.color,
                         self.rect, self.border_width)

    def draw_content(self):
        # height of tiles is approx 133... make font same size
        font = pygame.font.SysFont("", 133)
        text_box = font.render(self.content, True, self.color)
        rect1 = text_box.get_rect()
        # change center of rect1 to center of self.rect to place text box in middle of tile
        rect1.center = self.rect.center
        # set top left corner of textbox to the top left corner of the centerized rect1
        location = (rect1.x, rect1.y)
        self.surface.blit(text_box, location)


main()
