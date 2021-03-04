import pygame
import sys
import random
import numpy as np
from math import *

FPS = 60
W = 700
H = 700

BLACK    =   (0, 0, 0)
WHITE    =   (255, 255, 255)
RED      =   (245, 10, 10)

pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Fractal')

def main():
    sc.fill(BLACK)
    # a = [[3,1],[7,1],[1,5],[9,5],[5,9]]
    a = [[5,1],[9,8],[1,8]]
    for i in a:
        line(i[0],i[1])
    x = 4
    y = 3
    for i in range(10000):
        # clock.tick(1)
        ch = random.randint(0, len(a)-1) 
        x,y = pline(x,y,a[ch][0],a[ch][1])
        pygame.display.update()
    while True:    
        clock.tick(FPS)
        for i in pygame.event.get():
            if i.type == pygame.QUIT: exit()
        pygame.display.update()

def line(x,y):
    mn = 70
    pygame.draw.line(sc, RED, (x*mn,y*mn), (x*mn,y*mn), 1)
def pline(x,y,x1,y1):
    xx = (x + x1) / 2
    yy = (y + y1) / 2
    mn = 70
    pygame.draw.line(sc, WHITE, (xx*mn,yy*mn), (xx*mn,yy*mn), 1)
    return xx,yy

main()