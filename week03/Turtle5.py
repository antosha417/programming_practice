import turtle
turtle.shape('arrow')
width=10
num=10
a=10
for i in range(num):
    for j in range(4):
        turtle.forward(a)
        turtle.left(90)
    turtle.penup()
    turtle.right(135)
    turtle.forward(width*(2**0.5))
    turtle.left(135)
    turtle.pendown()
    a+=width*2