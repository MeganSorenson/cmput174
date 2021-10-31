# Pong
# a classic Atari-esk pong game where two players can move a paddle to try and bounce a moving ball off of
# if a player bounces the ball and it hits the opposite window edge, the player gains a point
# the first player to reach 11 points wins

# https://pypi.org/project/pygame/
import pygame


# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window of (width, height)
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
        # self is the Game to initialize
        # surface is the display window surface object

        # === objects that are part of every game
        self.surface = surface
        # set background color of surface
        self.bg_color = pygame.Color('black')

        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        # initially, window 'x' is not clicked and game continues
        self.close_clicked = False
        self.continue_game = True

        # === game specific objects
        # get size (width, height) of the game surface
        # for later use in creating objects
        size = self.surface.get_size()

        # create pong ball
        #   white ball initially in the middle of the surface
        self.ball = Ball(
            'white', 5, [size[0] / 2, size[1] / 2], [6, 2], self.surface)

        # create two paddles for each player usig the Paddle class
        #   left paddle is placed 1/5 way into surface
        #   right paddle is place 4/5 way in surface
        paddle_width = 10
        paddle_height = 40
        self.left_paddle = Paddle(
            'white', paddle_width, paddle_height, [size[0] / 5, (size[1] - paddle_height) / 2], "L", [0, 10], self.surface)
        self.right_paddle = Paddle(
            'white', paddle_width, paddle_height, [4 * size[0] / 5, (size[1] - paddle_height) / 2], "R", [0, 10], self.surface)

        # initially, left and right paddles are not moving in any direction
        self.left_direction = 0
        self.right_direction = 0

    def play(self):
        # Play the game until the player presses the close box.
        # self is the Game that should be continued or not.
        # return NoneType

        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()
            # continues to update game objects until the game is over
            if self.continue_game:
                self.update()
                self.decide_continue()
            # run at most with FPS Frames Per Second
            self.game_Clock.tick(self.FPS)

    def handle_events(self):
        # Handle each user event by changing the game state appropriately
        # or by calling the appropriate event method within the Game
        # self is the Game whose events will be handled
        # returns NoneType

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            if event.type == pygame.KEYDOWN:
                self.handle_key_down(event)
            if event.type == pygame.KEYUP:
                self.handle_key_up(event)

    def handle_key_up(self, event):
        # stops paddle movement by setting direction of the paddles to 0
        # paddles stop independently of one another
        # self is the Game whose event is being handled
        # event is an object of type pygame.Event
        # returns NoneType

        if event.key == pygame.K_p or event.key == pygame.K_l:  # stop right paddle movement
            self.right_direction = 0
        if event.key == pygame.K_q or event.key == pygame.K_a:  # stop left paddle movement
            self.left_direction = 0

    def handle_key_down(self, event):
        # starts paddle movement by setting correct direction to 1 (up) or -1 (down)
        # paddle move independently of one another
        # self is the Game whose event is being handled
        # event is an object of type pygame.Event
        # returns NoneType

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
        # self is the Game to draw
        # returns NoneType

        self.surface.fill(self.bg_color)  # clear the display surface first
        # draw ball and paddles
        self.ball.draw()
        self.left_paddle.draw()
        self.right_paddle.draw()
        # draw score board on both sides
        self.draw_scores()
        pygame.display.update()  # make the updated surface appear on the display

    def draw_scores(self):
        # draws score board on left and right sides
        # drawn score shows how mnay times the ball has hit the window edge on the side of the opposite paddle
        # returns NoneType

        # get left and right window hit tallies from the Ball object
        left_hits = self.ball.get_left_hits()
        right_hits = self.ball.get_right_hits()

        # create strings of the hit tallies
        left_score_string = str(right_hits)
        right_score_string = str(left_hits)
        # create font object
        font_size = 80
        font = pygame.font.SysFont("", font_size)
        # render font for both left and right sides
        fg_color = pygame.Color("white")
        left_text_box = font.render(left_score_string, True,
                                    fg_color, self.bg_color)
        right_text_box = font.render(right_score_string, True,
                                     fg_color, self.bg_color)
        # compute location for both left and right sides
        location_left = (2, 0)
        if left_hits >= 10:  # nudges text further if two digits
            location_right = (self.surface.get_width() - 60, 0)
        else:  # nudges text less if one digit
            location_right = (self.surface.get_width() - 30, 0)

        # blit source surface on target surface at specified location for left and right sides
        self.surface.blit(left_text_box, location_left)
        self.surface.blit(right_text_box, location_right)

    def update(self):
        # Update the game objects for the next frame.
        # self is the Game to update
        # returns NoneType

        # first move paddles in direction based on keydown and keyup events
        self.left_paddle.move(self.left_direction)
        self.right_paddle.move(self.right_direction)
        # check if ball has collided with either paddle
        left_collide = self.left_paddle.collide_ball(self.ball)
        right_collide = self.right_paddle.collide_ball(self.ball)
        # if ball has collided, change sign of ball's horizontal velocity
        self.ball.paddle_bounce(left_collide, right_collide)
        # check if ball hit either side of window
        self.ball.left_right_window_hit()
        # move ball according to velocity
        self.ball.move()

    def decide_continue(self):
        # Check and remember if the game should continue
        # self is the Game to check
        # returns NoneType

        # if one of player's scores (determines by window edge hits on the opposite side) reaches 11
        # stop drawing and updating game objects
        if self.ball.get_left_hits() == 11 or self.ball.get_right_hits() == 11:
            self.continue_game = False


