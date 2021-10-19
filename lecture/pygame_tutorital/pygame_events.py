# Pre-Poke Framework
# Implements a general game template for games with animation
# You must use this template for all your graphical lab assignments
# and you are only allowed to inlclude additional modules that are part of
# the Python Standard Library; no other modules are allowed

import pygame
import math


# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption(
        'A template for graphical games with two moving dots')
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
        self.default_color = 'yellow'
        self.small_dot = Dot(self.default_color, 30, [
                             50, 50], [1, 2], self.surface)

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
            if event.type == pygame.KEYDOWN:
                self.handle_keydown(event)
            if event.type == pygame.KEYUP:
                self.handle_keyup(event)
            if event.type == pygame.MOUSEBUTTONUP:
                self.handle_mouseup(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mousedown(event)
            if event.type == pygame.MOUSEMOTION:
                self.handle_mouse_motion(event)

    def handle_keydown(self, event):
        if event.key == pygame.K_r:
            self.small_dot.set_color("red")
        if event.key == pygame.K_g:
            self.small_dot.set_color("green")
        if event.key == pygame.K_b:
            self.small_dot.set_color("blue")
        if event.key == pygame.K_SPACE:
            self.small_dot.set_color(self.default_color)

    def handle_keyup(self, event):
        if event.key == pygame.K_r or event.key == pygame.K_g or event.key == pygame.K_b:
            self.small_dot.set_color(self.default_color)

    def handle_mouseup(self, event):
        if event.button == 3:
            if self.small_dot.collidepoint(event.pos):
                self.small_dot.stop()
            else:
                self.small_dot.restart()
        if event.button == 1:
            self.small_dot.restart()

    def handle_mousedown(self, event):
        if event.button == 1 and self.small_dot.collidepoint(event.pos):
            self.small_dot.stop()

    def handle_mouse_motion(self, event):
        if event.buttons == (1, 0, 0):
            self.small_dot.set_center(event.pos)

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color)  # clear the display surface first
        self.small_dot.draw()
        pygame.display.update()  # make the updated surface appear on the display

    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update

        self.small_dot.move()

    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
        pass


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
        self.velocity_backup = dot_velocity
        self.surface = surface

    def move(self):
        # Change the location of the Dot by adding the corresponding
        # speed values to the x and y coordinate of its center
        # - self is the Dot

        width_height = self.surface.get_size()
        for i in range(0, 2):
            self.center[i] = (
                self.center[i] + self.velocity[i]) % width_height[i]
            # if self.center[i] > width_
            # height[i]:
            # self.center[i] = 0

    def set_center(self, point):
        # sets center coordinates of the dot to a new point
        # self is the dot
        # point is the tuple or a list representing the new point
        for i in range(0, 2):
            self.center[i] = point[i]

    def stop(self):
        # stops the movment of the dotby setting its velocity to zero
        # self is the dot
        self.velocity = [0, 0]

    def restart(self):
        # restarts the movement of the dot by setting the velocity back to it's original value
        self.velocity = self.velocity_backup

    def collidepoint(self, point):
        # returns true if point is inside the dot, false otherwide
        # self is dot
        # point is tuple representing a point
        x = self.center[0] - point[0]
        y = self.center[1] - point[1]

        distance = math.sqrt(x ** 2 + y ** 2)

        return distance <= self.radius

    def set_color(self, color):
        # changes the colour of the dot
        # self id the dot
        # color is a string object representing a color name
        self.color = pygame.Color(color)

    def draw(self):
        # Draw the dot on the surface
        # - self is the Dot

        pygame.draw.circle(self.surface, self.color, self.center, self.radius)


main()
