def polygon(n, R):
    import turtle as t
    fi = 360 / n
    for i in range(0, n):
        t.forward(R)
        t.left(fi)
import turtle as t
n = 10
r = 10
for i in range(3, 3+n):
    t.left(180/i)
    polygon(i, r*i)
    t.right(180/i + 90)
    t.penup()
    t.forward(r)
    t.left(90)
    t.pendown()