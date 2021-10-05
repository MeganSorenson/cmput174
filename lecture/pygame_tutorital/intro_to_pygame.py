import sys
import pygame
# most big packages of software will need to be initialized
# before they can be used
pygame.init()

# create tuple with height and width of something
size = width, height = 800, 600
# how fast on the x and y axis that the ball is moving
speed = [2, 2]
black = 0, 0, 0

# return object 'screen'
screen = pygame.display.set_mode(size)

# loading an image from file and assigning variable
# returns surface that has the contents on that image on it
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

# loop that repeats indefinitely
while 1:
    for event in pygame.event.get():
        # when you click 'x' the program terminates
        if event.type == pygame.QUIT:
            sys.exit()

    # not moving ball but ballrect
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # fills surface with a solid color
    # gives the illusion of frame-by-frame rendering
    screen.fill(black)
    # instructions to draw ball image onto ballrect image
    screen.blit(ball, ballrect)
    # updates the contents of the entire display
    # draws all the things at once
    pygame.display.flip()
