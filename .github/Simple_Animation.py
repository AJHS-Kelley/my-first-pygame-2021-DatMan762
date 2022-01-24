# Simple Animation with PyGame, Bernard Samuels, 1/24/21, 1:49PM, v0.4

import pygame, sys, time
from pygame.locals import *

# setup PyGame
pygame.intit()

#setup the Window
WINDOWWIDTH = 400
WINDOWWIDTH = 400
windowSurface = pygame.displayset_mode((WINDOWWIDTH,WINDOWHEIGHT),0, 32)
pygame.display.set_caption('Animatiom Example!')

# Setup the direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# setup color values.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)


# setup the box data.
 b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
 b2 ={'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
 b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
 boxes = [b1, b2, b3]