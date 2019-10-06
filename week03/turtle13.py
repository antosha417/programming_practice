import turtle
turtle.speed(1)
def circle(x):
    for i in range(40):

        turtle.forward(x)
        turtle.left(360/40)

def dug(x):
    for i in range(40):

        turtle.forward(x)
        turtle.right(180/40)


turtle.penup()
turtle.forward(40)
turtle.pendown()
turtle.setheading(90)
turtle.color('yellow')
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()
turtle.penup()
turtle.goto(25,10)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
turtle.circle(20)
turtle.penup()
turtle.goto(-30,10)
turtle.pendown()
turtle.circle(20)
turtle.end_fill()
turtle.penup()
turtle.goto(-23,0)
turtle.pendown()
turtle.width(5)
turtle.color('red')
turtle.left(180)
turtle.forward(30)
turtle.penup()
turtle.goto(5,-19)
turtle.pendown()
dug(2)



turtle.done()