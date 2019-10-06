import turtle

turtle.shape('turtle')
for i in range(10):

    for k in range(4):
        turtle.forward(50+i*10)
        turtle.left(90)
    turtle.penup()
    turtle.right(135)
    turtle.forward(7.07)
    turtle.pendown()
    turtle.left(135)


turtle.done()