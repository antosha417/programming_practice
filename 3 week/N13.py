def duga(fi, R):
    import turtle as t
    dr = R/100
    n = 90
    turn = 360 / n
    for i in range(0, int(fi/turn)):
        t.forward(dr)
        t.left(turn)

def cvet_krug(R, cvet):
    import turtle as t
    dr = R/100
    t.begin_fill()
    duga(360, R)
    t.color(cvet)
    t.end_fill()

import turtle as t
import time
r = 100
R = 5*r
cvet_krug(R, 'yellow')
t.penup()
t.left(90)
t.forward(r)
t.left(90)
t.forward(r/4)
cvet_krug(r, 'blue')

t.left(180)
t.forward(r/2)
t.left(180)
cvet_krug(r, 'blue')

t.forward(r/4)
t.left(90)
t.forward(r/4)
t.pendown()
t.color('black')
t.width(r/10)
t.forward(r/4)
t.penup()

t.right(90)
t.forward(r/4)
t.left(90)
t.pendown()
t.color('red')
duga(180, 2*r)

time.sleep(2)