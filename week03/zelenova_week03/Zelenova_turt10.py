#10 Цветок. Нарисуйте «цветок» из окружностей. Используйте функцию, рисующую окружность.
from math import sin, pi
import turtle
turtle.shape('turtle')
r = 60
n = 90  # количество сторон правильного многоугольника, который уже похож на окружность
def dcircle(r):
    '''draw circle with turtle turning left'''
    sleng = (r * 2 * sin(pi / n))  # side length
    angle = (180 * (n - 2)) / n  # угол правильного многоугольника
    import turtle
    for i in range(n):
        turtle.shape('turtle')
        turtle.forward(sleng)
        turtle.left(180 - angle)

for i in range (6):
    dcircle(r)
    dcircle(-r)
    turtle.left(45)