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
    aks = 'A'
    for i in range(5):
        aks1 = ''
        for i in range(len(aks)):
            if aks[i] == 'A':
                aks1 += 'AB'
            elif aks[i] == 'B':
                aks1 += 'A'
        aks = aks1
    print(aks)
    x,y =0, 0
    dl = 10
    for i in range(len(aks)):
        if aks[i] == 'A':
            line(x,y,x,y+dl)
            y+=dl
        if aks[i] == 'B':
            line(x,y,x+dl,y)
            x+=dl
        pygame.display.update()
    while True:    
        clock.tick(FPS)
        for i in pygame.event.get():
            if i.type == pygame.QUIT: exit()
        pygame.display.update()

def line(x1,y1,x2,y2,k=1):
    pygame.draw.line(sc, WHITE, (x1*k,y1*k), (x2*k,y2*k), 1)

main()