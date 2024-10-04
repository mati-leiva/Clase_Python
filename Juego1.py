# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 08:45:33 2024

@author: icmat
"""

import pygame, sys
import pygame.locals

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption("hello World")
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()