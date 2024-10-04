import pygame
import sys
import pygame.locals as pl
import math


class Point:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        [pos_x_mouse,pos_y_mouse]=pygame.mouse.get_pos()    
        self.vel_x = (pos_x_mouse - self.pos_x)
        self.vel_y = (pos_y_mouse - self.pos_y)
        Point.normalice_vel(self)
        Point.update_position(self)

    def draw_point(self):
        pygame.draw.rect(DISPLAYSURF, RED, (self.pos_x ,self.pos_y,2,2))

    def normalice_vel(self):
        self.vel_x = self.vel_x / (self.vel_x^2 + self.vel_y^2)
        self.vel_y = self.vel_y / (self.vel_x^2 + self.vel_y^2)

    def update_position(self):

        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

def display_game():
    while True:
        

        Point_1 = Point(201,201)
        Point_1.draw_point()

        for event in pygame.event.get():
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()
        clock.tick(60)
        


# Starting the colors
BLACK = (10,   10,   10)
WHITE = (240, 240, 240)
RED = (255,   10,   10)
GREEN = (10, 255,   10)
BLUE = (10,   10, 255)
# Seting up the display

DISPLAYSURF = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('Drawing')
clock = pygame.time.Clock()
DISPLAYSURF.fill(WHITE)
# We display a colection of points
  
pygame.display.set_caption("hello World")

display_game()

