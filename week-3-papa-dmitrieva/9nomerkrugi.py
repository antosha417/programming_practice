import turtle
turtle.shape('circle')
def mng(n):
    turtle.left(180 - 180*(n - 2)/ n/2)
    for i in range(n):
        turtle.forward(10*n)
        turtle.left(180 - 180*(n - 2)/ n)
    turtle.right(180 - 180*(n - 2)/ n/2)

for i in range(3, 12):
    mng(i)
    turtle.penup()
    turtle.goto(i*3, 0)
    turtle.pendown()