class Ball:
    # An object in this class represents a Ball that moves and bounces

    def __init__(self, ball_color, ball_radius, ball_center, ball_velocity, surface):
        # Initialize a Ball.
        # self is the Ball to initialize
        # ball_color is the pygame.Color of the Ball
        # ball_radius is the int pixel radius of the Ball
        # ball_center is a list containing the x and y int coords of the center of the Ball
        # ball_velocity is a list containing the x and y components
        # surface is the window's pygame.Surface object

        self.color = pygame.Color(ball_color)
        self.radius = ball_radius
        self.center = ball_center
        self.velocity = ball_velocity
        self.surface = surface
        self.surface_size = self.surface.get_size()

        # initially, ball has not hit left nor right side of window
        # used to keep track of score
        self.right_side_hits = 0
        self.left_side_hits = 0

    def get_horizontal_direction(self):
        # fetches horizontal direction of ball by chekcing velocity sign
        # self is the Ball object
        # returns string which represents the horizontal direction of the ball
        # "R" means moving towards the right of the screen, "L" means moving towards the left of the screen

        if self.velocity[0] > 0:
            direction = "R"
        else:
            direction = "L"
        return direction

    def get_center(self):
        # fetches list containg x and y coordinates of the center of the Ball
        # self is the Ball object
        # returns list of integers representing centre of the ball
        return self.center

    def get_radius(self):
        # fetches radius of the Ball
        # self is the Ball object
        # returns integer representing the radius of the ball
        return self.radius

    def get_left_hits(self):
        # fetches how may times the ball has hit the left side of the window
        # self is the Ball object
        # returns integer representing the right paddle's score for the game
        return self.left_side_hits

    def get_right_hits(self):
        # fetches how may times the ball has hit the right side of the window
        # self is the Ball object
        # returns integer representing the left paddle's score for the game
        return self.right_side_hits

    def paddle_bounce(self, left_collide, right_collide):
        # if the ball has collided with the left or right paddle,
        # change the direction of the Ball's horizontal velocity to bounce off paddle
        # self is the Ball object moving
        # left_collide is a bool representing whether or not the ball has hit the left paddle
        # right_collide is a bool representing whether or not the ball has hit the right paddle
        # returns NoneType

        if left_collide or right_collide:
            self.velocity[0] = -self.velocity[0]

    def left_right_window_hit(self):
        # checks if ball has hit the left or right side of the window surface
        # appropriately tallies window side hits to self.right_sode_hits or self.left_side hits
        # self is the Ball moving
        # returns NoneType

        if self.center[0] + self.radius > self.surface_size[0]:
            self.right_side_hits += 1
        elif self.center[0] < self.radius:
            self.left_side_hits += 1

    def move(self):
        # Change the location of the Ball by adding the corresponding speed values to the x and y coordinate of its center
        # self is the Ball moving
        # continue moving until hits window edge
        # if hits edge, bounce by reversing appropriate velocity sign
        # returns NoneType

        for i in range(0, 2):
            self.center[i] = (self.center[i] + self.velocity[i])
            if self.center[i] < self.radius:
                # left or top edge touched
                self.velocity[i] = - self.velocity[i]
            elif self.center[i] + self.radius > self.surface_size[i]:
                # bottom or right edge touched
                self.velocity[i] = -self.velocity[i]

    def draw(self):
        # Draw the Ball on the surface based on intitialized characteristics
        # self is the Ball
        # returns NoneType

        pygame.draw.circle(self.surface, self.color, self.center, self.radius)


