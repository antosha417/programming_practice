import turtle

turtle.shape('turtle')
turtle.speed(10)
def circle(x):
    for i in range(40):

        turtle.forward(4)
        turtle.left(360/40)


for k in range (1,7):
    circle(k)
    turtle.setheading(360*k / 6)

turtle.done()