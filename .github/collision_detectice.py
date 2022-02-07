        # PyGame Collision Detection Practice, Bernard Samuels, february 07, 2022, 1:41pm, 0v.5

        import pygame, sys, random
        from pygame.locals import *

        # setup PyGame
        pygame.init()
        mainClock = pygame.time.Clock()

        # Setup the PyGame window 
        WINDOWWIDTH = 400
        WINDOWHEIGHT = 400
        windowSurface = pygame.display.set_mode(WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
        pygame.display.set_caption('Collision Detection 2022')

        #setup colors.
        Black = (0, 0, 0)
        Green = (0,255,0)
        White = (255,255,255)

# setup the player and food data structures.
NEWFOOD = 40
FOODSIZE = 20
player = pygame. Rect(300, 100, 50, 50)
foods = []

for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# Movement Variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6