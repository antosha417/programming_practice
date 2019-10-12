import turtle

def polygon(n):
    l = (15 + n * 5)
    turtle.forward(l)
    for i in range(n - 1):
        turtle.left(360 / n)
        turtle.forward(l)

turtle.shape('turtle')
for i in range(3, 13):
    angle = 90 - 180 / i
    turtle.left(180 - angle)
    polygon(i)
    turtle.right(angle)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()