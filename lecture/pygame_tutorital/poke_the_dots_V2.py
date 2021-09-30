# Poke The Dots
# in this game, the user tries to prevent two moving dots from colliding by
# pressing and reeleasing the mouse button to teleport the dots to a random location
# the score is the number of seconds from the start of the game until the dots collide

# STEP 1
# learn how to open a graphical window - DONE
# set title window - DONE
# draw basic geometric shapes - DONE
# change color of geometric shapes - DONE
# respond to user input (close window) - DONE

# STEP 2
# display image on screen - DONE
# render text to screen at different locations - DONE
# render text to screen in different colors - DONE
# move/animate geometric shapes on screen - DONE

# BONUS GOALS 3
# make sure geometric shapes stay within screen boundaries while they are moving
# track the passage of time

import pygame


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
    run_game = True

    # initialize game objects
    bg_color = pygame.Color("black")

    game_clock = pygame.time.Clock()
    frames_per_second = 30

    circle_pos = [150, 150]
    circle_velocity = [1, 1]
    circle_color = pygame.Color("green")
    circle_radius = 30

    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        # draw dot to screen and then move its location for next time
        # creates the illusion of motion
        screen.fill(bg_color)
        pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
        for index in range(0, 2):
            circle_pos[index] += circle_velocity[index]

        # render all drawn objects to the screen
        pygame.display.flip()
        # set framerate so doesn't move too fast
        game_clock.tick(frames_per_second)


main()
