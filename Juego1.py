# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 08:45:33 2024

@author: icmat
"""

import pygame, sys
import pygame.locals as pl


def iniciar_rectangulo():     
    while True:
        for event in pygame.event.get():
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()


BLACK = (  10,   10,   10)
WHITE = (240, 240, 240)
RED = (255,   10,   10)
GREEN = (  10, 255,   10)
BLUE = (  10,   10, 255)

# draw on the surface object

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')
DISPLAYSURF.fill(WHITE)


for i in range(0,15 ):
    pygame.draw.rect(DISPLAYSURF, RED, (250+ 10*i,200+ 10*i, 10, 10))

pygame.display.set_caption("hello World")
iniciar_rectangulo()




