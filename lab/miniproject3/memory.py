# Pre-Poke Framework
# Implements a general game template for games with animation
# You must use this template for all your graphical lab assignments
# and you are only allowed to inlclude additional modules that are part of
# the Python Standard Library; no other modules are allowed

import pygame
import random


# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption('Memory')
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
        self.load_images()

        # board will be represented as a list of lists
        self.board_size = 4
        self.board = []
        self.create_board()

        # initially, no tile have been clicked
        self.number_tiles_clicked = 0
        # list of tile objects that have been clicked
        self.clicked_tiles = []

        self.max_frames = 150
        self.frame_counter = 0

    def create_board(self):
        for row_index in range(self.board_size):
            row = []
            for col_index in range(self.board_size):
                image = self.images.pop()
                x = col_index * image.get_width()
                y = row_index * image.get_height()
                width = image.get_width()
                height = image.get_height()
                tile = Tile(self.hidden_image, image, x,
                            y, width, height, self.surface)
                row.append(tile)
            self.board.append(row)

    def load_images(self):
        self.images = []
        # upload the specified number of images
        # assumes filenames are image#.bmp
        number_images = 8
        for i in range(1, number_images + 1):
            image_filename = "image" + str(i) + ".bmp"
            image = pygame.image.load(image_filename)
            self.images.append(image)
        # create pairs for each image
        self.images += self.images
        # shuffle images
        random.shuffle(self.images)
        # upload hidden image
        self.hidden_image = pygame.image.load("image0.bmp")

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_down(event)

    def handle_mouse_down(self, event):
        for row in self.board:
            for tile in row:
                # get dimensions
                xy = tile.get_xy()
                width_height = tile.get_width_height()
                # check if mouse click in within x range of tile
                # then check if mouse click in within y range of tile
                # if yes to both, change tile state to exposed
                if event.pos[0] < xy[0] + width_height[0] and event.pos[0] > xy[0]:
                    if event.pos[1] > xy[1] and event.pos[1] < xy[1] + width_height[1]:
                        # only count tile click if the tile isn't already exposed
                        tile_exposed = tile.get_state()
                        if not tile_exposed:
                            tile.expose()
                            # keep track of tiles clicked
                            self.number_tiles_clicked += 1
                            self.clicked_tiles.append(tile)

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color)  # clear the display surface first
        # draw Tiles
        for row in self.board:
            for tile in row:
                tile.draw()
        pygame.display.update()  # make the updated surface appear on the display

    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update
        if self.number_tiles_clicked == 2:
            tile_one = self.clicked_tiles[0]
            tile_two = self.clicked_tiles[1]
            # check if tile images are the same
            matched = tile_one.check_matched(tile_two)
            # if the tile images are the not the same, hide tile images
            if not matched:
                tile_one.hide()
                tile_two.hide()

            if matched:
                print("MATCHED")
            # reset the number of clicked tiles and list of clicked tiles
            self.number_tiles_clicked = 0
            self.clicked_tiles = []

        self.frame_counter = self.frame_counter + 1

    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
        pass


class Tile:
    # An object in this class represents a Tile on a board
    def __init__(self, hidden_image, matched_image, x, y, width, height, surface):
        self.hidden_image = hidden_image
        self.matched_image = matched_image
        self.rect = pygame.Rect(x, y, width, height)
        self.surface = surface
        # initialized with hidden image showing
        self.exposed = False

    def get_xy(self):
        return (self.rect.x, self.rect.y)

    def get_width_height(self):
        return(self.rect.width, self.rect.height)

    def get_image(self):
        return self.matched_image

    def get_state(self):
        return self.exposed

    def draw(self):
        # draw appropriate image
        self.draw_image()
        # draw grid borders
        border_color = pygame.Color("white")
        border_width = 2
        pygame.draw.rect(self.surface, border_color, self.rect, border_width)

    def draw_image(self):
        location = (self.rect.x, self.rect.y)
        if not self.exposed:
            # if tile in hidden state, draw hidden_image
            self.surface.blit(self.hidden_image, location)
        else:
            # if tile not hidden state, draw matched_image
            self.surface.blit(self.matched_image, location)

    def expose(self):
        # when called, changes the Tile's state to exposed
        self.exposed = True

    def hide(self):
        # when called, changes the Tile's exposed state to false
        self.exposed = False

    def check_matched(self, other_tile):
        # checks whether two tiles have the same image
        # SOMETHING IS WRONG HERE
        if other_tile.get_image() == self.get_image():
            matched = True
        else:
            matched = False

        return matched


main()
