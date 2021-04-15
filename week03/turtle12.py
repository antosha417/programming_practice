import turtle


def draw_arc(n):
    for i in range(60):
        turtle.forward(n)
        turtle.right(3)


turtle.shape("turtle")
turtle.penup()
turtle.goto(-250, 0)
turtle.pendown()
turtle.left(90)
for _ in range(4):
    draw_arc(3)
    draw_arc(1)
