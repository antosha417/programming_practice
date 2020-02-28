#Нарисуйте «цветок» из окружностей. Используйте функцию, рисующую окружность.

import turtle
turtle.shape('turtle')
for j in range(1, 4):
    for i in range(360):
        turtle.forward(1)
        turtle.left(1)
    turtle.left(180)
    for i in range(360):
        turtle.forward(1)
        turtle.left(1)
    turtle.left(180+60)
