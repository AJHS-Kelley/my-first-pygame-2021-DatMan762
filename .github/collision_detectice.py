        # PyGame Collision Detection Practice, Bernard Samuels, february 07, 2022, 1:41pm, 0v.2

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