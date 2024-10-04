import pygame
import sys
import pygame.locals as pl
import numpy as np

class Point:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = 0.1
        self.vel_y = 0.1

    def draw_point(self):
        pygame.draw.rect(DISPLAYSURF, RED, (self.pos_x ,self.pos_y,10,10))


    def direction_to_mouse(self):
        [pos_x_mouse,pos_y_mouse]=pygame.mouse.get_pos()    
        dir_x = (pos_x_mouse - self.pos_x) 
        dir_y = (pos_y_mouse - self.pos_y) 
        
        vec_pos = np.array([dir_x, dir_y])
        vel = np.array(vec_pos)/((vec_pos**2).sum()**0.5)
        
        self.vel_x += vel[0]*1.1
        self.vel_y += vel[1]*1.1
    
    def velocity_limit(self):
        if np.linalg.norm([self.vel_x, self.vel_y])>=5.:
            self.vel_x = self.vel_x * 0.8
            self.vel_y = self.vel_y * 0.8

    def update_position(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

def display_game():
            # We display a colection of points
    Point_1 = Point(200,200)
    while True:

        DISPLAYSURF.fill(WHITE)  
        Point_1.draw_point()
        Point_1.direction_to_mouse()
        Point_1.velocity_limit()
        Point_1.update_position()
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
pygame.display.set_caption("hello World")

display_game()

