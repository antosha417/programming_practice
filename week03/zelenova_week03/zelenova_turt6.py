#6 Паук. Нарисуйте паука с n=12 лапами#
lpaw=90 #длина лапки паука
n=12
langle=360/n #угол между лапками
import turtle
turtle.shape('turtle')
for i in range(n):
    turtle.forward(lpaw)
    turtle.stamp()
    turtle.backward(lpaw)
    turtle.left(langle)

