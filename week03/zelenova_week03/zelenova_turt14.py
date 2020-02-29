#14 Звезды.
# Нарисуйте две звезды: одну с 5 вершинами, другую — с 11. Используйте функцию, рисующую звезду с n вершинами.
from math import sin
import turtle
turtle.shape('turtle')
def star(r,n):
    '''рисует звезду с n вершинами и радиусом описанной окружности r'''
    angle=180/n
    len=r*sin(angle/2) #длина хорды-"стороны" звезды
    for i in range(n):
        turtle.forward(len)
        turtle.left(180-angle)
turtle.up()
turtle.goto(-150,0)
turtle.down()
star(200,5)

turtle.up()
turtle.goto(150,0)
turtle.down()
star(200,11)