class Paddle:
    # An object in this class represents a rectangular Paddle that moves using key commands

    def __init__(self, rect_color, rect_width, rect_height, rect_left_top, side, rect_velocity, surface):
        # Initialize a Paddle.
        # self is the paddle to initialize
        # rect_color is the pygame.Color of the paddle
        # rect_width is the int pixel width of the paddle
        # rect_height is the int pixel height of the paddle
        # rect_left_top is a list of the the x and y coordinates of the top left corner
        # rect_velocity is a list containing the x and y components
        # surface is the window's pygame.Surface object

        self.color = pygame.Color(rect_color)
        self.width = rect_width
        self.height = rect_height
        self.left_top = rect_left_top
        self.side = side
        self.velocity = rect_velocity
        self.surface = surface

    def collide_ball(self, Ball):
        # check if Ball object has hit the Paddle
        # self is the Paddle object
        # Ball is an object of class Ball
        # returns a bool representing whther the Ball and Paddle have collided or not

        # initially, Paddle has not collided with anything
        collide = False
        # checks first which paddle it is and that ball is moving in right direction
        if self.side == Ball.get_horizontal_direction():
            # then checks that horizontal coordinates of Ball are colliding with paddle horizontal coordinates
            if Ball.get_center()[0] - Ball.get_radius() <= self.left_top[0] + self.width and Ball.get_center()[0] - Ball.get_radius() >= self.left_top[0]:
                # then checks if vertical coordinates of ball are within vertical coordinates of paddle
                if Ball.get_center()[1] >= self.left_top[1] and Ball.get_center()[1] <= self.left_top[1] + self.height:
                    # if all checks satisfied, ball has collided with paddle
                    collide = True
        return collide

    def move(self, direction):
        # Change the location of the Paddle
        # can only move vertically
        # self is the Paddle that is moving
        # direction is an integer representing the direction of movement of the paddle,
        # based on key inputs (0 = not moving, 1 = moving up, -1 = moving down)
        # returns NoneType

        size = self.surface.get_size()
        # move paddle up unless it hits top edge
        if direction == 1 and not self.left_top[1] == 0:
            self.left_top[1] -= self.velocity[1]
        # move paddle down unless it hits bottom edge
        if direction == -1 and not self.left_top[1] + self.height >= size[1]:
            self.left_top[1] += self.velocity[1]

    def draw(self):
        # Draw the Paddle on the surface based on initialized characteristics
        # self is the Paddle
        # returns NoneType
        self.rect = pygame.Rect(
            self.left_top[0], self.left_top[1], self.width, self.height)

        pygame.draw.rect(self.surface, self.color, self.rect)


main()
