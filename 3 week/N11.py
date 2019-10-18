def circle(R):
    n = 40
    import turtle as t
    fi = 360 / n
    for i in range(0, n):
        t.forward(R)
        t.left(fi)
import turtle as t
n = 7
R = 5
dr = 1
for i in range(0, n):
    circle(R + i*dr)
    t.left(180)
    circle(R + i*dr)
    t.left(180)