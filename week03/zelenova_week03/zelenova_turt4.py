#4 Окружность
n=90 #количество сторон правильного многоугольника
angle=(180*(n-2))/n #угол правильного многоугольника
import turtle
for i in range (n):
    turtle.shape('turtle')
    turtle.forward(5)
    turtle.left(180-angle)
