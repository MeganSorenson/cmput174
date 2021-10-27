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

        # create pong ball
        self.ball = Ball(
            'white', 5, [size[0] / 2, size[1] / 2], [4, 4], self.surface)
        # create two paddles for each player
        self.left_paddle = Paddle(
            'white', 10, 50, [100, 200], "L", [0, 10], self.surface)
        self.right_paddle = Paddle(
            'white', 10, 50, [400, 200], "R", [0, 10], self.surface)
        self.left_direction = 0
        self.right_direction = 0

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
                self.handle_key_down(event)
            if event.type == pygame.KEYUP:
                self.handle_key_up(event)

    def handle_key_up(self, event):
        # stops movement
        # have to do it separately so that both players can move independently from one another
        if event.key == pygame.K_p or event.key == pygame.K_l:
            self.right_direction = 0
        if event.key == pygame.K_q or event.key == pygame.K_a:
            self.left_direction = 0

    def handle_key_down(self, event):
        if event.key == pygame.K_p:
            # right paddle move up
            self.right_direction = 1
        if event.key == pygame.K_l:
            # right paddle move down
            self.right_direction = -1
        if event.key == pygame.K_q:
            # left paddle move up
            self.left_direction = 1
        if event.key == pygame.K_a:
            # left paddle move down
            self.left_direction = -1

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color)  # clear the display surface first
        self.ball.draw()
        self.left_paddle.draw()
        self.right_paddle.draw()
        pygame.display.update()  # make the updated surface appear on the display

    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update
        self.ball.move()
        self.left_paddle.move(self.left_direction)
        self.right_paddle.move(self.right_direction)
        left_collide = self.left_paddle.collide_ball(self.ball)
        right_collide = self.right_paddle.collide_ball(self.ball)
        self.ball.paddle_bounce(left_collide, right_collide)

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

    def get_horizontal_direction(self):
        if self.velocity[0] > 0:
            direction = "R"
        else:
            direction = "L"
        return direction

    def paddle_bounce(self, left_collide, right_collide):
        if left_collide or right_collide:
            self.velocity[0] = -self.velocity[0]

    def move(self):
        # Change the location of the Ball by adding the corresponding
        # speed values to the x and y coordinate of its center
        # - self is the Ball
        size = self.surface.get_size()

        # continue moving until hits window edge or paddle
        # if hits edge or paddle, bounce by reversing velocity sign
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


class Paddle:
    # An object in this class represents a rectangular Paddle
    # moves using key commands
    def __init__(self, rect_color, rect_width, rect_height, rect_left_top, side, rect_velocity, surface):
        # Initialize a Paddle.
        # - self is the paddle to initialize
        # - color is the pygame.Color of the paddle
        # - width is the int pixel width of the paddle
        # - height is the int pixel height of the paddle
        # - velocity is a list containing the x and y components
        # - left is the x coordinate of the top left corner
        # - top is the y coordinate of the top left corner
        # - surface is the window's pygame.Surface object

        self.color = pygame.Color(rect_color)
        self.width = rect_width
        self.height = rect_height
        self.left_top = rect_left_top
        self.side = side
        self.velocity = rect_velocity
        self.surface = surface

    def collide_ball(self, Ball):
        collide = False
        # need to still make getter functions in Ball class
        if self.side == "L" and Ball.get_horizontal_direction() == "L":
            if Ball.center[0] - Ball.radius <= self.left_top[0] + self.width and Ball.center[0] - Ball.radius >= self.left_top[0]:
                if Ball.center[1] > self.left_top[1] and Ball.center[1] < self.left_top[1] + self.height:
                    collide = True
        elif self.side == "R" and Ball.get_horizontal_direction() == "R":
            if Ball.center[0] + Ball.radius >= self.left_top[0] and Ball.center[0] + Ball.radius <= self.left_top[0] + self.width:
                if Ball.center[1] > self.left_top[1] and Ball.center[1] < self.left_top[1] + self.height:
                    collide = True
        return collide

    def move(self, direction):
        # Change the location of the Paddle using key inputs
        # can only move vertically and moves with different key input depedning on Paddle side
        # - self is the Paddle
        size = self.surface.get_size()
        # move paddle up unless it hits top edge
        if direction == 1 and not self.left_top[1] == 0:
            self.left_top[1] -= self.velocity[1]
        # move paddle down unless it hits bottom edge
        if direction == -1 and not self.left_top[1] + self.height >= size[1]:
            self.left_top[1] += self.velocity[1]

    def draw(self):
        # Draw the Paddle on the surface
        # - self is the Paddle
        self.rect = pygame.Rect(
            self.left_top[0], self.left_top[1], self.width, self.height)

        pygame.draw.rect(self.surface, self.color, self.rect)


# need to bounce the paddle back it it hits the sides in move method
# catch return in update to change score in game class
# use this when writing pong ball hitting sides score
# create draw_score method withhin game class
# if self.rect.right >=self.surface.get_width:
#   self.rect.right = self.surface.get_width - self.rect.width
#   edge = "right"
# elif self.rect.left <= 0:
#   self.rect.left = self.rect.width
#   edge = "left"
# return edge
main()
