import turtle

turtle.shape('turtle')


def f(n):
    for i in range(n):
        # turtle.left((n-2)/n*180)
        turtle.forward(10 + n * 10)
        turtle.left((180 - (n - 2) / n * 180))


for i in range(3, 9):
    f(i)
    turtle.penup()
    if i == 3:
        turtle.goto(-4, -10)
    else:
        turtle.goto(-4, -i * 7)
    turtle.pendown()