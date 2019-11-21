import  turtle
turtle.shape("turtle")
def circleL(n):
    turtle.right(0)
    for i in range(50):
        turtle.left(180 - 180 * (50 - 2) / 50)
        turtle.forward(n)

def circleR(n):
    turtle.left(0)
    for i in range(50):
        turtle.forward(n)
        turtle.right(180-180*(50-2)/50)

turtle.left(90)
for i in range(6):
    circleL(5 + i)
    circleR(5 + i)