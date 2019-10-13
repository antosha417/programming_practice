import turtle
turtle.shape('turtle')

k=10

for i in range (0,40,2):
    turtle.left(90)
    turtle.forward(k+i*2)
    turtle.left(90)
    turtle.forward(k+i*2)
    turtle.left(90)
    turtle.forward(k+i*2)
    turtle.left(90)
    turtle.forward(k+i*2)
    turtle.penup()
    turtle.goto(i+2,-i-2)
    turtle.pendown()