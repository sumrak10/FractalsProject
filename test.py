from turtle import *
from random import randint
aks = '0'
for i in range(11):
    aks1 = ''
    for i in range(len(aks)):
        if aks[i] == '1':
            aks1 += '21'
        elif aks[i] == '0':
            aks1 += '1[0]0'
        elif aks[i] == '[':
            aks1 += '['
        elif aks[i] == ']':
            aks1 += ']'
        elif aks[i] == '2':
            aks1 += '2'
    aks = aks1
hideturtle()
tracer(0)
left(90)
pu()
bk(200)
pd()
speed(10)
width(5)
a = 16
l = 10
thick = 16
stek = []
for i in range(len(aks)):
    if aks[i] == '0':
        pencolor('green')
        fd(l)
        pencolor('black')
    if aks[i] == '1':
        fd(l)
    if aks[i] == '2':
        ch = randint(0,100)
        if ch < 50:
            fd(l)
    if aks[i] == '[':
        thick = thick * 0.75
        width(thick)
        stek.append([xcor(),ycor(),heading(),thick])
        left(a+randint(-15,15))
    if aks[i] == ']':
        pu()
        st = stek.pop()
        setx(st[0])
        sety(st[1])
        setheading(st[2])
        width(st[3])
        right(a+randint(-15,15))
        pd()
done()