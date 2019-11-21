import  turtle
turtle.shape("turtle")
def star(n):
    turtle.left(180)
    for i in range(n):
        turtle.forward(150)
        turtle.left(180-180/n)

star(5)
star(11)

