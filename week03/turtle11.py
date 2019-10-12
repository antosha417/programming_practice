import turtle  # Бабочка


def draw_circle(n):
    i = 1
    while i <= n:
        turtle.left(360 / n)
        turtle.forward(5)
        i += 1


turtle.shape('turtle')
turtle.left(90)
n = 50
for i in range(12):
    draw_circle(n)
    turtle.left(180)
    draw_circle(n)
    turtle.left(180)
    n += 10
