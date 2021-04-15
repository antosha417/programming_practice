import turtle  # Вложенные правильные многоугольники


def figure(n):
    ang = 180 - 180 * (n - 2) / n / 2
    angle = 180 * (n - 2) / n
    turtle.left(ang)
    for i in range(n):
        turtle.forward(30 * n)
        turtle.left(180 - angle)
    turtle.right(ang)


for n in range(3, 14):
    figure(n)
    turtle.penup()
    turtle.goto((n - 2) * 20, 0)
    turtle.pendown()
