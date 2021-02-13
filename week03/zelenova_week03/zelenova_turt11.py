#11 Бабочка. Нарисуйте «бабочку» из окружностей. Используйте функцию, рисующую окружность.
from math import sin, pi
import turtle
turtle.shape('turtle')
r = 60
n = 90  # количество сторон правильного многоугольника, который уже похож на окружность
def dcircle(r:float,dir=1):
    '''draw a circle with turtle turning left if dir=1, and turning right if dir=-1'''
    sleng = (r * 2 * sin(pi / n))  # side length
    angle = (180 * (n - 2)) / n  # угол правильного многоугольника
    import turtle
    for i in range(n):
        turtle.forward(sleng)
        if dir==1:
            turtle.left(180 - angle)
        else: turtle.right(180-angle )
turtle.left(180-(90*(n-2))/n)
for i in range(10):
    dcircle(r)
    dcircle(r,-1)
    r+=10