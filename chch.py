import turtle
turtle.shape('turtle')
for i in range(10):
    turtle.forward(15 + i*10)
    turtle.left(90)
    turtle.forward(15 + i*10)
    turtle.left(90)
    turtle.forward(15 + i*10)
    turtle.left(90)
    turtle.forward(15 + i*10)
    turtle.left(90)
    turtle.penup()
    turtle.goto(-5 - i*5, -5 - i*5)
    turtle.pendown()