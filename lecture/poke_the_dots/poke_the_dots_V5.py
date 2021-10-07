# Poke The Dots
# in this game, the user tries to prevent two moving dots from colliding by
# pressing and reeleasing the mouse button to teleport the dots to a random location
# the score is the number of seconds from the start of the game until the dots collide

# some of the source code contained in this program is not original
# it was borrowed from a tutorital found on pygame's website
# specifically, this program uses portions of this tutorital to respond to QUIT events
# and to understand how to use the flip() function to render graphics
# https://www.pygame.org/docs/tut/PygameIntro.html

import pygame


class Game:
    def __init__(self, screen):
        # attributes of all games
        self.screen = screen

        self.bg_color = pygame.Color("black")
        self.game_clock = pygame.time.Clock()
        self.frames_per_second = 30

        self.run_game = True
        self.game_over = False

        # attributes specific to poke the dots
        red_dot_pos = [50, 50]
        red_dot_velocity = [1, 2]
        red_dot_color = pygame.Color("red")
        red_dot_radius = 30

        blue_dot_pos = [200, 100]
        blue_dot_velocity = [2, 1]
        blue_dot_color = pygame.Color("blue")
        blue_dot_radius = 20

        self.red_dot = Dot(red_dot_pos, red_dot_velocity,
                           red_dot_color, red_dot_radius)
        self.blue_dot = Dot(blue_dot_pos, blue_dot_velocity,
                            blue_dot_color, blue_dot_radius)

        self.frame_counter = 0
        self.max_frames = 100

    def play(self):
        # play game until player closes window
        while self.run_game:
            self.handle_events()
            self.draw()

            # look at game-over conditions
            if not self.game_over:
                self.update()
                self.check_game_over()

            # set framerate so doesn't move too fast
            self.game_clock.tick(self.frames_per_second)

    def handle_events(self):
        # check for new event generaeted by user input
        # and change game state appropriately
        # continues game as long as player doesn't close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run_game = False

    def draw(self):
        # draws all game objects to screen

        # clear screen
        self.screen.fill(self.bg_color)
        # draw dot to screen
        self.red_dot.draw(self.screen)
        self.blue_dot.draw(self.screen)
        # render all drawn objects to the screen
        pygame.display.flip()

    def check_game_over(self):
        # check and remeber if game should continue
        if self.frame_counter > self.max_frames:
            self.game_over = True

    def update(self):
        # update all of game's objects
        self.red_dot.move()
        self.blue_dot.move()
        self.frame_counter += 1


class Dot:
    # represents a single dot in the game
    def __init__(self, position, velocity, color, radius):
        # position is a list of [x,y] coordinates
        # velocity is a list of [x,y] coordinates
        # color is a str of color name or a list of rgb characters
        # radius is a float
        self.position = position
        self.velocity = velocity
        self.color = pygame.Color(color)
        self.radius = radius

    def move(self):
        # change location of the dot
        # by adding speed [x,y] to position [x,y] coordinates
        for index in range(0, 2):
            self.position[index] += self.velocity[index]

    def draw(self, screen):
        # draw dot on the game's window
        pygame.draw.circle(screen, self.color, self.position, self.radius)


def main():
    # initialize pygame
    pygame.init()

    # create graphical window (width, height)
    size = (500, 400)
    screen = pygame.display.set_mode(size)
    # set title of the window
    pygame.display.set_caption("Poke The Dots")

    # initialize game
    Poke_the_Dots = Game(screen)
    # call main game play method
    Poke_the_Dots.play()


main()
