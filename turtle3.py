import turtle as t
n = 10
k = 4
side = 10
while n > 0:
    while k > 0:
        t.forward(side)
        t.left(90)
        k -= 1
    k = 4
    t.penup()
    t.right(90)
    t.forward(4)
    t.right(90)
    t.forward(4)
    t.right(180)
    t.pendown()
    side += 8
    n -= 1



