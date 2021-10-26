# Pre-Poke Framework
# Implements a general game template for games with animation
# You must use this template for all your graphical lab assignments
# and you are only allowed to inlclude additional modules that are part of
# the Python Standard Library; no other modules are allowed

import pygame
import random
import math


# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption('Poke The Dots')
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
        self.create_dots()
        self.score = 0

        #self.max_frames = 150
        #self.frame_counter = 0

    def create_dots(self):
        self.small_dot = Dot('red', 30, [0, 0], [1, 2], self.surface)
        self.big_dot = Dot('blue', 40, [0, 0], [2, 1], self.surface)
        while self.small_dot.collide(self.big_dot):
            self.small_dot.randomize()
            self.big_dot.randomize()

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
                self.handle_mouse_up()

    def handle_mouse_up(self):
        # responds to MOUSEBUTTONUP event
        self.small_dot.randomize()
        self.big_dot.randomize()

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color)  # clear the display surface first
        self.small_dot.draw()
        self.big_dot.draw()
        self.draw_score()
        if not self.continue_game:
            self.draw_game_over()
        pygame.display.update()  # make the updated surface appear on the display

    def draw_game_over(self):
        string = "Game Over"
        fg_color = self.small_dot.get_color()
        bg_color = self.big_dot.get_color()
        font = pygame.font.SysFont("", 70)
        text_box = font.render(string, True, fg_color, bg_color)
        x = 0
        y = self.surface.get_height() - text_box.get_height()
        location = (x, y)
        self.surface.blit(text_box, location)

    def draw_score(self):
        score_string = "Score: " + str(self.score)
        # create font object
        font_size = 80
        font = pygame.font.SysFont("", font_size)
        # render font
        fg_color = pygame.Color("white")
        text_box = font.render(score_string, True, fg_color, self.bg_color)
        # compute location
        location = (0, 0)
        #y = 0
        #a = self.surface.get_size()[0]
        #a = self.surface.get_width()
        #b = text_box.get_size()[0]
        #b = text_box.get_width()
        #x = a - b
        #location = (x, y)

        # blit source surface on target surface at specified location
        self.surface.blit(text_box, location)

    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update

        self.small_dot.move()
        self.big_dot.move()
        self.score = pygame.time.get_ticks() // 1000  # ms / 1000 to get seconds
        #self.frame_counter = self.frame_counter + 1

    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
        if self.small_dot.collide(self.big_dot):
            self.continue_game = False
        # if self.frame_counter > self.max_frames:
        #self.continue_game = False


class Dot:
    # An object in this class represents a Dot that moves

    def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, surface):
        # Initialize a Dot.
        # - self is the Dot to initialize
        # - color is the pygame.Color of the dot
        # - center is a list containing the x and y int
        #   coords of the center of the dot
        # - radius is the int pixel radius of the dot
        # - velocity is a list containing the x and y components
        # - surface is the window's pygame.Surface object

        self.color = pygame.Color(dot_color)
        self.radius = dot_radius
        self.center = dot_center
        self.velocity = dot_velocity
        self.surface = surface

    def get_color(self):
        # returns instance attribute color
        return self.color

    def set_color(self, newcolor):
        self.color = pygame.Color(newcolor)

    def collide(self, other):
        # return True is self collide with other
        # False otherwise
        # self is the Dot object
        # other is also a Fot object
        distance_x = self.center[0] - other.center[0]
        distance_y = self.center[1] - other.center[1]

        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        return distance <= self.radius + other.radius

    def randomize(self):
        size = self.surface.get_size()

        for i in range(0, 2):
            self.center[i] = random.randint(self.radius, size[i] - self.radius)

    def move(self):
        # Change the location of the Dot by adding the corresponding
        # speed values to the x and y coordinate of its center
        # - self is the Dot
        size = self.surface.get_size()

        for i in range(0, 2):
            self.center[i] = (self.center[i] + self.velocity[i])
            if self.center[i] < self.radius:  # left or top edge touched
                self.velocity[i] = - self.velocity[i]
            elif self.center[i] + self.radius > size[i]:  # bottom or right edge touched
                self.velocity[i] = -self.velocity[i]

    def draw(self):
        # Draw the dot on the surface
        # - self is the Dot

        pygame.draw.circle(self.surface, self.color, self.center, self.radius)


main()
x = main()
print(type(x))
