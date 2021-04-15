import turtle  # Спираль

turtle.shape("turtle")
for i in range(1000):
    turtle.forward(0.01 + i * 0.01)
    turtle.left(5)
