import turtle

def arc(c):
    for i in range(90):
        turtle.forward(c)
        turtle.right(2)

turtle.shape('turtle')
turtle.left(90)
for i in range(5):
    arc(2)
    arc(0.5)