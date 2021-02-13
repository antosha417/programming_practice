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
