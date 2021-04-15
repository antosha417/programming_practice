import turtle  # окружность

turtle.shape('turtle')
i = 1
n = 60
while i <= n:
    turtle.left(360 / n)
    turtle.forward(12)
    i += 1
