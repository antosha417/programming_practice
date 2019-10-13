#13 Смайлик. Нарисуйте смайлик с помощью написанных функций рисования круга и дуги.
from math import sin, pi
import turtle
turtle.shape('turtle')
r = 60
n = 90  # количество сторон правильного многоугольника, который уже похож на окружность
def dbow(r:float,dir=1):
    '''draw a bow with turtle turning left if dir=1, and turning right if dir=-1'''
    sleng = (r * 2 * sin(pi / n))  # side length
    angle = (180 * (n - 2)) / n  # угол правильного многоугольника
    import turtle
    for i in range(n//2):
        turtle.forward(sleng)
        if dir==1:
            turtle.left(180 - angle)
        else: turtle.right(180-angle )
def dcircle(r:float,dir=1):
    '''draw circle with turtle turning left if dir=1, and turning right if dir=-1'''
    sleng = (r * 2 * sin(pi / n))  # side length
    angle = (180 * (n - 2)) / n  # угол правильного многоугольника
    import turtle
    for i in range(n):
        turtle.forward(sleng)
        if dir==1:
            turtle.left(180 - angle)
        else: turtle.right(180-angle )
'''yellow head'''
turtle.begin_fill()
dcircle(100)
turtle.color("yellow")
turtle.end_fill()
turtle.color("black")
'''blue eyes'''
turtle.up()
turtle.goto(-30,150)
turtle.down()

turtle.begin_fill()
dcircle(20)
turtle.color("blue")
turtle.end_fill()
turtle.color("black")

turtle.up()
turtle.goto(30,150)
turtle.down()

turtle.begin_fill()
dcircle(20)
turtle.color("blue")
turtle.end_fill()
turtle.color("black")
'''black nose'''
turtle.up()
turtle.goto(0,100)
turtle.down()

turtle.width(10)
turtle.right(90)
turtle.forward(30)
'''red mouth'''
turtle.up()
turtle.goto(30,50)
turtle.down()

turtle.color("red")
dbow(30,-1)

