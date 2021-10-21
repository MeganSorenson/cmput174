# Pre-Poke Framework
# Implements a general game template for games with animation
# You must use this template for all your graphical lab assignments
# and you are only allowed to inlclude additional modules that are part of
# the Python Standard Library; no other modules are allowed

import pygame


# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption('Pong')
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
        size = self.surface.get_size()

        self.ball = Ball(
            'white', 5, [size[0] / 2, size[1] / 2], [4, 4], self.surface)

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
        self.ball.draw()
        pygame.display.update()  # make the updated surface appear on the display

    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update

        self.ball.move()

    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check

        pass


class Ball:
    # An object in this class represents a Ball that moves

    def __init__(self, ball_color, ball_radius, ball_center, ball_velocity, surface):
        # Initialize a Ball.
        # - self is the Ball to initialize
        # - color is the pygame.Color of the Ball
        # - center is a list containing the x and y int
        #   coords of the center of the Ball
        # - radius is the int pixel radius of the Ball
        # - velocity is a list containing the x and y components
        # - surface is the window's pygame.Surface object

        self.color = pygame.Color(ball_color)
        self.radius = ball_radius
        self.center = ball_center
        self.velocity = ball_velocity
        self.surface = surface

    def move(self):
        # Change the location of the Ball by adding the corresponding
        # speed values to the x and y coordinate of its center
        # - self is the Ball
        size = self.surface.get_size()

        for i in range(0, 2):
            self.center[i] = (self.center[i] + self.velocity[i])
            if self.center[i] < self.radius:  # left or top edge touched
                self.velocity[i] = - self.velocity[i]
            elif self.center[i] + self.radius > size[i]:  # bottom or right edge touched
                self.velocity[i] = -self.velocity[i]

    def draw(self):
        # Draw the Ball on the surface
        # - self is the Ball

        pygame.draw.circle(self.surface, self.color, self.center, self.radius)


main()
