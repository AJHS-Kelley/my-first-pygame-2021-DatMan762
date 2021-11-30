 # My First PyGame, Bernard Samuels, 11/30/21, 2:14, v0.5

 import pygame, sys 
 from pygame.locals import *

 # Start Pygame 
  pygame.intit()

   # Setup the game window 
   windowSurface = pygame,display.set_mode((500,400)),0,32)
   pygame.display.set_caption('Hello, world')

   # Setup color values.
   BLACK = (0,0,0)
   White = (255,255,255)
   RED = (255,0,0)
   Green = (0,255,0)
   Blue = (0,0,255)
   violet = (125,255,25)

   # Setup fonts.
   basicFont = pygame.font.SysFont(None,48)
   textRect =text,get_rect()
   textRect.centerx = windowSurface.get_rect().centerx
   textRect.centerx = windowSurface.get_rect().centery
   

   # Draw the game background 
   windowSurface.fill(LAVARED)