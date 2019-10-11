import turtle  # Квадратная спираль

a = 10
i = 0
step = int(input())
while i <= step:
    turtle.forward(a + 10 * i)
    turtle.left(90)
    turtle.forward(a + 10 * i)
    i += 1
