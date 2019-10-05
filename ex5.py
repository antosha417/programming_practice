import  turtle
turtle.shape("turtle")
for i in range(10):
    turtle.forward(30 + 2*i*10)
    turtle.left(90)
    turtle.forward(30 + 2*i*10)
    turtle.left(90)
    turtle.forward(30 + 2*i*10)
    turtle.left(90)
    turtle.forward(30 + 2*i*10)
    turtle.left(90)
    turtle.penup()
    turtle.goto(-10-i*10,-10-i*10)
    turtle.pendown()
