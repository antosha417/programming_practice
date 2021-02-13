import turtle

def circle():
    for i in range(180):
        turtle.forward(1)
        turtle.left(2)

turtle.shape('turtle')
for i in range(6):
    circle()
    turtle.left(60)
#по 2 градуса чтобы быстрее рисовало