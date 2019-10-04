import turtle
turtle.shape('circle')
def crc(n):
    turtle.left(0)
    for i in range(50):
        turtle.forward(n)
        turtle.left(180-180*(50-2)/50)


def crl(n):
    turtle.left(0)
    for i in range(50):
        turtle.forward(n)
        turtle.right(180-180*(50-2)/50)

turtle.left(90)
for i in range(6):
    crc(5 + i)
    crl(5 + i)