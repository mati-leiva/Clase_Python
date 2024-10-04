# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 08:45:33 2024

@author: icmat
"""

import pygame
import sys
import pygame.locals as pl
import math


def iniciar_rectangulo():
    while True:
        for event in pygame.event.get():
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()


# Iniciamos los colores
BLACK = (10,   10,   10)
WHITE = (240, 240, 240)
RED = (255,   10,   10)
GREEN = (10, 255,   10)
BLUE = (10,   10, 255)
# Mostramos un display
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')
DISPLAYSURF.fill(WHITE)
# Mostramos una colecciòn de puntos
for i in range(0, 40):
    pygame.draw.rect(DISPLAYSURF, RED, (250 + 40 *math.cos(i), 200 + 40*math.sin(i), 2, 2))
    
pygame.display.set_caption("hello World")
iniciar_rectangulo()
