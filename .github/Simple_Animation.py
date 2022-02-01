# Simple Animation with PyGame, Bernard Samuels, 1/24/21, 1:49PM, v0.7

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

 # Run the game loop.
 while True: 
     # Check for QUIT event.
     for event in pygame.event.get():
         if event.type == QUIT:
             pyhame.quit()
             sys.exit()

       windowSurface.fill(WHITE)

       for b in boxes:
           # Move the box data structure.
           if b['dir'] == DOWNLEFT:
               b['rect'].left -= MOVESPEED 
               b['rect'].top += MOVESPEED 
               if b['dir'] == DOWNRIGHT:
                   b['rect'].left += MOVESPEED 
             # Move the box data structure.
           if b['dir'] == DOWNLEFT:
               b['rect'].left -= MOVESPEED 
               b['rect'].top += MOVESPEED 
               if b['dir'] == DOWNRIGHT:
                   b['rect'].left += MOVESPEED 
                    b['rect'].top += MOVESPEED 

              if b['rect'].top < 0:
                # the box has moved past the top.
                if b['rect'] == UPLEFT:
                    b['dir'] = DOWNLEFT:
                 if b['rect'] == UPRIGHT:
                    b['dir'] = DOWNRIGHT:   
                if b['rect'].bottom > WINDOWHEIGHT:
                    # the box has moved past the bottom.
                if b['rect'] == DOWNLEFT:
                    b['dir'] = UPLEFT:
                 if b['rect'] == DOWNRIGHT:
                    b['dir'] = UPRIGHT:
                  if b['rect']. < 0:      