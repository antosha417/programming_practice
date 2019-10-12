'''
Нарисуйте пружину. Используйте функцию, рисующую дугу.
'''
import turtle as tu
tu.shape('turtle')

n = 10
tu.penup()
tu.goto(-200,0)
tu.pendown()
while n >= 0:
    tu.right(90)
    tu.circle(10, -180)
    tu.circle(3, -180)
    tu.right(-90)
    n -= 1