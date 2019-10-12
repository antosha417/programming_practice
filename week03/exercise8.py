'''
Нарисуйте «квадратную» спираль.
'''
import turtle as tu
tu.shape('turtle')


def halfSQ(n, end): # начальная длина стороны квадрата, конечная длина
    while n != end:
        tu.forward(n)
        tu.left(90)
        n += 10


halfSQ(n, end)