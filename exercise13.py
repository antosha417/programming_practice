'''
Нарисуйте смайлик с помощью написанных функций рисования круга и дуги.
'''
import turtle as t


def duga(n):
    for i in range(180):
        t.forward(n)
        t.right(1)


def krug(n):
    for i in range(360):
        t.forward(n)
        t.left(1)



t.color('yellow')
t.begin_fill()
krug(3)
t.end_fill()
t.penup()
t.left(90)
t.forward(250)
t.left(90)
t.forward(70)
t.pendown()
t.color('blue')
t.begin_fill()
krug(0.3)
t.end_fill()
t.penup()
t.right(180)
t.forward(140)
t.pendown()
t.right(180)
t.begin_fill()
krug(0.3)
t.end_fill()
t.color('black')
t.width(10)
t.penup()
t.forward(70)
t.left(90)
t.forward(70)
t.pendown()
t.forward(70)
t.penup()
t.left(90)
t.forward(60)
t.pendown()
t.right(90)
t.width(10)
t.color('red')
duga(1)