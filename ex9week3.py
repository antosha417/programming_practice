import  turtle
turtle.shape('turtle')
def  geom(n):
    turtle.left(180 - 180 * (n - 2) / n / 2)
    for i in range(n):
        turtle.forward(20*n)
        turtle.left(180-180*(n-2)/n)
    turtle.right(180 - 180 * (n - 2) / n / 2)


for i in range(3, 13):
    geom(i)
    turtle.penup()
    turtle.goto((i-2)*33, 0)
    turtle.pendown()






