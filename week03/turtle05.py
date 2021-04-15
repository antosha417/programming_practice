import turtle  # Вложенные кавдраты

a = 10
i = 10
for _ in range(10):
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.penup()
    turtle.goto(-i, -i)
    turtle.pendown()
    turtle.left(90)
    i += 10
    a += 20
