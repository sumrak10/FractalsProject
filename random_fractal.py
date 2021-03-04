import pygame
import sys
import random
import numpy as np

FPC = 1000
W = 500
H = 500
cell_w = 5
width = W // cell_w
height = H // cell_w

BLACK    =   (0, 0, 0)
WHITE    =   (255, 255, 255)
ORANGE   =   (255, 150, 100)
BLUE     =   (0, 70, 225)
YELLOW   =   (255, 255, 0)
GREEN    =   (0, 255, 0)

pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Life')

class World:
    def __init__(self,w,h):
        self.world_w = w
        self.world_h = h
        self.world = np.zeros((w,h))
        self.x = w // 2
        self.y = h // 2
        self.x1 = self.x-5
        self.y1 = self.y-5
        self.x2 = self.x+5
        self.y2 = self.y+5
    def drawCell(self, x, y, col=0):
        if col == 0:
            color = WHITE
        elif col == 1:
            color = GREEN
        elif col == 2:
            color = BLACK
        elif col == 3:
            color = YELLOW
        pygame.draw.rect(sc, color, (x*cell_w, y*cell_w, cell_w, cell_w))
    def Logic(self):
        xd = random.randint(-1,1)
        yd = random.randint(-1,1)
        if ((self.x + xd) > self.x1 ) or ((self.y + yd) < self.y1 ) or ((self.x + xd) < self.x2 ) or ((self.y + yd) > self.y2 ):
            self.x += xd
            self.y += yd
        self.drawCell(self.x, self.y, 1)
        self.drawCell(self.x-xd, self.y-yd, 2)
        neighbours = self.world[self.x-1][self.y-1] + self.world[self.x][self.y-1] + self.world[self.x+1][self.y-1] + self.world[self.x-1][self.y] + self.world[self.x+1][self.y] + self.world[self.x-1][self.y+1] + self.world[self.x][self.y+1] + self.world[self.x+1][self.y+1]
        if neighbours > 0:
            self.world[self.x][self.y] = 1
            self.drawCell(self.x,self.y)
            self.x1 = self.x-5
            self.y1 = self.y-5
            self.x2 = self.x+5
            self.y2 = self.y+5
            self.x = self.x1
            self.y = self.y1
            self.drawCell(self.x1,3)
            self.drawCell(self.y1,3)
            self.drawCell(self.x2,3)
            self.drawCell(self.y2,3)

if __name__ == "__main__":
    w = World(width,height)
    w.world[width//2][height//2] = 1
    w.drawCell(width//2,height//2)
    while True:    
        clock.tick(FPC)
        w.Logic()
        for i in pygame.event.get():
            if i.type == pygame.QUIT: exit()
        pygame.display.update()