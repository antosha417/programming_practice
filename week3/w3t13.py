import turtle

def arc(c):
    for i in range(90):
        turtle.forward(c)
        turtle.right(2)

def circle(c):
    for i in range(180):
        turtle.forward(c)
        turtle.left(2)

turtle.shape('turtle')
turtle.width(5)
turtle.begin_fill()
turtle.color('yellow')
circle(3)
turtle.end_fill()
turtle.left(90)
turtle.color('black')
turtle.penup()
turtle.goto(20,100)
turtle.pendown()
turtle.width(2)
arc(0.7)
turtle.left(180)
turtle.penup()
turtle.goto(-50,100)
turtle.pendown()
arc(0.7)
turtle.penup()
turtle.goto(30,50)
turtle.pendown()
turtle.begin_fill()
arc(1)
turtle.goto(30, 50)
turtle.end_fill()
#надеюсь со смайликом можно было пофантазировать?