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
# move geometric shapes on screen

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

    # loop to continue game as long as player doesn't close the window
    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        # draw purple circle
        circle_color = pygame.Color("purple")
        circle_pos = (150, 150)
        circle_radius = 100
        pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
        # draw green rectangle
        rect_left = 0
        rect_top = 0
        rect_width = 200
        rect_height = 50
        rect_color = pygame.Color("green")
        green_rect = pygame.Rect(rect_left, rect_top, rect_width, rect_height)
        pygame.draw.rect(screen, rect_color, green_rect)
        # draw image to screen at position ball_pos
        ball = pygame.image.load("intro_ball.gif")
        ball_pos = (300, 270)
        screen.blit(ball, ball_pos)

        # render text to screen
        text_string = "Hello, World!"
        text_font = pygame.font.SysFont(
            "Comic Sans", 45)
        text_color = pygame.Color("blue")
        text_image = text_font.render(text_string, True, text_color)
        text_pos = (0, 0)
        screen.blit(text_image, text_pos)

        # update display all at once
        pygame.display.flip()


main()
