import turtle
turtle.speed(10)
def dug(x):
    for i in range(40):

        turtle.forward(x)
        turtle.right(180/40)

for i in range(5):
    turtle.setheading(90)
    dug(5)
    dug(1)
    turtle.setheading(-90)