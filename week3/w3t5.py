import turtle

turtle.shape('turtle')
for i in range(1, 11):
    turtle.forward(i * 20)
    for j in range(3):
        turtle.left(90)
        turtle.forward(i * 20)
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.left(180)