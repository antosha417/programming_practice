import turtle
turtle.shape('turtle')
for i in range(10):
    turtle.forward(10+20*i)
    turtle.left(90)
    turtle.forward(10+20*i)
    turtle.left(90)
    turtle.forward(10+20*i)
    turtle.left(90)
    turtle.forward(10+20*i)
    turtle.penup()
    turtle.goto(-10-10*i,-10-10*i)
    turtle.pendown()
    turtle.left(90)