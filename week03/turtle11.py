import turtle
turtle.setheading(90)
turtle.shape('turtle')
turtle.speed(10)
def circle(x):
    for i in range(40):

        turtle.forward(4+x)
        turtle.left(360/40)


for k in range (1,7):
    circle(k)
    turtle.setheading(-90)
    circle(k)
    turtle.setheading(90)

turtle.done()