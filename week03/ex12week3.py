import  turtle
turtle.shape("turtle")
def arc(n):
    for i in range(50):
        turtle.forward(n)
        turtle.right(180-180*(100-2)/100)

turtle.penup()
turtle.goto(-900, 0)
turtle.pendown()
turtle.left(90)
for u in range(5):
    arc(10)
    arc(1)


