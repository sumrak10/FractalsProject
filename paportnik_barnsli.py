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
GREEN    =   (0, 255, 0)

pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Fractal')

def main():
    sc.fill(BLACK)
    afin = [[0,0,0,0.16,0,0],[0.85,0.04,-0.04,0.85,0,1.6],[0.2,-0.26,0.23,0.22,0,0.44],[-0.15,0.28,0.26,0.24,0,0.44]]
    # afin = [[0,0,0,0.16,0,0],[0.85,0.04,-0.04,0.85,0,1.6],[0.2,-0.26,0.23,0.22,0,0.44],[-0.15,0.28,0.26,0.24,0,0.44]]
    x = 5
    y = 5
    xx,yy= 0,0
    for i in range(100000):
        # clock.tick(1)
        ch = random.randint(0, len(afin)-1)
        # ch = 0
        a = afin[ch][0]
        b = afin[ch][1]
        c = afin[ch][2]
        d = afin[ch][3]
        e = afin[ch][4]
        f = afin[ch][5]
        xx = (a * x) + (b * y) + e
        yy = (c * x) + (d * y) + f
        x = xx
        y = yy
        line(x,y)
        pygame.display.update()
    while True:    
        clock.tick(FPS)
        for i in pygame.event.get():
            if i.type == pygame.QUIT: exit()
        pygame.display.update()

def line(x,y):
    mn = 100
    pygame.draw.line(sc, GREEN, (x*mn+300,y*mn), (x*mn+301,y*mn), 1)

main()


# Private Sub Form_Click()
#  Randomize Timer
#  x = 0
#  y = 0
#  For i = 1 To 70000
#   r = Rnd
#   Select Case r
#    Case 0 To 0.01
#     a = 0: b = 0: c = 0: d = 0.16: e = 0: f = 0
#    Case 0.01 To 0.8
#     a = 0.85: b = 0.04: c = -0.04: d = 0.85: e = 0: f = 1.6
#    Case 0.8 To 0.9
#     a = 0.2: b = -0.26: c = 0.23: d = 0.22: e = 0: f = 1.6
#    Case 0.9 To 1
#     a = -0.15: b = 0.28: c = 0.26: d = 0.24: e = 0: f = 0.44
#   End Select
#   X1 = (a * x) + (b * y) + e
#   Y1 = (c * x) + (d * y) + f
#   x = X1
#   y = Y1
#   PSet (x + 10, 11 - y), RGB(0, 100, 0)
#  Next i
# End Sub