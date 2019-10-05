import  turtle
turtle.shape("turtle")
def circleL(n):
    turtle.left(n)
    for i in range(50):
        turtle.forward(5)
        turtle.left(180-180*(50-2)/50)


def circleR(n):
    turtle.left(n)
    for i in range(50):
        turtle.forward(5)
        turtle.right(180-180*(50-2)/50)

circleL(0)
circleR(0)
circleL(60)
circleR(0)
circleL(60)
circleR(0)
