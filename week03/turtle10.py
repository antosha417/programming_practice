import turtle # Цветок


def draw_circle():
    i = 1
    n = 80
    while i <= n:
        turtle.left(360 / n)
        turtle.forward(5)
        i += 1


turtle.shape("turtle")
for i in range(8):
    draw_circle()
    turtle.left(45)
