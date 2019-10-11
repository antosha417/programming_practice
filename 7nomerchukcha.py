import turtle
turtle.shape('turtle')
n = 15
for i in range(1, 1000):
    a = 10
    h = (a / 360) * n
    turtle.left(n)
    turtle.forward(0.1*i + h)