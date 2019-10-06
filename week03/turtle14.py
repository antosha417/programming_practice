import turtle


def star(n):
    for i in range(n):
        turtle.forward(150)
        turtle.left(180-180/n)




star(5)
turtle.penup()
turtle.forward(300)
turtle.pendown()
star(11)
turtle.done()