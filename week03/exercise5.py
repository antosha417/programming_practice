'''
Нарисуйте 10 вложенных квадратов.
'''
import turtle as tu
tu.shape('turtle')

def square(x, n):
    while n != 0:
        tu.forward(x)
        tu.left(90)
        n-=1

n = 4
x = 50
f = 11
ch1 = -5
while f != 0:
    square(x, n)
    tu.penup()
    tu.goto (ch1, ch1)
    tu.pendown()
    x += 10
    f -= 1
    ch1 -= 5
