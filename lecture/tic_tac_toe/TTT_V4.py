# TTT Version 4
# two player game

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
        self.board_size = 3
        self.board = []  # will be represented by a list of lists
        self.stop_color = pygame.Color("red")  # turn win cells red
        self.colored = []  # keeps track of which lists have win
        self.filled = []  # keeps track of the filled tiles
        self.player_1 = "X"
        self.player_2 = "O"
        self.turn = self.player_1  # always start with player 1's turn
        self.create_board()

    def create_board(self):
        width = self.surface.get_width()//self.board_size
        height = self.surface.get_height()//self.board_size
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
            if event.type == pygame.MOUSEBUTTONUP and self.continue_game:
                # event.pos is the position of the click as a tuple (x, y)
                self.handle_mouse_up(event.pos)

    def handle_mouse_up(self, position):
        # position is bound to event.pos
        # position is the (x, y) location of the click
        for row in self.board:
            for tile in row:
                # asking the tile 'have you been selected?'
                if tile.select(position, self.turn):
                    self.change_turn()
                    self.filled.append(tile)

    def change_turn(self):
        if self.turn == self.player_1:
            self.turn = self.player_2
        else:
            self.turn = self.player_1

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color)  # clear the display surface first

        # if end of game, change win rows/cols/diags to stop_color
        if self.continue_game == False:
            for tile in self.colored:
                tile.set_color(self.stop_color)

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

        if self.is_win() or self.is_tie():  # lazy evaluation... only checks for tie if there's no win
            self.continue_game = False

    def is_win(self):
        # see if there is a win
        # call is_row_win to see if there is a row win
        # call is_col_win to see if there is a column win
        # calls is_diagonal_win to see if there is a diagonal win
        win = False
        row_win = self.is_row_win()
        col_win = self.is_col_win()
        diagonal_win = self.is_diagonal_win()
        if row_win:
            win = True
        if col_win:
            win = True
        if diagonal_win:
            win = True
        return win

    def is_row_win(self):
        # collecting all the rows in the board
        # and putting these rows in a list called list_of_lists_of_tiles
        # calls contains_list_win to determine if there is a win in any row
        row_win = False
        list_of_lists_of_tiles = self.board
        if self.contains_list_win(list_of_lists_of_tiles):
            row_win = True
        return row_win

    def is_col_win(self):
        # collectinf all the columns in the board
        # and putting these columns in a list called list_of_lists_of_tiles
        # calls contains_list_win to determine if there is a win in any row
        col_win = False
        list_of_lists_of_tiles = []
        # for each column index, go to each row and pick up the column tiles
        # after creating each column list, append it to the list_of_lists_of_tiles
        for col_index in range(self.board_size):
            column = []
            for row_index in range(self.board_size):
                tile = self.board[row_index][col_index]
                column.append(tile)
            list_of_lists_of_tiles.append(column)
        if self.contains_list_win(list_of_lists_of_tiles):
            col_win = True
        return col_win

    def is_diagonal_win(self):
        # collecting all the diagonals in the board
        # and putting these diagonals in a lists called list_ofLists_of_tiles
        # calls contains_list_win to determine if there is a win in any diagonal
        diagonal_win = False
        list_of_lists_of_tiles = []
        # get diagonals and add to list_of_lists_of_tiles
        diag1 = []  # diagonal with same row and col index for each tile
        diag2 = []
        for index in range(self.board_size):
            tile1 = self.board[index][index]
            diag1.append(tile1)
            tile2 = self.board[index][self.board_size - 1 - index]
            diag2.append(tile2)
        list_of_lists_of_tiles.append(diag1)
        list_of_lists_of_tiles.append(diag2)
        if self.contains_list_win(list_of_lists_of_tiles):
            diagonal_win = True
        return diagonal_win

    def contains_list_win(self, list_of_lists_of_tiles):
        # walking through list in the list of lists of tiles
        # calls is_list_win to see if there is a win in that list
        win = False
        for list_of_tiles in list_of_lists_of_tiles:
            if self.is_list_win(list_of_tiles):
                win = True
        return win

    def is_list_win(self, list_of_tiles):
        # method that is checking each tile in the list
        # to see if all the tiles are the same
        # if they are, there is a win in that list
        # if they aren't, there is no win in that list
        same = True
        first = list_of_tiles[0]
        for tile in list_of_tiles:
            if not first == tile:  # can use operator because method is called __eq__
                same = False
        if same:
            for tile in list_of_tiles:
                self.colored.append(tile)
        return same

    def is_tie(self):
        # determine if the board is filled or not
        tie = False
        if len(self.filled) == self.board_size * self.board_size:
            tie = True
            self.colored = self.filled
        return tie


class Tile:
    # defines properties and behaviour
    def __init__(self, x, y, width, height, surface):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('white')
        self.border_width = 3
        self.surface = surface
        self.content = ""
        self.flashing = False

    def select(self, position, current_player):
        # position is the (x, y) of the location of the click
        selected = False
        if self.rect.collidepoint(position):  # is there a click?
            if self.content == "":  # is the tile unoccupied?
                self.content = current_player
                selected = True
            else:
                self.flashing = True
        return selected

    def __eq__(self, other_tile):  # can use an operator to call the method (overloading == operator)
        if self.content == other_tile.content:
            if self.content != "":
                return True
        else:
            return False

    def draw(self):
        if self.flashing:
            # draw a white ractangle
            pygame.draw.rect(self.surface, self.color, self.rect)
            self.flashing = False
        else:
            # draw a black rectangle with a white border
            pygame.draw.rect(self.surface, self.color,
                             self.rect, self.border_width)
        self.draw_content()

    def draw_content(self):
        # this method is called by the handle_mouse_up() method in the Game class

        # height of tiles is approx 133... make font same size
        font = pygame.font.SysFont("", 133)
        text_box = font.render(self.content, True, self.color)
        rect1 = text_box.get_rect()
        # change center of rect1 to center of self.rect to place text box in middle of tile
        rect1.center = self.rect.center
        # set top left corner of textbox to the top left corner of the centerized rect1
        location = (rect1.x, rect1.y)
        self.surface.blit(text_box, location)

    def set_color(self, color):
        # changes color of tile contents
        self.color = color


main()
