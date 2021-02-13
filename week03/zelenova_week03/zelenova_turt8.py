#8 Квадратная спираль
import turtle
step=10 #сторона наименьшего квадрата
n=100 #количество граней квадратов,пройденных черепашкой в спирале
turtle.shape('turtle')
for i in range(n):
     turtle.forward(step)
     turtle.left(90)
     step+=5