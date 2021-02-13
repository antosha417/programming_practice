#9 правильные многоугольники. Нарисуйте 10 вложенных правильных многоугольников.
# Используйте функцию, рисующую правильный n-угольник.

from math import sin, pi
import turtle
turtle.shape('turtle')
n=3 #число чторон многоугольника
r=50 #радиус описанной окружности первого многоугольника
sleng=(r*2*sin(pi/n)) #side length
angle=(180*(n-2))/n #угол правильного многоугольника
def nshape (n,r):
    '''draw a regular polygon'''

    for i in range (n):
        turtle.forward(sleng)
        turtle.left(180-angle)
    return (sleng)
    return (angle)

for i in range(10):
    turtle.up()
    turtle.goto(r, 0)
    turtle.down()
    turtle.left(180-(90*(n-2))/n)
    nshape(n,r)
    turtle.right(180-(90*(n-2))/n)
    n+=1
    r+=30


