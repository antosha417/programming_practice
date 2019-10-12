import turtle

#2 Следующая программа рисует букву S:
turtle.shape('turtle')
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

#3 Квадрат.
import turtle
turtle.shape('turtle')
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

#4 Окружность
n=90 #количество сторон правильного многоугольника
angle=(180*(n-2))/n #угол правильного многоугольника
import turtle
for i in range (n):
    turtle.shape('turtle')
    turtle.forward(5)
    turtle.left(180-angle)

#5 Больше квадратов. Нарисуйте 10 вложенных квадратов.
n=4
angle=(180*(n-2))/n
l=30 #длина стороны наименьшего квадрата
step=20 #шаг между квадратами
import turtle
for i in range(10):
    for i in range(n):
          turtle.shape('turtle')
          turtle.pendown()
          turtle.forward(l)
          turtle.left(180 - angle)
    turtle.penup()
    turtle.left(180)
    turtle.forward(step)
    turtle.left(90)
    turtle.forward(step)
    turtle.left(90)
    l+=2*(step)

#6 Паук. Нарисуйте паука с n=12 лапами
lpaw=90 #длинна лапки паука
n=12
langle=360/n #угол между лапками
import turtle
turtle.shape('turtle')
for i in range(n):
    turtle.forward(lpaw)
    turtle.stamp()
    turtle.backward(lpaw)
    turtle.left(langle)

#7 Спираль
k=1 #cмещение точки по лучу
rfi=0.1 #угол поворота в радианах
dfi=rfi*180/3.14 #угол поворота в градусах
import turtle
turtle.shape('turtle')
for i in range (100):
    ro=k*rfi #приращение спирали
    turtle.forward(ro)
    turtle.left(dfi)
    rfi+=0.1
    ro+=ro

#8 Квадратная спираль
import.turtle
step=10 #сторона меньшего квадрата
n=100 #количество граней квадратов,пройденных черепашкой в спирале
turtle.shape('turtle')
for i in range(n):
     turtle.forward(step)
     turtle.left(90)
     step+=5

