import turtle

turtle.shape('turtle')
for i in range(3600):
    turtle.forward(0.1 + i * 0.001)
    turtle.left(2)     #по 2 градуса чтобы быстрее рисовала