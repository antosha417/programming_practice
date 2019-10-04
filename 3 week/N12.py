def duga(fi, R):
    import turtle as t
    n = 90
    turn = 360 / n
    for i in range(0, int(fi/turn)):
        t.forward(R)
        t.left(turn)

import turtle as t
n = 3
R = 300
dr = R/100
for i in range(0, n):
    duga(180, dr)
    duga(180, dr/5)