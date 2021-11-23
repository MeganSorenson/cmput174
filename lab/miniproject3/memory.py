# Memory Game
# a 4x4 board of hidden tiles who reveal images in pairs as the player clicks the tiles
# if the the clicked tiles have matching images, the tiles remain revealed, otherwise the two tile become hidden again
# the game's score is kept by tracking the seconds that the player has been matching tiles
# the game continues until all tiles are matched

# https://www.pygame.org/docs/
import pygame
# https://docs.python.org/3/library/random.html
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
        # self is the Game to initialize
        # surface is the display window surface object

        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color('black')

        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

        # === game specific objects

        # load images for matching game
        self.load_images()

        # create game board
        # board will be represented as a list of lists
        self.board_size = 4
        self.board = []
        self.create_board()

        # initially, no tiles have been clicked
        self.number_tiles_clicked = 0
        # list of tile objects that have been clicked
        self.clicked_tiles = []

        self.frame_counter = 0

    def create_board(self):
        # create game board as a list of lists containing Tile objects
        # game board will be 4x4 tiles
        # self is the Game object whose board it is
        # returns NoneType
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
        # loads images for the matching game from a set of 9 files
        # one file is the hidden image, the other 8 are unique images
        # unique images are added to a list which is doubled to make pairs for each image
        # images are also shuffled randomly
        # self is the Game object who will use the images on the board tiles
        # returns NoneType

        # upload hidden image
        self.hidden_image = pygame.image.load("image0.bmp")

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
        # shuffle images randomly
        random.shuffle(self.images)

    def play(self):
        # Play the game until the player presses the close box.
        # self is the Game that should be continued or not.
        # returns NoneType

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
        # self is the Game whose events will be handled
        # returns NoneType

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_down(event)

    def handle_mouse_down(self, event):
        # handles the mouse click events
        # when mouse is clicked, check xy coordinates of click
        # determine which tile is clicked and expose the tile
        # self is the Game whose event is being handled
        # event is a pygame.Event object of type MOUSEBUTTONDOWN
        # returns NoneType

        # for each tile in each row, check find which tile the player clicked and expose it
        for row in self.board:
            for tile in row:
                # get tile dimensions
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
        # self is the Game to draw
        # returns NoneType

        self.surface.fill(self.bg_color)  # clear the display surface first
        # draw timer
        self.draw_timer()
        # draw Tiles
        for row in self.board:
            for tile in row:
                tile.draw()
        pygame.display.update()  # make the updated surface appear on the display

    def draw_timer(self):
        # draws the game timer from the Game frame counter
        # self is the Game whose timer is being drawn
        # returns NoneType

        # convert time to string of seconds
        time = str(self.frame_counter // 60)
        # set font characteristics
        font_size = 70
        font = pygame.font.SysFont("", font_size)
        fg_color = pygame.Color("white")
        # create text box of time string using font characteristics
        text_box = font.render(time, True, fg_color, self.bg_color)
        # location is top right corner of window
        location = (self.surface.get_width() - text_box.get_width(), 0)
        # blit to game surface at location
        self.surface.blit(text_box, location)

    def update(self):
        # Update the game objects for the next frame.
        # self is the Game to update
        # returns NoneType

        # only count frames if game is playing
        if self.continue_game:
            self.frame_counter = self.frame_counter + 1
        # update tiles after two tiles have been clicked
        self.update_tiles()

    def update_tiles(self):
        # updates tiles of the board after two unmaytched tiles have been clicked
        # check whether clickd tiles are matching
        # if yes, leave exposed, if no, hide tiles
        # self is the Game whose tiles are being updated
        # returns NoneType

        if self.number_tiles_clicked == 2:
            # get clicked tiles
            tile_one = self.clicked_tiles[0]
            tile_two = self.clicked_tiles[1]
            # check if tile images are the same
            matched = tile_one.check_matched(tile_two)
            # if the tile images are the not the same, hide tile images
            # wait 1 second before hiding the tiles again
            pygame.time.delay(500)
            if not matched:
                tile_one.hide()
                tile_two.hide()
            # reset the number of clicked tiles and list of clicked tiles
            self.number_tiles_clicked = 0
            self.clicked_tiles = []

    def decide_continue(self):
        # Check and remember if the game should continue
        # self is the Game to check
        # returns NoneType

        # initally assumes all tiles are matched
        # then checks each tile, and if one of them is unmatched, all tiles are not matched
        all_tiles_matched = True
        for row in self.board:
            for tile in row:
                tile_exposed = tile.get_state()
                if not tile_exposed:
                    all_tiles_matched = False
        # if all tiles are matched, game is over
        if all_tiles_matched:
            self.continue_game = False


class Tile:
    # An object in this class represents a Tile on a board with an image
    def __init__(self, hidden_image, matched_image, x, y, width, height, surface):
        # initializes a Tile object
        # self is the Tile object being initialized
        # hidden_image is a pygame.Surface with an image of a question mark
        # matched_image is a pygame.Surface with a unique image that the player is attempting to match
        # x is an int of the x coordinate of the top left corner of the tile
        # y in an int of the y coordinate of the top left corner of the tile
        # width is the width of the tile as an int
        # height is the height of the tile as an int
        # surface is the pygame.Surface object where the tile is drawn

        self.hidden_image = hidden_image
        self.matched_image = matched_image
        # create pygame.Rect object using intial tile parameters
        self.rect = pygame.Rect(x, y, width, height)
        self.surface = surface
        # initialized with hidden image showing
        self.exposed = False

    def get_xy(self):
        # gets the coordinates of the top left corner of the tile rect
        # self is the Tile whose top left coordinates are requested
        # returns a tuple with an x,y coordinate

        return (self.rect.x, self.rect.y)

    def get_width_height(self):
        # gets the width and height of the tile rect
        # self is the Tile whose wdith and height are requested
        # returns a tuple with the width,height parameters

        return(self.rect.width, self.rect.height)

    def get_image(self):
        # gets the matched_image of the tile
        # useful to check whether another tile's image matched
        # self is the Tile whose image is requested
        # returns an image of type pygame.Surface

        return self.matched_image

    def get_state(self):
        # gets the exposed state of the tile
        # useful for checking if tile has already been exposed
        # self is the Tile whose state is being requested
        # returns a bool of whether or not tile's image is exposed

        return self.exposed

    def draw(self):
        # draws tile outline and appropriate tile image
        # self is the Tile who is being drawn
        # returns NoneType

        # draw image based on draw_image() method
        self.draw_image()
        # draw grid borders on top of image
        border_color = pygame.Color("black")
        border_width = 5
        pygame.draw.rect(self.surface, border_color, self.rect, border_width)

    def draw_image(self):
        # draws the approriate image for the tile based on the exposed state
        # self is the Tile whose image is being drawn
        # returns NoneType

        # location is the top left corner of the Tile rect
        # because tile rect is the same size as the image
        location = (self.rect.x, self.rect.y)
        if not self.exposed:
            # if tile in hidden state, draw hidden_image
            self.surface.blit(self.hidden_image, location)
        else:
            # if tile not hidden state, draw matched_image
            self.surface.blit(self.matched_image, location)

    def expose(self):
        # when called, changes the Tile's state to exposed
        # self is the Tile whose state is being set
        # returns NoneType

        self.exposed = True

    def hide(self):
        # when called, changes the Tile's state to not exposed
        # self is the Tile whose state is being set
        # returns NoneType

        self.exposed = False

    def check_matched(self, other_tile):
        # checks whether two tiles have the same image
        # if images are the same, matched is true, is not, matched is false
        # self is the Tile whose image is being compared with another tile
        # other_tile is an object of type Tile who is being compared to self
        # returns a bool of whether or not images of both tiles match

        if other_tile.get_image() == self.get_image():
            matched = True
        else:
            matched = False

        return matched


main()
