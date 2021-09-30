# Poke The Dots
# in this game, the user tries to prevent two moving dots from colliding by
# pressing and reeleasing the mouse button to teleport the dots to a random location
# the score is the number of seconds from the start of the game until the dots collide

# BONUS GOALS
# make sure geometric shapes stay within screen boundaries while they are moving
# track the passage of time

# some of the source code contained in this program is not original
# it was borrowed from a tutorital found on pygame's website
# specifically, this program uses portions of this tutorital to respond to QUIT events
# and to understand how to use the flip() function to render graphics
# https://www.pygame.org/docs/tut/PygameIntro.html

import pygame


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

    # == Main Game Loop
    # each iteration over the loop will draw the dot at a static location
    # we will then move the dot a small amount and redraw the dot
    # repeat many times a second to give the appearance of motion
    # continue game as long as player doesn't close the window

    # handle user input
    # draw game objects
    # check for game-over conditions
    # if game-over conditions are not yet met, update the game state

    # initialize game objects

    # game object that are general to games
    bg_color = pygame.Color("black")
    game_clock = pygame.time.Clock()
    frames_per_second = 30

    run_game = True
    game_over = False

    # game objects that are specific to poke the dots
    green_dot_pos = [150, 150]
    green_dot_velocity = [1, 2]
    green_dot_color = pygame.Color("green")
    green_dot_radius = 30

    purple_dot_pos = [300, 150]
    purple_dot_velocity = [2, 1]
    purple_dot_color = pygame.Color("purple")
    purple_dot_radius = 20

    green_dot = Dot(green_dot_pos, green_dot_velocity,
                    green_dot_color, green_dot_radius)
    purple_dot = Dot(purple_dot_pos, purple_dot_velocity,
                     purple_dot_color, purple_dot_radius)

    frame_counter = 0
    max_frames = 100

    while run_game:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        # draw game objects

        # clear screen
        screen.fill(bg_color)
        # draw dot to screen
        green_dot.draw(screen)
        purple_dot.draw(screen)

        # render all drawn objects to the screen
        pygame.display.flip()

        # look at game-over conditions
        if not game_over:
            # update game objects (move dot to new location)
            green_dot.move()
            purple_dot.move()
            # update frame counter
            frame_counter += 1
            # check if game_over conditions are met
            if frame_counter > max_frames:
                game_over = True

        # set framerate so doesn't move too fast
        game_clock.tick(frames_per_second)


main()
