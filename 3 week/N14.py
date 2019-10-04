def star(n, R):
    import turtle as t
    for i in range(0, n):
        t.forward(R)
        t.left(180-180/n)

import turtle as t
R = 100
star(5, R)
t.penup()
t.forward(2*R)
t.pendown()
star(11, R)