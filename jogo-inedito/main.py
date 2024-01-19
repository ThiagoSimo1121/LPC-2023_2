# importing required library
import pygame

# activate the pygame library.
pygame.init()
X = 900
Y = 600

# create the display surface object
# of specific dimension..e(X, Y).
screen = pygame.display.set_mode((X, Y))

# Cor dos paddles
paddle_color = (250, 250, 250)
#

# set the pygame window name
pygame.display.set_caption('image')

# create a surface object, image is drawn on it.
imp = pygame.image.load("./assets/jogo-campo.jpg").convert()

# Using blit to copy content from one surface to other
screen.blit(imp, (0, 0))

# Rects
# player rects
player_front_paddle = pygame.draw.rect(screen, paddle_color, pygame.Rect(340, 250, 10, 90))
player_back_paddle = pygame.draw.rect(screen, paddle_color, pygame.Rect(90, 275, 10, 45))
# ia rects
ia_front_paddle = pygame.draw.rect(screen, paddle_color, pygame.Rect(560, 250, 10, 90))
ia_back_paddle = pygame.draw.rect(screen, paddle_color, pygame.Rect(810, 275, 10, 45))

# paint screen one time
pygame.display.flip()
status = True
while status:

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for i in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False

# deactivates the pygame library
pygame.quit()
