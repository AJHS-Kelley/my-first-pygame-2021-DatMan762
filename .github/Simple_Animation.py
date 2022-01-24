# Simple Animation with PyGame, Bernard Samuels, 1/24/21, 1:49PM, v0.1

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