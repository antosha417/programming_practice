import turtle

turtle.goto(0, 0)
n = 10
k = 10
turtle.shape('turtle')
for i in range(9):
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.up()
    turtle.goto(-k, -k)
    turtle.down()
    k += 10
    n += 20
