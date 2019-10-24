import turtle
turtle.shape('circle')
def crc(n):
    turtle.left(n)
    for i in range(50):
        turtle.forward(10)
        turtle.left(180-180*(50-2)/50)

def crl(n):
    turtle.left(n)
    for i in range(50):
        turtle.forward(10)
        turtle.right(180-180*(50-2)/50)
crl(0)
crc(0)
crl(60)
crc(0)
crl(60)
crc(0)
